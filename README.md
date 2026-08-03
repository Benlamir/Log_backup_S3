# ☁️ Automated S3 Backup & Archiving (FinOps)

This project is a complete Cloud Engineering and DevOps tool designed to generate local log files, securely back them up to AWS S3, and optimize storage costs using S3 Lifecycle Rules.

## 🎯 Key Features

### Log Generation

A Python script that uses standard Python modules such as `os`, `time`, and `random` to generate sample text log files in a designated local directory.

### Secure Backup

A main backup script that uses `boto3` to authenticate with AWS and upload new log files to an Amazon S3 bucket using the **S3 Standard** storage class.

### FinOps — Cost Optimization

A lifecycle manager that uses the `boto3` API to apply an S3 Lifecycle Rule to the bucket. Older files are automatically transitioned to **Amazon S3 Glacier** to reduce long-term storage costs.

### System Automation

A Linux `cron` job automatically runs the backup process without requiring manual intervention.

---

# 🏗️ Technical Architecture (OOP)

The project was developed using **Object-Oriented Programming (OOP)** to maintain clean, modular, and reusable code.

It is organized around three separate classes, each located in its own Python script and responsible for a specific part of the application:

### `LogGenerator` — `generate_logs.py`

Contains the logic required to generate sample text log files using standard Python modules.

### `S3BackupManager` — `s3_backup.py`

The core component of the project. It uses `boto3` to authenticate with AWS and upload log files to Amazon S3 using the **S3 Standard** storage class.

### `S3LifecycleManager` — `s3_lifecycle.py`

Uses the `boto3` API to create and apply S3 Lifecycle Rules that automatically archive older files.

---

# 🔒 Security and IAM

The application follows the **Principle of Least Privilege**, ensuring that the AWS user or bot has access only to the permissions required to perform its tasks.

Authentication is handled through a dedicated AWS profile with restricted permissions and securely configured credentials.

The `policy.json` file, which defines the limited IAM permissions, is stored locally and excluded from version control.

> **Security Note:** Never upload AWS access keys, secret keys, or sensitive IAM configuration files to GitHub.

---

# 🚀 Installation and Configuration

## 1. Prerequisites

Before running the project, make sure you have the following installed:

* Python 3
* Linux
* AWS CLI
* An authenticated AWS account

## 2. Create a Virtual Environment

A Python virtual environment (`venv`) is used to isolate the project's dependencies.

```bash
python3 -m venv venv
source venv/bin/activate
pip install boto3
```

> **Note:** The `venv/` directory isolates the project's Python dependencies and prevents installation files from being uploaded to the GitHub repository.
>
> Local log directories and backup registry files are also excluded using `.gitignore`.

## 3. Configure AWS CLI

Use the AWS CLI to create a dedicated AWS profile:

```bash
aws configure --profile s3-backup-bot
```

You will be asked to provide:

* AWS Access Key ID
* AWS Secret Access Key
* Default AWS Region
* Default output format

The credentials will be stored in the AWS credentials configuration under:

```text
~/.aws/credentials
```

---

# ⚙️ Usage

## Generate Test Logs

Run the following command to generate sample log files:

```bash
python3 generate_logs.py
```

## Back Up Logs to Amazon S3

Run the backup script:

```bash
python3 s3_backup.py
```

## Apply the S3 Lifecycle Rule

Run the lifecycle manager:

```bash
python3 s3_lifecycle.py
```

---

# ⏱️ Automation with Cron

To run the backup script automatically every night at **2:00 AM**, add the following entry to your Linux `crontab`:

```bash
00 02 * * * /absolute/path/to/venv/bin/python3 /absolute/path/to/s3_backup.py
```

Open the `crontab` editor with:

```bash
crontab -e
```

Then add the cron job and save the file.

> Replace `/absolute/path/to/` with the actual absolute paths on your system.

---

# 📁 Project Structure

```text
Log_backup_S3/               <-- Your existing local folder
├── s3_backup.py
├── generate_logs.py
├── policy.json              <-- Your existing IAM rules!
├── ...
└── terraform/               <-- NEW: Your Infrastructure folder
    ├── provider.tf
    ├── main.tf
    └── variables.tf
```


---

# 🛠️ Technologies Used

* **Python 3**
* **Boto3**
* **AWS S3**
* **Amazon S3 Glacier**
* **AWS IAM**
* **AWS CLI**
* **Linux**
* **Cron**
* **Object-Oriented Programming (OOP)**
* **FinOps**

