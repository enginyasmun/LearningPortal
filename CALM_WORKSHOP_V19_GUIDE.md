# Version 19 — "Calm Workshop"

A complete redesign — not a retheme. Every template and the entire stylesheet
were rewritten from scratch. The old 169KB CSS is replaced by a ~35KB system.

## Design direction

Modeled on the current gold standard of product design (Linear, Vercel, Notion):
**calm, simple, informative.** Every element must earn its place.

- **One accent color.** Evergreen `#0d8a5f` for actions and progress. Amber and
  red appear only as status signals.
- **Hairline borders, no shadows, no gradients.** Panels are flat white cards
  on a warm paper background (`#fcfcfa`).
- **One typeface.** Inter for everything; JetBrains Mono for numbers, week
  indices, and terminal commands.
- **Progressive disclosure.** Dashboards lead with one number and one next
  action. Detail lives one click deeper (details/summary drawers, accordions,
  tabs).
- **Signature element: the week strip.** A 16-segment progress strip shows
  where the classroom is in the program — on the student dashboard and every
  week workspace.

## What changed per page

- **Landing** — type-driven hero, stat band, three-column program summary,
  four-phase timeline. No stock imagery, no fake product mockups.
- **Login** — single centered card.
- **Student dashboard** — week strip, "Next up" card with one primary action,
  quiet stat line, milestone grid, filterable assignment table.
- **Instructor dashboard** — stat line, recent-activity table, classroom-model
  note. Marketing blocks removed.
- **Week workspace** — cleaner header with saved-progress meter, underline
  tabs (Build / Research / LinkedIn / Submit), sticky step navigator, dark
  terminal command cards, quality gate. All step tracking behavior unchanged.
- **Curriculum** — phase strip + a clean 16-row list. Week overview pages show
  the three streams (lesson / research / LinkedIn) and prev/next navigation.
- **Projects** — each project as one panel with a four-phase milestone map.
- **Submissions / grading** — two-column review layout: work on the left,
  sticky grade form on the right.
- **Manage pages** — simple forms + roster tables with live search.
- **Profile** — split layout: identity + upload on the left, portrait picker
  on the right.

## What did NOT change

- **No database changes.** V19 is design-only. Do not run any migration.
- All routes, form fields, and endpoints are identical.
- `app.js` is untouched — every interactive behavior (sidebar, ⌘K palette,
  tables, guided lab steps, avatar preview) works against the new markup.

## Deploy

1. Upload the repository contents to GitHub (replace existing files).
2. On PythonAnywhere:
   ```
   cd ~/LearningPortal
   rm -rf __pycache__
   git pull origin main
   ```
3. Web tab → **Reload**.
4. Hard refresh the browser (`Ctrl+F5`). The stylesheet is versioned `?v=19`.

> Note: `static/avatars/realistic-*.png` live only in the deployed repo —
> do not delete them when uploading.
