# Version 14.1 Classroom UI Repair

This package fixes the two rendering problems introduced by the classroom update:

1. Classroom and student creation forms now use the portal design system.
2. Student roster avatars are constrained to 44 × 44 pixels and cannot expand to their source-image dimensions.

## Files changed

- `templates/manage_classrooms.html`
- `templates/manage_students.html`
- `templates/base.html`
- `static/styles.css`

## GitHub

Upload the complete package or replace the four files above.

Suggested commit message:

`Fix classroom forms and student roster avatars`

## PythonAnywhere

```bash
cd ~/LearningPortal
git pull origin main
workon coaching-env
python -m py_compile app.py guided_labs.py curriculum_data.py migrate_v14.py
```

Reload the web app and refresh the browser. The stylesheet URL uses `v=14.1`, so the corrected CSS should load without the old cache.

No database migration is required for this UI repair.
