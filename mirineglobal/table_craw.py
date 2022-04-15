import pandas as pd
import time
page=''
while page not in ['losers', 'trending-tickers']:
    page = input('株価の状態を見たい (losers/trending-tickers)： ')
    if page not in ['losers', 'trending-tickers']:
        print('もう一度入力してください！')

url = 'https://finance.yahoo.com/{}'.format(page)

dfs = pd.read_html(url)
df = dfs[0]
if page == 'trending-tickers':
    df2 = df[['Symbol', 'Name', 'Last Price', 'Market Time', 'Change', '% Change',
              'Volume', 'Market Cap']]

else:
    df2 = df[['Symbol', 'Name', 'Price (Intraday)', 'Change', '% Change',
              'Volume', 'Market Cap']]

print(df2)

df2.to_excel('python-{}.xlsx'.format(page))
