# EC2 : Increase Volume size

To increase the volume of an Ubuntu EC2 instance while it is running, follow these steps:

## Step 1: Modify the EBS Volume

Open the Amazon EC2 Console:

![image](https://github.com/AmalSunny992/AWS-Hands-On/assets/169422802/a7e42c29-5d81-4c5d-898b-fd217be3cabe)

![image](https://github.com/AmalSunny992/AWS-Hands-On/assets/169422802/af39f329-318b-47bb-ad81-865425833587)


Go to the EC2 Console.

Stop I/O Operations:

Although not mandatory, it is recommended to stop I/O operations to avoid potential data corruption. This can be done by stopping the application temporarily.

Locate the Volume:

![image](https://github.com/AmalSunny992/AWS-Hands-On/assets/169422802/dc34881f-d500-4531-b950-a18cf842db08)

In the left-hand menu, click on Volumes under the Elastic Block Store section.

Select the volume you want to resize.

Modify the Volume:

![image](https://github.com/AmalSunny992/AWS-Hands-On/assets/169422802/a6c0a175-d96d-4dd4-91c5-423ccff9a999)

Click on the Actions dropdown menu and select Modify Volume.
In the Size field, enter the new desired size for the volume.
Click Modify, then Yes to confirm.

![image](https://github.com/AmalSunny992/AWS-Hands-On/assets/169422802/b9bf6979-d0fd-4d59-b5e6-e047a7506895)

![image](https://github.com/AmalSunny992/AWS-Hands-On/assets/169422802/121b129a-9491-4189-be79-16718437b410)


## Step 2: Extend the File System

After modifying the volume, you need to extend the file system to use the additional space.

SSH into the EC2 Instance:

Open a terminal and SSH into your EC2 instance.
Check the Existing File System:

Run the following command to check the existing file system:

``` bash
df -h
```

Extend the File System:

For ext4 or ext3 File Systems:

```bash
sudo resize2fs /dev/xvda1
```
Replace /dev/xvda1 with your specific device name.



Verify the Changes:

Run the df -h command again to ensure the file system now uses the additional space.


![image](https://github.com/AmalSunny992/AWS-Hands-On/assets/169422802/386844a7-925a-49f7-8b41-9618bc8f069e)


Example Commands

```bash

# SSH into your instance

ssh -i your-key.pem ubuntu@your-ec2-instance-ip

# Check the file system

df -h

# For ext4/ext3 file system

sudo resize2fs /dev/xvda1

# Verify the changes
df -h

```

## Additional Tips

**Backup Data:** Always backup your data before performing operations on your volume.

**Ensure Sufficient Quota:** Verify that you have sufficient quota in your AWS account for the new volume size.

**Monitor Performance:** After resizing, monitor the instance performance to ensure everything is functioning as expected.
