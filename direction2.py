
import talib as ta
import yfinance as yf
import pandas as pd
import datetime as dt
import sys
import re
import numpy as np
from talib import stream
import matplotlib.pyplot as plt
##from datetime import date
##today = date.today().isoformat()
import datetime
import math
from millify import millify
##today = datetime.date.today() + datetime.timedelta(days=1)
today = datetime.date.today()
##day = datetime.datetime.strptime(Date, '%d %m %Y').weekday()
##print(datetime.today().strftime('%Y-%m-%d'))
import mplfinance as mpl
import matplotlib
##from matplotlib.finance import candlestick2_ohlc
##from mpl_finance import candlestick_ohlc
##from mplfinance.original_flavor import candlestick_ohlc
from mplfinance.original_flavor import candlestick_ohlc
from optionprice import Option
from numerize import numerize

pd.options.display.width = 0
pd.set_option('display.max_columns', None)
pd.options.display.float_format = '{:.2f}'.format
##pd.options.display.max_columns=255
pd.options.display.max_rows=6500000
pd.set_option('display.max_colwidth', 200)
pd.set_option('display.max_columns', 0)
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import pandas as pd
import matplotlib.dates as mpl_dates
import yfinance as yf
import mplfinance as mpf

perda='40d'
intervla='5m'
yy=str(intervla).split('d')[0]
shiftbydays=3



##    g=input("Entr_Signal ticker: ")
perd=perda
intervl=intervla
##    ticker='^NDX'
ticker=['arkk']
##    ticker='MSTR'
##ticker='MRNA'
##ticker='ARKK'


for x in ticker:
    df = yf.download(x, period=perd, interval=intervl,prepost = True)
    

df.dropna() 
df['adx']= ta.ADX(df['High'],df['Low'],df['Close'], timeperiod=14)
df['PLUS_DI']=ta.PLUS_DI(df['High'],df['Low'],df['Close'], timeperiod=14)
df['MINUS_DI']=ta.MINUS_DI(df['High'],df['Low'],df['Close'], timeperiod=14)
##df['adx']= ta.ADX(df['High'],df['Low'],df['Close'], timeperiod=14)
##df['macd'], df['macdsignal'], df['macdhist'] = ta.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)

df['ticker']=''
for x in df.index:
    df['ticker'].loc[x]=ticker
##df=df[50:]    
print(df)



plt.style.use('ggplot')


ap = [
      mpf.make_addplot(df['adx'], type='line', panel=0, ylabel='ADX',color='blue', alpha=0.90),
      mpf.make_addplot(df['PLUS_DI'], type='line', panel=0, ylabel='PLUS_DI',color='green', alpha=0.90),
      mpf.make_addplot(df['MINUS_DI'], type='line', panel=0, ylabel='MINUS_DI',color='red', alpha=0.90)
      ]

s = mpf.make_mpf_style(base_mpl_style='yahoo')

##      mpl.make_addplot(df['Bought'], type='scatter',markersize=200,marker='>', color='#29854f', panel=1),
##      mpl.make_addplot(df['Sold'], type='scatter', marker='<', markersize=200, color='#720c06', panel=1),
##      mpl.make_addplot(df['ATR'], type='line', panel=0, ylabel='ATR', color='#8774AB', secondary_y=False, ylim=(
##          min(df['ATR']), max(df['ATR'])
##      )),
##      mpl.make_addplot(df['Lower B'], type='line', panel=1, color='#3838ea', alpha=0.50),
##      mpl.make_addplot(df['Upper B'], type='line', panel=1, color='#3838ea', alpha=0.50),
##      mpl.make_addplot(df['70'], panel=2, type='line', secondary_y=False, ylim=(0, 100), color='r', alpha=0.25),
##      mpl.make_addplot(df['30'], panel=2, type='line', secondary_y=False, ylim=(0, 100), color='g', alpha=0.25),
##      mpl.make_addplot(df['RSI'], panel=2, type='line', ylabel='RSI', secondary_y=False, ylim=(0, 100)),
##      mpl.make_addplot(df['SMA_20'], panel=1, type='line', alpha=0.5, color='orange'),
##      mpl.make_addplot(df['macdline'], type='line', color='purple', panel=3, secondary_y=False),
##      mpl.make_addplot(df['signalline'], type ='line', color='orange', panel=3, secondary_y=False),
##      mpl.make_addplot(df['hist'], type='bar',panel=3, ylabel='MACD',color='#9c9796'),
##      mpl.make_addplot(df['0'],type='line',panel=3,color='k',secondary_y=False,
##                       ylim=((min(df['signalline']-1), (max(df['signalline']+0.5)))))
      

for x in ticker:
    
    mpf.plot(df, title=x, type='candle',  style=s, ylabel='Price', addplot=ap,figscale=1.1,
             datetime_format='%m-%Y', tight_layout=True, main_panel=1
    ##         ylim=(min(df['Adj Close']-5), max(df['Adj Close']+5)),
    ##         fill_between=dict(y1=df['Lower B'].values, y2=df['Upper B'].values,
                              )
    plt.show()
##



##mpf.plot(df, type='candle', style='charles',
##        title='',
##        ylabel='',
##        ylabel_lower='',
##        volume=True, 
####        mav=(3,6,9), 
####        savefig='test-mplfiance.png'
##         )
