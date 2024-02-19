import os
import requests
from bs4 import BeautifulSoup



response = requests.get('https://www.mrftyres.com/products/passenger-cars')

soup = BeautifulSoup(response.text, 'html.parser')

div = soup.find_all('div',attrs={'class':'card-tyres-wrapper'})

print(len(div))
print(div[1])

