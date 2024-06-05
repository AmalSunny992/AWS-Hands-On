# Hands-On : Amazon Simple Notification Service (SNS)

## Table of Contents
1. [Introduction](#introduction)
2. [Prerequites](#prerequisites)
3. [How to create an SNS](#how-to-create-an-sns)
4. [Additional Features](#additional-features)
5. [An Example Use Case](#an-example-use-case)
6. [Conclusion](#conclusion)

## Introduction

This guide provides step-by-step instructions to set up Amazon Simple Notification Service (SNS) using the AWS Management Console. Amazon SNS is a fully managed messaging service for both system-to-system and app-to-person communication. This guide will help you create an SNS topic, subscribe to the topic, and publish messages to the topic.

## Prerequisites

- An AWS account
- Basic knowledge of AWS Management Console

## How to Create an SNS

### Step 1: Create an SNS Topic

1. **Log in to AWS Management Console**:
   - Navigate to the [SNS Console](https://console.aws.amazon.com/sns/).

2. **Create a New Topic**:
   - Click on "Topics" in the left-hand menu.
   - Click on the "Create topic" button.
   - Choose the "Standard" or "FIFO" topic type depending on your use case. For most cases, "Standard" is sufficient.
   - Enter a name for your topic (e.g., `MyFirstSNSTopic`).
   - Optionally, you can configure other settings like Display name, Encryption, and Access policy.
   - Click "Create topic".

ScreenShot:     

![image](https://github.com/AmalSunny992/AWS_Hands_On/assets/169422802/afad25b0-4fef-4143-b49d-06ab75ed6a4e)


### Step 2: Subscribe to the SNS Topic

1. **Add a Subscription**:
   - After creating the topic, click on the topic name to open its details.
   - Click on the "Create subscription" button.

2. **Configure Subscription**:
   - Select a protocol from the drop-down menu (e.g., Email, HTTP, HTTPS, SQS, Lambda).
   - Enter the endpoint for the selected protocol (e.g., your email address if you selected the Email protocol).
   - Optionally, you can configure the filter policy and redrive policy.
   - Click "Create subscription".

ScreenShot:

![image](https://github.com/AmalSunny992/AWS_Hands_On/assets/169422802/e5f251eb-cb3e-45fc-a326-35c9b3879dfe)

3. **Confirm Subscription** (For Email Protocol):
   - If you chose the Email protocol, check your email for a subscription confirmation message.
   - Click on the confirmation link in the email to confirm the subscription.

ScreenShot:

![image](https://github.com/AmalSunny992/AWS_Hands_On/assets/169422802/7abe5582-9b32-4c77-8f7b-5c686a40b2f4)

### Step 3: Publish a Message to the SNS Topic

1. **Publish Message**:
   - In the SNS Console, navigate to your topic details page.
   - Click on the "Publish message" button.

2. **Enter Message Details**:
   - Enter a subject for your message.
   - Enter the message body.
   - Optionally, you can configure other settings like Message attributes and Message structure.
   - Click "Publish message".

ScreenShot:

  ![image](https://github.com/AmalSunny992/AWS_Hands_On/assets/169422802/7f3db452-005b-48ac-9210-7bcb3888dc1c)


3. **Verify Message Delivery**:
   - Depending on the protocol you subscribed to, verify that the message was delivered (e.g., check your email inbox if you subscribed via Email).

ScreenShot:

![image](https://github.com/AmalSunny992/AWS_Hands_On/assets/169422802/5e89ec2f-c3ab-43ef-8faa-6e7365084ed0)

## Additional Features

#### 1. **Using SNS with AWS Lambda**
   - You can trigger AWS Lambda functions in response to messages published to an SNS topic. To do this, create a new subscription with the protocol set to "AWS Lambda" and enter the ARN of your Lambda function.

#### 2. **Using SNS with Amazon SQS**
   - You can use SNS to fan out messages to multiple SQS queues. Create a new subscription with the protocol set to "Amazon SQS" and enter the ARN of your SQS queue.

#### 3. **SMS Notifications**
   - SNS can send SMS messages to phone numbers. Create a new subscription with the protocol set to "SMS" and enter the phone number.

#### 4. **Message Filtering**
   - You can use message filtering to selectively send messages to subscribers based on message attributes. This is useful for implementing fine-grained control over message delivery.

## An Example Use Case

Amazon SNS notification to alert you when an EC2 instance's CPU usage exceeds 10%.

### Step 1: Create an SNS Topic
- Sign in to the AWS Management Console and open the [Amazon SNS console](https://console.aws.amazon.com/sns/v3/home).
- In the left navigation pane, choose Topics.
- Choose Create topic.
- For Type, select Standard.
- For Name, enter a name for your topic, such as EC2HighCPUNotification.
- Choose Create topic.

ScreenShot:

![image](https://github.com/AmalSunny992/AWS_Hands_On/assets/169422802/62dfa8cb-d570-4e71-b6c5-99b9c05cc303)

### Step 2: Create an SNS Subscription
- After creating the topic, you will be directed to the topic details page.
- Choose Create subscription.
- For Protocol, choose Email.
- For Endpoint, enter your email address.
- Choose Create subscription.
- Check your email inbox for a subscription confirmation email from AWS Notifications and confirm the subscription by clicking the link in the email.

Screenshots:

![image](https://github.com/AmalSunny992/AWS_Hands_On/assets/169422802/57aae8cd-dbb5-4642-afa0-bb9db0a8a8b2)

![image](https://github.com/AmalSunny992/AWS_Hands_On/assets/169422802/6afb5c1d-889d-4689-8410-c7c528947dd0)

![image](https://github.com/AmalSunny992/AWS_Hands_On/assets/169422802/6b774733-b5e7-4602-ad59-fdbfe55078ea)


### Step 3: Create a CloudWatch Alarm
- Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/).
- In the left navigation pane, choose Alarms, then choose All alarms.
- Choose Create alarm.
- Choose Select metric.
- In the Browse tab, choose EC2, then Per-Instance Metrics.
- Find and select the CPUUtilization metric for your instance. You can use the search bar to filter by instance ID or name. Once you’ve selected the metric, click Select metric.
- Under Metric name, ensure that CPUUtilization is selected and click Select metric.

### Step 4: Configure the Alarm
- In the Create Alarm wizard, under Specify metric and conditions:
   - Statistic: Choose Average.
   - Period: Set to 5 minutes (or 300 seconds).
   - Threshold type: Choose Static.
   - Whenever CPUUtilization is: Select Greater than.
   - Threshold: Enter 10.
- Choose Next to configure actions.

### Step 5: Configure Actions
- Under Notification, choose In alarm.
- For Send a notification to, choose the SNS topic you created earlier (EC2HighCPUNotification).
- Choose Next to add a name and description for the alarm.

### Step 6: Name and Description
- Enter a name for the alarm, such as EC2HighCPUAlarm.
- Optionally, add a description.
- Choose Next to preview the alarm.

### Step 7: Preview and Create
- Review the alarm configuration and ensure all details are correct.
- Choose Create alarm.

ScreenShots:

![image](https://github.com/AmalSunny992/AWS_Hands_On/assets/169422802/a2d526e6-82f2-4222-a482-98328d9345b3)

![image](https://github.com/AmalSunny992/AWS_Hands_On/assets/169422802/a11492f3-09d9-4d93-89d0-878e3d6f908f)

![image](https://github.com/AmalSunny992/AWS_Hands_On/assets/169422802/65b851d7-d486-411e-923d-09369f082b12)


## Conclusion

Amazon SNS is a powerful and flexible messaging service that integrates seamlessly with many AWS services. This guide covers the basics of creating an SNS topic, subscribing to it, and publishing messages. Explore additional features like Lambda triggers, SQS integration, and message filtering to fully leverage SNS in your applications.
