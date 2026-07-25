# Fresh GitHub and PythonAnywhere Setup

This package is complete. You do not need any older update ZIP.

## Part 1: Upload the complete project to GitHub

1. Extract `Coaching_Complete_Modern_v7_GitHub_Ready.zip` on your computer.
2. Open your GitHub repository: `enginyasmun/Coaching`.
3. Remove old repository files if you want a completely clean installation.
4. Click **Add file**, then **Upload files**.
5. Select every extracted file and folder, including `templates`, `static`, `uploads`, and all root files.
6. Do not upload only the ZIP. GitHub does not automatically extract it.
7. Commit with this message:

```text
Install complete modern Salesforce Developer Academy
```

## Part 2: Clone the complete project on PythonAnywhere

Open a Bash console and run:

```bash
cd ~
rm -rf Coaching
git clone https://github.com/enginyasmun/Coaching.git
cd Coaching
```

## Part 3: Create the virtual environment

Run:

```bash
mkvirtualenv --python=/usr/bin/python3.13 coaching-env
pip install -r requirements.txt
```

If `coaching-env` already exists, use:

```bash
workon coaching-env
cd ~/Coaching
pip install -r requirements.txt
```

## Part 4: Create the database and your administrator

Choose your administrator email and a strong password. Then run:

```bash
cd ~/Coaching
workon coaching-env
export ADMIN_NAME='Engin Yasmun'
export ADMIN_EMAIL='YOUR_EMAIL_ADDRESS'
export ADMIN_PASSWORD='YOUR_NEW_STRONG_PASSWORD'
python seed.py
```

The database will be created at:

```text
/home/enginyasmun/Coaching/academy.db
```

Do not upload `academy.db` to GitHub.

## Part 5: Configure the PythonAnywhere web app

1. Open the PythonAnywhere **Web** tab.
2. Add a new web app or open the existing web app.
3. Select **Manual configuration** and Python 3.13.
4. Set the virtualenv path to:

```text
/home/enginyasmun/.virtualenvs/coaching-env
```

5. Open the WSGI configuration file.
6. Replace its contents with:

```python
import os
import sys

PROJECT_HOME = "/home/enginyasmun/Coaching"
if PROJECT_HOME not in sys.path:
    sys.path.insert(0, PROJECT_HOME)

os.environ["SECRET_KEY"] = "REPLACE_THIS_WITH_A_LONG_RANDOM_SECRET"

from app import app as application
```

7. Save the WSGI file.
8. Click **Reload** on the Web tab.

## Part 6: Test the website

Open:

```text
https://enginyasmun.pythonanywhere.com
```

Sign in with the administrator email and password used before running `python seed.py`.

Test these pages:

- landing page
- login page
- instructor dashboard
- project plans
- curriculum
- Week 5 guided lab
- students
- instructors
- submissions

## Updating later

After future GitHub changes, run:

```bash
cd ~/Coaching
git pull origin main
workon coaching-env
pip install -r requirements.txt
python -m py_compile app.py guided_labs.py curriculum_data.py
```

Then click **Reload** in PythonAnywhere.

## Important database warning

After the site contains real students or homework, never run:

```bash
RESET_DB=1 python seed.py
```

That command intentionally resets the database.
