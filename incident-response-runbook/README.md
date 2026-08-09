# Incident Response Playbook & Template

A reusable incident response template built around NIST SP 800-61, using a real case study to show how it actually plays out. The February 2024 ransomware attack on Change Healthcare, the largest healthcare data breach in US history so far, with around 190 million people affected.

Built for GRC folks, security analysts, and auditors who want something they can actually use, not just another framework diagram.

## What's here

| File | What it is |
|---|---|
| `incident_response_playbook.xlsx` | The template itself. RACI matrix, NIST 800-61 checklist, the Change Healthcare timeline with sources, a detection log, a containment/eradication/recovery log, post-incident review, and a control mapping tab (NIST CSF 2.0, ISO 27001, HIPAA, SOC 2) |
| `incident-response-playbook-change-healthcare.md` | Article walking through the incident phase by phase against NIST 800-61 |
| `if-i-were-ir-lead-change-healthcare.md` | A different angle. Written as if I were actually running the response, hour by hour, including how I'd think through the ransom decision |
| `how-to-write-a-post-incident-report.md` | A general, reusable process for writing the formal report after any incident, not just this one |

## How to use it

- Tabs marked **(TEMPLATE)** are blank, meant for you to fill in for your own org or a client.
- Tabs marked **(CASE STUDY)** show Change Healthcare mapped into the same structure, so you can see it applied before you use it yourself.
- Yellow cells are where you're meant to type.
- It follows NIST SP 800-61's four phases (Preparation, Detection & Analysis, Containment/Eradication/Recovery, Post-Incident Activity) and cross-maps to NIST CSF 2.0, ISO 27001, HIPAA, and SOC 2 on the mapping tab.

Use it to study how a real breach lines up against the framework, or just take the structure and use it for your own IR docs or a tabletop exercise.

## Why this incident

Change Healthcare processed something close to 40% of US medical claims, so this one's a good teaching case. It shows what a single missing control (no MFA on one account) can turn into, how heavy the post-incident regulatory phase actually gets, and why vendor concentration risk deserves more attention than it usually gets. Everything referenced is pulled from public sources and cited in both articles.

## About me

Victor Eboh. CRISC, CompTIA CySA+, ISO 27001 Lead Implementer, ISC2 CC.

- GitHub: [github.com/ebohc](https://github.com/ebohc)

This sits alongside the rest of my GRC portfolio: AWS SOC 2 evidence collection, vulnerability management, a security frameworks master template, EU regulatory compliance (DORA, EU AI Act, CSRD, NIS2), threat modeling with STRIDE and PASTA, and OWASP Top 10 auditing.

## Disclaimer

This is a public portfolio project, built for learning and to show real hands-on work. All case study details come from public sources (Congressional testimony, HHS OCR, and reporting from Reuters, WIRED, TechCrunch, and Nixon Peabody LLP) cited in both articles. Not affiliated with Change Healthcare or UnitedHealth Group.
