import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import ctypes



url = input("Enter your product URL: ")
amount_of_time = input("For how long do you want to check the price (in minutes): ")
aimed_price = input("The price I'm looking for: ")


headers = {'User Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}
url_source = requests.get(url.strip(), headers=headers)
soup = BeautifulSoup(url_source.content, "lxml")



# NAME OF THE PRODUCT
name = soup.find(class_ ='page-title').text


# PRICE OF THE PRODUCT
price = soup.find(class_= 'product-new-price').text.strip()

# .99 or .00 from the price
for sup_price in soup.find_all('div', class_ = 'product-highlight product-page-pricing'):
    sup_extract =  sup_price.find('p', class_ = 'product-new-price')
    sup_extract1 = sup_extract.find('sup')
    sup = sup_extract1.text


full_price = (float(price[:-6].replace('.', '')) + (float(sup) / 100))


# TIME SPAN
time_to_end = time.time() + 60 * float(amount_of_time)

while time.time() < time_to_end:
    print("Name:  ", name.strip())
    print('Price: ', full_price)
    print('Time:  ',datetime.now().replace(microsecond=0))
    print('-'*40)
    time.sleep(1)  # Updates once per second
    if full_price <= float(aimed_price):
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, 'Hello', 'Window title', 0)
        break



