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
import mpl_finance
import matplotlib
##from matplotlib.finance import candlestick2_ohlc
##from mpl_finance import candlestick_ohlc
##from mplfinance.original_flavor import candlestick_ohlc
from mplfinance.original_flavor import candlestick_ohlc
from optionprice import Option 



pd.options.display.float_format = '{:.2f}'.format
pd.options.display.max_columns=255
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
    pd.options.display.max_columns=36
    pd.set_option("display.max_columns", 100)
    pd.set_option('display.width', 1000)


########################################################## daily ##################################################

    perda='55d'
    intervla='1d'


##    g=input("Entr_Signal ticker: ")
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
##    mm=input('Entr_Signal no of days: ')

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



############################################################################    


def new3(g,pdays,ptime,pprepost):
    import yfinance as yf
    import mplfinance as mpf
    import yfinance as yf, datetime as dt
    import pandas as pd
    import  datetime as dt
    import json
    import pandas_ta as ta
    from numerize import numerize
    import numpy as np

    pd.options.display.max_rows=9999
    pd.options.display.max_columns=36
    pd.set_option("display.max_columns", 100)
    pd.set_option('display.width', 1000)

##    ticker=input("Entr_Signal stock ticker: ")
    ticker=g
    no_of_days=365
    
    df = pd.DataFrame()

    
    start = dt.datetime.today() - dt.timedelta(no_of_days)
    end = dt.datetime.today()
    df = yf.download(ticker, start, end,prepost = True)

    print('azharisstupid',df)
    df.fillna(method='bfill', axis=0, inplace=True)


#### ######################################################## daily ##################################################
    
##    perd='2d'
    perd=pdays
##    intervl='60m'
    intervl=ptime

    dfday = pd.DataFrame()
##    ticker='amc'
    print('--- Running ---')
    ### [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]
    ##
    ####g=input("Entr_Signal Ticker :")
    ###perd=input("Entr_Signal no of days '5d','2d','1d' :")
    ###intervl=input("Entr_Signal mins '5m','1m' :")
    ##
    ##
    ###df=pd.DataFrame()
    ###Interval required 5 minutes
##    data = yf.download(tickers=ticker, period=perd, interval=intervl,prepost = True)
    data = yf.download(tickers=ticker, period=perd, interval=intervl,prepost=pprepost)
    dfday=pd.DataFrame(data)

    dfday['ticker']=g
    dfday.fillna(method='bfill', axis=0, inplace=True)
##    dfday['200-day Exponential MA'] = ta.ema(dfday["Close"], length=200)
    
    dfday['200-day Exponential MA'] = dfday['Close'].ewm(span=200, adjust=True).mean()
    dfday['100-day Exponential MA'] = dfday['Close'].ewm(span=100, adjust=True).mean()
    dfday['50-day Exponential MA'] = dfday['Close'].ewm(span=50, adjust=True).mean()
    
    dfday['20-day Exponential MA'] = dfday['Close'].ewm(span=3, adjust=True).mean()
    dfday['10-day Exponential MA'] = dfday['Close'].ewm(span=10, adjust=True).mean()
    dfday['5-day Exponential MA'] = dfday['Close'].ewm(span=5, adjust=True).mean()
    dfday['3-day Exponential MA'] = dfday['Close'].ewm(span=3, adjust=True).mean()

    dfday['3day_s']=dfday['Close']-dfday['3-day Exponential MA']
    dfday['5day_s']=dfday['Close']-dfday['5-day Exponential MA']
    dfday['10day_s']=dfday['Close']-dfday['10-day Exponential MA']
    dfday['20day_s']=dfday['Close']-dfday['20-day Exponential MA']
    dfday['50day_s']=dfday['Close']-dfday['50-day Exponential MA']
    dfday['100day_s']=dfday['Close']-dfday['100-day Exponential MA']
    dfday['200day_s']=dfday['Close']-dfday['200-day Exponential MA']
    dfday['price_shift']=(dfday['Close']-dfday['Close'].shift(1)).round(2)
####    print(dfday)
####    print(dfday.columns)

####    dfday = intraday.loc[1:30,:]
    dfday = dfday.loc[:,:]
##    dfday = intraday.loc[:63,:]
####    print(dfday)
####    print(dfday.columns)

    
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

    s  = mpf.make_mpf_style(base_mpf_style='yahoo',mavcolors=['#ef5714','#ef5714','#9f4878','#9f4878','#ef5714','#9f4878','#9f4878'])
     
    mpf.plot(dfday, block=False,type='candle', volume=True, figratio=(15, 15), mav=(200,100,50,20,10,3,5),
         title=ticker.upper() +' (Daily) '+
         str(p).split()[1]+' / (diff) '+str(p2).split()[1] + ', Open: '+ str(p5).split()[1] + ' ,low: '+str(p3).split()[1]+ ' ,High: '+ str(p4).split()[1]
         + ', day swing: ' + str(u3).split('.')[0],style=s,
         show_nontrading=True)

    dfday['HA_Signal']=''
    dfday['down']=''
    dfday['a_Close']=''
    dfday['a_High']=''
    dfday['a_Low']=''
    dfday['a_Open']=''
    dfday['HA']=''
    dfday['Opena']=''
    dfday['green']=''
    dfday['greenby']=''
    dfday['s']=' * '

    for x in dfday.index:
        dfday['s'].loc[x]='*'
        dfday['Opena'].loc[x]=int(dfday['Open'].loc[x])
        if dfday['Close'].loc[x]-dfday['Open'].loc[x] > 0:
            dfday['green'].loc[x]='Green'
            dfday['greenby'].loc[x]=dfday['Close'].loc[x]-dfday['Open'].loc[x]
            #            print(x,'  ','Green','  ',dfday['ns'].loc[x])
        else:
            dfday['green'].loc[x]='Red'
            dfday['greenby'].loc[x]=dfday['Close'].loc[x]-dfday['Open'].loc[x]

        dfday['a_Close'].loc[x]=1/4*(dfday['Open'].loc[x]+dfday['High'].loc[x]+dfday['Low'].loc[x]+dfday['Close'].loc[x])
        dfday['a_Open'].loc[x]=1/2*(dfday['Open'].shift(1).loc[x]+dfday['Close'].shift(1).loc[x])
        dfday['High'].loc[x]=dfday['High'].loc[x]
        dfday['Low'].loc[x]=dfday['Low'].loc[x]
        dfday['a_High'].loc[x]=max(dfday['High'].loc[x],dfday['a_Open'].loc[x],dfday['a_Close'].loc[x])
        dfday['a_Low'].loc[x]=min(dfday['Low'].loc[x],dfday['a_Open'].loc[x],dfday['a_Close'].loc[x])
     #   dfday['a_Open'].loc[x]=1/2*(dfday['Open'].shift(1).loc[x]+dfday['Close'].shift(1).loc[x])
        dfday['HA'].loc[x]=dfday['a_Close'].loc[x]-dfday['a_Open'].loc[x]




    #   if dfday['a_Close'].loc[x] > dfday['a_Open'].loc[x]:
        if dfday['HA'].loc[x] > 0:
            dfday['HA_Signal'].loc[x]='HA_Green'
        elif dfday['HA'].loc[x] < 0:
            dfday['HA_Signal'].loc[x]='HA_Red'

    for x in dfday.index:

        dfday['greenby'].loc[x]=dfday['greenby'].loc[x].round(2)
        dfday['HA'].loc[x]=dfday['HA'].loc[x].round(2)
        dfday['a_High'].loc[x]=dfday['a_High'].loc[x].round(2)
        dfday['a_Low'].loc[x]=dfday['a_Low'].loc[x].round(2)
        dfday['a_Close'].loc[x]=dfday['a_Close'].loc[x].round(2)
        dfday['a_Open'].loc[x]=dfday['a_Open'].loc[x].round(2)

    
    dfday['(cl_3day)']=''
    dfday['(cl_5day)']=''
    for x in dfday.index:
        dfday['(cl_3day)'].loc[x]=(dfday['Close'].loc[x]-dfday['3-day Exponential MA'].loc[x]).round(2)
        dfday['(cl_5day)'].loc[x]=(dfday['Close'].loc[x]-dfday['10-day Exponential MA'].loc[x]).round(2)
        
    dfday['stragety']=''
    for x in dfday.index:
        if (dfday['greenby'].loc[x] < 0 and dfday['(cl_3day)'].loc[x] < 0):
            dfday['stragety'].loc[x]=str('Red(')+str(dfday['greenby'].loc[x])+')_Call sell'
        elif (dfday['greenby'].loc[x] > 0 and dfday['(cl_3day)'].loc[x] > 0):
            dfday['stragety'].loc[x]=str('Green(')+str(dfday['greenby'].loc[x])+')_put sell'
        else:
            pass


    dfday.reset_index(drop=False,inplace=True)    
    print('sleeptrain',dfday)
    print('sleeptrain_columns',dfday.columns)
##    print(dfday[['Date', 'Open', 'High', 'Low']])
###################################################################
#############################

##    df['5']=''
##    df.reset_index(inplace=True)

##    dfday=pd.concat(df['Date'],[df['ticker'],df['Close'],df['3-day Exponential MA'],
##                                   df['5-day Exponential MA'],df['10-day Exponential MA'],
##                                   df['20-day Exponential MA'],df['50-day Exponential MA'],
##                                   df['100-day Exponential MA'],df['200-day Exponential MA']
##                                   ],axis=1)
##

                                   
##                                   ,
##                                   

##    dfdaya=dfday[['Date','ticker','Close','3-day Exponential MA','5-day Exponential MA','10-day Exponential MA','20-day Exponential MA','50-day Exponential MA','100-day Exponential MA','200-day Exponential MA']]
##    print('dd',dfdaya)
    dfday['3-MA']=''
    dfday['5-MA']=''
    dfday['10-MA']=''
    dfday['20-MA']=''
    dfday['50-MA']=''
    dfday['100-MA']=''
    dfday['200-MA']=''

    dfday['3-MA Entr_Signal']=''   
    dfday['5-MA Entr_Signal']=''
    dfday['10-MA Entr_Signal']=''
    dfday['20-MA Entr_Signal']=''
    dfday['50-MA Entr_Signal']=''
    dfday['100-MA Entr_Signal']=''
    dfday['200-MA Entr_Signal']=''

    dfday['3-MA-Exit_Signal']=''
    dfday['5-MA-Exit_Signal']=''
    dfday['10-MA-Exit_Signal']=''
    dfday['20-MA-Exit_Signal']=''
    dfday['50-MA-Exit_Signal']=''
    dfday['100-MA-Exit_Signal']=''
    dfday['200-MA-Exit_Signal']=''

##    print(dfday)
    i=0
    for x in dfday.index:
##        print(' 3day/shift ',dfday['Date'].loc[x],dfday['3-day Exponential MA'].loc[x].round(0)-dfday['3-day Exponential MA'].shift(1).loc[x].round(0))
              
##        print(dfday['Close'].loc[x] , dfday['3-day Exponential MA'].loc[x],dfday['3-day Exponential MA'].shift(1).loc[x])
        if (dfday['3-day Exponential MA'].loc[x].round(0)-dfday['3-day Exponential MA'].shift(1).loc[x].round(0)) > 0:
            
            if dfday['Close'].loc[x] - dfday['3-day Exponential MA'].loc[x] > 0:
                dfday['3-MA'].loc[x]=" ---> BUY-3-MA uptrend *** "
                dfday['3-MA Entr_Signal'].loc[x]=(dfday['Close'].loc[x] - dfday['3-day Exponential MA'].loc[x]).round(0)
                
            elif dfday['Close'].loc[x] - dfday['3-day Exponential MA'].loc[x] < 0:
                dfday['3-MA'].loc[x]=" *** BUY?(close<3MA)-3-MA uptrend *** "
                dfday['3-MA Entr_Signal'].loc[x]=(dfday['Close'].loc[x] - dfday['3-day Exponential MA'].loc[x]).round(0)

                
            else:
                pass


        if (dfday['3-day Exponential MA'].loc[x].round(0)-dfday['3-day Exponential MA'].shift(1).loc[x].round(0)) < 0:
            
            if dfday['Close'].loc[x] - dfday['3-day Exponential MA'].loc[x] > 0:
                dfday['3-MA'].loc[x]=" *** SELL?(close>3MA)-3-MA DWNtrend *** "
                dfday['3-MA Entr_Signal'].loc[x]=(dfday['Close'].loc[x] - dfday['3-day Exponential MA'].loc[x]).round(0)
                

            elif dfday['Close'].loc[x] - dfday['3-day Exponential MA'].loc[x] < 0:
                dfday['3-MA'].loc[x]=" <--- SELL-3-MA DWNtrend *** "
                dfday['3-MA Entr_Signal'].loc[x]=(dfday['Close'].loc[x] - dfday['3-day Exponential MA'].loc[x]).round(0)
                

            else:
                pass


##        if dfday['Close'].loc[x] - dfday['3-day Exponential MA'].loc[x] < 0:
##            dfday['3-MA-Exit_Signal']='Exit'




        if dfday['Close'].loc[x] - dfday['Close'].ewm(span=3, adjust=False).mean().loc[x] < 0:
            dfday['3-MA-Exit_Signal'].loc[x]= (dfday['Close'].loc[x] - dfday['Close'].ewm(span=3, adjust=False).mean().loc[x])

        else:
            dfday['3-MA-Exit_Signal'].loc[x]= (dfday['Close'].loc[x] - dfday['Close'].ewm(span=3, adjust=False).mean().loc[x])            
            
            
##    print('office_walnut',dfday)            
##################################################
#add

        if (dfday['5-day Exponential MA'].loc[x].round(0)-dfday['5-day Exponential MA'].shift(1).loc[x].round(0)) > 0: #(MA slopes upward)
            

            if dfday['Close'].loc[x] - dfday['5-day Exponential MA'].loc[x] > 0:  #(close price above MA)
                dfday['5-MA'].loc[x]=" ---> BUY-5-MA uptrend *** "  # buy signal
                dfday['5-MA Entr_Signal'].loc[x]=(dfday['Close'].loc[x] - dfday['5-day Exponential MA'].loc[x]).round(0)
                
            elif dfday['Close'].loc[x] - dfday['5-day Exponential MA'].loc[x] < 0: #(close price above MA)
                dfday['5-MA'].loc[x]=" *** BUY?(close<5-MA)-5-MA uptrend *** " # buy signal
                dfday['5-MA Entr_Signal'].loc[x]=(dfday['Close'].loc[x] - dfday['5-day Exponential MA'].loc[x]).round(0)

            elif dfday['Close'].loc[x] - dfday['5-day Exponential MA'].loc[x] == 0:
                dfday['5-MA'].loc[x]="close=5-day_exp"
                dfday['5-MA Entr_Signal'].loc[x]=(dfday['Close'].loc[x] - dfday['5-day Exponential MA'].loc[x]).round(0)
                
            else:
                pass


        if (dfday['5-day Exponential MA'].loc[x].round(0)-dfday['5-day Exponential MA'].shift(1).loc[x].round(0)) < 0:

            if dfday['Close'].loc[x] - dfday['5-day Exponential MA'].loc[x] > 0:
                dfday['5-MA'].loc[x]=" *** SELL?(close>5-MA)-5-MA DWNtrend *** "
                dfday['5-MA Entr_Signal'].loc[x]=(dfday['Close'].loc[x] - dfday['5-day Exponential MA'].loc[x]).round(0)
                

            elif dfday['Close'].loc[x] - dfday['5-day Exponential MA'].loc[x] < 0:
                dfday['5-MA'].loc[x]=" <--- SELL-5-MA DWNtrend *** "
                dfday['5-MA Entr_Signal'].loc[x]=(dfday['Close'].loc[x] - dfday['5-day Exponential MA'].loc[x]).round(0)

##        if dfday['Close'].loc[x] - dfday['5-day Exponential MA'].loc[x] < 0:
##            dfday['5-MA-Exit_Signal']='Exit'
##                
####        if dfday['Close'].loc[x] - dfday['5-day Exponential MA'].loc[x] < 0:
####            dfday['5-MA'].loc[x]="stupid"
####            dfday['5-MA Entr_Signal'].loc[x]="stupid"
##
##        else:
##            pass


        if dfday['Close'].loc[x] - dfday['Close'].ewm(span=5, adjust=False).mean().loc[x] < 0:
            dfday['5-MA-Exit_Signal'].loc[x]= (dfday['Close'].loc[x] - dfday['Close'].ewm(span=5, adjust=False).mean().loc[x])

        else:
            dfday['5-MA-Exit_Signal'].loc[x]= (dfday['Close'].loc[x] - dfday['Close'].ewm(span=5, adjust=False).mean().loc[x])            
            

###########################################
###add
##
        if (dfday['10-day Exponential MA'].loc[x].round(0)-dfday['10-day Exponential MA'].shift(1).loc[x].round(0)) > 0:
            

            if dfday['Close'].loc[x] - dfday['10-day Exponential MA'].loc[x] > 0:
                dfday['10-MA'].loc[x]=" ---> BUY-10-MA uptrend *** "
                dfday['10-MA Entr_Signal'].loc[x]=(dfday['Close'].loc[x] - dfday['10-day Exponential MA'].loc[x]).round(0)
                
            elif dfday['Close'].loc[x] - dfday['10-day Exponential MA'].loc[x] < 0:
                dfday['10-MA'].loc[x]=" *** BUY?(close<10-MA)-10-MA uptrend *** "
                dfday['10-MA Entr_Signal'].loc[x]=(dfday['Close'].loc[x] - dfday['10-day Exponential MA'].loc[x]).round(0)

                
            else:
                pass


        if (dfday['10-day Exponential MA'].loc[x].round(0)-dfday['10-day Exponential MA'].shift(1).loc[x].round(0)) < 0:

            if dfday['Close'].loc[x] - dfday['10-day Exponential MA'].loc[x] > 0:
                dfday['10-MA'].loc[x]=" *** SELL?(close>10-MA)-10-MA DWNtrend *** "
                dfday['10-MA Entr_Signal'].loc[x]=(dfday['Close'].loc[x] - dfday['10-day Exponential MA'].loc[x]).round(0)
                

            elif dfday['Close'].loc[x] - dfday['10-day Exponential MA'].loc[x] < 0:
                dfday['10-MA'].loc[x]=" <--- SELL-10-MA DWNtrend *** "
                dfday['10-MA Entr_Signal'].loc[x]=(dfday['Close'].loc[x] - dfday['10-day Exponential MA'].loc[x]).round(0)
                

            else:
                pass


##        if dfday['Close'].loc[x] - dfday['10-day Exponential MA'].loc[x] < 0:
##            dfday['10-MA-Exit_Signal']='Exit'


        if dfday['Close'].loc[x] - dfday['Close'].ewm(span=10, adjust=False).mean().loc[x] < 0:
            dfday['10-MA-Exit_Signal'].loc[x]= (dfday['Close'].loc[x] - dfday['Close'].ewm(span=10, adjust=False).mean().loc[x])

        else:
            dfday['10-MA-Exit_Signal'].loc[x]= (dfday['Close'].loc[x] - dfday['Close'].ewm(span=10, adjust=False).mean().loc[x])            
            


            
##    print('office_walnut',dfday)
#add
##            
###add
##
        if (dfday['20-day Exponential MA'].loc[x].round(0)-dfday['20-day Exponential MA'].shift(1).loc[x].round(0)) > 0:
            

            if dfday['Close'].loc[x] - dfday['20-day Exponential MA'].loc[x] > 0:
                dfday['20-MA'].loc[x]=" ---> BUY-20-MA uptrend *** "
                dfday['20-MA Entr_Signal'].loc[x]=(dfday['Close'].loc[x] - dfday['20-day Exponential MA'].loc[x]).round(0)
                
            elif dfday['Close'].loc[x] - dfday['20-day Exponential MA'].loc[x] < 0:
                dfday['20-MA'].loc[x]=" *** BUY?(close<20-MA)-20-MA uptrend *** "
                dfday['20-MA Entr_Signal'].loc[x]=(dfday['Close'].loc[x] - dfday['20-day Exponential MA'].loc[x]).round(0)

                
            else:
                pass


        if (dfday['20-day Exponential MA'].loc[x].round(0)-dfday['20-day Exponential MA'].shift(1).loc[x].round(0)) < 0:

            if dfday['Close'].loc[x] - dfday['20-day Exponential MA'].loc[x] > 0:
                dfday['20-MA'].loc[x]=" *** SELL?(close>20-MA)-20-MA DWNtrend *** "
                dfday['20-MA Entr_Signal'].loc[x]=(dfday['Close'].loc[x] - dfday['20-day Exponential MA'].loc[x]).round(0)
                

            elif dfday['Close'].loc[x] - dfday['20-day Exponential MA'].loc[x] < 0:
                dfday['20-MA'].loc[x]=" <--- SELL-20-MA DWNtrend *** "
                dfday['20-MA Entr_Signal'].loc[x]=(dfday['Close'].loc[x] - dfday['20-day Exponential MA'].loc[x]).round(0)


##        if dfday['Close'].loc[x] - dfday['20-day Exponential MA'].loc[x] < 0:
##            dfday['20-MA-Exit_Signal']='Exit'


        if dfday['Close'].loc[x] - dfday['Close'].ewm(span=20, adjust=False).mean().loc[x] < 0:
            dfday['20-MA-Exit_Signal'].loc[x]= (dfday['Close'].loc[x] - dfday['Close'].ewm(span=20, adjust=False).mean().loc[x])

        else:
            dfday['20-MA-Exit_Signal'].loc[x]= (dfday['Close'].loc[x] - dfday['Close'].ewm(span=20, adjust=False).mean().loc[x])            
            

            
                
##    print('office_walnut',dfday)
#add

        if (dfday['50-day Exponential MA'].loc[x].round(0)-dfday['50-day Exponential MA'].shift(1).loc[x].round(0)) > 0:
            

            if dfday['Close'].loc[x] - dfday['50-day Exponential MA'].loc[x] > 0:
                dfday['50-MA'].loc[x]=" ---> BUY-50-MA uptrend *** "
                dfday['50-MA Entr_Signal'].loc[x]=(dfday['Close'].loc[x] - dfday['50-day Exponential MA'].loc[x]).round(0)
                
            elif dfday['Close'].loc[x] - dfday['50-day Exponential MA'].loc[x] < 0:
                dfday['50-MA'].loc[x]=" *** BUY?(close<50-MA)-50-MA uptrend *** "
                dfday['50-MA Entr_Signal'].loc[x]=(dfday['Close'].loc[x] - dfday['50-day Exponential MA'].loc[x]).round(0)

                
            else:
                pass


        if (dfday['50-day Exponential MA'].loc[x].round(0)-dfday['50-day Exponential MA'].shift(1).loc[x].round(0)) < 0:

            if dfday['Close'].loc[x] - dfday['50-day Exponential MA'].loc[x] > 0:
                dfday['50-MA'].loc[x]=" *** SELL?(close>50-MA)-50-MA DWNtrend *** "
                dfday['50-MA Entr_Signal'].loc[x]=(dfday['Close'].loc[x] - dfday['50-day Exponential MA'].loc[x]).round(0)
                

            elif dfday['Close'].loc[x] - dfday['50-day Exponential MA'].loc[x] < 0:
                dfday['50-MA'].loc[x]=" <--- SELL-50-MA DWNtrend *** "
                dfday['50-MA Entr_Signal'].loc[x]=(dfday['Close'].loc[x] - dfday['50-day Exponential MA'].loc[x]).round(0)
                

##
##        if dfday['Close'].loc[x] - dfday['50-day Exponential MA'].loc[x] < 0:
##            dfday['50-MA-Exit_Signal']='Exit'


        if dfday['Close'].loc[x] - dfday['Close'].ewm(span=50, adjust=False).mean().loc[x] < 0:
            dfday['50-MA-Exit_Signal'].loc[x]= (dfday['Close'].loc[x] - dfday['Close'].ewm(span=50, adjust=False).mean().loc[x])

        else:
            dfday['50-MA-Exit_Signal'].loc[x]= (dfday['Close'].loc[x] - dfday['Close'].ewm(span=50, adjust=False).mean().loc[x])            
            







##    print('office_walnut',dfday)
##

##
###add

        if (dfday['100-day Exponential MA'].loc[x].round(0)-dfday['100-day Exponential MA'].shift(1).loc[x].round(0)) > 0:
            

            if dfday['Close'].loc[x] - dfday['100-day Exponential MA'].loc[x] > 0:
                dfday['100-MA'].loc[x]=" ---> BUY-100-MA uptrend *** "
                dfday['100-MA Entr_Signal'].loc[x]=(dfday['Close'].loc[x] - dfday['100-day Exponential MA'].loc[x]).round(0)
                
            elif dfday['Close'].loc[x] - dfday['100-day Exponential MA'].loc[x] < 0:
                dfday['100-MA'].loc[x]=" *** BUY?(close<100-MA)-100-MA uptrend *** "
                dfday['100-MA Entr_Signal'].loc[x]=(dfday['Close'].loc[x] - dfday['100-day Exponential MA'].loc[x]).round(0)

                
            else:
                pass


        if (dfday['100-day Exponential MA'].loc[x].round(0)-dfday['100-day Exponential MA'].shift(1).loc[x].round(0)) < 0:

            if dfday['Close'].loc[x] - dfday['100-day Exponential MA'].loc[x] > 0:
                dfday['100-MA'].loc[x]=" *** SELL?(close>100-MA)-100-MA DWNtrend *** "
                dfday['100-MA Entr_Signal'].loc[x]=(dfday['Close'].loc[x] - dfday['100-day Exponential MA'].loc[x]).round(0)
                

            elif dfday['Close'].loc[x] - dfday['100-day Exponential MA'].loc[x] < 0:
                dfday['100-MA'].loc[x]=" <--- SELL-100-MA DWNtrend *** "
                dfday['100-MA Entr_Signal'].loc[x]=(dfday['Close'].loc[x] - dfday['100-day Exponential MA'].loc[x]).round(0)
                

##
##        if dfday['Close'].loc[x] - dfday['100-day Exponential MA'].loc[x] < 0:
##            dfday['100-MA-Exit_Signal']='Exit'



        if dfday['Close'].loc[x] - dfday['Close'].ewm(span=100, adjust=False).mean().loc[x] < 0:
            dfday['100-MA-Exit_Signal'].loc[x]= (dfday['Close'].loc[x] - dfday['Close'].ewm(span=100, adjust=False).mean().loc[x])

        else:
            dfday['100-MA-Exit_Signal'].loc[x]= (dfday['Close'].loc[x] - dfday['Close'].ewm(span=100, adjust=False).mean().loc[x])            
            

            

##    print('office_walnut',dfday)
##
##
###add

        if (dfday['200-day Exponential MA'].loc[x].round(0)-dfday['200-day Exponential MA'].shift(1).loc[x].round(0)) > 0:
            

            if dfday['Close'].loc[x] - dfday['200-day Exponential MA'].loc[x] > 0:
                dfday['200-MA'].loc[x]=" ---> BUY-200-MA uptrend *** "
                dfday['200-MA Entr_Signal'].loc[x]=(dfday['Close'].loc[x] - dfday['200-day Exponential MA'].loc[x]).round(0)
                
            elif dfday['Close'].loc[x] - dfday['200-day Exponential MA'].loc[x] < 0:
                dfday['200-MA'].loc[x]=" *** BUY?(close<200-MA)-200-MA uptrend *** "
                dfday['200-MA Entr_Signal'].loc[x]=(dfday['Close'].loc[x] - dfday['200-day Exponential MA'].loc[x]).round(0)

                
            else:
                pass


        if (dfday['200-day Exponential MA'].loc[x].round(0)-dfday['200-day Exponential MA'].shift(1).loc[x].round(0)) < 0:

            if dfday['Close'].loc[x] - dfday['200-day Exponential MA'].loc[x] > 0:
                dfday['200-MA'].loc[x]=" *** SELL?(close>200-MA)-200-MA DWNtrend *** "
                dfday['200-MA Entr_Signal'].loc[x]=(dfday['Close'].loc[x] - dfday['200-day Exponential MA'].loc[x]).round(0)
                

            elif dfday['Close'].loc[x] - dfday['200-day Exponential MA'].loc[x] < 0:
                dfday['200-MA'].loc[x]=" <--- SELL-200-MA DWNtrend *** "
                dfday['200-MA Entr_Signal'].loc[x]=(dfday['Close'].loc[x] - dfday['200-day Exponential MA'].loc[x]).round(0)



##        if dfday['Close'].loc[x] - dfday['200-day Exponential MA'].loc[x] < 0:
##            dfday['200-MA-Exit_Signal']='Exit'
                

        if dfday['Close'].loc[x] - dfday['Close'].ewm(span=200, adjust=False).mean().loc[x] < 0:
            dfday['200-MA-Exit_Signal'].loc[x]= (dfday['Close'].loc[x] - dfday['Close'].ewm(span=200, adjust=False).mean().loc[x])

        else:
            dfday['200-MA-Exit_Signal'].loc[x]= (dfday['Close'].loc[x] - dfday['Close'].ewm(span=200, adjust=False).mean().loc[x])            
            


    for x in dfday.index:
            dfday['Volume'].loc[x]=numerize.numerize(np.float32(dfday['Volume'].loc[x]).item())

                
    print('dddd',dfday.columns)

##    for x in dfday.index:
##        dfday['3-MA Entr_Signal'].loc(x)=dfday['3-MA Entr_Signal'].loc(x)
    dfday.reset_index(drop=False,inplace=True) 
##    dfday.set_index('Date')

    dfday=dfday[['ticker','Date','stragety','s','HA_Signal','HA','s','price_shift','Close','Volume','s',
             '3-MA Entr_Signal', '5-MA Entr_Signal', '10-MA Entr_Signal', '20-MA Entr_Signal', '50-MA Entr_Signal', '100-MA Entr_Signal','200-MA Entr_Signal','s',
             '3-MA-Exit_Signal','5-MA-Exit_Signal','10-MA-Exit_Signal','20-MA-Exit_Signal','50-MA-Exit_Signal','100-MA-Exit_Signal','200-MA-Exit_Signal']]

    dfday['exit_signal_(>0)']=0
    dfday['exit_signal_(<0)']=0
    
    
    dfday['Enter_signal_(>0)']=0
    dfday['Enter_signal_(<0)']=0
    
    dfday['tot_Enter_signal']=0
    dfday['tot_Exit_signal']=0
    i=1
    
    while i < dfday.shape[0]:
        k2=0
        p2=0
        p3=0
        e2=0
        e3=0

        t2=0
        t3=0
    #    print(i,') ----->   ',x)
        while k2 < dfday.shape[1]:
            
##            print('row:',1,' column: ',k2,'  ',dfday.iloc[1,k2])
##            print('row:',i,' column: ',k2,'  ',dfday.iloc[i,k2])
            if dfday.iloc[i,k2] != '':
                
                if k2 >= 19 and k2 < 26:
                    
                    if int(float(dfday.iloc[i,k2])) > 0:
                        t2=t2+1
                        dfday.iloc[i,31]=t2
    ##                    print(int(float(dfday.iloc[i,k2])),'  p2= ',p2)
                        p2=p2+1 
                        dfday.iloc[i,26]=p2

                    if int(float(dfday.iloc[i,k2])) < 0:
    ##                    print(int(float(dfday.iloc[i,k2])),'  p3= ',p3)
                        p3=p3+1 
                        dfday.iloc[i,27]=p3

#############################################################
            if k2 > 10 and k2 < 18:
                
                
                if dfday.iloc[i,k2] != '':
                    t3=t3+1
                    dfday.iloc[i,30]=t3

                    if int(float(dfday.iloc[i,k2])) > 0:                    
    ##                    print(int(float(dfday.iloc[i,k2])),'  p2= ',p2)
                        e2=e2+1 
                        dfday.iloc[i,28]=e2

                    if int(float(dfday.iloc[i,k2])) < 0:
    ##                    print(int(float(dfday.iloc[i,k2])),'  p3= ',p3)
                        e3=e3+1 
                        dfday.iloc[i,29]=e3  

#############################################################

                    
##                       
            k2=k2+1        
##                
##
##        print('row:',i,' column: ',k2,'  ',dfday.iloc[i,k2])    
        i=i+1
         
##    print("dfday['5-MA Entr_Signal']>0 buy, < 0 sell",'\n','pp office_walnut',dfday.tail(300))
    dfx=dfday
##    print(dfxx.tail(300),'\n\n',dfxx.columns)
    dfx=dfx[['ticker', 'Date', 'stragety', 's', 'HA_Signal', 'HA', 's', 'price_shift', 'Close', 'Volume', 's', '3-MA Entr_Signal']]
##              '5-MA Entr_Signal', '10-MA Entr_Signal', '20-MA Entr_Signal', '50-MA Entr_Signal', '100-MA Entr_Signal', '200-MA Entr_Signal',
##              's', '3-MA-Exit_Signal', '5-MA-Exit_Signal', '10-MA-Exit_Signal', '20-MA-Exit_Signal', '50-MA-Exit_Signal', '100-MA-Exit_Signal',
##              '200-MA-Exit_Signal', 'exit_signal_(>0)', 'exit_signal_(<0)', 'Enter_signal_(>0)', 'Enter_signal_(<0)', 'tot_Enter_signal',
##              'tot_Exit_signal']]

##    dfx.reset_index(inplace=False)
##    dfx.set_index('Date')

##    print('before',dfday.shape)
    
##    print('after',dfday.shape)
##    for x in dfday.index:
##        dfday['dde8'].loc[x] = dfday['ticker'].loc[x]
##        print(dfx['dde'])

    dfday['SELL_PUT_Enter_signal_(>0)'] = ''
    g2=dfday.columns.get_loc('SELL_PUT_Enter_signal_(>0)')
##    g3=dfday.columns.get_loc('tot_Enter_signal')

    dfday['SELL_CALL_Enter_signal_(<0)'] = ''
    g3=dfday.columns.get_loc('SELL_CALL_Enter_signal_(<0)')


    dfday['SELL_CALL_Exit_signal_(>0)'] = ''
    g4=dfday.columns.get_loc('SELL_CALL_Exit_signal_(>0)')
##    g3=dfday.columns.get_loc('tot_Exit_signal')

    dfday['Sell_PUT_EXIT_signal_(<0)'] = ''
    g5=dfday.columns.get_loc('Sell_PUT_EXIT_signal_(<0)')
##    g3=dfday.columns.get_loc('tot_Exit_signal')
    
    i=0
##    j=dfday.shape[1]
    while (i < dfday.shape[0]):
        
##        dfday.iloc[i,dfday.shape[1]-1]=str(dfday['Enter_signal_(>0)'].loc[i])+'/'+str(dfday['tot_Enter_signal'].loc[i])
##        dfday['aEnter_signal_(>0)'].iloc[i]=str(dfday['Enter_signal_(>0)'].loc[i])+'/'+str(dfday['tot_Enter_signal'].loc[i])
        dfday.iloc[i,g2]=str(dfday['Enter_signal_(>0)'].loc[i])+'/'+str(dfday['tot_Enter_signal'].loc[i])
        dfday.iloc[i,g3]=str(dfday['Enter_signal_(<0)'].loc[i])+'/'+str(dfday['tot_Enter_signal'].loc[i])
        dfday.iloc[i,g4]=str(dfday['exit_signal_(>0)'].loc[i])+'/'+str(dfday['tot_Exit_signal'].loc[i])
        dfday.iloc[i,g5]=str(dfday['exit_signal_(<0)'].loc[i])+'/'+str(dfday['tot_Exit_signal'].loc[i])
        i=i+1
##        
##    rslt_df = dataframe.loc[dataframe['Percentage'] > 70]
##    dfday=dfday['Volume'] > 0
    print('Daily chart ----->  ',dfday.tail(223))
    

################################## section 2 hourly #####################################################################################
    
##    perd='2d'
    perd=pdays
##    intervl='60m'
    intervl=ptime

    dfi = pd.DataFrame()
##    ticker='amc'
    print('--- Running ---')
    ### [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]
    ##
    ####g=input("Entr_Signal Ticker :")
    ###perd=input("Entr_Signal no of days '5d','2d','1d' :")
    ###intervl=input("Entr_Signal mins '5m','1m' :")
    ##
    ##
    ###df=pd.DataFrame()
    ###Interval required 5 minutes
##    data = yf.download(tickers=ticker, period=perd, interval=intervl,prepost = True)
    data = yf.download(tickers=ticker, period=perd, interval=intervl,prepost=pprepost)
    dfi=pd.DataFrame(data)

    dfi['ticker']=g
    dfi.fillna(method='bfill', axis=0, inplace=True)
##    dfi['200-day Exponential MA'] = ta.ema(dfi["Close"], length=200)
    
    dfi['200-day Exponential MA'] = dfi['Close'].ewm(span=200, adjust=True).mean()
    dfi['100-day Exponential MA'] = dfi['Close'].ewm(span=100, adjust=True).mean()
    dfi['50-day Exponential MA'] = dfi['Close'].ewm(span=50, adjust=True).mean()
    
    dfi['20-day Exponential MA'] = dfi['Close'].ewm(span=3, adjust=True).mean()
    dfi['10-day Exponential MA'] = dfi['Close'].ewm(span=10, adjust=True).mean()
    dfi['5-day Exponential MA'] = dfi['Close'].ewm(span=5, adjust=True).mean()
    dfi['3-day Exponential MA'] = dfi['Close'].ewm(span=3, adjust=True).mean()

    dfi['3day_s']=dfi['Close']-dfi['3-day Exponential MA']
    dfi['5day_s']=dfi['Close']-dfi['5-day Exponential MA']
    dfi['10day_s']=dfi['Close']-dfi['10-day Exponential MA']
    dfi['20day_s']=dfi['Close']-dfi['20-day Exponential MA']
    dfi['50day_s']=dfi['Close']-dfi['50-day Exponential MA']
    dfi['100day_s']=dfi['Close']-dfi['100-day Exponential MA']
    dfi['200day_s']=dfi['Close']-dfi['200-day Exponential MA']
    dfi['price_shift']=(dfi['Close']-dfi['Close'].shift(1)).round(2)
####    print(dfi)
####    print(dfi.columns)

####    dfi = intraday.loc[1:30,:]
    dfi = dfi.loc[:,:]
##    dfi = intraday.loc[:63,:]
####    print(dfi)
####    print(dfi.columns)

    mpf.plot(dfi, block=False,type='candle', volume=True, figratio=(15, 15), style='yahoo', mav=(200,100,50,20,10,3), title=ticker+' - ('+perd + ' - '+intervl+')'
             +
             str(p).split()[1]+' / (diff) '+str(p2).split()[1] + ', Open: '+ str(p5).split()[1] + ' ,low: '+str(p3).split()[1]+ ' ,High: '+ str(p4).split()[1]
             + ', day swing: ' + str(u3).split('.')[0]

             )


    dfi['HA_Signal']=''
    dfi['down']=''
    dfi['a_Close']=''
    dfi['a_High']=''
    dfi['a_Low']=''
    dfi['a_Open']=''
    dfi['HA']=''
    dfi['Opena']=''
    dfi['green']=''
    dfi['greenby']=''
    dfi['s']=' * '

    for x in dfi.index:
        dfi['s'].loc[x]='*'
        dfi['Opena'].loc[x]=int(dfi['Open'].loc[x])
        if dfi['Close'].loc[x]-dfi['Open'].loc[x] > 0:
            dfi['green'].loc[x]='Green'
            dfi['greenby'].loc[x]=dfi['Close'].loc[x]-dfi['Open'].loc[x]
            #            print(x,'  ','Green','  ',dfi['ns'].loc[x])
        else:
            dfi['green'].loc[x]='Red'
            dfi['greenby'].loc[x]=dfi['Close'].loc[x]-dfi['Open'].loc[x]

        dfi['a_Close'].loc[x]=1/4*(dfi['Open'].loc[x]+dfi['High'].loc[x]+dfi['Low'].loc[x]+dfi['Close'].loc[x])
        dfi['a_Open'].loc[x]=1/2*(dfi['Open'].shift(1).loc[x]+dfi['Close'].shift(1).loc[x])
        dfi['High'].loc[x]=dfi['High'].loc[x]
        dfi['Low'].loc[x]=dfi['Low'].loc[x]
        dfi['a_High'].loc[x]=max(dfi['High'].loc[x],dfi['a_Open'].loc[x],dfi['a_Close'].loc[x])
        dfi['a_Low'].loc[x]=min(dfi['Low'].loc[x],dfi['a_Open'].loc[x],dfi['a_Close'].loc[x])
     #   dfi['a_Open'].loc[x]=1/2*(dfi['Open'].shift(1).loc[x]+dfi['Close'].shift(1).loc[x])
        dfi['HA'].loc[x]=dfi['a_Close'].loc[x]-dfi['a_Open'].loc[x]




    #   if dfi['a_Close'].loc[x] > dfi['a_Open'].loc[x]:
        if dfi['HA'].loc[x] > 0:
            dfi['HA_Signal'].loc[x]='HA_Green'
        elif dfi['HA'].loc[x] < 0:
            dfi['HA_Signal'].loc[x]='HA_Red'

    for x in dfi.index:

        dfi['greenby'].loc[x]=dfi['greenby'].loc[x].round(2)
        dfi['HA'].loc[x]=dfi['HA'].loc[x].round(2)
        dfi['a_High'].loc[x]=dfi['a_High'].loc[x].round(2)
        dfi['a_Low'].loc[x]=dfi['a_Low'].loc[x].round(2)
        dfi['a_Close'].loc[x]=dfi['a_Close'].loc[x].round(2)
        dfi['a_Open'].loc[x]=dfi['a_Open'].loc[x].round(2)

    
    dfi['(cl_3day)']=''
    dfi['(cl_5day)']=''
    for x in dfi.index:
        dfi['(cl_3day)'].loc[x]=(dfi['Close'].loc[x]-dfi['3-day Exponential MA'].loc[x]).round(2)
        dfi['(cl_5day)'].loc[x]=(dfi['Close'].loc[x]-dfi['10-day Exponential MA'].loc[x]).round(2)
        
    dfi['stragety']=''
    for x in dfi.index:
        if (dfi['greenby'].loc[x] < 0 and dfi['(cl_3day)'].loc[x] < 0):
            dfi['stragety'].loc[x]=str('Red(')+str(dfi['greenby'].loc[x])+')_Call sell'
        elif (dfi['greenby'].loc[x] > 0 and dfi['(cl_3day)'].loc[x] > 0):
            dfi['stragety'].loc[x]=str('Green(')+str(dfi['greenby'].loc[x])+')_put sell'
        else:
            pass


    dfi.reset_index(drop=False,inplace=True)    
    print('sleeptrain',dfi)
    print('sleeptrain_columns',dfi.columns)
##    print(dfi[['Datetime', 'Open', 'High', 'Low']])
###################################################################
#############################

##    df['5']=''
##    df.reset_index(inplace=True)

##    dfi=pd.concat(df['Datetime'],[df['ticker'],df['Close'],df['3-day Exponential MA'],
##                                   df['5-day Exponential MA'],df['10-day Exponential MA'],
##                                   df['20-day Exponential MA'],df['50-day Exponential MA'],
##                                   df['100-day Exponential MA'],df['200-day Exponential MA']
##                                   ],axis=1)
##

                                   
##                                   ,
##                                   

##    dfia=dfi[['Datetime','ticker','Close','3-day Exponential MA','5-day Exponential MA','10-day Exponential MA','20-day Exponential MA','50-day Exponential MA','100-day Exponential MA','200-day Exponential MA']]
##    print('dd',dfia)
    dfi['3-MA']=''
    dfi['5-MA']=''
    dfi['10-MA']=''
    dfi['20-MA']=''
    dfi['50-MA']=''
    dfi['100-MA']=''
    dfi['200-MA']=''

    dfi['3-MA Entr_Signal']=''   
    dfi['5-MA Entr_Signal']=''
    dfi['10-MA Entr_Signal']=''
    dfi['20-MA Entr_Signal']=''
    dfi['50-MA Entr_Signal']=''
    dfi['100-MA Entr_Signal']=''
    dfi['200-MA Entr_Signal']=''

    dfi['3-MA-Exit_Signal']=''
    dfi['5-MA-Exit_Signal']=''
    dfi['10-MA-Exit_Signal']=''
    dfi['20-MA-Exit_Signal']=''
    dfi['50-MA-Exit_Signal']=''
    dfi['100-MA-Exit_Signal']=''
    dfi['200-MA-Exit_Signal']=''

##    print(dfi)
    i=0
    for x in dfi.index:
##        print(' 3day/shift ',dfi['Date'].loc[x],dfi['3-day Exponential MA'].loc[x].round(0)-dfi['3-day Exponential MA'].shift(1).loc[x].round(0))
              
##        print(dfi['Close'].loc[x] , dfi['3-day Exponential MA'].loc[x],dfi['3-day Exponential MA'].shift(1).loc[x])
        if (dfi['3-day Exponential MA'].loc[x].round(0)-dfi['3-day Exponential MA'].shift(1).loc[x].round(0)) > 0:
            
            if dfi['Close'].loc[x] - dfi['3-day Exponential MA'].loc[x] > 0:
                dfi['3-MA'].loc[x]=" ---> BUY-3-MA uptrend *** "
                dfi['3-MA Entr_Signal'].loc[x]=(dfi['Close'].loc[x] - dfi['3-day Exponential MA'].loc[x]).round(0)
                
            elif dfi['Close'].loc[x] - dfi['3-day Exponential MA'].loc[x] < 0:
                dfi['3-MA'].loc[x]=" *** BUY?(close<3MA)-3-MA uptrend *** "
                dfi['3-MA Entr_Signal'].loc[x]=(dfi['Close'].loc[x] - dfi['3-day Exponential MA'].loc[x]).round(0)

                
            else:
                pass


        if (dfi['3-day Exponential MA'].loc[x].round(0)-dfi['3-day Exponential MA'].shift(1).loc[x].round(0)) < 0:
            
            if dfi['Close'].loc[x] - dfi['3-day Exponential MA'].loc[x] > 0:
                dfi['3-MA'].loc[x]=" *** SELL?(close>3MA)-3-MA DWNtrend *** "
                dfi['3-MA Entr_Signal'].loc[x]=(dfi['Close'].loc[x] - dfi['3-day Exponential MA'].loc[x]).round(0)
                

            elif dfi['Close'].loc[x] - dfi['3-day Exponential MA'].loc[x] < 0:
                dfi['3-MA'].loc[x]=" <--- SELL-3-MA DWNtrend *** "
                dfi['3-MA Entr_Signal'].loc[x]=(dfi['Close'].loc[x] - dfi['3-day Exponential MA'].loc[x]).round(0)
                

            else:
                pass


##        if dfi['Close'].loc[x] - dfi['3-day Exponential MA'].loc[x] < 0:
##            dfi['3-MA-Exit_Signal']='Exit'




        if dfi['Close'].loc[x] - dfi['Close'].ewm(span=3, adjust=False).mean().loc[x] < 0:
            dfi['3-MA-Exit_Signal'].loc[x]= (dfi['Close'].loc[x] - dfi['Close'].ewm(span=3, adjust=False).mean().loc[x])

        else:
            dfi['3-MA-Exit_Signal'].loc[x]= (dfi['Close'].loc[x] - dfi['Close'].ewm(span=3, adjust=False).mean().loc[x])            
            
            
##    print('office_walnut',dfi)            
##################################################
#add

        if (dfi['5-day Exponential MA'].loc[x].round(0)-dfi['5-day Exponential MA'].shift(1).loc[x].round(0)) > 0: #(MA slopes upward)
            

            if dfi['Close'].loc[x] - dfi['5-day Exponential MA'].loc[x] > 0:  #(close price above MA)
                dfi['5-MA'].loc[x]=" ---> BUY-5-MA uptrend *** "  # buy signal
                dfi['5-MA Entr_Signal'].loc[x]=(dfi['Close'].loc[x] - dfi['5-day Exponential MA'].loc[x]).round(0)
                
            elif dfi['Close'].loc[x] - dfi['5-day Exponential MA'].loc[x] < 0: #(close price above MA)
                dfi['5-MA'].loc[x]=" *** BUY?(close<5-MA)-5-MA uptrend *** " # buy signal
                dfi['5-MA Entr_Signal'].loc[x]=(dfi['Close'].loc[x] - dfi['5-day Exponential MA'].loc[x]).round(0)

            elif dfi['Close'].loc[x] - dfi['5-day Exponential MA'].loc[x] == 0:
                dfi['5-MA'].loc[x]="close=5-day_exp"
                dfi['5-MA Entr_Signal'].loc[x]=(dfi['Close'].loc[x] - dfi['5-day Exponential MA'].loc[x]).round(0)
                
            else:
                pass


        if (dfi['5-day Exponential MA'].loc[x].round(0)-dfi['5-day Exponential MA'].shift(1).loc[x].round(0)) < 0:

            if dfi['Close'].loc[x] - dfi['5-day Exponential MA'].loc[x] > 0:
                dfi['5-MA'].loc[x]=" *** SELL?(close>5-MA)-5-MA DWNtrend *** "
                dfi['5-MA Entr_Signal'].loc[x]=(dfi['Close'].loc[x] - dfi['5-day Exponential MA'].loc[x]).round(0)
                

            elif dfi['Close'].loc[x] - dfi['5-day Exponential MA'].loc[x] < 0:
                dfi['5-MA'].loc[x]=" <--- SELL-5-MA DWNtrend *** "
                dfi['5-MA Entr_Signal'].loc[x]=(dfi['Close'].loc[x] - dfi['5-day Exponential MA'].loc[x]).round(0)

##        if dfi['Close'].loc[x] - dfi['5-day Exponential MA'].loc[x] < 0:
##            dfi['5-MA-Exit_Signal']='Exit'
##                
####        if dfi['Close'].loc[x] - dfi['5-day Exponential MA'].loc[x] < 0:
####            dfi['5-MA'].loc[x]="stupid"
####            dfi['5-MA Entr_Signal'].loc[x]="stupid"
##
##        else:
##            pass


        if dfi['Close'].loc[x] - dfi['Close'].ewm(span=5, adjust=False).mean().loc[x] < 0:
            dfi['5-MA-Exit_Signal'].loc[x]= (dfi['Close'].loc[x] - dfi['Close'].ewm(span=5, adjust=False).mean().loc[x])

        else:
            dfi['5-MA-Exit_Signal'].loc[x]= (dfi['Close'].loc[x] - dfi['Close'].ewm(span=5, adjust=False).mean().loc[x])            
            

###########################################
###add
##
        if (dfi['10-day Exponential MA'].loc[x].round(0)-dfi['10-day Exponential MA'].shift(1).loc[x].round(0)) > 0:
            

            if dfi['Close'].loc[x] - dfi['10-day Exponential MA'].loc[x] > 0:
                dfi['10-MA'].loc[x]=" ---> BUY-10-MA uptrend *** "
                dfi['10-MA Entr_Signal'].loc[x]=(dfi['Close'].loc[x] - dfi['10-day Exponential MA'].loc[x]).round(0)
                
            elif dfi['Close'].loc[x] - dfi['10-day Exponential MA'].loc[x] < 0:
                dfi['10-MA'].loc[x]=" *** BUY?(close<10-MA)-10-MA uptrend *** "
                dfi['10-MA Entr_Signal'].loc[x]=(dfi['Close'].loc[x] - dfi['10-day Exponential MA'].loc[x]).round(0)

                
            else:
                pass


        if (dfi['10-day Exponential MA'].loc[x].round(0)-dfi['10-day Exponential MA'].shift(1).loc[x].round(0)) < 0:

            if dfi['Close'].loc[x] - dfi['10-day Exponential MA'].loc[x] > 0:
                dfi['10-MA'].loc[x]=" *** SELL?(close>10-MA)-10-MA DWNtrend *** "
                dfi['10-MA Entr_Signal'].loc[x]=(dfi['Close'].loc[x] - dfi['10-day Exponential MA'].loc[x]).round(0)
                

            elif dfi['Close'].loc[x] - dfi['10-day Exponential MA'].loc[x] < 0:
                dfi['10-MA'].loc[x]=" <--- SELL-10-MA DWNtrend *** "
                dfi['10-MA Entr_Signal'].loc[x]=(dfi['Close'].loc[x] - dfi['10-day Exponential MA'].loc[x]).round(0)
                

            else:
                pass


##        if dfi['Close'].loc[x] - dfi['10-day Exponential MA'].loc[x] < 0:
##            dfi['10-MA-Exit_Signal']='Exit'


        if dfi['Close'].loc[x] - dfi['Close'].ewm(span=10, adjust=False).mean().loc[x] < 0:
            dfi['10-MA-Exit_Signal'].loc[x]= (dfi['Close'].loc[x] - dfi['Close'].ewm(span=10, adjust=False).mean().loc[x])

        else:
            dfi['10-MA-Exit_Signal'].loc[x]= (dfi['Close'].loc[x] - dfi['Close'].ewm(span=10, adjust=False).mean().loc[x])            
            


            
##    print('office_walnut',dfi)
#add
##            
###add
##
        if (dfi['20-day Exponential MA'].loc[x].round(0)-dfi['20-day Exponential MA'].shift(1).loc[x].round(0)) > 0:
            

            if dfi['Close'].loc[x] - dfi['20-day Exponential MA'].loc[x] > 0:
                dfi['20-MA'].loc[x]=" ---> BUY-20-MA uptrend *** "
                dfi['20-MA Entr_Signal'].loc[x]=(dfi['Close'].loc[x] - dfi['20-day Exponential MA'].loc[x]).round(0)
                
            elif dfi['Close'].loc[x] - dfi['20-day Exponential MA'].loc[x] < 0:
                dfi['20-MA'].loc[x]=" *** BUY?(close<20-MA)-20-MA uptrend *** "
                dfi['20-MA Entr_Signal'].loc[x]=(dfi['Close'].loc[x] - dfi['20-day Exponential MA'].loc[x]).round(0)

                
            else:
                pass


        if (dfi['20-day Exponential MA'].loc[x].round(0)-dfi['20-day Exponential MA'].shift(1).loc[x].round(0)) < 0:

            if dfi['Close'].loc[x] - dfi['20-day Exponential MA'].loc[x] > 0:
                dfi['20-MA'].loc[x]=" *** SELL?(close>20-MA)-20-MA DWNtrend *** "
                dfi['20-MA Entr_Signal'].loc[x]=(dfi['Close'].loc[x] - dfi['20-day Exponential MA'].loc[x]).round(0)
                

            elif dfi['Close'].loc[x] - dfi['20-day Exponential MA'].loc[x] < 0:
                dfi['20-MA'].loc[x]=" <--- SELL-20-MA DWNtrend *** "
                dfi['20-MA Entr_Signal'].loc[x]=(dfi['Close'].loc[x] - dfi['20-day Exponential MA'].loc[x]).round(0)


##        if dfi['Close'].loc[x] - dfi['20-day Exponential MA'].loc[x] < 0:
##            dfi['20-MA-Exit_Signal']='Exit'


        if dfi['Close'].loc[x] - dfi['Close'].ewm(span=20, adjust=False).mean().loc[x] < 0:
            dfi['20-MA-Exit_Signal'].loc[x]= (dfi['Close'].loc[x] - dfi['Close'].ewm(span=20, adjust=False).mean().loc[x])

        else:
            dfi['20-MA-Exit_Signal'].loc[x]= (dfi['Close'].loc[x] - dfi['Close'].ewm(span=20, adjust=False).mean().loc[x])            
            

            
                
##    print('office_walnut',dfi)
#add

        if (dfi['50-day Exponential MA'].loc[x].round(0)-dfi['50-day Exponential MA'].shift(1).loc[x].round(0)) > 0:
            

            if dfi['Close'].loc[x] - dfi['50-day Exponential MA'].loc[x] > 0:
                dfi['50-MA'].loc[x]=" ---> BUY-50-MA uptrend *** "
                dfi['50-MA Entr_Signal'].loc[x]=(dfi['Close'].loc[x] - dfi['50-day Exponential MA'].loc[x]).round(0)
                
            elif dfi['Close'].loc[x] - dfi['50-day Exponential MA'].loc[x] < 0:
                dfi['50-MA'].loc[x]=" *** BUY?(close<50-MA)-50-MA uptrend *** "
                dfi['50-MA Entr_Signal'].loc[x]=(dfi['Close'].loc[x] - dfi['50-day Exponential MA'].loc[x]).round(0)

                
            else:
                pass


        if (dfi['50-day Exponential MA'].loc[x].round(0)-dfi['50-day Exponential MA'].shift(1).loc[x].round(0)) < 0:

            if dfi['Close'].loc[x] - dfi['50-day Exponential MA'].loc[x] > 0:
                dfi['50-MA'].loc[x]=" *** SELL?(close>50-MA)-50-MA DWNtrend *** "
                dfi['50-MA Entr_Signal'].loc[x]=(dfi['Close'].loc[x] - dfi['50-day Exponential MA'].loc[x]).round(0)
                

            elif dfi['Close'].loc[x] - dfi['50-day Exponential MA'].loc[x] < 0:
                dfi['50-MA'].loc[x]=" <--- SELL-50-MA DWNtrend *** "
                dfi['50-MA Entr_Signal'].loc[x]=(dfi['Close'].loc[x] - dfi['50-day Exponential MA'].loc[x]).round(0)
                

##
##        if dfi['Close'].loc[x] - dfi['50-day Exponential MA'].loc[x] < 0:
##            dfi['50-MA-Exit_Signal']='Exit'


        if dfi['Close'].loc[x] - dfi['Close'].ewm(span=50, adjust=False).mean().loc[x] < 0:
            dfi['50-MA-Exit_Signal'].loc[x]= (dfi['Close'].loc[x] - dfi['Close'].ewm(span=50, adjust=False).mean().loc[x])

        else:
            dfi['50-MA-Exit_Signal'].loc[x]= (dfi['Close'].loc[x] - dfi['Close'].ewm(span=50, adjust=False).mean().loc[x])            
            







##    print('office_walnut',dfi)
##

##
###add

        if (dfi['100-day Exponential MA'].loc[x].round(0)-dfi['100-day Exponential MA'].shift(1).loc[x].round(0)) > 0:
            

            if dfi['Close'].loc[x] - dfi['100-day Exponential MA'].loc[x] > 0:
                dfi['100-MA'].loc[x]=" ---> BUY-100-MA uptrend *** "
                dfi['100-MA Entr_Signal'].loc[x]=(dfi['Close'].loc[x] - dfi['100-day Exponential MA'].loc[x]).round(0)
                
            elif dfi['Close'].loc[x] - dfi['100-day Exponential MA'].loc[x] < 0:
                dfi['100-MA'].loc[x]=" *** BUY?(close<100-MA)-100-MA uptrend *** "
                dfi['100-MA Entr_Signal'].loc[x]=(dfi['Close'].loc[x] - dfi['100-day Exponential MA'].loc[x]).round(0)

                
            else:
                pass


        if (dfi['100-day Exponential MA'].loc[x].round(0)-dfi['100-day Exponential MA'].shift(1).loc[x].round(0)) < 0:

            if dfi['Close'].loc[x] - dfi['100-day Exponential MA'].loc[x] > 0:
                dfi['100-MA'].loc[x]=" *** SELL?(close>100-MA)-100-MA DWNtrend *** "
                dfi['100-MA Entr_Signal'].loc[x]=(dfi['Close'].loc[x] - dfi['100-day Exponential MA'].loc[x]).round(0)
                

            elif dfi['Close'].loc[x] - dfi['100-day Exponential MA'].loc[x] < 0:
                dfi['100-MA'].loc[x]=" <--- SELL-100-MA DWNtrend *** "
                dfi['100-MA Entr_Signal'].loc[x]=(dfi['Close'].loc[x] - dfi['100-day Exponential MA'].loc[x]).round(0)
                

##
##        if dfi['Close'].loc[x] - dfi['100-day Exponential MA'].loc[x] < 0:
##            dfi['100-MA-Exit_Signal']='Exit'



        if dfi['Close'].loc[x] - dfi['Close'].ewm(span=100, adjust=False).mean().loc[x] < 0:
            dfi['100-MA-Exit_Signal'].loc[x]= (dfi['Close'].loc[x] - dfi['Close'].ewm(span=100, adjust=False).mean().loc[x])

        else:
            dfi['100-MA-Exit_Signal'].loc[x]= (dfi['Close'].loc[x] - dfi['Close'].ewm(span=100, adjust=False).mean().loc[x])            
            

            

##    print('office_walnut',dfi)
##
##
###add

        if (dfi['200-day Exponential MA'].loc[x].round(0)-dfi['200-day Exponential MA'].shift(1).loc[x].round(0)) > 0:
            

            if dfi['Close'].loc[x] - dfi['200-day Exponential MA'].loc[x] > 0:
                dfi['200-MA'].loc[x]=" ---> BUY-200-MA uptrend *** "
                dfi['200-MA Entr_Signal'].loc[x]=(dfi['Close'].loc[x] - dfi['200-day Exponential MA'].loc[x]).round(0)
                
            elif dfi['Close'].loc[x] - dfi['200-day Exponential MA'].loc[x] < 0:
                dfi['200-MA'].loc[x]=" *** BUY?(close<200-MA)-200-MA uptrend *** "
                dfi['200-MA Entr_Signal'].loc[x]=(dfi['Close'].loc[x] - dfi['200-day Exponential MA'].loc[x]).round(0)

                
            else:
                pass


        if (dfi['200-day Exponential MA'].loc[x].round(0)-dfi['200-day Exponential MA'].shift(1).loc[x].round(0)) < 0:

            if dfi['Close'].loc[x] - dfi['200-day Exponential MA'].loc[x] > 0:
                dfi['200-MA'].loc[x]=" *** SELL?(close>200-MA)-200-MA DWNtrend *** "
                dfi['200-MA Entr_Signal'].loc[x]=(dfi['Close'].loc[x] - dfi['200-day Exponential MA'].loc[x]).round(0)
                

            elif dfi['Close'].loc[x] - dfi['200-day Exponential MA'].loc[x] < 0:
                dfi['200-MA'].loc[x]=" <--- SELL-200-MA DWNtrend *** "
                dfi['200-MA Entr_Signal'].loc[x]=(dfi['Close'].loc[x] - dfi['200-day Exponential MA'].loc[x]).round(0)



##        if dfi['Close'].loc[x] - dfi['200-day Exponential MA'].loc[x] < 0:
##            dfi['200-MA-Exit_Signal']='Exit'
                

        if dfi['Close'].loc[x] - dfi['Close'].ewm(span=200, adjust=False).mean().loc[x] < 0:
            dfi['200-MA-Exit_Signal'].loc[x]= (dfi['Close'].loc[x] - dfi['Close'].ewm(span=200, adjust=False).mean().loc[x])

        else:
            dfi['200-MA-Exit_Signal'].loc[x]= (dfi['Close'].loc[x] - dfi['Close'].ewm(span=200, adjust=False).mean().loc[x])            
            


    for x in dfi.index:
            dfi['Volume'].loc[x]=numerize.numerize(np.float32(dfi['Volume'].loc[x]).item())

                
    print('dddd',dfi.columns)

##    for x in dfi.index:
##        dfi['3-MA Entr_Signal'].loc(x)=dfi['3-MA Entr_Signal'].loc(x)
    dfi.set_index('Datetime')

    dfi=dfi[['ticker','Datetime','stragety','s','HA_Signal','HA','s','price_shift','Close','Volume','s',
             '3-MA Entr_Signal', '5-MA Entr_Signal', '10-MA Entr_Signal', '20-MA Entr_Signal', '50-MA Entr_Signal', '100-MA Entr_Signal','200-MA Entr_Signal','s',
             '3-MA-Exit_Signal','5-MA-Exit_Signal','10-MA-Exit_Signal','20-MA-Exit_Signal','50-MA-Exit_Signal','100-MA-Exit_Signal','200-MA-Exit_Signal']]

    dfi['exit_signal_(>0)']=0
    dfi['exit_signal_(<0)']=0
    
    
    dfi['Enter_signal_(>0)']=0
    dfi['Enter_signal_(<0)']=0
    
    dfi['tot_Enter_signal']=0
    dfi['tot_Exit_signal']=0
    i=1
    
    while i < dfi.shape[0]:
        k2=0
        p2=0
        p3=0
        e2=0
        e3=0

        t2=0
        t3=0
    #    print(i,') ----->   ',x)
        while k2 < dfi.shape[1]:
            
##            print('row:',1,' column: ',k2,'  ',dfi.iloc[1,k2])
##            print('row:',i,' column: ',k2,'  ',dfi.iloc[i,k2])
            if dfi.iloc[i,k2] != '':
                
                if k2 >= 19 and k2 < 26:
                    
                    if int(float(dfi.iloc[i,k2])) > 0:
                        t2=t2+1
                        dfi.iloc[i,31]=t2
    ##                    print(int(float(dfi.iloc[i,k2])),'  p2= ',p2)
                        p2=p2+1 
                        dfi.iloc[i,26]=p2

                    if int(float(dfi.iloc[i,k2])) < 0:
    ##                    print(int(float(dfi.iloc[i,k2])),'  p3= ',p3)
                        p3=p3+1 
                        dfi.iloc[i,27]=p3

#############################################################
            if k2 > 10 and k2 < 18:
                
                
                if dfi.iloc[i,k2] != '':
                    t3=t3+1
                    dfi.iloc[i,30]=t3
                    if int(float(dfi.iloc[i,k2])) > 0:                    
    ##                    print(int(float(dfi.iloc[i,k2])),'  p2= ',p2)
                        e2=e2+1 
                        dfi.iloc[i,28]=e2

                    if int(float(dfi.iloc[i,k2])) < 0:
    ##                    print(int(float(dfi.iloc[i,k2])),'  p3= ',p3)
                        e3=e3+1 
                        dfi.iloc[i,29]=e3  

#############################################################

                    
##                       
            k2=k2+1        
##                
##
##        print('row:',i,' column: ',k2,'  ',dfi.iloc[i,k2])    
        i=i+1
         
##    print("dfi['5-MA Entr_Signal']>0 buy, < 0 sell",'\n','pp office_walnut',dfi.tail(300))
    dfx=dfi
##    print(dfxx.tail(300),'\n\n',dfxx.columns)
    dfx=dfx[['ticker', 'Datetime', 'stragety', 's', 'HA_Signal', 'HA', 's', 'price_shift', 'Close', 'Volume', 's', '3-MA Entr_Signal']]
##              '5-MA Entr_Signal', '10-MA Entr_Signal', '20-MA Entr_Signal', '50-MA Entr_Signal', '100-MA Entr_Signal', '200-MA Entr_Signal',
##              's', '3-MA-Exit_Signal', '5-MA-Exit_Signal', '10-MA-Exit_Signal', '20-MA-Exit_Signal', '50-MA-Exit_Signal', '100-MA-Exit_Signal',
##              '200-MA-Exit_Signal', 'exit_signal_(>0)', 'exit_signal_(<0)', 'Enter_signal_(>0)', 'Enter_signal_(<0)', 'tot_Enter_signal',
##              'tot_Exit_signal']]

##    dfx.reset_index(inplace=False)
##    dfx.set_index('Datetime')

##    print('before',dfi.shape)
    
##    print('after',dfi.shape)
##    for x in dfi.index:
##        dfi['dde8'].loc[x] = dfi['ticker'].loc[x]
##        print(dfx['dde'])

    dfi['SELL_PUT_Enter_signal_(>0)'] = ''
    g2=dfi.columns.get_loc('SELL_PUT_Enter_signal_(>0)')
##    g3=dfi.columns.get_loc('tot_Enter_signal')

    dfi['SELL_CALL_Enter_signal_(<0)'] = ''
    g3=dfi.columns.get_loc('SELL_CALL_Enter_signal_(<0)')


    dfi['SELL_CALL_Exit_signal_(>0)'] = ''
    g4=dfi.columns.get_loc('SELL_CALL_Exit_signal_(>0)')
##    g3=dfi.columns.get_loc('tot_Exit_signal')

    dfi['Sell_PUT_EXIT_signal_(<0)'] = ''
    g5=dfi.columns.get_loc('Sell_PUT_EXIT_signal_(<0)')
##    g3=dfi.columns.get_loc('tot_Exit_signal')
    
    i=0
##    j=dfi.shape[1]
    while (i < dfi.shape[0]):
        
##        dfi.iloc[i,dfi.shape[1]-1]=str(dfi['Enter_signal_(>0)'].loc[i])+'/'+str(dfi['tot_Enter_signal'].loc[i])
##        dfi['aEnter_signal_(>0)'].iloc[i]=str(dfi['Enter_signal_(>0)'].loc[i])+'/'+str(dfi['tot_Enter_signal'].loc[i])
        dfi.iloc[i,g2]=str(dfi['Enter_signal_(>0)'].loc[i])+'/'+str(dfi['tot_Enter_signal'].loc[i])
        dfi.iloc[i,g3]=str(dfi['Enter_signal_(<0)'].loc[i])+'/'+str(dfi['tot_Enter_signal'].loc[i])
        dfi.iloc[i,g4]=str(dfi['exit_signal_(>0)'].loc[i])+'/'+str(dfi['tot_Exit_signal'].loc[i])
        dfi.iloc[i,g5]=str(dfi['exit_signal_(<0)'].loc[i])+'/'+str(dfi['tot_Exit_signal'].loc[i])
        i=i+1
##        
##    rslt_df = dataframe.loc[dataframe['Percentage'] > 70]
##    dfi=dfi['Volume'] > 0
    print('Hourly chart ----->  ',dfi.tail(223))
########################################################################    

##g='^NDX'
##g='^DJI'
##g='^SPX'
##g='spy'
##g='tsla'
g='MRNA'
##g='mstr'
##g='amzn'
##g='amc'
##g='gme'
##g='ccl'    
pdays='2d'
ptime='60m'
pprepost=True
##ptime=[1,5,60,120] minutes
new3(g,pdays,ptime,pprepost)
##u=[1,5,7,10,15,30]
##
##for x in u:
##    new4(x,g)


