#Middle Band = 20-day simple moving average (SMA)
#Upper Band = 20-day SMA + (2 x 20-day standard deviation of price)
#Lower Band = 20-day SMA - (2 x 20-day standard deviation of price)

# Load the necessary packages and modules

import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import pandas as pd
import yfinance

# Compute the Bollinger Bands 
def BBANDS(data, n ):
    MA = data.Close.rolling(window=n).mean()
    SD = data.Close.rolling(window=n).std()
    data['UpperBB'] = MA + (2 * SD) 
    data['LowerBB'] = MA - (2 * SD)
    data['MidBB'] = MA
    return data
 
# Retrieve the ETH-EUR data from Yahoo finance:
data = pdr.get_data_yahoo("ETH-EUR", start="2021-01-01", end="2022-01-01")  
data = pd.DataFrame(data)

print(data)

# Compute the Bollinger Bands ETH EUR using the 20-day Moving average
n = 20
ETH_EUR_BBANDS = BBANDS(data, n)
print(ETH_EUR_BBANDS)

plt.figure(figsize=(9,5))
plt.plot(ETH_EUR_BBANDS.Close,lw=1, label='ETH EUR Prices')
plt.plot(ETH_EUR_BBANDS.UpperBB,'r',lw=1, label='20-day Bollinger Band (red)')
plt.plot(ETH_EUR_BBANDS.LowerBB, 'r', lw=1, label='20-day Bollinger Band (red)')
plt.plot(ETH_EUR_BBANDS.MidBB, 'g', lw=1, label='20-day SMA (green)')
plt.legend(loc=2,prop={'size':9})
plt.grid(True)
plt.setp(plt.gca().get_xticklabels(), rotation=30)
plt.show()
