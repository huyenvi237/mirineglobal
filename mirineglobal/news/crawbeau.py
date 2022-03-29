import requests
from bs4 import BeautifulSoup
import time
import csv
import logging
from datetime import datetime

#Logging Setting
logger = logging.getLogger('Output_logging_file')
file_logger = logging.FileHandler('ouput_logging_file.log')
new_format = '[%(asctime)s] - [%(levelname)s] - %(message)s'
file_logger_format = logging.Formatter(new_format)

# ファイルでもコンソールでもデータを入力するため Stream Handlerを使います
file_logger.setFormatter(file_logger_format)
logger.addHandler(file_logger)
logger.setLevel(logging.INFO)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger('Output_logging_file').addHandler(console)

logger.info('Collecting news from Yahoo website')
run_time=datetime.now()
string_run_time = run_time.strftime("%m/%d/%Y, %H:%M:%S")
logger.info('Program run at:{} '.format(string_run_time))

#HomePage
response = requests.get("https://www.yahoo.co.jp/")
soup = BeautifulSoup(response.content, "html.parser")
#Mainの情報
main_infor = soup.find_all("div",{"class":"_1XAfHUWtx6tfYZuWDVjNxZ"})
x=main_infor[0]
#ニューズのリングは"li"のタグで残っているから"li"タグから取得する
li=x.find_all("li")
links = [link.find('a').attrs["href"] for link in li]
logger.info('Collect links from home page successful')

#ニューズのリングにアクセスする
def getMain_page(li):
    list_link=[]
    for links in li:
        news_page = requests.get(links)
        soup1 = BeautifulSoup(news_page.content, "html.parser")
        page_info = soup1.find_all("div", {"class": "sc-fXUGxx lawZbQ"})
        for link in page_info:
            list_link.append(link.find('a').attrs["href"])
    return list_link

craw_source=getMain_page(links)
title=[]
content=[]
for link in craw_source:
    main_news = requests.get(link)
    soup2 = BeautifulSoup(main_news.content, "html.parser")
    title.append(soup2.find("h1", {"class": "sc-eInJlc jCuuwn"}).text)
    body = soup2.find_all("div", {"class": "sc-ipZHIp ieFwHi"})
    y = body[0]
    content.append(y.findChild("p", {"class": "sc-giadOv loZBCE yjSlinkDirectlink highLightSearchTarget"}).text)
    #クローリング情報を確認
    """print('title is {}'.format(title))
    print()
    print('contents is {}'.format(content))"""

    leng_list=len(craw_source)
    if link is not craw_source[leng_list]:  #Sleep time　セットしないとウェブからblockさせられるかもしれない。
        time.sleep(180)
logger.info('Collect all data!')

#Create CSV File
date=run_time.strftime("%m/%d")
with open("new2.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["No","Date","Titles","Contents"])
    for row in range(len(title)):
        writer.writerow([row+1, date, title[row], content[row]])
logger.info('Created a CSV file')   









