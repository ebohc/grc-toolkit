#!/usr/bin/env python3
"""Operate-stage gate: post-deploy log review / anomaly triage.
Simple rule-based pass over an access log sample, standing in for the
SIEM correlation rules that would flag this in production monitoring."""
import re, sys, pathlib

SUSPECT_PATTERNS = [
    ("SQLi probe",        re.compile(r"(\bOR\b.*=.*|UNION\s+SELECT|--\s*$|'\s*OR\s*'1'='1)", re.I)),
    ("Path traversal probe", re.compile(r"\.\./")),
    ("Repeated 500s from single IP", None),  # handled separately below
]

def main(log_path):
    path = pathlib.Path(log_path)
    lines = path.read_text().splitlines()
    print("log-anomaly-check v0.1  (rule-based SIEM-style triage)")
    print(f"target: {path.name}  ({len(lines)} lines)\n")

    findings = []
    ip_500_count = {}
    for lineno, line in enumerate(lines, start=1):
        for name, pattern in SUSPECT_PATTERNS:
            if pattern and pattern.search(line):
                findings.append((lineno, name, line.strip()))
        m = re.match(r"^(\S+) .* \" 500 ", line)
        if m:
            ip_500_count[m.group(1)] = ip_500_count.get(m.group(1), 0) + 1

    for lineno, name, line in findings:
        print(f"[ALERT] line {lineno}: {name}")
        print(f"        {line}")

    for ip, count in ip_500_count.items():
        if count >= 3:
            print(f"[ALERT] {ip} triggered {count} server errors in window, possible probing")

    total = len(findings) + sum(1 for c in ip_500_count.values() if c >= 3)
    print(f"\n{total} alert(s) raised, routed to on-call queue.")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "access.log"))
