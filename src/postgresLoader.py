import pandas as pd
from sqlalchemy import create_engine


engine = create_engine("postgresql://postgres:root@localhost:5432/AmazonScrapeVisualization")


def read_csv_to_postgres(file_path, table_name):
    df = pd.read_csv(file_path)
    df[["title","price"]].to_sql(table_name, engine, if_exists="append", index=False)
    # print(f"Data from {file_path} has been loaded into {table_name} table in PostgreSQL.")
    # print(df.head()) 
    print("success")


read_csv_to_postgres("data/transformedData/desktop/dim_products.csv", "desktop_dim_products")
read_csv_to_postgres("data/transformedData/laptop/dim_products.csv", "laptop_dim_products")
read_csv_to_postgres("data/transformedData/smartwatch/dim_products.csv", "smartwatch_dim_products")
read_csv_to_postgres("data/transformedData/smartphone/dim_products.csv", "smartphone_dim_products")

def read_fact_csv_to_postgres(file_path, table_name):
    df = pd.read_csv(file_path)
    df[["product_id","rating"]].to_sql(table_name, engine, if_exists="append", index=False)
    print("success")

read_fact_csv_to_postgres("data/transformedData/smartwatch/fact_reviews.csv", "smartwatch_fact_reviews")
read_fact_csv_to_postgres("data/transformedData/smartphone/fact_reviews.csv", "smartphone_fact_reviews")
read_fact_csv_to_postgres("data/transformedData/laptop/fact_reviews.csv", "laptop_fact_reviews")
read_fact_csv_to_postgres("data/transformedData/desktop/fact_reviews.csv", "desktop_fact_reviews")
