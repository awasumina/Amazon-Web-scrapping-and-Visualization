-- Run in psql or pgAdmin

CREATE TABLE laptop_dim_products (
    product_id SERIAL PRIMARY KEY,
    title TEXT,
    price FLOAT
);

CREATE TABLE laptop_fact_reviews (
    review_id SERIAL PRIMARY KEY,
    product_id INT REFERENCES laptop_dim_products(product_id),
    rating FLOAT
);

CREATE TABLE smartwatch_dim_products (
    product_id SERIAL PRIMARY KEY,
    title TEXT,
    price FLOAT
);

CREATE TABLE smartwatch_fact_reviews (
    review_id SERIAL PRIMARY KEY,
    product_id INT REFERENCES smartwatch_dim_products(product_id),
    rating FLOAT
);

CREATE TABLE smartphone_dim_products (
    product_id SERIAL PRIMARY KEY,
    title TEXT,
    price FLOAT
);

CREATE TABLE smartphone_fact_reviews (
    review_id SERIAL PRIMARY KEY,
    product_id INT REFERENCES smartphone_dim_products(product_id),
    rating FLOAT
);

CREATE TABLE desktop_dim_products (
    product_id SERIAL PRIMARY KEY,
    title TEXT,
    price FLOAT
);

CREATE TABLE desktop_fact_reviews (
    review_id SERIAL PRIMARY KEY,
    product_id INT REFERENCES desktop_dim_products(product_id),
    rating FLOAT
);



