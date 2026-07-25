# Version 14.2: Project Week and Classroom Diagram Fix

## Fixed

- Corrected the `/projects/<project>/week/<week>` 500 error.
- The route now passes the guided lab under the variable name expected by the template.
- Replaced the purple advertisement-style card with a visual classroom diagram showing one instructor, one classroom/project roadmap, and many students.
- Updated CSS and JavaScript cache version to `14.2`.

## PythonAnywhere

```bash
cd ~/LearningPortal
rm -rf __pycache__
git pull origin main
workon coaching-env
python -m py_compile app.py guided_labs.py curriculum_data.py migrate_v14.py
```

Reload the Web app and press `Ctrl + F5`. No migration is required.
