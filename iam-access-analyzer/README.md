# IAM Access Analyzer: Finding and Fixing Unintended Access

A methodology reference for using IAM Access Analyzer to find and
resolve unintended access, tied back to the same failure mode behind
most real breaches: an identity with more access than it should have,
that nobody was watching.

> **Note on this artifact:** This reflects methodology built from
> professional cloud security practice, using AWS's own published
> documentation as the source of truth. No client, employer, or
> real-environment data is used anywhere in this document.

## Table of Contents

1. [Why Identity, Specifically](#1-why-identity-specifically)
2. [The Three Analyzers, and Which One Is Actually Free](#2-the-three-analyzers-and-which-one-is-actually-free)
3. [How External Access Analysis Actually Works](#3-how-external-access-analysis-actually-works)
4. [Control Matrix](#4-control-matrix)
5. [Common Mistakes](#5-common-mistakes)
6. [Maintenance](#6-maintenance)

## 1. Why Identity, Specifically

The incident response case study elsewhere in this repo traces the
largest healthcare breach in US history back to one compromised account
with no MFA. That's not a network problem or a patching problem. It's
an identity governance failure, and it's the failure mode that shows up
disproportionately often in real breach post-mortems compared to how
much attention it gets in day-to-day security work.

IAM Access Analyzer exists to answer a question most teams only ask
after something's gone wrong: who actually has access to this resource
right now, not who's supposed to, not who had access when the policy
was written, who actually has it today.

## 2. The Three Analyzers, and Which One Is Actually Free

IAM Access Analyzer isn't one feature. It's three separate analyzers
with different scope, different cost, and different lifecycles, and
treating them as one thing is a common source of false confidence.

| Analyzer | What It Finds | Cost |
|---|---|---|
| **External Access** | Resource-based policies (S3 buckets, IAM roles, KMS keys, and others) that grant access to a principal outside your defined zone of trust | Free |
| **Internal Access** | Which principals inside your organization or account can reach a specific business-critical resource you've selected | Paid, per resource monitored per region per month |
| **Unused Access** | IAM roles, access keys, and passwords that haven't been used within a defined window, and specific unused permissions within roles that are otherwise active | Paid, per IAM role or user analyzed per month |

A team that enabled External Access years ago and never revisited the
other two has real coverage on one axis and zero on the others. They
are complements, not substitutes for each other. An identity with
access to everything but that nobody outside the account can reach
generates nothing on External Access, because nothing was shared
externally, the risk there is entirely on the Unused and Internal axes.

## 3. How External Access Analysis Actually Works

You define a **zone of trust**, either your whole AWS Organization or
a single account. Anything inside that zone is considered trusted.
IAM Access Analyzer then evaluates resource-based policies using
automated reasoning, not just pattern matching, and generates a finding
any time a policy grants access to a principal outside that zone.

This matters because it catches things a manual policy review misses.
A bucket policy that looks fine in isolation can still grant access to
an external account if a wildcard or a cross-account role assumption
resolves further than the person who wrote it intended. The analyzer
reasons through what the policy actually permits, not what it appears
to permit at a glance.

Findings re-evaluate automatically as policies change, and you can
force an immediate re-scan through the console or the
`StartResourceScan` API instead of waiting for the next periodic pass.

## 4. Control Matrix

| Finding Type | What It Means | NIST CSF 2.0 | PCI DSS v4.0.1 |
|---|---|---|---|
| External access finding, S3 bucket | A bucket policy, ACL, or access point grants access to a principal outside the zone of trust | PR.AA, ID.AM | Req. 7, Req. 9 |
| External access finding, IAM role | A role can be assumed by a principal outside the zone of trust | PR.AA | Req. 7, Req. 8 |
| External access finding, KMS key | A key policy grants use or management permissions to an external principal | PR.AA, PR.DS | Req. 3.5, Req. 7 |
| Unused IAM role | A role has had no access activity within the configured usage window | PR.AA | Req. 7.2, Req. 8.6 |
| Unused access key or password | Credentials belonging to a user haven't been used to access the account within the window | PR.AA | Req. 8.6 |
| Unused permissions | Specific service or action-level permissions on an otherwise active role or user show no usage | PR.AA | Req. 7.2 |

## 5. Common Mistakes

**Treating External Access as full coverage.** It only reasons about
resource-based policies. An identity-based policy that grants broad
internal access, the kind that lets a standard employee reach a
production database they have no reason to touch, produces zero
External Access findings, because nothing was shared outside the trust
boundary. That's what Internal and Unused access analysis exist to
catch, and it's exactly the gap the section above warns about.

**Confusing a finding with an incident.** A finding means a policy
grants access to something outside your zone of trust. That's
sometimes completely intentional, a legitimate cross-account
integration, a partner relationship. The job isn't to treat every
finding as a breach, it's to confirm each one is either intended and
documented, or genuinely wrong and needs fixing.

**Setting the zone of trust too broadly by default.** If you analyze
at the AWS Organization level without thinking about it, cross-account
access within your own org won't generate findings at all, since
everything in the org is trusted by definition. That's often correct,
but it should be a deliberate choice, not an accident of which scope
was selected during setup.

## 6. Maintenance

Re-validate the zone of trust definition whenever the account or
organization structure changes, an acquisition, a new business unit, a
restructured OU. A zone of trust that made sense a year ago can quietly
stop matching reality. Review archived findings periodically too, a
finding marked as intended today should still be intended six months
from now, not just assumed to be.

---

*Part of the [GRC Toolkit](https://github.com/ebohc/grc-toolkit).*

Victor Eboh, GRC Lead | [LinkedIn](https://www.linkedin.com/in/evictorc/)
