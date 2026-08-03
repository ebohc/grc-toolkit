# PCI DSS v4.0.1 Customized Approach Playbook

**Author:** Victor Eboh, GRC Lead, Information Security & Compliance

**Purpose:** A complete, usable methodology for implementing and documenting the PCI DSS v4.0.1 Customized Approach: when it applies, how to build the required Controls Matrix and Targeted Risk Analysis, how to co-design a testing procedure a QSA will actually accept, and a fully worked example from scoping through documentation. Most PCI programs never touch this path. This is written for the ones that need to.

> **Note on this artifact:** This is an original methodology and template set built from professional GRC practice and PCI SSC public guidance. The worked example uses a fictional entity (**"Meridian Retail Co."**) and contains no client, employer, or real-environment data.

---

## Table of Contents

1. [Who This Is For](#1-who-this-is-for)
2. [Customized Approach vs Defined Approach vs Compensating Controls](#2-customized-approach-vs-defined-approach-vs-compensating-controls)
3. [Eligibility Gate](#3-eligibility-gate)
4. [The Required Documentation Package](#4-the-required-documentation-package)
5. [Methodology: Eight Steps](#5-methodology-eight-steps)
6. [Worked Example: Passwordless Authentication in Place of Req. 8.3.6 to 8.3.9](#6-worked-example-passwordless-authentication-in-place-of-req-836-to-839)
7. [Blank Controls Matrix Template](#7-blank-controls-matrix-template)
8. [Blank Targeted Risk Analysis Template (Customized Approach)](#8-blank-targeted-risk-analysis-template-customized-approach)
9. [Why QSAs Reject Customized Controls](#9-why-qsas-reject-customized-controls)
10. [Maintenance](#10-maintenance)

---

## 1. Who This Is For

PCI DSS v4.0.1 offers two paths to meeting any given requirement. The Defined Approach is the traditional path: follow the requirement and its printed testing procedure exactly as written. The Customized Approach is different in kind, not just in flexibility. It lets an entity design its own control to meet the requirement's stated security objective, using a method the standard's authors never anticipated, validated through a testing procedure the entity and its QSA design together rather than one PCI already wrote.

Almost nobody uses it. PCI SSC's own guidance says the Customized Approach is intended for organizations with an established, mature, risk-based security program, one where senior executives already understand and own risk decisions as a normal part of how the business runs, not as a compliance exercise bolted on top. If your organization needs a QSA's help to design the control in the first place, PCI's own guidance suggests you are not a good candidate, because you will also struggle to maintain and defend it on every subsequent audit cycle.

This playbook exists because that gap, between organizations that could benefit from this path and organizations that actually know how to execute it, is wide, and closing it is a genuinely rare skill.

---

## 2. Customized Approach vs Defined Approach vs Compensating Controls

These three get confused constantly, and mixing them up is one of the most common mistakes in PCI programs. The distinction comes down to intent, not mechanics.

| | Defined Approach | Compensating Controls | Customized Approach |
|---|---|---|---|
| **When you use it** | Standard path, no constraint | You **cannot** meet the requirement as written due to a genuine technical or business constraint | You **choose** to meet the requirement differently, by design, not by constraint |
| **What you're meeting** | The requirement as printed | The requirement as printed, via an alternative control that provides equivalent protection | The requirement's stated **Customized Approach Objective**, not the printed requirement text |
| **Testing procedure** | PCI's printed testing procedure | PCI's printed testing procedure, applied to the alternative control | A testing procedure you and your QSA design together; PCI's printed procedure does not apply |
| **Documentation** | Standard ROC entries | Appendix B worksheet | Controls Matrix (Appendix E1) and Targeted Risk Analysis (Appendix E2), reported in ROC Appendix E |
| **Can combine with the other?** | N/A | Not usable within a Customized Approach implementation, Appendix D makes this explicit | Not usable with compensating controls for the same requirement |

The critical point most teams get wrong: **compensating controls are not a lighter version of the Customized Approach.** A compensating control is what you reach for when something is broken or blocked. The Customized Approach is what you reach for when you have deliberately chosen a better or more modern way to achieve the same security outcome. If you cannot articulate why your approach is a deliberate improvement rather than a workaround, you are describing a compensating control, not a customized one, and you need to use that path instead.

---

## 3. Eligibility Gate

Before doing any design work, confirm the requirement and the entity actually qualify. This is where most Customized Approach attempts should stop before they start.

- **SAQ-eligible entities cannot use the Customized Approach.** It is only available through a full Report on Compliance (ROC) with a QSA. If your organization validates via Self-Assessment Questionnaire, this entire path is closed to you regardless of how mature your controls are.
- **The requirement must carry a stated Customized Approach Objective.** Not every PCI DSS requirement has one. Confirm the specific requirement you're targeting includes this language in the current version of the standard before designing anything against it.
- **Compensating controls are off the table for any requirement handled this way.** You cannot mix approaches on the same requirement.
- **Executive risk ownership has to be real, not nominal.** The required risk analysis must be reviewed and approved by an executive, and PCI's guidance is explicit that this only works when risk ownership is a genuine organizational habit, not a signature gathered once for the audit.
- **Engage the QSA before building anything.** PCI's own guidance to entities is to communicate early with the assessor about Customized Approach plans. A control designed in isolation and presented to the QSA after the fact has a materially higher rejection rate than one shaped collaboratively from the start.

If any of these fail, stop and use the Defined Approach or a compensating control instead. Forcing a Customized Approach through a QSA who was not consulted early is the single most common way this path fails expensively, late in an audit cycle.

---

## 4. The Required Documentation Package

Every requirement met through the Customized Approach needs all of the following, and PCI's own Appendix E1 guidance states plainly that the entity must provide this exact information to its assessor, not a summary of it.

| Document | What It Contains | PCI Reference |
|---|---|---|
| **Controls Matrix** | What the control is, how it operates, who owns and runs it, and how it meets the requirement's stated Customized Approach Objective | Appendix E1 |
| **Targeted Risk Analysis** | Analysis demonstrating the customized control is sufficiently robust to provide protection at least equivalent to the Defined Requirement it replaces | Req. 12.3.2, Appendix E2 |
| **Testing Procedure** | Co-designed with the QSA; validates the control actually meets the objective, since the standard's printed procedure no longer applies | Appendix D |
| **Executive Review Record** | Sign-off confirming the risk analysis was reviewed and approved at an appropriate level of the organization | Appendix D |
| **ROC Appendix E Entry** | The assessor's documentation of each instance where a customized control was used, including testing performed and results | ROC Template, Appendix E |

None of these are optional extras. A Customized Approach implementation missing any one of them is not audit-ready, regardless of how good the underlying control is.

---

## 5. Methodology: Eight Steps

**Step 1: Confirm eligibility.** Run the requirement and the organization through Section 3 above before doing any other work.

**Step 2: Extract the stated Customized Approach Objective.** Find the exact objective language PCI publishes for the target requirement. This is what you are actually being measured against, not the requirement's prescriptive text. Misreading the objective is the root cause of most rejected controls later in this process.

**Step 3: Design the control to meet the objective, not to resemble the original requirement.** A common failure mode is designing something that looks like a lighter version of the Defined Approach control. A genuine Customized Approach control should be justifiable on its own terms as meeting the objective, even to someone unfamiliar with how the Defined Approach handles it.

**Step 4: Build the Controls Matrix.** Use the structure in Section 7. Every field PCI requires must be filled in with the exact detail level Appendix E1 calls for, not a summary.

**Step 5: Perform the Targeted Risk Analysis required under 12.3.2.** This is a different analysis from a general enterprise risk assessment, and different in purpose from the frequency-justification TRA covered in this repo's [PCI DSS TRA template](../pci-dss-tra). This TRA has one specific job: demonstrate the customized control provides protection at least equivalent to the Defined Requirement it is replacing. Use the structure in Section 8.

**Step 6: Secure executive review and sign-off on the risk analysis** before presenting anything to the QSA. This has to be a real review, not a formality, and needs to be documented as such.

**Step 7: Co-design the testing procedure with the QSA.** Bring a draft testing procedure to this conversation rather than an empty page. Section 9 covers the specific reasons QSAs reject proposed testing procedures, and most of them are avoidable by anticipating the QSA's actual validation needs at this stage rather than after a rejection.

**Step 8: Validate, document in ROC Appendix E, and calendar the next review.** A Customized Approach implementation is not a one-time project. Confirm with the QSA how re-validation will work on the next assessment cycle, since the control, the risk analysis, and the testing procedure all need to still be defensible then, not just at the moment of this year's ROC.

---

## 6. Worked Example: Passwordless Authentication in Place of Req. 8.3.6 to 8.3.9

This is the most commonly cited real-world Customized Approach scenario in the industry: replacing PCI's prescriptive password requirements (minimum length, complexity, history, and account lockout rules under Req. 8.3.6 through 8.3.9) with a modern authentication approach aligned to NIST SP 800-63B, such as FIDO2 or platform passkeys, that does not rely on traditional password complexity rules at all.

**Scenario:** Meridian Retail Co. wants to move CDE administrative access from traditional password authentication to FIDO2 hardware security keys for all personnel with access to systems storing cardholder data. Under the Defined Approach, this would fail Req. 8.3.6's complexity rules outright, since there is no traditional password to measure. The Customized Approach is the correct path because this is a deliberate security improvement, not a constraint-driven workaround.

### Controls Matrix (Appendix E1 structure)

| Field | Entry |
|---|---|
| **Requirement** | 8.3.6 to 8.3.9 (password complexity, length, history, and lockout for CDE administrative access) |
| **Customized Approach Objective** | Authentication credentials for administrative access to system components are resistant to guessing, brute-force, and credential replay attacks |
| **Customized Control Description** | Administrative access to all CDE system components requires FIDO2 hardware security key authentication. Password-based authentication is disabled entirely for these accounts at the identity provider level. Each key is bound to a single named individual and registered through an in-person or verified remote identity check before issuance. |
| **How the Control Meets the Objective** | FIDO2 authentication is cryptographically resistant to brute-force and credential replay by design, since no shared secret is transmitted or stored that could be guessed, intercepted, or reused. This provides materially stronger resistance to the threats Req. 8.3.6 through 8.3.9 exist to address than password complexity rules do, which remain vulnerable to credential stuffing, phishing, and reuse across systems regardless of complexity. |
| **Control Owner** | Identity and Access Management lead |
| **Systems in Scope** | Identity provider, CDE administrative jump hosts, ServiceNow GRC admin console, AWS IAM privileged roles |
| **Monitoring and Maintenance** | Quarterly access review confirms every active administrative account is bound to a registered FIDO2 key with no password fallback enabled; key issuance and revocation logged and reviewed monthly |

### Targeted Risk Analysis (Appendix E2 structure, per Req. 12.3.2)

**(a) Requirement and assets in scope.** Req. 8.3.6 through 8.3.9, covering authentication for administrative access to CDE system components at Meridian Retail Co.

**(b) Description of the customized control.** FIDO2 hardware key authentication replacing password-based authentication entirely for administrative CDE access, detailed in the Controls Matrix above.

**(c) Threats and vulnerabilities the Defined Requirement addresses.** Password guessing, credential stuffing using previously breached passwords, brute-force login attempts, and credential reuse across systems.

**(d) Analysis of whether the customized control addresses those threats at least as effectively.** Password complexity and history rules reduce but do not eliminate these threats, since human-generated passwords remain guessable, reusable, and phishable even when compliant with complexity rules. FIDO2 authentication removes the underlying attack surface these threats depend on: there is no shared secret to guess, no password to reuse across systems, and no credential that can be usefully phished, since the cryptographic key never leaves the hardware device and is bound to the specific origin it was registered against. This represents materially stronger, not merely equivalent, protection against the threats the Defined Requirement addresses.

**(e) Residual risk.** Physical loss of a hardware key is the primary residual risk, mitigated by immediate revocation upon loss report and a documented re-issuance process requiring identity re-verification before a replacement key is bound to an account.

**(f) Executive review and approval.** Reviewed and approved by [Risk Owner], [Date], prior to QSA engagement.

### Testing Procedure (co-designed with QSA)

1. For a sample of administrative accounts with CDE access, confirm password-based authentication is disabled at the identity provider level with no fallback mechanism enabled.
2. Confirm each sampled account is bound to a registered FIDO2 key tied to a single named individual, with registration records showing identity verification at issuance.
3. Attempt authentication using a password or a credential other than the registered key, and confirm access is denied with no fallback path.
4. Review the most recent quarterly access review and monthly key issuance and revocation logs for completeness and evidence of follow-up on any discrepancies.

---

## 7. Blank Controls Matrix Template

Copy this structure for each requirement handled through the Customized Approach. One matrix per requirement, not one for the whole engagement.

| Field | Entry | Notes |
|---|---|---|
| **Requirement** | | The specific PCI DSS requirement number, not a range unless the objective genuinely spans several sub-requirements the way 8.3.6 to 8.3.9 does in the worked example above |
| **Customized Approach Objective** | | Copy this verbatim from the current version of the standard. Do not paraphrase it, since the QSA will check your control against the exact published wording |
| **Customized Control Description** | | What the control actually is and how it operates day to day, written so someone with no PCI background could still understand the mechanism |
| **How the Control Meets the Objective** | | This is the argument, not just a restatement. Explain the causal link between the control and the objective, the way the FIDO2 example above ties key-based auth to resistance against credential replay |
| **Control Owner** | | A named role, not a team name. The QSA will ask who to interview |
| **Systems in Scope** | | Every system the control actually touches, not just the primary one |
| **Monitoring and Maintenance** | | How you will know a year from now that this control is still working, not just that it was working on the day of the audit |

---

## 8. Blank Targeted Risk Analysis Template (Customized Approach)

This is a separate document from the Controls Matrix above, required under Req. 12.3.2. Fill in all six parts. A QSA can reject an otherwise strong control on an incomplete risk analysis alone.

**(a) Requirement and assets in scope:**
*What's being protected, and by which requirement.*

**(b) Description of the customized control:**
*Can usually be copied from the Controls Matrix above, kept consistent across both documents.*

**(c) Threats and vulnerabilities the Defined Requirement addresses:**
*Name the actual attack patterns, not a generic "unauthorized access" statement. The worked example names credential stuffing, brute force, and reuse specifically because that's what a QSA expects to see.*

**(d) Analysis of whether the customized control addresses those threats at least as effectively:**
*This is the section that gets rejected most often. State the mechanism, not just the conclusion. "Equally effective" without an explanation of why is not an analysis.*

**(e) Residual risk:**
*Every control has some. Naming it convincingly is more credible than implying there isn't any.*

**(f) Executive review and approval:**
Reviewed and approved by [Risk Owner], [Date]

---

## 9. Why QSAs Reject Customized Controls

- **The proposed control targets the printed requirement text instead of the stated Customized Approach Objective.** This is the single most common rejection reason. Re-check Section 5, Step 2 if a control gets rejected on this basis.
- **The risk analysis asserts equivalence without demonstrating it.** A risk analysis that concludes "this control is equally effective" without walking through the specific threats and how the new control addresses each one will not survive QSA review.
- **The entity proposes the testing procedure alone, without QSA input, late in the process.** Section 3's eligibility gate exists specifically to prevent this. A testing procedure built collaboratively from the start has a far higher acceptance rate than one presented as a finished product.
- **The control cannot be demonstrated as owned and maintained by the entity itself.** If a QSA suspects the control was designed by a consultant and the entity cannot explain or defend it independently, that is itself grounds for rejection under PCI's guidance, since an entity that cannot maintain a control is not a good candidate for this path regardless of the control's technical merit.
- **Compensating controls language appears anywhere in the documentation.** Any suggestion that the customized control exists because the entity could not meet the Defined Requirement, rather than chose not to, undermines the entire basis for using this path instead of a compensating control.

---

## 10. Maintenance

Re-confirm eligibility and re-validate every Customized Approach implementation at each assessment cycle, not just at initial approval. A control, risk analysis, or testing procedure that was defensible last year needs to still be defensible against the current version of PCI DSS and the current threat landscape, not grandfathered in. Re-check the Customized Approach Objective language against the current standard version at each cycle, since PCI SSC guidance and requirement text can be revised between major versions.

---

*Part of the [GRC Toolkit](https://github.com/ebohc/grc-toolkit). Built to work alongside the [PCI DSS v4.0.1 TRA template](../pci-dss-tra) and the [SOC 2 / ISO 27001 / PCI DSS crosswalk](../crosswalk) elsewhere in this repo.*

Victor Eboh, GRC Lead | [LinkedIn](https://www.linkedin.com/in/evictorc/)
