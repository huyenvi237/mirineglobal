import pandas as pd

url = 'https://finance.yahoo.com/trending-tickers'
dfs = pd.read_html(url)

df = dfs[0]
df2 = df[['Symbol','Name','Last Price','Market Time','Change','% Change',
          'Volume','Market Cap']]
df2.to_excel('python.xlsx')