# Zero-to-Audit-Ready Runbook: Building a GRC Program From Scratch

**Author:** Victor Eboh, GRC Lead, Information Security & Compliance

**Purpose:** The operating sequence for taking an organization with no formal compliance program to a clean first-attempt audit opinion (SOC 2 Type II and/or ISO 27001), and keeping it clean on every cycle after. Written as a runbook, not a framework overview. This assumes you already know what SOC 2 and ISO 27001 require, and documents the order of operations that determines whether the first audit passes or generates a findings list.

> **Note on this artifact:** This runbook reflects a methodology built through hands-on program-building work. All company references below are fictional (**"Meridian Retail Co."**) and provided to demonstrate process only. No client, employer, or real-environment data is used anywhere in this document.

---

## Table of Contents

1. [Why Order of Operations Matters](#1-why-order-of-operations-matters)
2. [Scope & Assumptions](#2-scope--assumptions)
3. [Timeline at a Glance](#3-timeline-at-a-glance)
4. [The Eight Phases](#4-the-eight-phases)
   - [Phase 0: Executive Alignment & Scope](#phase-0--executive-alignment--scope)
   - [Phase 1: Framework & Control Selection](#phase-1--framework--control-selection)
   - [Phase 2: Gap Assessment](#phase-2--gap-assessment)
   - [Phase 3: Control Design & Remediation](#phase-3--control-design--remediation)
   - [Phase 4: Evidence Operationalization](#phase-4--evidence-operationalization)
   - [Phase 5: Internal Readiness Review](#phase-5--internal-readiness-review)
   - [Phase 6: Audit Execution & Auditor Liaison](#phase-6--audit-execution--auditor-liaison)
   - [Phase 7: Post-Audit: Remediation & Continuous Operation](#phase-7--post-audit-remediation--continuous-operation)
5. [The Mistake That Kills First-Attempt Audits](#5-the-mistake-that-kills-first-attempt-audits)
6. [Ownership Model](#6-ownership-model)
7. [Maintenance](#7-maintenance)

---

## 1. Why Order of Operations Matters

Most failed first-attempt audits aren't caused by missing controls. They're caused by doing the right things in the wrong sequence. The most common failure pattern: a team designs controls before scoping, builds evidence collection as a pre-audit scramble instead of an operating habit, and only discovers gaps during the actual audit fieldwork instead of months earlier when there was still time to fix them cheaply.

This runbook is sequenced deliberately. Each phase produces an input the next phase depends on. Skipping ahead, starting control design before the gap assessment is done for instance, doesn't save time. It just moves the rework to a more expensive point later in the cycle, usually the week before the auditor shows up.

---

## 2. Scope & Assumptions

This runbook assumes:
- The organization is pursuing SOC 2 Type II and/or ISO 27001 for the first time, with no pre-existing formal GRC function
- A single accountable owner exists for the program (see [Section 6](#6-ownership-model))
- Executive sponsorship exists or is being actively secured in Phase 0. This runbook does not cover how to build that business case, only what to do once it exists

It is framework-agnostic in structure but written primarily against SOC 2 and ISO 27001, since those two are most commonly pursued together and share the highest control overlap (see the [SOC 2 / ISO 27001 / PCI DSS crosswalk](../crosswalk) elsewhere in this repo). Where PCI DSS is also in scope, Phase 1 and Phase 3 both reference the crosswalk directly rather than duplicating the control-selection logic here.

---

## 3. Timeline at a Glance

| Phase | Typical Duration (First Cycle) | Can Run in Parallel With |
|---|---|---|
| 0: Executive Alignment & Scope | 2–4 weeks | None |
| 1: Framework & Control Selection | 2–3 weeks | Phase 0 (final weeks) |
| 2: Gap Assessment | 3–6 weeks | None |
| 3: Control Design & Remediation | 8–16 weeks | Phase 4 (early controls) |
| 4: Evidence Operationalization | 4–8 weeks, then continuous | Phase 3 (later stages) |
| 5: Internal Readiness Review | 2–3 weeks | None |
| 6: Audit Execution | 4–8 weeks (SOC 2 Type II observation period is separate, see Phase 6) | None |
| 7: Post-Audit | Continuous | None |

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

Victor Eboh, GRC Lead | [LinkedIn](https://www.linkedin.com/in/evictorc/)| 7 - Post-Audit | Continuous | - |

A realistic first-cycle timeline from Phase 0 kickoff to audit report in hand runs **9–14 months** for SOC 2 Type II specifically, because Type II requires an operating-effectiveness observation window (commonly 6 months minimum) layered on top of the control-build work - that window is often the most underestimated part of the whole timeline by teams new to the process.

---

## 4. The Eight Phases

### Phase 0 - Executive Alignment & Scope

**Objective:** Establish who owns this program, what's actually in scope, and what "done" means before any control work begins.

**Key activities:**
- Identify the executive sponsor and the program owner (may be the same person; document it either way)
- Define system/environment scope - which products, which infrastructure, which data flows are actually in the audit boundary
- Set the target framework(s) and target audit window
- Establish a standing reporting cadence to leadership before it's needed, not after the first delay

**Deliverable:** A one-page scope charter - sponsor, owner, in-scope systems, target framework, target date.

**Common failure point:** Scope creep discovered mid-Phase 3, when someone realizes a system everyone assumed was out of scope is actually in it. This is why scope gets written down and signed off in Phase 0, not held as tribal knowledge.

---

### Phase 1 - Framework & Control Selection

**Objective:** Translate the target framework's requirements into a concrete control list mapped to the organization's actual environment.

**Key activities:**
- Select the specific Trust Services Criteria (for SOC 2) or confirm Annex A applicability and draft the Statement of Applicability (for ISO 27001)
- If multiple frameworks are in scope, build the control list from the overlap first - see the [crosswalk](../crosswalk) for where SOC 2, ISO 27001, and PCI DSS controls converge, so the same evidence satisfies more than one framework from day one
- Assign a control owner to every control before Phase 2 starts, even provisionally - Phase 2 needs someone to interview

**Deliverable:** A control matrix - control ID, framework citation(s), owner, current status (not yet assessed).

**Common failure point:** Selecting every possible control instead of scoping to what's actually applicable. Over-scoping in Phase 1 multiplies the cost of every phase after it.

---

### Phase 2 - Gap Assessment

**Objective:** Establish the honest current-state baseline against the control matrix from Phase 1 - what exists, what's partial, what doesn't exist at all.

**Key activities:**
- Interview each control owner; don't rely solely on policy documents, since a written policy with no operating evidence behind it is a gap, not a pass
- Rate each control: Implemented / Partially Implemented / Not Implemented
- For every gap, capture the remediation effort estimate, not just the gap itself - this feeds directly into Phase 3 sequencing

**Deliverable:** A gap assessment report, prioritized by remediation effort and audit risk, not alphabetically by control ID.

**Common failure point:** Treating the gap assessment as a compliance exercise instead of an engineering-effort estimate. The output needs to be usable by whoever is prioritizing Phase 3 work, which means every gap needs an effort size attached, not just a pass/fail rating.

---

### Phase 3 - Control Design & Remediation

**Objective:** Close the gaps identified in Phase 2, in priority order, with each control built to produce evidence as a byproduct of normal operation rather than as a separate audit-time task.

**Key activities:**
- Sequence remediation by a combination of audit risk and dependency - access control and logging typically come first, since later controls (incident response, vendor management) often depend on them being operational
- Design every control with its evidence artifact defined at the same time as the control itself - "how will we prove this happened" is a design question, not an afterthought
- Where a control spans multiple frameworks, build it once to the strictest framework's standard (the [crosswalk](../crosswalk) flags where that matters - encryption key management and vendor acknowledgment being the two most common places a "close enough" control fails the stricter framework)

**Deliverable:** Each control moved from Not Implemented / Partial to Implemented, with a named evidence source.

**Common failure point:** Building the control but not the evidence trail. A control that works but produces no artifact is functionally invisible to an auditor.

---

### Phase 4 - Evidence Operationalization

**Objective:** Make evidence collection a routine operational habit before the audit period begins, not a retroactive scramble once it's underway.

**Key activities:**
- Automate evidence collection wherever the control allows it (ticketing exports, cloud config snapshots, access review exports) - manual evidence collection is the single biggest source of audit-week fire drills
- Establish an evidence calendar: what gets collected, how often, and by whom, independent of the audit timeline
- Run a dry-run evidence pull partway through this phase - request a sample of evidence exactly as an auditor would, and see what actually comes back

**Deliverable:** A live evidence repository, populated on a recurring schedule, not assembled after the fact.

**Common failure point:** Treating evidence collection as something that starts when the audit starts. For SOC 2 Type II specifically, the observation period requires evidence generated *before* the audit fieldwork begins - evidence operationalized in Phase 4 is what makes that observation period possible at all, not just easier.

---

### Phase 5 - Internal Readiness Review

**Objective:** Find the findings before the auditor does.

**Key activities:**
- Run a mock audit against the full control matrix, using someone who wasn't involved in building the controls if at all possible - fresh eyes catch what builders have stopped seeing
- Pull evidence for a sample of controls exactly as the external auditor will, and score it pass/fail against what an auditor would actually accept
- Remediate anything that fails the mock audit before the real one starts - this is the last cheap point to fix a gap; every phase after this gets progressively more expensive to fix in

**Deliverable:** A readiness scorecard and a final remediation list, closed out before Phase 6 begins.

**Common failure point:** Skipping this phase under schedule pressure. It's the single highest-leverage phase in the entire runbook for the effort it takes, because every finding caught here is a finding that doesn't appear in the actual audit report.

---

### Phase 6 - Audit Execution & Auditor Liaison

**Objective:** Run the actual audit engagement efficiently, with the program owner as the single point of coordination.

**Key activities:**
- Single point of contact for all evidence requests - routing every request through one person prevents duplicate or inconsistent responses across control owners
- Track every evidence request and its status in a PBC (provided-by-client) tracker, visible to the audit team and leadership both
- For SOC 2 Type II, remember the audit report covers the full observation period, not just the point-in-time fieldwork - evidence gaps discovered here can mean gaps in that historical window that can't be retroactively created, which is exactly why Phase 4 matters as much as it does

**Deliverable:** Completed audit fieldwork, all PBC items closed, exit meeting held.

**Common failure point:** Letting individual control owners respond directly and inconsistently to auditor requests instead of routing through the program owner - this creates contradictory answers to the same underlying question, which reads as a control weakness even when the control itself is fine.

---

### Phase 7 - Post-Audit: Remediation & Continuous Operation

**Objective:** Close any findings, and convert the program from a one-time project into a standing operational function.

**Key activities:**
- Remediate any findings with a documented timeline and owner, tracked the same way Phase 2's gaps were tracked
- Fold the evidence calendar from Phase 4 into permanent operating rhythm - this is what makes the next audit cycle a maintenance exercise instead of a repeat of Phases 2–5
- Schedule the next cycle's Phase 5 mock audit before the current cycle's memory fades - this is cheaper to plan while the process is fresh than to reconstruct a year later

**Deliverable:** A closed findings log and a standing operating calendar for the next cycle.

**Common failure point:** Treating a clean audit opinion as the finish line instead of the baseline. Programs that don't operationalize past Phase 7 tend to rediscover the same gaps on the next cycle, effectively repeating Phases 2 through 5 from scratch.

---

## 5. The Mistake That Kills First-Attempt Audits

If this runbook has one governing principle, it's this: **evidence collection has to be operationalized before the audit period starts, not built to satisfy it once it's underway.** Every phase in this runbook either builds toward that (Phases 1–4) or depends on it already being true (Phases 5–7).

Teams that treat audit prep as a sprint that starts a few weeks before the auditor arrives are, structurally, trying to prove months of consistent operation using days of evidence. That's not a documentation problem to fix with better templates - it's a sequencing problem, and it's the reason this runbook exists as an ordered process rather than a checklist.

---

## 6. Ownership Model

| Role | Responsibility |
|---|---|
| **Executive Sponsor** | Removes organizational blockers, approves resourcing, receives the standing reporting cadence from Phase 0 |
| **Program Owner** | Owns the runbook end to end; single point of contact for the auditor in Phase 6; accountable for the Phase 7 operating calendar |
| **Control Owners** | Accountable for their assigned controls' implementation and evidence, but route all audit communication through the Program Owner |
| **Internal Reviewer (Phase 5)** | Ideally independent of the build work - brought in specifically to avoid the blind spots builders develop toward their own controls |

---

## 7. Maintenance

Re-validate this runbook's phase sequencing at least once per audit cycle - frameworks change (PCI DSS version updates, ISO Annex A revisions), and what counted as sufficient evidence on the last cycle may not on the next. The phases themselves are durable; the specific controls and evidence standards inside each one are not.

---

*Part of the [GRC Toolkit](https://github.com/ebohc/grc-toolkit) - built to work alongside the [PCI DSS v4.0.1 TRA template](../pci-dss-tra) and the [SOC 2 / ISO 27001 / PCI DSS crosswalk](../crosswalk) elsewhere in this repo.*

Victor Eboh - GRC Lead | [LinkedIn](https://www.linkedin.com/in/evictorc/)
