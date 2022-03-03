import sys          #Terminalでのコードを読むため
from datetime import datetime
import yfinance as yf       #Yahoo financeを使いために
import plotly.graph_objects as go
import pandas as pd
import logging

#データを取得
def get_data(stock_name,time):
    # Datetimeを設定
    end_date = datetime.now()

    #Yahoo Financeからデータを取得
    dt=yf.download(stock_name,start=time,end=end_date)
    dt.to_csv('stock_data1.csv')         #データをCSVファイルに書き込む

    dr = pd.read_csv('stock_data1.csv')

    #Graphを設計
    fig = go.Figure(data=[go.Candlestick(x=dr['Date'],
                                         open=dr['Open'], high=dr['High'],
                                         low=dr['Low'], close=dr['Close'])
                          ])

    fig.update_layout(
        title='CandleStick Chart',
        yaxis_title='SBI Stock',
        shapes=[dict(
            x0='2022-02-15', x1='2022-02-15', y0=0, y1=1, xref='x', yref='paper',
            line_width=2)],
        annotations=[dict(
            x='2022-02-15', y=0.05, xref='x', yref='paper',
            showarrow=False, xanchor='left', text='Nami Period Begins')]
    )
    fig.show()

if __name__ == "__main__":

    args=sys.argv
    get_data(args[1],args[2])
