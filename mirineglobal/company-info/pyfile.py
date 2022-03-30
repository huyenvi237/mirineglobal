from bs4 import BeautifulSoup
import requests
from http.client import RemoteDisconnected
import time
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

#headersをセットしないとRemoteDisconnectというエーラが出る場合がある
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0"
}

url = "https://www.sbigroup.co.jp/english/investors/disclosure/fiscalresults/index.html"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

info = soup.find_all("a",{"class":"pdf"})

links=[]
for i in info:
    links.append(i.attrs["href"])
logger.info('Get all link from <a>')

#PDFファイルを作成関数
def download_file(download_url, filename):
    response = requests.get(download_url, headers=headers)
    file = open(filename + ".pdf", 'wb')
    file.write(response.content)
    file.close()

#Main
if __name__ == "__main__":
    run_time = datetime.now()
    string_run_time = run_time.strftime("%m/%d/%Y, %H:%M:%S")
    logger.info('Program run at:{} '.format(string_run_time))

    i = 0   #File nameを作るため
    for n in range(len(links)):
        i += 1
        if n == 0:
            try:
                download_file(links[n], "PDFfile{}".format(i))
            except RemoteDisconnected:
                logger.error("Disconnect error")
        else:
            try:
                download_file("https://www.sbigroup.co.jp" + links[n], "PDFfile{}".format(i))
            except RemoteDisconnected:
                logger.error("Disconnect error")
        time.sleep(15)  # 全部ファイルを取得するとサーバーが困る場合もありますのでスレッドが15秒スリープに設定しました
    logger.info('Finished.')