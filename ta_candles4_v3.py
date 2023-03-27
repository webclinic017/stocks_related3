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
import mpl_finance
import matplotlib
##from matplotlib.finance import candlestick2_ohlc
##from mpl_finance import candlestick_ohlc
##from mplfinance.original_flavor import candlestick_ohlc
from mplfinance.original_flavor import candlestick_ohlc
from optionprice import Option 

##import matplotlib.pyplot as plt
##import matplotlib.ticker as ticker
##import datetime as datetime
##import numpy as np


pd.options.display.float_format = '{:.2f}'.format
pd.options.display.max_columns=155
pd.options.display.max_rows=6500000
pd.set_option('display.max_colwidth', 200)
pd.set_option('display.max_columns', 0)


def new4(mm,g):
    
    import plotly.graph_objs as go
    import pandas as pd
    import yfinance as yf
    import numpy as np
    from datetime import time
    from numerize import numerize
    from yahoo_fin import stock_info as f
    import yahoo_fin.stock_info as si
    import json




    pd.options.display.max_rows=9999
    pd.options.display.max_columns=26
    pd.set_option("display.max_columns", 100)
    pd.set_option('display.width', 1000)


########################################################## daily ##################################################

    perda='55d'
    intervla='1d'


##    g=input("Enter ticker: ")
    perd=perda
    intervl=intervla

# [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]



#df=pd.DataFrame()
#Interval required 5 minutes
    data = yf.download(g, period=perd, interval=intervl,prepost = True)

    df=pd.DataFrame(data)
    df.reset_index(drop=False,inplace=True)
    df['ticker']=g
#df['Open']=df['Open']
    df['5day']=df['Close']-df['Close'].shift(5)
    df['5day_gain']=df['5day'].round(2)
    df['1day']=df['Close']-df['Close'].shift(1)
    df['1day_gain']=df['1day'].round(2)

#print(df.columns)
##    mm=input('Enter no of days: ')

    df5=df.tail(int(mm))
    df5_low = df5['Low'].min()
    df5_high=df5['High'].max()

    print('\n\n')
    print('*************************************************************************')
    print('                               ',mm,' days','                             ')
    print('\n')
    
    print("Today's/yesterday close",str(df['Close'].tail(1)).split()[1])
    print(mm,' days low=',df5_low.round(2))
    print(mm,' days High=',df5_high.round(2))
    gt=(df5_high.round(2)-df5_low.round(2)).round(2)
    print('Low-High gap with  ',mm,' days = ',(df5_high.round(2)-df5_low.round(2)).round(2))

    print('\n')
    print("Today's/yesterday close",str(df['Close'].tail(1)).split()[1])
    print('Low Yesterday close, how far from ',mm,' days low: ',str(df['Close'].tail(1)-df5_low.round(2)).split()[1])
    print('High Yesterday close, how far from ',mm,' days high: ',str(df['Close'].tail(1)-df5_high.round(2)).split()[1])
    print('\n')
    gt2=str(df['Close'].tail(1)).split()[1]
    print('Proposed put  : ',(float(gt2)-float(gt)))
    print('Proposed call : ',(float(gt)+float(gt2)))
#### ######################################################## daily ##################################################

def new3(g):
    import yfinance as yf
    import mplfinance as mpf
    import yfinance as yf, datetime as dt
    import pandas as pd
    import  datetime as dt
    import json


    pd.options.display.max_rows=9999
    pd.options.display.max_columns=26
    pd.set_option("display.max_columns", 100)
    pd.set_option('display.width', 1000)

##    ticker=input("Enter stock ticker: ")
    ticker=g
    no_of_days=300
    
    df = pd.DataFrame()

    
    start = dt.datetime.today() - dt.timedelta(no_of_days)
    end = dt.datetime.today()
    df = yf.download(ticker, start, end,prepost = True)
    print('azharisstupid',df)
    df.fillna(method='bfill', axis=0, inplace=True)
    df['ticker']=ticker
    df['200-day Exponential MA'] = df['Adj Close'].ewm(span=200, adjust=False).mean()
    df['100-day Exponential MA'] = df['Adj Close'].ewm(span=100, adjust=False).mean()
    df['50-day Exponential MA'] = df['Adj Close'].ewm(span=50, adjust=False).mean()
    
    df['20-day Exponential MA'] = df['Adj Close'].ewm(span=20, adjust=False).mean()
    df['10-day Exponential MA'] = df['Adj Close'].ewm(span=10, adjust=False).mean()
    df['3-day Exponential MA'] = df['Adj Close'].ewm(span=3, adjust=False).mean()

    df['3day_s']=df['Close']-df['3-day Exponential MA']
    df['10day_s']=df['Close']-df['10-day Exponential MA']
    df['20day_s']=df['Close']-df['20-day Exponential MA']
    df['50day_s']=df['Close']-df['50-day Exponential MA']
    df['100day_s']=df['Close']-df['100-day Exponential MA']
    df['200day_s']=df['Close']-df['200-day Exponential MA']



    
    
    df['direct']=''
    df['down']=''
    df['a_Close']=''
    df['a_High']=''
    df['a_Low']=''
    df['a_Open']=''
    df['HA']=''
    df['Opena']=''
    df['green']=''
    df['greenby']=''

    for x in df.index:

        df['Opena'].loc[x]=int(df['Open'].loc[x])
        if df['Close'].loc[x]-df['Open'].loc[x] > 0:
            df['green'].loc[x]='Green'
            df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
            #            print(x,'  ','Green','  ',df['ns'].loc[x])
        else:
            df['green'].loc[x]='Red'
            df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]

        df['a_Close'].loc[x]=1/4*(df['Open'].loc[x]+df['High'].loc[x]+df['Low'].loc[x]+df['Close'].loc[x])
        df['a_Open'].loc[x]=1/2*(df['Open'].shift(1).loc[x]+df['Close'].shift(1).loc[x])
        df['High'].loc[x]=df['High'].loc[x]
        df['Low'].loc[x]=df['Low'].loc[x]
        df['a_High'].loc[x]=max(df['High'].loc[x],df['a_Open'].loc[x],df['a_Close'].loc[x])
        df['a_Low'].loc[x]=min(df['Low'].loc[x],df['a_Open'].loc[x],df['a_Close'].loc[x])
     #   df['a_Open'].loc[x]=1/2*(df['Open'].shift(1).loc[x]+df['Close'].shift(1).loc[x])
        df['HA'].loc[x]=df['a_Close'].loc[x]-df['a_Open'].loc[x]




    #   if df['a_Close'].loc[x] > df['a_Open'].loc[x]:
        if df['HA'].loc[x] > 0:
            df['direct'].loc[x]='HA_Green'
        elif df['HA'].loc[x] < 0:
            df['direct'].loc[x]='HA_Red'

    for x in df.index:

        df['greenby'].loc[x]=df['greenby'].loc[x].round(2)
        df['HA'].loc[x]=df['HA'].loc[x].round(2)
        df['a_High'].loc[x]=df['a_High'].loc[x].round(2)
        df['a_Low'].loc[x]=df['a_Low'].loc[x].round(2)
        df['a_Close'].loc[x]=df['a_Close'].loc[x].round(2)
        df['a_Open'].loc[x]=df['a_Open'].loc[x].round(2)

    
    df['(cl_3day)']=''
    df['(cl_5day)']=''
    for x in df.index:
        df['(cl_3day)'].loc[x]=(df['Close'].loc[x]-df['3-day Exponential MA'].loc[x]).round(2)
        df['(cl_5day)'].loc[x]=(df['Close'].loc[x]-df['10-day Exponential MA'].loc[x]).round(2)
        
    df['stragety']=''
    for x in df.index:
        if (df['greenby'].loc[x] < 0 and df['(cl_3day)'].loc[x] < 0):
            df['stragety'].loc[x]=str('Red(')+str(df['greenby'].loc[x])+')_Call sell'
        elif (df['greenby'].loc[x] > 0 and df['(cl_3day)'].loc[x] > 0):
            df['stragety'].loc[x]=str('Green(')+str(df['greenby'].loc[x])+')_put sell'
        else:
            pass
        

    
    df.reset_index(inplace=True)
    p=df['Close'].tail(1)
####    print(p)
    df['yest']=df['Close']-df['Close'].shift(1)
    p6=df['yest'].tail(1)
    p2=df['yest'].tail(1)
    p3=df['Low'].tail(1)
    p4=df['High'].tail(1)
    p5=df['Open'].tail(1)
    df.set_index('Date',inplace=True)
##    print(df.columns)
    u1=str(p3).split()[1]
    u2=str(p4).split()[1]
    u3=float(u1)-float(u2)
    
    
    print(df)

    mpf.plot(df, block=False,type='candle', volume=True, figratio=(15, 15), style='yahoo', mav=(200,100,50,20,10,3), title=ticker.upper() +' (Daily) '+
             str(p).split()[1]+' / (diff) '+str(p2).split()[1] + ', Open: '+ str(p5).split()[1] + ' ,low: '+str(p3).split()[1]+ ' ,High: '+ str(p4).split()[1]
             + ', day swing: ' + str(u3).split('.')[0],
             show_nontrading=True)
  

##    df['5']=''
    df.reset_index(inplace=True)

    df5=pd.concat([df['Date'],df['ticker'],df['Close'],df['3-day Exponential MA'],df['10-day Exponential MA'],
                   df['20-day Exponential MA'],df['50-day Exponential MA'],
                   df['100-day Exponential MA'],df['200-day Exponential MA']
                   ],axis=1)
    
    df5['3']=''
    df5['10']=''
    df5['20']=''
    df5['50']=''
    df5['100']=''
    df5['200']=''
    print(df5)
    i=0
    for x in df5.index:
##        print(' 3day/shift ',df5['Date'].loc[x],df5['3-day Exponential MA'].loc[x].round(0)-df5['3-day Exponential MA'].shift(1).loc[x].round(0))
              
##        print(df5['Close'].loc[x] , df5['3-day Exponential MA'].loc[x],df5['3-day Exponential MA'].shift(1).loc[x])
        if (df5['3-day Exponential MA'].loc[x].round(0)-df5['3-day Exponential MA'].shift(1).loc[x].round(0)) > 0:
            
            if df5['Close'].loc[x] - df5['3-day Exponential MA'].loc[x] > 0:
                print(df5['Date'].loc[x],df['ticker'].loc[x],int(df['Close'].loc[x])," ---> BUY-3-MA uptrend *** ",
                      '(',(df5['Close'].loc[x] - df5['3-day Exponential MA'].loc[x]).round(0),')  ',int(df5['Close'].loc[x]-df5['Close'].shift(1).loc[x]))

            elif df5['Close'].loc[x] - df5['3-day Exponential MA'].loc[x] < 0:
                print(df5['Date'].loc[x],df['ticker'].loc[x],int(df['Close'].loc[x])," *** BUY?(close<3MA)-3-MA uptrend *** ",'   ',
                      '(',(df5['Close'].loc[x] - df5['3-day Exponential MA'].loc[x]).round(0),')  ',int(df5['Close'].loc[x]-df5['Close'].shift(1).loc[x]))
            else:
                pass


        if (df5['3-day Exponential MA'].loc[x].round(0)-df5['3-day Exponential MA'].shift(1).loc[x].round(0)) < 0:
            
            if df5['Close'].loc[x] - df5['3-day Exponential MA'].loc[x] > 0:
                print(df5['Date'].loc[x],df['ticker'].loc[x],int(df['Close'].loc[x])," *** SELL?(close>3MA)-3-MA DWNtrend *** ",
                      '(',(df5['Close'].loc[x] - df5['3-day Exponential MA'].loc[x]).round(0),')  ',int(df5['Close'].loc[x]-df5['Close'].shift(1).loc[x]))

            elif df5['Close'].loc[x] - df5['3-day Exponential MA'].loc[x] < 0:
                print(df5['Date'].loc[x],df['ticker'].loc[x],int(df['Close'].loc[x])," <--- SELL-3-MA DWNtrend *** ",'   ',
                      '(',(df5['Close'].loc[x] - df5['3-day Exponential MA'].loc[x]).round(0),')  ',int(df5['Close'].loc[x]-df5['Close'].shift(1).loc[x]))
            else:
                pass
            




##        if (df5['10-day Exponential MA'].loc[x].round(0)-df5['10-day Exponential MA'].shift(1).loc[x].round(0)) > 0:
##            
##            if df5['Close'].loc[x] - df5['10-day Exponential MA'].loc[x] > 0:
##                print(df5['Date'].loc[x],df['ticker'].loc[x],int(df['Close'].loc[x])," ---> BUY-10-MA uptrend *** ",
##                      '(',(df5['Close'].loc[x] - df5['10-day Exponential MA'].loc[x]).round(0),')  ',int(df5['Close'].loc[x]-df5['Close'].shift(1).loc[x]))
##
##            elif df5['Close'].loc[x] - df5['10-day Exponential MA'].loc[x] < 0:
##                print(df5['Date'].loc[x],df['ticker'].loc[x],int(df['Close'].loc[x])," *** BUY?(close<3MA)-10-MA uptrend *** ",'   ',
##                      '(',(df5['Close'].loc[x] - df5['10-day Exponential MA'].loc[x]).round(0),')  ',int(df5['Close'].loc[x]-df5['Close'].shift(1).loc[x]))
##            else:
##                pass
##
##
##        if (df5['10-day Exponential MA'].loc[x].round(0)-df5['10-day Exponential MA'].shift(1).loc[x].round(0)) < 0:
##            
##            if df5['Close'].loc[x] - df5['10-day Exponential MA'].loc[x] > 0:
##                print(df5['Date'].loc[x],df['ticker'].loc[x],int(df['Close'].loc[x])," *** SELL?(close>3MA)-10-MA DWNtrend *** ",
##                      '(',(df5['Close'].loc[x] - df5['10-day Exponential MA'].loc[x]).round(0),')  ',int(df5['Close'].loc[x]-df5['Close'].shift(1).loc[x]))
##
##            elif df5['Close'].loc[x] - df5['10-day Exponential MA'].loc[x] < 0:
##                print(df5['Date'].loc[x],df['ticker'].loc[x],int(df['Close'].loc[x])," <--- SELL-10-MA DWNtrend *** ",'   ',
##                      '(',(df5['Close'].loc[x] - df5['10-day Exponential MA'].loc[x]).round(0),')  ',int(df5['Close'].loc[x]-df5['Close'].shift(1).loc[x]))
##            else:
##                pass


            
##        if df5['3-day Exponential MA'].loc[x] <  df5['3-day Exponential MA'].shift(1).loc[x] and df5['Close'].loc[x] > df5['3-day Exponential MA'].loc[x]:            
##            print(i," rr bromley")
####        (float(df5['3-day Exponential MA'].loc[x]) <  float(df5['3-day Exponential MA'].shift(1).loc[x]):
##
##        if df5['Close'].loc[x] < df5['3-day Exponential MA'].loc[x] and df5['3-day Exponential MA'].loc[x] > df5['3-day Exponential MA'].shift(1).loc[x]:
##            df5['3'].loc[x]='Buy Put8'
##            print(i," linda bromley")
##
####        elif (float(df5['Close'].loc[x]) < float(df5['3-day Exponential MA'].loc[x]) and  float(df5['Close'].loc[x]) <float(df5['3-day Exponential MA'].loc[x])):  
####            df5['3'].loc[x]='Close Put'
##            
####        elif (df5['3-day Exponential MA'].loc[x] < df5['3-day Exponential MA'].shift(1).loc[x]) :  
####            df5['3'].loc[x]='Buy Call'
##        if df5['3-day Exponential MA'].loc[x] >  df5['3-day Exponential MA'].shift(1).loc[x] and df5['Close'].loc[x] < df5['3-day Exponential MA'].loc[x]:
##            df5['3'].loc[x]='Close call9'
##            print(i," andrea boggs")
##
##        ##
##        if df5['3-day Exponential MA'].loc[x] < df5['3-day Exponential MA'].shift(1).loc[x] and df['Close'].loc[x] < df['3-day Exponential MA'].loc[x] :  
##            df5['3'].loc[x]='Buy Call777'
##            print(i, " julie")
####            print("uuuuuu df5['3-day Exponential MA'].loc[x]) < float((df5['3-day Exponential MA'].shift(1)).loc[x] ")
####            print(df5['3-day Exponential MA'].loc[x],' < ' , df5['3-day Exponential MA'].shift(1).loc[x],' ****  ',df['Close'].loc[x],'   ;',df['3-day Exponential MA'].loc[x])
##            print('\n')
##                           
####        else:
####            print("K")
        i=i+1
##  i
    print(df5['3-day Exponential MA'],'         ',df5['Close'])    
##        if (df['10-day Exponential MA'].loc[x] >  df['10-day Exponential MA'].shift(1).loc[x]) and (df['Close'].loc[x] > df['10-day Exponential MA'].loc[x]) :
##            df5['10'].loc[x]='Buy Put'
##        elif (df['Close'].loc[x] < df['10-day Exponential MA'].loc[x]):     
##            df5['10'].loc[x]='Close Put'
##        if (df['10-day Exponential MA'].loc[x] <  df['10-day Exponential MA'].shift(1).loc[x]) and (df['Close'].loc[x] < df['10-day Exponential MA'].loc[x]): 
##            df5['10'].loc[x]='Buy Call'
##        elif (df['Close'].loc[x] > df['10-day Exponential MA'].loc[x]):
##            df5['10'].loc[x]='Close call'   
##
##        if (df['20-day Exponential MA'].loc[x] >  df['20-day Exponential MA'].shift(1).loc[x]) and (df['Close'].loc[x] > df['20-day Exponential MA'].loc[x]):
##            df5['20'].loc[x]='Buy Put'
##        elif (df['Close'].loc[x] < df['20-day Exponential MA'].loc[x]): 
##            df5['20'].loc[x]='Close Put'
##        if (df['20-day Exponential MA'].loc[x] <  df['20-day Exponential MA'].shift(1).loc[x]) and (df['Close'].loc[x] < df['20-day Exponential MA'].loc[x]):
##            df5['20'].loc[x]='Buy Call'
##        elif (df['Close'].loc[x] > df['20-day Exponential MA'].loc[x]):
##            
##            df5['20'].loc[x]='Close call'
##
##
##        if (df['50-day Exponential MA'].loc[x] >  df['50-day Exponential MA'].shift(1).loc[x]) and (df['Close'].loc[x] > df['50-day Exponential MA'].loc[x]):
##            df5['50'].loc[x]='Buy Put'
##        elif (df['Close'].loc[x] < df['50-day Exponential MA'].loc[x]):            
##            df5['50'].loc[x],='Close Put'
##        if (df['50-day Exponential MA'].loc[x] <  df['50-day Exponential MA'].shift(1).loc[x]) and (df['Close'].loc[x] < df['50-day Exponential MA'].loc[x]):            
##            df5['50'].loc[x]='Buy Call'
##        elif (df['Close'].loc[x] > df['50-day Exponential MA'].loc[x]):
##            
##            df5['50'].loc[x]='Close call'
##            
##        if (df['100-day Exponential MA'].loc[x] >  df['100-day Exponential MA'].shift(1).loc[x]) and (df['Close'].loc[x] > df['100-day Exponential MA'].loc[x]):
##            df5['100'].loc[x]='Buy Put'
##        elif (df['Close'].loc[x] < df['100-day Exponential MA'].loc[x]):            
##            df5['100'].loc[x]='Close Put'
##        if (df['100-day Exponential MA'].loc[x] <  df['100-day Exponential MA'].shift(1).loc[x]) and (df['Close'].loc[x] < df['100-day Exponential MA'].loc[x]):         
##            df5['100'].loc[x]='Buy Call'
##        elif (df['Close'].loc[x] > df['100-day Exponential MA'].loc[x]):            
##            df5['100'].loc[x]='Close call'
##
##        if (df['200-day Exponential MA'].loc[x] >  df['200-day Exponential MA'].shift(1).loc[x]) and (df['Close'].loc[x] > df['200-day Exponential MA'].loc[x]) :
##            df5['200'].loc[x]='Buy Put'
##        elif (df['Close'].loc[x] < df['200-day Exponential MA'].loc[x]):      
##            df5['200'].loc[x]='Close Put'
##        if (df['200-day Exponential MA'].loc[x] <  df['200-day Exponential MA'].shift(1).loc[x]) and (df['Close'].loc[x] < df['200-day Exponential MA'].loc[x]) :
##            df5['200'].loc[x]='Buy Call'
##        elif (df['Close'].loc[x] > df['200-day Exponential MA'].loc[x]):
##            
##            df5['200'].loc[x]='Close call'
    print('buuu')        
##    df.plot()
##################################
    perd='2d'
    intervl='15m'
    dfi = pd.DataFrame()
##    ticker='amc'
    print('--- Running ---')
    ### [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]
    ##
    ####g=input("Enter Ticker :")
    ###perd=input("Enter no of days '5d','2d','1d' :")
    ###intervl=input("Enter mins '5m','1m' :")
    ##
    ##
    ###df=pd.DataFrame()
    ###Interval required 5 minutes
    data = yf.download(tickers=ticker, period=perd, interval=intervl,prepost = True)
    dfi=pd.DataFrame(data)


    dfi.fillna(method='bfill', axis=0, inplace=True)    
    dfi['200-day Exponential MA'] = dfi['Adj Close'].ewm(span=200, adjust=True).mean()
    dfi['100-day Exponential MA'] = dfi['Adj Close'].ewm(span=100, adjust=True).mean()
    dfi['50-day Exponential MA'] = dfi['Adj Close'].ewm(span=50, adjust=True).mean()
    
    dfi['20-day Exponential MA'] = dfi['Adj Close'].ewm(span=3, adjust=True).mean()
    dfi['10-day Exponential MA'] = dfi['Adj Close'].ewm(span=10, adjust=True).mean()
    dfi['3-day Exponential MA'] = dfi['Adj Close'].ewm(span=2, adjust=True).mean()

    dfi['3day_s']=dfi['Close']-dfi['3-day Exponential MA']
    dfi['10day_s']=dfi['Close']-dfi['10-day Exponential MA']
    dfi['20day_s']=dfi['Close']-dfi['20-day Exponential MA']
    dfi['50day_s']=dfi['Close']-dfi['50-day Exponential MA']
    dfi['100day_s']=dfi['Close']-dfi['100-day Exponential MA']
    dfi['200day_s']=dfi['Close']-dfi['200-day Exponential MA']
    dfi['price_shift']=(dfi['Close']-dfi['Close'].shift(1)).round(2)
####    print(dfi)
####    print(dfi.columns)

####    iday = intraday.loc[1:30,:]
    iday = dfi.loc[:,:]
##    iday = intraday.loc[:63,:]
####    print(iday)
####    print(iday.columns)

    mpf.plot(iday, block=False,type='candle', volume=True, figratio=(15, 15), style='yahoo', mav=(200,100,50,20,10,3), title=ticker+' - ('+perd + ' - '+intervl+')'
             +
             str(p).split()[1]+' / (diff) '+str(p2).split()[1] + ', Open: '+ str(p5).split()[1] + ' ,low: '+str(p3).split()[1]+ ' ,High: '+ str(p4).split()[1]
             + ', day swing: ' + str(u3).split('.')[0]

             )


    iday['direct']=''
    iday['down']=''
    iday['a_Close']=''
    iday['a_High']=''
    iday['a_Low']=''
    iday['a_Open']=''
    iday['HA']=''
    iday['Opena']=''
    iday['green']=''
    iday['greenby']=''

    for x in iday.index:

        iday['Opena'].loc[x]=int(iday['Open'].loc[x])
        if iday['Close'].loc[x]-iday['Open'].loc[x] > 0:
            iday['green'].loc[x]='Green'
            iday['greenby'].loc[x]=iday['Close'].loc[x]-iday['Open'].loc[x]
            #            print(x,'  ','Green','  ',iday['ns'].loc[x])
        else:
            iday['green'].loc[x]='Red'
            iday['greenby'].loc[x]=iday['Close'].loc[x]-iday['Open'].loc[x]

        iday['a_Close'].loc[x]=1/4*(iday['Open'].loc[x]+iday['High'].loc[x]+iday['Low'].loc[x]+iday['Close'].loc[x])
        iday['a_Open'].loc[x]=1/2*(iday['Open'].shift(1).loc[x]+iday['Close'].shift(1).loc[x])
        iday['High'].loc[x]=iday['High'].loc[x]
        iday['Low'].loc[x]=iday['Low'].loc[x]
        iday['a_High'].loc[x]=max(iday['High'].loc[x],iday['a_Open'].loc[x],iday['a_Close'].loc[x])
        iday['a_Low'].loc[x]=min(iday['Low'].loc[x],iday['a_Open'].loc[x],iday['a_Close'].loc[x])
     #   iday['a_Open'].loc[x]=1/2*(iday['Open'].shift(1).loc[x]+iday['Close'].shift(1).loc[x])
        iday['HA'].loc[x]=iday['a_Close'].loc[x]-iday['a_Open'].loc[x]




    #   if iday['a_Close'].loc[x] > iday['a_Open'].loc[x]:
        if iday['HA'].loc[x] > 0:
            iday['direct'].loc[x]='HA_Green'
        elif iday['HA'].loc[x] < 0:
            iday['direct'].loc[x]='HA_Red'

    for x in iday.index:

        iday['greenby'].loc[x]=iday['greenby'].loc[x].round(2)
        iday['HA'].loc[x]=iday['HA'].loc[x].round(2)
        iday['a_High'].loc[x]=iday['a_High'].loc[x].round(2)
        iday['a_Low'].loc[x]=iday['a_Low'].loc[x].round(2)
        iday['a_Close'].loc[x]=iday['a_Close'].loc[x].round(2)
        iday['a_Open'].loc[x]=iday['a_Open'].loc[x].round(2)

    
    iday['(cl_3day)']=''
    iday['(cl_5day)']=''
    for x in iday.index:
        iday['(cl_3day)'].loc[x]=(iday['Close'].loc[x]-iday['3-day Exponential MA'].loc[x]).round(2)
        iday['(cl_5day)'].loc[x]=(iday['Close'].loc[x]-iday['10-day Exponential MA'].loc[x]).round(2)
        
    iday['stragety']=''
    for x in iday.index:
        if (iday['greenby'].loc[x] < 0 and iday['(cl_3day)'].loc[x] < 0):
            iday['stragety'].loc[x]=str('Red(')+str(iday['greenby'].loc[x])+')_Call sell'
        elif (iday['greenby'].loc[x] > 0 and iday['(cl_3day)'].loc[x] > 0):
            iday['stragety'].loc[x]=str('Green(')+str(iday['greenby'].loc[x])+')_put sell'
        else:
            pass
        
    print(iday)


g='^NDX'
##g='amzn'    
new3(g)
u=[1,5,7,10,15,30]

for x in u:
    new4(x,g)
