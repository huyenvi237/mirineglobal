import requests
from bs4 import BeautifulSoup
import urllib
import os
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

logger.info('Collecting news from Hoya Company website')
run_time=datetime.now()
string_run_time = run_time.strftime("%m/%d/%Y, %H:%M:%S")
logger.info('Program run at:{} '.format(string_run_time))

#Library Page
response = requests.get("https://www.hoya.co.jp/investor/library.html")
soup = BeautifulSoup(response.content, "html.parser")

document_find=soup.find_all("div",class_="irLibraryBox_col")
titles=[]   #分類書類
links=[]    #過去書類を見つけるlinks
for d in document_find:
    titles.append(d.find("h3"))
    links.append(d.find("a").attrs["href"])
with open('title.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(['Titles','Links'])
    for i in range(len(titles)):
        writer.writerow([titles[i],links[i]])
logger.info("Finished!")


#for l in links:
url = "https://www.hoya.co.jp/investor/" + links[0]
logger.info(url)  # Check link
page_res = requests.get(url)
soup = BeautifulSoup(page_res.content, "html.parser")

find_div= soup.find("div", {"id": "divDataArea"}).findChildren('dl')
print(len(find_div))
"""prod_name = find_div[0].findChildren("dd", {"class": "get"}).findChildren('a')
print(prod_name.get_text(strip=True))
dl_data=find_div[0].find_all("a")
for dli in dl_data:
    print(dli.string)
a タグからのデータを取得できませんでした<===原因は考えています"""

