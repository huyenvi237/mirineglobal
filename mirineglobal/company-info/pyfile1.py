from bs4 import BeautifulSoup
import requests
from http.client import RemoteDisconnected
import time

#headersをセットしないとRemoteDisconnectというエーラが出る場合がある
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0"
}

url = "https://www.sbigroup.co.jp/english/investors/disclosure/presentation/"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

info = soup.find_all("a",{"class":"pdf"})

links=[]
for i in info:
    links.append(i.attrs["href"])
print('Get all link from <a>')

#PDFファイルを作成関数
def download_file(download_url, filename):
    response = requests.get(download_url, headers=headers)
    file = open(filename + ".pdf", 'wb')
    file.write(response.content)
    file.close()

#Main
if __name__ == "__main__":

    i = 0   #File nameを作るため
    for n in range(len(links)):
        if i ==20:
            break;
        i += 1
        try:
            download_file("https://www.sbigroup.co.jp" + links[n], "PDFfile{}".format(i))
        except RemoteDisconnected:
            print("Disconnect error")

        time.sleep(15)  # 全部ファイルを取得するとサーバーが困る場合もありますのでスレッドが15秒スリープに設定しました
    print('Finished.')