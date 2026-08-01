# SOC 2 / ISO 27001:2022 / PCI DSS v4.0.1 — Control Crosswalk

**Author:** Victor Eboh — GRC Lead, Information Security & Compliance

**Purpose:** A working control-mapping reference across the three frameworks most compliance teams run simultaneously. Built to reduce duplicate evidence collection and to make the divergences — not just the overlaps — visible, since the divergences are where audit findings actually happen.

> **Note on this artifact:** Control references are drawn from SOC 2 Trust Services Criteria (2017, as revised), ISO/IEC 27001:2022 Annex A, and PCI DSS v4.0.1. All notes reflect professional GRC practice, genericized — no client or employer environment is referenced.

---

## Table of Contents

1. [Why a Crosswalk, Not Three Separate Programs](#1-why-a-crosswalk-not-three-separate-programs)
2. [How to Use This](#2-how-to-use-this)
3. [Master Crosswalk Table](#3-master-crosswalk-table)
4. [Domain Detail](#4-domain-detail)
5. [Where the Frameworks Genuinely Diverge](#5-where-the-frameworks-genuinely-diverge)
6. [Maintenance](#6-maintenance)

---

## 1. Why a Crosswalk, Not Three Separate Programs

Running SOC 2, ISO 27001, and PCI DSS as three independent programs means three sets of policies, three evidence requests for the same control, and three audit cycles that all ask a version of "who has access to what, and how do you know." The overlap across these frameworks is real — access control, encryption, logging, incident response, and vendor management account for most of the control mass in all three.

The risk in treating them as fully interchangeable is the opposite failure: assuming a control that satisfies SOC 2 automatically satisfies PCI DSS, when PCI is frequently the most prescriptive of the three and adds requirements the others don't carry at all (specific retention periods, mandatory scan cadences, written third-party acknowledgment of cardholder data responsibility). A crosswalk only earns its keep if it documents both — where one control genuinely covers three frameworks, and where it covers two and a half.

---

## 2. How to Use This

**If you're scoping a program that needs two or three of these frameworks:** start with the Master Crosswalk Table to identify which domains can run on a single control set, then check Section 5 before assuming full coverage — that section exists specifically to stop a team from marking a PCI requirement "satisfied" off the back of a SOC 2 control that doesn't actually go far enough.

**If you're an auditor or assessor reviewing evidence:** the Domain Detail section states which framework's version of a control is the strictest, so you know which evidence set to request first — it's usually the superset.

**If you're building a unified control library:** the "Note" column in the master table is written as the seed for a control description in whatever GRC platform you use — it states the shared intent, not just the citation.

---

## 3. Master Crosswalk Table

| Domain | SOC 2 (Trust Services Criteria) | ISO 27001:2022 (Annex A) | PCI DSS v4.0.1 | Alignment |
|---|---|---|---|---|
| Access Control (Logical) | CC6.1, CC6.2, CC6.3 | A.5.15, A.5.16, A.5.18, A.8.2, A.8.3 | Req. 7, Req. 8 | Strong overlap; PCI most prescriptive |
| Privileged Access | CC6.3 | A.8.2 | Req. 7.2, Req. 8.2 | Strong overlap |
| Encryption / Cryptography | CC6.1 (Confidentiality category) | A.8.24 | Req. 3, Req. 4 | Intent aligned; PCI mandates specific technical detail |
| Vulnerability Management | CC7.1 | A.8.8 | Req. 6, Req. 11.3 | Intent aligned; PCI mandates scan cadence and remediation SLA |
| Logging & Monitoring | CC7.2 | A.8.15, A.8.16 | Req. 10 | PCI most prescriptive (retention, review frequency) |
| Incident Response | CC7.3, CC7.4 | A.5.24, A.5.25, A.5.26, A.5.27 | Req. 12.10 | Near-identical intent across all three |
| Change Management | CC8.1 | A.8.32 | Req. 6.5 | Strong overlap; PCI adds CDE-specific documentation |
| Vendor / Third-Party Risk | CC9.2 | A.5.19, A.5.20, A.5.21, A.5.22 | Req. 12.8, Req. 12.9 | PCI adds a requirement the others don't have (see Section 5) |
| Physical Security | CC6.4 | A.7.1 – A.7.14 | Req. 9 | PCI is CDE-scoped only; ISO/SOC 2 are enterprise-wide |
| Risk Assessment | CC3.1 – CC3.4 | Clause 6.1.2, A.5.7 | Req. 12.3 | See the [PCI DSS TRA template](../pci-dss-tra) for the PCI-specific mechanism |
| Security Awareness Training | CC1.4 | A.6.3 | Req. 12.6 | Strong overlap; PCI requires role-specific and annual cadence |

---

## 4. Domain Detail

### Access Control (Logical)
**SOC 2:** CC6.1 (logical access security), CC6.2 (provisioning/deprovisioning), CC6.3 (role-based access)

**ISO 27001:2022:** A.5.15 (access control), A.5.16 (identity management), A.5.18 (access rights), A.8.2 (privileged access), A.8.3 (information access restriction)

**PCI DSS v4.0.1:** Req. 7 (restrict access by business need to know), Req. 8 (identify users and authenticate access)

All three require least-privilege provisioning and periodic access review. The meaningful divergence is authentication strength: PCI DSS v4.0.1 mandates MFA for **all** access into the CDE, including local/on-premise access — a change from v3.2.1, where MFA was only required for remote access. SOC 2 and ISO 27001 leave MFA scope to the entity's own risk assessment. A control built to PCI's bar satisfies the other two; the reverse is not guaranteed.

### Privileged Access
**SOC 2:** CC6.3

**ISO 27001:2022:** A.8.2

**PCI DSS v4.0.1:** Req. 7.2 (access control model), Req. 8.2 (unique ID and privileged account management)

Strong overlap across all three — the shared control is a documented access control model, unique account ownership (no shared/generic accounts for administrative functions), and evidence of periodic entitlement review. A single privileged-access-review process, run quarterly, satisfies all three frameworks' evidence expectations.

### Encryption / Cryptography
**SOC 2:** CC6.1, under the Confidentiality Trust Services Category where elected

**ISO 27001:2022:** A.8.24 (use of cryptography)

**PCI DSS v4.0.1:** Req. 3 (protect stored account data), Req. 4 (protect data in transit)

This is the domain with the widest gap between principle and prescription. ISO 27001's A.8.24 says encryption decisions should follow the organization's risk assessment — it does not specify algorithms, key lengths, or rotation cadence. PCI DSS Req. 3.5 does: cryptographic keys used to protect stored account data must be stored in two or fewer locations, documented in a formal key-management program, and rotated at least annually (or on suspected compromise). A crosswalk that treats "we encrypt data at rest" as sufficient evidence for all three frameworks will pass ISO and SOC 2 review and fail a PCI QSA's request for the key-management program documentation.

### Vulnerability Management
**SOC 2:** CC7.1

**ISO 27001:2022:** A.8.8 (management of technical vulnerabilities)

**PCI DSS v4.0.1:** Req. 6 (develop and maintain secure systems), Req. 11.3 (internal and external vulnerability scanning)

PCI is the only one of the three with a fixed scan cadence baked into the requirement itself: quarterly external ASV scans (with passing results), and internal scanning aligned to the entity's own risk ranking under 11.3.1.1 — which is exactly the kind of activity-frequency TRA covered in the [PCI DSS TRA template](../pci-dss-tra) in this repo. ISO and SOC 2 require a vulnerability management process but leave frequency to the entity's risk determination. Running PCI's cadence as the baseline satisfies the other two frameworks' evidence expectations without extra work.

### Logging & Monitoring
**SOC 2:** CC7.2

**ISO 27001:2022:** A.8.15 (logging), A.8.16 (monitoring activities)

**PCI DSS v4.0.1:** Req. 10 (log and monitor all access to system components and cardholder data)

PCI is the most prescriptive control in this entire crosswalk: minimum 12-month log retention with 3 months immediately available for analysis, and daily review requirements for security-critical systems (with a TRA-justified frequency permitted for non-critical systems under 10.4.2.1 — see the TRA template). ISO and SOC 2 require logging and monitoring but don't specify retention periods or review frequency. Building log retention to PCI's minimum by default avoids having to run two retention policies.

### Incident Response
**SOC 2:** CC7.3 (incident identification), CC7.4 (incident response)

**ISO 27001:2022:** A.5.24 (planning), A.5.25 (assessment and decision), A.5.26 (response), A.5.27 (learning from incidents)

**PCI DSS v4.0.1:** Req. 12.10 (incident response plan and readiness)

The closest alignment of any domain in this crosswalk — all three expect a documented plan, defined roles, and a post-incident review/lessons-learned step. PCI adds a specific testing requirement (annual IR plan test, which most commonly takes the form of a tabletop exercise) that ISO and SOC 2 don't mandate as explicitly, though both would accept it as strong evidence.

### Change Management
**SOC 2:** CC8.1

**ISO 27001:2022:** A.8.32 (change management)

**PCI DSS v4.0.1:** Req. 6.5 (changes to in-scope systems are managed securely)

Strong overlap on the core control (documented approval, testing, and rollback plan before production changes). PCI's addition is CDE-specificity: change documentation must show the change didn't introduce a PCI DSS control gap, which requires a compliance-impact check most general change-management processes don't include by default.

### Vendor / Third-Party Risk
**SOC 2:** CC9.2

**ISO 27001:2022:** A.5.19 (supplier relationships), A.5.20 (addressing security in supplier agreements), A.5.21 (ICT supply chain), A.5.22 (monitoring supplier services)

**PCI DSS v4.0.1:** Req. 12.8 (TPSP relationships managed), Req. 12.9 (written acknowledgment of responsibility)

See Section 5 — this is one of the two domains where PCI requires something structurally absent from the other frameworks.

### Physical Security
**SOC 2:** CC6.4

**ISO 27001:2022:** A.7.1 through A.7.14 (secure areas, equipment, media handling)

**PCI DSS v4.0.1:** Req. 9 (restrict physical access to cardholder data)

Scope is the divergence, not intent. ISO and SOC 2 physical controls apply enterprise-wide. PCI's Req. 9 applies only to locations where the CDE physically exists — but within that scope, PCI adds specifics the others don't carry, including periodic inspection of point-of-interaction devices for tampering (Req. 9.4, itself a TRA-eligible frequency control under 9.4.1.1).

### Risk Assessment
**SOC 2:** CC3.1 – CC3.4

**ISO 27001:2022:** Clause 6.1.2 (formal ISMS requirement), A.5.7 (threat intelligence)

**PCI DSS v4.0.1:** Req. 12.3 (risk assessment / Targeted Risk Analysis)

This is where PCI's model structurally differs rather than just adding detail. ISO and SOC 2 both expect an enterprise-wide risk assessment process. PCI DSS v4.0.1 replaced its old annual risk-assessment requirement with Targeted Risk Analyses scoped to individual requirements — a narrower, more frequent mechanism. The full methodology for that specific PCI mechanism is built out separately in this repo's [PCI DSS TRA template](../pci-dss-tra).

### Security Awareness Training
**SOC 2:** CC1.4

**ISO 27001:2022:** A.6.3

**PCI DSS v4.0.1:** Req. 12.6

Strong overlap on the base requirement (documented, recurring training program). PCI is explicit about annual cadence and role-specific content (e.g., additional training for personnel with access to the CDE); ISO and SOC 2 expect "regular" training without pinning the interval, which in practice most programs set to annual anyway to satisfy the strictest of the three.

---

## 5. Where the Frameworks Genuinely Diverge

Two domains where mapping a single control across all three actively risks an audit finding if you stop at "these are basically the same":

**Vendor/Third-Party Risk (PCI Req. 12.9).** PCI DSS is the only framework of the three that requires a *written acknowledgment from the third-party service provider itself* — not just your own vendor risk assessment of them — stating they are responsible for the security of cardholder data they possess or otherwise store, process, or transmit. ISO's A.5.20 and SOC 2's CC9.2 both expect strong contractual security terms, but neither requires this specific bilateral written acknowledgment as a named artifact. A vendor risk program built only to ISO/SOC 2 expectations will be missing a document a PCI QSA will explicitly ask for by name.

**Encryption Key Management (PCI Req. 3.5–3.6).** Covered in Section 4, repeated here because it's the single most common gap: ISO and SOC 2 accept "we have an encryption policy driven by our risk assessment." PCI wants the key-management program itself as a document — custody, storage location count, rotation schedule, and split-knowledge/dual-control procedures for manual key operations. Teams that build encryption controls to ISO's principle-based standard first, then try to retrofit PCI evidence later, consistently find this is where the retrofit takes the longest.

---

## 6. Maintenance

This crosswalk reflects SOC 2 (2017 TSC, as revised), ISO/IEC 27001:2022, and PCI DSS v4.0.1 as of publication. ISO 27001:2013 certificates fully expired in October 2025 — if you're referencing an older ISO mapping, confirm it's been updated to the 2022 Annex A control numbering (93 controls, not the prior 114) before relying on it. Re-validate this mapping against the current PCI DSS version at least annually, and immediately on any major version release.

---

*Part of the [GRC Toolkit](https://github.com/ebohc/grc-toolkit) — see also the [PCI DSS v4.0.1 Targeted Risk Analysis template](../pci-dss-tra) referenced throughout this document.*

Victor Eboh — GRC Lead | [LinkedIn](https://www.linkedin.com/in/evictorc/)
