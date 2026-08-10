############################################
# Continuous Compliance Monitoring
# GuardDuty + Config -> EventBridge -> SNS
#
# Assumes an AWS Config recorder and delivery
# channel already exist in this account.
############################################

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

variable "notification_email" {
  description = "Email address to subscribe to the compliance/security SNS topic."
  type        = string
}

variable "guardduty_finding_severity_floor" {
  description = "Minimum GuardDuty severity that triggers a notification (4.0 = MEDIUM)."
  type        = number
  default     = 4.0
}

############################################
# GuardDuty
############################################

resource "aws_guardduty_detector" "main" {
  enable = true

  datasources {
    s3_logs {
      enable = true
    }
    kubernetes {
      audit_logs {
        enable = true
      }
    }
    malware_protection {
      scan_ec2_instance_with_findings {
        ebs_volumes {
          enable = true
        }
      }
    }
  }
}

############################################
# SNS topic for both GuardDuty and Config alerts
############################################

resource "aws_sns_topic" "compliance_alerts" {
  name = "continuous-compliance-alerts"
}

resource "aws_sns_topic_subscription" "email" {
  topic_arn = aws_sns_topic.compliance_alerts.arn
  protocol  = "email"
  endpoint  = var.notification_email
}

resource "aws_sns_topic_policy" "allow_eventbridge" {
  arn = aws_sns_topic.compliance_alerts.arn

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "AllowEventBridgePublish"
        Effect    = "Allow"
        Principal = { Service = "events.amazonaws.com" }
        Action    = "sns:Publish"
        Resource  = aws_sns_topic.compliance_alerts.arn
      }
    ]
  })
}

############################################
# EventBridge: GuardDuty findings >= severity floor
############################################

resource "aws_cloudwatch_event_rule" "guardduty_findings" {
  name        = "guardduty-findings-to-sns"
  description = "Routes GuardDuty findings at or above the configured severity floor to SNS."

  event_pattern = jsonencode({
    source      = ["aws.guardduty"]
    detail-type = ["GuardDuty Finding"]
    detail = {
      severity = [{ numeric = [">=", var.guardduty_finding_severity_floor] }]
    }
  })
}

resource "aws_cloudwatch_event_target" "guardduty_to_sns" {
  rule      = aws_cloudwatch_event_rule.guardduty_findings.name
  target_id = "guardduty-to-sns"
  arn       = aws_sns_topic.compliance_alerts.arn
}

############################################
# EventBridge: Config compliance state changes to NON_COMPLIANT
############################################

resource "aws_cloudwatch_event_rule" "config_noncompliant" {
  name        = "config-noncompliant-to-sns"
  description = "Routes AWS Config NON_COMPLIANT evaluations to SNS."

  event_pattern = jsonencode({
    source      = ["aws.config"]
    detail-type = ["Config Rules Compliance Change"]
    detail = {
      messageType     = ["ComplianceChangeNotification"]
      newEvaluationResult = {
        complianceType = ["NON_COMPLIANT"]
      }
    }
  })
}

resource "aws_cloudwatch_event_target" "config_to_sns" {
  rule      = aws_cloudwatch_event_rule.config_noncompliant.name
  target_id = "config-to-sns"
  arn       = aws_sns_topic.compliance_alerts.arn
}

############################################
# Config managed rules (see README section 4 for the
# full rule-to-framework mapping)
############################################

locals {
  security_config_rules = {
    "root-account-mfa-enabled"                  = "ROOT_ACCOUNT_MFA_ENABLED"
    "iam-user-mfa-enabled"                      = "IAM_USER_MFA_ENABLED"
    "iam-password-policy"                       = "IAM_PASSWORD_POLICY"
    "access-keys-rotated"                       = "ACCESS_KEYS_ROTATED"
    "s3-bucket-public-read-prohibited"          = "S3_BUCKET_PUBLIC_READ_PROHIBITED"
    "s3-bucket-public-write-prohibited"         = "S3_BUCKET_PUBLIC_WRITE_PROHIBITED"
    "s3-bucket-server-side-encryption-enabled"  = "S3_BUCKET_SERVER_SIDE_ENCRYPTION_ENABLED"
    "encrypted-volumes"                         = "ENCRYPTED_VOLUMES"
    "rds-storage-encrypted"                     = "RDS_STORAGE_ENCRYPTED"
    "cloudtrail-enabled"                        = "CLOUD_TRAIL_ENABLED"
    "cloud-trail-log-file-validation-enabled"   = "CLOUD_TRAIL_LOG_FILE_VALIDATION_ENABLED"
    "vpc-flow-logs-enabled"                     = "VPC_FLOW_LOGS_ENABLED"
    "restricted-ssh"                            = "INCOMING_SSH_DISABLED"
    "guardduty-enabled-centralized"             = "GUARDDUTY_ENABLED_CENTRALIZED"
  }
}

resource "aws_config_config_rule" "security_rules" {
  for_each = local.security_config_rules

  name = each.key

  source {
    owner             = "AWS"
    source_identifier = each.value
  }

  depends_on = [aws_guardduty_detector.main]
}

############################################
# Outputs
############################################

output "guardduty_detector_id" {
  value = aws_guardduty_detector.main.id
}

output "compliance_alerts_topic_arn" {
  value = aws_sns_topic.compliance_alerts.arn
}

output "config_rules_deployed" {
  value = keys(local.security_config_rules)
}
