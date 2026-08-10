# expense-approval-service

Intentionally flawed internal Flask API, built solely to be scanned as
part of the SDLC governance-gate demo one level up in this repo.

**Do not deploy this anywhere real.** It contains a hardcoded live-format
API key, a hardcoded password, a string-concatenated SQL query, and an
`eval()` call on user-supplied input, on purpose, so the six governance
gates in `../scans/` have something real to catch.

`app.py` is the real target (Flask). `run_stdlib_server.py` is a
dependency-free stand-in that serves the same vulnerable route for
environments without package registry access. `seed_db.py` populates a
throwaway SQLite database with two sample rows.
