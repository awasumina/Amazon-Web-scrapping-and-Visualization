from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello():
    print("Hello Airflow")

with DAG('test_dag', start_date=datetime(2025, 5, 1), schedule_interval='@daily', catchup=False) as dag:
    task1 = PythonOperator(
        task_id='hello_task',
        python_callable=hello
    )
