# Hands-On : AWS S3 Static Website Hosting Guide with Route 53

This guide provides step-by-step instructions to set up static website hosting on AWS S3 with CloudFront and a custom domain using Route 53, ensuring that you follow the necessary steps to achieve a secure and distributed web presence.

## Prerequisites
- An AWS account
- A registered domain name
- Basic knowledge of AWS Management Console

## Step 1: Create an S3 Bucket

1. **Log in to AWS Management Console**:
   - Navigate to the [S3 Console](https://console.aws.amazon.com/s3/).

     ScreenShot:
     ![image](https://github.com/AmalSunny992/handson-s3-static-website-hosting/assets/169422802/913a78a1-e1a8-42de-bafb-a1c274153365)


2. **Create a New S3 Bucket**:
   - Click on "Create bucket".
   - Enter a unique bucket name (e.g., `my-static-website-bucket`).
   - Select the appropriate AWS Region.
   - Click "Create bucket".

   ScreenShot:
   ![image](https://github.com/AmalSunny992/handson-s3-static-website-hosting/assets/169422802/6f72094b-8a6d-4eb2-82c4-cb09770beb70)

   ![image](https://github.com/AmalSunny992/handson-s3-static-website-hosting/assets/169422802/373e5fa7-dcd0-430c-a9c4-9eb660586282)


   
## Step 2: Upload Static Content

1. **Navigate to Your S3 Bucket**:
   - Click on the bucket name you just created.

2. **Upload Files**:
   - Click on the "Upload" button.
   - Add files by dragging and dropping or using the "Add files" button.
   - Click "Upload" to start the upload process.

   ScreenShot :
   ![image](https://github.com/AmalSunny992/handson-s3-static-website-hosting/assets/169422802/f2ed8210-793e-4830-a818-cdf3555b819f)


## Step 3: Enable Static Website Hosting

1. **Configure Static Website Hosting**:
   - In the S3 bucket, go to the "Properties" tab.
   - Scroll down to the "Static website hosting" section.
   - Select "Enable".
   - Enter the index document (e.g., `index.html`).
   - Optionally, enter an error document (e.g., `error.html`).
   - Click "Save".
  
     ScreenShot :
     ![image](https://github.com/AmalSunny992/handson-s3-static-website-hosting/assets/169422802/a09d3d16-b602-42f4-b0ee-a8fd13b7f265)


## Step 4: Set Up Bucket Policy for Public Access

1. **Edit Bucket Policy**:
   - Go to the "Permissions" tab.
   - Click on "Bucket Policy".
   - Add the following policy to make the bucket contents publicly accessible:
     ```json
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Sid": "PublicReadGetObject",
           "Effect": "Allow",
           "Principal": "*",
           "Action": "s3:GetObject",
           "Resource": "arn:aws:s3:::my-static-website-bucket/*"
         }
       ]
     }
     ```
   - Click "Save".
   
   ScreenShots :
   ![image](https://github.com/AmalSunny992/handson-s3-static-website-hosting/assets/169422802/cbdf6ec2-4c07-4b4a-a05f-f7e0281e7676)

## Step 5: Add a Custom Domain with CloudFront

1. **Create a CloudFront Distribution**:
   - Navigate to the [CloudFront Console](https://console.aws.amazon.com/cloudfront/).
   - Click on "Create Distribution".
   - Choose "Web" as the delivery method.
   - In the "Origin Settings", enter your S3 bucket URL (e.g., `my-static-website-bucket.s3.amazonaws.com`).
   - Under "Default Cache Behavior Settings", set the "Viewer Protocol Policy" to "Redirect HTTP to HTTPS".
   - Click "Create Distribution".

     Screenshot:
     ![image](https://github.com/AmalSunny992/handson-s3-static-website-hosting/assets/169422802/bcda40d3-2552-4d95-a4b5-a0a044c4df28)
 

2. **Configure Custom Domain in CloudFront**:
   - Click on your CloudFront distribution ID.
   - Go to the "General" tab.
   - Click on "Edit".
   - In the "Alternate Domain Names (CNAMEs)" field, enter your custom domain (e.g., `www.mycustomdomain.com`).
   - Click "Save Changes".
   
   ScreenShots:
   ![image](https://github.com/AmalSunny992/handson-s3-static-website-hosting/assets/169422802/741673b2-2e9e-48d3-a978-c0ec92a08f75)


3. **Set Up SSL/TLS Certificate**:
   - In the "General" tab of your CloudFront distribution, click on "Edit".
   - Under "SSL Certificate", choose "Custom SSL Certificate".
   - Select or request a new ACM certificate for your custom domain.
   - Click "Save Changes".
   - 
     ScreenShot:
     ![image](https://github.com/AmalSunny992/handson-s3-static-website-hosting/assets/169422802/78e357bb-8d2d-45d7-8544-3c6c2cb8861b)


## Step 6: Update DNS Records in Route 53

1. **Create a Hosted Zone**:
   - Navigate to the [Route 53 Console](https://console.aws.amazon.com/route53/).
   - Click on "Hosted zones".
   - Click on "Create Hosted Zone".
   - Enter your domain name and click "Create Hosted Zone".

     ScreenShot :
     ![image](https://github.com/AmalSunny992/handson-s3-static-website-hosting/assets/169422802/e0e8a025-1537-4d35-8726-f0618790552e)


2. **Add a Record Set**:
   - Click on the hosted zone for your domain.
   - Click on "Create Record".
   - Choose "Simple" record type.
   - Set the "Record Name" to your subdomain (e.g., `www`).
   - Choose "CNAME" as the "Record Type".
   - Enter your S3 bucket domain name (e.g., `d1234.cloudfront.net`).
   - Click "Create Records".

     Screenshot :
     ![image](https://github.com/AmalSunny992/handson-s3-static-website-hosting/assets/169422802/69744ca0-8581-4e62-8c60-84b264c94b60)

3. **Update Name Servers**:
   - Go to your domain registrar.
   - Replace the current name servers with the name servers provided by Route 53 in your hosted zone.


## Step 7: Test Your Setup

1. **Access Your Website**:
   - Open a web browser and navigate to your custom domain (e.g., `www.mycustomdomain.com`).
   - Ensure that your static content is loading securely over HTTPS.

     Screenshot:
     ![image](https://github.com/AmalSunny992/handson-s3-static-website-hosting/assets/169422802/97e65db9-1c54-4d07-bb9a-50d4af5273de)


## Summary

This guide covers creating an S3 bucket, uploading static content, enabling static website hosting, setting up a custom domain with Route 53, and using CloudFront with TLS to secure and distribute your content. Make sure to replace placeholder names (e.g., `my-static-website-bucket`, `www.mycustomdomain.com`) with your actual bucket name and domain.
