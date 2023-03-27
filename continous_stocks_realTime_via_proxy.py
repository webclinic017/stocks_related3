# Notes for azhar.
# ta_candles6_v3.py is stable.
# ta_candles8_v3.py is the Best version.
import sys  #system specific parameters and names
import gc   #garbage collector interface
import talib as ta
import yfinance as yf
import pandas as pd
import datetime as dt
import sys
import re,os,random
import numpy as np
from talib import stream


import datetime
import math

import time
from time import time
import mplfinance
import matplotlib

from mplfinance.original_flavor import candlestick_ohlc
from optionprice import Option 
import mplfinance as mpf
from datetime import datetime





pd.options.display.float_format = '{:.2f}'.format
pd.options.display.max_columns=255
pd.options.display.max_rows=6500000

pd.options.display.max_rows=9999
pd.options.display.max_columns=36
pd.set_option("display.max_columns", 100)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 200)
pd.set_option('display.max_columns', 0)


############################################################    
def xz(periodb,intervalb,p):
    import time
    from time import time
    import re,random,os,requests
    from mplfinance._utils import _construct_vline_collections
    from numerize import numerize
    import warnings
    warnings.filterwarnings("ignore")

    
    ticker=p
    proxies = [
##        'http://138.197.222.35:80',
##        'http://1138.197.222.35:8080'
    '103.105.49.53:80'
    '167.172.248.53:3128',
    '194.226.34.132:5555',
    '203.202.245.62:80',
    '141.0.70.211:8080',
    '118.69.50.155:80',
    '201.55.164.177:3128',
    '51.15.166.107:3128',
    '91.205.218.64:80',
    '128.199.237.57:8080',
    '206.253.164.146:80', 
    '206.253.164.122:80', 
    '206.253.164.101:80', 
    '69.75.122.146:39593', 
    '103.105.49.53:80', 
    '67.201.33.9:25280', 
    '47.254.89.30:7328', 
    '23.251.138.105:8080', 
    '67.201.33.10:25283', 
    '47.56.69.11:8000', 
    '132.145.103.245:8118', 
    '4.53.28.242:80', 
    '47.242.116.120:59394', 
    '47.242.6.186:59394',
    '65.20.187.60:5678', 
    '65.20.155.226:5678', 
    '159.65.69.186:9200', 
    '65.21.183.114:3232', 
    '54.193.134.2:20030', 
    '165.225.114.76:10605', 
    '138.68.18.219:9050', 
    '47.90.132.228:8081', 
    '47.242.86.153:59394', 
    '193.123.227.220:59394', 
    '161.82.252.35:4153', 
    '35.184.126.42:80', 
    '165.225.124.97:10605', 
    '154.212.5.190:5678', 
    '184.105.134.166:48324', 
    '47.242.158.41:8080', 
    '68.183.130.112:19053', 
    '47.242.5.82:5678', 
    '35.232.186.191:3128'

    ]
    
##    for x in range(5):
    proxyb = random.choice(proxies)
    
    df=yf.Ticker(ticker).history(period = periodb, interval = intervalb,prepost = True, proxies=proxyb)
##        print(proxyb,'  ','\n\n',df)
    ##        df=df[['Open', 'High', 'Low', 'Close', 'Volume']]
    df=df[1:]

    df['ticker']=''
    df['delta_price']=''
    df['Vol_delta']=''
    df['Vol_deltan']=''
    dp=pd.DataFrame()
    for x in df.index:
        df['delta_price'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]
        df['ticker'].loc[x]=ticker
        df['Vol_delta'].loc[x]=str((df['Volume'].loc[x]-df['Volume'].shift(1).loc[x])/1000000)+'M'




##    dp=dp.append(df[['ticker','Close','delta_price','Vol_delta']].tail(1))
##        

        
    print(df[['ticker','Close','delta_price','Vol_delta']].tail(1))
##    print(df[['ticker','Close','delta_price','Vol_delta']].tail(1),'\n','    hhh  ','via ip = ',proxyb,'\n')
##    print('ask  (seller)-> ',yf.Ticker(ticker).info['ask'],'/',yf.Ticker(ticker).info['askSize'])
##    print('bid (buyer) -> ',yf.Ticker(ticker).info['bid'],'/',yf.Ticker(ticker).info['bidSize'])
####    print('volume:',(yf.Ticker(ticker).info['averageVolume'])/1000000+'M','/',str(yf.Ticker(ticker).info['volume']/100000)+'M')
##    print('Volume delta:',(yf.Ticker(ticker).info['averageVolume']-yf.Ticker(ticker).info['volume'])/100000)
    now = datetime.now()

##    df=df[['ticker','Close','delta_price','Vol_delta']].tail(1)
##    dp=dp.append(df)
##    print(dp,'\n')
##    print(yf.Ticker(ticker).info)

##
##    
##    

##
##    current_time = now.strftime("%H:%M:%S")
##    print("Current Time =", current_time)
##    if yf.Ticker(ticker).info['bidSize']-yf.Ticker(ticker).info['askSize'] > 0:
##        print('More Buyers ',yf.Ticker(ticker).info['bidSize']-yf.Ticker(ticker).info['askSize'])
##    else:
##        print('More sellers ',yf.Ticker(ticker).info['bidSize']-yf.Ticker(ticker).info['askSize'])
##


##stocks('30d','1d')
p7=['vg','astr','ispc','mpln','nbev','avya','cei','nvts']
p2=['now','snow','amc','aapl','f','asml','zm']  #miscl
p3=['tsla','nio','plug','lcid','rivn','fsr','blnk']  #ev
p4=['mrna','bntx','nvax','bntx','isrg','biib','pfe','abt']   #covid
p77=['qcom','nvda','avgo','qrvo','gfs','tsm']  #semiconductor
p5=['adbe','gme','nvda','nflx','asml','mu','avgo','amd','asml','qcom','mrvl','txn','intc']
p6=['dltr','penn','coin','mstr','uber','lyft','z']
p8=['^ndx','RSX','AUPH']
u2=['BHP', 'DUST', 'EWY', 'NYCB', 'QID', 'SQQQ', 'SVRA', 'AEP']
u3=['bby','zm','dks','anf','dltr','xpev'],
gg=['arkk','^ndx','^gspc','^dji','spy','tna','qqq','tsla','^dji']
butter=['pfe','f','intc','spy']
##s=['btc-usd']
s=['spy','btc-usd','DOCU','tsla','^NDX','SPY','QQQ','^DJI','^GSPC','ARKK','TNA','RUT']
uu=['vg','astr','ispc','mpln','nbev','avya','cei','nvts','now','snow','amc','aapl','f','asml','zm',
    'tsla','nio','plug','lcid','rivn','fsr','blnk','mrna','bntx','nvax','bntx','isrg','biib','pfe','abt',
    'qcom','nvda','avgo','qrvo','gfs','tsm',
    'adbe','gme','nvda','nflx','asml','mu','avgo','amd','asml','qcom','mrvl','txn','intc,dltr','penn','coin','mstr','uber','lyft','z',
    '^ndx','RSX','AUPH','BHP', 'DUST', 'EWY', 'NYCB', 'QID', 'SQQQ', 'SVRA', 'AEP',
    'BHP', 'DUST', 'EWY', 'NYCB', 'QID', 'SQQQ', 'SVRA', 'AEP',
    'bby','zm','dks','anf','dltr','xpev','arkk','^ndx','^gspc','^dji','spy','tna','qqq','tsla','^dji','pfe','f','intc','spy']
    
    
while True:

    for x in s:        
        xz('32d','1d',x)  # works

        if x==s[-1]:
            break
##    break
        ##    xz('200d','1d',x)  # works
        ############    xz('3d','60m',x)   
        ####    xz('2d','30m',x)
        ##    xz('7h','5m',x)   # works
        ##    xz('320m','1m',x)
            
    ##        sleep(62)



















  
########################################################### clear the cache #######################3
import sys  #system specific parameters and names
import gc   #garbage collector interface

memory_usage_by_variable=pd.DataFrame({k:sys.getsizeof(v) for (k,v) in locals().items()},index=['Size'])
memory_usage_by_variable=memory_usage_by_variable.T
memory_usage_by_variable=memory_usage_by_variable.sort_values(by='Size',ascending=False).head(10)
##print(memory_usage_by_variable.head())

def obj_size_fmt(num):
    if num<10**3:
        return "{:.2f}{}".format(num,"B")
    elif ((num>=10**3)&(num<10**6)):
        return "{:.2f}{}".format(num/(1.024*10**3),"KB")
    elif ((num>=10**6)&(num<10**9)):
        return "{:.2f}{}".format(num/(1.024*10**6),"MB")
    else:
        return "{:.2f}{}".format(num/(1.024*10**9),"GB")


def memory_usage():
    memory_usage_by_variable=pd.DataFrame({k:sys.getsizeof(v)\
    for (k,v) in globals().items()},index=['Size'])
    memory_usage_by_variable=memory_usage_by_variable.T
    memory_usage_by_variable=memory_usage_by_variable\
   .sort_values(by='Size',ascending=False).head(10)
    memory_usage_by_variable['Size']=memory_usage_by_variable['Size'].apply(lambda x: obj_size_fmt(x))
    return memory_usage_by_variable

memory_usage()
##print(memory_usage_by_variable)

##print('\n''kaku khan','\n\n')
##
##print('2) gc.get_count()',gc.get_count())
##
##print('3) memory_usage-->: ',memory_usage())
##print('\n\n')
##print('4) gc.collect',gc.collect())
##print('5) gc.get_count() ',gc.get_count())
##print('memory_usage():',memory_usage())
##print('tota hoai baba')
##
##print('--------------------------------------------------','\n\n')
##print('\n')
##print('plotting loop', end4-start4)
##print('mpf plotting time',end3-start3)
##print('read from api/read from y.finance',end2-start2)


##print('--------------------------------------------------','\n\n')

del gg
del xz


#triggering collection
##print('After deleting df,df33,gg ,gc.collect()---',gc.collect())

#finally check memory usage
##print('\n')
##print('After deleting df,df33,gg,memory.usage()',memory_usage())




##['binance',
## 'blueskies',
## ,
## 'charles',
## 'checkers',
## 'classic',
## 'default',
## 'mike',
## 'nightclouds',
## 'sas',
## 'starsandstripes',
## 'yahoo']



######################################################
##import pandas as pd
##import mplfinance as mpf
##import datetime as dt
##import yfinance as yf
##
##
### Load data file.
##g='t'
##ticker=g
##no_of_days=365
##
##df = pd.DataFrame()
##
##
##start = dt.datetime.today() - dt.timedelta(no_of_days)
##end = dt.datetime.today()
##df = yf.download(ticker, start, end,prepost = True)
##
### Plot candlestick.
### Add volume.
### Add moving averages: 3,6,9.
### Save graph to *.png.
##mpf.plot(df, type='candle', style='charles',
##        title='',
##        ylabel='',
##        ylabel_lower='',
##        volume=True, 
##        mav=(200,100,50,20,10,3,5))
##
##
####################################
##import matplotlib.pyplot as plt
##from mpl_finance import candlestick_ohlc
##import pandas as pd
##import matplotlib.dates as mpl_dates
##import yfinance as yf
##import mplfinance as mpf
##
##plt.style.use('ggplot')
##
### Extracting Data for plotting
##df = yf.download('tsla', '2021-01-1','2021-06-28', index=False)
### Plot candlestick.
### Add volume.
### Add moving averages: 3,6,9.
### Save graph to *.png.
##mpf.plot(df, type='candle', style='charles',
##        title='',
##        ylabel='',
##        ylabel_lower='',
##        volume=True, 
##        mav=(3,6,9), 
##        savefig='test-mplfiance.png')





