# What the Change Healthcare Breach Actually Teaches About Incident Response

I keep seeing incident response treated like a SOC-only problem in GRC circles, and I think that's a mistake. When something actually breaks, GRC ends up in the middle of it: notification deadlines, board updates, contract obligations, evidence for auditors later. So I wanted to break down a real incident using the standard IR framework, NIST SP 800-61, and see what it actually looks like phase by phase. Not the clean textbook version. The real, messy one.

I used the Change Healthcare ransomware attack from February 2024 because it's about as well-documented as a breach gets. There was Congressional testimony, an HHS investigation, and a ton of reporting from outlets like Reuters and WIRED. You don't have to guess at what happened.

I built a free workbook to go with this (link at the bottom) if you want to run the same exercise for your own org.

## The short version of what happened

Change Healthcare processes something like 40% of medical claims in the US. Huge chunk of the healthcare system runs through them. So when they got hit, it wasn't just their problem.

Here's the timeline:

- **Feb 12, 2024**: Attackers (an ALPHV/BlackCat affiliate) get in using stolen credentials on a Citrix remote access portal. No MFA on that portal.
- **Feb 12 to 21**: Nobody notices for nine days. In that window they pull out a large amount of sensitive data.
- **Feb 21**: Change Healthcare finally detects it and pulls systems offline across the whole company. Claims processing stops for hospitals, pharmacies, and doctors' offices nationwide.
- **March 3**: They pay roughly $22 million in ransom.
- **April**: A different group starts trying to sell the same stolen data. So the ransom didn't actually make the problem go away.
- **May 1**: CEO Andrew Witty testifies to Congress and confirms the root cause on record: one compromised account, no MFA.
- **January 2025**: Final number comes out. About 190 million people affected. Largest healthcare breach in US history.

That root cause is the part that sticks with me. One account. No MFA. That's it. Everything downstream of that (the ransom, the lawsuits, the testimony) traces back to a control gap that probably looked minor on somebody's risk register.

## Walking it through NIST 800-61

### Preparation

Change Healthcare had been acquired by UnitedHealth in October 2022. Testimony suggested the security procedures from that acquisition hadn't been fully folded in yet, including MFA coverage on remote access.

This tracks with what I've seen generally. M&A creates security gaps almost by default, right at the seam between two companies' programs, and those gaps can sit there for a long time before anyone notices. If you're doing GRC work around an acquisition, MFA coverage on remote access shouldn't be an assumption. It should be something you actually go verify and document.

### Detection and Analysis

Nine days between the break-in and detection. That's the expensive number in this whole story. It's the window where the data actually left the building, before any ransomware was even deployed.

Dwell time isn't just a SOC metric. If you're building out a SOC 2 evidence package or a frameworks template, logging and monitoring coverage on internet-facing systems needs real, specific evidence behind it, not a generic "logging is enabled" line.

### Containment, Eradication, Recovery

Their containment call was blunt: shut the whole company down. It stopped the spread, but it also meant claims processing froze for a huge chunk of the country for weeks. Two crises running at once: the security incident, and the fact that providers suddenly couldn't bill or get paid.

Eradication was straightforward once they knew the cause: kill the compromised credentials, close the MFA gap. Recovery took weeks, phased, and UnitedHealth ended up standing up a temporary funding program just to keep providers financially afloat while things got fixed.

The lesson for me here is that containment decisions have consequences way outside security, and that should get war-gamed ahead of time, not figured out live during the incident. If "isolate this system" would also take down something your org depends on operationally, that needs to be in your business continuity plan before it happens, not after.

### Post-Incident

This is where it gets long and heavy. Notifications ran into 2025. The final number, 190 million, was almost double their earlier estimate, which is a good reminder that early breach scope numbers are usually wrong and should be communicated that way. HHS opened an investigation. State AGs got involved. Lawsuits got consolidated into one big case. And Congress got a public, on-record account of exactly what went wrong.

Most orgs will never see that level of scrutiny, but any regulated org should plan like they might. Post-incident isn't a wrap-up step you tack on at the end. It's its own phase, with its own timeline that can run months, and its own set of people involved: regulators, lawyers, the board, and every person whose data got exposed.

## The thing that bugs me most about this one

Change Healthcare wasn't just a vendor. It was infrastructure. When it went down, there wasn't really a backup plan, because there's nothing else at that scale to fail over to.

That's worth sitting with if you do vendor risk work. It's not enough to check whether a vendor has good security controls. Ask what happens if they're down for three weeks. Most vendor risk programs are heavy on point-in-time questionnaires and light on "what if this vendor just isn't available" planning, and this incident is a pretty clear argument for fixing that balance.

## What's in the template

Free workbook on GitHub, built to actually be used, not just admired:

- RACI tab for IR roles
- A blank phase-by-phase checklist mapped to NIST 800-61
- The full Change Healthcare timeline with sources
- A detection log with an example entry
- A containment/eradication/recovery log with the Change Healthcare notes next to blank fields for your own incident
- A post-incident review tab, same setup
- A control mapping tab tying NIST 800-61 to NIST CSF 2.0, ISO 27001, HIPAA, and SOC 2

Use it to study how a real incident maps to the framework, or just steal the structure for your own IR docs or tabletop exercise.

---

Template and full workbook, plus the companion piece walking through how I'd have run the response hour by hour, are in this same folder: [github.com/ebohc/grc-toolkit/tree/main/incident-response-runbook](https://github.com/ebohc/grc-toolkit/tree/main/incident-response-runbook). More of my GRC work at [github.com/ebohc/grc-toolkit](https://github.com/ebohc/grc-toolkit). Feel free to connect on [LinkedIn](https://www.linkedin.com/in/evictorc/) too.

**Sources:** Congressional testimony of Andrew Witty (Senate Finance Committee, May 1, 2024); HHS Office for Civil Rights; reporting from Reuters, WIRED, and TechCrunch; legal analysis from Nixon Peabody LLP; American Hospital Association briefings.
