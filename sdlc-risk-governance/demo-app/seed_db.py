#!/usr/bin/env python3
"""Seeds a throwaway SQLite database with a few sample expense rows so
app.py / run_stdlib_server.py have something real to query. Not part of
the security surface being scanned, just fixture data."""
import sqlite3

conn = sqlite3.connect("expenses.db")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS expenses")
cur.execute("""
    CREATE TABLE expenses (
        id TEXT PRIMARY KEY,
        employee TEXT NOT NULL,
        amount REAL NOT NULL,
        status TEXT NOT NULL
    )
""")
cur.executemany(
    "INSERT INTO expenses VALUES (?, ?, ?, ?)",
    [
        ("1001", "J. Alvarez", 87.50, "approved"),
        ("1002", "T. Nguyen", 214.00, "pending"),
    ],
)
conn.commit()
conn.close()
print("expenses.db seeded with 2 rows.")
