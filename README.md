# Salesforce Developer Academy LearningPortal

A Flask-based learning portal for a 16-week junior Salesforce developer academy.

## Classroom model

The academy is organized around classrooms:

- One classroom has one instructor.
- A classroom can have multiple students.
- One project is assigned to the whole classroom.
- Students submit individual homework and receive private grades and feedback.
- The instructor sees only their classrooms unless they are an academy administrator.

## Project choices

1. Warehouse Management & Logistics
2. Patient Referral & Care Coordination
3. Donor & Volunteer Engagement
4. Production & Quality Operations
5. AI-Enabled Client Delivery

Each classroom follows one complete 16-week guided project plan.

## Weekly learning rhythm

Every student completes 48 deliverables:

- 16 classroom-project build milestones, including the final application
- 16 research assignments
- 16 LinkedIn assignments

## Real integrations

Week 11 now requires a genuine Salesforce callout through a Named Credential. Each project includes a safe training API:

- Warehouse: Zippopotam.us postal-code validation
- Healthcare: CMS NPI Registry
- Nonprofit: US Census Geocoding Services
- Manufacturing: NHTSA vPIC
- Professional Services: GitHub REST API

The runtime lab performs a real HTTP call. `HttpCalloutMock` is used only inside automated Apex tests.

## Existing site update

Run:

```bash
cd ~/LearningPortal
git pull origin main
workon coaching-env
python migrate_v14.py
```

Then reload the PythonAnywhere web app. The migration creates a timestamped database backup.

## Fresh installation

```bash
export ADMIN_NAME='Your Name'
export ADMIN_EMAIL='you@example.com'
export ADMIN_PASSWORD='A strong password'
python seed.py
```

Do not run `RESET_DB=1 python seed.py` on an existing installation.
