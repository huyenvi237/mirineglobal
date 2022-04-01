import requests
from bs4 import BeautifulSoup as bs
from random import randint
from time import sleep
import csv

### 必ずsleep timeをセットする。ページからblock可能性が高いです。
### random ライブラリを使用すると時間が調整しやすい。
URL = 'https://news.yahoo.co.jp/topics/top-picks?page='

#使用リスク
titles=[]   #title list
links=[]    #link list
index=[]    #削除したelementsのインデックスを保存リスク
content=[]  #content list

for page in range(1, 2):
    req = requests.get(URL + str(page))
    soup = bs(req.text, 'html.parser')

    tit=soup.find_all('div', {'class': 'newsFeed_item_title'})
    li=soup.find_all('a', {'class': 'newsFeed_item_link'})

    for l in li:
        links.append(l.attrs["href"])
    for t in tit:
        titles.append(t.text)
    sleep(randint(4, 10))

#ページによって関数を使用するかどうか決める
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

#アクセスできるリングを調整する
for c in craw_source:
    if "articles" not in c:
        if len(index) == 0:
            index.append(craw_source.index(c))
            craw_source.remove(c)
        else:
            index.append((craw_source.index(c)+len(index)))
            craw_source.remove(c)

#リスクの保存ができるかどうか確認する
print(len(index))      
print(len(titles))

#Titles listを調整する
for i in sorted(index, reverse=True):
    del  titles[i]

#リスクの保存ができるかどうか確認する
print(len(titles))
print(len(craw_source))

#Contentsを取得する
for link in craw_source:
    main_news = requests.get(link)
    soup2 = bs(main_news.content, "html.parser")
    body = soup2.find_all("div", {"class": "sc-ipZHIp ieFwHi"})
    y = body[0]
    content.append(y.findChild("p", {"class": "sc-giadOv loZBCE yjSlinkDirectlink highLightSearchTarget"}).text)
    sleep(randint(4, 10))

#CSVファイルを作成
with open("file.csv", "w", encoding='UTF-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Titles","Links","Contents"])
    writer.writerows(zip(titles, links, content))

