#!/bin/bash

# Set AWS CLI path
AWS_CLI="/usr/local/bin/aws"

# Set AWS credentials and region
export AWS_PROFILE=admin
export AWS_DEFAULT_REGION=ap-southeast-1
export HOME=/home/ubuntu

# Variables
BUCKET_NAME="my-ubuntu-backup"
BACKUP_DIRS=("config-files" "config-tables" "os-config" "sys-config" "sys-control" "sys-data" "sys-updates" "usr-config" "usr-control" "usr-data")
DATE=$(date +%Y%m%d%H%M%S)
S3_PATH="s3://$BUCKET_NAME/backups/$DATE"
LOG_FILE="$HOME/backup-log/backup_to_s3.log"

# Function to log messages
log_message() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" >> $LOG_FILE
}

# Function to backup directories
backup_directory() {
    local dir=$1
    log_message "Backing up $dir to $S3_PATH/$dir"
    if ! aws s3 cp "$HOME/$dir/" "$S3_PATH/$dir/" --recursive >> $LOG_FILE 2>&1; then
        log_message "Error backing up $dir"
        return 1
    else
        log_message "Successfully backed up $dir"
    fi
}

# Function to delete files older than 3 days
delete_old_files() {
    local dir=$1
    log_message "Deleting files older than 3 days in $dir"
    if ! find "$dir" -type f -mtime +3 -exec rm -f {} \; >> $LOG_FILE 2>&1; then
        log_message "Error deleting files in $dir"
        return 1
    else
        log_message "Successfully deleted old files in $dir"
    fi
}

# Start backup process
log_message "========================================================================[Backup started]================================================================"

for dir in "${BACKUP_DIRS[@]}"; do
    if [ -d "$dir" ]; then
        if ! backup_directory "$dir"; then
            log_message "Failed to backup $dir"
        fi
        if ! delete_old_files "$dir"; then
            log_message "Failed to delete old files in $dir"
        fi
    else
        log_message "Directory $dir does not exist"
    fi
done

log_message "==================================================================[Backup completed]==================================================================="
