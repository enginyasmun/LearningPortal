import os
import sqlite3
from functools import wraps
from datetime import datetime, date, timezone
from pathlib import Path

from flask import (
    Flask, render_template, request, redirect, url_for,
    session, flash, abort, send_from_directory
)
import hashlib
import secrets
from werkzeug.utils import secure_filename

from guided_labs import build_guided_lab

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = Path(os.environ.get("DATABASE_PATH", BASE_DIR / "academy.db"))
UPLOAD_DIR = Path(os.environ.get("UPLOAD_DIR", BASE_DIR / "uploads"))
AVATAR_DIR = Path(os.environ.get("AVATAR_DIR", BASE_DIR / "avatars"))
DB_PATH.parent.mkdir(parents=True, exist_ok=True)
ALLOWED_EXTENSIONS = {"pdf", "doc", "docx", "txt", "md", "png", "jpg", "jpeg", "zip"}
AVATAR_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}
AVATAR_PRESETS = [
    {"filename": f"realistic-male-{index:02d}.png", "label": f"Male portrait {index}", "group": "Male"}
    for index in range(1, 6)
] + [
    {"filename": f"realistic-female-{index:02d}.png", "label": f"Female portrait {index}", "group": "Female"}
    for index in range(1, 6)
]
LEGACY_AVATAR_PRESET_FILES = {
    *(f"avatar-male-{index:02d}.svg" for index in range(1, 6)),
    *(f"avatar-female-{index:02d}.svg" for index in range(1, 6)),
}
AVATAR_PRESET_FILES = {item["filename"] for item in AVATAR_PRESETS} | LEGACY_AVATAR_PRESET_FILES

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "change-this-secret-in-production")
app.config["MAX_CONTENT_LENGTH"] = 12 * 1024 * 1024
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
AVATAR_DIR.mkdir(parents=True, exist_ok=True)
PASSWORD_ITERATIONS = 260_000


def generate_password_hash(password):
    salt = secrets.token_hex(16)
    digest = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt.encode("utf-8"), PASSWORD_ITERATIONS
    ).hex()
    return f"pbkdf2_sha256${PASSWORD_ITERATIONS}${salt}${digest}"


def check_password_hash(stored, password):
    try:
        algorithm, iterations, salt, expected = stored.split("$", 3)
        if algorithm != "pbkdf2_sha256":
            return False
        actual = hashlib.pbkdf2_hmac(
            "sha256", password.encode("utf-8"), salt.encode("utf-8"), int(iterations)
        ).hex()
        return secrets.compare_digest(actual, expected)
    except (ValueError, TypeError):
        return False


def get_csrf_token():
    token = session.get("_csrf_token")
    if not token:
        token = secrets.token_urlsafe(32)
        session["_csrf_token"] = token
    return token


@app.before_request
def protect_csrf():
    if request.method == "POST":
        sent = request.form.get("csrf_token", "")
        expected = session.get("_csrf_token", "")
        if not expected or not sent or not secrets.compare_digest(sent, expected):
            abort(400)


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def query_one(sql, params=()):
    with get_db() as conn:
        return conn.execute(sql, params).fetchone()


def query_all(sql, params=()):
    with get_db() as conn:
        return conn.execute(sql, params).fetchall()


def execute(sql, params=()):
    with get_db() as conn:
        cur = conn.execute(sql, params)
        conn.commit()
        return cur.lastrowid


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if "user_id" not in session:
            flash("Please sign in to continue.", "warning")
            return redirect(url_for("login"))
        return view(*args, **kwargs)
    return wrapped


def role_required(role):
    def decorator(view):
        @wraps(view)
        def wrapped(*args, **kwargs):
            if "user_id" not in session:
                flash("Please sign in to continue.", "warning")
                return redirect(url_for("login"))
            if session.get("role") != role:
                abort(403)
            return view(*args, **kwargs)
        return wrapped
    return decorator


def admin_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        user = current_user()
        if not user:
            flash("Please sign in to continue.", "warning")
            return redirect(url_for("login"))
        if user["role"] != "instructor" or not bool(user["is_admin"]):
            abort(403)
        return view(*args, **kwargs)
    return wrapped


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def allowed_avatar_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in AVATAR_EXTENSIONS


def clean_email(value):
    if not value:
        return ""
    email = str(value).strip()
    upper = email.upper()
    if "YOUR_EMAIL" in upper or "REPLACE" in upper or email in {"-", "_"}:
        return ""
    return email


def avatar_src(filename=None):
    if filename:
        return url_for("avatar_file", filename=filename)
    return url_for("static", filename="images/default-avatar.webp")


def current_user():
    if "user_id" not in session:
        return None
    return query_one("SELECT * FROM users WHERE id=?", (session["user_id"],))


def user_is_admin(user=None):
    user = user or current_user()
    return bool(user and user["role"] == "instructor" and user["is_admin"])


def classroom_for_student(student_id):
    return query_one(
        """
        SELECT c.*,i.name AS instructor_name,i.email AS instructor_email,
               i.avatar_filename AS instructor_avatar,
               p.id AS project_id,p.project_number,p.industry,p.title AS project_title,
               p.summary AS project_summary,p.entities,p.personas,p.process,p.integration,
               p.integration_name,p.integration_base_url,p.integration_docs_url,
               p.integration_auth,p.integration_operation,p.integration_path,
               p.workspace,p.agent,p.accent
        FROM users u
        LEFT JOIN classrooms c ON c.id=u.classroom_id
        LEFT JOIN users i ON i.id=c.instructor_id
        LEFT JOIN projects p ON p.id=c.project_id
        WHERE u.id=? AND u.role='student'
        """,
        (student_id,),
    )


def project_for_student(student_id):
    classroom = classroom_for_student(student_id)
    if not classroom or classroom["project_id"] is None:
        return None
    return query_one("SELECT * FROM projects WHERE id=?", (classroom["project_id"],))


def instructor_can_access_student(student_id, user=None):
    user = user or current_user()
    if not user:
        return False
    if user["role"] == "student":
        return user["id"] == student_id
    if user_is_admin(user):
        return True
    row = query_one(
        """
        SELECT c.instructor_id
        FROM users s JOIN classrooms c ON c.id=s.classroom_id
        WHERE s.id=? AND s.role='student'
        """,
        (student_id,),
    )
    return bool(row and row["instructor_id"] == user["id"])


def instructor_can_access_classroom(classroom_id, user=None):
    user = user or current_user()
    if not user or user["role"] != "instructor":
        return False
    if user_is_admin(user):
        return True
    row = query_one("SELECT instructor_id FROM classrooms WHERE id=?", (classroom_id,))
    return bool(row and row["instructor_id"] == user["id"])


def classroom_has_work(classroom_id):
    row = query_one(
        """
        SELECT COUNT(*) AS total
        FROM submissions s
        JOIN users u ON u.id=s.student_id
        WHERE u.classroom_id=?
        """,
        (classroom_id,),
    )
    return bool(row and row["total"])


def now_iso():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


@app.context_processor
def inject_globals():
    user = current_user()
    return {
        "current_user": user,
        "is_academy_admin": user_is_admin(user),
        "today": date.today().isoformat(),
        "csrf_token": get_csrf_token(),
        "avatar_src": avatar_src,
        "clean_email": clean_email,
    }


@app.route("/")
def home():
    if session.get("role") == "instructor":
        return redirect(url_for("instructor_dashboard"))
    if session.get("role") == "student":
        return redirect(url_for("student_dashboard"))
    return render_template("landing.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        user = query_one("SELECT * FROM users WHERE lower(email)=?", (email,))
        if user and user["is_active"] and check_password_hash(user["password_hash"], password):
            session.clear()
            session["user_id"] = user["id"]
            session["role"] = user["role"]
            session["name"] = user["name"]
            flash(f"Welcome back, {user['name']}.", "success")
            return redirect(url_for("home"))
        flash("Invalid email or password.", "danger")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("You have been signed out.", "info")
    return redirect(url_for("login"))


@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    user = current_user()
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        if not name or not email:
            flash("Name and email are required.", "danger")
            return redirect(url_for("profile"))
        duplicate = query_one("SELECT id FROM users WHERE lower(email)=? AND id<>?", (email, user["id"]))
        if duplicate:
            flash("Another account already uses that email address.", "danger")
            return redirect(url_for("profile"))

        avatar_filename = user["avatar_filename"]
        selected_preset = request.form.get("avatar_preset", "").strip()

        def remove_custom_avatar(filename):
            if filename and filename not in AVATAR_PRESET_FILES:
                old_path = AVATAR_DIR / filename
                if old_path.exists():
                    old_path.unlink()

        if selected_preset in AVATAR_PRESET_FILES:
            remove_custom_avatar(avatar_filename)
            avatar_filename = selected_preset
        elif request.form.get("remove_avatar") == "1":
            remove_custom_avatar(avatar_filename)
            avatar_filename = None

        uploaded = request.files.get("avatar")
        if uploaded and uploaded.filename:
            if not allowed_avatar_file(uploaded.filename):
                flash("Profile pictures must be PNG, JPG, JPEG, or WebP.", "danger")
                return redirect(url_for("profile"))
            extension = uploaded.filename.rsplit(".", 1)[1].lower()
            timestamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
            new_filename = f"user_{user['id']}_{timestamp}.{extension}"
            uploaded.save(AVATAR_DIR / new_filename)
            remove_custom_avatar(avatar_filename)
            avatar_filename = new_filename

        execute("UPDATE users SET name=?,email=?,avatar_filename=? WHERE id=?", (name, email, avatar_filename, user["id"]))
        session["name"] = name
        flash("Your profile has been updated.", "success")
        return redirect(url_for("profile"))
    return render_template("profile.html", user=user, avatar_presets=AVATAR_PRESETS)


@app.route("/avatars/<path:filename>")
@login_required
def avatar_file(filename):
    return send_from_directory(AVATAR_DIR, filename)


@app.route("/projects")
@login_required
def projects():
    user = current_user()
    rows = query_all("SELECT * FROM projects ORDER BY project_number")
    milestones = query_all(
        """
        SELECT pm.*,p.project_number,p.title AS project_title
        FROM project_milestones pm JOIN projects p ON p.id=pm.project_id
        ORDER BY p.project_number,pm.week_number
        """
    )
    selected_project = None
    classroom = None
    if user["role"] == "student":
        classroom = classroom_for_student(user["id"])
        selected_project = project_for_student(user["id"])
    return render_template(
        "projects.html", projects=rows, milestones=milestones,
        selected_project=selected_project, classroom=classroom,
    )


@app.route("/student/select-project", methods=["GET", "POST"])
@role_required("student")
def select_project():
    flash("Your project is assigned through your classroom. Contact your instructor if the classroom is incorrect.", "info")
    return redirect(url_for("projects"))


@app.route("/curriculum")
@login_required
def curriculum():
    weeks = query_all("SELECT * FROM weeks WHERE week_number BETWEEN 1 AND 16 ORDER BY week_number")
    return render_template("curriculum.html", weeks=weeks)


@app.route("/curriculum/week/<int:week_number>")
@login_required
def curriculum_week(week_number):
    if not 1 <= week_number <= 16:
        abort(404)
    week = query_one("SELECT * FROM weeks WHERE week_number=?", (week_number,))
    if not week:
        abort(404)
    project = None
    classroom = None
    if current_user()["role"] == "student":
        classroom = classroom_for_student(current_user()["id"])
        project = project_for_student(current_user()["id"])
    return render_template("curriculum_week_overview.html", week=week, project=project, selected_project=project, classroom=classroom)


@app.route("/projects/<int:project_id>/week/<int:week_number>")
@login_required
def project_week(project_id, week_number):
    if not 1 <= week_number <= 16:
        abort(404)
    user = current_user()
    if user["role"] == "student":
        classroom = classroom_for_student(user["id"])
        if not classroom or classroom["project_id"] != project_id:
            abort(403)
    project = query_one("SELECT * FROM projects WHERE id=?", (project_id,))
    week = query_one("SELECT * FROM weeks WHERE week_number=?", (week_number,))
    milestone = query_one(
        "SELECT * FROM project_milestones WHERE project_id=? AND week_number=?",
        (project_id, week_number),
    )
    if not project or not week or not milestone:
        abort(404)
    assignments = query_all(
        """
        SELECT a.* FROM assignments a JOIN weeks w ON w.id=a.week_id
        WHERE w.week_number=? AND a.is_published=1
        ORDER BY CASE a.category WHEN 'Hands-On' THEN 1 WHEN 'Research' THEN 2
          WHEN 'LinkedIn' THEN 3 WHEN 'Capstone' THEN 4 ELSE 5 END
        """,
        (week_number,),
    )
    context = dict(project)
    context.update({
        "project_id": project["id"], "project_number": project["project_number"], "project_title": project["title"],
        "project_summary": project["summary"], "milestone_title": milestone["title"],
        "milestone_instructions": milestone["instructions"],
        "milestone_deliverable": milestone["deliverable"], "is_final": milestone["is_final"],
        "week_number": week["week_number"], "stage": week["stage"], "topics": week["topics"],
        "research_topic": week["research_topic"], "linkedin_topic": week["linkedin_topic"],
    })
    guide = build_guided_lab(context, week_number, week["research_topic"], week["linkedin_topic"])
    return render_template("week_detail.html", week=context, assignments=assignments, guide=guide)


@app.route("/student")
@role_required("student")
def student_dashboard():
    user = current_user()
    classroom = classroom_for_student(user["id"])
    project = project_for_student(user["id"])
    if not classroom or not project:
        return render_template("error.html", code=409, message="Your classroom assignment is pending. Ask the academy administrator to place you in a classroom.")

    rows = query_all(
        """
        SELECT a.*,w.week_number,w.title AS week_title,
               CASE WHEN a.category IN ('Hands-On','Capstone') THEN pm.title ELSE a.title END AS display_title,
               CASE WHEN a.category IN ('Hands-On','Capstone') THEN pm.instructions ELSE a.instructions END AS display_instructions,
               CASE WHEN a.category IN ('Hands-On','Capstone') THEN pm.deliverable ELSE a.deliverable END AS display_deliverable,
               s.id AS submission_id,s.status AS submission_status,s.score,s.submitted_at,s.updated_at,s.mentor_feedback
        FROM assignments a
        JOIN weeks w ON w.id=a.week_id
        LEFT JOIN project_milestones pm ON pm.project_id=? AND pm.week_number=w.week_number
        LEFT JOIN submissions s ON s.assignment_id=a.id AND s.student_id=?
        WHERE a.is_published=1 AND w.week_number BETWEEN 1 AND 16
        ORDER BY w.week_number,CASE a.category WHEN 'Hands-On' THEN 1 WHEN 'Research' THEN 2 WHEN 'LinkedIn' THEN 3 WHEN 'Capstone' THEN 4 ELSE 5 END
        """,
        (project["id"], user["id"]),
    )
    summary = query_one(
        """
        SELECT COUNT(a.id) AS total,
               SUM(CASE WHEN s.status IN ('Submitted','Under Review','Revision Required','Approved') THEN 1 ELSE 0 END) AS submitted,
               SUM(CASE WHEN s.status='Approved' THEN 1 ELSE 0 END) AS approved,
               COALESCE(ROUND(AVG(CASE WHEN s.score IS NOT NULL THEN s.score END),1),0) AS avg_score
        FROM assignments a JOIN weeks w ON w.id=a.week_id
        LEFT JOIN submissions s ON s.assignment_id=a.id AND s.student_id=?
        WHERE a.is_published=1 AND w.week_number BETWEEN 1 AND 16
        """,
        (user["id"],),
    )
    project_progress = query_all(
        """
        SELECT w.week_number,pm.title,a.id AS assignment_id,a.category,s.status,s.score
        FROM weeks w
        JOIN project_milestones pm ON pm.week_number=w.week_number AND pm.project_id=?
        JOIN assignments a ON a.week_id=w.id AND a.is_published=1 AND a.category IN ('Hands-On','Capstone')
        LEFT JOIN submissions s ON s.assignment_id=a.id AND s.student_id=?
        WHERE w.week_number BETWEEN 1 AND 16 ORDER BY w.week_number
        """,
        (project["id"], user["id"]),
    )
    mentor = query_one("SELECT id,name,email,avatar_filename FROM users WHERE id=?", (classroom["instructor_id"],))
    return render_template(
        "student_dashboard.html", rows=rows, summary=summary, project=project,
        project_progress=project_progress, mentor=mentor, classroom=classroom,
    )


@app.route("/student/assignment/<int:assignment_id>", methods=["GET", "POST"])
@role_required("student")
def student_assignment(assignment_id):
    user = current_user()
    classroom = classroom_for_student(user["id"])
    project = project_for_student(user["id"])
    if not classroom or not project:
        abort(409)
    assignment = query_one(
        """
        SELECT a.*,w.week_number,w.title AS week_title,w.topics,
               p.project_number,p.industry,p.title AS project_title,
               CASE WHEN a.category IN ('Hands-On','Capstone') THEN pm.title ELSE a.title END AS display_title,
               CASE WHEN a.category IN ('Hands-On','Capstone') THEN pm.instructions ELSE a.instructions END AS display_instructions,
               CASE WHEN a.category IN ('Hands-On','Capstone') THEN pm.deliverable ELSE a.deliverable END AS display_deliverable
        FROM assignments a JOIN weeks w ON w.id=a.week_id
        JOIN projects p ON p.id=?
        LEFT JOIN project_milestones pm ON pm.project_id=p.id AND pm.week_number=w.week_number
        WHERE a.id=? AND a.is_published=1 AND w.week_number BETWEEN 1 AND 16
        """,
        (project["id"], assignment_id),
    )
    if not assignment:
        abort(404)
    submission = query_one("SELECT * FROM submissions WHERE assignment_id=? AND student_id=?", (assignment_id, user["id"]))
    if request.method == "POST":
        status = request.form.get("status", "Draft")
        if status not in {"Draft", "Submitted"}:
            status = "Draft"
        submission_text = request.form.get("submission_text", "").strip()
        submission_url = request.form.get("submission_url", "").strip()
        linkedin_url = request.form.get("linkedin_url", "").strip()
        student_note = request.form.get("student_note", "").strip()
        filename = submission["file_name"] if submission else None
        uploaded = request.files.get("file")
        if uploaded and uploaded.filename:
            if not allowed_file(uploaded.filename):
                flash("Unsupported file type.", "danger")
                return redirect(request.url)
            safe = secure_filename(uploaded.filename)
            timestamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
            filename = f"{user['id']}_{assignment_id}_{timestamp}_{safe}"
            uploaded.save(UPLOAD_DIR / filename)
        now = now_iso()
        submitted_at = now if status == "Submitted" else (submission["submitted_at"] if submission else None)
        if submission:
            execute(
                """
                UPDATE submissions SET status=?,submission_text=?,submission_url=?,linkedin_url=?,
                    student_note=?,file_name=?,submitted_at=?,updated_at=?,
                    revision_number=revision_number+CASE WHEN status='Revision Required' AND ?='Submitted' THEN 1 ELSE 0 END
                WHERE id=? AND student_id=?
                """,
                (status,submission_text,submission_url,linkedin_url,student_note,filename,submitted_at,now,status,submission["id"],user["id"]),
            )
        else:
            execute(
                """
                INSERT INTO submissions
                (assignment_id,student_id,status,submission_text,submission_url,linkedin_url,student_note,file_name,submitted_at,updated_at,revision_number)
                VALUES (?,?,?,?,?,?,?,?,?,?,0)
                """,
                (assignment_id,user["id"],status,submission_text,submission_url,linkedin_url,student_note,filename,submitted_at,now),
            )
        flash("Your work has been saved.", "success")
        return redirect(url_for("student_assignment", assignment_id=assignment_id))
    return render_template("student_assignment.html", assignment=assignment, submission=submission, classroom=classroom)


@app.route("/uploads/<path:filename>")
@login_required
def uploaded_file(filename):
    record = query_one(
        """
        SELECT s.student_id,c.instructor_id
        FROM submissions s JOIN users u ON u.id=s.student_id
        LEFT JOIN classrooms c ON c.id=u.classroom_id
        WHERE s.file_name=?
        """,
        (filename,),
    )
    if not record:
        abort(404)
    user = current_user()
    if user["role"] == "student" and record["student_id"] != user["id"]:
        abort(403)
    if user["role"] == "instructor" and not user_is_admin(user) and record["instructor_id"] != user["id"]:
        abort(403)
    return send_from_directory(UPLOAD_DIR, filename, as_attachment=True)


@app.route("/instructor")
@role_required("instructor")
def instructor_dashboard():
    user = current_user()
    class_scope = "" if user_is_admin(user) else " AND c.instructor_id=?"
    params = [] if user_is_admin(user) else [user["id"]]
    classroom_count = query_one("SELECT COUNT(*) AS total FROM classrooms c WHERE c.is_active=1" + class_scope, params)["total"]
    students = query_one(
        "SELECT COUNT(*) AS total FROM users u JOIN classrooms c ON c.id=u.classroom_id WHERE u.role='student' AND u.is_active=1" + class_scope,
        params,
    )["total"]
    awaiting = query_one(
        """
        SELECT COUNT(*) AS total FROM submissions s
        JOIN users u ON u.id=s.student_id JOIN classrooms c ON c.id=u.classroom_id
        WHERE s.status IN ('Submitted','Under Review')
        """ + class_scope,
        params,
    )["total"]
    revisions = query_one(
        """
        SELECT COUNT(*) AS total FROM submissions s
        JOIN users u ON u.id=s.student_id JOIN classrooms c ON c.id=u.classroom_id
        WHERE s.status='Revision Required'
        """ + class_scope,
        params,
    )["total"]
    assignments = query_one("SELECT COUNT(*) AS total FROM assignments WHERE is_published=1")["total"]
    recent_sql = """
        SELECT s.*,u.name AS student_name,u.email AS student_email,u.avatar_filename AS student_avatar,
               c.name AS classroom_name,p.title AS project_title,p.industry,w.week_number,a.category,
               CASE WHEN a.category IN ('Hands-On','Capstone') THEN pm.title ELSE a.title END AS assignment_title
        FROM submissions s JOIN users u ON u.id=s.student_id
        JOIN classrooms c ON c.id=u.classroom_id JOIN projects p ON p.id=c.project_id
        JOIN assignments a ON a.id=s.assignment_id JOIN weeks w ON w.id=a.week_id
        LEFT JOIN project_milestones pm ON pm.project_id=p.id AND pm.week_number=w.week_number
        WHERE 1=1
    """
    recent_params = []
    if not user_is_admin(user):
        recent_sql += " AND c.instructor_id=?"
        recent_params.append(user["id"])
    recent_sql += " ORDER BY COALESCE(s.submitted_at,s.updated_at) DESC LIMIT 12"
    recent = query_all(recent_sql, recent_params)
    stats = {"classrooms": classroom_count, "students": students, "assignments": assignments, "awaiting_review": awaiting, "revisions": revisions}
    return render_template(
        "instructor_dashboard.html", stats=stats, recent=recent,
        scope_title="Academy overview" if user_is_admin(user) else "My classrooms",
        scope_note="All classrooms and program activity" if user_is_admin(user) else "Only classrooms assigned to you",
    )


@app.route("/instructor/submissions")
@role_required("instructor")
def submissions_list():
    user = current_user()
    status = request.args.get("status", "").strip()
    student_id = request.args.get("student_id", "").strip()
    category = request.args.get("category", "").strip()
    classroom_id = request.args.get("classroom_id", "").strip()
    sql = """
        SELECT s.*,u.name AS student_name,u.email AS student_email,u.avatar_filename AS student_avatar,
               c.id AS classroom_id,c.name AS classroom_name,c.instructor_id,
               p.title AS project_title,p.industry,a.category,a.max_score,w.week_number,w.title AS week_title,
               CASE WHEN a.category IN ('Hands-On','Capstone') THEN pm.title ELSE a.title END AS assignment_title
        FROM submissions s JOIN users u ON u.id=s.student_id
        JOIN classrooms c ON c.id=u.classroom_id JOIN projects p ON p.id=c.project_id
        JOIN assignments a ON a.id=s.assignment_id JOIN weeks w ON w.id=a.week_id
        LEFT JOIN project_milestones pm ON pm.project_id=p.id AND pm.week_number=w.week_number
        WHERE 1=1
    """
    params = []
    if not user_is_admin(user):
        sql += " AND c.instructor_id=?"
        params.append(user["id"])
    if status:
        sql += " AND s.status=?"; params.append(status)
    if student_id:
        sql += " AND s.student_id=?"; params.append(student_id)
    if category:
        sql += " AND a.category=?"; params.append(category)
    if classroom_id:
        sql += " AND c.id=?"; params.append(classroom_id)
    sql += " ORDER BY c.name,w.week_number,u.name,CASE a.category WHEN 'Hands-On' THEN 1 WHEN 'Research' THEN 2 WHEN 'LinkedIn' THEN 3 WHEN 'Capstone' THEN 4 ELSE 5 END"
    rows = query_all(sql, params)
    scope = "" if user_is_admin(user) else " WHERE c.instructor_id=?"
    scope_params = [] if user_is_admin(user) else [user["id"]]
    students = query_all("SELECT u.id,u.name FROM users u JOIN classrooms c ON c.id=u.classroom_id" + scope + " AND u.role='student' ORDER BY u.name" if scope else "SELECT u.id,u.name FROM users u JOIN classrooms c ON c.id=u.classroom_id WHERE u.role='student' ORDER BY u.name", scope_params)
    classrooms = query_all("SELECT c.id,c.name FROM classrooms c" + scope + " ORDER BY c.name", scope_params)
    return render_template(
        "submissions_list.html", rows=rows, students=students, classrooms=classrooms,
        selected_status=status, selected_student=student_id, selected_category=category, selected_classroom=classroom_id,
    )


@app.route("/instructor/submission/<int:submission_id>", methods=["GET", "POST"])
@role_required("instructor")
def grade_submission(submission_id):
    user = current_user()
    row = query_one(
        """
        SELECT s.*,u.name AS student_name,u.email AS student_email,u.avatar_filename AS student_avatar,
               c.name AS classroom_name,c.instructor_id,p.title AS project_title,p.industry,
               a.category,a.max_score,w.week_number,w.title AS week_title,
               CASE WHEN a.category IN ('Hands-On','Capstone') THEN pm.title ELSE a.title END AS assignment_title,
               CASE WHEN a.category IN ('Hands-On','Capstone') THEN pm.instructions ELSE a.instructions END AS instructions,
               CASE WHEN a.category IN ('Hands-On','Capstone') THEN pm.deliverable ELSE a.deliverable END AS deliverable
        FROM submissions s JOIN users u ON u.id=s.student_id
        JOIN classrooms c ON c.id=u.classroom_id JOIN projects p ON p.id=c.project_id
        JOIN assignments a ON a.id=s.assignment_id JOIN weeks w ON w.id=a.week_id
        LEFT JOIN project_milestones pm ON pm.project_id=p.id AND pm.week_number=w.week_number
        WHERE s.id=?
        """,
        (submission_id,),
    )
    if not row:
        abort(404)
    if not user_is_admin(user) and row["instructor_id"] != user["id"]:
        abort(403)
    if request.method == "POST":
        status = request.form.get("status", "Under Review")
        if status not in {"Under Review", "Revision Required", "Approved", "Late"}:
            status = "Under Review"
        score_raw = request.form.get("score", "").strip()
        try:
            score = float(score_raw) if score_raw else None
        except ValueError:
            flash("Enter a valid numeric score.", "danger")
            return redirect(request.url)
        if score is not None and (score < 0 or score > row["max_score"]):
            flash(f"Score must be between 0 and {row['max_score']}.", "danger")
            return redirect(request.url)
        feedback = request.form.get("mentor_feedback", "").strip()
        now = now_iso()
        execute(
            "UPDATE submissions SET status=?,score=?,mentor_feedback=?,graded_by=?,graded_at=?,updated_at=? WHERE id=?",
            (status,score,feedback,user["id"],now,now,submission_id),
        )
        flash("Grade and feedback saved.", "success")
        return redirect(url_for("grade_submission", submission_id=submission_id))
    return render_template("grade_submission.html", row=row)


@app.route("/instructor/classrooms", methods=["GET", "POST"])
@role_required("instructor")
def manage_classrooms():
    user = current_user()
    is_admin = user_is_admin(user)
    instructors = query_all("SELECT id,name,email FROM users WHERE role='instructor' AND is_active=1 ORDER BY name") if is_admin else []
    projects = query_all("SELECT id,industry,title FROM projects ORDER BY project_number")
    if request.method == "POST":
        if not is_admin:
            abort(403)
        name = request.form.get("name", "").strip()
        description = request.form.get("description", "").strip()
        try:
            instructor_id = int(request.form.get("instructor_id", "0"))
            project_id = int(request.form.get("project_id", "0"))
        except ValueError:
            instructor_id = project_id = 0
        instructor = query_one("SELECT id FROM users WHERE id=? AND role='instructor' AND is_active=1", (instructor_id,))
        project = query_one("SELECT id FROM projects WHERE id=?", (project_id,))
        if not name or not instructor or not project:
            flash("Classroom name, active instructor, and project are required.", "danger")
        elif query_one("SELECT id FROM classrooms WHERE lower(name)=? AND instructor_id=?", (name.lower(), instructor_id)):
            flash("This instructor already has a classroom with that name.", "danger")
        else:
            execute(
                "INSERT INTO classrooms(name,instructor_id,project_id,description,is_active,created_at) VALUES (?,?,?,?,1,?)",
                (name,instructor_id,project_id,description,now_iso()),
            )
            flash("Classroom created.", "success")
            return redirect(url_for("manage_classrooms"))
    sql = """
        SELECT c.*,i.name AS instructor_name,i.email AS instructor_email,i.avatar_filename AS instructor_avatar,
               p.industry,p.title AS project_title,p.accent,COUNT(u.id) AS student_count
        FROM classrooms c JOIN users i ON i.id=c.instructor_id JOIN projects p ON p.id=c.project_id
        LEFT JOIN users u ON u.classroom_id=c.id AND u.role='student'
        WHERE 1=1
    """
    params=[]
    if not is_admin:
        sql += " AND c.instructor_id=?"; params.append(user["id"])
    sql += " GROUP BY c.id ORDER BY c.is_active DESC,c.name"
    classrooms=query_all(sql,params)
    return render_template("manage_classrooms.html", classrooms=classrooms, instructors=instructors, projects=projects, page_is_admin=is_admin)


@app.route("/instructor/classroom/<int:classroom_id>/update", methods=["POST"])
@admin_required
def update_classroom(classroom_id):
    classroom = query_one("SELECT * FROM classrooms WHERE id=?", (classroom_id,))
    if not classroom:
        abort(404)
    name = request.form.get("name", "").strip()
    description = request.form.get("description", "").strip()
    try:
        instructor_id = int(request.form.get("instructor_id", "0"))
        project_id = int(request.form.get("project_id", "0"))
    except ValueError:
        instructor_id = project_id = 0
    if not query_one("SELECT id FROM users WHERE id=? AND role='instructor' AND is_active=1", (instructor_id,)) or not query_one("SELECT id FROM projects WHERE id=?", (project_id,)):
        flash("Select a valid instructor and project.", "danger")
        return redirect(url_for("manage_classrooms"))
    if project_id != classroom["project_id"] and classroom_has_work(classroom_id):
        flash("The classroom project cannot change after students have submitted work.", "warning")
        return redirect(url_for("manage_classrooms"))
    execute("UPDATE classrooms SET name=?,instructor_id=?,project_id=?,description=? WHERE id=?", (name,instructor_id,project_id,description,classroom_id))
    flash("Classroom updated.", "success")
    return redirect(url_for("manage_classrooms"))


@app.route("/instructor/classroom/<int:classroom_id>/toggle", methods=["POST"])
@admin_required
def toggle_classroom(classroom_id):
    row=query_one("SELECT * FROM classrooms WHERE id=?",(classroom_id,))
    if not row: abort(404)
    execute("UPDATE classrooms SET is_active=? WHERE id=?",(0 if row["is_active"] else 1,classroom_id))
    flash("Classroom status updated.","success")
    return redirect(url_for("manage_classrooms"))


@app.route("/instructor/students", methods=["GET", "POST"])
@role_required("instructor")
def manage_students():
    user=current_user(); is_admin=user_is_admin(user)
    class_sql="SELECT c.id,c.name,p.industry,p.title AS project_title FROM classrooms c JOIN projects p ON p.id=c.project_id WHERE c.is_active=1"
    class_params=[]
    if not is_admin:
        class_sql += " AND c.instructor_id=?"; class_params.append(user["id"])
    class_sql += " ORDER BY c.name"
    classrooms=query_all(class_sql,class_params)
    if request.method=="POST":
        name=request.form.get("name","").strip(); email=request.form.get("email","").strip().lower(); password=request.form.get("password","").strip()
        try: classroom_id=int(request.form.get("classroom_id","0"))
        except ValueError: classroom_id=0
        classroom=query_one("SELECT * FROM classrooms WHERE id=? AND is_active=1",(classroom_id,))
        if not classroom or (not is_admin and classroom["instructor_id"]!=user["id"]):
            flash("Select a classroom you can manage.","danger")
        elif not name or not email or not password:
            flash("Name, email, and temporary password are required.","danger")
        elif query_one("SELECT id FROM users WHERE lower(email)=?",(email,)):
            flash("A user with this email already exists.","danger")
        else:
            execute(
                "INSERT INTO users(name,email,avatar_filename,password_hash,role,classroom_id,is_admin,is_active,created_at) VALUES (?,?,NULL,?,'student',?,0,1,?)",
                (name,email,generate_password_hash(password),classroom_id,now_iso()),
            )
            flash("Student account created and added to the classroom.","success")
            return redirect(url_for("manage_students"))
    sql="""
        SELECT u.*,c.name AS classroom_name,c.instructor_id,i.name AS instructor_name,
               p.industry,p.title AS project_title,COUNT(s.id) AS submissions,
               SUM(CASE WHEN s.status='Approved' THEN 1 ELSE 0 END) AS approved,
               COALESCE(ROUND(AVG(CASE WHEN s.score IS NOT NULL THEN s.score END),1),0) AS avg_score
        FROM users u JOIN classrooms c ON c.id=u.classroom_id JOIN users i ON i.id=c.instructor_id
        JOIN projects p ON p.id=c.project_id LEFT JOIN submissions s ON s.student_id=u.id
        WHERE u.role='student'
    """
    params=[]
    if not is_admin:
        sql += " AND c.instructor_id=?"; params.append(user["id"])
    sql += " GROUP BY u.id ORDER BY c.name,u.name"
    students=query_all(sql,params)
    return render_template("manage_students.html",students=students,classrooms=classrooms,page_is_admin=is_admin)


@app.route("/instructor/student/<int:user_id>/classroom", methods=["POST"])
@role_required("instructor")
def assign_student_classroom(user_id):
    user=current_user()
    student=query_one("SELECT * FROM users WHERE id=? AND role='student'",(user_id,))
    if not student or not instructor_can_access_student(user_id,user): abort(403)
    try: classroom_id=int(request.form.get("classroom_id","0"))
    except ValueError: classroom_id=0
    classroom=query_one("SELECT * FROM classrooms WHERE id=? AND is_active=1",(classroom_id,))
    if not classroom or (not user_is_admin(user) and classroom["instructor_id"]!=user["id"]):
        flash("Select a classroom you can manage.","danger")
        return redirect(url_for("manage_students"))
    if student["classroom_id"] != classroom_id and query_one("SELECT COUNT(*) AS total FROM submissions WHERE student_id=?",(user_id,))["total"]:
        flash("Move is blocked because this student already has submitted work. An administrator should archive or review the work first.","warning")
        return redirect(url_for("manage_students"))
    execute("UPDATE users SET classroom_id=? WHERE id=?",(classroom_id,user_id))
    flash("Student classroom updated.","success")
    return redirect(url_for("manage_students"))


# Legacy URLs retained so old links do not fail.
@app.route("/instructor/student/<int:user_id>/class", methods=["POST"])
@role_required("instructor")
def update_student_class(user_id):
    flash("Classes are now managed as classrooms. Choose a classroom from the student roster.","info")
    return redirect(url_for("manage_students"))


@app.route("/instructor/student/<int:user_id>/assign", methods=["POST"])
@role_required("instructor")
def assign_student_instructor(user_id):
    flash("Instructor ownership is defined by the classroom, not by the individual student.","info")
    return redirect(url_for("manage_students"))


@app.route("/instructor/student/<int:user_id>/project", methods=["POST"])
@role_required("instructor")
def assign_student_project(user_id):
    flash("Project selection is defined by the classroom, not by the individual student.","info")
    return redirect(url_for("manage_students"))


@app.route("/instructor/instructors", methods=["GET", "POST"])
@admin_required
def manage_instructors():
    if request.method=="POST":
        name=request.form.get("name","").strip(); email=request.form.get("email","").strip().lower(); password=request.form.get("password","").strip(); is_admin=1 if request.form.get("is_admin")=="1" else 0
        if not name or not email or not password: flash("Name, email, and temporary password are required.","danger")
        elif query_one("SELECT id FROM users WHERE lower(email)=?",(email,)): flash("A user with this email already exists.","danger")
        else:
            execute("INSERT INTO users(name,email,avatar_filename,password_hash,role,classroom_id,is_admin,is_active,created_at) VALUES (?,?,NULL,?,'instructor',NULL,?,1,?)",(name,email,generate_password_hash(password),is_admin,now_iso()))
            flash("Instructor account created.","success"); return redirect(url_for("manage_instructors"))
    instructors=query_all(
        """
        SELECT i.*,COUNT(DISTINCT c.id) AS classroom_count,COUNT(DISTINCT s.id) AS assigned_students
        FROM users i LEFT JOIN classrooms c ON c.instructor_id=i.id
        LEFT JOIN users s ON s.classroom_id=c.id AND s.role='student'
        WHERE i.role='instructor' GROUP BY i.id
        ORDER BY i.is_active DESC,i.is_admin DESC,i.name
        """
    )
    return render_template("manage_instructors.html",instructors=instructors)


@app.route("/instructor/instructor/<int:user_id>/toggle", methods=["POST"])
@admin_required
def toggle_instructor(user_id):
    instructor=query_one("SELECT * FROM users WHERE id=? AND role='instructor'",(user_id,))
    if not instructor: abort(404)
    if user_id==session["user_id"]:
        flash("You cannot deactivate your own instructor account.","warning"); return redirect(url_for("manage_instructors"))
    if instructor["is_active"]:
        active_classrooms=query_one("SELECT COUNT(*) AS total FROM classrooms WHERE instructor_id=? AND is_active=1",(user_id,))["total"]
        if active_classrooms:
            flash("Reassign or deactivate this instructor's classrooms first.","warning"); return redirect(url_for("manage_instructors"))
        if instructor["is_admin"]:
            admin_count=query_one("SELECT COUNT(*) AS total FROM users WHERE role='instructor' AND is_active=1 AND is_admin=1")["total"]
            if admin_count<=1:
                flash("At least one active academy administrator is required.","warning"); return redirect(url_for("manage_instructors"))
    execute("UPDATE users SET is_active=? WHERE id=?",(0 if instructor["is_active"] else 1,user_id))
    flash("Instructor status updated.","success"); return redirect(url_for("manage_instructors"))


@app.route("/instructor/student/<int:user_id>/toggle", methods=["POST"])
@role_required("instructor")
def toggle_student(user_id):
    user=current_user()
    if not instructor_can_access_student(user_id,user): abort(403)
    student=query_one("SELECT * FROM users WHERE id=? AND role='student'",(user_id,))
    if not student: abort(404)
    execute("UPDATE users SET is_active=? WHERE id=?",(0 if student["is_active"] else 1,user_id))
    flash("Student status updated.","success"); return redirect(url_for("manage_students"))


@app.route("/instructor/assignments")
@role_required("instructor")
def manage_assignments():
    user=current_user()
    sql="""
        SELECT a.*,w.week_number,w.title AS week_title,COUNT(s.id) AS submissions
        FROM assignments a JOIN weeks w ON w.id=a.week_id
        LEFT JOIN submissions s ON s.assignment_id=a.id
        LEFT JOIN users u ON u.id=s.student_id
        LEFT JOIN classrooms c ON c.id=u.classroom_id
        WHERE a.is_published=1
    """
    params=[]
    if not user_is_admin(user):
        sql += " AND (c.instructor_id=? OR s.id IS NULL)"; params.append(user["id"])
    sql += " GROUP BY a.id ORDER BY w.week_number,CASE a.category WHEN 'Hands-On' THEN 1 WHEN 'Research' THEN 2 WHEN 'LinkedIn' THEN 3 WHEN 'Capstone' THEN 4 ELSE 5 END"
    return render_template("manage_assignments.html",rows=query_all(sql,params))


@app.errorhandler(400)
def bad_request(_):
    return render_template("error.html",code=400,message="The request could not be validated."),400


@app.errorhandler(403)
def forbidden(_):
    return render_template("error.html",code=403,message="You do not have access to this page."),403


@app.errorhandler(404)
def not_found(_):
    return render_template("error.html",code=404,message="The requested page was not found."),404


@app.errorhandler(409)
def conflict(_):
    return render_template("error.html",code=409,message="This account is not assigned to a classroom yet."),409


if __name__=="__main__":
    app.run(debug=True)
