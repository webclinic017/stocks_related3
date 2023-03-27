'''
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
'''
######################################################################################################################################

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


ticker=['ETH-USD', 'ETH-USD','BNB-USD', 'USDT-USD','ADA-USD', 'SOL1-USD', 'XRP-USD', 'DOT1-USD', 'HEX-USD']
perd='35d'
intervl='1d'


df0= yf.download(ticker[0], period=perd, interval=intervl,prepost = True)
df1= yf.download(ticker[1], period=perd, interval=intervl,prepost = True)
df2= yf.download(ticker[2], period=perd, interval=intervl,prepost = True)
df3= yf.download(ticker[3], period=perd, interval=intervl,prepost = True)
df4= yf.download(ticker[4], period=perd, interval=intervl,prepost = True)
df5= yf.download(ticker[5], period=perd, interval=intervl,prepost = True)
df6= yf.download(ticker[6], period=perd, interval=intervl,prepost = True)
df7= yf.download(ticker[7], period=perd, interval=intervl,prepost = True)
df8= yf.download(ticker[8], period=perd, interval=intervl,prepost = True)



df0.reset_index()
df1.reset_index()
df2.reset_index()
df3.reset_index()
df4.reset_index()
df5.reset_index()
df6.reset_index()
df7.reset_index()
df8.reset_index()



df0['xx']=''
for x in df0.index:
    df0['xx'].loc[x]=ticker[0]
df0=pd.DataFrame(df0,columns=('xx','Close','Volume'))
df0.columns=['xx',ticker[0]+'_'+'Close',ticker[0]+'_'+'Volume']


df1['xx']=''
for x in df1.index:
    df1['xx'].loc[x]=ticker[1]
df1=pd.DataFrame(df1,columns=('xx','Close','Volume'))
df1.columns=['xx',ticker[1]+'_'+'Close',ticker[1]+'_'+'Volume']


df2['xx']=''
for x in df2.index:
    df2['xx'].loc[x]=ticker[2]
df2=pd.DataFrame(df2,columns=('xx','Close','Volume'))
df2.columns=['xx',ticker[2]+'_'+'Close',ticker[2]+'_'+'Volume']


df3['xx']=''
for x in df3.index:
    df3['xx'].loc[x]=ticker[3]
df3=pd.DataFrame(df3,columns=('xx','Close','Volume'))
df3.columns=['xx',ticker[3]+'_'+'Close',ticker[3]+'_'+'Volume']


df4['xx']=''
for x in df4.index:
    df4['xx'].loc[x]=ticker[4]
df4=pd.DataFrame(df4,columns=('xx','Close','Volume'))
df4.columns=['xx',ticker[4]+'_'+'Close',ticker[4]+'_'+'Volume']


df5['xx']=''
for x in df5.index:
    df5['xx'].loc[x]=ticker[5]
df5=pd.DataFrame(df5,columns=('xx','Close','Volume'))
df5.columns=['xx',ticker[5]+'_'+'Close',ticker[5]+'_'+'Volume']


df6['xx']=''
for x in df6.index:
    df6['xx'].loc[x]=ticker[6]
df6=pd.DataFrame(df6,columns=('xx','Close','Volume'))
df6.columns=['xx',ticker[6]+'_'+'Close',ticker[6]+'_'+'Volume']


df7['xx']=''
for x in df7.index:
    df7['xx'].loc[x]=ticker[7]
df7=pd.DataFrame(df7,columns=('xx','Close','Volume'))
df7.columns=['xx',ticker[7]+'_'+'Close',ticker[7]+'_'+'Volume']


df8['xx']=''
for x in df8.index:
    df8['xx'].loc[x]=ticker[8]
df8=pd.DataFrame(df8,columns=('xx','Close','Volume'))
df8.columns=['xx',ticker[8]+'_'+'Close',ticker[8]+'_'+'Volume']


df0 ,df1 ,df2 ,df3 ,df4 ,df5 ,df6 ,df7 ,df8 
dfa=pd.concat([df0 ,df1 ,df2 ,df3 ,df4 ,df5 ,df6 ,df7 ,df8 ],axis=1)
print(dfa)
sys.exit()

