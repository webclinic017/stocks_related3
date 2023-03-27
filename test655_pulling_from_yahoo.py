'''
This file contains a simple animation demo using mplfinance "external axes mode".
Note that presently mplfinance does not support "blitting" (blitting makes animation
more efficient).  Nonetheless, the animation is efficient enough to update at least
once per second, and typically more frequently depending on the size of the plot.
'''

import ccxt,sys
import ccxt
import calendar,time
from datetime import datetime
import pandas as pd
import sys
pd.options.display.width = 0
pd.set_option('display.max_columns', None)
pd.options.display.float_format = '{:.2f}'.format
##pd.options.display.max_columns=255
pd.options.display.max_rows=6500000
pd.set_option('display.max_colwidth', 500)
pd.set_option('display.max_columns', 550)
pd.options.mode.chained_assignment = None  # default='warn'
import pandas as pd
from datetime import datetime
import json,sys
import numpy as np
from numerize import numerize
import ccxt
import yfinance as yf
import sys
from time import time
from datetime import datetime
import tzlocal
import numerize
from numerize import numerize


import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from datetime import timedelta
import pandas_alive
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
##from hhpy.plotting import animplot

##import yfinance as yf
##
##from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
##
##x1='y9SvMHSmcHMw7wrGBF5SLKRGYBU8VjOJkGdwkN9XrnPelKeBcqXhyNKt28LDPxxG'
##y1='BsKSkRvqtbvo2gmV5Brgjc3CujV724vfDCSuTES9DfhaZdVxQmR293tjtYVdTFcO'
######client = RequestClient(api_key=x1, secret_key=y1, https://fapi.binance.com')
####client = Client(x1, y1, url='https://testnet.binancefuture.com')
####client = SubscriptionClient(api_key=x1, secret_key=y1, uri='wss://fstream.binance.com/ws')
##client = Client('y9SvMHSmcHMw7wrGBF5SLKRGYBU8VjOJkGdwkN9XrnPelKeBcqXhyNKt28LDPxxG', 'BsKSkRvqtbvo2gmV5Brgjc3CujV724vfDCSuTES9DfhaZdVxQmR293tjtYVdTFcO'
##                , tld='us')
##
##prices = client.get_all_tickers()
##print(prices)


##df=pd.DataFrame()
##ticker='BTC-USD'
##
##c2=[]
##c3=[]
##c4=[]
##c5=[]
##c6=[]
##c7=[]
##
##while True:
##
##    b=time()
##    unix_timestamp = float(b)
##    local_timezone = tzlocal.get_localzone() # get pytz timezone
##    local_time = datetime.fromtimestamp(unix_timestamp, local_timezone)
##    
##    stock = yf.Ticker(ticker).info['regularMarketPrice']
##    openb = yf.Ticker(ticker).info['open']
##    volumeb = (yf.Ticker(ticker).info['volume'])
####    volumec=numerize(volumeb)
##    
##    #,'regularMarketDayHigh']
##    c2.append(ticker)
##    c3.append(stock)
##    c4.append(openb)
##    c5.append(volumeb)
##    c6.append(local_time.strftime("%Y-%m-%d %H:%M:%S"))
####    print(ticker,'  ',stock,'   ',openb,'  ',(volumeb),'  ',local_time.strftime("%Y-%m-%d %H:%M:%S"))
##
##    dfc=df.append([c2,c3,c6])
##    dfc=dfc.T
##    print(dfc)
##sleep(5)

from random import randint

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

##sys.exit()
####
####sys.exit()
##
df = yf.download('BTC-USD', period='1d', interval='1m')
df.reset_index(inplace=True)

for x in df.index:
    df['Datetime'].loc[x]=str(df['Datetime'].loc[x])[0:16]

print(df)
##df.set_index('Datetime',inplace=True)
df=df[['Close','Datetime']]
##



df.plot_animated(dfkind='line')
print(df['Datetime'])
##df.set_index('Datetime')
animplot(data=df, x='x', y='y', t='t', t_format='%Y-%m-%d')





x = []
y = []

## create the figure and axes objects
fig, ax = plt.subplots()


##def animate(i):
##
##    x.append(df['Datetime'].loc[i])
##    y.append(df['Close'].loc[i])
##
##    ax.clear()
##    ax.plot(x, y)
##    ax.set_xlim([0,20])
##    ax.set_ylim([0,10])
##
##
#### run the animation
##ani = FuncAnimation(fig, animate, frames=2, interval=5, repeat=False)
##
##plt.show()
    

