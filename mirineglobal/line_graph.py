import matplotlib.pyplot as plt
import datetime
import pandas_datareader.data as web

start = datetime.datetime(2022, 1, 1)
end = datetime.datetime(2022, 3, 3)

df = web.DataReader("SBI", 'yahoo', start, end)
print(df.tail())

plt.plot(df['Close'].tail(100), linestyle = '-', marker = 'o')
plt.ylabel('PRICE')
plt.xlabel('DATE-TIME')
plt.title('SBI STOCK')
plt.show()