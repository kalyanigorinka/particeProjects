#import section
import requests
import pandas as pd
from bs4 import BeautifulSoup
response=requests.get("https://www.flipkart.com/search?q=teddy+bear&sid=tng%2Cclb%2Cxv3&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=teddy+bear%7CTeddy+Bears&requestId=fe27f90c-a412-440a-a266-c4c8f3f412d2&as-searchtext=teddy")
#print(response)

soup = BeautifulSoup(response.content,'html.parser')
#print(soup)

'''......names....'''

names = soup.find_all('a',class_="s1Q9rs")
#print(names)
name = []
for i in names[0:10]:
    d=i.get_text()
    name.append(d)
#print(name)

'''......prices..........'''


prices = soup.find_all('div',class_="_30jeq3")
#print(prices)
price = []
for i in prices[0:10]:
    d=i.get_text()
    price.append(d)
#print(price)

'''......rates........'''

rates= soup.find_all('div',class_="_3LWZlK")
#print(rates)
rate= []
for i in rates[0:10]:
    d= i.get_text()
    rate.append(float(d))
#print(rate)


'''......images........'''

images = soup.find_all('img',class_="_396cs4")
#print(images)
image = []
for i in images[0:10]:
    d=i['src']
    image.append(d)
#print(image)

'''...........links..........'''

links= soup.find_all('a',class_="s1Q9rs")
#print(links)
link= []
for i in links[0:10]:
    d="https://www.flipkart.com"+i["href"]
    link.append(d)
#print(link)

df=pd.DataFrame()

df["Teddy_Names"]=name

df["Teddy_Prices"]=price

df["Teddy_Ratings"]=rate

df["Teddy_Images"]=image

df["Teddy_Links"]=link

print(df)

df.to_csv('teddy.csv')
