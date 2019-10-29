import pandas as pd
import numpy as np
from mpl_finance import candlestick2_ohlc
import matplotlib.pyplot as plt
from scipy.signal import argrelmax
from scipy.signal import argrelmin


df = pd.read_csv('EURCHFClean.csv')
df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
df = df.set_index(df.Date)
df['Date'] = pd.to_datetime(df['Date']).tolist()
df = df.iloc[:100]


open = df.Open.copy()
high = df.High.copy()
low = df.Low.copy()
close = df.Close.copy()
volume = df.Volume.copy()

support = argrelmin(low.values, order=5)
#df['Support'] = support
support_prices = low[support[0]]

support_prices_lower = open[support[0]]


resistance = argrelmax(high.values, order=5)
resistance_prices = high[resistance[0]]
resistance_prices_higher = open[resistance[0]]



print('Support prices', support_prices)
print('Support:', support)
print('Resistance:', resistance)





fig, ax = plt.subplots(figsize=[15, 9])
candlestick2_ohlc(ax, df['Open'], df['High'], df['Low'], df['Close'], colorup='green', colordown='red', width=0.5)

plt.gca().add_patch(plt.Rectangle((low[support[0]], high[5]), height=0.001, width=5))
plt.scatter(support, support_prices)
plt.scatter(resistance, resistance_prices)
plt.show()


#Generate a new CSV File with complete data frame
df.to_csv("SRlines.csv")
