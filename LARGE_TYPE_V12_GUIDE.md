# Version 12: Large-screen readability

This release increases the default typography and spacing across the complete portal. It is designed for normal browser zoom on a large desktop monitor.

## Main changes

- Base text increased to 18 px on desktop
- Guided-lab actions increased to 15 px
- Lab overview lists increased to 14 px
- Step titles increased to 25 px
- Command blocks increased to 14 px
- Research and LinkedIn instructions increased to 14 px
- Tables, forms, navigation, buttons, and dashboard supporting text enlarged
- Reading width reduced to improve line length
- Static CSS and JavaScript URLs include Version 12 cache-busting parameters

## GitHub

Upload the complete package or replace these files:

- `static/styles.css`
- `templates/base.html`

Suggested commit message:

`Increase portal typography for large-screen readability`

## PythonAnywhere

```bash
cd ~/LearningPortal
git pull origin main
workon coaching-env
python -m py_compile app.py guided_labs.py curriculum_data.py seed.py
```

Reload the Web app. The `?v=12` asset version should prevent the previous stylesheet from remaining cached.

No database migration is required.
