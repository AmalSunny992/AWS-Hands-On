# EC2 : Increase Volume size

To increase the volume of an Ubuntu EC2 instance while it is running, follow these steps:

## Step 1: Modify the EBS Volume

Open the Amazon EC2 Console:

Go to the EC2 Console.
Stop I/O Operations:

Although not mandatory, it is recommended to stop I/O operations to avoid potential data corruption. This can be done by stopping the application temporarily.
Locate the Volume:

In the left-hand menu, click on Volumes under the Elastic Block Store section.
Select the volume you want to resize.
Modify the Volume:

Click on the Actions dropdown menu and select Modify Volume.
In the Size field, enter the new desired size for the volume.
Click Modify, then Yes to confirm.


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
``

Replace /dev/xvda1 with your specific device name.

Verify the Changes:

Run the df -h command again to ensure the file system now uses the additional space.


Example Commands

```bash

# SSH into your instance

ssh -i your-key.pem ubuntu@your-ec2-instance-ip

# Check the file system

df -h

# For ext4/ext3 file system

sudo resize2fs /dev/xvda1

# For XFS file system

sudo xfs_growfs -d /


# Verify the changes
df -h

```

## Additional Tips

**Backup Data:** Always backup your data before performing operations on your volume.
**Ensure Sufficient Quota:** Verify that you have sufficient quota in your AWS account for the new volume size.
**Monitor Performance:** After resizing, monitor the instance performance to ensure everything is functioning as expected.
