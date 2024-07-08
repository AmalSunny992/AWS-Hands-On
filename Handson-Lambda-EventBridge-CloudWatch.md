# Automated Backup Solution with AWS CloudWatch, EventBridge, and Lambda

Step-by-Step Guide to Back Up Directories from an EC2 Instance Using AWS EventBridge and Lambda
We'll create a solution where an AWS Lambda function backs up specific directories from an EC2 instance daily at 2 AM.
The backup will be stored in an S3 bucket and files older than 3 days will be deleted from the mentioned directories. 
CloudWatch Logs will be used for logging.

## Step 1: Set Up IAM Roles and Policies

Create an IAM Role for the EC2 instance (Jenkins) with the necessary permissions to allow the Lambda function to access it. Attach the following policy to the role

Create an IAM Role for Lambda with the following policy to allow necessary actions

## Step 2: Create the Lambda Function

Create a Lambda function in the AWS Management Console.

Upload the following script as the Lambda function ([lambda_function.py](./lambda_function.py))

## Step 3: Create an EventBridge Rule
Navigate to the EventBridge console and create a new rule.

Configure the rule to trigger at 2 AM every day:

- Rule type: Schedule
- Schedule pattern: cron(0 2 * * ? *)
- Set the target to the Lambda function created in Step 2.

Screenshots:
![image](https://github.com/AmalSunny992/AWS-Hands-On/assets/169422802/85b029e5-e49f-40c2-9490-8fcd3f91cfa2)

![image](https://github.com/AmalSunny992/AWS-Hands-On/assets/169422802/533f87d5-9163-4f7c-974e-db9b6eee781e)

![image](https://github.com/AmalSunny992/AWS-Hands-On/assets/169422802/470c1081-86d9-42a7-acf1-b8e4f30a5702)

## Step 4: Configure CloudWatch Logs
In the Lambda function's configuration, ensure that CloudWatch Logs is enabled to capture the output and errors.

![image](https://github.com/AmalSunny992/AWS-Hands-On/assets/169422802/f6dc567d-f847-4624-9581-ac003e10f4bb)

Verify the log group and log stream in the CloudWatch Logs console to ensure that the logs are being generated.

![image](https://github.com/AmalSunny992/AWS-Hands-On/assets/169422802/f5a09b1c-706a-424a-baac-6f87065c0dc2)


## Final Setup on the EC2 Instance
Ensure the IAM Role with S3 and CloudWatch permissions is attached to the EC2 instance.

Install the AWS CLI if it's not already installed

Ensure the AWS credentials are configured on the EC2 instance.

## S3 Bucket 

Screenshot afer back up is  done 

![image](https://github.com/AmalSunny992/AWS-Hands-On/assets/169422802/b7e0e569-ccd9-4393-af44-2459a90c2a12)

![image](https://github.com/AmalSunny992/AWS-Hands-On/assets/169422802/c788bf6f-8274-4b60-a359-710584c6229a)

![image](https://github.com/AmalSunny992/AWS-Hands-On/assets/169422802/b427c14c-541a-4cc7-9dfd-0f7b930b0f18)

![image](https://github.com/AmalSunny992/AWS-Hands-On/assets/169422802/b17bc9ba-f47c-4619-a89f-013e4b34fca8)


## Conclusion
With these steps, you have a complete setup where directories from an EC2 instance is backed up daily at 2 AM using AWS EventBridge and Lambda, and logs are maintained in CloudWatch Logs. The Lambda function triggers an SSM command to execute the backup script on the EC2 instance, and the script handles the backup and deletion of old files.
