import requests
from bs4 import BeautifulSoup

url = "https://www.trendyol.com/sr?wb=101470&lc=103108&os=1"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find("div",{"class":"prdct-cntnr-wrppr"}).find_all("div",limit=5)
list = soup.find_all("div",{"class":"p-card-chldrn-cntnr card-border"},limit=5)
count = 0

for div in list:
    title = div.find("a").text
    
    count +=1
    
    print(f"{count}- PC: {title}")
