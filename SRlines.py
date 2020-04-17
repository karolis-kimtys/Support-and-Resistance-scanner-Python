"""
This code will plot Market OHLC Data & Support & Resistance zones using Matplotlib
"""

import pandas as pd
import numpy as np
from mpl_finance import candlestick2_ohlc
import matplotlib.pyplot as plt
from scipy.signal import argrelmax
from scipy.signal import argrelmin

#Read CSV file with Pandas
df = pd.read_csv('EURCHFClean.csv')

#Set Pandas columns
df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']

#Set Date column as index
df = df.set_index(df.Date)
df['Date'] = pd.to_datetime(df['Date']).tolist()

#Use only 100 data rows 
df = df.iloc[:100]

#Make copies of Pandas Dataframe columns data
df_open = df.Open.copy()
df_high = df.High.copy()
df_low = df.Low.copy()
df_close = df.Close.copy()
df_volume = df.Volume.copy()

#Find Low Extremes in data set from Low price values
df_support = argrelmin(df_low.values, order=5)
support_prices = df_low[df_support[0]]
support_prices_lower = df_open[df_support[0]]

#Find High Extremes in data set from High price values
resistance = argrelmax(df_high.values, order=5)
resistance_prices = df_high[resistance[0]]
resistance_prices_higher = df_open[resistance[0]]

print('Support prices', support_prices)
print('Support:', df_support)
print('Resistance:', resistance)

#Plot Market OHLC Data Candles chart
fig, ax = plt.subplots(figsize=[15, 9])
candlestick2_ohlc(ax, df['Open'], df['High'], df['Low'], df['Close'], colorup='green', colordown='red', width=0.5)

#Plot Suppport and Resistance zones
plt.gca().add_patch(plt.Rectangle((low[support[0]], high[5]), height=0.001, width=5))
plt.scatter(support, support_prices)
plt.scatter(resistance, resistance_prices)
plt.show()

#Generate a new CSV File with complete data frame
df.to_csv("SRlines.csv")
