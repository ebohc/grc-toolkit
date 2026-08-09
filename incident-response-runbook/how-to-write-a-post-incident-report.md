# How to Write a Post-Incident Report, Step by Step

This is the process I'd actually follow to write the formal report after an incident, the one that goes to leadership, and sometimes to regulators or auditors later. Not a template to fill in blindly, but the order I'd do the thinking in.

## Step 1: Nail down the timeline first, before writing a word of narrative

Pull your incident log and lay out a bare timeline: timestamps, what happened, who did it. No analysis yet, no writing yet. Just the facts in order.

Why first: everything else in the report depends on this being right. If the timeline's wrong, the root cause section, the impact section, all of it inherits the mistake. Get this locked down and reviewed by whoever was actually on the bridge before you build anything on top of it.

## Step 2: Write the executive summary last, but plan it first

Sounds backwards, but it works. Decide now what the three or four sentences at the top need to say: what happened, root cause, impact, current status. That forces you to know what the whole report is actually about before you start writing the details. You'll come back and write the real version once the rest is done, but sketch it now so you're not wandering.

Leadership reads this section and maybe nothing else. It needs to stand alone.

## Step 3: Write the root cause section like you're explaining it to someone who'll ask "why" three times

Don't stop at "an account was compromised." Ask why. Why was that account compromised? No MFA. Why was there no MFA? Because it wasn't in scope for the post-acquisition security review. Now you're at something people can actually act on.

If you can't get to a real root cause yet because forensics isn't done, say that plainly. "Root cause investigation ongoing, preliminary finding is X" is a legitimate sentence. Don't guess and present it as certain.

## Step 4: Document impact in numbers, not adjectives

Skip "significant disruption." Use real numbers: how many systems, how many users or customers, how many hours of downtime, dollar impact if you have it, data exposed if any. If you don't have a number yet, say "estimate pending" rather than filling the gap with vague language.

This section is what usually gets fact-checked hardest, especially if regulators or lawyers see this report later. Keep it tight to what you can actually back up.

## Step 5: Walk through the response chronologically, phase by phase

This is where the NIST 800-61 structure earns its keep: Detection, Containment, Eradication, Recovery, in that order, each with what was done and when. Keep this factual. This is not the place to editorialize about what should've happened differently. That goes in the next section.

## Step 6: Separate "what we'd do differently" from "what we're actually going to change"

Two different things, don't blur them. "What we'd do differently" is retrospective and can be a short paragraph. "What we're actually going to change" needs to be a list with an owner and a date on each item. If an action item doesn't have both, it's not a commitment, it's a wish, and it'll read that way to anyone reviewing the report later.

## Step 7: Get it reviewed by Legal before it goes anywhere

Not as a formality. A post-incident report can end up as evidence in litigation or regulatory proceedings. Legal needs to see it before it's final, especially the root cause and impact sections, to make sure nothing's stated as fact that isn't confirmed yet.

## Step 8: Match the level of detail to the audience

You're probably writing two versions, not one:

- **Board/executive version.** A page, maybe two. Summary, impact, current status, what's changing. No jargon, no technical detail they don't need.
- **Technical/regulatory version.** Full detail. Timeline, IOCs, technical root cause, every action taken. This is the one that goes to auditors or regulators if it comes to that.

Don't try to make one document serve both audiences. It ends up too long for the board and too thin for the technical reviewers.

## Step 9: Date it, version it, and lock it once it's approved

Once the report's signed off, treat it like a controlled document, versioned, dated, with sign-off recorded. If details get corrected later (numbers often do, as investigations continue), that's a new version with a changelog, not a silent edit to the original.

---

## Quick structure to work from

If you want a skeleton to start from:

1. Executive Summary
2. Incident Overview (what, when, who found it)
3. Timeline
4. Root Cause
5. Impact (systems, data, people, cost)
6. Response Actions Taken (by phase)
7. Regulatory/Notification Status
8. Lessons Learned
9. Action Items (owner and deadline for each)
10. Appendix (technical detail, logs, IOCs, for the technical version only)

This lines up with the Post-Incident Review tab in the workbook, so if you've already filled that in, you're most of the way to a draft.
