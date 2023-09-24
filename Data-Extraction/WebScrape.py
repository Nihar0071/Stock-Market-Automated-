import csv
import time
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

BASE_URL = "https://www.investing.com/indices/investing.com-"

def get_stock_data(stock_name):
    stock_url = BASE_URL + stock_name.replace(' ', '-').lower()

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU for Windows compatibility
    chrome_options.add_argument("--window-size=1920x1080")  # Set default window size

    # Initialize the browser
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(stock_url)

    # Wait for the page to load and find the price element
    price_element = driver.find_element(By.CSS_SELECTOR, 'div[class*="text-5xl"]')
    price = price_element.text

    # Print the stock name and its price
    print(f"{stock_name}: {price}")

    # Close the browser
    driver.quit()

    return price

def store_in_csv(stock_name, price):
    filename = f"{stock_name}.csv"
    with open(filename, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([time.strftime('%Y-%m-%d %H:%M:%S'), price])


def main():
    num_stocks = int(input("Enter the number of stocks you want to store prices of: "))
    stock_names = [input(f"Enter the stock name as listed in stock exchange for stock {i+1}: ") for i in range(num_stocks)]

    # Create CSV files with headers
    for stock_name in stock_names:
        with open(f"{stock_name}.csv", 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['Timestamp', 'Price'])

    while True:
        for stock_name in stock_names:
            price = get_stock_data(stock_name)
            store_in_csv(stock_name, price)

        time.sleep(6)

if __name__ == "__main__":
    main()
