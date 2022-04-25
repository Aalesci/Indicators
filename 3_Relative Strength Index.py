# Relative Strength Index
# Relative Strength Index (RSI) and the Relative Strength (RS).
# The RS is a proportional measure of average price gains and average price losses 
# and the RSI provides a standardized value from 0-100 to reflect that relationship. 
# The formula for each are as follows:
#  RS  = avg.gain / avg.loss 
#  RSI = 100 - { 100 / (1 + RSI) }

from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
import yfinance


def rsi(df, periods = 14, ema = True):
    #Returns a pd.Series with the relative strength index
    close_delta = df['Close'].diff()

    # Make two series: one for lower closes and one for higher closes
    up = close_delta.clip(lower=0)
    down = -1 * close_delta.clip(upper=0)
    
    if ema == True:
	    # Use exponential moving average
        ma_up = up.ewm(com = periods - 1, adjust=True, min_periods = periods).mean()
        ma_down = down.ewm(com = periods - 1, adjust=True, min_periods = periods).mean()
    else:
        # Use simple moving average
        ma_up = up.rolling(window = periods, adjust=False).mean()
        ma_down = down.rolling(window = periods, adjust=False).mean()
        
    rsi = ma_up / ma_down
    rsi = 100 - (100/(1 + rsi))
    rsi = pd.Series(rsi )
    return rsi

data = pdr.get_data_yahoo("SOL-EUR", start="2021-01-01", end="2022-01-01")
RSI_SOL = rsi(data)  
RSI_SOL.replace(np.nan, 50, inplace=True)
print(RSI_SOL)



plt.figure(figsize=(12,8))

plt.subplot(211)
plt.title('Price of SOL-EUR')
plt.plot( data['Close'] ,lw=1, label='SOL-EUR')
plt.grid(True)
plt.legend(loc=2,prop={'size':11})
plt.setp(plt.gca().get_xticklabels(), rotation=30)

plt.subplot(212)
plt.title('RSI of SOL-EUR')
plt.plot( RSI_SOL,'g',lw=1, label='Relative Strength Index')
plt.grid(True)
plt.legend(loc=2,prop={'size':11})
plt.setp(plt.gca().get_xticklabels(), rotation=30)

plt.show()
