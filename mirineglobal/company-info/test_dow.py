from http.client import RemoteDisconnected

import requests

#headersをセットしないとRemoteDisconnectというエーラが出る場合がある
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0"
}
pdf_path = "https://ssl4.eir-parts.net/doc/7741/tdnet/2075306/00.pdf"


def download_file(download_url, filename):
    response = requests.get(download_url, headers=headers)
    file = open(filename + ".pdf", 'wb')
    file.write(response.content)
    file.close()

try:
    download_file(pdf_path, "Test")
except RemoteDisconnected:
    print("error")
