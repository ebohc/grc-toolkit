> Part of the [GRC Toolkit](https://github.com/ebohc/grc-toolkit) — a broader collection of GRC artifacts.
>
>
> # CPCSC Compliance Template

A practical, opinionated template for implementing the **Canadian Program for Cyber Security Certification (CPCSC)** - built from an analyst and auditor perspective.

Straight to the point. What's required, what evidence to keep, what an assessor will ask for. No filler.

[**Download the template (.xlsx)**](./CPCSC_Compliance_Template_v1.1.xlsx)

---

## What is CPCSC?

Canada's mandatory cybersecurity certification for defence suppliers. It's built on **ITSP.10.171** - Canada's adaptation of NIST SP 800-171 Revision 3 - and is managed by Public Services and Procurement Canada (PSPC).

Three certification levels:

| Level | Who | Requirement | Assessment |
|---|---|---|---|
| **Level 1** | Suppliers handling Federal Contractual Information (FCI) | ~13 basic controls across 6 ITSP.10.171 families | Annual self-assessment via Canada Buys |
| **Level 2** | Suppliers handling Controlled Information / Protected B | 97 controls across 17 ITSP.10.171 families | Third-party assessment by SCC-accredited Certification Body |
| **Level 3** | Highest-sensitivity contracts (e.g. NORAD Modernisation) | Enhanced controls beyond Level 2 | Assessment by Department of National Defence |

**Level 1 is mandatory for National Defence contracts from Spring 2026.** Level 2 becomes mandatory for Controlled Information contracts in 2027.

---

## Who this template is for

- Canadian defence suppliers and subcontractors preparing for Level 1 self-attestation
- Organisations scoping a Level 2 readiness programme and building their first gap assessment
- GRC analysts, auditors, and internal audit teams mapping CPCSC against existing SOC 2, ISO 27001, or PCI-DSS programmes
- Cross-border organisations that need to understand where CPCSC and US CMMC overlap (and where they don't)

---

## What's inside

The workbook has six tabs. Each one is designed to be usable as a standalone artefact you can hand to a stakeholder without explaining.

**1. Overview** - Plain-English summary of what CPCSC is, who it applies to, the three certification levels, and the implementation timeline through 2027.

**2. ITSP.10.171 Controls** - All 17 control families. For each family: what it covers, what to implement, evidence to maintain (analyst view), evidence an assessor will request (auditor view), what a pass looks like, and the common failures that cause findings.

**3. Level 1 Checklist** - The basic controls required for Level 1 self-assessment. For each: the self-assessment question, the evidence to retain internally, an owner, target date, and status column ready to track.

**4. Gap Assessment** - Current state vs required state by control family. Includes remediation owner, priority, target date, and a RAG status column. Pre-populated with a realistic example so you can see how a filled-in row should read.

**5. CPCSC vs CMMC** - Side-by-side comparison of Canada's CPCSC and the US CMMC. Critical if your organisation works cross-border. Covers governing bodies, control counts, assessment structures, and mutual-recognition status (there isn't one).

**6. Glossary** - Plain-English definitions for every CPCSC term, acronym, and document reference used in the workbook.

---

## How to use it

**If you're an analyst implementing CPCSC:**
Work left-to-right on the ITSP.10.171 Controls tab. The *Analyst - What to implement* and *Analyst - Evidence to maintain* columns tell you what to build and what to keep. Drop the Level 1 Checklist in front of your team as-is for the Spring 2026 self-assessment. Use the Gap Assessment tab to track current state and close findings in order of priority.

**If you're an auditor or internal audit lead:**
The *Assessor - Evidence requested* and *Assessor - What a PASS looks like* columns on the ITSP.10.171 Controls tab are your request list and your evaluation criteria. The *Common failures* column is what to watch for during walkthroughs.

**If you're a GRC lead scoping the programme:**
Start with the Overview tab. Use CPCSC vs CMMC to scope cross-border impact. Use the Gap Assessment tab as your first read-out to leadership.

---

## About the author

Built by **Victor Eboh** - Senior GRC & Information Security Lead. Seven years building security programmes that hold up under audit: SOC 2 Type II and ISO 27001 from zero to clean opinion, PCI-DSS across Requirements 1–12 and A1–A3, NIST CSF 2.0, and a TPRM programme covering 200+ vendors.

**Certifications:** CRISC · CompTIA CySA+ · ISO 27001 Lead Implementer · ISC2 CC

- GitHub: [github.com/ebohc](https://github.com/ebohc)
- Medium: [medium.com/@ebohc](https://medium.com/@ebohc)

Open to collaborations - especially with Canadian defence suppliers working toward Level 1 this spring or Level 2 in 2027.

---

## Disclaimer

This template is a practitioner's guide, not a legal or regulatory opinion. It reflects ITSP.10.171 requirements as understood at the time of publication. CPCSC is a live programme and its scope, timelines, and assessment guidance continue to evolve. Always confirm current requirements against the official CCCS and PSPC publications before certifying.

## Licence

Free to download, fork, adapt, and share. Attribution appreciated but not required.

---

*v1.1 · Refined April 2026*
