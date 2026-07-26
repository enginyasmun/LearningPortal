# Version 22 — Self-registration with approval

Students can now create their own accounts, but **nobody enters the academy
until an instructor approves them and assigns a classroom.**

## How it works

1. A visitor clicks **Create account** (landing page, top nav, or the sign-in
   page) and fills in `/register`: name, email, password (min 8 characters,
   confirmed), optionally the classroom they think they belong to, and an
   optional note to the instructor.
2. The account is saved with `approval_status='pending'` and **no classroom**.
   They see a confirmation page explaining the three steps that follow.
3. If they try to sign in before approval they get a clear message:
   *"Your registration is still waiting for academy approval."* They cannot
   reach any page of the app.
4. You see an amber **"N students waiting for approval"** banner on your
   dashboard and a badge on the new **Registrations** item in the sidebar.
5. On **Registrations** you review each request (name, email, when they
   registered, the classroom they asked for, their note) and either:
   - **Approve** — you must pick a classroom; this places them, marks them
     approved, and records who decided and when. They can sign in immediately.
   - **Decline** — with an optional reason that is shown to them at sign-in.
     Declined accounts are also deactivated.
6. Recent decisions are listed underneath with a **Reopen** button that puts a
   declined person back in the pending queue.

## Rules enforced

- Duplicate emails, invalid emails, short passwords, and mismatched passwords
  are all rejected with specific messages.
- Approving requires an active classroom you manage. Administrators can use any
  classroom; a plain instructor can only approve into their own.
- Students get **403** on every approval endpoint.
- If you revoke someone's approval while they are signed in, their next click
  signs them out with an explanation.
- Re-approving an already-approved student is a safe no-op (it will not
  overwrite their existing classroom).
- Accounts you create manually under **Students** or **Instructors** are
  approved automatically — that flow is unchanged.
- All existing accounts are marked approved by the migration, so nobody who can
  sign in today is locked out.

## Database change — migration required

This release adds columns to `users`:
`approval_status`, `requested_classroom_id`, `registration_note`,
`registered_at`, `decision_at`, `decision_by`, `rejection_reason`.

`migrate_v22.py` backs up the database first and is safe to run more than once.
If you deploy the code and forget the migration, the app keeps working normally
and simply tells you to run it — it will not crash.

## Deploy

1. Upload the repository contents to GitHub (keep `static/avatars/`).
2. On PythonAnywhere:
   ```
   cd ~/LearningPortal
   rm -rf __pycache__
   git pull origin main
   python migrate_v22.py
   ```
3. Web tab → **Reload**.
4. Hard refresh with `Ctrl+F5` (stylesheet is now `?v=22`).

Test it end to end: open `/register` in a private window, submit a request,
then approve it from your admin account and sign in as that new student.
