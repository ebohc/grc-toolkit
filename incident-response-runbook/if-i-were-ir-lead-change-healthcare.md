# If I Were Running This: How I'd Handle the Change Healthcare Incident

I wanted to write this one differently. Most incident response content is either a framework diagram or a post-mortem written after the fact, when everything's already known. What actually gets tested, in an interview or in the moment, is what you do when you don't know everything yet. So this is my own attempt at walking through the Change Healthcare breach as if I were the one running it, hour by hour, using the real public timeline as the scenario.

Where the actual company made a call, I've said so. Where I'd have done something differently, I've said that too, and why.

## Hour 0-1: Just declare it

06:00. EDR and SIEM are showing weird data movement and what looks like ransom-note files getting created on a subnet tied to claims processing.

First thing I do isn't technical. I declare a Sev-1 and activate the IR plan right away, before I even know root cause. Waiting until you're sure before you declare is probably the most common mistake in incident response. It doesn't cost you certainty. It just costs you hours you don't get back.

So:

1. I take Incident Commander (or confirm who has it).
2. I pull in the pre-assigned people: SOC, Legal, Comms, IT, an exec sponsor. Not as a courtesy. HIPAA's notification clock starts running once you have a reasonable basis to believe there was a breach, not once you've fully confirmed it.
3. I start a running log, timestamped, right now. This becomes the record everything else gets built on: the post-incident review, and if it comes to it, whatever regulators or outside counsel end up asking for.

One thing I wouldn't do: wait to loop Legal in until I have a clearer picture. They need to be on the call from hour one, even with incomplete info, because notification timing and privilege decisions start immediately.

## Hour 1-4: Figure out what we're actually dealing with

4. Pull the initial indicators from the SOC. What systems, what accounts, is this spreading or is it contained to one spot.
5. Classify severity against a real matrix, not a gut feeling. Given PHI and claims infrastructure at this scale, this is a Sev-1 no matter how you slice it.
6. The one question I'd ask first: is there evidence data actually left, or is this still just an encryption risk? That answer changes almost everything downstream: what we owe regulators, whether ransom is even relevant, how we message this internally.
7. In the real incident, it turned out the attacker had been in for nine days before anyone noticed, and data was already out by the time they were caught. I'd want an early answer here, even a rough one, because it decides whether we're running "contain and recover" or "assume it's already gone."

## Hour 4-24: Containment, and not the blunt version first

8. I don't take everything offline right away. First move is targeted: kill the compromised accounts, isolate the specific hosts and subnet showing signs of compromise, block the known bad IPs at the perimeter. Shutting the whole company down is sometimes the right call, but it's a last resort, not a first instinct, because of what it costs.
9. I'd set a checkpoint: if targeted containment isn't visibly working within a few hours, escalate to something broader. The real company went straight to a full shutdown the day they found it, which is understandable given nine days of undetected access and a lot of uncertainty about scope, but it's also why claims processing stopped for something like 900,000 physicians, 33,000 pharmacies, and 5,500 hospitals at once. I'd want to know we'd actually tried the targeted route first, and I'd want Business Continuity in the room before pulling that trigger, not after.
10. Speaking of which, once containment scope goes beyond a single system, I'm bringing in Business Continuity immediately. "Isolate the environment" sounds like a pure security call, but here it meant an entire sector couldn't bill or get paid. That needs a business sign-off, not just a security one.
11. Before anyone starts fixing things, I preserve evidence: memory captures, disk images, logs, proper chain of custody. I'd rather lose an hour to imaging than lose the ability to say for certain how they got in.

## Day 1-3: Root cause, and the ransom question

12. Root cause work runs in parallel with containment, not after it. In the real case it came down fast once people looked in the right place: one compromised account on a Citrix portal with no MFA. That's a strong argument for bringing in outside forensics help on day one instead of waiting to see if the internal team can chase it down alone.

13. The ransom decision is the one I'd actually want to slow down for.

I'd get Legal, the exec sponsor, outside counsel, and a ransomware negotiator (if we have access to one) in a room before responding to the attacker at all, even to say no.

My starting position: paying doesn't guarantee the data gets deleted, so it shouldn't be treated as a way to fix the data exposure. The Change Healthcare case backs this up pretty directly. They paid around $22 million, and about a month later a second group was trying to sell the same data anyway. Somebody kept a copy regardless of payment.

Where I'd actually consider paying is narrower. If decryption is genuinely the only path back and the cost of extended downtime is severe, not backups failing because nobody tested them. That's a different justification than "make the exposure go away," and I'd want that distinction said out loud in the room, because people tend to blur the two.

Either way, that call gets made by the exec sponsor and Legal together, on the record, with the reasoning written down. Not by me alone, and not implicitly.

## Day 1-3, running alongside all of this: notifications and comms

14. The moment there's a reasonable basis to think PHI was exposed, I start the HIPAA notification clock formally and get Legal scoping out what we owe: individuals, HHS, possibly media, each with its own deadline.

15. Two comms tracks, kept separate: internal (what's happening, what's fixed, what's next) and external (drafted with Legal, reviewed before it goes anywhere). Nothing goes out to press, regulators, or affected people without Legal's sign-off. Not optional.

16. Given the scale here, I'd flag early that our first estimate of how many people are affected is probably going to go up. That's exactly what happened in real life. The final number nearly doubled the original estimate. Better to set that expectation on day one than have people lose trust every time the number changes.

## Week 1-4: Eradication and recovery

17. Eradication follows straight from root cause: kill the bad credentials, rotate them, enforce MFA everywhere, not just on the door that got used. Then check hard for anything else left behind, especially given that a second actor apparently still had the data afterward.

18. Recovery is phased, not assumed. Restore from backups you've actually confirmed are clean, bring systems back in order of how critical they are to the business, and put tighter monitoring on anything you just restored before calling it done.

19. I don't sign off on "recovered" by myself. That's a joint call with IT and whoever owns the business side of that system, and it goes in the log.

## Month 1-3: what happens after it's "over"

20. I'd run the lessons-learned session about two weeks after closing the incident, not immediately, while people are still exhausted, but not so late that memory's already fading.

21. Whatever comes out of that session needs an owner and a deadline, not a vague "we'll do better" line. Things like: an actual audit of MFA coverage across every remote access path, a real checklist for post-acquisition security integration, and a rewritten containment decision tree that spells out when targeted isolation should escalate to something bigger.

22. I'd also push for a hard look at vendor concentration risk. If your org depends heavily on one vendor the way the healthcare system depended on Change Healthcare, "what happens if they're down for three weeks" needs to be a real part of how you assess that vendor, not something you only think about after it happens.

23. Last step: close the loop with the board. Root cause, cost, what regulators are doing, and specifically what's changed to keep this from happening again. Not a story of what happened. Proof that something's different now.

## If someone pushed back on me over coffee

Three calls from this I'd actually defend if someone challenged them:

1. **Declare before you're sure.** Being wrong early costs almost nothing. Waiting for certainty costs you the dwell-time window you can never get back.
2. **Try targeted containment before shutting everything down.** Full shutdown is sometimes right, but it should be a deliberate escalation with the business in the room, not the default reaction.
3. **Ransom payment isn't a data-deletion guarantee. Don't treat it like one.** This incident is about as clean a real-world example of that as you'll find.

---

This one's a companion to my NIST 800-61 breakdown of the same incident, also in this repo: [incident-response-playbook-change-healthcare.md](./incident-response-playbook-change-healthcare.md). Full template, RACI matrix, and control mapping are in this same folder: [github.com/ebohc/grc-toolkit/tree/main/incident-response-runbook](https://github.com/ebohc/grc-toolkit/tree/main/incident-response-runbook).

**Sources:** Congressional testimony of Andrew Witty (Senate Finance Committee, May 1, 2024); HHS Office for Civil Rights; reporting from Reuters, WIRED, and TechCrunch; legal analysis from Nixon Peabody LLP; American Hospital Association briefings.
