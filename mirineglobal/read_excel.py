import pandas as pd
from datetime import datetime
import yfinance as yf       #Yahoo financeを使いために
import plotly.graph_objects as go

def pick_file(inp):
    df = pd.read_excel('python-{}.xlsx'.format(inp))
    return df

def find(df):
    logic = True
    while logic:
        n = 0
        stock_name = input('見つけたい会社の記号を入力してください：　').upper()
        for d in df['Symbol']:
            if stock_name == d :
                print('みつけた')
                print(df[df['Symbol'] == stock_name])
                n+=1

        if n == 0:
            print('見つけない！')
        ans = ''
        while ans not in ['Y','N']:
            ans = input('続けますか？（Y/N）: ').upper()
            if ans not in ['Y','N']:
                print('もう一度入力してください！')
            if ans == 'N':
                logic = False
                print('Thank!')

def printF(df):
    print('Running')
    check = 0
    for d in df['% Change']:
        # print(d.replace('%','0'))
        if float(d.replace('%', '0')) <= -10:
            print(df[df['% Change'] == d])
            check +=1
        else:
            continue
    if check < 1:
        print('-10%より下がった株価がない！')

def get_data():
    end_date = datetime.now()
    stock_name = input('Enter stock symbol: ')
    check_date = input('Check from when: ')
    dt = yf.download(stock_name, start=check_date, end=end_date)
    print(dt)
    dt.to_csv('stock.csv')
    dr = pd.read_csv('stock.csv')
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
    #Save graph to picture(.png)
    fig.write_image("graph.png")
    # pass

def infor():
    print("""
        -------------------------------------
        List of action:
            1.Print stock data which lost more than 10%
            2.Find stock data
            3.Get data from web (If you can't find in stock data)
            0.Exit
        -------------------------------------
        """)
    choice = int(input('Choose number: '))
    return choice

if __name__ == '__main__':
    while(True):
        choice = infor()
        if choice == 1:
            df = pick_file('losers')
            print(df)
            printF(df)
        elif choice == 2:
            inp = input('Type of stock data: (losers/trending-tickers/gainers) ')
            df = pick_file(inp)
            print(df)
            find(df)
        elif choice == 3:
            get_data()
        elif choice == 0:
            print('Thank!')
            exit()


