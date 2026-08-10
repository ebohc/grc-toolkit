#!/usr/bin/env python3
"""Build-stage gate: software composition analysis (SCA).
Compares pinned dependency versions in requirements.txt against a small
local reference of publicly disclosed CVEs affecting old Flask/Werkzeug/
Jinja2/requests releases. Mirrors what `pip-audit` / `npm audit` do against
an advisory database, using a static local table instead of a live feed."""
import re, sys, pathlib

# Reference table: package -> (max_affected_version, cve, summary)
KNOWN_CVES = {
    "flask":    [("1.0", "CVE-2019-1010083", "DoS via crafted Host header / large multipart requests")],
    "jinja2":   [("2.10.1", "CVE-2019-10906", "Sandbox escape via crafted template (str.format_map)")],
    "werkzeug": [("0.15.3", "CVE-2019-14806", "Improper multipart form parsing leads to DoS")],
    "requests": [("2.19.1", "CVE-2018-18074", "Authorization header leaked to redirected host")],
}

def parse_requirements(path):
    pkgs = {}
    for line in path.read_text().splitlines():
        line = line.strip()
        m = re.match(r"([A-Za-z0-9_\-]+)==([0-9][0-9A-Za-z.\-]*)", line)
        if m:
            pkgs[m.group(1).lower()] = m.group(2)
    return pkgs

def version_leq(a, b):
    def norm(v): return [int(x) for x in re.findall(r"\d+", v)]
    return norm(a) <= norm(b)

def main(target_dir):
    root = pathlib.Path(target_dir)
    req = root / "requirements.txt"
    pkgs = parse_requirements(req)
    print("sca-check v0.2  (local CVE reference table, 4 packages tracked)")
    print(f"target: {req.relative_to(root.parent)}\n")

    findings = []
    for pkg, version in pkgs.items():
        for max_version, cve, summary in KNOWN_CVES.get(pkg, []):
            if version_leq(version, max_version):
                findings.append((pkg, version, cve, summary))

    for pkg, version, cve, summary in findings:
        print(f"[HIGH] {pkg}=={version}  {cve}")
        print(f"       {summary}")
    print(f"\n{len(findings)} finding(s) across {len(pkgs)} pinned dependencies. Gate: FAIL (release blocked).")
    return 1 if findings else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "demo-app"))
