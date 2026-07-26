# LearningPortal Version 16: Student Focus Mode

Version 16 simplifies each weekly project page so students are not shown every lab, method, and submission card at the same time.

## New weekly workflow

The page is divided into four focused workspaces:

1. Build lab
2. Research lab
3. LinkedIn lab
4. Submit work

Only the selected workspace is visible. The other sections remain hidden until the student selects them.

## Guided build behavior

Only one build step is displayed at a time.

The student:

1. Completes the listed actions.
2. Confirms the expected checkpoint.
3. Saves the requested evidence.
4. Clicks **Mark step complete**.

Completion is manual because the website cannot reliably verify external actions performed in Git, GitHub, VS Code, Salesforce Setup, or a terminal.

The browser automatically saves the student's manual checkmarks in local storage and opens the next step. Returning to the same page on the same browser restores the saved progress.

A student can reopen a completed step and click the completion button again to mark it incomplete.

## Important distinction

A guided-step checkmark:

- tracks personal progress
- is stored in the current browser
- does not submit homework
- does not grade homework
- is not visible to the instructor as a submission

The student must use the separate **Submit work** area to send Hands-On, Research, and LinkedIn deliverables to the instructor.

## Reduced information density

Version 16 removes the large repeated project-context and page-explanation sections from the weekly workflow. Objectives, tools, prerequisites, and learning resources are now inside one expandable **Before you begin** card.

Research steps are displayed as expandable items. LinkedIn guidance appears only inside the LinkedIn workspace. Submission cards appear only inside the Submit workspace.

## Files changed

- `templates/week_detail.html`
- `templates/base.html`
- `static/app.js`
- `static/styles.css`

## GitHub upload

Upload the complete repository or replace the changed files above.

Suggested commit message:

```text
Simplify weekly labs with focused step-by-step workflow
```

## PythonAnywhere

```bash
cd ~/LearningPortal
rm -rf __pycache__
git pull origin main
workon coaching-env
python -m py_compile app.py guided_labs.py curriculum_data.py migrate_v14.py migrate_v15.py
```

Then reload the web app from the PythonAnywhere Web tab.

No database migration is required.
