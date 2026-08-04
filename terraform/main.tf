# Create the S3 Bucket
resource"aws_s3_bucket" "backup_bucket" {
  bucket = var.bucket_name

  tags = {
    Name        = "Log Backup Bucket"
    Environment = "Production"
    ManagedBy   = "Terraform"
  }
}

# create the iam user

resource "aws_iam_user" "backup_bot" {
  name = var.bot_username
  path = "/"

  tags = {
    Environment = "Production"
    ManagedBy   = "Terraform"
    Name        = "S3 Backup Bot"
  }
}

# create the access ID and key

resource "aws_iam_access_key" "bot_keys" {
  user = aws_iam_user.backup_bot.name
}

output "bot_access_key_id" {
  description = "The Access Key ID for the S3 backup bot"
  value       = aws_iam_access_key.bot_keys.id
}

output "bot_secret_access_key" {
  description = "The Secret Access Key for the S3 backup bot"
  value       = aws_iam_access_key.bot_keys.secret
  sensitive   = true
}

# use the function templatefile() to fetch the policy.json

resource "aws_iam_policy" "bot_s3_policy" {
  name        = "S3BackupBotPolicy"
  description = "Allows the backup bot to put objects into the specific backup bucket"

  # This tells Terraform to go up one folder level to find your JSON, 
  # and pass the dynamic bucket ARN into it!
  policy = templatefile("${path.module}/../policy.json", {
    bucket_arn = aws_s3_bucket.backup_bucket.arn
  })
}

resource "aws_iam_user_policy_attachment" "bot_policy_attach" {
  user       = aws_iam_user.backup_bot.name
  policy_arn = aws_iam_policy.bot_s3_policy.arn
}
