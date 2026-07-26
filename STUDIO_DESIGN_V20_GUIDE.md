# Version 20 — "Studio"

Apple-inspired redesign of the visual layer, replacing the flat V19 look.
Same page structure, completely new visual language modeled on apple.com:

- **Big, confident typography.** 34px page titles, a 72px landing headline
  with a gradient accent, Apple's #1d1d1f/#6e6e73 text palette on the
  classic #f5f5f7 canvas gray.
- **Soft layered depth.** Cards are large-radius (16–28px) white surfaces with
  real shadows that lift on hover — no hairline-border flatness.
- **Frosted glass.** The sidebar, top bar, and command palette use
  saturate+blur backdrop filters like Apple's navigation.
- **Pill buttons.** Rounded-full buttons; the primary action carries an
  emerald→teal gradient with a colored glow shadow.
- **Segmented-control tabs** in the week workspace (Build / Research /
  LinkedIn / Submit), exactly like iOS segmented controls.
- **Dark closing band** on the landing page with gradient headline text.
- **Colorful status system.** Type and status pills with tinted backgrounds;
  Final Project is purple, LinkedIn blue, Research warm brown.
- Terminal cards use Apple's #1d1d1f with a green "copied" state.

Design-only release — **no database migration**. Cache version bumped to
`?v=20`. Also added: avatar portrait images now fall back to the default
avatar if `static/avatars/` files are missing on the server.

## Deploy
1. Upload repository contents to GitHub (do not delete `static/avatars/`).
2. PythonAnywhere: `cd ~/LearningPortal && rm -rf __pycache__ && git pull origin main`
3. Web tab → Reload, then Ctrl+F5 in the browser.


## V21 addendum — "Gallery" visual layer

Added rich designed visuals on top of the Studio system (cache `?v=21`):

- **Landing page**: soft gradient blob backdrop behind the hero, a CSS-built
  product mockup (browser window showing the student dashboard) as the hero
  illustration, and gradient icon badges on the three feature cards.
- **Student dashboard**: emerald gradient welcome banner with the 16-week
  strip inside a frosted glass inset; colorful gradient stat icons.
- **Instructor dashboard**: gradient stat icons (classrooms, assignments,
  review clock, revisions).
- **Projects**: every project opens with its own gradient hero — blue for
  Warehouse & Logistics, teal for Healthcare, pink for Nonprofit, amber for
  Manufacturing, violet for Professional Services — each with a frosted
  industry icon.
- **Curriculum**: the four phase cards carry gradient icon badges (git branch,
  code, lightning, agent).
- **Week workspace**: deep forest-gradient banner header with frosted progress
  meter and week strip.

Still design-only. No migration. Deploy the same way, then Ctrl+F5.
