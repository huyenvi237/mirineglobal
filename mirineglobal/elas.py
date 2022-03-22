from elasticsearch import Elasticsearch, helpers
import csv, ssl, json
from datetime import datetime

#Solve problem about Certificate
ctx = ssl.create_default_context()
ctx.load_verify_locations("elasticsearch-8.1.0/config/certs/http_ca.crt")

# Create the elasticsearch client.
es = Elasticsearch("http://localhost:9200",ssl_context=ctx)

#毎日株価をESに登録するため、実行するの日でstock名を保存
run_time=datetime.now()
time_string=run_time.strftime("%d")

# Open csv file and bulk upload
with open('stock_data1.csv') as f:
    reader = csv.DictReader(f)  #CSVファイルからデータを読んで、Dictionaryを作る。
    line=1
    for row in reader:
        #helpers.bulk(es, reader, index='stock1', doc_type="type", id=line) <----up by bulk
        es.index(index='stock{}'.format(time_string), doc_type='prod', id=line,
                 body=json.dumps(row))      #json formatに変換し、elasticsearchにアップロードする。
        line+=1
