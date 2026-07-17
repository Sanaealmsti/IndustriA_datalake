import boto3
import os

client = boto3.client("s3",
    endpoint_url="http://localhost:9000",
    aws_access_key_id="minioadmin",
    aws_secret_access_key="minioadmin")

DATA_DIR = "data"

lignes = {"LineA_Stable_10K.csv": "lineA",
    "LineB_Flux.csv": "lineB",
    "LineC_Turbulent.csv": "lineC",
    "LineD_SpikeControl.csv": "lineD",
    "LineE_SmoothRun.csv": "lineE"}

for fichier, ligne in lignes.items():
    chemin_local = os.path.join(DATA_DIR, fichier)
    cle = f"production_lines/{ligne}/year=2025/month=05/{fichier}"
    client.upload_file(chemin_local, "raw", cle)
    print(f"uploade : {cle}")