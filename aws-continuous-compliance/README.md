# Continuous Compliance Monitoring with GuardDuty and Config

A methodology and deployable reference for combining Amazon GuardDuty and
AWS Config into a single continuous compliance monitoring layer, instead
of running each in isolation the way most environments do.

> **Note on this artifact:** This reflects methodology built from
> professional cloud security practice, using AWS's own published rule
> and finding type catalogs as the source of truth. The Config portion
> of this reference has been verified against a real AWS account, see
> the [case study](#7-case-study-a-real-finding-live). The Terraform in
> this repo has not been applied against a live account as part of
> writing this, review and run `terraform plan` yourself before applying
> it anywhere. No client, employer, or real-environment data is used
> anywhere in this document, the account referenced in the case study is
> a personal account used solely for this demonstration.

## Table of Contents

1. [Why These Two Together](#1-why-these-two-together)
2. [What Each Service Actually Does](#2-what-each-service-actually-does)
3. [The Architecture](#3-the-architecture)
4. [Control Matrix](#4-control-matrix)
5. [Deploying It](#5-deploying-it)
6. [Tuning Signal vs Noise](#6-tuning-signal-vs-noise)
7. [Case Study: A Real Finding, Live](#7-case-study-a-real-finding-live)
8. [Maintenance](#8-maintenance)

## 1. Why These Two Together

GuardDuty and Config get treated as separate tools solving separate
problems, threat detection on one side, configuration compliance on the
other. In practice they cover two different failure modes that both
matter continuously, not at a point in time:

- **Config answers**: is this resource configured the way our policy
  says it should be, right now, and does it stay that way after someone
  changes it.
- **GuardDuty answers**: is something actively behaving maliciously
  against this environment, right now, regardless of whether the
  underlying configuration is compliant.

A resource can be perfectly compliant on every Config rule and still be
under active attack. A resource can also drift out of compliance without
anyone touching it maliciously, a permissive security group added for a
weekend debugging session that never got removed. Treating these as one
monitoring layer, rather than two separate dashboards nobody correlates,
is the actual point of this artifact.

## 2. What Each Service Actually Does

**AWS Config** continuously records configuration state for supported
resource types and evaluates that state against rules, either AWS
managed rules or custom ones. A rule evaluation isn't a point-in-time
scan, it re-evaluates whenever the resource configuration changes, which
is what makes it meaningfully different from running a periodic audit
script. Config's real output is a compliance status per resource per
rule, tracked over time, not just a snapshot.

**Amazon GuardDuty** analyzes VPC Flow Logs, DNS logs, CloudTrail
management and data events, and (with the relevant protection plans
enabled) EKS audit logs and runtime activity, correlating them against
threat intelligence and behavioral models to produce findings. It is not
a configuration checker, it has no opinion on whether your S3 bucket
policy is correct. It has an opinion on whether something is actively
trying to compromise your environment.

## 3. The Architecture

```
AWS Config Rules  ──┐
 (compliance drift)  │
                      ├──> EventBridge ──> SNS ──> Security Hub / ticketing
GuardDuty Findings ──┘        (rule)         (notify)   (aggregate + track)
 (active threats)
```

Both services publish events to EventBridge natively. The architecture
in this repo's `terraform/` directory wires both into a single
EventBridge rule pattern feeding one SNS topic, so a security team gets
one notification channel to actually watch, not two dashboards to
remember to check. In an org running AWS Organizations, both GuardDuty
and Config support delegated administrator accounts, so this pattern
extends to multi-account environments without duplicating the
monitoring stack per account.

## 4. Control Matrix

A sample of the Config rules and GuardDuty finding categories this
reference deploys, mapped to CIS AWS Foundations Benchmark v3.0, NIST
CSF 2.0, and PCI DSS v4.0.1. This is a representative slice, not the
full rule catalog, extend it with your own environment's applicable
rules.

### AWS Config managed rules

| Config Rule | What It Checks | CIS AWS Foundations v3.0 | NIST CSF 2.0 | PCI DSS v4.0.1 |
|---|---|---|---|---|
| [`root-account-mfa-enabled`](https://docs.aws.amazon.com/config/latest/developerguide/root-account-mfa-enabled.html) | Root account has MFA enabled | Section 1 (IAM) | PR.AA | Req. 8.4 |
| [`iam-user-mfa-enabled`](https://docs.aws.amazon.com/config/latest/developerguide/iam-user-mfa-enabled.html) | IAM users have MFA enabled | Section 1 (IAM) | PR.AA | Req. 8.4 |
| [`iam-password-policy`](https://docs.aws.amazon.com/config/latest/developerguide/iam-password-policy.html) | Account password policy meets minimum strength requirements | Section 1 (IAM) | PR.AA | Req. 8.3 |
| [`access-keys-rotated`](https://docs.aws.amazon.com/config/latest/developerguide/access-keys-rotated.html) | IAM access keys rotated within a defined window | Section 1 (IAM) | PR.AA | Req. 8.6 |
| [`s3-bucket-public-read-prohibited`](https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-public-read-prohibited.html) | S3 buckets don't allow public read access | Section 2 (Storage) | PR.DS | Req. 3, Req. 9 |
| [`s3-bucket-public-write-prohibited`](https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-public-write-prohibited.html) | S3 buckets don't allow public write access | Section 2 (Storage) | PR.DS | Req. 3, Req. 9 |
| [`s3-bucket-server-side-encryption-enabled`](https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-server-side-encryption-enabled.html) | S3 buckets encrypt data at rest | Section 2 (Storage) | PR.DS | Req. 3.5 |
| [`encrypted-volumes`](https://docs.aws.amazon.com/config/latest/developerguide/encrypted-volumes.html) | EBS volumes are encrypted | Section 2 (Storage) | PR.DS | Req. 3.5 |
| [`rds-storage-encrypted`](https://docs.aws.amazon.com/config/latest/developerguide/rds-storage-encrypted.html) | RDS instances encrypt storage | Section 2 (Storage) | PR.DS | Req. 3.5 |
| [`cloudtrail-enabled`](https://docs.aws.amazon.com/config/latest/developerguide/cloudtrail-enabled.html) | CloudTrail is enabled account-wide | Section 3 (Logging) | PR.PS, DE.CM | Req. 10 |
| [`cloud-trail-log-file-validation-enabled`](https://docs.aws.amazon.com/config/latest/developerguide/cloud-trail-log-file-validation-enabled.html) | CloudTrail log integrity validation is on | Section 3 (Logging) | PR.PS | Req. 10.5 |
| [`vpc-flow-logs-enabled`](https://docs.aws.amazon.com/config/latest/developerguide/vpc-flow-logs-enabled.html) | VPC Flow Logs are capturing network traffic | Section 5 (Networking) | DE.CM | Req. 10 |
| [`restricted-ssh`](https://docs.aws.amazon.com/config/latest/developerguide/restricted-ssh.html) | No security group allows unrestricted inbound SSH | Section 5 (Networking) | PR.AA, PR.IR | Req. 1 |
| [`guardduty-enabled-centralized`](https://docs.aws.amazon.com/config/latest/developerguide/guardduty-enabled-centralized.html) | GuardDuty is enabled across the org | Section 4 (Monitoring) | DE.CM | Req. 11.5 |

### GuardDuty finding categories

| Finding Type (examples, verified against AWS's published catalog) | Category | NIST CSF 2.0 | PCI DSS v4.0.1 |
|---|---|---|---|
| `UnauthorizedAccess:EC2/SSHBruteForce` | Brute force attempt against an EC2 instance | DE.CM, DE.AE | Req. 10, Req. 11.5 |
| `UnauthorizedAccess:IAMUser/ConsoleLoginSuccess.B` | Console login from an anomalous or unusual source | DE.AE | Req. 10, Req. 8 |
| `UnauthorizedAccess:IAMUser/InstanceCredentialExfiltration.OutsideAWS` | Instance credentials used from outside AWS | DE.AE, RS.AN | Req. 8, Req. 10 |
| `PrivilegeEscalation:IAMUser/AdministrativePermissions` | An identity granted itself elevated permissions | DE.AE, PR.AA | Req. 7, Req. 8 |
| `Recon:EC2/PortProbeUnprotectedPort` | Port scanning activity against an unprotected port | DE.CM, DE.AE | Req. 11.5 |
| `CryptoCurrency:EC2/BitcoinTool.B` | Instance communicating with cryptocurrency mining infrastructure | DE.AE, RS.AN | Req. 11.5 |
| `UnauthorizedAccess:EC2/TorClient` | Instance communicating with the Tor network | DE.AE | Req. 11.5 |

GuardDuty's full finding type catalog is larger than this and changes as
AWS adds detections, this table is a representative slice for mapping
purposes, not a complete reference. Check AWS's own finding types
documentation for the current full list before treating any mapping as
exhaustive.

## 5. Deploying It

The Terraform in [`terraform/`](./terraform) deploys:

- A GuardDuty detector with S3, Kubernetes, and Malware Protection data
  sources enabled
- The Config rules listed in Section 4 above
- An SNS topic
- Two EventBridge rules, one matching GuardDuty findings at MEDIUM
  severity and above, one matching Config compliance state changes to
  NON_COMPLIANT, both targeting the same SNS topic

```
cd terraform
terraform init
terraform plan    # review every resource before applying anything
terraform apply
```

This assumes an AWS Config recorder and delivery channel already exist
in the target account, if they don't, add an `aws_config_configuration_recorder`
and `aws_config_delivery_channel` resource before applying the rules,
Config rules won't evaluate without an active recorder.

## 6. Tuning Signal vs Noise

The single biggest reason continuous monitoring setups get ignored
within a few months isn't bad tooling, it's alert volume nobody tuned.
Two adjustments matter more than any others:

**Severity floor on GuardDuty.** The Terraform here filters to MEDIUM
and above by default. LOW severity findings are frequently expected
behavior (a bastion host getting SSH brute force attempts is normal,
not a compromise), routing every LOW finding to the same channel as a
genuine PrivilegeEscalation finding trains people to stop reading the
channel entirely.

**Suppression rules with an actual owner and expiration**, not silent
ignoring. GuardDuty and Config both support suppression, use it
deliberately for known, accepted patterns (see the SQL exceptions
pattern), but track suppressions the same way risk acceptances are
tracked elsewhere in this repo's [runbook](../audit-readiness-runbook):
named owner, documented reason, review date. A suppression with no
expiration is a permanent blind spot nobody remembers agreeing to.

## 7. Case Study: A Real Finding, Live

Section 4's control matrix is built from AWS's published documentation.
This section is different: a real AWS account, the rules above actually
deployed, a real finding Config caught, and a real remediation with the
compliance status verified as changed afterward, not just asserted.

Full walkthrough with all eight screenshots: [`case-study.md`](./case-study.md)

## 8. Maintenance

Re-review the Config rule set and GuardDuty finding type mappings at
least annually, and whenever CIS publishes a new AWS Foundations
Benchmark version, since rule-to-control mappings shift between
versions. Re-verify severity floor and suppression rules quarterly,
since both tend to drift toward either too noisy or too quiet without
periodic review.

---

*Part of the [GRC Toolkit](https://github.com/ebohc/grc-toolkit).*

Victor Eboh, GRC Lead | [LinkedIn](https://www.linkedin.com/in/evictorc/)
