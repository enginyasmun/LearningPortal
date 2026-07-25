# Version 14: Classrooms and Real Integrations

## Correct program model

- One classroom has one instructor.
- A classroom can contain multiple students.
- One project is assigned to the entire classroom.
- Students submit individual work and receive private grades and feedback.
- Regular instructors see only their classrooms.
- Academy administrators see and manage all classrooms.

## Classroom workflow

1. Create an instructor account.
2. Open **Classrooms**.
3. Create a classroom.
4. Assign one instructor and one project to the classroom.
5. Add multiple students to that classroom.
6. Every student sees the same project roadmap and guided labs.

## Project changes

The lending project has been removed. Project 1 is now:

**Warehouse Management & Logistics App**

The Manufacturing project is now focused on production and quality so it does not duplicate the warehouse project.

## Real Week 11 callouts

Week 11 now requires a real API call from the Salesforce training org through a Named Credential.

- Warehouse: Zippopotam.us Postal Code API
- Healthcare: CMS NPI Registry API
- Nonprofit: US Census Geocoding Services
- Manufacturing: NHTSA vPIC API
- Professional Services: GitHub REST API

Students must provide evidence of a genuine HTTP response and a mapped Salesforce record. `HttpCalloutMock` is used only inside automated Apex tests.

## Update an existing PythonAnywhere installation

```bash
cd ~/LearningPortal
git pull origin main
workon coaching-env
pip install -r requirements.txt
python migrate_v14.py
python -m py_compile app.py guided_labs.py curriculum_data.py seed.py migrate_v14.py
```

Then click **Reload** on the PythonAnywhere Web tab and press `Ctrl + F5`.

## Migration behavior

The migration:

- creates a timestamped database backup
- creates the `classrooms` table
- adds `classroom_id` to students
- groups existing students by old class, instructor, and project
- preserves accounts, submissions, grades, feedback, and file references
- replaces the lending project with warehouse management
- refreshes all 80 project milestones

Do not run `RESET_DB=1 python seed.py` on an existing site.
