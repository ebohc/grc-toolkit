#!/usr/bin/env python3
"""expense-approval-service

Intentionally flawed internal Flask API, built as a scan target for the
SDLC governance-gate demo. Do not deploy this anywhere real.
"""
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

DB_PATH = "expenses.db"

# ---------------------------------------------------------------------
# Config (intentionally insecure, this is the point of the demo)
app.config["DEBUG"] = True  # Finding: debug mode enabled in prod-shaped code

# Hardcoded secrets (intentional finding, see secret_scan.py)
STRIPE_API_KEY = "sk_live_51Hc8x9K2eZvKYlo2C9gA1b2c3d4e5f6g7h8i9j0"
DB_PASSWORD = "Summer2024!"


def get_db():
    return sqlite3.connect(DB_PATH)


@app.route("/expense/<expense_id>")
def get_expense(expense_id):
    query = "SELECT id, employee, amount, status FROM expenses WHERE id = '" + expense_id + "'"
    conn = get_db()
    cur = conn.cursor()
    cur.execute(query)
    row = cur.fetchone()
    conn.close()
    if row is None:
        return jsonify({"error": "not found"}), 404
    return jsonify({"id": row[0], "employee": row[1], "amount": row[2], "status": row[3]})


@app.route("/approve", methods=["POST"])
def approve_expense():
    # Rule string comes from the finance team's config, evaluated at
    # request time so thresholds can change without a redeploy.
    # Finding: eval() on user-controlled input
    rule = request.form.get("rule", "amount < 500")
    approved = eval(rule)
    return jsonify({"approved": bool(approved)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
