from datetime import datetime, date, timedelta, timezone
import sqlite3
import os
import hashlib
import secrets
from pathlib import Path

from curriculum_data import PROGRAM_WEEKS, PROJECTS, PROJECT_MILESTONES

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = Path(os.environ.get("DATABASE_PATH", BASE_DIR / "academy.db"))
DB_PATH.parent.mkdir(parents=True, exist_ok=True)
PASSWORD_ITERATIONS = 260_000


def generate_password_hash(password):
    salt = secrets.token_hex(16)
    digest = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt.encode("utf-8"), PASSWORD_ITERATIONS
    ).hex()
    return f"pbkdf2_sha256${PASSWORD_ITERATIONS}${salt}${digest}"


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


with get_db() as conn:
    existing = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='users'"
    ).fetchone()
    if existing and os.environ.get("RESET_DB") != "1":
        user_count = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
        if user_count > 0:
            print(f"Existing database retained at {DB_PATH}")
            raise SystemExit(0)

    conn.executescript((BASE_DIR / "schema.sql").read_text(encoding="utf-8"))
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")

    admin_email = os.environ.get("ADMIN_EMAIL", "admin@example.com")
    admin_password = os.environ.get("ADMIN_PASSWORD", "Admin123!")
    admin_id = conn.execute(
        """
        INSERT INTO users
        (name,email,avatar_filename,password_hash,role,classroom_id,is_admin,is_active,created_at)
        VALUES (?,?,NULL,?,'instructor',NULL,1,1,?)
        """,
        (
            os.environ.get("ADMIN_NAME", "Academy Instructor"),
            admin_email,
            generate_password_hash(admin_password),
            now,
        ),
    ).lastrowid

    project_ids = {}
    for project in PROJECTS:
        project_ids[project["number"]] = conn.execute(
            """
            INSERT INTO projects
            (project_number,industry,title,summary,entities,personas,process,integration,
             integration_name,integration_base_url,integration_docs_url,integration_auth,
             integration_operation,integration_path,workspace,agent,accent)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                project["number"], project["industry"], project["title"], project["summary"],
                project["entities"], project["personas"], project["process"], project["integration"],
                project["integration_name"], project["integration_base_url"], project["integration_docs_url"],
                project["integration_auth"], project["integration_operation"], project["integration_path"],
                project["workspace"], project["agent"], project["accent"],
            ),
        ).lastrowid

    classroom_id = conn.execute(
        """
        INSERT INTO classrooms(name,instructor_id,project_id,description,is_active,created_at)
        VALUES (?,?,?,?,1,?)
        """,
        (
            os.environ.get("DEMO_CLASSROOM_NAME", "Classroom 1"),
            admin_id,
            project_ids[int(os.environ.get("DEMO_CLASSROOM_PROJECT", "1"))],
            "Demo classroom. One instructor, multiple students, one shared project.",
            now,
        ),
    ).lastrowid

    conn.execute(
        """
        INSERT INTO users
        (name,email,avatar_filename,password_hash,role,classroom_id,is_admin,is_active,created_at)
        VALUES (?,?,NULL,?,'student',?,0,1,?)
        """,
        (
            os.environ.get("DEMO_STUDENT_NAME", "Demo Student"),
            os.environ.get("DEMO_STUDENT_EMAIL", "student@example.com"),
            generate_password_hash(os.environ.get("DEMO_STUDENT_PASSWORD", "Student123!")),
            classroom_id,
            now,
        ),
    )

    for project in PROJECTS:
        project_id = project_ids[project["number"]]
        for milestone in PROJECT_MILESTONES[project["number"]]:
            conn.execute(
                """
                INSERT INTO project_milestones
                (project_id,week_number,title,instructions,deliverable,is_final)
                VALUES (?,?,?,?,?,?)
                """,
                (
                    project_id, milestone["week_number"], milestone["title"],
                    milestone["instructions"], milestone["deliverable"], milestone["is_final"],
                ),
            )

    start = date.today()
    for item in PROGRAM_WEEKS:
        week_number, stage, title, topics, research_topic, linkedin_topic = item
        week_id = conn.execute(
            """
            INSERT INTO weeks
            (week_number,stage,title,topics,research_topic,linkedin_topic)
            VALUES (?,?,?,?,?,?)
            """,
            item,
        ).lastrowid
        due = (start + timedelta(days=week_number * 7)).isoformat()

        if week_number < 16:
            category = "Hands-On"
            build_key = f"v14:w{week_number:02d}:build"
            build_title = f"Week {week_number} Classroom Project Build"
            max_score = 100
            build_instructions = (
                f"Complete Week {week_number} of the project assigned to your classroom."
            )
            build_deliverable = "The classroom project milestone defines the required deliverable."
        else:
            category = "Capstone"
            build_key = "v14:w16:capstone"
            build_title = "Week 16 Final Classroom Application"
            max_score = 150
            build_instructions = (
                "Complete, deploy, document, and demonstrate the application shared by your classroom."
            )
            build_deliverable = (
                "A production-style application, source repository, architecture documentation, tests, "
                "release evidence, agent guardrails, and final classroom demonstration."
            )

        specs = [
            (build_key, build_title, category, build_instructions, build_deliverable, max_score),
            (
                f"v14:w{week_number:02d}:research",
                f"Week {week_number} Research: {research_topic}",
                "Research",
                research_topic,
                "500 to 1,000 words, at least three credible sources including one official Salesforce source, "
                "one practical example, and a conclusion connected to the classroom project.",
                100,
            ),
            (
                f"v14:w{week_number:02d}:linkedin",
                f"Week {week_number} LinkedIn: {linkedin_topic}",
                "LinkedIn",
                linkedin_topic,
                "Submit an instructor-reviewed draft first. After approval, publish it and add the LinkedIn post URL.",
                100,
            ),
        ]
        for key, assignment_title, assignment_category, instructions, deliverable, score in specs:
            conn.execute(
                """
                INSERT INTO assignments
                (week_id,assignment_key,program_version,title,category,instructions,
                 deliverable,max_score,due_date,is_published)
                VALUES (?,?,'v14',?,?,?,?,?,?,1)
                """,
                (
                    week_id, key, assignment_title, assignment_category, instructions,
                    deliverable, score, due,
                ),
            )


    conn.commit()

print(f"Database initialized at {DB_PATH}")
print(f"Instructor email: {admin_email}")
print("Program model: classrooms, one instructor, many students, one shared project.")
print("Program: 16 weeks, 5 classroom project choices, 48 assignments per student.")
