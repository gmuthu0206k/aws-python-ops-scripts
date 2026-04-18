import boto3


ec2 = boto3.client('ec2')


def main():

    # Get all snapshots owned by your account
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']

    # Process each snapshot
    for snapshot in snapshots:

        snapshot_id = snapshot['SnapshotId']
        volume_id = snapshot.get('VolumeId')

        # Skip if no volume id
        if not volume_id:
            continue

        try:
            # Get volume details
            volume_response = ec2.describe_volumes(
                VolumeIds=[volume_id]
            )

            volumes = volume_response['Volumes']

            # If volume exists
            if volumes:

                volume = volumes[0]
                attachments = volume['Attachments']

                # If volume not attached
                if len(attachments) == 0:

                    ec2.delete_snapshot(
                        SnapshotId=snapshot_id
                    )

                    print(f"Deleted snapshot: {snapshot_id}")
                else:
                    print(
                        f"Snapshot {snapshot_id} is attached with instance {attachments[0]['InstanceId']}")

        except Exception as e:
            if "InvalidVolume.NotFound" in str(e):
                ec2.delete_snapshot(SnapshotId=snapshot_id)
                print(f"Deleted orphan snapshot: {snapshot_id}")
            else:
                print(f"Skipping {snapshot_id}: {str(e)}")


if __name__ == "__main__":
    main()
