from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import boto3

def upload_lineA():
    client = boto3.client("s3", endpoint_url="http://minio:9000", aws_access_key_id="minioadmin", aws_secret_access_key="minioadmin")
    client.upload_file("/opt/airflow/data/LineA_Stable_10K.csv", "raw", "production_lines/lineA/year=2025/month=05/LineA_Stable_10K.csv")

def upload_lineB():
    client = boto3.client("s3", endpoint_url="http://minio:9000", aws_access_key_id="minioadmin", aws_secret_access_key="minioadmin")
    client.upload_file("/opt/airflow/data/LineB_Flux.csv", "raw", "production_lines/lineB/year=2025/month=05/LineB_Flux.csv")

def upload_lineC():
    client = boto3.client("s3", endpoint_url="http://minio:9000", aws_access_key_id="minioadmin", aws_secret_access_key="minioadmin")
    client.upload_file("/opt/airflow/data/LineC_Turbulent.csv", "raw", "production_lines/lineC/year=2025/month=05/LineC_Turbulent.csv")

def upload_lineD():
    client = boto3.client("s3", endpoint_url="http://minio:9000", aws_access_key_id="minioadmin", aws_secret_access_key="minioadmin")
    client.upload_file("/opt/airflow/data/LineD_SpikeControl.csv", "raw", "production_lines/lineD/year=2025/month=05/LineD_SpikeControl.csv")

def upload_lineE():
    client = boto3.client("s3", endpoint_url="http://minio:9000", aws_access_key_id="minioadmin", aws_secret_access_key="minioadmin")
    client.upload_file("/opt/airflow/data/LineE_SmoothRun.csv", "raw", "production_lines/lineE/year=2025/month=05/LineE_SmoothRun.csv")

with DAG("ingestion_raw", start_date=datetime(2025, 1, 1), schedule=None) as dag:
    upload_lineA = PythonOperator(task_id="upload_lineA", python_callable=upload_lineA)
    upload_lineB = PythonOperator(task_id="upload_lineB", python_callable=upload_lineB)
    upload_lineC = PythonOperator(task_id="upload_lineC", python_callable=upload_lineC)
    upload_lineD = PythonOperator(task_id="upload_lineD", python_callable=upload_lineD)
    upload_lineE = PythonOperator(task_id="upload_lineE", python_callable=upload_lineE)

    upload_lineA >> upload_lineB >> upload_lineC >> upload_lineD >> upload_lineE