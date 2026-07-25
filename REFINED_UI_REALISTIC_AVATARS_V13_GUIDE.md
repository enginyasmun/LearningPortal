# LearningPortal Version 13

Version 13 refines the large-text design without making the project phase cards unnecessarily tall.

## Included

- wider desktop sidebar
- larger navigation and profile text
- shorter and denser four-phase project cards
- preserved readable 16-week roadmap cards
- improved Students form, instructor dropdown, and roster typography
- ten new semi-realistic avatar portraits
- larger two-row avatar selection gallery
- custom profile-picture upload remains available
- stylesheet and JavaScript cache-busting set to Version 13

## GitHub

Upload everything in this folder to the root of `enginyasmun/LearningPortal` and replace existing files.

Suggested commit message:

`Refine project density sidebar and realistic avatars`

## PythonAnywhere

```bash
cd ~/LearningPortal
git pull origin main
workon coaching-env
python -m py_compile app.py guided_labs.py curriculum_data.py seed.py
```

Reload the PythonAnywhere web app and press `Ctrl + F5`.

No database migration is required. Do not delete `academy.db` and do not run a reset seed.
