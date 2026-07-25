# LearningPortal Version 11

This complete release improves readability and visual polish while preserving the Version 10 curriculum and guided-project separation.

## Main improvements

- Larger text across navigation, tables, forms, cards, dashboards, and project plans
- Larger text inside the expanded 16-week milestone cards
- More expressive four-phase project layout
- Improved whitespace, contrast, hover states, and subtle motion
- Ten built-in illustrated avatar options: five male and five female
- Custom photo upload remains available
- No database migration is required

## Deployment

Upload every file and folder from this project to the root of `enginyasmun/LearningPortal`.

Suggested commit message:

`Improve readability and add ten profile avatars`

On PythonAnywhere:

```bash
cd ~/LearningPortal
git pull origin main
workon coaching-env
pip install -r requirements.txt
python -m py_compile app.py guided_labs.py curriculum_data.py seed.py
```

Then reload the web app and press Ctrl + F5.

Do not delete `academy.db` and do not run `RESET_DB=1 python seed.py`.

The bundled `avatars/avatar-*.svg` files must be committed. Custom user-uploaded avatar files remain ignored.
