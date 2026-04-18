# aws-python-ops-scripts

AWS Python automation toolkit for managing EC2, EBS, S3, IAM, and cloud operations tasks.

## Current Scripts

### ebs/delete_unused_ebs_snapshots.py
Python script to identify and delete unused or orphan EBS snapshots in AWS.  
The script checks snapshots owned by the account, verifies whether the associated EBS volume exists and is attached to an EC2 instance, and removes snapshots whose source volumes are deleted or no longer in use.

#### Requirements

- Python 3
- boto3
- AWS credentials configured

#### Install

pip install -r requirements.txt

#### Run

python3 ebs/delete_unused_ebs_snapshots.py
