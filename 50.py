
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
import mplfinance
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

def hourly(x):
    from numerize import numerize
    import openpyxl

##    perda='635d'
##    intervla='1d'
##    yy=str(intervla).split('d')[0]
##    shiftbydays=3


    perda='2d'
    intervla='5m'

    yy=str(intervla).split('d')[0]
    shiftbydays=3
    ticker=x


    ##    g=input("Entr_Signal ticker: ")
    perd=perda
    intervl=intervla
    
##    ticker='^NDX'
##    ticker='MSTR'
##    ticker='MRNA'

    # [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]



    #df=pd.DataFrame()
    #Interval required 5 minutes
    df = yf.download(ticker, period=perd, interval=intervl,prepost = True)
    df2=pd.DataFrame()



    v = df['Volume'].values
##    tp = (df['Low'] + df['Close'] + df['High']).div(3).values
    tp = (df['Low'] + df['Close'] + df['High'])/(3)
    df = df.assign(vwap=(tp * v).cumsum() / v.cumsum())

   
    df['ticker']=''
    df['EMA_3s']=ta.EMA(df['Close'], timeperiod=3)
    df['EMA_5s']=ta.EMA(df['Close'], timeperiod=5)
    df['EMA_10s']=ta.EMA(df['Close'], timeperiod=10)
    df['EMA_21s']=ta.EMA(df['Close'], timeperiod=21)
    df['EMA_50s']=ta.EMA(df['Close'], timeperiod=50)
    df['EMA_100s']=ta.EMA(df['Close'], timeperiod=100)
    df['EMA_200s']=ta.EMA(df['Close'], timeperiod=200)
    
    df['MOM']=ta.MOM(df['Close'], timeperiod=3)
    df['adx']= ta.ADX(df['High'],df['Low'],df['Close'], timeperiod=14)
    df['PLUS_DI']=ta.PLUS_DI(df['High'],df['Low'],df['Close'], timeperiod=14)
    df['PLUS_DM']=ta.PLUS_DM(df['High'],df['Low'], timeperiod=14)

    df['ULTOSC'] = ta.ULTOSC(df['High'],df['Low'],df['Close'], timeperiod1=7, timeperiod2=14, timeperiod3=28)
    df['STOCHRSI_fastk'], df['STOCHRSI_fastd'] = ta.STOCHRSI(df['Close'], timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
    df['aroondown'],df['aroonup']=ta.AROON(df['High'],df['Low'], timeperiod=14)
    df['PPO']=ta.PPO(df['Close'], fastperiod=12, slowperiod=26, matype=0)
   
    df['Cl>21']=''
    df['21>50']=''
    df['10>21']=''
    df['5>10']=''
    df['color']=''
    df['colorx']=''
    df['clr_bar']=''
    df['Cl>vwap']=''
    df['21>vwap']=''
    df['10>vwap']=''
    df['50>vwap']=''
    df['*']='*'
    df['vwap_trend']=''
    df['adx_trend']=''
    df['5_trend']=''
    df['10_trend']=''
    df['21_trend']=''
    df['50_trend']=''
    df['Cl_del']=''
    df['5_10_signal']=''
    df['10>21_signal']=''
    df['21_50_signal']=''
    df['cl>vwap']=''
    df['5>vwap']=''
    df['50_vwap_sigal']=''
    df['21_vwap_signal']=''
    df['10_vwap_signal']=''
    df['5_vwap_signal']=''
    df['cl_vwap_signal']=''
    df['big']=''
    df['50_vwap_signal']=''


    
##    df=df[133:]
    
    for x in df.index:
        df['ticker'].loc[x]=ticker
        df['macd'], df['macdsignal'], df['macdhist']=ta.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)

        df['Cl_del'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]
        df['5>10'].loc[x]=df['EMA_5s'].loc[x]-df['EMA_10s'].loc[x]
        df['10>21'].loc[x]=df['EMA_10s'].loc[x]-df['EMA_21s'].loc[x]
        df['21>50'].loc[x]=df['EMA_21s'].loc[x]-df['EMA_50s'].loc[x]
        df['10>21'].loc[x]=df['EMA_10s'].loc[x]-df['EMA_21s'].loc[x]
        df['Cl>21'].loc[x]=df['Close'].loc[x]-df['EMA_21s'].loc[x]
        df['color'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
        if df['5>10'].loc[x] > 0:
            df['5_trend'].loc[x]='5_uptrend'
        else: df['5_trend'].loc[x]='5_downtrend'

        if df['10>21'].loc[x] > 0:
            df['10_trend'].loc[x]='10_uptrend'
        else: df['10_trend'].loc[x]='10_downtrend'

            
        if df['color'].loc[x]>0:
            df['colorx'].loc[x]='Green'
        else:
            df['colorx'].loc[x]='Red'
        df['Cl>vwap'].loc[x]=df['Close'].loc[x]-df['vwap'].loc[x]
        if df['Cl>vwap'].loc[x] > 0:
            df['vwap_trend'].loc[x]='vswr/uptrend'
        else:
            df['vwap_trend'].loc[x]='vswr/Downtrend'

        if df['adx'].loc[x] > 25 and df['PLUS_DI'].loc[x] > 20:
            df['adx_trend'].loc[x]='Strong Uptrend'
        elif df['adx'].loc[x] < 25 and df['PLUS_DI'].loc[x] > 20:
            df['adx_trend'].loc[x]='Weak Uptrend/can change direction'
        elif df['adx'].loc[x] > 25 and df['PLUS_DI'].loc[x] < 20:
            df['adx_trend'].loc[x]='Strong Downtrend'
        elif df['adx'].loc[x] < 25 and df['PLUS_DI'].loc[x] < 20:
            df['adx_trend'].loc[x]='Weak Downtrend/can change direction'     
            
            
            
        df['cl>vwap'].loc[x]=df['Close'].loc[x]-df['vwap'].loc[x]
        df['5>vwap'].loc[x]=df['EMA_5s'].loc[x]-df['vwap'].loc[x]  
        df['10>vwap'].loc[x]=df['EMA_10s'].loc[x]-df['vwap'].loc[x]
        df['21>vwap'].loc[x]=df['EMA_21s'].loc[x]-df['vwap'].loc[x]
        df['50>vwap'].loc[x]=df['EMA_50s'].loc[x]-df['vwap'].loc[x]
        df['clr_bar'].loc[x]=abs(df['Close'].loc[x]-df['Open'].loc[x])

        if df['5>10'].loc[x] > 0 and df['5>10'].shift(1).loc[x] < 0:
            df['5_10_signal'].loc[x]='5_10_crossover_UP'
        elif df['5>10'].loc[x] < 0 and df['5>10'].shift(1).loc[x] > 0:
            df['5_10_signal'].loc[x]='5_10_crossover_Down'


        if df['10>21'].loc[x] > 0 and df['10>21'].shift(1).loc[x] < 0:
            df['10>21_signal'].loc[x]='10_21_crossover_UP'
        elif df['10>21'].loc[x] < 0 and df['10>21'].shift(1).loc[x] > 0:
            df['10>21_signal'].loc[x]='10_21_crossover_Down'


        if df['21>50'].loc[x] > 0 and df['21>50'].shift(1).loc[x] < 0:
            df['21_50_signal'].loc[x]='10_21_crossover_UP'
        elif df['21>50'].loc[x] < 0 and df['21>50'].shift(1).loc[x] > 0:
            df['21_50_signal'].loc[x]='21_50_crossover_Down'


        if df['cl>vwap'].loc[x] >  0 and df['cl>vwap'].shift(1).loc[x] < 0:
            df['cl_vwap_signal'].loc[x]='cl_vwap_crossover_UP'
        elif df['cl>vwap'].loc[x] <  0 and df['cl>vwap'].shift(1).loc[x] > 0:
             df['cl_vwap_signal'].loc[x]='cl_vwap_crossover_Down'


        if df['5>vwap'].loc[x] >  0 and df['5>vwap'].shift(1).loc[x] < 0:
            df['5_vwap_signal'].loc[x]='5_vwap_crossover_UP'
        elif df['5>vwap'].loc[x] <  0 and df['5>vwap'].shift(1).loc[x] > 0:
             df['5_vwap_signal'].loc[x]='5_vwap_crossover_Down'


        if df['10>vwap'].loc[x] >  0 and df['10>vwap'].shift(1).loc[x] < 0:
            df['10_vwap_signal'].loc[x]='10_vwap_crossover_UP'

        elif df['10>vwap'].loc[x] <  0 and df['10>vwap'].shift(1).loc[x] > 0:
            df['10_vwap_signal'].loc[x]='10_vwap_crossover_Down'


        if df['21>vwap'].loc[x] >  0 and df['21>vwap'].shift(1).loc[x] < 0:
            df['21_vwap_signal'].loc[x]='21_vwap_crossover_UP'

        elif df['21>vwap'].loc[x] <  0 and df['21>vwap'].shift(1).loc[x] > 0:
            df['21_vwap_signal'].loc[x]='21_vwap_crossover_Down'


        if df['50>vwap'].loc[x] >  0 and df['50>vwap'].shift(1).loc[x] < 0:
            df['50_vwap_signal'].loc[x]='50_vwap_crossover_UP'

        elif df['50>vwap'].loc[x] <  0 and df['50>vwap'].shift(1).loc[x] > 0:
             df['50_vwap_sigal'].loc[x]='50_vwap_crossover_Down'

        if abs(df['Cl_del'].loc[x]-df['Cl_del'].shift(1).loc[x]) > 1:
            df['big'].loc[x]='big $ change'+str(round(df['Cl_del'].loc[x]-df['Cl_del'].shift(1).loc[x],2))
            
            
            
            
 
##    df.reset_index(inplace=True)
##    df['Datetime']=str(df['Datetime'])[0:27]
##    df.set_index('Datetime',inplace=True)

    df3=df[['ticker','colorx','clr_bar','Close', 'Cl_del','5>10','10>21','21>50', 'Cl>21','vwap','Cl>vwap','10>vwap','21>vwap','50>vwap',
           '*','MOM','adx','PLUS_DI','PLUS_DM','STOCHRSI_fastd','aroondown','aroonup','macd','macdsignal','macdhist','PPO','5>vwap']]
    df2=df[['ticker','colorx','clr_bar','Close', 'Cl_del','*','vwap_trend','adx_trend','5_trend','10_trend','ULTOSC','21>50']]

    df4=df[['ticker','colorx','clr_bar','Close', 'Cl_del','*','5_10_signal','10>21_signal','21_50_signal','macd','macdsignal','macdhist']]

    df5=df[['ticker','colorx','clr_bar','Close', 'Cl_del','*','cl_vwap_signal','5_vwap_signal','10_vwap_signal','21_vwap_signal','50_vwap_sigal','big']]




##    print('\n')
##    print(df3.tail(12))
##    print('\n')
##    print(df2.tail(12))
##    print('\n')
##    print(df4.tail(12))
##    print('\n')
##    print(df5.tail(12))
##    print('\n')

    print('\n')
    print(df3,'\n','df3','  ',ticker)
    print(df3[['ticker', 'colorx','clr_bar','Close','Cl_del','Cl>21','Cl>vwap','5>10','MOM']],'\n','kkkk')
##    import matplotlib.pyplot as plt
##    import numpy as np
##    df3.reset_index(inplace=True)
####    plt.plot(df3['Date'],df3['MOM'],'-b',label='MOM')
##    plt.bar(df3['Date'],df3['Cl_del'],color = 'b',width = 1.25,label='Cl_del')
##    plt.bar(df3['Date'],df3['aroonup'],color = 'g',width = .55,label='aroonup')
##    plt.bar(df3['Date'],df3['aroondown'],color = 'r',width = .45,label='aroondown')
##    plt.xticks(None, rotation=44)
####    plt.plot(df3['Date'],df3['Cl_del'],'-r',label='Closed-delta')
##    plt.title("Combined Statistics")
##    plt.legend(loc="upper left")
##    
##    plt.show()

    import matplotlib.pyplot as plt
    import numpy as np
    df3.reset_index(inplace=True)
##    plt.plot(df3['Date'],df3['MOM'],'-b',label='MOM')
    plt.bar(df3['Datetime'],df3['Cl_del'],color = 'b',width = 1.25,label='Cl_del')
##    plt.bar(df3['Date'],df3['aroonup'],color = 'g',width = .55,label='aroonup')
##    plt.bar(df3['Date'],df3['aroondown'],color = 'r',width = .45,label='aroondown')
####    plt.bar(df3['Date'],df3['5>10'],color = 'y',width = .85,label='5>10')
##    plt.bar(df3['Date'],df3['50>vwap'],color = 'y',width = .45,label='50>vwap')
##    plt.bar(df3['Date'],df3['21>50'],color = 'c',width = .45,label='21>50')
##    plt.xticks(None, rotation=44)
##    plt.plot(df3['Date'],df3['Cl_del'],'-r',label='Closed-delta')
    plt.title("Combined Statistics")
    plt.legend(loc="upper left")
    
    plt.show()


    
    print('\n')
    print(df2,'\n','df2','   ',ticker)
    print('\n')
    print(df4,'\n','df4',' MAs > MAs+ MACD  ',ticker)
    print('\n')
    print(df5,'\n','df5 MAs above VWAP','   ',ticker)
    print('\n') 




    

ticker=['ARKK','TSLA','MRNA','BNTX','NVDA','amc','gme']
ticker=['arkk','^ndx','gspc','spy','dji']

p7=['vg','astr','ispc','mpln','nbev','avya','cei','nvts']
p2=['now','snow','amc','aapl','f','asml','zm']  #miscl
p3=['tsla','nio','plug','lcid','rivn','fsr','blnk','rivn']  #ev
p4=['mrna','bntx','nvax','bntx','isrg','biib','pfe','abt']   #covid
p5=['adbe','gme','nvda','nflx','asml','mu','avgo','amd','asml','qcom','mrvl','txn','intc']
p6=['dltr','penn','coin','mstr','uber','lyft','z']
p8=['^ndx','RSX','AUPH']
u2=['BHP', 'DUST', 'EWY', 'NYCB', 'QID', 'SQQQ', 'SVRA', 'AEP']
u3=['bby','zm','dks','anf','dltr','xpev']
gg3=['arkk','^ndx','^gspc','^dji','spy','tna','qqq','tsla','^dji']
gg=['TSLA']

##while True:
##    
##    for x in p4:
##        hourly(x)
##
##    sleep(64)    

for x in gg:
    hourly(x)
    
