![Amazon AWS Badge](https://img.shields.io/badge/Amazon%20AWS-232F3E?logo=amazonaws&logoColor=fff&style=for-the-badge)
# AWS Hands-On Projects
This repository contains step-by-step guides for hands-on AWS projects done by me.

## Table Of Contents

1. [Setting up a WordPress site using LightSail and a Load Balancer](#1-wordpress-site-on-lightsail-with-load-balancer)
2. [Hosting a static website on S3 with CloudFront and a custom domain using Route 53](#2-static-website-hosting-on-s3-with-cloudfront-and-route-53)
3. [Creating and using Amazon Simple Notification Service (SNS)](#3-amazon-simple-notification-service-sns)
4. [Increase volume of ec2 machine](#4-increase-ec2-volume-size)
5. [Auto Backup Files to S3 using Bash Script and Cron Job]()
6. [Auto Backup Files to S3 using Lambda-EventBridge-CloudWatch]()

## Projects Overview

### 1. WordPress Site on LightSail with Load Balancer

This project demonstrates how to set up two Amazon LightSail instances running WordPress and connect them to a Load Balancer for high availability and fault tolerance. It also includes instructions on how to host a website with a domain name from another DNS provider.

[Detailed Guide](./Handson-AmazonLightsail.md)

### 2. Static Website Hosting on S3 with CloudFront and Route 53

This project explains how to create an S3 bucket, upload your static content, and enable static website hosting. 
Additionally, it covers how to use CloudFront to distribute the content and Route 53 for DNS management, ensuring a secure and reliable web presence with a custom domain.

[Detailed Guide](./Handson-S3_Static_Website.md)

### 3. Amazon Simple Notification Service (SNS)

This guide provides step-by-step instructions to set up Amazon Simple Notification Service (SNS), create a topic, subscribe to the topic, and publish messages. 
It also includes additional features like integrating with AWS Lambda, Amazon SQS, and SMS notifications.

[Detailed Guide](./Handson-SNS.md)

### 4. Increase EC2 Volume size

This guide provides detailed instructions on how to modify the Elastic Block Store (EBS) volume and extend the file system to utilize the additional space. Ensuring proper volume resizing can help accommodate growing data needs and improve instance performance without causing downtime or data corruption. By following these steps, you can efficiently manage your EC2 storage and ensure your applications continue to run smoothly.

[Detailed Guide](./Handson-Ec2-increase-volume.md)

### 5. Auto Backup Files to S3 using Bash Script and Cron Job

This guide contains a shell script designed to back up 10 different directories on an EC2 instance to an AWS S3 bucket. The script also includes functionality to delete files older than 3 days from the local directories after the backup is completed. The backup process runs automatically using a cron job.

[Detailed Guide](./Handson-Backup-Files-to-S3.md)

### 6. Auto Backup Files to S3 using Lambda-EventBridge-CloudWatch

A complete setup where directories from an EC2 instance is backed up daily at 2 AM using AWS EventBridge and Lambda, and logs are maintained in CloudWatch Logs. The Lambda function triggers an SSM command to execute the backup script on the EC2 instance, and the script handles the backup and deletion of old files.

[Detailed Guide](./Handson-Lambda-EventBridge-CloudWatch.md)


## License

This project is licensed under the terms of the Apache license. See the LICENSE file for details.
