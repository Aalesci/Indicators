# Moving Averages Code

# Load packages and modules
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import pandas as pd
import yfinance

# Simple Moving Average 
def SMA(data, number_of_days): 
 SMA = pd.Series(data['Close'].rolling(number_of_days).mean(), name = 'SMA') 
 data = data.join(SMA) 
 return data

# Exponentially weighted Moving Average 
def EWMA(data, number_of_days): 
 EMA = pd.Series(data['Close'].ewm(span = number_of_days, min_periods = number_of_days - 1).mean(), 
                 name = 'EWMA_' + str(number_of_days)) 
 data = data.join(EMA) 
 return data

# Retrieve the BTC/EUR data from Yahoo finance:
data = pdr.get_data_yahoo("BTC-EUR", start="2021-01-01", end="2022-01-01") 
data = pd.DataFrame(data) 
close = data['Close']  #Note: Close is a series. 
#print(close)


# Compute the 50-day SMA for BTC-EUR
Nfd_sma = 10
SMA_BTC = SMA(data,Nfd_sma)
SMA_BTC = SMA_BTC.dropna()
SMA = SMA_BTC['SMA']


# Compute the 200-day EWMA for BTC-EUR
Nfd_ewma = 20
EWMA_BTC = EWMA(data,Nfd_ewma)
EWMA_BTC = EWMA_BTC.dropna()
EWMA = EWMA_BTC['EWMA_20'] 

# Plotting the NIFTY Price Series chart and Moving Averages below
plt.figure(figsize=(9,5))
plt.plot(data['Close'],lw=1, label='NSE Prices')
plt.plot(SMA,'g',lw=1, label='50-day SMA (green)')
plt.plot(EWMA,'r', lw=1, label='200-day EWMA (red)')
plt.legend(loc=2,prop={'size':11})
plt.grid(True)
plt.setp(plt.gca().get_xticklabels(), rotation=30)
plt.show()