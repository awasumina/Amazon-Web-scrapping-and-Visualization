#generate a test_py dag file that will generate hello world
from airflow import DAG 
from airflow.operators.python import PythonOperator
from datetime import datetime
import logging
from airflow.utils.dates import days_ago
def hello_world():
    logging.info("Hello, World!")
with DAG(
    "hello_world_dag",
    default_args={
        "owner": "airflow",
        "depends_on_past": False,
        "start_date": days_ago(1),
        "retries": 1,
    },
    schedule_interval="@daily",
    catchup=False,
) as dag:
    hello_task = PythonOperator(
        task_id="hello_world_task",
        python_callable=hello_world,
    )

    hello_task
# Set the task dependencies
hello_task
# This DAG will run the hello_world function daily and log "Hello, World!" in the Airflow logs.
