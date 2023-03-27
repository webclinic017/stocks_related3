import talib as ta
from ta.utils import dropna
import yfinance as yf
import pandas as pd
import sys
import re
import numpy as np
from talib import stream
##from matplotlib import dates
##import matplotlib.pyplot as plt
####from datetime import date
####today = date.today().isoformat()
import datetime
import math
##import matplotlib.pyplot as plt
##import matplotlib.pyplot as plt2
##plt.style.use('fivethirtyeight')
##from millify import millify
##today = datetime.date.today() + datetime.timedelta(days=1)
today = datetime.date.today()
##day = datetime.datetime.strptime(Date, '%d %m %Y').weekday()
##print(datetime.today().strftime('%Y-%m-%d'))
import mpl_finance
##import matplotlib
import sys
##from matplotlib.finance import candlestick2_ohlc
##from mpl_finance import candlestick_ohlc
##from mplfinance.original_flavor import candlestick_ohlc
##from mplfinance.original_flavor import candlestick_ohlc
##from optionprice import Option
##from numerize import numerize
##import matplotlib.pyplot as plt
pd.options.display.width = 0
pd.set_option('display.max_columns', None)
pd.options.display.float_format = '{:.2f}'.format
##pd.options.display.max_columns=255
pd.options.display.max_rows=6500000
pd.set_option('display.max_colwidth', 500)
pd.set_option('display.max_columns', 550)
pd.options.mode.chained_assignment = None  # default='warn'
import time
import pandas_datareader as web
import datetime as dt



while True:
        
    def days():
        import sys
        import time
        

        start=time.time()

        
        perda='1d'
        intervla='2m'
##        yy=str(intervla).split('d')[0]
##        shiftbydays=3



        ##    g=input("Entr_Signal ticker: ")
        perd=perda
        intervl=intervla
        tickerb=['BTC-USD','ETH-USD','SOL1-USD','USDT-USD','BNB-USD','ADA-USD',]
    ##    ticker='^NDX'
    ##    ticker='spx'
    ##    ticker='tna'
    ##    ticker='arkk'
    ##    ticker='spy'
    ##    ticker='spx'
        
    ##    ticker='MSTR'
    ##    ticker='COIN'
        
    ##    ticker='AMZN'
    ##    ticker='NVDA'
    ##    ticker='DOCU'
    ##    ticker='adbe'
    ##    ticker='shop'
    ##    ticker='car'


    ##    ticker='NOW'
    ##    ticker='amc'

    ##    ticker='zm'
    ##    ticker='asml'
    ##    ticker='isrg'
    ##    ticker='asml'
    ##    ticker='pton'

    ##    ticker='jd'
    ##    ticker='avgo'
    ##    ticker='nvda'
    ##    ticker='spce'
    ##    ticker='adbe'
    ##    ticker='bbcp'
    ##    ticker='now'
    ##    ticker='snow'
    ##    ticker='nvda'
    ##    ticker='xlnx'

    #vaccine
    ##    ticker='MRNA'
    ##    ticker='bntx'
    ##    ticker='nvax'
    ##    ticker='azn'
        
        # [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]
        k=0
        for x in tickerb:
            
            
            ticker=tickerb[k]
            print(ticker)
            bb(ticker,perda,intervl)
            k=k+1
        sys.exit

    def bb(ticker,perda,intervl):
##        from alpha_vantage.timeseries import TimeSeries
##        ts = TimeSeries(key='MUY7K7XOWL48HELB', output_format='pandas')
##        ts.get_intraday(symbol='NDX',interval='hourly',outputsize='full'


        df = yf.download(ticker, period=perda, interval=intervl,prepost = True)
        df=pd.DataFrame(df)
        print('############################## end of ', ticker,' #######################################################')
##        print('\n\n\n')   
##
##        print(ticker,df[['Close','Open','Low','High']].tail(6),' from start')
##        
##        df=df[:df.shape[0]-1]
##        print(df.shape,'after')
##        print(df[['Close','Open','Low','High']].tail(6),' from start_lastrow rmv')

        print('==========',ticker,' running ===========')

        
        df2=pd.DataFrame()
        df['*']=''
        df['Candlea']=''

            
    ##    df['EMA_3']=df['Close']-ta.EMA(df['Close'], timeperiod=3)
##        df['EMA_5']=df['Close']-ta.EMA(df['Close'], timeperiod=5)
##        df['EMA_10']=df['Close']-ta.EMA(df['Close'], timeperiod=10)
##        df['EMA_21']=df['Close']-ta.EMA(df['Close'], timeperiod=21)
##        df['EMA_50']=df['Close']-ta.EMA(df['Close'], timeperiod=50)
##        df['EMA_100']=df['Close']-ta.EMA(df['Close'], timeperiod=100)
##        df['EMA_200']=df['Close']-ta.EMA(df['Close'], timeperiod=200)


        df['EMA_5']=ta.EMA(df['Close'], timeperiod=5)
        df['EMA_10']=ta.EMA(df['Close'], timeperiod=10)
        df['EMA_21']=ta.EMA(df['Close'], timeperiod=21)
        df['EMA_50']=ta.EMA(df['Close'], timeperiod=50)
        df['EMA_100']=ta.EMA(df['Close'], timeperiod=100)
        df['EMA_200']=ta.EMA(df['Close'], timeperiod=200)


        df['5_10_Crossovr']=''
        df['5_21_Crossovr']=''
        df['5_50_Crossovr']=''
        df['5_100_Crossovr']=''
        df['5_200_Crossovr']=''

        df['10_21_Crossovr']=''
        df['21_50_Crossovr']=''
        df['50_100_Crossovr']=''
        df['100_200_Crossovr']=''

        df['*5_10_signal']=''
        df['*5_21_signal']=''
        df['*5_50_signal']=''
        df['*5_100_signal']=''
        df['*5_200_signal']=''
        df['10_21_Crossovr_signal']=''
        df['50_100_signal']=''
        df['100_200_signal']=''
        df['ticker']=''
        
        
        

        for x in df.index:
            df['ticker'].loc[x]=ticker
            df['5_10_Crossovr'].loc[x]=df['EMA_5'].loc[x]-df['EMA_10'].loc[x]
            df['5_21_Crossovr'].loc[x]=df['EMA_5'].loc[x]-df['EMA_21'].loc[x]
            df['5_50_Crossovr'].loc[x]=df['EMA_5'].loc[x]-df['EMA_50'].loc[x]
            df['5_100_Crossovr'].loc[x]=df['EMA_5'].loc[x]-df['EMA_100'].loc[x]
            df['5_200_Crossovr'].loc[x]=df['EMA_5'].loc[x]-df['EMA_200'].loc[x]

            df['10_21_Crossovr'].loc[x]=df['EMA_10'].loc[x]-df['EMA_21'].loc[x]
            df['21_50_Crossovr'].loc[x]=df['EMA_21'].loc[x]-df['EMA_50'].loc[x]
            df['50_100_Crossovr'].loc[x]=df['EMA_50'].loc[x]-df['EMA_100'].loc[x]
            df['100_200_Crossovr'].loc[x]=df['EMA_100'].loc[x]-df['EMA_200'].loc[x]


        cc_buy=[]
        cc_sell=[]
        for x in df.index:
            
            if df['5_10_Crossovr'].loc[x] > 0:
                if df['5_10_Crossovr'].shift(1).loc[x] < 0:
                    df['*5_10_signal'].loc[x]='5_10_buy'
                    cc_buy.append(x)
                elif df['5_10_Crossovr'].shift(1).loc[x] > 0:
                    pass
            elif df['5_10_Crossovr'].loc[x] < 0:
                if df['5_10_Crossovr'].shift(1).loc[x] > 0:
                    df['*5_10_signal'].loc[x]='5_10_sell'
                    cc_sell.append(x)
                elif  df['5_10_Crossovr'].shift(1).loc[x] < 0:
                    pass


            if df['5_21_Crossovr'].loc[x] > 0 and df['5_21_Crossovr'].shift(1).loc[x] < 0:
                df['*5_21_signal'].loc[x]='5_21_buy'
            else:
                df['*5_21_signal'].loc[x]='5_21_sell'


            if df['5_50_Crossovr'].loc[x] > 0 and df['5_50_Crossovr'].shift(1).loc[x] < 0:
               df['*5_50_signal'].loc[x]='5_50_buy'
            else:
                df['*5_50_signal'].loc[x]='5_50_sell'


            if df['5_100_Crossovr'].loc[x] > 0 and df['5_100_Crossovr'].shift(1).loc[x] < 0:
               df['*5_100_signal'].loc[x]='5_100_buy'
            else:
                df['*5_100_signal'].loc[x]='5_100_sell'

            if df['5_200_Crossovr'].loc[x] > 0 and df['5_200_Crossovr'].shift(1).loc[x] < 0:
               df['*5_200_signal'].loc[x]='5_200_buy'
            else:
                df['*5_200_signal'].loc[x]='5_200_sell'
    #######################################################

            if df['10_21_Crossovr'].loc[x] > 0:
                if df['10_21_Crossovr'].shift(1).loc[x] < 0:
                    df['10_21_Crossovr_signal'].loc[x]='10_21_Crossovr_buy'
            elif df['10_21_Crossovr'].loc[x] < 0:
                if df['10_21_Crossovr'].shift(1).loc[x] > 0:
                    df['10_21_Crossovr_signal'].loc[x]='10_21_Crossovr_sell'

            if df['50_100_Crossovr'].loc[x] > 0:
                if df['50_100_Crossovr'].shift(1).loc[x] < 0:
                    df['50_100_signal'].loc[x]='50_100_buy'
            elif df['50_100_Crossovr'].loc[x] < 0:
                if df['50_100_Crossovr'].shift(1).loc[x] > 0:
                    df['50_100_signal'].loc[x]='50_100_sell'

            if df['100_200_Crossovr'].loc[x] > 0:
                if df['100_200_Crossovr'].shift(1).loc[x] < 0:
                    df['100_200_signal'].loc[x]='100_200_buy'
            elif df['100_200_Crossovr'].loc[x] < 0:
                if df['100_200_Crossovr'].shift(1).loc[x] > 0:
                    df['100_200_signal'].loc[x]='100_200_sell'

                

        
        a=len(cc_buy)
        b=len(cc_sell)
        print(ticker,' ---->  ''buys=',a,'   sells=',b)
        if a > b:
            print('mm')
        else:
            print('ggg')
    #****************************************************************** 
        x=df.shape[0]-1

##        print(df[['ticker','Close','Open','Low','High','ticker','EMA_5','5_10_Crossovr','*5_10_signal']][-1:],'\n','55pppppppp')
##        print('\n')
##
##
##
##        print('Current last record,ticker=',ticker,'Close price=',df['Close'][-1],\
##              'Open=',df['Open'][-1],' Close=',df['Close'][-1],' Candle=',df['Close'][-1]-df['Open'][-1]
##              )

    #*****************************************************************
        if df['*5_10_signal'][-1] != '':
            print(df['*5_10_signal'][-1],'======================================================>') 
            g=open('/home/az2/Downloads/ohwell.txt','a+')
            g.write(str(df['*5_10_signal'][-1]))
            g.write('  ')
            g.write(ticker)
            g.write('  ')
            g.write(str(df['Close'][-1]))
            g.write('  ')
##            g.write(str(df[-1]))
            g.write('\n')
            g.close()    
    #******************************************************************    
        print(ticker,' signal details','\n')
    
        if df['EMA_5'][-1] > df['EMA_10'][-1]:
            print(ticker, ' EMA5 > EMA10  Buy ',df['EMA_5'][-1],'/',df['EMA_10'][-1],'/ diff=',float(df['EMA_5'][-1])-float(df['EMA_10'][-1]))    
        elif df['EMA_5'][-1] < df['EMA_10'][-1]:          
            print('EMA5 < EMA10  Sell ------------------',df['EMA_5'][-1],'/',df['EMA_10'][-1],'/ diff=',float(df['EMA_10'][-1])-float(df['EMA_5'][-1]))        

        if df['EMA_10'][-1] > df['EMA_21'][-1]:
            print(ticker, ' EMA10 > EMA21  Buy ',df['EMA_10'][-1],'/',df['EMA_21'][-1],'/ diff=',float(df['EMA_10'][-1])-float(df['EMA_21'][-1]))    
        elif df['EMA_10'][-1] < df['EMA_21'][-1]:   
            print('EMA10 < EMA21  Sell ------------------',df['EMA_10'][-1],'/',df['EMA_21'][-1],'/ diff=',float(df['EMA_21'][-1])-float(df['EMA_10'][-1]))        

        if df['EMA_21'][-1] > df['EMA_50'][-1]:
            print(ticker, ' EMA21 > EMA50  Buy ',df['EMA_21'][-1],'/',df['EMA_50'][-1],'/ diff=',float(df['EMA_21'][-1])-float(df['EMA_50'][-1]))    
        elif df['EMA_21'][-1] < df['EMA_50'][-1]:   
            print('EMA21 < EMA50  Sell ------------------',df['EMA_21'][-1],'/',df['EMA_50'][-1],'/ diff=',float(df['EMA_50'][-1])-float(df['EMA_21'][-1]))        

        if df['EMA_50'][-1] > df['EMA_100'][-1]:
            print(ticker, ' EMA50 > EMA100  Buy ',df['EMA_50'][-1],'/',df['EMA_100'][-1],'/ diff=',float(df['EMA_50'][-1])-float(df['EMA_100'][-1]))    
        elif df['EMA_50'][-1] < df['EMA_100'][-1]:   
            print('EMA50 < EMA100  Sell ------------------',df['EMA_50'][-1],'/',df['EMA_100'][-1],'/ diff=',float(df['EMA_100'][-1])-float(df['EMA_50'][-1]))        

        if df['EMA_100'][-1] > df['EMA_200'][-1]:
            print(ticker, ' EMA100 > EMA200  Buy ',df['EMA_100'][-1],'/',df['EMA_200'][-1],'/ diff=',float(df['EMA_100'][-1])-float(df['EMA_200'][-1]))    
        elif df['EMA_100'][-1] < df['EMA_200'][-1]:   
            print('EMA100 < EMA200  Sell ------------------',df['EMA_100'][-1],'/',df['EMA_200'][-1],'/ diff=',float(df['EMA_200'][-1])-float(df['EMA_100'][-1]))     
            
##        print(df[['Close','Open']].tail(4),'end of the road')
        print('############################## end of ', ticker,' #######################################################')
        print('\n\n\n')   

    days()
    time.sleep(130)
