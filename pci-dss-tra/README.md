# PCI DSS v4.0.1 Targeted Risk Analysis (TRA) Template and Methodology

**Author:** Victor Eboh, GRC Lead, Information Security & Compliance
**Purpose:** A reusable, audit-ready Targeted Risk Analysis framework built to PCI DSS v4.0.1 Requirement 12.3.1, covering the eight control domains where PCI DSS grants an entity flexibility to self-define activity frequency.

> **Note on this artifact:** This is an original template built from professional GRC practice. All entity names, environments, findings, and risk ratings below are fictional (**"Meridian Retail Co."**) and provided to demonstrate methodology only. No client, employer, or real-environment data is used anywhere in this document.

---

## Table of Contents

1. [Why This Exists](#1-why-this-exists)
2. [TRA Methodology](#2-tra-methodology)
3. [Required Elements per Requirement 12.3.1](#3-required-elements-per-requirement-1231)
4. [Risk Scoring Model](#4-risk-scoring-model)
5. [The Eight TRAs](#5-the-eight-tras)
   - [5.1. TRA-01: Malware Evaluation Frequency (Req. 5.2.3.1)](#51-tra-01-malware-evaluation-frequency-req-5231)
   - [5.2. TRA-02: Removable Media Scan Frequency (Req. 5.3.2.1)](#52-tra-02-removable-media-scan-frequency-req-5321)
   - [5.3. TRA-03: User Account & Access Privilege Review Frequency (Req. 7.2.5.1)](#53-tra-03-user-account--access-privilege-review-frequency-req-7251)
   - [5.4. TRA-04: System/Application Account Password Change Frequency (Req. 8.6.3)](#54-tra-04-systemapplication-account-password-change-frequency-req-863)
   - [5.5. TRA-05: Log Review Frequency for Non-Critical Systems (Req. 10.4.2.1)](#55-tra-05-log-review-frequency-for-non-critical-systems-req-10421)
   - [5.6. TRA-06: Remediation Timeline for Non-Critical Vulnerabilities (Req. 11.3.1.1)](#56-tra-06-remediation-timeline-for-non-critical-vulnerabilities-req-11311)
   - [5.7. TRA-07: Payment Page Tamper-Detection Review Frequency (Req. 11.6.1)](#57-tra-07-payment-page-tamper-detection-review-frequency-req-1161)
   - [5.8. TRA-08: Incident Response Training Frequency (Req. 12.10.4.1)](#58-tra-08-incident-response-training-frequency-req-121041)
6. [Governance, Review Cycle & Sign-Off](#6-governance-review-cycle--sign-off)
7. [Blank Template (Copy/Paste)](#7-blank-template-copypaste)

---

## 1. Why This Exists

PCI DSS v4.0.1 replaced the old model, a single annual, entity-wide risk assessment, with **Targeted Risk Analyses**: narrow, requirement-specific analyses that justify *why* a chosen frequency or approach is appropriate, tied to the entity's actual assets, threats, and risk appetite. Requirement 12.3.1 applies specifically wherever PCI DSS says an activity must happen "periodically" or "as appropriate" rather than on a fixed schedule.

Most organizations treat this as a documentation exercise and produce eight (or more) TRAs that all reach the same generic conclusion, with no real risk logic behind the number they pick. A QSA can tell the difference between a TRA that was actually reasoned through and one that was reverse-engineered to justify whatever frequency the team already wanted. This template is built to survive that scrutiny. Every conclusion traces back through a documented risk score, not a preference.

---

## 2. TRA Methodology

Each TRA in this template follows the same five-stage process, applied independently per requirement. This is the core discipline of a *targeted* analysis rather than an enterprise-wide one:

| Stage | What Happens | Output |
|---|---|---|
| **1. Scope the control** | Identify the exact PCI DSS sub-requirement, the assets it protects, and the specific activity whose frequency is being justified. | Scope statement |
| **2. Identify threats & vulnerabilities** | Map realistic threat scenarios against the asset if the activity were performed *less* often than proposed. | Threat/vulnerability list |
| **3. Score likelihood & impact** | Rate each threat scenario using the scoring model in Section 4. | Likelihood × Impact = Risk Rating |
| **4. Determine frequency** | Select a frequency that reduces residual risk to an acceptable level, referencing the risk rating, not the other way around. | Defined frequency + rationale |
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

Every TRA below is structured to hit all six elements explicitly. This is the checklist a QSA will actually run your documentation against, so the template enforces it by section header rather than leaving it to memory.

---

## 4. Risk Scoring Model

A simple 3×3 qualitative matrix, chosen deliberately over a more elaborate model. PCI DSS does not require quantitative scoring, and an overbuilt model is harder to defend consistently across eight TRAs than a transparent, repeatable one.

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

### 5.1. TRA-01: Malware Evaluation Frequency (Req. 5.2.3.1)

| Field | Detail |
|---|---|
| **Requirement** | 5.2.3.1: Frequency of evaluating system components identified as not at risk for malware |
| **(a) Assets** | Point-of-sale terminals, back-office workstations, and application servers within the CDE not currently running active anti-malware due to system type/function |
| **(b) Threat/Vulnerability** | Introduction of malware via removable media, lateral movement from a compromised adjacent system, or a change in system function that invalidates the "not at risk" classification |
| **(c) Prior incidents** | None recorded in the trailing 12 months for in-scope system types |
| **(d) Likelihood & Impact if under-evaluated** | Likelihood: **2 (Medium)**. System classification can silently drift as software/config changes. Impact: **3 (High)**. Undetected malware on a CDE-adjacent system risks direct cardholder data exposure |
| **Risk Rating** | 6 (High) |
| **(e) Determined Frequency** | Re-evaluation of "not at risk" classification every **90 days**, with an ad hoc trigger on any change-management ticket touching the system's function or network placement |
| **Rationale** | A 90-day cycle is short enough to catch classification drift within a single quarterly change-review cadence, and the change-triggered re-evaluation closes the gap between scheduled reviews rather than relying on the schedule alone |
| **(f) Sign-off** | Reviewed and approved by [Risk Owner], [Date] |

---

### 5.2. TRA-02: Removable Media Scan Frequency (Req. 5.3.2.1)

| Field | Detail |
|---|---|
| **Requirement** | 5.3.2.1: Frequency of periodic malware scans (in lieu of active/real-time scanning) |
| **(a) Assets** | Legacy back-office file servers where real-time anti-malware degrades application performance |
| **(b) Threat/Vulnerability** | Malware persistence between scheduled scans; dwell time before detection |
| **(c) Prior incidents** | One low-severity detection 8 months prior, commodity malware, contained, no CDE impact |
| **(d) Likelihood & Impact** | Likelihood: **2 (Medium)**. Prior detection shows the vector is live, though contained. Impact: **2 (Medium)**. System is CDE-adjacent, not CDE-storing |
| **Risk Rating** | 4 (Moderate) |
| **(e) Determined Frequency** | Full scan **weekly**, with real-time scanning re-evaluated annually as hardware refresh may remove the original performance constraint |
| **Rationale** | Weekly scanning bounds maximum dwell time to a level consistent with the moderate risk rating; the annual re-evaluation prevents the exception from becoming permanent by default |
| **(f) Sign-off** | Reviewed and approved by [Risk Owner], [Date] |

---

### 5.3. TRA-03: User Account & Access Privilege Review Frequency (Req. 7.2.5.1)

| Field | Detail |
|---|---|
| **Requirement** | 7.2.5.1: Frequency of reviewing user accounts and access privileges |
| **(a) Assets** | User and service accounts with access to systems storing, processing, or transmitting cardholder data |
| **(b) Threat/Vulnerability** | Privilege creep from role changes; orphaned accounts following offboarding; excessive standing access enabling insider misuse or lateral movement post-compromise |
| **(c) Prior incidents** | Internal audit (prior cycle) identified 3 stale accounts from role transfers, remediated within SLA |
| **(d) Likelihood & Impact** | Likelihood: **2 (Medium)**. Organization has moderate personnel turnover and prior evidence of drift. Impact: **3 (High)**. Excess CDE access is a direct escalation path |
| **Risk Rating** | 6 (High) |
| **(e) Determined Frequency** | Full access review **quarterly**, with an automated offboarding trigger disabling access within 24 hours of HR termination record |
| **Rationale** | Quarterly review addresses gradual privilege creep; the automated offboarding trigger addresses the higher-risk, time-sensitive termination scenario separately rather than relying on the quarterly cycle to catch it |
| **(f) Sign-off** | Reviewed and approved by [Risk Owner], [Date] |

---

### 5.4. TRA-04: System/Application Account Password Change Frequency (Req. 8.6.3)

| Field | Detail |
|---|---|
| **Requirement** | 8.6.3: Frequency of changing passwords/passphrases for application and system accounts (default: 90 days, extendable if justified by TRA) |
| **(a) Assets** | Service accounts used for application-to-database and application-to-application authentication within the CDE |
| **(b) Threat/Vulnerability** | Credential compromise via exposure in logs, code repositories, or configuration files; extended validity window increases exposure time if leaked |
| **(c) Prior incidents** | None recorded; accounts are managed through a secrets vault with access logging |
| **(d) Likelihood & Impact** | Likelihood: **1 (Low)**. Vaulted, logged, no human interactive use, rotation independent of memorization. Impact: **3 (High)**. Compromise of a service account is a direct CDE access path |
| **Risk Rating** | 3 (Moderate) |
| **(e) Determined Frequency** | **180 days**, contingent on continued vault enforcement, access logging, and absence of any credential-exposure event |
| **Rationale** | The extended interval is justified specifically because compensating controls (vaulting, logging, no human memorization) lower likelihood; the TRA explicitly ties the extension to those controls remaining in place, so it is invalidated automatically if the vault is ever bypassed |
| **(f) Sign-off** | Reviewed and approved by [Risk Owner], [Date] |

---

### 5.5. TRA-05: Log Review Frequency for Non-Critical Systems (Req. 10.4.2.1)

| Field | Detail |
|---|---|
| **Requirement** | 10.4.2.1: Frequency of log reviews for system components not defined as critical under 10.4.1 |
| **(a) Assets** | Non-critical internal systems (e.g., internal reporting tools) with no direct CDE data path |
| **(b) Threat/Vulnerability** | Delayed detection of anomalous activity that could indicate reconnaissance or staging ahead of a pivot toward in-scope systems |
| **(c) Prior incidents** | None recorded for this system tier |
| **(d) Likelihood & Impact** | Likelihood: **1 (Low)**. No direct CDE connectivity, limited attacker interest as a primary target. Impact: **2 (Medium)**. Could serve as a staging point even without direct data access |
| **Risk Rating** | 2 (Low) |
| **(e) Determined Frequency** | Log review **weekly**, via automated SIEM correlation rules with alert-based escalation outside the weekly cycle |
| **Rationale** | The low risk rating supports an extended manual review interval, but automated correlation rules close the gap for any activity that shouldn't wait a week. The TRA frequency governs the *scheduled* review, not the detection capability itself |
| **(f) Sign-off** | Reviewed and approved by [Risk Owner], [Date] |

---

### 5.6. TRA-06: Remediation Timeline for Non-Critical Vulnerabilities (Req. 11.3.1.1)

| Field | Detail |
|---|---|
| **Requirement** | 11.3.1.1: Approach for addressing vulnerabilities not ranked as high-risk or critical per the entity's risk ranking |
| **(a) Assets** | All CDE and CDE-connected systems subject to internal vulnerability scanning |
| **(b) Threat/Vulnerability** | Accumulation of unpatched medium/low findings that, chained together, could enable an attack path even without a single critical vulnerability |
| **(c) Prior incidents** | None; medium/low findings have historically closed within informal timelines averaging ~45 days |
| **(d) Likelihood & Impact** | Likelihood: **2 (Medium)**. Chaining risk is real but requires multiple conditions. Impact: **2 (Medium)**. No single finding provides direct CDE compromise |
| **Risk Rating** | 4 (Moderate) |
| **(e) Determined Frequency** | Medium findings remediated within **30 days**, low findings within **90 days**, both tracked against a formal SLA rather than the prior informal average |
| **Rationale** | Formalizing the SLA at a tighter interval than the historical average reduces the chaining window without requiring the same treatment as critical findings, matching effort to the moderate rather than high risk rating |
| **(f) Sign-off** | Reviewed and approved by [Risk Owner], [Date] |

---

### 5.7. TRA-07: Payment Page Tamper-Detection Review Frequency (Req. 11.6.1)

| Field | Detail |
|---|---|
| **Requirement** | 11.6.1: Frequency of reviewing the change-and-tamper-detection mechanism for payment pages |
| **(a) Assets** | Customer-facing checkout and payment pages served to cardholders |
| **(b) Threat/Vulnerability** | E-skimming (e.g., Magecart-style) script injection going undetected between review cycles |
| **(c) Prior incidents** | None recorded; industry threat pattern for e-skimming is active and well-documented |
| **(d) Likelihood & Impact** | Likelihood: **3 (High)**. E-skimming is an active, industry-wide attack pattern against payment pages specifically. Impact: **3 (High)**. Direct, large-scale cardholder data exposure at the point of capture |
| **Risk Rating** | 9 (High) |
| **(e) Determined Frequency** | Automated, continuous monitoring with alerting, supplemented by a **weekly** manual verification review |
| **Rationale** | The high risk rating on both axes rules out any extended manual-only interval; this is the one TRA in the set where the conclusion is that flexibility should be used minimally, not maximally. The TRA still documents the reasoning even though the outcome is "stay tight" |
| **(f) Sign-off** | Reviewed and approved by [Risk Owner], [Date] |

---

### 5.8. TRA-08: Incident Response Training Frequency (Req. 12.10.4.1)

| Field | Detail |
|---|---|
| **Requirement** | 12.10.4.1: Frequency of incident response personnel training |
| **(a) Assets** | Incident response team roles and their operational readiness |
| **(b) Threat/Vulnerability** | Degraded response effectiveness from outdated procedures, tool changes, or team turnover between training cycles |
| **(c) Prior incidents** | One tabletop exercise (prior cycle) identified a 20-minute delay in escalation path due to an outdated contact list |
| **(d) Likelihood & Impact** | Likelihood: **2 (Medium)**. Team composition and tooling change often enough to erode readiness within a year. Impact: **3 (High)**. A delayed or disorganized response directly extends breach dwell time and scope |
| **Risk Rating** | 6 (High) |
| **(e) Determined Frequency** | Formal training **annually**, with a **tabletop exercise every 6 months** and immediate ad hoc refresh triggered by any IR team membership change |
| **Rationale** | The annual/semi-annual split addresses both formal knowledge currency and practical readiness; the membership-change trigger directly closes the exact gap the prior tabletop exercise surfaced |
| **(f) Sign-off** | Reviewed and approved by [Risk Owner], [Date] |

---

## 6. Governance, Review Cycle & Sign-Off

- **Full TRA set reviewed:** at least once every 12 months, per PCI DSS v4.0.1 requirement, regardless of whether any individual frequency changes.
- **Ad hoc triggers:** any material change to the underlying environment (new system classification, incident, architecture change, or control failure) requires the affected TRA to be re-run outside the annual cycle. The TRA is invalid the moment its stated assumptions no longer hold, not just when the calendar says so.
- **Ownership:** each TRA has a named risk owner accountable for the conclusion, distinct from whoever performs the underlying activity. This separation is what a QSA is checking for when they ask "who approved this frequency."
- **Version control:** every TRA revision is logged with date, author, and reason for change, so the analysis has an audit trail of its own, not just a static conclusion.

---

## 7. Blank Template (Copy/Paste)

```markdown
### TRA-XX: [Activity Name] (Req. X.X.X.X)

| Field | Detail |
|---|---|
| **Requirement** | |
| **(a) Assets** | |
| **(b) Threat/Vulnerability** | |
| **(c) Prior incidents** | |
| **(d) Likelihood & Impact** | Likelihood: **_ (___)**. Reasoning. Impact: **_ (___)**. Reasoning |
| **Risk Rating** | |
| **(e) Determined Frequency** | |
| **Rationale** | |
| **(f) Sign-off** | Reviewed and approved by [Risk Owner], [Date] |
```

---

*This template reflects methodology built through hands-on PCI DSS v4.0.1 compliance work, reconstructed here without any real environment, vendor, or client data. Requirement references are drawn from official PCI SSC v4.0.1 guidance on Targeted Risk Analysis.*| 7: Post-Audit | Continuous | None |

A realistic first-cycle timeline from Phase 0 kickoff to audit report in hand runs **9–14 months** for SOC 2 Type II specifically, because Type II requires an operating-effectiveness observation window (commonly 6 months minimum) layered on top of the control-build work. That window is often the most underestimated part of the whole timeline by teams new to the process.

---

## 4. The Eight Phases

### Phase 0: Executive Alignment & Scope

**Objective:** Establish who owns this program, what's actually in scope, and what "done" means before any control work begins.

**Key activities:**
- Identify the executive sponsor and the program owner (may be the same person; document it either way)
- Define system/environment scope: which products, which infrastructure, which data flows are actually in the audit boundary
- Set the target framework(s) and target audit window
- Establish a standing reporting cadence to leadership before it's needed, not after the first delay

**Deliverable:** A one-page scope charter: sponsor, owner, in-scope systems, target framework, target date.

**Common failure point:** Scope creep discovered mid-Phase 3, when someone realizes a system everyone assumed was out of scope is actually in it. This is why scope gets written down and signed off in Phase 0, not held as tribal knowledge.

---

### Phase 1: Framework & Control Selection

**Objective:** Translate the target framework's requirements into a concrete control list mapped to the organization's actual environment.

**Key activities:**
- Select the specific Trust Services Criteria (for SOC 2) or confirm Annex A applicability and draft the Statement of Applicability (for ISO 27001)
- If multiple frameworks are in scope, build the control list from the overlap first. See the [crosswalk](../crosswalk) for where SOC 2, ISO 27001, and PCI DSS controls converge, so the same evidence satisfies more than one framework from day one
- Assign a control owner to every control before Phase 2 starts, even provisionally. Phase 2 needs someone to interview

**Deliverable:** A control matrix: control ID, framework citation(s), owner, current status (not yet assessed).

**Common failure point:** Selecting every possible control instead of scoping to what's actually applicable. Over-scoping in Phase 1 multiplies the cost of every phase after it.

---

### Phase 2: Gap Assessment

**Objective:** Establish the honest current-state baseline against the control matrix from Phase 1: what exists, what's partial, what doesn't exist at all.

**Key activities:**
- Interview each control owner; don't rely solely on policy documents, since a written policy with no operating evidence behind it is a gap, not a pass
- Rate each control: Implemented / Partially Implemented / Not Implemented
- For every gap, capture the remediation effort estimate, not just the gap itself. This feeds directly into Phase 3 sequencing

**Deliverable:** A gap assessment report, prioritized by remediation effort and audit risk, not alphabetically by control ID.

**Common failure point:** Treating the gap assessment as a compliance exercise instead of an engineering-effort estimate. The output needs to be usable by whoever is prioritizing Phase 3 work, which means every gap needs an effort size attached, not just a pass/fail rating.

---

### Phase 3: Control Design & Remediation

**Objective:** Close the gaps identified in Phase 2, in priority order, with each control built to produce evidence as a byproduct of normal operation rather than as a separate audit-time task.

**Key activities:**
- Sequence remediation by a combination of audit risk and dependency. Access control and logging typically come first, since later controls (incident response, vendor management) often depend on them being operational
- Design every control with its evidence artifact defined at the same time as the control itself. "How will we prove this happened" is a design question, not an afterthought
- Where a control spans multiple frameworks, build it once to the strictest framework's standard (the [crosswalk](../crosswalk) flags where that matters: encryption key management and vendor acknowledgment are the two most common places a "close enough" control fails the stricter framework)

**Deliverable:** Each control moved from Not Implemented / Partial to Implemented, with a named evidence source.

**Common failure point:** Building the control but not the evidence trail. A control that works but produces no artifact is functionally invisible to an auditor.

---

### Phase 4: Evidence Operationalization

**Objective:** Make evidence collection a routine operational habit before the audit period begins, not a retroactive scramble once it's underway.

**Key activities:**
- Automate evidence collection wherever the control allows it (ticketing exports, cloud config snapshots, access review exports). Manual evidence collection is the single biggest source of audit-week fire drills
- Establish an evidence calendar: what gets collected, how often, and by whom, independent of the audit timeline
- Run a dry-run evidence pull partway through this phase. Request a sample of evidence exactly as an auditor would, and see what actually comes back

**Deliverable:** A live evidence repository, populated on a recurring schedule, not assembled after the fact.

**Common failure point:** Treating evidence collection as something that starts when the audit starts. For SOC 2 Type II specifically, the observation period requires evidence generated *before* the audit fieldwork begins. Evidence operationalized in Phase 4 is what makes that observation period possible at all, not just easier.

---

### Phase 5: Internal Readiness Review

**Objective:** Find the findings before the auditor does.

**Key activities:**
- Run a mock audit against the full control matrix, using someone who wasn't involved in building the controls if at all possible. Fresh eyes catch what builders have stopped seeing
- Pull evidence for a sample of controls exactly as the external auditor will, and score it pass/fail against what an auditor would actually accept
- Remediate anything that fails the mock audit before the real one starts. This is the last cheap point to fix a gap; every phase after this gets progressively more expensive to fix in

**Deliverable:** A readiness scorecard and a final remediation list, closed out before Phase 6 begins.

**Common failure point:** Skipping this phase under schedule pressure. It's the single highest-leverage phase in the entire runbook for the effort it takes, because every finding caught here is a finding that doesn't appear in the actual audit report.

---

### Phase 6: Audit Execution & Auditor Liaison

**Objective:** Run the actual audit engagement efficiently, with the program owner as the single point of coordination.

**Key activities:**
- Single point of contact for all evidence requests. Routing every request through one person prevents duplicate or inconsistent responses across control owners
- Track every evidence request and its status in a PBC (provided-by-client) tracker, visible to the audit team and leadership both
- For SOC 2 Type II, remember the audit report covers the full observation period, not just the point-in-time fieldwork. Evidence gaps discovered here can mean gaps in that historical window that can't be retroactively created, which is exactly why Phase 4 matters as much as it does

**Deliverable:** Completed audit fieldwork, all PBC items closed, exit meeting held.

**Common failure point:** Letting individual control owners respond directly and inconsistently to auditor requests instead of routing through the program owner. This creates contradictory answers to the same underlying question, which reads as a control weakness even when the control itself is fine.

---

### Phase 7: Post-Audit: Remediation & Continuous Operation

**Objective:** Close any findings, and convert the program from a one-time project into a standing operational function.

**Key activities:**
- Remediate any findings with a documented timeline and owner, tracked the same way Phase 2's gaps were tracked
- Fold the evidence calendar from Phase 4 into permanent operating rhythm. This is what makes the next audit cycle a maintenance exercise instead of a repeat of Phases 2 through 5
- Schedule the next cycle's Phase 5 mock audit before the current cycle's memory fades. This is cheaper to plan while the process is fresh than to reconstruct a year later

**Deliverable:** A closed findings log and a standing operating calendar for the next cycle.

**Common failure point:** Treating a clean audit opinion as the finish line instead of the baseline. Programs that don't operationalize past Phase 7 tend to rediscover the same gaps on the next cycle, effectively repeating Phases 2 through 5 from scratch.

---

## 5. The Mistake That Kills First-Attempt Audits

If this runbook has one governing principle, it's this: **evidence collection has to be operationalized before the audit period starts, not built to satisfy it once it's underway.** Every phase in this runbook either builds toward that (Phases 1–4) or depends on it already being true (Phases 5–7).

Teams that treat audit prep as a sprint that starts a few weeks before the auditor arrives are, structurally, trying to prove months of consistent operation using days of evidence. That's not a documentation problem to fix with better templates. It's a sequencing problem, and it's the reason this runbook exists as an ordered process rather than a checklist.

---

## 6. Ownership Model

| Role | Responsibility |
|---|---|
| **Executive Sponsor** | Removes organizational blockers, approves resourcing, receives the standing reporting cadence from Phase 0 |
| **Program Owner** | Owns the runbook end to end; single point of contact for the auditor in Phase 6; accountable for the Phase 7 operating calendar |
| **Control Owners** | Accountable for their assigned controls' implementation and evidence, but route all audit communication through the Program Owner |
| **Internal Reviewer (Phase 5)** | Ideally independent of the build work, brought in specifically to avoid the blind spots builders develop toward their own controls |

---

## 7. Maintenance

Re-validate this runbook's phase sequencing at least once per audit cycle. Frameworks change (PCI DSS version updates, ISO Annex A revisions), and what counted as sufficient evidence on the last cycle may not on the next. The phases themselves are durable; the specific controls and evidence standards inside each one are not.

---

*Part of the [GRC Toolkit](https://github.com/ebohc/grc-toolkit). Built to work alongside the [PCI DSS v4.0.1 TRA template](../pci-dss-tra) and the [SOC 2 / ISO 27001 / PCI DSS crosswalk](../crosswalk) elsewhere in this repo.*

Victor Eboh, GRC Lead | [LinkedIn](https://www.linkedin.com/in/evictorc/)
