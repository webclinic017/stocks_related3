# Notes for azhar.
# ta_candles6_v3.py is stable.
# ta_candles8_v3.py is the Best version.

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
##print(datetime.today().strftime('%Y-%m-%d'))
import mplfinance
import matplotlib
##from matplotlib.finance import candlestick2_ohlc
##from mpl_finance import candlestick_ohlc
##from mplfinance.original_flavor import candlestick_ohlc
from mplfinance.original_flavor import candlestick_ohlc
from optionprice import Option 
import mplfinance as mpf

##import matplotlib.pyplot as plt
##import matplotlib.ticker as ticker
##import datetime as datetime
##import numpy as np


pd.options.display.float_format = '{:.2f}'.format
pd.options.display.max_columns=255
pd.options.display.max_rows=6500000

pd.options.display.max_rows=9999
pd.options.display.max_columns=36
pd.set_option("display.max_columns", 100)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 200)
pd.set_option('display.max_columns', 0)

def daily(periodb,intervalb,g):
        ##    ticker=input("Entr_Signal stock ticker: ")

    ############################################################    
##    g='ndx'
    ticker=g
    no_of_days=12

    df = pd.DataFrame()


    df=yf.Ticker(g).history(period = periodb, interval = intervalb)
##    customstyle = mpf.make_mpf_style(base_mpf_style='yahoo',
##                                 y_on_right=False,
##                                 facecolor='w')

##    start = dt.datetime.today() - dt.timedelta(no_of_days)
##    end = dt.datetime.today()
##    df = yf.download(ticker, start, end,prepost = True)

    s  = mpf.make_mpf_style(base_mpf_style='yahoo',mavcolors=['#ef5714','#e7d111','#9f4878','#ef5714','#ef5714','#489f93','#ffff00'])

    v = df['Volume'].values
    tp = (df['Low'] + df['Close'] + df['High']).div(3).values
    df = df.assign(vwap=(tp * v).cumsum() / v.cumsum())
    adp = mpf.make_addplot(df['vwap'], type='line')

    ##df.reset_index(inplace=True)
    ##df.set_index('Date')
    mpf.plot(df, block=False,type='candle',addplot=adp, volume=True, figratio=(15, 15), mav=(200,100,50,20,10,5,3),
         title=ticker.upper() +' (Daily) , Price_change '+str('%.2f' % float(df['Close'][-1]-df['Close'][-2]))+
             ' ',
    ##     str(p).split()[1]+' / (diff) '+str(p2).split()[1] + ', Open: '+ str(p5).split()[1] + ' ,low: '+str(p3).split()[1]+ ' ,High: '+ str(p4).split()[1]
    ##     + ', day swing: ' + str(u3).split('.')[0],
             style=s,
         show_nontrading=True)


    ###############################################################
def hourly(periodb,intervalb,g):
##    g='tna'
    ticker=g
##    no_of_days=365

    df = pd.DataFrame()


    df=yf.Ticker(g).history(period = periodb, interval = intervalb)
##    df = yf.download(ticker, period, interval,prepost = True)
    s  = mpf.make_mpf_style(base_mpf_style='yahoo',mavcolors=['#ef5714','#e7d111','#9f4878','#ef5714','#ef5714','#489f93','#ffff00'])


    v = df['Volume'].values
    tp = (df['Low'] + df['Close'] + df['High']).div(3).values
    df = df.assign(vwap=(tp * v).cumsum() / v.cumsum())
    adp = mpf.make_addplot(df['vwap'], type='line')


    mpf.plot(df, block=False,type='candle', addplot=adp,volume=True, figratio=(15, 15), mav=(200,100,50,20,10,5,3),
         title=ticker.upper() +' --> ' +periodb+' '+intervalb +' Price_change '+str('%.2f' % float(df['Close'][-1]-df['Close'][-2])),
    ##     str(p).split()[1]+' / (diff) '+str(p2).split()[1] + ', Open: '+ str(p5).split()[1] + ' ,low: '+str(p3).split()[1]+ ' ,High: '+ str(p4).split()[1]
    ##     + ', day swing: ' + str(u3).split('.')[0],
             style=s,
         show_nontrading=False)

    ############################################################    

    ############################################################

    ###############################################################

    ###############################################################



    ###############################################################

    ###############################################################

    ###############################################################

    ###############################################################

    ############################################################
def xz(periodb,intervalb,p):
    g=p
    ticker=g
##    no_of_days=365

    df = pd.DataFrame()


    df=yf.Ticker(g).history(period = periodb, interval = intervalb)
##    df = yf.download(ticker, period, interval,prepost = True)
##    s  = mpf.make_mpf_style(base_mpf_style='yahoo',mavcolors=['#ef5714','#e7d111','#9f4878','#ef5714','#ef5714','#ff00dd','#1900ff'])
    s  = mpf.make_mpf_style(base_mpf_style='yahoo',mavcolors=['#ef5714','#e7d111','#9f4878','#ef5714','#ef5714','#489f93','#ffff00'])

    df33=yf.Ticker(g).history(period = '3d', interval = '1d')
    cto=df33['Close'][-1]
    c1day=df33['Close'][-2]
##    c10day=df33['Close'][-10]
##    c30day=df33['Close'][-30]

    v = df['Volume'].values
    tp = (df['Low'] + df['Close'] + df['High']).div(3).values
    df = df.assign(vwap=(tp * v).cumsum() / v.cumsum())
    adp = mpf.make_addplot(df['vwap'], type='line')

    mpf.plot(df, block=False,type='candle', addplot=adp,volume=True, figratio=(15, 15), mav=(200,100,50,20,10,5,3),
         title=ticker.upper() +'  '+str(cto.round(2))+'/'+str(c1day.round(2))+'/['+str((cto-c1day).round(2))+'] --> ' +periodb+' '+intervalb +' Price_change '+str('%.2f' % float(df['Close'][-1]-df['Close'][-2])),
    ##     str(p).split()[1]+' / (diff) '+str(p2).split()[1] + ', Open: '+ str(p5).split()[1] + ' ,low: '+str(p3).split()[1]+ ' ,High: '+ str(p4).split()[1]
    ##     + ', day swing: ' + str(u3).split('.')[0],
             style=s,
         show_nontrading=False)


##    mpf.plot(df, block=False,type='candle', volume=True, figratio=(15, 15), mav=(200,100,50,20,10,5,3),
##         title=ticker.upper() +' --> ' +periodb+' '+intervalb +' Price_change '+str('%.2f' % float(df['Close'][-1]-df['Close'][-2])),
##    ##     str(p).split()[1]+' / (diff) '+str(p2).split()[1] + ', Open: '+ str(p5).split()[1] + ' ,low: '+str(p3).split()[1]+ ' ,High: '+ str(p4).split()[1]
##    ##     + ', day swing: ' + str(u3).split('.')[0],
##             style=s,
##         show_nontrading=False)
    

    ############################################################       
gg=['arkf','^ndx','^gspc','^dji','spy','tna','arkk']

##for x in gg:
####    daily('20d','1d',x)
####    daily('5h','5m',x)                                            # best one
##    hourly('1d','5m',x)
##    hourly('2h','1m',x)
    ############################################################  
    
##stocks('30d','1d')
p7=['vg','astr','ispc','mpln','nbev','avya','cei','nvts']
p2=['now','snow','amc','aapl','f','asml','zm']  #miscl
p3=['tsla','nio','plug','lcid','rivn','fsr','blnk']  #ev
p4=['mrna','bntx','nvax','bntx','isrg','biib','pfe','abt']   #covid
p5=['adbe','gme','nvda','nflx','asml','mu','avgo','amd','asml','qcom','mrvl','txn','intc']
p6=['dltr','penn','coin','mstr','uber','lyft','z']
p8=['^ndx','RSX','AUPH']
u2=['BHP', 'DUST', 'EWY', 'NYCB', 'QID', 'SQQQ', 'SVRA', 'AEP']
u3=['bby','zm','dks','anf','dltr','xpev']
gg=['arkf','^ndx','^gspc','^dji','spy','tna','arkk','qqq','tsla']
for x in gg:
##    xz('20d','1d',x)
############    xz('3d','60m',x)
####    xz('2d','30m',x)
##    xz('5h','5m',x)
    xz('120m','1m',x)
##    

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




