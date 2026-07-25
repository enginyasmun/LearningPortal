# Salesforce Developer Academy: Modern LearningPortal V8

A complete Flask learning portal for a 16-week Salesforce junior developer program. Version 8 includes a redesigned modern workspace while preserving the existing curriculum, guided labs, authentication, instructor assignment, grading, and project model.

See [`MODERN_UI_V8_GUIDE.md`](MODERN_UI_V8_GUIDE.md) for deployment instructions.

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
