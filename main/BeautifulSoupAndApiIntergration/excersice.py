# In financial market analysis, retrieving stock price data is essential for making informed investment decisions. There are two common approaches for obtaining such data: web scraping and API integration. Web scraping involves fetching and processing HTML content from financial websites, while APIs provide structured data access from official stock market services. Python offers libraries such as requests, and BeautifulSoup to streamline these tasks.
# Assume you are developing a financial data retrieval system that collects real-time stock market data from an online finance portal. The stock market platform offers data through two methods:
# 1. A web page containing stock details within its HTML structure.
# 2. A REST API that returns stock market data in JSON format.

# (a) Web Scraping
# The finance website displays stock information using the following HTML format: 
        # < div class="market-data">
        #   <h2 class="company-name"> Tesla Inc. </h2>
        #   <p class="ticker"> TSLA</p>
        #   ‹span class="current-price">$695-50</span>
        # </div>
# Write a Python program using requests and BeautifulSoup. to:
# • retrive the web page content from htts://example. com/market
# • Extract the company name, stock ticker. and price.

# (b) Error Handling in Web Scraping
# Since web scraping is susceptible to network failures, website updates, or anti-scraping measures, enhance your script by:
# • Handling HTTP request failures (e.g., checking for unsuccessful responses).
# • Implementing a check to confirm that the expected HTML. elements are present before extracting data.
# 
# (e) API Integration       
# The finacial platform also provides an API at https://api.example.com/market, returning stock data in the following JSON format:
#       [
#            ("company": "Apple Inc.", "ticker": "AAPL", "price": 150.25), ("company": "Microsoft Corp.", "ticker": "MSFT", "price": 299.80}
#       ]
#
# Write a Python script that:
# 1. Sends a GET request to retrieve stock data from the API.
# 2. Parses and processes the JSON response.
# 3. Displays the retrieved stock details in a well-structured output.  

from bs4 import BeautifulSoup as bs
import requests as req

base_url = "https://example.com/market."

# answer (a) and (b)
def extract_data():

    try:
        response = req.get(base_url)
        
        if response.status_code == 200:
            soup = bs(response.text,"html.parser")

            company_name = soup.find("h2", class_ ="company-name")
            ticker = soup.find("p", class_ ="ticker")
            current_price = soup.find("span", class_ ="current-price")
            
            if company_name and ticker and current_price:
                print(f"Company Name : {company_name.text.strip()}")
                print(f"Ticker : {ticker.text.strip()}")
                print(f"Current Price : {current_price.text.strip()}")
            else:
                print("Expected element not found in html structure!")
        else:
            print("Failed to retrival data. status code :", response.status_code)
    except req.exceptions.RequestException as e:
        print(e)

extract_data()

        
# answer (c)

base_url_api = "https://api.example.com/market"

def stock_manage():
    
    try:
        response = req.get(base_url)
        response.raise_for_status() # Riase an error for http failures
    
        stock_data = response.json()
        
        for data in stock_data:
            print(f"company name : {data["company"]}")
            print(f"Ticker : {data["ticker"]}")
            print(f"Price : {data["price"]:2f}")
            print("-" * 30)
            
    except req.exceptions.RequestException as e:
        print(e)
        
stock_manage()