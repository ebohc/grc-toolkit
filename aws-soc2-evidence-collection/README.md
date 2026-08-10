# AWS SOC 2 Evidence Collection

How to use AWS CloudTrail and AWS Config to automatically collect
SOC 2 audit evidence, continuously, accurately, and in a format
your auditor will accept.

---

## What this covers

Most SOC 2 teams spend weeks manually collecting evidence before
every audit. If your infrastructure runs on AWS, two native services
eliminate most of that work: CloudTrail and AWS Config.

This guide walks through exactly how to set them up, what to look
for, and how to export evidence for your auditor, with real AWS
console screenshots.

---

## The two services

| Service | What it does | SOC 2 value |
|---------|-------------|-------------|
| AWS CloudTrail | Records every API call and user action | Login history, MFA evidence, permission changes |
| AWS Config | Continuously evaluates resource configurations | Compliance history across the full audit period |

---

## SOC 2 controls covered

| AWS Config Rule | What it checks | SOC 2 control |
|----------------|---------------|---------------|
| `mfa-enabled-for-iam-console-access` | MFA on all IAM users | CC6.2 |
| `root-account-mfa-enabled` | MFA on root account | CC6.2 |
| `cloudtrail-enabled` | CloudTrail active in all regions | CC7.1 |
| `s3-bucket-public-read-prohibited` | No public S3 buckets | CC6.6 |
| `encrypted-volumes` | EBS volumes encrypted at rest | CC6.6 |
| `iam-password-policy` | Password complexity enforced | CC6.1 |
| `vpc-flow-logs-enabled` | VPC flow logs active | CC7.1 |
| `access-keys-rotated` | IAM keys rotated within 90 days | CC6.1 |

---

## CloudTrail: key events to capture

| Event name | What it shows | SOC 2 control |
|-----------|--------------|---------------|
| `ConsoleLogin` | Who logged in and whether MFA was used | CC6.2 |
| `CreateUser` / `DeleteUser` | IAM user lifecycle | CC6.1 |
| `AttachUserPolicy` | Permission changes | CC6.3 |
| `PutBucketPolicy` | S3 access changes | CC6.6 |
| `StopLogging` | CloudTrail tampering attempts | CC7.1 |

---

## Setup checklist

- [ ] Create a CloudTrail trail, multi-region, logging to S3
- [ ] Enable AWS Config with continuous recording
- [ ] Add all SOC 2 Config rules listed above
- [ ] Fix any noncompliant findings before audit fieldwork
- [ ] Export CloudTrail ConsoleLogin events for full audit period
- [ ] Export Config compliance history for full audit period

---

## Related resources

**[SOC 2 Audit Prep](../soc2-audit-prep/)**
Excel workbook: evidence tracker, gap assessment, control
testing log, PBC tracker, and audit checklist.

---

## Read the full guide

Full article with real AWS console screenshots published on Medium.

---

## Disclaimer

Screenshots and examples are based on a demo AWS environment.
All account IDs and IP addresses have been removed.
Adapted for educational use.

---

## About

Built by a GRC practitioner who has led SOC 2 Type II audits
to clean opinions on AWS infrastructure.

📫 ebohc@protonmail.com
