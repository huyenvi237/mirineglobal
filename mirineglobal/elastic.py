import requests
substring = "You Know, for Search".encode()
response= requests.get("http://localhost:9200")
if substring in response.content:
    print("OK")
else:
    print("Error")
