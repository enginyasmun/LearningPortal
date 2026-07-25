# Version 10: Curriculum and Projects Separated Clearly

## New structure

### Curriculum

The Curriculum section is the shared 16-week class syllabus for every student.

It contains:

- the overall academy learning path
- common weekly Salesforce topics
- class stages and learning progression
- weekly research themes
- weekly LinkedIn communication themes
- a general explanation of how each topic connects to project work

It does not select or describe one industry application.

### Project Plans

The Project Plans section contains the five industry choices:

1. Financial Services
2. Healthcare
3. Nonprofit
4. Manufacturing
5. Professional Services

Each project contains:

- its own 16-week milestone plan
- project-specific objects and business process
- exact step-by-step guided build labs
- checkpoints, testing, commands, and evidence requirements
- the project-specific application of the common curriculum topic

## Page flow

- `/curriculum` shows the shared class overview.
- `/curriculum/week/5` shows what the entire class learns in Week 5.
- `/projects` shows the five industry tracks.
- `/projects/1/week/5` shows the detailed Week 5 guided lab for Project 1.

A curriculum week contains a button that sends the student to the corresponding guided lab for the project they selected.

## Upload to GitHub

Upload and replace all files from the complete package in the root of your `LearningPortal` repository.

Suggested commit message:

`Separate class curriculum from guided project plans`

## PythonAnywhere

After committing to GitHub, run:

```bash
cd ~/LearningPortal
git pull origin main
workon coaching-env
python -m py_compile app.py guided_labs.py curriculum_data.py seed.py
```

Then reload the web application from the PythonAnywhere Web tab and press `Ctrl + F5` in the browser.

## Database

No database migration is required.

Do not run `RESET_DB=1 python seed.py` and do not delete `academy.db`.
