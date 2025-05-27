import os
import pandas as pd
from sqlalchemy import create_engine

def load_to_postgres():
    engine = create_engine("postgresql://postgres:root@localhost:5432/AmazonScrapeVisualization")

    base_path = "data/transformedData"

    if not os.path.exists(base_path):
        print("Transformed data folder not found.")
        return

    for category in os.listdir(base_path):
        category_path = os.path.join(base_path, category)
        if not os.path.isdir(category_path):
            continue

        print(f"Loading data for category: {category}")

        # Load dim_products
        dim_path = os.path.join(category_path, "dim_products.csv")
        if os.path.exists(dim_path):
            try:
                df = pd.read_csv(dim_path)
                df.to_sql(f"{category}_dim_products", engine, if_exists="append", index=False)
                print(f"Loaded: {dim_path}")
            except Exception as e:
                print(f"Error loading {dim_path}: {e}")

        # Load fact_reviews
        fact_path = os.path.join(category_path, "fact_reviews.csv")
        if os.path.exists(fact_path):
            try:
                df = pd.read_csv(fact_path)
                df.to_sql(f"{category}_fact_reviews", engine, if_exists="append", index=False)
                print(f"Loaded: {fact_path}")
            except Exception as e:
                print(f"Error loading {fact_path}: {e}")



# import pandas as pd
# from sqlalchemy import create_engine


# engine = create_engine("postgresql://postgres:root@localhost:5432/AmazonScrapeVisualization")


# def read_csv_to_postgres(file_path, table_name):
#     df = pd.read_csv(file_path)
#     df[["title","price"]].to_sql(table_name, engine, if_exists="append", index=False)
#     # print(f"Data from {file_path} has been loaded into {table_name} table in PostgreSQL.")
#     # print(df.head()) 
#     print("success")


# read_csv_to_postgres("data/transformedData/desktop/dim_products.csv", "desktop_dim_products")
# read_csv_to_postgres("data/transformedData/laptop/dim_products.csv", "laptop_dim_products")
# read_csv_to_postgres("data/transformedData/smartwatch/dim_products.csv", "smartwatch_dim_products")
# read_csv_to_postgres("data/transformedData/smartphone/dim_products.csv", "smartphone_dim_products")

# def read_fact_csv_to_postgres(file_path, table_name):
#     df = pd.read_csv(file_path)
#     df[["product_id","rating"]].to_sql(table_name, engine, if_exists="append", index=False)
#     print("success")

# read_fact_csv_to_postgres("data/transformedData/smartwatch/fact_reviews.csv", "smartwatch_fact_reviews")
# read_fact_csv_to_postgres("data/transformedData/smartphone/fact_reviews.csv", "smartphone_fact_reviews")
# read_fact_csv_to_postgres("data/transformedData/laptop/fact_reviews.csv", "laptop_fact_reviews")
# read_fact_csv_to_postgres("data/transformedData/desktop/fact_reviews.csv", "desktop_fact_reviews")
