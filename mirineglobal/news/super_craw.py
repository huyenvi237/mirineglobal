import requests
from bs4 import BeautifulSoup as bs
from random import randint
from time import sleep
import logging
from datetime import datetime
from elasticsearch import Elasticsearch
import ssl

### 必ずsleep timeをセットする。ページからblock可能性が高いです。
### random ライブラリを使用すると時間が調整しやすい。
### elastic dockerを実行したらプログラムを実行
URL = 'https://news.yahoo.co.jp/topics/it?page='

#使用リスク
links=[]    #link list
index=[]    #削除したelementsのインデックスを保存リスク

#Logging Setting
logger = logging.getLogger('Output_logging_file')
file_logger = logging.FileHandler('ouput_logging_newsfile.log')
new_format = '[%(asctime)s] - [%(levelname)s] - %(message)s'
file_logger_format = logging.Formatter(new_format)

# ファイルでもコンソールでもデータを入力するため Stream Handlerを使います
file_logger.setFormatter(file_logger_format)
logger.addHandler(file_logger)
logger.setLevel(logging.INFO)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger('Output_logging_file').addHandler(console)

logger.info('Collecting IT news from Yahoo website')
run_time=datetime.now()
string_run_time = run_time.strftime("%m/%d/%Y, %H:%M:%S")
logger.info('Program run at:{} '.format(string_run_time))

for page in range(1, 2):
    req = requests.get(URL + str(page))
    soup = bs(req.text, 'html.parser')

    #tit=soup.find_all('div', {'class': 'newsFeed_item_title'})
    li=soup.find_all('a', {'class': 'newsFeed_item_link'})

    for l in li:
        links.append(l.attrs["href"])
    """for t in tit:
        titles.append(t.text)"""
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
logger.info("Original links: {}".format(len(craw_source)))

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
logger.info("Index of not usual links: {}".format(len(index)))
logger.info("Links after edit: {}".format(len(craw_source)))

#Elasticサーバーの設定
ctx = ssl.create_default_context()
ctx.load_verify_locations("./http_ca.crt")
es = Elasticsearch("http://localhost:9200")
index = "daily-news-stocks"

count=1     #Check link error
line = 1    #Create index in elastic server
#Contentsを取得する
for link in craw_source:
    main_news = requests.get(link)
    soup2 = bs(main_news.content)

    try:
        title = soup2.find('h1', class_ = 'sc-eInJlc jCuuwn').text
        main_text = soup2.find("p", {"class": "sc-giadOv loZBCE yjSlinkDirectlink highLightSearchTarget"})

        #Find tag <a> and delete
        tags_delete = main_text.find_all('a')       #ページコードによって<ruby> tag, <a> tag, <h{1-3}> tagなど
        for t in tags_delete:                       #全部削除する場合もあります
            t.decompose()
            
        #Clean text
        main_text.text.replace('\n\n\n\n', '')
        main_text.text.replace(' ', '')
        content= main_text.text
        body = {
            "title": title,
            "link": link,               #Format data for elasticsearch
            "content": content
        }
        es.index(index=index, id=line, body=body)
        line += 1
        logger.info("Link {} ok".format(count))
        count += 1
    except IndexError as ie:
        logger.error("Link {} get {}".format(count,ie))
        logger.error("Link error: {}".format(link))
        count += 1
    sleep(randint(4, 10))

