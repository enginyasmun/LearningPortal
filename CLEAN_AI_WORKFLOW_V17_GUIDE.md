# LearningPortal Version 17

Version 17 makes the weekly learning page easier to focus on and introduces two dedicated AI-engineering weeks.

## Cleaner weekly page

The weekly page now uses:

- one compact week summary instead of a large promotional hero
- four simple work tabs: Build, Research, LinkedIn, and Submit
- only one visible workspace at a time
- one guided build step at a time
- a vertical step navigator on desktop
- a compact preparation drawer for objectives, tools, prerequisites, and resources
- clear manual completion language
- separate submission actions so students do not confuse a progress checkmark with homework submission

Students manually click **Mark step complete** after completing the actions, confirming the checkpoint, and saving the evidence. The browser saves those step checkmarks locally. A step checkmark does not submit work and does not create a grade.

## Dedicated AI engineering sequence

### Week 14: Claude AI and Salesforce CLI Development Workflow

Students learn to:

- install and verify Claude Code
- install and verify Salesforce CLI
- create a bounded AI task
- define repository instructions in `CLAUDE.md`
- protect secrets and customer data
- use Claude plan mode before editing
- review every requested tool or command
- compare AI reasoning with deterministic CLI output
- retrieve source, run tests, run Code Analyzer, and validate deployment using Salesforce CLI
- review and correct the complete AI-generated diff
- document hallucinations, security issues, failed commands, corrections, and final human decisions
- open a reviewed pull request with AI-use disclosure

### Week 15: MCP Servers, Secure Tool Use, and Agent Skills

Students learn to:

- explain MCP clients, servers, prompts, resources, and tools
- draw the authentication, data, tool, and approval architecture
- connect only instructor-approved project-scoped servers
- begin with read-only tools
- inventory tool schemas and side effects
- compare an MCP operation with the equivalent direct Salesforce CLI command
- execute one narrow human-approved tool action
- deny an out-of-scope action
- test authentication, permission, timeout, bad-input, and unavailable-server failures
- create a reusable skill or instruction
- remove unused access and create a security review

### Week 16: Agentforce, AI Governance, and Final Production Demonstration

Students combine the full application with:

- Agentforce grounding and instructions
- narrow Flow and Apex actions
- permission-aware execution
- confirmation before state changes
- prompt-injection and guardrail tests
- monitoring and human escalation
- final Salesforce CLI tests, Code Analyzer, and deployment validation
- Claude and MCP governance evidence
- a production-style classroom demonstration

## Required files

Version 17 changes or adds:

- `curriculum_data.py`
- `guided_labs.py`
- `seed.py`
- `migrate_v17.py`
- `templates/week_detail.html`
- `templates/base.html`
- `templates/curriculum.html`
- `templates/projects.html`
- `static/styles.css`
- `CLEAN_AI_WORKFLOW_V17_GUIDE.md`

## GitHub upload

Upload the complete extracted project to the root of:

`enginyasmun/LearningPortal`

Suggested commit message:

`Clean weekly workspace and add Claude CLI MCP training`

## PythonAnywhere update

```bash
cd ~/LearningPortal
rm -rf __pycache__
git pull origin main
workon coaching-env
python migrate_v17.py
python -m py_compile \
  app.py \
  guided_labs.py \
  curriculum_data.py \
  migrate_v14.py \
  migrate_v15.py \
  migrate_v17.py
```

Then open the PythonAnywhere **Web** tab, click **Reload**, open the portal, and press `Ctrl + F5`.

## Database safety

The migration creates a timestamped backup and preserves existing classrooms, users, submissions, scores, feedback, and file references.

Do not delete `academy.db`.

Do not run:

```bash
RESET_DB=1 python seed.py
```
