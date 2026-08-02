import boto3, logging
import boto3.session
from pathlib import Path

logging.basicConfig(level=logging.INFO)

class S3_lifecycleManager:
    def __init__(self, profile_name, bucket_name):
        session = boto3.Session(profile_name=profile_name)
        s3_client = session.client('s3')
        self.profile_name = profile_name
        self.bucket_name = bucket_name
        self.session = session
        self.s3 = s3_client

    def apply_glacier_transition_rule(self):
        response = self.s3.put_bucket_lifecycle_configuration(
        Bucket=self.bucket_name,
        LifecycleConfiguration={
            'Rules': [
                {
                    'Filter': {
                            'Prefix': '',
                        },
                        'ID': 'TestOnly',
                        'Status': 'Enabled',
                        'Transitions': [
                            {
                                'Days': 30,
                                'StorageClass': 'GLACIER',
                            },
                        ],
                    },
                ],
            },
        )
        logging.info(f"Lifecycle rule applied succesufly!")

if __name__ == '__main__':
    lifecycle_rule = S3_lifecycleManager(
            profile_name='s3-backup-bot',
            bucket_name='benlamir-logs-backup-2026')
    lifecycle_rule.apply_glacier_transition_rule()
