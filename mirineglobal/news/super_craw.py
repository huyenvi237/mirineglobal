import requests
from bs4 import BeautifulSoup as bs
from random import randint
from time import sleep
import csv
import pandas as pd

URL = 'https://news.yahoo.co.jp/topics/top-picks?page='

titles=[]
links=[]
tit=[]
li=[]
for page in range(1, 10):
    req = requests.get(URL + str(page))
    soup = bs(req.text, 'html.parser')

    tit = soup.find_all('div', {'class': 'newsFeed_item_title'})
    li = soup.find_all('a', {'class': 'newsFeed_item_link'})

    sleep(randint(4, 10))

for l in li:
    links.append(l.attrs["href"])
for t in tit:
    titles.append(t.text)

with open("new2.csv", "w", encoding='UTF-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Titles","Links"])
    writer.writerows(zip(titles, links))

def getMain_page(li):
    list_link=[]
    for links in li:
        news_page = requests.get(links)
        soup1 = bs(news_page.content, "html.parser")
        page_info = soup1.find_all("div", {"class": "sc-muxYx kNLljN"})
        for link in page_info:
            list_link.append(link.find('a').attrs["href"])
        sleep(randint(4, 10))
    return list_link

craw_source=getMain_page(links)
#print(craw_source)
for c in craw_source:
    if "articles" not in c:
        craw_source.remove(c)

content=[]

for link in craw_source:
    main_news = requests.get(link)
    soup2 = bs(main_news.content, "html.parser")
    body = soup2.find_all("div", {"class": "sc-ipZHIp ieFwHi"})
    y = body[0]
    content.append(y.findChild("p", {"class": "sc-giadOv loZBCE yjSlinkDirectlink highLightSearchTarget"}).text)
    sleep(randint(4, 10))
dt = pd.read_csv('new2.csv')
dt['Contents'] = content
dt.to_csv('file.csv')
