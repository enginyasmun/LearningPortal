# Salesforce Junior Developer Academy

A complete Flask website for running a 16-week Salesforce junior developer academy.

## Program model

Each student selects one of five industry projects and builds that same Salesforce application for all 16 weeks.

Every week includes:

- one step-by-step hands-on guided lab
- one research homework assignment
- one LinkedIn post assignment

Each student receives 48 active assignments:

- 15 weekly hands-on project milestones
- 1 final application assignment in Week 16
- 16 research assignments
- 16 LinkedIn assignments

## Website features

- modern responsive landing, login, curriculum, and guided-lab pages
- student and instructor authentication
- academy administrator and regular instructor access levels
- student-to-instructor assignment
- private instructor review queues
- student project selection
- guided Trailhead-style build instructions
- research training and source-quality checks
- weekly LinkedIn workflow
- file uploads, repository links, submissions, grading, revisions, and feedback
- SQLite database

## Required Python packages

```bash
pip install -r requirements.txt
```

## Fresh installation

Follow `PYTHONANYWHERE_FRESH_SETUP.md`.

## Development credentials

`seed.py` uses environment variables when provided. Without them, the local development defaults are:

- Instructor: `admin@example.com` / `Admin123!`
- Student: `student@example.com` / `Student123!`

Set your own instructor credentials before running `seed.py` on a public website.


## Curriculum and project plans

The Curriculum section provides the common 16-week class syllabus for every student. Project Plans contain the five industry-specific, step-by-step guided build tracks.


## Version 11

Version 11 increases readability across the portal, modernizes the guided project-plan experience, and adds ten built-in profile avatar choices while retaining custom photo uploads.


## Version 15 Git readiness gate

Weeks 1 and 2 teach Git, GitHub, VS Code source control, pull requests, review, merge conflicts, and the Salesforce DX repository workflow before industry development begins in Week 3.

## Version 16 focus mode

Weekly guided project pages now show one workspace and one build step at a time. Step completion is manually confirmed by the student and automatically saved in the current browser. Lab checkmarks do not replace assignment submission. See `FOCUS_MODE_V16_GUIDE.md`.

## Version 17: clean focus mode and two dedicated AI weeks

The weekly project page now presents one workspace and one guided step at a time. Week 14 is dedicated to Claude AI plus Salesforce CLI, Week 15 is dedicated to MCP servers and secure tool orchestration, and Week 16 completes the governed Agentforce application. Run `python migrate_v17.py` after updating an existing installation.

## Version 18: Expedition design and refreshed AI curriculum

Version 18 replaces the purple software theme with an evergreen-and-campfire Expedition identity, new typography (Bricolage Grotesque, Inter, and JetBrains Mono for terminal blocks), trail-style progress bars, visible keyboard focus, and reduced-motion support. Curriculum content is modernized: Week 2 adds GitHub Actions CI basics, Week 10 adds AI-assisted code review with human verification, and Weeks 14–16 are refreshed with CLAUDE.md instructions, plan mode, agent skills, MCP OAuth and tool permissions, and the Agentforce Testing Center. Run `python migrate_v18.py` after updating an existing installation. See `EXPEDITION_DESIGN_V18_GUIDE.md`.
