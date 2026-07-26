# Version 23 — Avatar fix and the ten portraits

## The bug

Every avatar in the portrait picker looked identical. Two causes:

1. **Wrong URL in the profile template.** The picker linked to
   `/static/avatars/<file>`, but the app serves portraits from `/avatars/<file>`
   through its `avatar_file` route. Every image returned 404.
2. **A fallback was hiding it.** An `onerror` handler swapped each broken image
   for `default-avatar.webp`, so all ten tiles showed the same default face.

Fixed: the picker now uses the app's own `avatar_src()` helper, so it always
matches the serving route. The masking fallback is gone, so a genuinely missing
file is visible instead of silently uniform.

## The ten portraits

`avatars/` now ships all ten preset portraits, generated at 400x400 with
transparent rounded edges and a soft radial background:

| Male | Female |
| --- | --- |
| 01 dark hair, glasses, navy | 01 long wavy dark hair, plum |
| 02 buzz cut, teal | 02 afro, mustard |
| 03 side part, beard, gray | 03 long fair hair, blue |
| 04 dark hair, burgundy | 04 hair in a bun, teal |
| 05 fair hair, glasses, green | 05 auburn hair, glasses, forest |

Each has a distinct skin tone, hair style and color, clothing color, and
background tint.

`tools/make_avatars.py` regenerates the whole set if you ever want to tweak
colors or add more:

```bash
python tools/make_avatars.py
```

Then raise the `range(1, 6)` values in `AVATAR_PRESETS` in `app.py` if you add
portraits beyond ten.

## Also in this release

- The **Create account** button in the public nav had unreadable gray-on-green
  text (a CSS specificity conflict with `.pub-nav a`). Fixed.
- On sign-in and register pages the flash message sat on a detached white strip
  above the card; the auth pages now share one backdrop and the message is
  centered to the card width with a dismiss button.
- The register card is wider with a 1-2-3 flow strip, and the password
  placeholders no longer clip.

No database migration in this release. If you have not yet run the version 22
step, run it now:

```bash
cd ~/LearningPortal
rm -rf __pycache__
git pull origin main
python migrate_v22.py     # only if you have not run it before
```

Reload the web app, then `Ctrl+F5` (assets are versioned `?v=23`).

> When uploading to GitHub, include the whole `avatars/` folder. `.gitignore`
> already whitelists `avatars/realistic-*.png`, so the portraits are tracked
> while student uploads stay out of the repository.
