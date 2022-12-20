import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

url = "https://www.targetsite.com"
response = requests.get(url)
html_contents = response.content
soup = BeautifulSoup(html_contents,"html.parser")
name =soup.find_all("a",{"class":"prd-name"})
price = soup.find_all("div",{"class":"prd-price"})
value1 =soup.find_all("a",{"class":"who text-overflow"})
value2 =soup.find_all("a",{"class":"prd-publisher"})
liste = list()
for i in range(len(price)):
    name[i] = (name[i].text).strip("\n").strip()
    price[i] = (price[i].text).strip("\n").replace("\nTL"," TL").strip()
    value1[i] = (value1[i].text).strip("\n").strip()
    value2[i] = (value2[i].text).strip()
    liste.append([name[i],price[i],value1[i],value2[i]])


df = pd.DataFrame(liste,columns = ["Name","Price","Value 1","value2"])
with open('output.html', 'w') as f:
  f.write(str(df) )
print(df)




