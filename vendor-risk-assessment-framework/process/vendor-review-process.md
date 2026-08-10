# Vendor Review Process

A step-by-step guide for assessing, scoring, and managing third-party vendors
from initial intake through to ongoing monitoring.

---

## Overview

This process applies to any third party that provides services to your organization —
cloud providers, SaaS tools, consultants, and suppliers. Every vendor goes through
the same steps. The score determines how much attention they get after that.

**The five stages:**

1. Intake — identify the vendor and gather basic information
2. Score — rate the vendor across four risk factors
3. Classify — assign a risk level based on the weighted score
4. Document — record the assessment outcome and evidence
5. Monitor — schedule the next review based on risk level

---

## Stage 1 — Intake

**Trigger:** A new vendor is being onboarded, or an existing vendor is due for reassessment.

**Who does this:** The requestor (procurement, IT, or business owner) completes the
intake form before any contract is signed or access is granted.

| Field | Description |
|-------|-------------|
| Vendor name | Full legal or trading name |
| Category | SaaS / IaaS / PaaS / Supplier / Consultant / Other |
| Business owner | Internal person accountable for this vendor relationship |
| Service description | What does this vendor do for your organization? |
| Contract start date | When does or did the engagement begin? |
| Data shared | What data, if any, will the vendor access or process? |
| Systems connected | Which internal systems will the vendor connect to? |

**Rule:** No vendor gets system access or data access before completing intake.

---

## Stage 2 — Score

**Trigger:** Intake form is complete.

**Who does this:** The GRC or security team assigns scores using the four-factor model.

### Factor C — Data access (weight: 40%)

| Score | Criteria |
|-------|----------|
| 1 | No sensitive data — public or non-personal information only |
| 2 | Internal business data — employee records, financial systems, operational data |
| 3 | Regulated or sensitive data — PII, PCI, PHI, customer credentials, or IP |

### Factor D — Integration depth (weight: 30%)

| Score | Criteria |
|-------|----------|
| 1 | No integration — standalone tool, no API or system connection |
| 2 | Moderate integration — some data sync or API connection to internal systems |
| 3 | Deep integration — core infrastructure, SSO, real-time pipelines, or production systems |

### Factor E — Business criticality (weight: 20%)

| Score | Criteria |
|-------|----------|
| 1 | Low impact — business continues normally without this vendor |
| 2 | Moderate impact — productivity suffers but core operations survive |
| 3 | Critical — vendor outage causes immediate business disruption or customer downtime |

### Factor F — Security posture (weight: 10%)

| Score | Criteria |
|-------|----------|
| 1 | Strong — SOC 2 Type II, ISO 27001, or equivalent. Questionnaire fully completed. |
| 2 | Partial — some certifications or questionnaire partially completed |
| 3 | Unknown or weak — no certifications, no questionnaire response |

### Weighted score formula
```
Weighted Score = (C × 0.4) + (D × 0.3) + (E × 0.2) + (F × 0.1)
```

Enter scores into the Excel template — Columns G and H calculate automatically.

---

## Stage 3 — Classify

| Risk level | Score range | Review cadence | Owner |
|------------|-------------|----------------|-------|
| High | 2.5 and above | Quarterly | GRC + Business Owner |
| Medium | 1.5 to 2.4 | Annual | GRC |
| Low | Below 1.5 | Biennial | GRC |

### What each level requires

**High risk**
- Quarterly security review
- Annual SOC 2 Type II or equivalent audit report review
- Documented shared responsibility model
- Service health alerts configured
- Vendor included in Business Continuity Plan
- Security posture changes escalated to leadership immediately

**Medium risk**
- Annual security review
- Vendor security questionnaire sent and tracked every 12 months
- Certifications verified at contract renewal
- Passive monitoring for breach or incident news

**Low risk**
- Biennial review or event-triggered reassessment
- Reassess if vendor changes data scope, ownership, or service model

---

## Stage 4 — Document

| Item | Description |
|------|-------------|
| Completed risk register row | All nine columns filled in the Excel template |
| Score rationale | One sentence per factor explaining the score |
| Evidence collected | SOC 2 report, questionnaire response, or notes if unavailable |
| Assessment date | Date the review was completed |
| Next review date | Calculated from risk level and review cadence |
| Business owner sign-off | Confirmation the accountable owner has reviewed the outcome |

---

## Stage 5 — Monitor

### Event-triggered reassessment

Reassess any vendor immediately when:

- The vendor suffers a publicly disclosed breach or security incident
- The vendor is acquired or undergoes significant ownership change
- The vendor's service scope expands to include additional data or system access
- A contract renewal is approaching
- The vendor fails to respond to a security questionnaire within 30 days

### Escalation path

| Situation | Action |
|-----------|--------|
| High risk vendor score increases | Escalate to CISO within 5 business days |
| Vendor breach confirmed | Invoke incident response process immediately |
| Vendor fails questionnaire | Remediation plan with 60-day deadline |
| Vendor refuses questionnaire | Escalate to business owner for contract review |
| Low risk vendor scope expands | Reassess immediately |

---

## Related files

- [Vendor Risk Assessment Template (Excel)](../Vendor_Risk_Assessment_Template.xlsx)
- [Sample Assessment — Amazon AWS](../samples/assessment.md)
