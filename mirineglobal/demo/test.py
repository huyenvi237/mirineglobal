#Import Library
 #まだ使えない
import requests
from time import sleep      #エーラ429をfixするためにimportですがまだ改善できません。
from bs4 import BeautifulSoup
import investpy as inv  # investing.comからデータを取得
import matplotlib.pyplot as plt     #Graphを書くため
from bokeh.plotting import figure, show, output_file
 #使っているLibrary
from datetime import datetime
import csv                  #CSVを処理ために
import yfinance as yf       #Yahoo financeを使いために
import plotly.graph_objects as go
import pandas as pd
import logging

#銘柄コードのCSVファイルから読み込む
stock_list=[]
with open('../stock.csv') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')

    for row in csv_reader:
        stock_list.append(row[0])
#実行チェック
print(stock_list)
print(stock_list[15])

#investpyを使ってみましたがエーラ429出てきました
#df = inv.get_stock_historical_data(stock='1332',
                                      # country='Japan',
                                       #from_date=start_date,
                                       #to_date=end_date)

start_date=datetime(2022,1,1)
end_date=datetime.now()
#データを取得
dt= yf.download('SBI',start=start_date,end=end_date)
print(dt)
dt.to_csv('stock_data.csv')         #CSVファイルにデータを書き込む

dr=pd.read_csv('stock_data.csv')
fig = go.Figure(data=[go.Candlestick(x=dr['Date'],
                open=dr['Open'], high=dr['High'],
                low=dr['Low'], close=dr['Close'])
                     ])

fig.update_layout(
title='CandleStick Chart',
    yaxis_title='SBI Stock',
    shapes = [dict(
        x0='2022-02-15', x1='2022-02-15', y0=0, y1=1, xref='x', yref='paper',
        line_width=2)],
    annotations=[dict(
        x='2022-02-15', y=0.05, xref='x', yref='paper',
        showarrow=False, xanchor='left', text='Nami Period Begins')]
)
fig.show()