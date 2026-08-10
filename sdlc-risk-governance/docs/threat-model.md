# Threat Model: expense-approval-service

STRIDE-based threat model, completed at the Plan & Design stage, before
any of the code in `demo-app/` existed. This is the artifact cited as
evidence in the Control Matrix's Plan & Design row.

**Scope:** a small internal API exposing two functions, employees look up
the status of an expense claim, and a rule-based check approves or
rejects claims automatically.

## Assets

- Expense records (employee name, amount, approval status)
- The approval decision logic itself
- Credentials the service uses to reach its own database and any
  downstream payment processor

## STRIDE Analysis

| Threat | Applies to this service | Design-time mitigation planned |
|---|---|---|
| **Spoofing** | An attacker impersonates a legitimate employee to look up or approve claims that aren't theirs | Require authenticated sessions on every route; no anonymous access to `/expense/<id>` or `/approve` |
| **Tampering** | Expense ID or approval rule input is manipulated to reach unintended data or logic | Parameterized queries only; approval rules evaluated through a fixed, non-executable comparison, not dynamic code evaluation |
| **Repudiation** | An employee or approver denies having submitted or approved a claim | Every approval action logged with actor identity and timestamp, immutable audit trail |
| **Information Disclosure** | Expense records, framework version, or credentials leak through error messages, headers, or overly broad query results | Generic error responses to clients; security headers set on every response; no secrets in source or environment files committed to version control |
| **Denial of Service** | A flood of lookups or malformed input degrades or crashes the service | Rate limiting at the gateway; input validation before any lookup reaches the database layer |
| **Elevation of Privilege** | A standard employee reaches approval authority they shouldn't have, or arbitrary code executes through the approval logic | Approval logic must be a fixed rule set, never dynamically evaluated code; role checks enforced server-side on every approval request |

## What the demo intentionally violates

This threat model describes what the service *should* do. `demo-app/` was
then built to intentionally violate several of these mitigations, so the
downstream gates (secret scan, SAST, SCA, DAST, log anomaly detection)
would have something real to catch:

- **Tampering / Elevation of Privilege**: the approval rule is evaluated
  with `eval()` on user-supplied input, and the expense lookup uses
  string-concatenated SQL, both direct violations of the Tampering and
  Elevation of Privilege mitigations above.
- **Information Disclosure**: hardcoded API key and database password
  committed to source; no security headers set; the server header
  discloses framework and Python version.
- **Denial of Service**: pinned dependency versions with known DoS CVEs
  (Flask, Werkzeug) left unpatched.

This gap between the threat model and the actual demo code is
deliberate. It's what the rest of the gates in this repo exist to catch
before any of it reaches production.

## Sign-off

Reviewed and approved by [Eng Lead], [Date], prior to Develop-stage work
beginning.

---

*Part of the [GRC Toolkit](https://github.com/ebohc/grc-toolkit), specifically the [Technology Risk Governance Across the SDLC](../) worked example.*
