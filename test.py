import os
import requests
from bs4 import BeautifulSoup
from logs import *

response = requests.get('https://www.mrftyres.com/products/passenger-cars')
# response = requests.get('https://www.ceat.com/car-tyres/car-product-listing/product-details/235-70r16-crossdrive-at-tl-106s.html')
print(response)

soup = BeautifulSoup(response.content, 'html.parser')

div_1 = soup.find_all('div',class_ = 'card-tyres')

print("sahil is fine")

a= [45,18,100,17,9]
for i in a:
    print(i)
    
print(len(div_1))

print("Be Happy Code is working")
