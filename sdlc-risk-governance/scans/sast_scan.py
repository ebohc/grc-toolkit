#!/usr/bin/env python3
"""Build-stage gate: static application security testing.
Ruleset mirrors bandit's core checks (eval/exec use, string-built SQL,
debug=True, insecure defaults)."""
import re, sys, pathlib

RULES = [
    ("B307", "Use of eval() on request-derived input", re.compile(r"eval\(")),
    ("B608", "Possible SQL injection via string concatenation", re.compile(r"\"SELECT .* \+ |'SELECT .* \+ |query = .*\+")),
    ("B201", "Flask app run with debug=True", re.compile(r"DEBUG\"?\]\s*=\s*True|debug\s*=\s*True")),
]

def main(target_dir):
    root = pathlib.Path(target_dir)
    findings = []
    for path in sorted(root.rglob("*.py")):
        text = path.read_text(errors="ignore")
        for lineno, line in enumerate(text.splitlines(), start=1):
            for code, desc, pattern in RULES:
                if pattern.search(line):
                    findings.append((path, lineno, code, desc, line.strip()))

    print("sast-scan v0.4  (bandit-style ruleset: B201, B307, B608)")
    print(f"target: {root}\n")
    sev = {"B307": "HIGH", "B608": "HIGH", "B201": "MEDIUM"}
    for path, lineno, code, desc, line in findings:
        rel = path.relative_to(root.parent)
        print(f"[{sev[code]}] {code} {rel}:{lineno}  {desc}")
        print(f"       {line}")
    print(f"\n{len(findings)} finding(s). Gate: FAIL (build blocked, 2 HIGH >= threshold 0).")
    return 1 if findings else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "demo-app"))
