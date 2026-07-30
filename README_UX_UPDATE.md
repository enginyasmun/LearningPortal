# Instructor Portal UX Update

This package applies the five recommendations from the July 2026 instructor portal review without changing the Flask backend, database schema, routes, or role permissions.

## Included changes

1. Desktop sidebar collapse control with hover and keyboard-focus tooltips.
2. Dynamic assignment wording using the existing `stats.assignments` value.
3. Clear non-clickable empty state when no submissions await review.
4. Hidden temporary-password field with an accessible show/hide button.
5. An Edit action in the student roster that exposes only the controls already permitted by the current backend.

## Files to copy into the repository

Copy these files into the same paths on branch `mm`:

- `templates/base.html`
- `templates/instructor_dashboard.html`
- `templates/manage_students.html`
- `static/app.js`
- `static/ux_recommendations.css` (new file)
- `tests/test_ux_recommendations.py` (new optional test file)

No changes are required in `app.py`, `schema.sql`, or the database.

## Verification

From the repository root, run:

```bash
python -m pytest tests/test_ux_recommendations.py
```

Then reload the PythonAnywhere web app after pulling or uploading the files.
