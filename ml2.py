# import random
# import time
# print("Collecting temperature data from the virtual sensor...")

# temps = []
# for i in range(5):
#     t = 20 + random.random()*5
#     temps.append(t)
#     print(f"Reading {i+1}: Sensor says it's {t:.2f}°C")
#     time.sleep(1)

# print("\nAll readings:")
# print("Final temperature dataset:", temps)


# import requests

# print("Contacting the CoinDesk server: ")

# response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

# if response.status_code == 200:
#     data = response.json()
#     print("Data received")

#     print("Time updated:", data["time"]["updated"])
#     print("Bitcoin prices now:")

#     for currency, info in data["bpi"].items():
#         print(f" - {currency}: {info['rate']} {info['symbol']}")


import requests
from bs4 import BeautifulSoup

print("🔍 Visiting the online shop to see what's available...")

url = "https://example.com/products"
page = requests.get(url)

if page.status_code == 200:
    print("Successfully connected")
    soup = BeautifulSoup(page.text, "html.parser")

    products = soup.find_all("h2", class_="product-title")

    if len(products) > 0:
        print("🛒 Here are the products I found:\n")
        for product in products:
            print(f"• {product.text}")
    else:
        print("I looked around but couldn't find product titles.")
else:
    print("Failed to reach the site")
