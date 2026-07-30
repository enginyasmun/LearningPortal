# LearningPortal Avatar Upgrade

This package is prepared for `enginyasmun/LearningPortal`.

## What is included

- `avatars/realistic-male-01.png` through `realistic-male-05.png`
- `avatars/realistic-female-01.png` through `realistic-female-05.png`
- `static/images/default-avatar.webp`
- `AVATAR_PREVIEW.jpg`

The portrait filenames exactly match the `AVATAR_PRESETS` entries already used by
`app.py`. No Python, template, route, database, or migration change is required.

## Upload to GitHub

Upload the contents while preserving the folder structure:

```text
avatars/
static/images/default-avatar.webp
```

Choose **Replace files** when GitHub warns that the avatar files already exist.

Suggested commit message:

```text
Replace preset avatars with professional portraits
```

## Pull into PythonAnywhere

After committing the files to the `main` branch, run:

```bash
cd ~/LearningPortal && git pull origin main && touch /var/www/enginyasmun_pythonanywhere_com_wsgi.py
```

Then refresh the site with `Ctrl + F5`.

## Technical details

- Preset portraits: optimized PNG, 400 × 400 pixels
- Default avatar: optimized WebP, 400 × 400 pixels
- Existing user selections continue working because filenames are unchanged
