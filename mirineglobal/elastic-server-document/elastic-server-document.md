Elasticsearch保存の自動化




# I. 概要：  
## 1. ドキュメントの目的：  
- プログラムで直したコードと使用する関数、追加ライブラリの目的が分かるようになる。
- コーディングの手順またを入力・出力イメージ明確化する。
## 2. 概略仕様:  
- 直した部分の説明。
- 追加ライブラリ。
- コーディングの手順。
- Crontabの説明。
# II. 作業一覧:  
## 1. 直した部分の説明：
- クローリングした会社のDate 、株価、VolumeをElasticSearchにデータを保存するため、elas.pyという新しいファイルを作成しました。
- Crontabを実行するとデータを自動的に保存するから時間がlogファイルに書き残すためstock1.pyのファイルでコードを追加します。

![自動的に生成された説明](Aspose.Words.b4e956b6-7cf2-47cf-b817-7654df7ff04e.002.png)

## 2. Elas.pyファイルで使用するライブラリ：

![低い精度で自動的に生成された説明](Aspose.Words.b4e956b6-7cf2-47cf-b817-7654df7ff04e.003.png)

Elasticsearch: elasticsearch	サーバーを使うため。

Csv: csvファイルを読むため。

Ssl: SSL Certificateを処理するため。

Json: jsonファイルを操作するため。

Datetime: 日付の管理ため。

## 3. コーディングの手順：
- ElasticSearchサーバーの活動を確認します。

![自動的に生成された説明](Aspose.Words.b4e956b6-7cf2-47cf-b817-7654df7ff04e.004.png)

「elasticsearch is running」->サーバーが実行しています。

サーバーを実行した後でサーバーの情報を確認できます。

![自動的に生成された説明](Aspose.Words.b4e956b6-7cf2-47cf-b817-7654df7ff04e.005.png)

- クローリングしたデータがcsvファイルとして取得するためstock1.pyというファイルを実行します。

python3 stock1.py SBI 2022-02-15

![](Aspose.Words.b4e956b6-7cf2-47cf-b817-7654df7ff04e.006.png)

- Elas.pyファイルを実行します。

python3 elas.py

![](Aspose.Words.b4e956b6-7cf2-47cf-b817-7654df7ff04e.007.png)

- Elasticsearchのサーバーでインデックスをチェックします。

curl -XGET "http://localhost:9200/\_cat/indices"

![](Aspose.Words.b4e956b6-7cf2-47cf-b817-7654df7ff04e.008.png)

- Stockの情報を確認できます。

![自動的に生成された説明](Aspose.Words.b4e956b6-7cf2-47cf-b817-7654df7ff04e.009.png)

## 4. crontabの説明：

“crontabは定期的にジョブを実行するようスケジュールするcronを設定するコマンドです。”

![自動的に生成された説明](Aspose.Words.b4e956b6-7cf2-47cf-b817-7654df7ff04e.010.png)

Crontabのファイルで

「0 10 \* \* \* cd /mnt/c/Users/mg-sa/Desktop/mirineglobal && python3 stock1.py SBI 2022-01-30

2 10 \* \* \* cd /mnt/c/Users/mg-sa/Desktop/mirineglobal && python3 elas.py」という命令を書きました。

意味は：毎日10時にmirineglobalのフォルダに移動して、stock1.pyのファイルを実行します。また2分後でelas.pyのファイルも実行します。















