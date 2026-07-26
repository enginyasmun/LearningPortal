"""Rerunnable migration: Expedition design release and refreshed AI-engineering curriculum."""
from datetime import datetime, timezone
from pathlib import Path
import os
import shutil
import sqlite3

from curriculum_data import PROGRAM_WEEKS, PROJECT_MILESTONES

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = Path(os.environ.get("DATABASE_PATH", BASE_DIR / "academy.db"))

if not DB_PATH.exists():
    raise SystemExit(f"Database not found: {DB_PATH}")

stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
backup = DB_PATH.with_name(f"{DB_PATH.stem}_backup_before_v18_{stamp}{DB_PATH.suffix}")
shutil.copy2(DB_PATH, backup)

with sqlite3.connect(DB_PATH) as conn:
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")

    for week_number, stage, title, topics, research_topic, linkedin_topic in PROGRAM_WEEKS:
        conn.execute(
            """
            UPDATE weeks
            SET stage=?, title=?, topics=?, research_topic=?, linkedin_topic=?
            WHERE week_number=?
            """,
            (stage, title, topics, research_topic, linkedin_topic, week_number),
        )

    project_ids = {
        row["project_number"]: row["id"]
        for row in conn.execute("SELECT id, project_number FROM projects")
    }
    for project_number, milestones in PROJECT_MILESTONES.items():
        project_id = project_ids.get(project_number)
        if not project_id:
            continue
        for milestone in milestones:
            conn.execute(
                """
                UPDATE project_milestones
                SET title=?, instructions=?, deliverable=?, is_final=?
                WHERE project_id=? AND week_number=?
                """,
                (
                    milestone["title"],
                    milestone["instructions"],
                    milestone["deliverable"],
                    milestone["is_final"],
                    project_id,
                    milestone["week_number"],
                ),
            )

    week_ids = {
        row["week_number"]: row["id"]
        for row in conn.execute("SELECT id, week_number FROM weeks")
    }
    week_info = {week[0]: week for week in PROGRAM_WEEKS}

    for week_number in range(1, 17):
        week_id = week_ids[week_number]
        _, _, _, _, research_topic, linkedin_topic = week_info[week_number]

        if week_number < 16:
            category = "Hands-On"
            key = f"v18:w{week_number:02d}:build"
            max_score = 100
            if week_number == 1:
                title = "Week 1 Git Foundations Portfolio"
                instructions = "Complete the individual Git foundations lab before classroom project development."
                deliverable = "Personal Git practice repository, commit history, branch and merge evidence, safe undo evidence, and GitHub URL."
            elif week_number == 2:
                title = "Week 2 Classroom GitHub Workflow"
                instructions = "Complete the classroom Salesforce DX branch, pull-request, review, conflict-resolution, and synchronization lab."
                deliverable = "Pull-request URL, review link, conflict-resolution evidence, and clean synchronized main branch."
            elif week_number == 14:
                title = "Week 14 Claude AI and Salesforce CLI Workflow"
                instructions = "Complete the controlled Claude Code and deterministic Salesforce CLI development lab."
                deliverable = "CLAUDE.md instructions, bounded task, plan-mode evidence, reviewed AI diff, CLI tests, Code Analyzer, deployment validation, AI-use disclosure, and pull-request evidence."
            elif week_number == 15:
                title = "Week 15 MCP and Secure Agent Tooling Workflow"
                instructions = "Complete the governed Claude MCP connection, least-privilege tool workflow, and security review."
                deliverable = "MCP architecture, redacted configuration, tool inventory and permissions, read-only and controlled-action evidence, denied-action test, audit logs, skill file, and pull request."
            else:
                title = f"Week {week_number} Guided Build Lab"
                instructions = f"Complete Week {week_number} of the project assigned to your classroom."
                deliverable = "The classroom project milestone defines the required deliverable."
        else:
            category = "Capstone"
            key = "v18:w16:capstone"
            max_score = 150
            title = "Week 16 Governed Agentforce Final Application"
            instructions = "Complete, deploy, govern, document, and demonstrate the application shared by your classroom."
            deliverable = "A production-style application, source repository, architecture documentation, tests, Agentforce Testing Center evidence, AI governance evidence, agent guardrails, release validation, and final classroom demonstration."

        conn.execute(
            """
            UPDATE assignments
            SET assignment_key=?, program_version='v18', title=?, instructions=?, deliverable=?, max_score=?
            WHERE week_id=? AND category=? AND is_published=1
            """,
            (key, title, instructions, deliverable, max_score, week_id, category),
        )
        conn.execute(
            """
            UPDATE assignments
            SET assignment_key=?, program_version='v18', title=?, instructions=?, deliverable=?
            WHERE week_id=? AND category='Research' AND is_published=1
            """,
            (
                f"v18:w{week_number:02d}:research",
                f"Week {week_number} Research: {research_topic}",
                research_topic,
                "500 to 1,000 words, at least three credible sources including one official source, one practical example, and a conclusion connected to the classroom workflow or project.",
                week_id,
            ),
        )
        conn.execute(
            """
            UPDATE assignments
            SET assignment_key=?, program_version='v18', title=?, instructions=?, deliverable=?
            WHERE week_id=? AND category='LinkedIn' AND is_published=1
            """,
            (
                f"v18:w{week_number:02d}:linkedin",
                f"Week {week_number} LinkedIn: {linkedin_topic}",
                linkedin_topic,
                "Submit an instructor-reviewed draft first. After approval, publish it and add the LinkedIn post URL.",
                week_id,
            ),
        )

    conn.commit()

with sqlite3.connect(DB_PATH) as conn:
    print(f"Migration completed: {DB_PATH}")
    print(f"Backup created: {backup}")
    print("Version 18: Expedition design and refreshed AI-engineering curriculum")
    print("Week 2 now includes GitHub Actions continuous-integration basics")
    print("Week 10 now includes AI-assisted code review with human verification")
    print("Weeks 14-16 refreshed: CLAUDE.md, plan mode, agent skills, MCP OAuth and tool permissions, Agentforce Testing Center")
    print("Active assignments:", conn.execute("SELECT COUNT(*) FROM assignments WHERE is_published=1").fetchone()[0])
    print("Project milestones:", conn.execute("SELECT COUNT(*) FROM project_milestones").fetchone()[0])
