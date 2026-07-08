import boto3
import json

client = boto3.client(
    "s3",
    endpoint_url="http://localhost:9000",
    aws_access_key_id="minioadmin",
    aws_secret_access_key="minioadmin"
)

def creer_policy(bucket, actions):
    return json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": "*",
            "Action": actions,
            "Resource": [f"arn:aws:s3:::{bucket}/*"]
        }]
    })

for bucket in ["raw", "staging"]:
    client.put_bucket_policy(Bucket=bucket, Policy=creer_policy(bucket, ["s3:GetObject", "s3:PutObject"]))

for bucket in ["curated", "archive"]:
    client.put_bucket_policy(Bucket=bucket, Policy=creer_policy(bucket, ["s3:GetObject"]))