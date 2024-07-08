# Automated Backup Solution with AWS CloudWatch, EventBridge, and Lambda

This guide explains how to set up an automated backup solution for your server directories to an S3 bucket using AWS CloudWatch, EventBridge, and Lambda.

## Prerequisites

- AWS CLI installed and configured with necessary permissions.
- AWS IAM user with appropriate permissions to create CloudWatch, EventBridge, Lambda, and S3 resources.
- A pre-existing S3 bucket to store the backups.

## Steps

### 1. Create IAM Role for Lambda

Create an IAM role that Lambda will use to execute the backup script and access S3.

1. Go to the IAM console.

2. Create a new role with the following permissions:
   - AWSLambdaBasicExecutionRole
   - AmazonS3FullAccess

3. Note the ARN of the newly created role.

### 2. Create Lambda Function

Create a Lambda function that will execute the backup script.

1. Go to the Lambda console.

2. Create a new function:
   - **Name**: `BackupToS3Function`
   - **Runtime**: Python 3.x
   - **Role**: Use the IAM role created earlier

3. Use the following Python code for the Lambda function:
   
   ```python
   import subprocess
   import logging

   logger = logging.getLogger()
   logger.setLevel(logging.INFO)

   def lambda_handler(event, context):
       command = "/home/ubuntu/backup_script.sh"
       try:
           result = subprocess.run([command], capture_output=True, text=True, check=True)
           logger.info(result.stdout)
           return {
               'statusCode': 200,
               'body': 'Backup script executed successfully'
           }
       except subprocess.CalledProcessError as e:
           logger.error(e.stderr)
           return {
               'statusCode': 500,
               'body': 'Backup script execution failed'
           }

Upload the backup script (backup_script.sh) to the Lambda function's deployment package.

### 3. Create EventBridge Rule

Create an EventBridge rule to trigger the Lambda function on a schedule.

Go to the EventBridge console.

Create a new rule:

Name: DailyBackupRule

Event Source: EventBridge

Schedule: Cron expression (e.g., cron(0 0 * * ? *) for daily at midnight)

Add a target:

Target: Lambda function

Function: BackupToS3Function

### 4. Create CloudWatch Log Group

Ensure CloudWatch logging is enabled to monitor the execution of the Lambda function.

Go to the CloudWatch console.

Create a new log group (if not already created):

Name: /aws/lambda/BackupToS3Function

Backup Script 


## Conclusion
By following this guide, you will have set up an automated backup solution that uses CloudWatch, EventBridge, and Lambda to back up your directories to an S3 bucket. This setup ensures that backups are performed regularly without manual intervention.
