# Version 15: Git and GitHub First

The first two weeks are now a required source-control readiness gate.

## Week 1
Individual Git Foundations Portfolio: install and configure Git, learn repository states, create meaningful commits, inspect history, branch, merge, undo safely, and publish a personal repository.

## Week 2
Classroom GitHub and Salesforce DX workflow: clone in VS Code, inspect DX structure, authenticate the org without committing secrets, create a feature branch, commit a safe change, push, open a draft pull request, review a peer, address feedback, resolve a controlled conflict, merge, and synchronize main.

The industry application starts in Week 3.

## Install
Upload all files to GitHub, then run:

```bash
cd ~/LearningPortal
rm -rf __pycache__
git pull origin main
workon coaching-env
python migrate_v15.py
python -m py_compile app.py guided_labs.py curriculum_data.py migrate_v14.py migrate_v15.py
```

Reload the PythonAnywhere web app and hard refresh the browser. Do not reset or delete academy.db.
