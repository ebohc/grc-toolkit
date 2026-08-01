
# PCI DSS v4.0.1 - Targeted Risk Analysis (TRA) Template & Methodology

**Author:** Victor Eboh - GRC Lead, Information Security & Compliance
**Purpose:** A reusable, audit-ready Targeted Risk Analysis framework built to PCI DSS v4.0.1 Requirement 12.3.1, covering the eight control domains where PCI DSS grants an entity flexibility to self-define activity frequency.

> **Note on this artifact:** This is an original template built from professional GRC practice. All entity names, environments, findings, and risk ratings below are fictional (**"Meridian Retail Co."**) and provided to demonstrate methodology only - no client, employer, or real-environment data is used anywhere in this document.

---

## Table of Contents

1. [Why This Exists](#1-why-this-exists)
2. [TRA Methodology](#2-tra-methodology)
3. [Required Elements per Requirement 12.3.1](#3-required-elements-per-requirement-1231)
4. [Risk Scoring Model](#4-risk-scoring-model)
5. [The Eight TRAs](#5-the-eight-tras)
   - [5.1 - TRA-01: Malware Evaluation Frequency (Req. 5.2.3.1)](#51-tra-01-malware-evaluation-frequency-req-5231)
   - [5.2 - TRA-02: Removable Media Scan Frequency (Req. 5.3.2.1)](#52-tra-02-removable-media-scan-frequency-req-5321)
   - [5.3 - TRA-03: User Account & Access Privilege Review Frequency (Req. 7.2.5.1)](#53-tra-03-user-account--access-privilege-review-frequency-req-7251)
   - [5.4 - TRA-04: System/Application Account Password Change Frequency (Req. 8.6.3)](#54-tra-04-systemapplication-account-password-change-frequency-req-863)
   - [5.5 - TRA-05: Log Review Frequency for Non-Critical Systems (Req. 10.4.2.1)](#55-tra-05-log-review-frequency-for-non-critical-systems-req-10421)
   - [5.6 - TRA-06: Remediation Timeline for Non-Critical Vulnerabilities (Req. 11.3.1.1)](#56-tra-06-remediation-timeline-for-non-critical-vulnerabilities-req-11311)
   - [5.7 - TRA-07: Payment Page Tamper-Detection Review Frequency (Req. 11.6.1)](#57-tra-07-payment-page-tamper-detection-review-frequency-req-1161)
   - [5.8 - TRA-08: Incident Response Training Frequency (Req. 12.10.4.1)](#58-tra-08-incident-response-training-frequency-req-121041)
6. [Governance, Review Cycle & Sign-Off](#6-governance-review-cycle--sign-off)
7. [Blank Template (Copy/Paste)](#7-blank-template-copypaste)

---

## 1. Why This Exists

PCI DSS v4.0.1 replaced the old model - a single annual, entity-wide risk assessment - with **Targeted Risk Analyses**: narrow, requirement-specific analyses that justify *why* a chosen frequency or approach is appropriate, tied to the entity's actual assets, threats, and risk appetite. Requirement 12.3.1 applies specifically wherever PCI DSS says an activity must happen "periodically" or "as appropriate" rather than on a fixed schedule.

Most organizations treat this as a documentation exercise and produce eight (or more) TRAs that all reach the same generic conclusion, with no real risk logic behind the number they pick. A QSA can tell the difference between a TRA that was actually reasoned through and one that was reverse-engineered to justify whatever frequency the team already wanted. This template is built to survive that scrutiny - every conclusion traces back through a documented risk score, not a preference.

---

## 2. TRA Methodology

Each TRA in this template follows the same five-stage process, applied independently per requirement - this is the core discipline of a *targeted* analysis rather than an enterprise-wide one:

| Stage | What Happens | Output |
|---|---|---|
| **1. Scope the control** | Identify the exact PCI DSS sub-requirement, the assets it protects, and the specific activity whose frequency is being justified. | Scope statement |
| **2. Identify threats & vulnerabilities** | Map realistic threat scenarios against the asset if the activity were performed *less* often than proposed. | Threat/vulnerability list |
| **3. Score likelihood & impact** | Rate each threat scenario using the scoring model in Section 4. | Likelihood × Impact = Risk Rating |
| **4. Determine frequency** | Select a frequency that reduces residual risk to an acceptable level, referencing the risk rating - not the other way around. | Defined frequency + rationale |
| **5. Validate & approve** | Senior management (or designated risk owner) reviews and formally signs off before the TRA is considered active evidence. | Sign-off record |

---

## 3. Required Elements per Requirement 12.3.1

Per PCI DSS v4.0.1, every TRA performed to justify activity frequency must document:

- **(a)** The assets being protected
- **(b)** The threat(s) or vulnerability(ies) the activity addresses
- **(c)** Prior frequency-related incidents (if any) affecting the entity
- **(d)** The likelihood and impact of the threat materializing if the activity is *not* performed at the proposed frequency
- **(e)** How the resulting frequency reduces the likelihood and/or impact of a threat being realized
- **(f)** Review and sign-off by senior management

Every TRA below is structured to hit all six elements explicitly - this is the checklist a QSA will actually run your documentation against, so the template enforces it by section header rather than leaving it to memory.

---

## 4. Risk Scoring Model

A simple 3×3 qualitative matrix, chosen deliberately over a more elaborate model - PCI DSS does not require quantitative scoring, and an overbuilt model is harder to defend consistently across eight TRAs than a transparent, repeatable one.

**Likelihood**

| Score | Rating | Definition |
|---|---|---|
| 1 | Low | Requires a specific, uncommon set of conditions; no history of occurrence in similar environments |
| 2 | Medium | Plausible under normal operating conditions; occasional industry precedent |
| 3 | High | Likely without compensating controls; known active threat pattern or prior internal occurrence |

**Impact**

| Score | Rating | Definition |
|---|---|---|
| 1 | Low | Contained to a single non-critical system; no cardholder data exposure |
| 2 | Medium | Potential exposure of limited cardholder data or degradation of a compensating control |
| 3 | High | Direct cardholder data exposure, CDE-wide impact, or breach of a compensating control boundary |

**Risk Rating = Likelihood × Impact**

| Range | Rating | Frequency Implication |
|---|---|---|
| 1–2 | Low | Longer interval defensible (e.g., quarterly/semi-annual) |
| 3–4 | Moderate | Mid-range interval (e.g., monthly/quarterly) |
| 6–9 | High | Short interval required (e.g., daily/weekly), or activity is not a candidate for extended frequency at all |

---

## 5. The Eight TRAs

### 5.1 - TRA-01: Malware Evaluation Frequency (Req. 5.2.3.1)

| Field | Detail |
|---|---|
| **Requirement** | 5.2.3.1 - Frequency of evaluating system components identified as not at risk for malware |
| **(a) Assets** | Point-of-sale terminals, back-office workstations, and application servers within the CDE not currently running active anti-malware due to system type/function |
| **(b) Threat/Vulnerability** | Introduction of malware via removable media, lateral movement from a compromised adjacent system, or a change in system function that invalidates the "not at risk" classification |
| **(c) Prior incidents** | None recorded in the trailing 12 months for in-scope system types |
| **(d) Likelihood & Impact if under-evaluated** | Likelihood: **2 (Medium)** - system classification can silently drift as software/config changes. Impact: **3 (High)** - undetected malware on a CDE-adjacent system risks direct cardholder data exposure |
| **Risk Rating** | 6 - High |
| **(e) Determined Frequency** | Re-evaluation of "not at risk" classification every **90 days**, with an ad hoc trigger on any change-management ticket touching the system's function or network placement |
| **Rationale** | A 90-day cycle is short enough to catch classification drift within a single quarterly change-review cadence, and the change-triggered re-evaluation closes the gap between scheduled reviews rather than relying on the schedule alone |
| **(f) Sign-off** | Reviewed and approved by [Risk Owner], [Date] |

---

### 5.2 - TRA-02: Removable Media Scan Frequency (Req. 5.3.2.1)

| Field | Detail |
|---|---|
| **Requirement** | 5.3.2.1 - Frequency of periodic malware scans (in lieu of active/real-time scanning) |
| **(a) Assets** | Legacy back-office file servers where real-time anti-malware degrades application performance |
| **(b) Threat/Vulnerability** | Malware persistence between scheduled scans; dwell time before detection |
| **(c) Prior incidents** | One low-severity detection 8 months prior - commodity malware, contained, no CDE impact |
| **(d) Likelihood & Impact** | Likelihood: **2 (Medium)** - prior detection shows the vector is live, though contained. Impact: **2 (Medium)** - system is CDE-adjacent, not CDE-storing |
| **Risk Rating** | 4 - Moderate |
| **(e) Determined Frequency** | Full scan **weekly**, with real-time scanning re-evaluated annually as hardware refresh may remove the original performance constraint |
| **Rationale** | Weekly scanning bounds maximum dwell time to a level consistent with the moderate risk rating; the annual re-evaluation prevents the exception from becoming permanent by default |
| **(f) Sign-off** | Reviewed and approved by [Risk Owner], [Date] |

---

### 5.3 - TRA-03: User Account & Access Privilege Review Frequency (Req. 7.2.5.1)

| Field | Detail |
|---|---|
| **Requirement** | 7.2.5.1 - Frequency of reviewing user accounts and access privileges |
| **(a) Assets** | User and service accounts with access to systems storing, processing, or transmitting cardholder data |
| **(b) Threat/Vulnerability** | Privilege creep from role changes; orphaned accounts following offboarding; excessive standing access enabling insider misuse or lateral movement post-compromise |
| **(c) Prior incidents** | Internal audit (prior cycle) identified 3 stale accounts from role transfers, remediated within SLA |
| **(d) Likelihood & Impact** | Likelihood: **2 (Medium)** - organization has moderate personnel turnover and prior evidence of drift. Impact: **3 (High)** - excess CDE access is a direct escalation path |
| **Risk Rating** | 6 - High |
| **(e) Determined Frequency** | Full access review **quarterly**, with an automated offboarding trigger disabling access within 24 hours of HR termination record |
| **Rationale** | Quarterly review addresses gradual privilege creep; the automated offboarding trigger addresses the higher-risk, time-sensitive termination scenario separately rather than relying on the quarterly cycle to catch it |
| **(f) Sign-off** | Reviewed and approved by [Risk Owner], [Date] |

---

### 5.4 - TRA-04: System/Application Account Password Change Frequency (Req. 8.6.3)

| Field | Detail |
|---|---|
| **Requirement** | 8.6.3 - Frequency of changing passwords/passphrases for application and system accounts (default: 90 days, extendable if justified by TRA) |
| **(a) Assets** | Service accounts used for application-to-database and application-to-application authentication within the CDE |
| **(b) Threat/Vulnerability** | Credential compromise via exposure in logs, code repositories, or configuration files; extended validity window increases exposure time if leaked |
| **(c) Prior incidents** | None recorded; accounts are managed through a secrets vault with access logging |
| **(d) Likelihood & Impact** | Likelihood: **1 (Low)** - vaulted, logged, no human interactive use, rotation independent of memorization. Impact: **3 (High)** - compromise of a service account is a direct CDE access path |
| **Risk Rating** | 3 - Moderate |
| **(e) Determined Frequency** | **180 days**, contingent on continued vault enforcement, access logging, and absence of any credential-exposure event |
| **Rationale** | The extended interval is justified specifically because compensating controls (vaulting, logging, no human memorization) lower likelihood; the TRA explicitly ties the extension to those controls remaining in place, so it is invalidated automatically if the vault is ever bypassed |
| **(f) Sign-off** | Reviewed and approved by [Risk Owner], [Date] |

---

### 5.5 - TRA-05: Log Review Frequency for Non-Critical Systems (Req. 10.4.2.1)

| Field | Detail |
|---|---|
| **Requirement** | 10.4.2.1 - Frequency of log reviews for system components not defined as critical under 10.4.1 |
| **(a) Assets** | Non-critical internal systems (e.g., internal reporting tools) with no direct CDE data path |
| **(b) Threat/Vulnerability** | Delayed detection of anomalous activity that could indicate reconnaissance or staging ahead of a pivot toward in-scope systems |
| **(c) Prior incidents** | None recorded for this system tier |
| **(d) Likelihood & Impact** | Likelihood: **1 (Low)** - no direct CDE connectivity, limited attacker interest as a primary target. Impact: **2 (Medium)** - could serve as a staging point even without direct data access |
| **Risk Rating** | 2 - Low |
| **(e) Determined Frequency** | Log review **weekly**, via automated SIEM correlation rules with alert-based escalation outside the weekly cycle |
| **Rationale** | The low risk rating supports an extended manual review interval, but automated correlation rules close the gap for any activity that shouldn't wait a week - the TRA frequency governs the *scheduled* review, not the detection capability itself |
| **(f) Sign-off** | Reviewed and approved by [Risk Owner], [Date] |

---

### 5.6 - TRA-06: Remediation Timeline for Non-Critical Vulnerabilities (Req. 11.3.1.1)

| Field | Detail |
|---|---|
| **Requirement** | 11.3.1.1 - Approach for addressing vulnerabilities not ranked as high-risk or critical per the entity's risk ranking |
| **(a) Assets** | All CDE and CDE-connected systems subject to internal vulnerability scanning |
| **(b) Threat/Vulnerability** | Accumulation of unpatched medium/low findings that, chained together, could enable an attack path even without a single critical vulnerability |
| **(c) Prior incidents** | None; medium/low findings have historically closed within informal timelines averaging ~45 days |
| **(d) Likelihood & Impact** | Likelihood: **2 (Medium)** - chaining risk is real but requires multiple conditions. Impact: **2 (Medium)** - no single finding provides direct CDE compromise |
| **Risk Rating** | 4 - Moderate |
| **(e) Determined Frequency** | Medium findings remediated within **30 days**, low findings within **90 days**, both tracked against a formal SLA rather than the prior informal average |
| **Rationale** | Formalizing the SLA at a tighter interval than the historical average reduces the chaining window without requiring the same treatment as critical findings, matching effort to the moderate rather than high risk rating |
| **(f) Sign-off** | Reviewed and approved by [Risk Owner], [Date] |

---

### 5.7 - TRA-07: Payment Page Tamper-Detection Review Frequency (Req. 11.6.1)

| Field | Detail |
|---|---|
| **Requirement** | 11.6.1 - Frequency of reviewing the change-and-tamper-detection mechanism for payment pages |
| **(a) Assets** | Customer-facing checkout and payment pages served to cardholders |
| **(b) Threat/Vulnerability** | E-skimming (e.g., Magecart-style) script injection going undetected between review cycles |
| **(c) Prior incidents** | None recorded; industry threat pattern for e-skimming is active and well-documented |
| **(d) Likelihood & Impact** | Likelihood: **3 (High)** - e-skimming is an active, industry-wide attack pattern against payment pages specifically. Impact: **3 (High)** - direct, large-scale cardholder data exposure at the point of capture |
| **Risk Rating** | 9 - High |
| **(e) Determined Frequency** | Automated, continuous monitoring with alerting, supplemented by a **weekly** manual verification review |
| **Rationale** | The high risk rating on both axes rules out any extended manual-only interval; this is the one TRA in the set where the conclusion is that flexibility should be used minimally, not maximally - the TRA still documents the reasoning even though the outcome is "stay tight" |
| **(f) Sign-off** | Reviewed and approved by [Risk Owner], [Date] |

---

### 5.8 - TRA-08: Incident Response Training Frequency (Req. 12.10.4.1)

| Field | Detail |
|---|---|
| **Requirement** | 12.10.4.1 - Frequency of incident response personnel training |
| **(a) Assets** | Incident response team roles and their operational readiness |
| **(b) Threat/Vulnerability** | Degraded response effectiveness from outdated procedures, tool changes, or team turnover between training cycles |
| **(c) Prior incidents** | One tabletop exercise (prior cycle) identified a 20-minute delay in escalation path due to an outdated contact list |
| **(d) Likelihood & Impact** | Likelihood: **2 (Medium)** - team composition and tooling change often enough to erode readiness within a year. Impact: **3 (High)** - a delayed or disorganized response directly extends breach dwell time and scope |
| **Risk Rating** | 6 - High |
| **(e) Determined Frequency** | Formal training **annually**, with a **tabletop exercise every 6 months** and immediate ad hoc refresh triggered by any IR team membership change |
| **Rationale** | The annual/semi-annual split addresses both formal knowledge currency and practical readiness; the membership-change trigger directly closes the exact gap the prior tabletop exercise surfaced |
| **(f) Sign-off** | Reviewed and approved by [Risk Owner], [Date] |

---

## 6. Governance, Review Cycle & Sign-Off

- **Full TRA set reviewed:** at least once every 12 months, per PCI DSS v4.0.1 requirement, regardless of whether any individual frequency changes.
- **Ad hoc triggers:** any material change to the underlying environment (new system classification, incident, architecture change, or control failure) requires the affected TRA to be re-run outside the annual cycle - the TRA is invalid the moment its stated assumptions no longer hold, not just when the calendar says so.
- **Ownership:** each TRA has a named risk owner accountable for the conclusion, distinct from whoever performs the underlying activity - this separation is what a QSA is checking for when they ask "who approved this frequency."
- **Version control:** every TRA revision is logged with date, author, and reason for change, so the analysis has an audit trail of its own, not just a static conclusion.

---


---

*This template reflects methodology built through hands-on PCI DSS v4.0.1 compliance work, reconstructed here without any real environment, vendor, or client data. Requirement references are drawn from official PCI SSC v4.0.1 guidance on Targeted Risk Analysis.*
