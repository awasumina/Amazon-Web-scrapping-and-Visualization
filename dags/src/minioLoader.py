from minio import Minio
from minio.error import S3Error

client = Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

bucket_name = "amazon-data"
if not client.bucket_exists(bucket_name):
    client.make_bucket(bucket_name)

client.fput_object(bucket_name, "products/smartphone.json", "data/products_smartphone.json")
client.fput_object(bucket_name, "products/desktop.json", "data/products_desktop.json")
client.fput_object(bucket_name, "products/laptop.json", "data/products_laptop.json")
client.fput_object(bucket_name, "products/smartwatch.json", "data/products_smartwatch.json")
