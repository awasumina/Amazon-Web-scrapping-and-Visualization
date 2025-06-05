# Amazon Web Scraping and Visualization

This project builds an end-to-end data engineering pipeline to extract, transform, and visualize e-commerce data from Amazon. The primary goal is to scrape product details and customer reviews, store the data in a structured data warehouse, apply data modeling and transformation techniques, and create interactive visualizations. This includes skills in web scraping, data processing, data warehousing, and workflow automation using industry-relevant tools and technologies.

---

## Project Steps

### Step 1: Web Scraping
- Scrape product information for categories such as mobile phones, laptops, desktop and smartwatches.
- Used **Scrapy** and **Selenium** 
- Stored raw extracted data in **MinIO** (Data Lake) as JSON.

### Step 2: Data Modeling & Storage
- Designed a **Star Schema**  for structured data storage with bronze, silver, and gold layers.
- Defined tables for products, reviews, and related attributes.
- Implement the schema using **PostgreSQL** to create a Data Warehouse for efficient querying.

### Step 3: Data Transformation
- Clean and preprocess the raw data using **Pandas** or **Apache Spark**.
- Handle missing values, normalize text, and convert categorical data as necessary.
- Load the cleaned and transformed data into the PostgreSQL Data Warehouse.

### Step 4: Data Visualization
- Created insightful dashboards using **Apache Superset**.

### Step 5: Automation with Airflow
- Automate the entire pipeline with **Apache Airflow**:

---

## Technologies & Tools

| Category             | Tools & Technologies                           |
|----------------------|-----------------------------------------------|
| Web Scraping         | Scrapy, BeautifulSoup, Selenium                |
| Data Storage         | MinIO (Data Lake), PostgreSQL (Data Warehouse)|
| Data Processing      | Pandas, Apache Spark                           |
| Visualization        | Apache Superset                               |
| Workflow Automation  | Apache Airflow                                |

---
