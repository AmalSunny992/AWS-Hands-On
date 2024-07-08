import boto3
import time

# AWS clients
ec2_client = boto3.client('ec2')
ssm_client = boto3.client('ssm')

# AWS Configurations
AWS_REGION = 'ap-southeast-1'
AWS_PROFILE = 'default'  # Replace with your AWS profile name if necessary
BUCKET_NAME = 'my-ec2-backup-files'
BACKUP_DIRS = ["config-files", "config-tables", "os-config", "sys-config", "sys-control", "sys-data", "sys-updates", "usr-config", "usr-control", "usr-data"]

def lambda_handler(event, context):
    # Set AWS profile and region
    # boto3.setup_default_session(profile_name=AWS_PROFILE, region_name=AWS_REGION)
    
    # Fetch instance ID by name
    instance_ids = get_instance_ids_by_name(["Jenkins"])  # Replace with your instance name
    print (instance_ids)
    
    if not instance_ids:
        return {
            'statusCode': 404,
            'body': 'No instances found with the specified name'
        }
    
    # Start instances if not running
    for instance_id in instance_ids:
        instance_state = get_instance_state(instance_id)
        if instance_state != 'running':
            start_instance(instance_id)
            wait_instance_running(instance_id)
    
    # Create backup script
    backup_script = create_backup_script()
    
    # Send SSM command to each instance
    try:
        for instance_id in instance_ids:
            send_ssm_command(instance_id, backup_script)
    
        return {
            'statusCode': 200,
            'body': 'Backup process initiated successfully'
        }
    except Exception as e:
        logger.error(f"Failed to send SSM command: {e}")

def create_backup_script():
    script_lines = [
        "#!/bin/bash",
        "AWS_CLI=/usr/local/bin/aws",
        "export HOME=/home/ubuntu",
        "DATE=$(date +%Y%m%d%H%M%S)",
        "BACKUP_DIRS=(" + " ".join(BACKUP_DIRS) + ")",
        "S3_PATH=\"s3://{}/backups/$DATE\"".format(BUCKET_NAME),
        "for dir in \"${BACKUP_DIRS[@]}\"; do",
        "  if [ -d \"$HOME/$dir\" ]; then",
        "    aws s3 cp \"$HOME/$dir/\" \"$S3_PATH/$dir/\" --recursive",
        "    find \"$HOME/$dir\" -type f -mtime +3 -exec rm -f {} \\;",
        "  fi",
        "done"
    ]
    return "\n".join(script_lines)

def get_instance_ids_by_name(instance_names):
    response = ec2_client.describe_instances(
        Filters=[
            {'Name': 'tag:Name', 'Values': instance_names},
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
    )
    instance_ids = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])
    return instance_ids

def get_instance_state(instance_id):
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    state = response['Reservations'][0]['Instances'][0]['State']['Name']
    return state

def start_instance(instance_id):
    ec2_client.start_instances(InstanceIds=[instance_id])

def wait_instance_running(instance_id):
    waiter = ec2_client.get_waiter('instance_running')
    waiter.wait(InstanceIds=[instance_id])

def send_ssm_command(instance_id, script):
    response = ssm_client.send_command(
        InstanceIds=[instance_id],
        DocumentName="AWS-RunShellScript",
        Parameters={'commands': [script]},
        TimeoutSeconds=3600
    )
    command_id = response['Command']['CommandId']
    check_command_status(command_id, instance_id)

def check_command_status(command_id, instance_id):
    time.sleep(10)
    response = ssm_client.list_command_invocations(
        CommandId=command_id,
        InstanceId=instance_id,
        Details=True
    )
    for invocation in response['CommandInvocations']:
        if invocation['Status'] == 'Success':
            print("Backup successful.")
        else:
            print("Backup failed: " + invocation['StatusDetails'])

