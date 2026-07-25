# Visual Experience Version 9

This complete package adds:

- larger typography and more comfortable spacing
- a visual project-plans page with four readable phases per project
- generated learning illustrations on dashboard, project plans, and guided labs
- profile-picture upload for students and instructors
- profile settings for name and sign-in email
- automatic hiding of placeholder email text in instructor selection
- automatic database upgrade that adds `avatar_filename` without deleting data

## Upload

Upload every file and folder in this package to the root of `enginyasmun/LearningPortal` and replace existing files.

Suggested commit message:

`Add visual learning experience and profile avatars`

## PythonAnywhere

```bash
cd ~/LearningPortal
git pull origin main
workon coaching-env
pip install -r requirements.txt
python -m py_compile app.py guided_labs.py curriculum_data.py seed.py
```

Reload the web app and hard refresh with `Ctrl + F5`.

No database reset and no manual migration are required. The application adds the new avatar column automatically when it starts.

## Fix the placeholder email

After signing in, click your picture or **Profile settings**. Replace `YOUR_EMAIL_ADDRESS` with your real email and save.
