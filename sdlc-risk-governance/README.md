# Technology Risk Governance Across the SDLC

A worked example of risk governance gates at every stage of the software
development lifecycle, backed by a small deliberately flawed demo service
and real (not staged) scan output. Every finding in the article is
actual tool output, verified by running the same scripts published here
against the same demo app published here.

## What's here

| File | What it is |
|---|---|
| [`article.md`](./article.md) | The full writeup, stage by stage, with the screenshots below embedded |
| [`SDLC-Risk-Governance-Control-Matrix.xlsx`](./SDLC-Risk-Governance-Control-Matrix.xlsx) | Control matrix mapping each SDLC stage to risks, controls, owners, and a framework crosswalk (NIST SSDF, OWASP SAMM, ISO/IEC 27034, NIST CSF 2.0), plus a 1-5 maturity model |
| [`docs/threat-model.md`](./docs/threat-model.md) | STRIDE threat model for the demo service, done at the Plan & Design stage, before the code below existed |
| [`demo-app/`](./demo-app) | `expense-approval-service`, an intentionally flawed internal Flask API (hardcoded secrets, SQL injection, `eval()` on user input, outdated pinned dependencies). Built solely to be scanned. Do not deploy it anywhere real |
| [`scans/`](./scans) | The governance-gate scripts run against the demo app at each stage: secret scan (Develop), SAST + SCA (Build), header check (Test), artifact integrity manifest (Release), log anomaly triage (Operate) |
| [`screenshots/`](./screenshots) | Captured terminal output from each gate actually running against the demo app |
| [`logs/access-sample.log`](./logs/access-sample.log) | Sample access log with normal traffic mixed with SQLi and path-traversal probes, used by the Operate-stage log anomaly check |
| [`linkedin-post.md`](./linkedin-post.md) | Companion post for the article |

## How to use it

- Rows in the Control Matrix marked with a Demo Reference show exactly which scan script and screenshot back that control up. Rows without one are template rows, meant for you to fill in with your own org's evidence.
- The Framework Crosswalk tab cross-references NIST SSDF, OWASP SAMM, ISO/IEC 27034, and NIST CSF 2.0, so one control satisfies more than one framework's evidence expectation at once.
- The Maturity Model tab is a 1-5 scoring rubric, score where each stage sits today versus a target.
- `demo-app/` and `scans/` are the worked example, the Plan & Design, Develop, Build, Test, Release, and Operate gates run against one small, intentionally flawed service, with captured output in `screenshots/`.

## Running it yourself

```
# from this folder
cd demo-app && python3 seed_db.py && cd ..

python3 scans/secret_scan.py demo-app
python3 scans/sast_scan.py demo-app
python3 scans/sca_check.py demo-app

(cd demo-app && python3 run_stdlib_server.py &)       # stdlib stand-in for Flask, must run from demo-app/
sleep 1
python3 scans/dast_headers.py http://127.0.0.1:5001/expense/1001
pkill -f run_stdlib_server.py

python3 scans/artifact_integrity.py demo-app
python3 scans/log_anomaly_check.py logs/access-sample.log
```

`run_stdlib_server.py` exists only because this was built in an offline sandbox without
package registry access. In a normal environment, run `app.py` directly with Flask
installed (`pip install -r demo-app/requirements.txt`), the SAST/SCA/secret findings
are identical either way since they scan source, not the running process.

## Why this exists

Most SDLC security write-ups describe controls in the abstract. This repo runs them for
real against code with real, intentional flaws, so the findings in the article are actual
tool output, not a mockup.

## Disclaimer

This is a public portfolio project, built for learning and to show real hands-on work.
`demo-app/` is intentionally vulnerable and exists solely to be scanned. Do not deploy it,
and do not reuse its patterns (string-built SQL, `eval()` on user input, hardcoded
secrets) anywhere outside this demo.

---

*Part of the [GRC Toolkit](https://github.com/ebohc/grc-toolkit), alongside a PCI DSS v4.0.1 Targeted Risk Analysis template, a SOC 2 / ISO 27001 / PCI DSS control crosswalk, a zero-to-audit-ready program runbook, a PCI DSS Customized Approach playbook, a vulnerability scan coverage reference, and an incident response runbook.*

Victor Eboh, GRC Lead | [LinkedIn](https://www.linkedin.com/in/evictorc/) 
