# The Moving Average Convergence Divergence (MACD) 

# This indicator serves as a momentum indicator that can help signal shifts 
# in market momentum and help signal potential breakouts.

# standard imports
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from pandas_datareader import data as pdr


#Setting
# MACD parameters
short_period = 12
long_period  = 26
signal_period = 9
 
# define the dates for downloading the data
startDate= '2020-01-01'
endDate= '2021-01-28'

#Get data 
data = pdr.get_data_yahoo("BTC-EUR", start= startDate, end=endDate) 
df = pd.DataFrame(data) 

def macd(df, ema_long,ema_short, ema_MACD ):

    EMA_short = pd.Series( df['Close'].ewm(span=ema_short).mean(), name = 'EMA_short' )
    EMA_long = pd.Series( df['Close'].ewm(span=ema_long).mean(), name = 'EMA_long' )
    Macd  = pd.Series(EMA_long.sub(EMA_short), name = 'Macd' )
    MACDSignalLine = pd.Series(Macd.ewm(span=9).mean(), name = 'MACDSignalLine') 
    Histogram  = pd.Series(Macd.sub(MACDSignalLine), name = 'Histogram')

    df = df.join(EMA_short)
    df = df.join(EMA_long)
    df = df.join(Macd)
    df = df.join(MACDSignalLine)
    df = df.join(Histogram)
    
    return df


df = macd(df,long_period,short_period,signal_period)
print(df)


#Plot data 
ax1 = plt.subplot(211)
ax1.plot(df['Close'],lw=1, label='BTC-EUR')
ax1.plot(df['EMA_short'],'g',lw=1, label='EMA Short')
ax1.plot(df['EMA_long'],'r', lw=1, label='EMA Long')
ax1.legend(loc=2,prop={'size':9})
ax1.grid(True)

ax2 = plt.subplot(212, sharex=ax1)
ax2.plot(df['MACDSignalLine'],'b', lw=1, label='Signal Line') 
ax2.plot(df['Macd'],'r', lw=1, label='Macd') 
#ax2.bar( df['Histogram'],'b')
ax2.bar(df.index, df['Histogram'].fillna(0), width=0.5, snap=False)
ax2.legend(loc=2,prop={'size':9})
ax2.grid(True)
plt.show()

