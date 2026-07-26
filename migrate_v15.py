"""Rerunnable migration: make Git and GitHub the first two academy weeks."""
from datetime import datetime, timezone
from pathlib import Path
import os, shutil, sqlite3
from curriculum_data import PROGRAM_WEEKS, PROJECTS, PROJECT_MILESTONES

BASE_DIR=Path(__file__).resolve().parent
DB_PATH=Path(os.environ.get("DATABASE_PATH", BASE_DIR/"academy.db"))
if not DB_PATH.exists(): raise SystemExit(f"Database not found: {DB_PATH}")
stamp=datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
backup=DB_PATH.with_name(f"{DB_PATH.stem}_backup_before_v15_{stamp}{DB_PATH.suffix}")
shutil.copy2(DB_PATH,backup)

with sqlite3.connect(DB_PATH) as conn:
    conn.row_factory=sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    for week_number,stage,title,topics,research_topic,linkedin_topic in PROGRAM_WEEKS:
        conn.execute("""UPDATE weeks SET stage=?,title=?,topics=?,research_topic=?,linkedin_topic=? WHERE week_number=?""",
                     (stage,title,topics,research_topic,linkedin_topic,week_number))
    project_ids={r['project_number']:r['id'] for r in conn.execute("SELECT id,project_number FROM projects")}
    for project_number,milestones in PROJECT_MILESTONES.items():
        pid=project_ids[project_number]
        for m in milestones:
            conn.execute("""UPDATE project_milestones SET title=?,instructions=?,deliverable=?,is_final=? WHERE project_id=? AND week_number=?""",
                         (m['title'],m['instructions'],m['deliverable'],m['is_final'],pid,m['week_number']))
    week_ids={r['week_number']:r['id'] for r in conn.execute("SELECT id,week_number FROM weeks")}
    week_info={w[0]:w for w in PROGRAM_WEEKS}
    for week_number in range(1,17):
        wid=week_ids[week_number]; _,_,_,_,research_topic,linkedin_topic=week_info[week_number]
        if week_number < 16:
            category='Hands-On'; key=f'v15:w{week_number:02d}:build'; score=100
            if week_number==1:
                title='Week 1 Git Foundations Portfolio'; instructions='Complete the individual Git foundations lab before accessing classroom project development.'; deliverable='Personal Git practice repository, commit history, branch and merge evidence, safe undo evidence, and GitHub URL.'
            elif week_number==2:
                title='Week 2 Classroom GitHub Workflow'; instructions='Complete the classroom Salesforce DX branch, pull-request, review, conflict-resolution, and synchronization lab.'; deliverable='Pull-request URL, review link, conflict-resolution evidence, and clean synchronized main branch.'
            else:
                title=f'Week {week_number} Guided Build Lab'; instructions=f'Complete Week {week_number} of the project assigned to your classroom.'; deliverable='The classroom project milestone defines the required deliverable.'
        else:
            category='Capstone'; key='v15:w16:capstone'; score=150; title='Week 16 Final Classroom Application'; instructions='Complete, deploy, document, and demonstrate the application shared by your classroom.'; deliverable='A production-style application, source repository, architecture documentation, tests, release evidence, agent guardrails, and final classroom demonstration.'
        conn.execute("""UPDATE assignments SET assignment_key=?,program_version='v15',title=?,instructions=?,deliverable=?,max_score=? WHERE week_id=? AND category=? AND is_published=1""",
                     (key,title,instructions,deliverable,score,wid,category))
        conn.execute("""UPDATE assignments SET assignment_key=?,program_version='v15',title=?,instructions=?,deliverable=? WHERE week_id=? AND category='Research' AND is_published=1""",
                     (f'v15:w{week_number:02d}:research',f'Week {week_number} Research: {research_topic}',research_topic,'500 to 1,000 words, at least three credible sources including one official source, one practical example, and a conclusion connected to the classroom workflow or project.',wid))
        conn.execute("""UPDATE assignments SET assignment_key=?,program_version='v15',title=?,instructions=?,deliverable=? WHERE week_id=? AND category='LinkedIn' AND is_published=1""",
                     (f'v15:w{week_number:02d}:linkedin',f'Week {week_number} LinkedIn: {linkedin_topic}',linkedin_topic,'Submit an instructor-reviewed draft first. After approval, publish it and add the LinkedIn post URL.',wid))
    conn.commit()

with sqlite3.connect(DB_PATH) as conn:
    print(f"Migration completed: {DB_PATH}")
    print(f"Backup created: {backup}")
    print("Week 1: Git and GitHub Foundations")
    print("Week 2: Collaborative GitHub Workflow in VS Code and Salesforce DX")
    print("Industry project development begins in Week 3")
    print("Active assignments:",conn.execute("SELECT COUNT(*) FROM assignments WHERE is_published=1").fetchone()[0])
    print("Project milestones:",conn.execute("SELECT COUNT(*) FROM project_milestones").fetchone()[0])
