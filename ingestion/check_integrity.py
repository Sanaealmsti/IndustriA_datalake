import boto3
import hashlib

client = boto3.client("s3",
    endpoint_url="http://localhost:9000",
    aws_access_key_id="minioadmin",
    aws_secret_access_key="minioadmin")

fichiers = {"LineA_Stable_10K.csv": "lineA",
    "LineB_Flux.csv": "lineB",
    "LineC_Turbulent.csv": "lineC",
    "LineD_SpikeControl.csv": "lineD",
    "LineE_SmoothRun.csv": "lineE"}

for fichier, ligne in fichiers.items():
    md5 = hashlib.md5(open(f"data/{fichier}", "rb").read()).hexdigest()
    etag = client.head_object(Bucket="raw", Key=f"production_lines/{ligne}/year=2025/month=05/{fichier}")["ETag"].strip('"')
    print(fichier, md5 == etag)