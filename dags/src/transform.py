import pandas as pd
from textblob import TextBlob
import os
import glob

def clean_transform_data():
    input_folder = "data"
    output_folder = "data/transformedData"

    os.makedirs(output_folder, exist_ok=True)

    json_files = glob.glob(os.path.join(input_folder, "products_*.json"))

    for file_path in json_files:
        try:
            query = os.path.basename(file_path).replace("products_", "").replace(".json", "")
            print(f"Processing: {query}")

            df = pd.read_json(file_path)

            df["rating"] = df["rating"].str.extract(r"([0-9.]+)").astype(float)

            df["sentiment_score"] = df["title"].apply(
                lambda text: TextBlob(text).sentiment.polarity if text else None
            )

            df["product_id"] = range(1, len(df) + 1)

            category_folder = os.path.join(output_folder, query)
            os.makedirs(category_folder, exist_ok=True)

            dim_products = df[["product_id", "title", "price"]]
            dim_products.to_csv(os.path.join(category_folder, "dim_products.csv"), index=False)

            fact_reviews = df[["product_id", "rating"]].copy()
            fact_reviews["review_id"] = range(1, len(fact_reviews) + 1)
            fact_reviews = fact_reviews[["review_id", "product_id", "rating"]]
            fact_reviews.to_csv(os.path.join(category_folder, "fact_reviews.csv"), index=False)

        except Exception as e:
            print(f"Failed to process {file_path}: {e}")




# import pandas as pd
# from textblob import TextBlob

# # df = pd.read_json("data/products_smartwatch.json")
# # df = pd.read_json("data/products_smartphone.json")
# # df = pd.read_json("data/products_laptop.json")
# df = pd.read_json("data/products_desktop.json")



# df["rating"] = df["rating"].str.extract(r"([0-9.]+)").astype(float) # Extract float rating from text like "4.4 out of 5 stars"

# df["sentiment_score"] = df["title"].apply(lambda text: TextBlob(text).sentiment.polarity if text else None)

# df["product_id"] = range(1, len(df) + 1)        # Assign product_id

# # Create dim_products table data
# dim_products = df[["product_id", "title", "price"]]
# # dim_products.to_csv("data/transformedData/smartwatch/dim_products.csv", index=False)
# # dim_products.to_csv("data/transformedData/smartphone/dim_products.csv", index=False)
# # dim_products.to_csv("data/transformedData/laptop/dim_products.csv", index=False)
# dim_products.to_csv("data/transformedData/desktop/dim_products.csv", index=False)

# # Create fact_reviews table data (this time using actual ratings)
# fact_reviews = df[["product_id", "rating"]].copy()
# fact_reviews["review_id"] = range(1, len(fact_reviews) + 1)
# fact_reviews = fact_reviews[["review_id", "product_id", "rating"]]
# # fact_reviews.to_csv("data/transformedData/smartwatch/fact_reviews.csv", index=False)
# # fact_reviews.to_csv("data/transformedData/smartphone/fact_reviews.csv", index=False)
# # fact_reviews.to_csv("data/transformedData/laptop/fact_reviews.csv", index=False)
# fact_reviews.to_csv("data/transformedData/desktop/fact_reviews.csv", index=False)
