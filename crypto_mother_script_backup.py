p=['USDBTC-USD', 'USDETH-USD', 'USDBNB-USD', 'USDUSDT-USD', 'USDADA-USD', 'USDSOL1-USD', 'USDXRP-USD', 'USDDOT1-USD', 'USDHEX-USD']

##p=['p5','p7','p9','p77']

uu=''
for x in p:
    uu=uu+str(x)+', '
uu2=uu[:len(uu)-2]
print('ticker=['+uu2+']')
print('\n\n')


k=0
for x in p:
    print('df'+str(k)+'= yf.download(ticker[' + str(k) +'], period=perd, interval=intervl,prepost = True)')
    k=k+1

print('\n\n')

    
k=0
for x in p:
    print('df'+str(k)+'.reset_index()')
    k=k+1
    
print('\n\n')
    
k=0
for x in p:
    print('df'+str(k)+"['xx']=''")
    print('for x in df'+str(k)+'.index:')
    print('    df'+str(k)+"['xx'].loc[x]=ticker["+str(k)+']')
    print('df'+str(k)+'=pd.DataFrame(df'+str(k)+",columns=('xx','Close','Volume'))")      
    print('df'+str(k)+".columns=['xx',ticker["+str(k)+"]+'_'+'Close',ticker["+str(k)+"]+'_'+'Volume']")      
    k=k+1
    print('\n')


dd=''
k=0
for x in  p:
    dd=dd+'df'+str(k)+' ,'
    k=k+1

f=dd[:len(dd)-1]
print(f)
cc='dfa=pd.concat(['+f+'],axis=1)'
print(cc)
print('print(dfa)')

######################################################################################################################################
'''
perda='635d'
intervla='1d'
yy=str(intervla).split('d')[0]
shiftbydays=3
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



##    g=input("Entr_Signal ticker: ")
perd=perda
intervl=intervla
##    ticker='BTC-USD'
##    ticker='^NDX'
##    ticker='MSTR'
##    ticker='MRNA'
##    ticker='AMZN'
##    ticker='TSLA'
ticker=['HIVE-USD','JDC-USD','DOGE-USD']
# [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]

print(ticker[2])

#df=pd.DataFrame()
#Interval required 5 minutes
df2 = yf.download(ticker[0], period=perd, interval=intervl,prepost = True)
df3 = yf.download(ticker[1], period=perd, interval=intervl,prepost = True)
df4 = yf.download(ticker[2], period=perd, interval=intervl,prepost = True)
df2.reset_index()
df3.reset_index()
df4.reset_index()

print(ticker[0],ticker[1],ticker[2])
###########################################
df2['xx']=''
for x in df2.index:
    df2['xx'].loc[x]=ticker[0]
df2=pd.DataFrame(df2,columns=('xx','Close','Volume'))
df2.columns=['xx',ticker[0]+'_'+'Close',ticker[0]+'_'+'Volume']
##################3
df3['xx']=''
for x in df3.index:
    df3['xx'].loc[x]=ticker[1]
df3=pd.DataFrame(df3,columns=('xx','Close','Volume'))
df3.columns=['xx',ticker[1]+'_'+'Close',ticker[1]+'_'+'Volume']
##################3
df4['xx']=''
for x in df4.index:
    df4['xx'].loc[x]=ticker[2]
df4=pd.DataFrame(df4,columns=('xx','Close','Volume'))
df4.columns=['xx',ticker[2]+'_'+'Close',ticker[2]+'_'+'Volume']
##print(df4)
##################3



dfa=pd.concat([df2,df3,df4],axis=1)
print(dfa)
sys.exit()
'''
