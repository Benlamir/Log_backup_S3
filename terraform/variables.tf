variable "bucket_name" {
  description = "The name of the S3 bucket for storing backups"
  type        = string
  default     = "benlamir-logs-backup-2026"
}

variable "bot_username" {
  description = "The name of the IAM user that will run the backup script"
  type        = string
  default     = "s3-backup-bot"
}
