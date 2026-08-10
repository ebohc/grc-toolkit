#!/usr/bin/env python3
"""Develop-stage gate: pre-commit / pre-merge secret scan.
Regex ruleset mirrors common gitleaks-style patterns (API keys, AWS keys,
generic high-entropy secrets, hardcoded passwords)."""
import re, sys, pathlib

RULES = [
    ("Stripe live secret key", re.compile(r"sk_live_[0-9a-zA-Z]{24,}")),
    ("AWS access key ID",      re.compile(r"AKIA[0-9A-Z]{16}")),
    ("Hardcoded password assignment", re.compile(r"(?i)(password|db_password|secret)\s*=\s*[\"'][^\"']{6,}[\"']")),
]

def scan_file(path):
    findings = []
    text = path.read_text(errors="ignore")
    for lineno, line in enumerate(text.splitlines(), start=1):
        for rule_name, pattern in RULES:
            if pattern.search(line):
                findings.append((path, lineno, rule_name, line.strip()))
    return findings

def main(target_dir):
    root = pathlib.Path(target_dir)
    all_findings = []
    for path in sorted(root.rglob("*")):
        if path.is_file() and path.suffix in (".py", ".env", ".example", ".txt", ".md") or path.name.startswith(".env"):
            all_findings.extend(scan_file(path))

    print(f"secret-scan v0.3  (gitleaks-style ruleset, {len(RULES)} rules)")
    print(f"target: {root}\n")
    if not all_findings:
        print("No findings.")
        return 0
    for path, lineno, rule_name, line in all_findings:
        rel = path.relative_to(root.parent)
        print(f"[HIGH] {rel}:{lineno}  {rule_name}")
        print(f"       {line}")
    print(f"\n{len(all_findings)} finding(s). Gate: FAIL (merge blocked).")
    return 1

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "demo-app"))
