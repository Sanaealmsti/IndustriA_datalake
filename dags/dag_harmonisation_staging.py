from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import boto3
import pandas as pd
import io

def harmoniser_ligne(fichier, ligne):
    client = boto3.client("s3", endpoint_url="http://minio:9000", aws_access_key_id="minioadmin", aws_secret_access_key="minioadmin")

    objet = client.get_object(Bucket="raw", Key=f"production_lines/{ligne}/year=2025/month=05/{fichier}")
    donnees = pd.read_csv(io.BytesIO(objet["Body"].read()))

    donnees.columns = [col.lower() for col in donnees.columns]

    if "elapsed_time" not in donnees.columns:
        donnees["elapsed_time"] = None

    contenu = io.StringIO()
    donnees.to_csv(contenu, index=False)

    client.put_object(Bucket="staging", Key=f"production_lines/{ligne}/year=2025/month=05/{fichier}", Body=contenu.getvalue())

with DAG("harmonisation_staging", start_date=datetime(2025, 1, 1), schedule=None) as dag:
    lineA = PythonOperator(task_id="lineA", python_callable=harmoniser_ligne, op_args=["LineA_Stable_10K.csv", "lineA"])
    lineB = PythonOperator(task_id="lineB", python_callable=harmoniser_ligne, op_args=["LineB_Flux.csv", "lineB"])
    lineC = PythonOperator(task_id="lineC", python_callable=harmoniser_ligne, op_args=["LineC_Turbulent.csv", "lineC"])
    lineD = PythonOperator(task_id="lineD", python_callable=harmoniser_ligne, op_args=["LineD_SpikeControl.csv", "lineD"])
    lineE = PythonOperator(task_id="lineE", python_callable=harmoniser_ligne, op_args=["LineE_SmoothRun.csv", "lineE"])

    lineA >> lineB >> lineC >> lineD >> lineE