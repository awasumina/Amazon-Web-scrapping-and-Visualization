# import time
# import json
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# def get_driver():
#     # Set up Chrome options
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument("--headless")   #  it operates without a GUI i.e where displaying a browser window isn't necessary
#     chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
#     driver = webdriver.Chrome(options=chrome_options)
#     return driver

# def scrape_amazon_product(query, max_pages = 2):
#     base_url = "https://www.amazon.com"
#     search_url = f"{base_url}/s?k={query.replace(' ','+')}"

#     driver = get_driver()
#     all_products = []

#     for page in range(1, max_pages + 1):
#         driver.get(f"{search_url}&page={page}")
#         time.sleep(2)  # for waiting the page to load
#         soup = BeautifulSoup(driver.page_source, "html.parser")
#         products = soup.select('div[data-component-type="s-search-result"]')

#         for iteam in products:
#             try:
#                 if not iteam.h2 or not iteam.h2.a:
#                     continue  # skip if h2 or link is missing
#                 title = iteam.find("h2").text.strip() if iteam.find("h2") else "No Title"

#                 price = iteam.select_one('.a-price .a-offscreen').text.strip()

#                 rating = iteam.select_one('.a-icon-alt').text.strip()
                
#                 link = base_url + iteam.h2.a['href']

#                 all_products.append({
#                     "title": title,
#                     "price": price.text if price else "N/A",
#                     "rating": rating.text if rating else "N/A",
#                     "url": link
#                 })
#             except AttributeError:
#                 continue
#     driver.quit()
#     return all_products

# if __name__ == "__main__":
#     query = "laptop"
#     # max_pages = 2
#     data = scrape_amazon_product(query)
#     import os
#     os.makedirs("data", exist_ok=True)
#     with open("data/products_laptop.json", "w") as f:
#         json.dump(data, f, indent=4)



import time
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

def get_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def scrape_amazon_product(query, max_pages=2):
    base_url = "https://www.amazon.com"
    search_url = f"{base_url}/s?k={query.replace(' ', '+')}"

    driver = get_driver()
    all_products = []

    for page in range(1, max_pages + 1):
        print(f"Loading page {page}...")
        driver.get(f"{search_url}&page={page}")
        time.sleep(2)  # wait for page to load

        soup = BeautifulSoup(driver.page_source, "html.parser")
        products = soup.select('div[data-component-type="s-search-result"]')
        print(f"Found {len(products)} products on page {page}")

        for idx, item in enumerate(products, 1):
            try:
                title = item.h2.text.strip() if item.h2 else "N/A"
                
                price_el = item.select_one('.a-color-base .a-price .a-offscreen')
                price = price_el.text.strip() if price_el else "N/A"

                rating_el = item.select_one('.a-icon-alt')
                rating = rating_el.text.strip() if rating_el else "N/A"

                # link = base_url + item.h2.a['href'] if item.h2 and item.h2.a else "N/A"

                # Print product info as we scrape it
                print(f"[Product {idx}] Title: {title}, Price: {price}, Rating: {rating}")
                      
                    #   , Link: {link}")

                all_products.append({
                    "title": title,
                    "price": price,
                    "rating": rating,
                    # "url": link
                })

            except Exception as e:
                print(f"Error scraping product {idx}: {e}")

    driver.quit()
    print(f"Total products scraped: {len(all_products)}")
    return all_products

if __name__ == "__main__":
    query = "desktop"
    data = scrape_amazon_product(query)
    os.makedirs("data", exist_ok=True)
    with open("data/products_desktop.json", "w") as f:
        json.dump(data, f, indent=4)