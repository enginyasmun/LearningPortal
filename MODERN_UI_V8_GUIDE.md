# LearningPortal Modern UI Version 8

This is a complete GitHub-ready project. It is not a partial CSS patch.

## Design direction

Version 8 replaces the previous dense, traditional admin layout with a modern learning workspace:

- floating light navigation instead of the old solid dark sidebar
- collapsible desktop navigation with saved preference
- responsive mobile navigation
- command palette opened with `Ctrl + K`
- larger typography and clearer page hierarchy
- bento-style instructor and student dashboards
- modern metrics and progress visualization
- cleaner assignment, student, instructor, and submission tables
- redesigned project selection and 16-week roadmaps
- redesigned guided labs with clearer steps, checkpoints, commands, evidence, and quality gates
- modern landing and login pages
- subtle entrance animations and reduced-motion support
- official LinkedIn blue for LinkedIn assignments

The backend, database schema, roles, instructor privacy, project selection, guided-lab content, submissions, grading, and uploaded-file behavior are unchanged.

## Upload the complete project to GitHub

Repository:

`enginyasmun/LearningPortal`

1. Extract the complete ZIP.
2. Open the extracted folder.
3. Upload everything inside the folder to the root of the GitHub repository.
4. Allow GitHub to replace existing files.
5. Do not upload the ZIP file itself.

Suggested commit message:

`Replace portal UI with modern learning workspace`

## Update PythonAnywhere

Open a Bash console and run:

```bash
cd ~/LearningPortal
git pull origin main
workon coaching-env
pip install -r requirements.txt
python -m py_compile app.py guided_labs.py curriculum_data.py seed.py
```

Then open the PythonAnywhere **Web** tab and click **Reload**.

Open the website and press:

`Ctrl + F5`

This clears the old cached CSS and JavaScript.

## Database safety

This UI update does not require a migration.

Do not run:

```bash
RESET_DB=1 python seed.py
```

Do not delete:

`academy.db`

The repository `.gitignore` excludes `academy.db`, backup databases, environment files, and uploaded student files.

## Useful interface controls

- `Ctrl + K`: open quick navigation
- `/`: open quick navigation when not typing in a field
- `Esc`: close quick navigation or mobile navigation
- sidebar arrow: collapse or expand desktop navigation
- guided-lab checkboxes: save completion state in the student's browser
