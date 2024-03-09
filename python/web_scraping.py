# import section
import requests
import pandas as p
import bs4 as BeautifulSoup 


# print response
response = requests.get("https://www.flipkart.com/search?q=phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
print(response)

#print soup
soup = BeautifulSoup(response.content,"html.parser")
print(soup)