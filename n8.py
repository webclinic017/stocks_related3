#!/usr/bin/python
import ccxt,sys
import time
##################################################################################################################################
##################################################################################################################################
def bb33(ticker,df,trash,pass2,garbage,df6):

    #df6 is daily data
    #df is per min
    
    import datetime
    import talib as ta
    from ta.utils import dropna
    import yfinance as yf
    import pandas as pd
    import sys
    import re
    import numpy as np
    import numerize 
    from talib import stream
    import mpl_finance
    from numerize import numerize
    ##from matplotlib import dates
    ##import matplotlib.pyplot as plt
    ####from datetime import date
    ####today = date.today().isoformat()
    import datetime
    import math
##        from alpha_vantage.timeseries import TimeSeries
##        ts = TimeSeries(key='MUY7K7XOWL48HELB', output_format='pandas')
##        ts.get_intraday(symbol='NDX',interval='hourly',outputsize='full'

##
##    df = yf.download(ticker, period=perda, interval=intervl,prepost = True)
##    df=pd.DataFrame(df)


##    print(ticker)
##    sys.exit()

    print('############################## end of ', ticker,' #######################################################')

    df6['Volumeb']=''
    for x in df6.index:
        df6['ticker'].loc[x]=ticker
        df6['Volumeb'].loc[x]=numerize.numerize(np.float64(df6['Volume'].loc[x]).item())
##    print(df6,'Daily --------------------------------------------------',ticker)
###############################################################################################################
    volume_check=sum(df6['Volume'])/df6.shape[0]
    print('rows=',df6.shape[0])
    print('   from bb33 -------------------74----')
##    if int(volume_check) > int(2000000):
##        print('Average volume in last ',df6.shape[0], 'days =',numerize.numerize(volume_check),'     ',ticker)
        
        
###############################################################################################################        



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

            

    print(df,'ssssss (1 min) '+ticker)
    a=len(cc_buy)  # Buy signal array
    b=len(cc_sell)  # sell signal array
    print(ticker,' ---->  ''buys=',a,'   sells=',b)
    if a > b:
        print('added to Buy signal array')
    else:
        print('added to sell signal array')
#****************************************************************** 
##    x=df.shape[0]-1

##        print(df[['ticker','Close','Open','Low','High','ticker','EMA_5','5_10_Crossovr','*5_10_signal']][-1:],'\n','55pppppppp')
##        print('\n')
##
##
##
##        print('Current last record,ticker=',ticker,'Close price=',df['Close'][-1],\
##              'Open=',df['Open'][-1],' Close=',df['Close'][-1],' Candle=',df['Close'][-1]-df['Open'][-1]
##              )

#*****************************************************************
    print(df,'ttttttttt (1 min) '+ticker)
    c88=df.shape[0]-1
##    c44=df.columns.get_loc('*5_10_signal')
##    df5=df['*5_10_signal']
##    print(df['*5_10_signal'][c88],'# of rows')
##    print(df5.iloc[-1],'# of rows')
##    print(df[7],'dddd')
##    print(df[-1],'ggggg')
##    print(df['*5_10_signal'][x])
##    sys.exit()
##    if df5.iloc[-1] != '':
################### delete me
    k4=0
    g3=open('/home/az2/Downloads/ohwell3332.txt','a+')
    g3.write('k4')
    g3.write('\n')
    k4=k4+1
    g3.close()
################
    if df['*5_10_signal'][c88] != '':   
        print(df['*5_10_signal'][c88],'======================================================>') 
        g=open('/home/az2/Downloads/ohwell333.txt','a+')
        g.write(str(df['*5_10_signal'][c88]))
        g.write('  ')
        g.write(ticker)
        g.write('   close=')
        g.write(str(df['Close'][c88]))
        g.write('  ')
        g.write('  EMA_5/10=')
        g.write(str((df['EMA_5'][c88]-df['EMA_10'][c88]).round(2)))
        g.write('  ')
        g.write(str(df['Time'][c88]))
        g.write('  volume=')
        g.write(str(df['Volume'].mean().round(2)))
        g.write('  open=')
        g.write(str(df['Open'][c88].round(3)))
        g.write(' close=')
        g.write(str(df['Close'][c88].round(3)))
        g.write('  low=')
        g.write(str(df['Low'][c88].round(3)))
        g.write('  high=')
        g.write(str(df['High'][c88].round(3)))  
                
##            g.write(str(df[-1]))
        g.write('\n')
        g.close()    
#******************************************************************
   
    print('=================================================================================================77777777')    
    print(ticker,'   ',c88,'   @time ',df['Time'][c88],'    signal details','\n')
    c88=df.shape[0]-1
    print('at time latest 1min record =============================================:',df['Time'][c88])
##    print()
##    print(df['EMA_5'][c88])
##    sys.exit()
    if df['EMA_5'][c88] > df['EMA_10'][c88]:
        print(ticker, ' EMA5 > EMA10  Buy ',df['EMA_5'][c88],'/',df['EMA_10'][c88],'/ diff=',float(df['EMA_5'][c88])-float(df['EMA_10'][c88]))    
    elif df['EMA_5'][c88] < df['EMA_10'][c88]:          
        print('EMA5 < EMA10  Sell ------------------',df['EMA_5'][c88],'/',df['EMA_10'][c88],'/ diff=',float(df['EMA_10'][c88])-float(df['EMA_5'][c88]))

####    sys.exit()    
    if df['EMA_10'][c88] > df['EMA_21'][c88]:
        print(ticker, ' EMA10 > EMA21  Buy ',df['EMA_10'][c88],'/',df['EMA_21'][c88],'/ diff=',float(df['EMA_10'][c88])-float(df['EMA_21'][c88]))    
    elif df['EMA_10'][c88] < df['EMA_21'][c88]:   
        print('EMA10 < EMA21  Sell ------------------',df['EMA_10'][c88],'/',df['EMA_21'][c88],'/ diff=',float(df['EMA_21'][c88])-float(df['EMA_10'][c88]))        

    if df['EMA_21'][c88] > df['EMA_50'][c88]:
        print(ticker, ' EMA21 > EMA50  Buy ',df['EMA_21'][c88],'/',df['EMA_50'][c88],'/ diff=',float(df['EMA_21'][c88])-float(df['EMA_50'][c88]))    
    elif df['EMA_21'][c88] < df['EMA_50'][c88]:   
        print('EMA21 < EMA50  Sell ------------------',df['EMA_21'][c88],'/',df['EMA_50'][c88],'/ diff=',float(df['EMA_50'][c88])-float(df['EMA_21'][c88]))        

    if df['EMA_50'][c88] > df['EMA_100'][c88]:
        print(ticker, ' EMA50 > EMA100  Buy ',df['EMA_50'][c88],'/',df['EMA_100'][c88],'/ diff=',float(df['EMA_50'][c88])-float(df['EMA_100'][c88]))    
    elif df['EMA_50'][c88] < df['EMA_100'][c88]:   
        print('EMA50 < EMA100  Sell ------------------',df['EMA_50'][c88],'/',df['EMA_100'][c88],'/ diff=',float(df['EMA_100'][c88])-float(df['EMA_50'][c88]))        

    if df['EMA_100'][c88] > df['EMA_200'][c88]:
        print(ticker, ' EMA100 > EMA200  Buy ',df['EMA_100'][c88],'/',df['EMA_200'][c88],'/ diff=',float(df['EMA_100'][c88])-float(df['EMA_200'][c88]))    
    elif df['EMA_100'][c88] < df['EMA_200'][c88]:   
        print('EMA100 < EMA200  Sell ------------------',df['EMA_100'][c88],'/',df['EMA_200'][c88],'/ diff=',float(df['EMA_200'][c88])-float(df['EMA_100'][c88]))     
        
##        print(df[['Close','Open']].tail(4),'end of the road')
    print('############################## end of ', ticker,' #######################################################')
    print('\n\n\n')
    print('trashed tickers=',trash,'   pass2 tickers=',pass2,'  total_tickers=',(trash+pass2))
    print('garbage tickers=',garbage)
    print('\n\n\n')







def bb(x):
    import pandas as pd
    from datetime import datetime
    import json,sys
    import numpy as np
    from numerize import numerize
    import calendar
    
    binance = ccxt.binanceus()

################ adding daily data ###################
##    now = datetime.utcnow()
##    unixtime = calendar.timegm(now.utctimetuple())

##    now = datetime.utcnow()
##    unixtime = calendar.timegm(now.utctimetuple()
    
    df6b = binance.fetch_ohlcv(str(x),'1d',limit=10)

##    pd.to_datetime(str(df6b['Time']), format='%Y%m%d', errors='ignore')
    df6 = pd.DataFrame(df6b, columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume'])


    df6['Time']=pd.to_numeric(df6['Time'])

##    print(type(df6b['Time']))
    df6['Time'] = pd.to_datetime(df6['Time'],unit='ms')
##    print(df6['Time'])
##    sys.exit()

    
    df6.reset_index(inplace=True)
    df6['ticker']=''
##    df6['Volumeb']=''
##    for x in df6.index:
##        df6['Volumeb'].loc[x]=numerize.numerize(np.float64(df6['Volume'].loc[x]).item())
    ##for x in df.index:
    ##            df['Volume'].loc[x]=numerize.numerize(np.float32(df['Volume'].loc[x]).item())

        
    df6=df6[['ticker','Time', 'Open', 'High', 'Low', 'Close', 'Volume']]
##    print(df6,'Daily data')
###################################################  


    

    now = datetime.utcnow()
    unixtime = calendar.timegm(now.utctimetuple())
    since = (unixtime - 60*60) * 1000 # UTC timestamp in milliseconds
##    ticker='ETH/BTC'
    ticker=x
    ohlcv = binance.fetch_ohlcv(str(x),'1m',limit=80)
##    ohlcv = binance.fetch_ohlcv(symbol='ETH/BTC', timeframe='1d', since=since, limit=3)
    start_dt = datetime.fromtimestamp(ohlcv[0][0]/1000)
    end_dt = datetime.fromtimestamp(ohlcv[-1][0]/1000)
##    print(ohlcv)
    # convert it into Pandas DataFrame
    

    df = pd.DataFrame(ohlcv, columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume'])
    df['Time'] = [datetime.fromtimestamp(float(time)/1000) for time in df['Time']]
    df.set_index('Time', inplace=True)
    ##print(df)
    df.reset_index(inplace=True)

    
    df['ticker']=''
    for x in df.index:
        df['ticker'].loc[x]=ticker
    df=df[['ticker','Time', 'Open', 'High', 'Low', 'Close', 'Volume']]

  
    
################################################################# checking for tickers with garbage data
    trash=0
    pass2=0
    df5=df.tail(6)
    df5['v2']=''
    df5['v3']=''
    df5['v4']=''
##    print(df5,'kkkkkkk')

    
    
##    g8=open('/home/az2/Downloads/ohwell333g.txt','a+') 
    for x in df5.index:
        df5['v2'].loc[x]=df5['Open'].loc[x]-df5['Close'].loc[x]
        df5['v3'].loc[x]=df5['Low'].loc[x]-df5['High'].loc[x]
        df5['v4'].loc[x]=df5['Low'].loc[x]-df5['Open'].loc[x]
##    print(df5[['v2','v3','v4']],'vs info')
    
##
    c89=df5.shape[0]-1
##
    garbage=[]
    for x in df5.index:
        if (df5['v2'].loc[x]==df5['v3'].loc[x]) and (df5['v2'].loc[x]==df5['v4'].loc[x]):
            trash=trash+1
            garbage.append(str(df5['ticker']))
##            g8.write(str(df5['ticker'][c89]))
##            g8.write('\n')
##            g8.close()
            break
        else:
##            print(df,'dataset from bb(x) funct')
            pass2=pass2+1
            bb33(ticker,df,trash,pass2,garbage,df6) #---------------------------------------------------------------------------------------------------
            
##        
##    
 ########################################################################################################### checking        
##    print(df,'dataset from bb(x) funct')
##    bb33(ticker,df) ##============================================================================>>>
##################################################################################################################################







    
# https://itnext.io/getting-started-with-ccxt-crypto-exchange-library-and-python-93175d5a898d
##    btc_usdt_ohlcv = binance.fetch_ohlcv('BTC/USDT','1d',limit=13)
##    print(btc_usdt_ohlcv)
##    print(df,ticker)
##    btc_ticker = binance.fetch_ticker('BTC/USDT') [['symbol','timestamp','datetime','high','low','open','close','volume','change','percentage',
##                                                    'vwap']]

##    btc_ticker = binance.fetch_ticker('BTC/USDT') ('symbol','Open') 
    
##    print(btc_ticker)

def exchange_info():
    import time
    from time import sleep
    for x in ccxt.exchanges:
        print(x,'   ')
    print('------exchange_info()')    
##################################################################################################################################

def main():
    
    while True:
        
        ##exchange_info()
        ##exchange=ccxt.binance()
        exchange=ccxt.binanceus()  #---------------------------------------------------------------------------------------------------
        ##print(exchange)

        ##print(exchange_info)
        markets=exchange.loadMarkets()
        ##print(markets)
        i=0
        for x in markets:
            
        ##    print(x,'   ',markets[x])
            if 'USD' in x:
                x=str(x)
                print(x,'   ')
                bb(x) ##============================================================================>>>
                
                if i > 1:
                    break
                i=i+1
        print('------ from main() ')        
        print ("output file or signal file is: '/home/az2/Downloads/ohwell333.txt' ")
        time.sleep(120)

main()

        
##################################################################################################################################
##schedule.every(5).minutes.do(func)
##
##while True:
##    schedule.run_pending()
##    time.sleep(1)
##
