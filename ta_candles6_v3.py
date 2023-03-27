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
    import pandas_ta as ta

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
    df['5-day Exponential MA'] = df['Adj Close'].ewm(span=5, adjust=False).mean()
    
    df['3day_s']=df['Close']-df['3-day Exponential MA']
    df['5day_s']=df['Close']-df['5-day Exponential MA']
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

##    mavcolors     = ['#ef5714','#ef5714','#9f4878','#9f4878','#ef5714','#9f4878','#9f4878']
    s  = mpf.make_mpf_style(base_mpf_style='yahoo',mavcolors=['#ef5714','#ef5714','#9f4878','#9f4878','#ef5714','#9f4878','#9f4878'])
    
##    mpf.plot(df, block=False,type='candle', volume=True, figratio=(15, 15), style='charles', mav=(200,100,50,20,10,3,5),
##             title=ticker.upper() +' (Daily) '+
##             str(p).split()[1]+' / (diff) '+str(p2).split()[1] + ', Open: '+ str(p5).split()[1] + ' ,low: '+str(p3).split()[1]+ ' ,High: '+ str(p4).split()[1]
##             + ', day swing: ' + str(u3).split('.')[0],
##             show_nontrading=True)
    mpf.plot(df, block=False,type='candle', volume=True, figratio=(15, 15), mav=(200,100,50,20,10,3,5),
         title=ticker.upper() +' (Daily) '+
         str(p).split()[1]+' / (diff) '+str(p2).split()[1] + ', Open: '+ str(p5).split()[1] + ' ,low: '+str(p3).split()[1]+ ' ,High: '+ str(p4).split()[1]
         + ', day swing: ' + str(u3).split('.')[0],style=s,
         show_nontrading=True)
##             update_width_config=dict(candle_linewidth=0.25),alines=dict(alines=seq_of_points, colors=seq_of_colors, linestyle='-', linewidths=3))

######
######    import pandas as pd
######    import matplotlib.pyplot as plt
######    import matplotlib.colors as mcolors
######    import seaborn as sns
######    import mplfinance as mpf
######
######    color_palette = sns.color_palette("husl", 3)
######    colors = [mcolors.to_hex(c) for c in color_palette] 
######
########    df = pd.read_csv('./data/yahoofinance-SPY-20080101-20180101.csv',index_col=0,parse_dates=True)
########    df = df.loc['2016-05-01':'2016-06-16',:]
######
######    seq_of_seq_repeat_point_in_between=[
######        [('2021-05-02',207),('2021-05-06',204)],
######        [('20121-05-06',204),('2021-05-10',208.5),('2021-05-19',203.5),('2021-25',209.5)],
######        [('2021-05-25',209.5),('2021-06-08',212),('2021-06-16',207.5)]]
######        
######    mpf.plot(df,
######             type='candle',style='charles',
######             alines=dict(alines=seq_of_seq_repeat_point_in_between,
######                         colors=colors,
######                         linewidths=4,
######                         alpha=0.7),
######             figscale=1.25
######            )

##  mpf.plot(df_history, show_nontrading=True, figratio=(10,7), figscale=2, datetime_format='%d.%m.%y', #figscale=2
##             xrotation=90, tight_layout=False, xlim=(xmin, xmax), ylim=(chart_unten, chart_oben),
##             alines=dict(alines=seq_of_points, colors=seq_of_colors, linestyle='-', linewidths=1),
##             type='candle', savefig=bildpfad, addplot=apdict, style=s, title=chart_title,
##             update_width_config=dict(candle_linewidth=0.5))


#####################
    ##    mpf.make_addplot(stck['Volume'].iloc[170:],type = 'line',linestyle=' ',panel =1, mav = 10)
##    mc = mpf.make_marketcolors(up='g',down='r',
##                           edge='inherit',
##                           wick='black',
##                           volume='in',
##                           ohlc='i')
##    s    = mpf.make_mpf_style(marketcolors=mc)
##    apc = [mpf.make_addplot(df['rsi'].iloc[1:],panel=2,color='g',type = 'line',ylabel='RSI'),
##           mpf.make_addplot(df['rsi_overbought'].iloc[1:], panel=2,color='blue',type = 'line',linestyle='-.',secondary_y=False),
##           mpf.make_addplot(df['rsi_oversold'].iloc[1:], panel=2,color='red',type = 'line',linestyle='-.', secondary_y=False),
##           mpf.make_addplot(df['Volume'].iloc[1:],panel =1,type = 'bar', mav = 10,color = 'in')]
##
##    mpf.plot(df.iloc[1:], type='candlestick', volume=True,title = ticker, tight_layout=True, hlines=ml_results, mav=(9,26),
##             style = s, returnfig=True,addplot = apc)
#############################

##    df['5']=''
    df.reset_index(inplace=True)

    df5=pd.concat([df['Date'],df['ticker'],df['Close'],df['3-day Exponential MA'],df['5-day Exponential MA'],df['10-day Exponential MA'],
                   df['20-day Exponential MA'],df['50-day Exponential MA'],
                   df['100-day Exponential MA'],df['200-day Exponential MA']
                   ],axis=1)
    
    df5['3-MA']=''
    df5['5-MA']=''
    df5['10-MA']=''
    df5['20-MA']=''
    df5['50-MA']=''
    df5['100-MA']=''
    df5['200-MA']=''

    df5['3-MA #']=''   
    df5['5-MA #']=''
    df5['10-MA #']=''
    df5['20-MA #']=''
    df5['50-MA #']=''
    df5['100-MA #']=''
    df5['200-MA #']=''
    print(df5)
    i=0
    for x in df5.index:
##        print(' 3day/shift ',df5['Date'].loc[x],df5['3-day Exponential MA'].loc[x].round(0)-df5['3-day Exponential MA'].shift(1).loc[x].round(0))
              
##        print(df5['Close'].loc[x] , df5['3-day Exponential MA'].loc[x],df5['3-day Exponential MA'].shift(1).loc[x])
        if (df5['3-day Exponential MA'].loc[x].round(0)-df5['3-day Exponential MA'].shift(1).loc[x].round(0)) > 0:
            
            if df5['Close'].loc[x] - df5['3-day Exponential MA'].loc[x] > 0:
                df5['3-MA'].loc[x]=" ---> BUY-3-MA uptrend *** "
                df5['3-MA #'].loc[x]=(df5['Close'].loc[x] - df5['3-day Exponential MA'].loc[x]).round(0)
                
            elif df5['Close'].loc[x] - df5['3-day Exponential MA'].loc[x] < 0:
                df5['3-MA'].loc[x]=" *** BUY?(close<3MA)-3-MA uptrend *** "
                df5['3-MA #'].loc[x]=(df5['Close'].loc[x] - df5['3-day Exponential MA'].loc[x]).round(0)

                
            else:
                pass


        if (df5['3-day Exponential MA'].loc[x].round(0)-df5['3-day Exponential MA'].shift(1).loc[x].round(0)) < 0:
            
            if df5['Close'].loc[x] - df5['3-day Exponential MA'].loc[x] > 0:
                df5['3-MA'].loc[x]=" *** SELL?(close>3MA)-3-MA DWNtrend *** "
                df5['3-MA #'].loc[x]=(df5['Close'].loc[x] - df5['3-day Exponential MA'].loc[x]).round(0)
                

            elif df5['Close'].loc[x] - df5['3-day Exponential MA'].loc[x] < 0:
                df5['3-MA'].loc[x]=" <--- SELL-3-MA DWNtrend *** "
                df5['3-MA #'].loc[x]=(df5['Close'].loc[x] - df5['3-day Exponential MA'].loc[x]).round(0)
                

            else:
                pass
##    print('office_walnut',df5)            
##################################################
#add

        if (df5['5-day Exponential MA'].loc[x].round(0)-df5['5-day Exponential MA'].shift(1).loc[x].round(0)) > 0:
            

            if df5['Close'].loc[x] - df5['5-day Exponential MA'].loc[x] > 0:
                df5['5-MA'].loc[x]=" ---> BUY-5-MA uptrend *** "
                df5['5-MA #'].loc[x]=(df5['Close'].loc[x] - df5['5-day Exponential MA'].loc[x]).round(0)
                
            elif df5['Close'].loc[x] - df5['5-day Exponential MA'].loc[x] < 0:
                df5['5-MA'].loc[x]=" *** BUY?(close<5-MA)-5-MA uptrend *** "
                df5['5-MA #'].loc[x]=(df5['Close'].loc[x] - df5['5-day Exponential MA'].loc[x]).round(0)

                
            else:
                pass


        if (df5['5-day Exponential MA'].loc[x].round(0)-df5['5-day Exponential MA'].shift(1).loc[x].round(0)) < 0:

            if df5['Close'].loc[x] - df5['5-day Exponential MA'].loc[x] > 0:
                df5['5-MA'].loc[x]=" *** SELL?(close>5-MA)-5-MA DWNtrend *** "
                df5['5-MA #'].loc[x]=(df5['Close'].loc[x] - df5['5-day Exponential MA'].loc[x]).round(0)
                

            elif df5['Close'].loc[x] - df5['5-day Exponential MA'].loc[x] < 0:
                df5['5-MA'].loc[x]=" <--- SELL-5-MA DWNtrend *** "
                df5['5-MA #'].loc[x]=(df5['Close'].loc[x] - df5['5-day Exponential MA'].loc[x]).round(0)
                


            else:
                pass




###########################################
###add
##
        if (df5['10-day Exponential MA'].loc[x].round(0)-df5['10-day Exponential MA'].shift(1).loc[x].round(0)) > 0:
            

            if df5['Close'].loc[x] - df5['10-day Exponential MA'].loc[x] > 0:
                df5['10-MA'].loc[x]=" ---> BUY-10-MA uptrend *** "
                df5['10-MA #'].loc[x]=(df5['Close'].loc[x] - df5['10-day Exponential MA'].loc[x]).round(0)
                
            elif df5['Close'].loc[x] - df5['10-day Exponential MA'].loc[x] < 0:
                df5['10-MA'].loc[x]=" *** BUY?(close<10-MA)-10-MA uptrend *** "
                df5['10-MA #'].loc[x]=(df5['Close'].loc[x] - df5['10-day Exponential MA'].loc[x]).round(0)

                
            else:
                pass


        if (df5['10-day Exponential MA'].loc[x].round(0)-df5['10-day Exponential MA'].shift(1).loc[x].round(0)) < 0:

            if df5['Close'].loc[x] - df5['10-day Exponential MA'].loc[x] > 0:
                df5['10-MA'].loc[x]=" *** SELL?(close>10-MA)-10-MA DWNtrend *** "
                df5['10-MA #'].loc[x]=(df5['Close'].loc[x] - df5['10-day Exponential MA'].loc[x]).round(0)
                

            elif df5['Close'].loc[x] - df5['10-day Exponential MA'].loc[x] < 0:
                df5['10-MA'].loc[x]=" <--- SELL-10-MA DWNtrend *** "
                df5['10-MA #'].loc[x]=(df5['Close'].loc[x] - df5['10-day Exponential MA'].loc[x]).round(0)
                

            else:
                pass

##    print('office_walnut',df5)
#add
##            
###add
##
        if (df5['20-day Exponential MA'].loc[x].round(0)-df5['20-day Exponential MA'].shift(1).loc[x].round(0)) > 0:
            

            if df5['Close'].loc[x] - df5['20-day Exponential MA'].loc[x] > 0:
                df5['20-MA'].loc[x]=" ---> BUY-20-MA uptrend *** "
                df5['20-MA #'].loc[x]=(df5['Close'].loc[x] - df5['20-day Exponential MA'].loc[x]).round(0)
                
            elif df5['Close'].loc[x] - df5['20-day Exponential MA'].loc[x] < 0:
                df5['20-MA'].loc[x]=" *** BUY?(close<20-MA)-20-MA uptrend *** "
                df5['20-MA #'].loc[x]=(df5['Close'].loc[x] - df5['20-day Exponential MA'].loc[x]).round(0)

                
            else:
                pass


        if (df5['20-day Exponential MA'].loc[x].round(0)-df5['20-day Exponential MA'].shift(1).loc[x].round(0)) < 0:

            if df5['Close'].loc[x] - df5['20-day Exponential MA'].loc[x] > 0:
                df5['20-MA'].loc[x]=" *** SELL?(close>20-MA)-20-MA DWNtrend *** "
                df5['20-MA #'].loc[x]=(df5['Close'].loc[x] - df5['20-day Exponential MA'].loc[x]).round(0)
                

            elif df5['Close'].loc[x] - df5['20-day Exponential MA'].loc[x] < 0:
                df5['20-MA'].loc[x]=" <--- SELL-20-MA DWNtrend *** "
                df5['20-MA #'].loc[x]=(df5['Close'].loc[x] - df5['20-day Exponential MA'].loc[x]).round(0)
                
##    print('office_walnut',df5)
#add

        if (df5['50-day Exponential MA'].loc[x].round(0)-df5['50-day Exponential MA'].shift(1).loc[x].round(0)) > 0:
            

            if df5['Close'].loc[x] - df5['50-day Exponential MA'].loc[x] > 0:
                df5['50-MA'].loc[x]=" ---> BUY-50-MA uptrend *** "
                df5['50-MA #'].loc[x]=(df5['Close'].loc[x] - df5['50-day Exponential MA'].loc[x]).round(0)
                
            elif df5['Close'].loc[x] - df5['50-day Exponential MA'].loc[x] < 0:
                df5['50-MA'].loc[x]=" *** BUY?(close<50-MA)-50-MA uptrend *** "
                df5['50-MA #'].loc[x]=(df5['Close'].loc[x] - df5['50-day Exponential MA'].loc[x]).round(0)

                
            else:
                pass


        if (df5['50-day Exponential MA'].loc[x].round(0)-df5['50-day Exponential MA'].shift(1).loc[x].round(0)) < 0:

            if df5['Close'].loc[x] - df5['50-day Exponential MA'].loc[x] > 0:
                df5['50-MA'].loc[x]=" *** SELL?(close>50-MA)-50-MA DWNtrend *** "
                df5['50-MA #'].loc[x]=(df5['Close'].loc[x] - df5['50-day Exponential MA'].loc[x]).round(0)
                

            elif df5['Close'].loc[x] - df5['50-day Exponential MA'].loc[x] < 0:
                df5['50-MA'].loc[x]=" <--- SELL-50-MA DWNtrend *** "
                df5['50-MA #'].loc[x]=(df5['Close'].loc[x] - df5['50-day Exponential MA'].loc[x]).round(0)
                
##    print('office_walnut',df5)
##

##
###add

        if (df5['100-day Exponential MA'].loc[x].round(0)-df5['100-day Exponential MA'].shift(1).loc[x].round(0)) > 0:
            

            if df5['Close'].loc[x] - df5['100-day Exponential MA'].loc[x] > 0:
                df5['100-MA'].loc[x]=" ---> BUY-100-MA uptrend *** "
                df5['100-MA #'].loc[x]=(df5['Close'].loc[x] - df5['100-day Exponential MA'].loc[x]).round(0)
                
            elif df5['Close'].loc[x] - df5['100-day Exponential MA'].loc[x] < 0:
                df5['100-MA'].loc[x]=" *** BUY?(close<100-MA)-100-MA uptrend *** "
                df5['100-MA #'].loc[x]=(df5['Close'].loc[x] - df5['100-day Exponential MA'].loc[x]).round(0)

                
            else:
                pass


        if (df5['100-day Exponential MA'].loc[x].round(0)-df5['100-day Exponential MA'].shift(1).loc[x].round(0)) < 0:

            if df5['Close'].loc[x] - df5['100-day Exponential MA'].loc[x] > 0:
                df5['100-MA'].loc[x]=" *** SELL?(close>100-MA)-100-MA DWNtrend *** "
                df5['100-MA #'].loc[x]=(df5['Close'].loc[x] - df5['100-day Exponential MA'].loc[x]).round(0)
                

            elif df5['Close'].loc[x] - df5['100-day Exponential MA'].loc[x] < 0:
                df5['100-MA'].loc[x]=" <--- SELL-100-MA DWNtrend *** "
                df5['100-MA #'].loc[x]=(df5['Close'].loc[x] - df5['100-day Exponential MA'].loc[x]).round(0)
                


##    print('office_walnut',df5)
##
##
###add

        if (df5['200-day Exponential MA'].loc[x].round(0)-df5['200-day Exponential MA'].shift(1).loc[x].round(0)) > 0:
            

            if df5['Close'].loc[x] - df5['200-day Exponential MA'].loc[x] > 0:
                df5['200-MA'].loc[x]=" ---> BUY-200-MA uptrend *** "
                df5['200-MA #'].loc[x]=(df5['Close'].loc[x] - df5['200-day Exponential MA'].loc[x]).round(0)
                
            elif df5['Close'].loc[x] - df5['200-day Exponential MA'].loc[x] < 0:
                df5['200-MA'].loc[x]=" *** BUY?(close<200-MA)-200-MA uptrend *** "
                df5['200-MA #'].loc[x]=(df5['Close'].loc[x] - df5['200-day Exponential MA'].loc[x]).round(0)

                
            else:
                pass


        if (df5['200-day Exponential MA'].loc[x].round(0)-df5['200-day Exponential MA'].shift(1).loc[x].round(0)) < 0:

            if df5['Close'].loc[x] - df5['200-day Exponential MA'].loc[x] > 0:
                df5['200-MA'].loc[x]=" *** SELL?(close>200-MA)-200-MA DWNtrend *** "
                df5['200-MA #'].loc[x]=(df5['Close'].loc[x] - df5['200-day Exponential MA'].loc[x]).round(0)
                

            elif df5['Close'].loc[x] - df5['200-day Exponential MA'].loc[x] < 0:
                df5['200-MA'].loc[x]=" <--- SELL-200-MA DWNtrend *** "
                df5['200-MA #'].loc[x]=(df5['Close'].loc[x] - df5['200-day Exponential MA'].loc[x]).round(0)
                


    print('office_walnut',df5)
    
##    print('stupid azhar is a looser',f5)
##    print(df5.columns)
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
##    i=i+1
####  i
##    print(df5['3-day Exponential MA'],'         ',df5['Close'])    
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
##    print('buuu')        
##    df.plot()
################################## section 2 hourly
    
    perd='7d'
    intervl='60m'
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


    dfi['direct']=''
    dfi['down']=''
    dfi['a_Close']=''
    dfi['a_High']=''
    dfi['a_Low']=''
    dfi['a_Open']=''
    dfi['HA']=''
    dfi['Opena']=''
    dfi['green']=''
    dfi['greenby']=''

    for x in dfi.index:

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
            dfi['direct'].loc[x]='HA_Green'
        elif dfi['HA'].loc[x] < 0:
            dfi['direct'].loc[x]='HA_Red'

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

    dfi['3-MA #']=''   
    dfi['5-MA #']=''
    dfi['10-MA #']=''
    dfi['20-MA #']=''
    dfi['50-MA #']=''
    dfi['100-MA #']=''
    dfi['200-MA #']=''

##    print(dfi)
    i=0
    for x in dfi.index:
##        print(' 3day/shift ',dfi['Date'].loc[x],dfi['3-day Exponential MA'].loc[x].round(0)-dfi['3-day Exponential MA'].shift(1).loc[x].round(0))
              
##        print(dfi['Close'].loc[x] , dfi['3-day Exponential MA'].loc[x],dfi['3-day Exponential MA'].shift(1).loc[x])
        if (dfi['3-day Exponential MA'].loc[x].round(0)-dfi['3-day Exponential MA'].shift(1).loc[x].round(0)) > 0:
            
            if dfi['Close'].loc[x] - dfi['3-day Exponential MA'].loc[x] > 0:
                dfi['3-MA'].loc[x]=" ---> BUY-3-MA uptrend *** "
                dfi['3-MA #'].loc[x]=(dfi['Close'].loc[x] - dfi['3-day Exponential MA'].loc[x]).round(0)
                
            elif dfi['Close'].loc[x] - dfi['3-day Exponential MA'].loc[x] < 0:
                dfi['3-MA'].loc[x]=" *** BUY?(close<3MA)-3-MA uptrend *** "
                dfi['3-MA #'].loc[x]=(dfi['Close'].loc[x] - dfi['3-day Exponential MA'].loc[x]).round(0)

                
            else:
                pass


        if (dfi['3-day Exponential MA'].loc[x].round(0)-dfi['3-day Exponential MA'].shift(1).loc[x].round(0)) < 0:
            
            if dfi['Close'].loc[x] - dfi['3-day Exponential MA'].loc[x] > 0:
                dfi['3-MA'].loc[x]=" *** SELL?(close>3MA)-3-MA DWNtrend *** "
                dfi['3-MA #'].loc[x]=(dfi['Close'].loc[x] - dfi['3-day Exponential MA'].loc[x]).round(0)
                

            elif dfi['Close'].loc[x] - dfi['3-day Exponential MA'].loc[x] < 0:
                dfi['3-MA'].loc[x]=" <--- SELL-3-MA DWNtrend *** "
                dfi['3-MA #'].loc[x]=(dfi['Close'].loc[x] - dfi['3-day Exponential MA'].loc[x]).round(0)
                

            else:
                pass
##    print('office_walnut',dfi)            
##################################################
#add

        if (dfi['5-day Exponential MA'].loc[x].round(0)-dfi['5-day Exponential MA'].shift(1).loc[x].round(0)) > 0: #(MA slopes upward)
            

            if dfi['Close'].loc[x] - dfi['5-day Exponential MA'].loc[x] > 0:  #(close price above MA)
                dfi['5-MA'].loc[x]=" ---> BUY-5-MA uptrend *** "  # buy signal
                dfi['5-MA #'].loc[x]=(dfi['Close'].loc[x] - dfi['5-day Exponential MA'].loc[x]).round(0)
                
            elif dfi['Close'].loc[x] - dfi['5-day Exponential MA'].loc[x] < 0: #(close price above MA)
                dfi['5-MA'].loc[x]=" *** BUY?(close<5-MA)-5-MA uptrend *** " # buy signal
                dfi['5-MA #'].loc[x]=(dfi['Close'].loc[x] - dfi['5-day Exponential MA'].loc[x]).round(0)

            elif dfi['Close'].loc[x] - dfi['5-day Exponential MA'].loc[x] == 0:
                dfi['5-MA'].loc[x]="close=5-day_exp"
                dfi['5-MA #'].loc[x]=(dfi['Close'].loc[x] - dfi['5-day Exponential MA'].loc[x]).round(0)
                
            else:
                pass


        if (dfi['5-day Exponential MA'].loc[x].round(0)-dfi['5-day Exponential MA'].shift(1).loc[x].round(0)) < 0:

            if dfi['Close'].loc[x] - dfi['5-day Exponential MA'].loc[x] > 0:
                dfi['5-MA'].loc[x]=" *** SELL?(close>5-MA)-5-MA DWNtrend *** "
                dfi['5-MA #'].loc[x]=(dfi['Close'].loc[x] - dfi['5-day Exponential MA'].loc[x]).round(0)
                

            elif dfi['Close'].loc[x] - dfi['5-day Exponential MA'].loc[x] < 0:
                dfi['5-MA'].loc[x]=" <--- SELL-5-MA DWNtrend *** "
                dfi['5-MA #'].loc[x]=(dfi['Close'].loc[x] - dfi['5-day Exponential MA'].loc[x]).round(0)


                
##        if dfi['Close'].loc[x] - dfi['5-day Exponential MA'].loc[x] < 0:
##            dfi['5-MA'].loc[x]="stupid"
##            dfi['5-MA #'].loc[x]="stupid"

        else:
            pass




###########################################
###add
##
        if (dfi['10-day Exponential MA'].loc[x].round(0)-dfi['10-day Exponential MA'].shift(1).loc[x].round(0)) > 0:
            

            if dfi['Close'].loc[x] - dfi['10-day Exponential MA'].loc[x] > 0:
                dfi['10-MA'].loc[x]=" ---> BUY-10-MA uptrend *** "
                dfi['10-MA #'].loc[x]=(dfi['Close'].loc[x] - dfi['10-day Exponential MA'].loc[x]).round(0)
                
            elif dfi['Close'].loc[x] - dfi['10-day Exponential MA'].loc[x] < 0:
                dfi['10-MA'].loc[x]=" *** BUY?(close<10-MA)-10-MA uptrend *** "
                dfi['10-MA #'].loc[x]=(dfi['Close'].loc[x] - dfi['10-day Exponential MA'].loc[x]).round(0)

                
            else:
                pass


        if (dfi['10-day Exponential MA'].loc[x].round(0)-dfi['10-day Exponential MA'].shift(1).loc[x].round(0)) < 0:

            if dfi['Close'].loc[x] - dfi['10-day Exponential MA'].loc[x] > 0:
                dfi['10-MA'].loc[x]=" *** SELL?(close>10-MA)-10-MA DWNtrend *** "
                dfi['10-MA #'].loc[x]=(dfi['Close'].loc[x] - dfi['10-day Exponential MA'].loc[x]).round(0)
                

            elif dfi['Close'].loc[x] - dfi['10-day Exponential MA'].loc[x] < 0:
                dfi['10-MA'].loc[x]=" <--- SELL-10-MA DWNtrend *** "
                dfi['10-MA #'].loc[x]=(dfi['Close'].loc[x] - dfi['10-day Exponential MA'].loc[x]).round(0)
                

            else:
                pass

##    print('office_walnut',dfi)
#add
##            
###add
##
        if (dfi['20-day Exponential MA'].loc[x].round(0)-dfi['20-day Exponential MA'].shift(1).loc[x].round(0)) > 0:
            

            if dfi['Close'].loc[x] - dfi['20-day Exponential MA'].loc[x] > 0:
                dfi['20-MA'].loc[x]=" ---> BUY-20-MA uptrend *** "
                dfi['20-MA #'].loc[x]=(dfi['Close'].loc[x] - dfi['20-day Exponential MA'].loc[x]).round(0)
                
            elif dfi['Close'].loc[x] - dfi['20-day Exponential MA'].loc[x] < 0:
                dfi['20-MA'].loc[x]=" *** BUY?(close<20-MA)-20-MA uptrend *** "
                dfi['20-MA #'].loc[x]=(dfi['Close'].loc[x] - dfi['20-day Exponential MA'].loc[x]).round(0)

                
            else:
                pass


        if (dfi['20-day Exponential MA'].loc[x].round(0)-dfi['20-day Exponential MA'].shift(1).loc[x].round(0)) < 0:

            if dfi['Close'].loc[x] - dfi['20-day Exponential MA'].loc[x] > 0:
                dfi['20-MA'].loc[x]=" *** SELL?(close>20-MA)-20-MA DWNtrend *** "
                dfi['20-MA #'].loc[x]=(dfi['Close'].loc[x] - dfi['20-day Exponential MA'].loc[x]).round(0)
                

            elif dfi['Close'].loc[x] - dfi['20-day Exponential MA'].loc[x] < 0:
                dfi['20-MA'].loc[x]=" <--- SELL-20-MA DWNtrend *** "
                dfi['20-MA #'].loc[x]=(dfi['Close'].loc[x] - dfi['20-day Exponential MA'].loc[x]).round(0)
                
##    print('office_walnut',dfi)
#add

        if (dfi['50-day Exponential MA'].loc[x].round(0)-dfi['50-day Exponential MA'].shift(1).loc[x].round(0)) > 0:
            

            if dfi['Close'].loc[x] - dfi['50-day Exponential MA'].loc[x] > 0:
                dfi['50-MA'].loc[x]=" ---> BUY-50-MA uptrend *** "
                dfi['50-MA #'].loc[x]=(dfi['Close'].loc[x] - dfi['50-day Exponential MA'].loc[x]).round(0)
                
            elif dfi['Close'].loc[x] - dfi['50-day Exponential MA'].loc[x] < 0:
                dfi['50-MA'].loc[x]=" *** BUY?(close<50-MA)-50-MA uptrend *** "
                dfi['50-MA #'].loc[x]=(dfi['Close'].loc[x] - dfi['50-day Exponential MA'].loc[x]).round(0)

                
            else:
                pass


        if (dfi['50-day Exponential MA'].loc[x].round(0)-dfi['50-day Exponential MA'].shift(1).loc[x].round(0)) < 0:

            if dfi['Close'].loc[x] - dfi['50-day Exponential MA'].loc[x] > 0:
                dfi['50-MA'].loc[x]=" *** SELL?(close>50-MA)-50-MA DWNtrend *** "
                dfi['50-MA #'].loc[x]=(dfi['Close'].loc[x] - dfi['50-day Exponential MA'].loc[x]).round(0)
                

            elif dfi['Close'].loc[x] - dfi['50-day Exponential MA'].loc[x] < 0:
                dfi['50-MA'].loc[x]=" <--- SELL-50-MA DWNtrend *** "
                dfi['50-MA #'].loc[x]=(dfi['Close'].loc[x] - dfi['50-day Exponential MA'].loc[x]).round(0)
                
##    print('office_walnut',dfi)
##

##
###add

        if (dfi['100-day Exponential MA'].loc[x].round(0)-dfi['100-day Exponential MA'].shift(1).loc[x].round(0)) > 0:
            

            if dfi['Close'].loc[x] - dfi['100-day Exponential MA'].loc[x] > 0:
                dfi['100-MA'].loc[x]=" ---> BUY-100-MA uptrend *** "
                dfi['100-MA #'].loc[x]=(dfi['Close'].loc[x] - dfi['100-day Exponential MA'].loc[x]).round(0)
                
            elif dfi['Close'].loc[x] - dfi['100-day Exponential MA'].loc[x] < 0:
                dfi['100-MA'].loc[x]=" *** BUY?(close<100-MA)-100-MA uptrend *** "
                dfi['100-MA #'].loc[x]=(dfi['Close'].loc[x] - dfi['100-day Exponential MA'].loc[x]).round(0)

                
            else:
                pass


        if (dfi['100-day Exponential MA'].loc[x].round(0)-dfi['100-day Exponential MA'].shift(1).loc[x].round(0)) < 0:

            if dfi['Close'].loc[x] - dfi['100-day Exponential MA'].loc[x] > 0:
                dfi['100-MA'].loc[x]=" *** SELL?(close>100-MA)-100-MA DWNtrend *** "
                dfi['100-MA #'].loc[x]=(dfi['Close'].loc[x] - dfi['100-day Exponential MA'].loc[x]).round(0)
                

            elif dfi['Close'].loc[x] - dfi['100-day Exponential MA'].loc[x] < 0:
                dfi['100-MA'].loc[x]=" <--- SELL-100-MA DWNtrend *** "
                dfi['100-MA #'].loc[x]=(dfi['Close'].loc[x] - dfi['100-day Exponential MA'].loc[x]).round(0)
                


##    print('office_walnut',dfi)
##
##
###add

        if (dfi['200-day Exponential MA'].loc[x].round(0)-dfi['200-day Exponential MA'].shift(1).loc[x].round(0)) > 0:
            

            if dfi['Close'].loc[x] - dfi['200-day Exponential MA'].loc[x] > 0:
                dfi['200-MA'].loc[x]=" ---> BUY-200-MA uptrend *** "
                dfi['200-MA #'].loc[x]=(dfi['Close'].loc[x] - dfi['200-day Exponential MA'].loc[x]).round(0)
                
            elif dfi['Close'].loc[x] - dfi['200-day Exponential MA'].loc[x] < 0:
                dfi['200-MA'].loc[x]=" *** BUY?(close<200-MA)-200-MA uptrend *** "
                dfi['200-MA #'].loc[x]=(dfi['Close'].loc[x] - dfi['200-day Exponential MA'].loc[x]).round(0)

                
            else:
                pass


        if (dfi['200-day Exponential MA'].loc[x].round(0)-dfi['200-day Exponential MA'].shift(1).loc[x].round(0)) < 0:

            if dfi['Close'].loc[x] - dfi['200-day Exponential MA'].loc[x] > 0:
                dfi['200-MA'].loc[x]=" *** SELL?(close>200-MA)-200-MA DWNtrend *** "
                dfi['200-MA #'].loc[x]=(dfi['Close'].loc[x] - dfi['200-day Exponential MA'].loc[x]).round(0)
                

            elif dfi['Close'].loc[x] - dfi['200-day Exponential MA'].loc[x] < 0:
                dfi['200-MA'].loc[x]=" <--- SELL-200-MA DWNtrend *** "
                dfi['200-MA #'].loc[x]=(dfi['Close'].loc[x] - dfi['200-day Exponential MA'].loc[x]).round(0)
                
    print('dddd',dfi.columns)

##    for x in dfi.index:
##        dfi['3-MA #'].loc(x)=dfi['3-MA #'].loc(x)
    dfi.set_index('Datetime')

    dfi=dfi[['stragety','direct','Datetime','price_shift','Close','Volume','ticker','HA','3-MA #', '5-MA #', '10-MA #', '20-MA #', '50-MA #', '100-MA #',
             '200-MA #']]
    print('pp office_walnut',dfi.tail(300))
########################################################################    

##g='^NDX'
g='amzn'    
new3(g)
##u=[1,5,7,10,15,30]
##
##for x in u:
##    new4(x,g)
