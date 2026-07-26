"""Rerunnable migration: student self-registration with instructor approval.

Adds approval columns to the users table. Every account that already exists is
marked 'approved' so nobody is locked out by this upgrade.
"""
from datetime import datetime, timezone
from pathlib import Path
import os
import shutil
import sqlite3

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = Path(os.environ.get("DATABASE_PATH", BASE_DIR / "academy.db"))

if not DB_PATH.exists():
    raise SystemExit(f"Database not found: {DB_PATH}")

stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
backup = DB_PATH.with_name(f"{DB_PATH.stem}_backup_before_v22_{stamp}{DB_PATH.suffix}")
shutil.copy2(DB_PATH, backup)

NEW_COLUMNS = (
    ("approval_status", "TEXT NOT NULL DEFAULT 'approved'"),
    ("requested_classroom_id", "INTEGER"),
    ("registration_note", "TEXT"),
    ("registered_at", "TEXT"),
    ("decision_at", "TEXT"),
    ("decision_by", "INTEGER"),
    ("rejection_reason", "TEXT"),
)

with sqlite3.connect(DB_PATH) as conn:
    conn.row_factory = sqlite3.Row

    existing = {row["name"] for row in conn.execute("PRAGMA table_info(users)")}
    added = []
    for column, definition in NEW_COLUMNS:
        if column not in existing:
            conn.execute(f"ALTER TABLE users ADD COLUMN {column} {definition}")
            added.append(column)

    # Any pre-existing account keeps working: it is already approved.
    conn.execute(
        "UPDATE users SET approval_status='approved' "
        "WHERE approval_status IS NULL OR TRIM(approval_status)=''"
    )

    conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_users_approval_status ON users(approval_status)"
    )
    conn.commit()

    counts = {
        row["approval_status"]: row["total"]
        for row in conn.execute(
            "SELECT approval_status, COUNT(*) AS total FROM users GROUP BY approval_status"
        )
    }

print(f"Migration completed: {DB_PATH}")
print(f"Backup created: {backup}")
print("Version 22: student self-registration with instructor approval")
if added:
    print("Columns added to users: " + ", ".join(added))
else:
    print("Columns already present - nothing to add (safe rerun)")
print("Account approval states: " + (", ".join(f"{k}={v}" for k, v in sorted(counts.items())) or "none"))
print("Existing accounts were all marked approved, so no one is locked out.")
