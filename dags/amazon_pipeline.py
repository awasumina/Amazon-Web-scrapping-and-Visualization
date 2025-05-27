from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime
from src.scrappy import scrape_amazon_products
from src.transform import clean_transform_data
from src.postgresLoader import load_to_postgres

with DAG("amazon_pipeline", start_date=datetime(2025, 5, 22), schedule_interval="@daily", catchup=False) as dag:
    t1 = PythonOperator(task_id="scrape", python_callable=scrape_amazon_products)
    t2 = PythonOperator(task_id="transform", python_callable=clean_transform_data)
    t3 = PythonOperator(task_id="load", python_callable=load_to_postgres)

    t1 >> t2 >> t3
