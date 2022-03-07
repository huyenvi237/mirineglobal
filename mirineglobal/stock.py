import sys          #Terminalでのコードを読むため
from datetime import datetime
import yfinance as yf       #Yahoo financeを使いために
import plotly.graph_objects as go
import pandas as pd         #Data Analysisの対応
import logging

#データを取得

def get_data(stock_name,time):
    # Datetimeを設定

    end_date = datetime.now()

    #Yahoo Financeからデータを取得
    try:
        dt=yf.download(stock_name,start=time,end=end_date)
        dt.to_csv('stock_data1.csv')         #データをCSVファイルに書き込む
        logger.info('Download Succeed!')
    except Exception:
        logger.info('Can not download data!Try again!')

    dr = pd.read_csv('stock_data1.csv')
    fig = go.Figure(data=[go.Candlestick(x=dr['Date'],
                                         open=dr['Open'], high=dr['High'],
                                         low=dr['Low'], close=dr['Close'])
                          ])

    fig.update_layout(
        title='CandleStick Chart',
        yaxis_title='{} Stock'.format(stock_name),
        shapes=[dict(
            x0='2022-02-15', x1='2022-02-15', y0=0, y1=1, xref='x', yref='paper',
            line_width=2)],
        annotations=[dict(
            x='2022-02-15', y=0.05, xref='x', yref='paper',
            showarrow=False, xanchor='left', text='Nami Period Begins')]
    )
    fig.show()

#入力したdatetime formatをチェック
def check_date_input(time):
    check_time=time
    date_format= '%Y-%m-%d'
    try:
        change=datetime.strptime(check_time,date_format)
        logger.info('Date time format is correct')
        logger.info('Date time is {}'.format(change))

    except ValueError as ve:
        logger.error(ve)
        exit(1)

#Main
if __name__ == "__main__":

    #Logging Setting
    logger = logging.getLogger('Output_logging_file')
    file_logger = logging.FileHandler('ouput_logging_file.log')
    new_format = '[%(asctime)s] - [%(levelname)s] - %(message)s'
    file_logger_format = logging.Formatter(new_format)

    #ファイルでもコンソールでもデータを入力するため Stream Handlerを使います
    file_logger.setFormatter(file_logger_format)
    logger.addHandler(file_logger)
    logger.setLevel(logging.INFO)

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    logging.getLogger('Output_logging_file').addHandler(console)

    try:
        args=sys.argv
        #print(type(args))----->argsのタイプを確認します
        check_date_input(args[2])
        get_data(args[1], args[2])
        logger.info('No problem with parameter!')
        print('Stock name is {d[1]},checked from {d[2]}'.format(d=args))
    except IndexError as ie:
        logger.error(ie)



