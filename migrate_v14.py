"""Rerunnable migration to classroom ownership and live integration project data."""

from datetime import datetime, timezone
from pathlib import Path
import os
import shutil
import sqlite3

from curriculum_data import PROJECTS, PROJECT_MILESTONES

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = Path(os.environ.get("DATABASE_PATH", BASE_DIR / "academy.db"))


def table_exists(conn, name):
    return conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (name,)
    ).fetchone() is not None


def columns(conn, table):
    return {row[1] for row in conn.execute(f"PRAGMA table_info({table})")}


def add_column(conn, table, definition):
    name = definition.split()[0]
    if name not in columns(conn, table):
        conn.execute(f"ALTER TABLE {table} ADD COLUMN {definition}")


if not DB_PATH.exists():
    raise SystemExit(f"Database not found: {DB_PATH}")

stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
backup = DB_PATH.with_name(f"{DB_PATH.stem}_backup_before_v14_{stamp}{DB_PATH.suffix}")
shutil.copy2(DB_PATH, backup)

with sqlite3.connect(DB_PATH) as conn:
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = OFF")

    if not table_exists(conn, "users") or not table_exists(conn, "projects"):
        raise RuntimeError("The existing LearningPortal database schema was not found.")

    add_column(conn, "users", "avatar_filename TEXT")
    add_column(conn, "users", "classroom_id INTEGER")

    project_columns = [
        "integration_name TEXT NOT NULL DEFAULT ''",
        "integration_base_url TEXT NOT NULL DEFAULT ''",
        "integration_docs_url TEXT NOT NULL DEFAULT ''",
        "integration_auth TEXT NOT NULL DEFAULT ''",
        "integration_operation TEXT NOT NULL DEFAULT ''",
        "integration_path TEXT NOT NULL DEFAULT ''",
    ]
    for definition in project_columns:
        add_column(conn, "projects", definition)

    if not table_exists(conn, "classrooms"):
        conn.execute(
            """
            CREATE TABLE classrooms (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                instructor_id INTEGER NOT NULL,
                project_id INTEGER NOT NULL,
                description TEXT,
                is_active INTEGER NOT NULL DEFAULT 1,
                created_at TEXT NOT NULL,
                FOREIGN KEY (instructor_id) REFERENCES users(id),
                FOREIGN KEY (project_id) REFERENCES projects(id),
                UNIQUE(name, instructor_id)
            )
            """
        )
    conn.execute("CREATE INDEX IF NOT EXISTS idx_users_classroom ON users(classroom_id)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_classrooms_instructor ON classrooms(instructor_id)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_classrooms_project ON classrooms(project_id)")

    project_ids = {}
    for project in PROJECTS:
        existing = conn.execute(
            "SELECT id FROM projects WHERE project_number=?", (project["number"],)
        ).fetchone()
        values = (
            project["industry"], project["title"], project["summary"],
            project["entities"], project["personas"], project["process"],
            project["integration"], project["integration_name"],
            project["integration_base_url"], project["integration_docs_url"],
            project["integration_auth"], project["integration_operation"],
            project["integration_path"], project["workspace"], project["agent"],
            project["accent"], project["number"],
        )
        if existing:
            conn.execute(
                """
                UPDATE projects SET industry=?,title=?,summary=?,entities=?,personas=?,
                    process=?,integration=?,integration_name=?,integration_base_url=?,
                    integration_docs_url=?,integration_auth=?,integration_operation=?,
                    integration_path=?,workspace=?,agent=?,accent=?
                WHERE project_number=?
                """,
                values,
            )
            project_ids[project["number"]] = existing["id"]
        else:
            project_ids[project["number"]] = conn.execute(
                """
                INSERT INTO projects
                (industry,title,summary,entities,personas,process,integration,
                 integration_name,integration_base_url,integration_docs_url,
                 integration_auth,integration_operation,integration_path,
                 workspace,agent,accent,project_number)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                values,
            ).lastrowid

    if not table_exists(conn, "project_milestones"):
        conn.execute(
            """
            CREATE TABLE project_milestones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                project_id INTEGER NOT NULL,
                week_number INTEGER NOT NULL,
                title TEXT NOT NULL,
                instructions TEXT NOT NULL,
                deliverable TEXT NOT NULL,
                is_final INTEGER NOT NULL DEFAULT 0,
                UNIQUE(project_id, week_number)
            )
            """
        )

    for project in PROJECTS:
        project_id = project_ids[project["number"]]
        for milestone in PROJECT_MILESTONES[project["number"]]:
            row = conn.execute(
                "SELECT id FROM project_milestones WHERE project_id=? AND week_number=?",
                (project_id, milestone["week_number"]),
            ).fetchone()
            values = (
                milestone["title"], milestone["instructions"],
                milestone["deliverable"], milestone["is_final"],
                project_id, milestone["week_number"],
            )
            if row:
                conn.execute(
                    """
                    UPDATE project_milestones
                    SET title=?,instructions=?,deliverable=?,is_final=?
                    WHERE project_id=? AND week_number=?
                    """,
                    values,
                )
            else:
                conn.execute(
                    """
                    INSERT INTO project_milestones
                    (title,instructions,deliverable,is_final,project_id,week_number)
                    VALUES (?,?,?,?,?,?)
                    """,
                    values,
                )

    admin = conn.execute(
        """
        SELECT id FROM users
        WHERE role='instructor' AND is_active=1
        ORDER BY is_admin DESC,id
        LIMIT 1
        """
    ).fetchone()
    if not admin:
        raise RuntimeError("At least one active instructor is required.")
    first_project_id = project_ids[min(project_ids)]
    user_cols = columns(conn, "users")

    students = conn.execute(
        "SELECT * FROM users WHERE role='student' ORDER BY id"
    ).fetchall()
    classroom_cache = {}
    sequence = 1
    for student in students:
        if student["classroom_id"]:
            continue
        instructor_id = student["assigned_instructor_id"] if "assigned_instructor_id" in user_cols else None
        if not instructor_id or not conn.execute(
            "SELECT 1 FROM users WHERE id=? AND role='instructor'", (instructor_id,)
        ).fetchone():
            instructor_id = admin["id"]
        project_id = student["selected_project_id"] if "selected_project_id" in user_cols else None
        if not project_id or not conn.execute(
            "SELECT 1 FROM projects WHERE id=?", (project_id,)
        ).fetchone():
            project_id = first_project_id
        class_name = ""
        if "cohort" in user_cols and student["cohort"]:
            class_name = str(student["cohort"]).strip().replace("Cohort ", "Classroom ")
        if not class_name:
            class_name = f"Classroom {sequence}"
        key = (class_name.lower(), instructor_id, project_id)
        classroom_id = classroom_cache.get(key)
        if not classroom_id:
            existing = conn.execute(
                "SELECT id,project_id FROM classrooms WHERE lower(name)=? AND instructor_id=?",
                (class_name.lower(), instructor_id),
            ).fetchone()
            if existing and existing["project_id"] == project_id:
                classroom_id = existing["id"]
            else:
                classroom_name = class_name
                if existing and existing["project_id"] != project_id:
                    project_label = conn.execute(
                        "SELECT industry FROM projects WHERE id=?", (project_id,)
                    ).fetchone()["industry"]
                    classroom_name = f"{class_name} · {project_label}"
                classroom_id = conn.execute(
                    """
                    INSERT INTO classrooms
                    (name,instructor_id,project_id,description,is_active,created_at)
                    VALUES (?,?,?,?,1,?)
                    """,
                    (
                        classroom_name, instructor_id, project_id,
                        "Migrated classroom. Review the instructor and shared project.",
                        datetime.now(timezone.utc).isoformat(timespec="seconds"),
                    ),
                ).lastrowid
            classroom_cache[key] = classroom_id
            sequence += 1
        conn.execute("UPDATE users SET classroom_id=? WHERE id=?", (classroom_id, student["id"]))

    if table_exists(conn, "assignments"):
        assignment_cols = columns(conn, "assignments")
        if "program_version" in assignment_cols:
            conn.execute("UPDATE assignments SET program_version='v14' WHERE is_published=1")
        conn.execute(
            """
            UPDATE assignments
            SET title='Week ' || (SELECT week_number FROM weeks WHERE id=assignments.week_id) || ' Classroom Project Build'
            WHERE category='Hands-On' AND is_published=1
            """
        )
        conn.execute(
            """
            UPDATE assignments
            SET title='Week 16 Final Classroom Application'
            WHERE category='Capstone' AND is_published=1
            """
        )

    conn.commit()
    conn.execute("PRAGMA foreign_keys = ON")

with sqlite3.connect(DB_PATH) as conn:
    classroom_count = conn.execute("SELECT COUNT(*) FROM classrooms").fetchone()[0]
    student_count = conn.execute("SELECT COUNT(*) FROM users WHERE role='student'").fetchone()[0]
    assigned_count = conn.execute(
        "SELECT COUNT(*) FROM users WHERE role='student' AND classroom_id IS NOT NULL"
    ).fetchone()[0]
    project_count = conn.execute("SELECT COUNT(*) FROM projects").fetchone()[0]
    milestone_count = conn.execute("SELECT COUNT(*) FROM project_milestones").fetchone()[0]

print(f"Migration completed: {DB_PATH}")
print(f"Backup created: {backup}")
print(f"Classrooms: {classroom_count}")
print(f"Students assigned to classrooms: {assigned_count} of {student_count}")
print(f"Project choices: {project_count}")
print(f"Guided project milestones: {milestone_count}")
print("Project 1 is now Warehouse Management & Logistics.")
print("Week 11 now requires a real Salesforce callout; mocks remain in tests only.")
