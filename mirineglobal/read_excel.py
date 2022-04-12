import pandas as pd

logic = True
file = pd.ExcelFile('python-losers.xlsx')
df = pd.read_excel(file)

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


