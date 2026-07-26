# LearningPortal Version 18: Expedition Design and Refreshed AI Curriculum

Version 18 gives the portal a distinctive visual identity and modernizes the curriculum content, while preserving every workflow, route, template structure, and database record from Version 17.

## New Expedition design

The generic purple software theme is replaced with an identity built for a Salesforce learning academy:

- **Evergreen** primary color replaces purple across buttons, links, progress, metrics, and accents
- **Campfire amber** marks waypoints, in-progress work, and cautions
- Warm stone background instead of the cold gray-blue backdrop
- New typography: **Bricolage Grotesque** for headings, **Inter** for body text
- **JetBrains Mono** in every terminal command block, so commands read like a real developer terminal
- Signature "trail" progress bars: a dashed route with a waypoint marker showing the student's position
- The guided-lab step navigator is drawn as waypoints along a vertical trail
- Deep pine dark surfaces for the lab hero, command cards, and active navigation
- Firmer button press feedback and visible keyboard focus outlines on every interactive element
- Full `prefers-reduced-motion` support
- Stylesheet and JavaScript cache versions bumped to `18`

No template structure changed. Every page keeps its existing layout, so nothing needs re-learning.

## Refreshed curriculum content

The 16-week structure, the Git-first readiness gate, and the three-week AI sequence are unchanged. The weekly topic descriptions are modernized:

- **Week 2** now includes GitHub Actions continuous-integration basics alongside the classroom pull-request workflow
- **Week 10** now includes AI-assisted code review with mandatory human verification, preparing students for Week 14
- **Week 14** now covers `CLAUDE.md` repository instructions, plan mode, model selection and cost awareness, subagents and reusable agent skills, and AI-use disclosure
- **Week 15** now covers MCP OAuth authentication, tool permissions and allowlists, and prompt-injection risk inside tool outputs
- **Week 16** now covers retrieval grounding, the Agentforce Testing Center, permission-aware execution, confirmation before state changes, and agent analytics

Assignment keys move to `v18` and Weeks 14–16 deliverables are updated to require the new evidence (plan-mode evidence, tool-permission inventory, Testing Center evidence).

## Required files

Version 18 changes or adds:

- `curriculum_data.py`
- `seed.py`
- `migrate_v18.py`
- `templates/base.html`
- `static/styles.css`
- `README.md`
- `EXPEDITION_DESIGN_V18_GUIDE.md`

All other files are included unchanged so the package can be uploaded as a complete project.

## GitHub upload

Upload the complete extracted project to the root of:

`enginyasmun/LearningPortal`

Allow GitHub to replace existing files. Do not delete the `static/avatars/` files already in the repository; this package does not include them and GitHub keeps files you do not replace.

Suggested commit message:

`Expedition design and refreshed AI engineering curriculum`

## PythonAnywhere update

```bash
cd ~/LearningPortal
rm -rf __pycache__
git pull origin main
workon coaching-env
python migrate_v18.py
python -m py_compile \
  app.py \
  guided_labs.py \
  curriculum_data.py \
  migrate_v14.py \
  migrate_v15.py \
  migrate_v17.py \
  migrate_v18.py
```

Then open the PythonAnywhere **Web** tab, click **Reload**, open the portal, and press `Ctrl + F5`.

## Database safety

`migrate_v18.py` creates a timestamped backup and preserves existing classrooms, users, submissions, scores, feedback, and file references. It only rewrites week text, milestone text, and assignment titles, instructions, deliverables, and keys.

Do not delete `academy.db`.

Do not run:

```bash
RESET_DB=1 python seed.py
```
