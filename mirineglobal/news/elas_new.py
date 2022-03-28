from elasticsearch import Elasticsearch
import csv, ssl, json
from datetime import datetime

#Solve problem about Certificate
ctx = ssl.create_default_context()
ctx.load_verify_locations("../elasticsearch-8.1.0/config/certs/http_ca.crt")

# Create the elasticsearch client.
es = Elasticsearch("http://localhost:9200",ssl_context=ctx)

#毎日株価をESに登録するため、実行するの日でstock名を保存
run_time=datetime.now()
date_string=run_time.strftime("%d")
time_string=run_time.strftime("%H")
# Open csv file and bulk upload
with open('new2.csv') as f:
    reader = csv.DictReader(f)  #CSVファイルからデータを読んで、Dictionaryを作る。
    line=1
    for row in reader:
        es.index(index='{}stock_new{}'.format(time_string,date_string), doc_type='type', id=line,
                 body=json.dumps(row))      #json formatに変換し、elasticsearchにアップロードする。
        line+=1