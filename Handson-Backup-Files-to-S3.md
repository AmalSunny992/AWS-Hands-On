# Backup Files to AWS S3
This hands on contains a shell script for backing up 10 specified directories to an AWS S3 bucket. 
The script also includes functionality to delete files older than 3 days from the local directories and can be scheduled to run automatically every day using a cron job.

## Prerequisites
Before running the script, ensure the following:

**AWS CLI**: The AWS CLI should be installed and configured on your system.

**AWS Profile**: An AWS profile named admin should be set up with the necessary permissions to upload to the S3 bucket.

**AWS S3 Bucket**: A designated S3 bucket where the backups will be stored.

![image](https://github.com/AmalSunny992/AWS-Hands-On/assets/169422802/164d76c0-f195-4091-8428-6a7d2abcb146)

**Log Directory**: Ensure the log directory ($HOME/backup-log/) exists.

## Script Overview
The script performs the following tasks:

1. Set AWS Environment Variables: Sets the AWS profile, region, and home directory.
2. Define Backup Variables: Specifies the directories to back up and the S3 bucket path.
3. Log Messages: Logs messages to a log file for tracking the backup process.
4. Backup Directories: Copies the specified directories to the S3 bucket.
5. Delete Old Files: Deletes files older than 3 days in the specified directories.
6. Log Backup Completion: Logs the completion of the backup process.

## Script Details
### Variables
- **AWS_CLI**: Path to the AWS CLI executable.
- **AWS_PROFILE**: AWS profile to use for authentication.
- **AWS_DEFAULT_REGION**: AWS region where the S3 bucket is located.
- **HOME**: Home directory of the user.
- **BUCKET_NAME**: Name of the S3 bucket.
- **BACKUP_DIRS**: Array of directories to back up.
- **DATE**: Timestamp for the backup.
- **S3_PATH**: S3 bucket path where backups will be stored.
- **LOG_FILE**: Path to the log file.

### Functions

**log_message()**
Logs messages with a timestamp to the log file.

**backup_directory()**
Backs up a specified directory to the S3 bucket and logs the process.

**delete_old_files()**
Deletes files older than 3 days in a specified directory and logs the process.

### Backup Process
The script iterates over the directories listed in BACKUP_DIRS, backing up each one to the S3 bucket and then deleting files older than 3 days from the local directory. 
The process is logged for monitoring and troubleshooting purposes.

## Script

Script File : [backup-to-s3](./backup-to-s3.sh)


Make the script executable:

```bash
chmod +x backup_to_s3.sh
```

## Automating the Backup with Cron

To automate the backup process to run daily, you can set up a cron job:

Open the cron table for editing:

```bash

crontab -e

#Add the following line to schedule the script to run every day at 2 AM:

0 2 * * * /home/ubuntu/your-repository/backup_to_s3.sh

#Save and exit the editor.
```
Screenshots of bacjed up s3 bucket : 

![image](https://github.com/AmalSunny992/AWS-Hands-On/assets/169422802/5b3569db-110d-4d68-84ba-17b47fc61234)

![image](https://github.com/AmalSunny992/AWS-Hands-On/assets/169422802/a2f9f091-d29e-491a-913e-b7208c4427d1)

## Example Log Output

Log File : [backup_to_s3.log](./backup_to_s3.log)

## Troubleshooting
Ensure that the AWS CLI is properly installed and configured.

Verify that the admin profile has the necessary permissions to upload to the S3 bucket.

Check the log file ($HOME/backup-log/backup_to_s3.log) for any errors or issues.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
