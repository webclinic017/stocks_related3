import talib as ta
from ta.utils import dropna
import yfinance as yf
import pandas as pd
import sys
import re
import numpy as np
from talib import stream
from matplotlib import dates
import matplotlib.pyplot as plt
##from datetime import date
##today = date.today().isoformat()
import datetime
import math
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
plt.style.use('fivethirtyeight')
from millify import millify
##today = datetime.date.today() + datetime.timedelta(days=1)
today = datetime.date.today()
##day = datetime.datetime.strptime(Date, '%d %m %Y').weekday()
##print(datetime.today().strftime('%Y-%m-%d'))
import mpl_finance
import matplotlib
import sys
##from matplotlib.finance import candlestick2_ohlc
##from mpl_finance import candlestick_ohlc
##from mplfinance.original_flavor import candlestick_ohlc
from mplfinance.original_flavor import candlestick_ohlc
from optionprice import Option
from numerize import numerize
import matplotlib.pyplot as plt
pd.options.display.width = 0
pd.set_option('display.max_columns', None)
pd.options.display.float_format = '{:.2f}'.format
##pd.options.display.max_columns=255
pd.options.display.max_rows=6500000
pd.set_option('display.max_colwidth', 500)
pd.set_option('display.max_columns', 550)
pd.options.mode.chained_assignment = None  # default='warn'

   


perda='1d'
intervla='1m'
yy=str(intervla).split('d')[0]
shiftbydays=3



##    g=input("Entr_Signal ticker: ")
perd=perda
intervl=intervla
##    ticker='BTC-USD'
##    ticker='^NDX'
##    ticker='MSTR'
##    ticker='MRNA'
##    ticker='AMZN'
##    ticker='TSLA'
ticker='DOCU'
# [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]



#df=pd.DataFrame()
#Interval required 5 minutes
df = yf.download(ticker, period=perd, interval=intervl,prepost = True)
df=pd.DataFrame(df)

df.reset_index(inplace=True)
df=df[:7]
##print(df)
df['m']=''
for x in df.index:
    df['m'].loc[x]=87
print(df)    
    
