# Docker-EBS-Persistent-Volume
Creating a project that deploys a Docker container on an EC2 instance with a persistent volume using EBS involves several steps. 

## Prerequisites
AWS Account: Ensure you have an AWS account.
AWS CLI: Install and configure the AWS CLI on your local machine.
Docker: Install Docker on your local machine for building the Docker image.
Terraform or AWS Management Console: Optional for resource provisioning.

## Steps
- Create an EBS Volume: This will be used as the persistent storage.
- Launch an EC2 Instance: This instance will host your Docker container.
- Attach the EBS Volume to the EC2 Instance.
- Install Docker on the EC2 Instance.
- Deploy the Docker Container.
- Mount the EBS Volume Inside the Docker Container.

### Step 1: Create an EBS Volume
```sh
aws ec2 create-volume --availability-zone us-west-2a --size 10 --volume-type gp2
#Save the Volume ID from the response, e.g., vol-1234567890abcdef0.
```

### Step 2: Attach the EBS Volume to the EC2 Instance
```sh
aws ec2 attach-volume --volume-id vol-1234567890abcdef0 --instance-id i-1234567890abcdef0 --device /dev/sdf
```

### Step 3: Install Docker on the EC2 Instance

Install Docker:

```sh
sudo yum update -y
sudo amazon-linux-extras install docker
sudo service docker start
sudo usermod -a -G docker ec2-user
```

Log out and log back in to apply the new group membership.

### Step 4: Deploy the Docker Container

First, create a Dockerfile on your local machine:

Dockerfile

#Dockerfile
FROM nginx:latest
COPY . /usr/share/nginx/html


Build and push the Docker image to Docker Hub or any other container registry:
```sh
docker build -t my-nginx .
docker tag my-nginx:latest <your-dockerhub-username>/my-nginx:latest
docker push <your-dockerhub-username>/my-nginx:latest
```

On the EC2 instance, pull and run the Docker container:

```sh
docker pull <your-dockerhub-username>/my-nginx:latest
```

### Step 5: Mount the EBS Volume Inside the Docker Container

Format and mount the EBS volume:

```sh
sudo mkfs -t ext4 /dev/xvdf
sudo mkdir /mnt/ebs
sudo mount /dev/xvdf /mnt/ebs
sudo chown ec2-user:ec2-user /mnt/ebs
```

Run the Docker container with the EBS volume mounted:

```sh
docker run -d -p 80:80 -v /mnt/ebs:/usr/share/nginx/html <your-dockerhub-username>/my-nginx:latest
```
## Conclusion
This guide provides a high-level overview of deploying a Docker container on an EC2 instance with persistent storage from an EBS volume.
