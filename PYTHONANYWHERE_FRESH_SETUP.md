# Fresh LearningPortal Setup

## Upload to GitHub

Upload every file and folder from this package to:

`enginyasmun/LearningPortal`

Do not upload only the ZIP file.

## Clone on PythonAnywhere

```bash
cd ~
rm -rf LearningPortal
git clone https://github.com/enginyasmun/LearningPortal.git
cd LearningPortal
workon coaching-env
pip install -r requirements.txt
```

## Create a fresh database

Use this only for a new installation:

```bash
export ADMIN_NAME='Engin Yasmun'
export ADMIN_EMAIL='YOUR_EMAIL_ADDRESS'
export ADMIN_PASSWORD='YOUR_NEW_STRONG_PASSWORD'
python seed.py
```

The fresh database creates one demo classroom with one instructor, one student, and the Warehouse Management & Logistics project.

## WSGI configuration

```python
import os
import sys

PROJECT_HOME = "/home/enginyasmun/LearningPortal"
if PROJECT_HOME not in sys.path:
    sys.path.insert(0, PROJECT_HOME)

os.environ["SECRET_KEY"] = "REPLACE_WITH_A_LONG_RANDOM_SECRET"

from app import app as application
```

Set the PythonAnywhere static mapping to:

- URL: `/static/`
- Directory: `/home/enginyasmun/LearningPortal/static`

Set the virtual environment to:

`/home/enginyasmun/.virtualenvs/coaching-env`

Click Reload.

## Existing database

For an existing installation, do not run `seed.py`. Run:

```bash
python migrate_v14.py
```

The migration creates a timestamped backup before changing the schema.
