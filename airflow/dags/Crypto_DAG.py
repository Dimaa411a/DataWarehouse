from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

sys.path.append("/home/dimaa/PycharmProjects/DataWarehouse")

from etl.crypto_pipeline import crypto_pipeline



with DAG(
    dag_id="crypto_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule="@hourly",
    catchup=False
) as dag:

    run_pipeline = PythonOperator(
        task_id="run_etl",
        python_callable=crypto_pipeline
    )
