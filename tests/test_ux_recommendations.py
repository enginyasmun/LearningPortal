from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def test_sidebar_has_collapse_control_and_accessible_tooltips():
    base = read("templates/base.html")
    script = read("static/app.js")
    css = read("static/ux_recommendations.css")
    assert "data-sidebar-collapse" in base
    assert "ux_recommendations.css" in base
    assert "link.dataset.tooltip = label" in script
    assert ".sidebar-collapsed .nav-link[data-tooltip]" in css
    assert ":focus-visible::after" in css


def test_assignment_count_is_dynamic_and_not_hard_coded():
    dashboard = read("templates/instructor_dashboard.html")
    assert "{{ stats.assignments }}" in dashboard
    assert "Published in the active 16-week program" in dashboard
    assert "48 per student" not in dashboard


def test_empty_review_queue_is_explained_and_not_clickable():
    dashboard = read("templates/instructor_dashboard.html")
    assert "{% if stats.awaiting_review %}" in dashboard
    assert "No submissions are awaiting review" in dashboard
    assert 'aria-disabled="true"' in dashboard


def test_temporary_password_is_hidden_with_toggle():
    students = read("templates/manage_students.html")
    script = read("static/app.js")
    assert 'type="password" name="password"' in students
    assert "data-password-toggle" in students
    assert "data-password-shell" in students
    assert 'input.type = showing ? "password" : "text"' in script


def test_student_edit_panel_preserves_existing_permission_scopes():
    students = read("templates/manage_students.html")
    assert "data-student-edit-toggle" in students
    assert "update_student_class" in students
    assert "{% if page_is_admin %}" in students
    assert "assign_student_instructor" in students
    assert "assign_student_project" in students
    assert "toggle_student" in students
    assert "Only controls permitted for your role are shown." in students
