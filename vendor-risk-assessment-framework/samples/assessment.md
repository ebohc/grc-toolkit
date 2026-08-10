# Sample Vendor Assessment — Amazon Web Services (AWS)

**Assessment date:** April 2025
**Category:** IaaS
**Assessed by:** GRC Team
**Status:** Complete

---

## Vendor overview

Amazon Web Services is a cloud infrastructure provider offering compute, storage,
database, networking, and security services. This assessment is based entirely on
publicly available information including AWS compliance documentation and the
AWS Artifact portal.

---

## Risk scoring

| Factor | Column | Score | Rationale |
|--------|--------|-------|-----------|
| Data access | C | 3 | AWS hosts servers, databases, S3 buckets, and backups. They have access to everything on the infrastructure — customer data, application data, and credentials. |
| Integration depth | D | 3 | AWS is not integrated with the infrastructure — it IS the infrastructure. IAM, VPCs, RDS, Route 53, Lambda. Remove AWS and the entire stack is gone. |
| Business criticality | E | 3 | An AWS outage takes applications down instantly. No manual fallback exists at this level of dependency. |
| Security posture | F | 1 | AWS holds SOC 1, SOC 2, SOC 3, ISO 27001, PCI DSS Level 1, FedRAMP High, and 140+ certifications. Reports available via AWS Artifact. |

---

## Weighted score calculation
```
G = (3×0.4) + (3×0.3) + (3×0.2) + (1×0.1)
G = 1.2 + 0.9 + 0.6 + 0.1
G = 2.8
```

**Risk level: HIGH** (threshold: score ≥ 2.5)

---

## What this means

A High risk rating does not mean AWS is an unreliable vendor. It means they require
the highest level of governance attention — because the consequences of an incident
are severe and immediate.

---

## Required actions

| Action | Frequency | Owner |
|--------|-----------|-------|
| Security review | Quarterly | GRC Team |
| SOC 2 Type II report review | Annual | GRC Team |
| Shared responsibility model review | Annual | GRC + IT |
| Service health alerts | Ongoing | IT Operations |
| BCP inclusion review | Annual | Business Continuity Lead |

---

## Evidence collected

- AWS SOC 2 Type II report — available via AWS Artifact
- AWS compliance page: https://aws.amazon.com/compliance/programs/
- ISO 27001 certificate — publicly available
- AWS shared responsibility model: https://aws.amazon.com/compliance/shared-responsibility-model/

---

## Disclaimer

This assessment is based entirely on publicly available information.
No proprietary, confidential, or internal data is referenced.
No vendor relationship is implied.
