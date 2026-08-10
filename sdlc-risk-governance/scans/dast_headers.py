#!/usr/bin/env python3
"""Test-stage gate: lightweight DAST check against a running instance.
Confirms baseline security headers are present (OWASP secure headers
project baseline). Run against the demo app started locally on :5001."""
import sys, urllib.request

REQUIRED_HEADERS = [
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Strict-Transport-Security",
]

def main(url):
    print(f"dast-headers-check v0.1  (OWASP secure headers baseline)")
    print(f"target: {url}\n")
    try:
        resp = urllib.request.urlopen(url, timeout=5)
        headers = dict(resp.getheaders())
    except Exception as e:
        print(f"ERROR: could not reach target ({e})")
        return 2

    missing = [h for h in REQUIRED_HEADERS if h not in headers]
    print(f"HTTP {resp.status} {url}")
    for h in REQUIRED_HEADERS:
        status = "present" if h in headers else "MISSING"
        print(f"  {h:<28} {status}")
    print(f"\nServer header: {headers.get('Server', 'n/a')}  (framework/version disclosure)")
    print(f"\n{len(missing)} of {len(REQUIRED_HEADERS)} required headers missing. Gate: FAIL.")
    return 1 if missing else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:5001/expense/1001"))
