#!/usr/bin/env python3
"""Stdlib stand-in for app.py, used only because this repo was built in an
offline sandbox without package registry access. Serves the same
/expense/<id> route with the same vulnerability, so the DAST and log
anomaly gates have something real to run against without needing Flask
installed. In a normal environment, run app.py directly instead.

This mirrors app.py's get_expense() logic, including the same
unparameterized query, exercising the same vulnerability class through
a dependency-free path.
"""
import sqlite3
import re
from http.server import BaseHTTPRequestHandler, HTTPServer

DB_PATH = "expenses.db"


def get_expense(expense_id):
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT id, employee, amount, status FROM expenses WHERE id = '" + expense_id + "'"
    cur = conn.cursor()
    cur.execute(query)
    row = cur.fetchone()
    conn.close()
    return row


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        m = re.match(r"^/expense/(.+)$", self.path)
        if not m:
            self.send_response(404)
            self.end_headers()
            return
        expense_id = m.group(1)
        try:
            row = get_expense(expense_id)
        except Exception:
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"error": "internal error"}')
            return
        if row is None:
            self.send_response(404)
            self.end_headers()
            return
        body = ('{"id": "%s", "employee": "%s", "amount": %s, "status": "%s"}'
                % (row[0], row[1], row[2], row[3])).encode()
        self.send_response(200)
        # Intentionally minimal headers, no CSP / HSTS / X-Frame-Options / X-Content-Type-Options
        self.send_header("Content-Type", "application/json")
        self.send_header("Server", "Werkzeug/0.14.1 Python/3.10.12")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        pass


if __name__ == "__main__":
    HTTPServer(("127.0.0.1", 5001), Handler).serve_forever()
