import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.yogendra-swaroop.tech")

soup = BeautifulSoup(response.content, "html.parser")
title = (soup.select('title'))
print(title[0].getText())
para = soup.select('p')
print(para[0].getText())
id = soup.select("#author")
print(id)
img = soup.find('img')
print(img['alt'])
href = soup.findAll('a')
for i in href:
    print()
