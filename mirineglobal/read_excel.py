import pandas as pd

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

def infor():
    print("""
        -------------------------------------
        List of action:
            1.Print stock data which lost more than 10%
            2.Find stock data 
            3.Exit
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
            find(df)
        elif choice == 3:
            print('Thank!')
            exit()


