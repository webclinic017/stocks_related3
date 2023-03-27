
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
import mpl_finance
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



def hourly_buy():
    import warnings
    warnings.filterwarnings("ignore", category=FutureWarning)
    import sys



    
    from numerize import numerize
    import openpyxl
    m33=0
    x34=34
    x35=35
    

##    perda='635d'
##    intervla='1d'
##    yy=str(intervla).split('d')[0]
##    shiftbydays=3

    buy_order="no"
    perda='2d'
    intervla='1m'

    yy=str(intervla).split('d')[0]
    shiftbydays=3



    ##    g=input("Entr_Signal ticker: ")
    perd=perda
    intervl=intervla
    ticker='BTC-USD'
##    ticker='^NDX'
##    ticker='MSTR'
##    ticker='MRNA'

    # [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]



    #df=pd.DataFrame()
    #Interval required 5 minutes
    df = yf.download(ticker, period=perd, interval=intervl)
    df2=pd.DataFrame()
##    df['*']=''
##    for x in df.index:
##        df['*'].loc[x]='*'
##        df['Close_d_ch'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc(x)
    ##    print(df['Close'].loc[x])
        ########################################################

    ##close = numpy.random.random(100)
    
    df['CCI']=ta.CCI(df['High'],df['Low'],df['Close'],timeperiod=5)
    df['DX']=ta.DX(df['High'],df['Low'],df['Close'],timeperiod=5)
    df['WILLR']=ta.WILLR(df['High'],df['Low'],df['Close'],timeperiod=5)
    df['RSI']= ta.RSI(df['Close'], timeperiod=14)
    df['stoch_slowk'], df['stoch_slowd'] = ta.STOCH(df['High'],df['Low'],df['Close'], fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
    df['STOCHRSI_fastk'], df['STOCHRSI_fastd'] = ta.STOCHRSI(df['Close'], timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
    df['macd'], df['macdsignal'], df['macdhist'] = ta.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    df['adx']= ta.ADX(df['High'],df['Low'],df['Close'], timeperiod=14)
    df['WilliamsR']= ta.WILLR(df['High'],df['Low'],df['Close'], timeperiod=14)
    df['ATR']=ta.ATR(df['High'],df['Low'],df['Close'], timeperiod=14)
    df['ULTOSC'] = ta.ULTOSC(df['High'],df['Low'],df['Close'], timeperiod1=7, timeperiod2=14, timeperiod3=28)
    df['ROC'] = ta.ROC(df['Close'], timeperiod=4)
    df['PLUS_DI']=ta.PLUS_DI(df['High'],df['Low'],df['Close'], timeperiod=14)
    df['PLUS_DM']=ta.PLUS_DM(df['High'],df['Low'], timeperiod=14)
    df['aroondown'],df['aroonup']=ta.AROON(df['High'],df['Low'], timeperiod=14)
    df['HT_DCPERIOD']=ta.HT_DCPERIOD(df['Close'])
    df['HT_DCPHASE']=ta.HT_DCPHASE(df['Close'])
    df['sine'], df['leadsine']=ta.HT_SINE(df['Close'])
    
    df['macd'], df['macdsignal'], df['macdhist']=ta.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    df['PLUS_DI']=ta.PLUS_DI(df['High'],df['Low'],df['Close'], timeperiod=14)
    df['PLUS_DM']=ta.PLUS_DM(df['High'],df['Low'], timeperiod=14)
    df['PPO']=ta.PPO(df['Close'], fastperiod=12, slowperiod=26, matype=0)
    df['ROC']=ta.ROC(df['Close'], timeperiod=10)
    df['ROCP']=ta.ROCP(df['Close'], timeperiod=10)
    df['ROCR']=ta.ROCR(df['Close'], timeperiod=10)
    df['ROCR100']=ta.ROCR100(df['Close'], timeperiod=10)
    df['MOM']=ta.MOM(df['Close'], timeperiod=3)

    df['CDLDOJI']=ta.CDLDOJI(df['Open'], df['High'],df['Low'],df['Close'])
    df['CDLDOJISTAR']=ta.CDLDOJISTAR(df['Open'], df['High'],df['Low'],df['Close'])
    df['CDLDRAGONFLYDOJI']=ta.CDLDRAGONFLYDOJI(df['Open'], df['High'],df['Low'],df['Close'])
    df['CDLEVENINGDOJISTAR']=ta.CDLEVENINGDOJISTAR(df['Open'], df['High'],df['Low'],df['Close'], penetration=0)
    df['CDLGRAVESTONEDOJI']=ta.CDLGRAVESTONEDOJI(df['Open'], df['High'],df['Low'],df['Close'])
    df['CDLHAMMER']=ta.CDLHAMMER(df['Open'], df['High'],df['Low'],df['Close'])
    df['CDLXSIDEGAP3METHODS']=ta.CDLXSIDEGAP3METHODS(df['Open'], df['High'],df['Low'],df['Close'])
    aroondown, aroonup = ta.AROON(df['High'],df['Low'], timeperiod=3)

# switching from EMA to MA
    df['EMA_3']=df['Close']-ta.EMA(df['Close'], timeperiod=3)
    df['EMA_5']=df['Close']-ta.EMA(df['Close'], timeperiod=5)
    df['EMA_10']=df['Close']-ta.EMA(df['Close'], timeperiod=10)
    df['EMA_21']=df['Close']-ta.EMA(df['Close'], timeperiod=21)
    df['EMA_50']=df['Close']-ta.EMA(df['Close'], timeperiod=50)
    df['EMA_100']=df['Close']-ta.EMA(df['Close'], timeperiod=100)
    df['EMA_200']=df['Close']-ta.EMA(df['Close'], timeperiod=200)


    df['EMA_3s']=ta.EMA(df['Close'], timeperiod=3)
    df['EMA_5s']=ta.EMA(df['Close'], timeperiod=5)
    df['EMA_10s']=ta.EMA(df['Close'], timeperiod=10)
    df['EMA_21s']=ta.EMA(df['Close'], timeperiod=21)
    df['EMA_50s']=ta.EMA(df['Close'], timeperiod=50)
    df['EMA_100s']=ta.EMA(df['Close'], timeperiod=100)
    df['EMA_200s']=ta.EMA(df['Close'], timeperiod=200)

##    df['EMA_3']=df['Close']-ta.MA(df['Close'], timeperiod=3)
##    df['EMA_5']=df['Close']-ta.MA(df['Close'], timeperiod=5)
##    df['EMA_10']=df['Close']-ta.MA(df['Close'], timeperiod=10)
##    df['EMA_21']=df['Close']-ta.MA(df['Close'], timeperiod=21)
##    df['EMA_50']=df['Close']-ta.MA(df['Close'], timeperiod=50)
##    df['EMA_100']=df['Close']-ta.MA(df['Close'], timeperiod=100)
##    df['EMA_200']=df['Close']-ta.MA(df['Close'], timeperiod=200)
##
##
##    df['EMA_3s']=ta.MA(df['Close'], timeperiod=3)
##    df['EMA_5s']=ta.MA(df['Close'], timeperiod=5)
##    df['EMA_10s']=ta.MA(df['Close'], timeperiod=10)
##    df['EMA_21s']=ta.MA(df['Close'], timeperiod=21)
##    df['EMA_50s']=ta.MA(df['Close'], timeperiod=50)
##    df['EMA_100s']=ta.MA(df['Close'], timeperiod=100)
##    df['EMA_200s']=ta.MA(df['Close'], timeperiod=200)




    
##    df['day']=Datetimetime.Datetimetime(df['Datetime'])
    

    #############################
    ##for x in df.index:
    ##            df['Volume'].loc[x]=numerize.numerize(np.float32(df['Volume'].loc[x]).item())

    df2=df

    df['Opena']=''
    df['green']=''
    df['greenby']=''
    df['compare_d']=''
    buy = '3'
##    print('\n','****************************************************','\n')
##    print("jjjj ",df)
##    print('\n','****************************************************','\n')
    k3=0

    for x in df.index:

        df['Low'].loc[x]=df['Low'].loc[x]
        df['High'].loc[x]=df['High'].loc[x]
        df['compare_d'].loc[x]=str(shiftbydays)+'d'   
        df['Opena'].loc[x]=int(df['Open'].loc[x])
        if df['Close'].loc[x]-df['Open'].loc[x] > 0:



            df['green'].loc[x]='Green'
            df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
                                            #            print(x,'  ','Green','  ',df['ns'].loc[x])
        else:

            df['green'].loc[x]='Red'
            df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
    ##print(df)
    ##print('\n',' 1-day    ',g,'\n')

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
    df['Volumea']=''
    df['Close_d_ch']=''
    df['ticker']=''
    df['intervl']=''
    df['Close_d']=''
    df['Close_1d_ch']=''
    df['Close_3d_ch']=''
    df['Close_5d_ch']=''
    df['Close_30d_ch']=''
    df['swng']=''
    df['*']=''
    df['MA->']=''
    df['CCI/RSI->']=''
    df['HA->']=''
    df['Close->']=''

    df['pp']=''
    df['r1']=''
    df['r2']=''
    df['r3']=''
    df['s1']=''
    df['s2']=''
    df['s3']=''
    df['pivot']=''
    df['pivotx']=''

    df['ppx']=''
    df['r1x']=''
    df['r2x']=''
    df['r3x']=''
    df['s1x']=''
    df['s2x']=''
    df['s3x']=''
    df['crash']=''
    df['crash->']=''
    df['MSTR->']=''
    df['MSTR']=''
    df['Move->']=''
    df['Move']=''
    df['signal']=''
    df['signal->']=''
    df['MOM->']=''
    df['ff']=''
    df['uu']=''
    
   
##    df['MD->']=''
##    df['MD']=''
    
    q=0
    k=0
    k3=0
    k4=0
    for x in df.index:
        k3=k3+1
        
##        df['CDLDRAGONFLYDOJI'].loc[x]=ta.CDLDRAGONFLYDOJI(df['Open'].loc[x], df['High'].loc[x],df['Low'].loc[x],df['Close'].loc[x])
        if df['MOM'].loc[x] < 0:
            k=k+1
            (df['ff']).append(df['MOM'])
####################### Start of HA ####################
        df['MOM->']='MOM->'
        df['HA->'].loc[x]='HA->'
        df['Close->'].loc[x]='Close->'
        df['*'].loc[x]='*'
        df['MA->'].loc[x]='MA->'
        df['CCI/RSI->']='CCI/RSI->'
        df['swng'].loc[x]=df['High'].loc[x]-df['Low'].loc[x]
##        df['Close_d'].loc[x]=df['Close'].loc[x]-df['Close'].loc[x].timedelta(1)
        
        df['Close_d'].loc[x]=df['Close'].shift(shiftbydays).loc[x]
        df['Close_1d_ch'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]
        df['Close_3d_ch'].loc[x]=df['Close'].loc[x]-df['Close'].shift(3).loc[x]
        df['Close_5d_ch'].loc[x]=df['Close'].loc[x]-df['Close'].shift(5).loc[x]
        df['Close_30d_ch'].loc[x]=df['Close'].loc[x]-df['Close'].shift(30).loc[x]
        df['intervl'].loc[x]=intervl
        df['ticker'].loc[x]=ticker
        df['Close_d_ch'].loc[x]=df['Close'].loc[x]-df['Close_d'].loc[x]
        df['Opena'].loc[x]=int(df['Open'].loc[x])
        if df['Close'].loc[x]-df['Open'].loc[x] > 0:
            df['green'].loc[x]='Green'
            df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
            #            print(x,'  ','Green','  ',df['ns'].loc[x])
    #    elif:
    #        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
            #            print(x,'  ','Green','  ',df['ns'].loc[x])
        else:
            df['green'].loc[x]='Red'
            df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]


        df['a_Close'].loc[x]=1/4*(df['Open'].loc[x]+df['High'].loc[x]+df['Low'].loc[x]+df['Close'].loc[x])
        df['a_Open'].loc[x]=1/2*(df['Open'].shift(1).loc[x]+df['Close'].shift(1).loc[x])
        df['High'].loc[x]=df['High'].loc[x]
        df['Low'].loc[x]=df['Low'].loc[x]

# old ones        
        df['a_High'].loc[x]=max(df['High'].loc[x],df['a_Open'].loc[x],df['a_Close'].loc[x])
        df['a_Low'].loc[x]=min(df['Low'].loc[x],df['a_Open'].loc[x],df['a_Close'].loc[x])
#new ones
##        df['a_High'].loc[x]=max(df['High'].loc[x],df['Open'].loc[x],df['Close'].loc[x])
##        df['a_Low'].loc[x]=min(df['Low'].loc[x],df['Open'].loc[x],df['Close'].loc[x])
#2146955245

        
     #   df2['a_Open'].loc[x]=1/2*(df2['Open'].shift(1).loc[x]+df2['Close'].shift(1).loc[x])
        df['HA'].loc[x]=df['a_Close'].loc[x]-df['a_Open'].loc[x]
    ##    df2['d']=df2['Datetime'].dt.day_name()
    #    print(df2)

    #   if df2['a_Close'].loc[x] > df2['a_Open'].loc[x]:
        if df['HA'].loc[x] > 0:
            df['direct'].loc[x]='HA_Green'
        elif df['HA'].loc[x] < 0:
            df['direct'].loc[x]='HA_Red'
##        df['day'].loc[x]=df['day'].loc[x]
##        df['Volumea']=(df['Volume']-df['Volume'].shift(1))

############################ end of ha ######################
##          df['Close_1d_ch'].shift(1).loc[x]  > 33 and\
##           df['macd'].loc[x]  > 10 and\
##           df['Close_1d_ch'].loc[x]  > 15  and\
##           df['HA'].loc[x] > 5 and\

            
#########################################  buy ###################################
                  
        if (df['MOM'].loc[x])  > 30 and\
           df['Close_1d_ch'].shift(1).loc[x]  > 33 and\
           df['macd'].loc[x]  > 10 and\
           df['Close_1d_ch'].loc[x]  > 15  and\
           df['HA'].loc[x] > 5 and\
           df['HA'].shift(1).loc[x] > 5 :
            df['signal'].loc[x]='Buy_Signal'
##            print(k3,'  buy value: ', buy)

            df['signal'].loc[x]='rr///Buy_Signal'
            m33=df['Close'].loc[x]
##            print("**********************************************************",'\n')
##            print("buy ---->")      
##            print(k3, "longer=== buy ",df['Close'].loc[x])

            k4=k4+1
            hourly_sell(k3,k4,m33)

##            q=k3
            

############################################################################################################################################################            
          
            
#andrea boggs########################################### sell #############################


###############################################SELL########################################################################################################
        
##  
##        
##        if df['Close'].loc[x]-m33 > 80 and\
##           (df['MOM'].loc[x])  < 5 or df['Close_1d_ch'].loc[x] < -60 and\
##           (df['EMA_3'].loc[x]) < 0 and\
##           (df['Close_1d_ch'].loc[x])  < -40:
##             df['signal'].loc[x]='** Major Sell_Signal'
##                 
##             df['signal'].loc[x]='///Sell_Signal'
##             print("sell ---->",)
##             print(x, "*** === sell ",df['Close'].loc[x],'   points: ',df['Close'].loc[x]-m33,'   m33',m33,' \n')
##             print('close_1day_ch==>  ',df['Close_1d_ch'].loc[x],'  close-m33-->  ',df['Close'].loc[x]-m33,'\n')
##             print('MOM: ',df['MOM'].loc[x], 'EMA(3): ',df['EMA_3'].loc[x],' EMA21: ',df['EMA_3'].loc[x])
##             print('**********************************************************************************')
##             print('\n\n')
##
##

             #######################################################################

##        if (df['Close_1d_ch'].loc[x])  > 17:
##            df['signal'].loc[x]='**Buy_Signal**' 
            
######        
######             if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > 5000:
######                 df['Move->'].loc[x]='**[5K >]** Move UP->'
######                 df['Move'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]
######
######
######             if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > 3000 and (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < 5000:
######                 df['Move->'].loc[x]='**[3K-5K]** Move UP->'
######                 df['Move'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]
######
######             if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > 1000 and (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < 3000:
######                 df['Move->'].loc[x]='[1K-3K] Move UP->'
######                 df['Move'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]
######
######
######             if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > 500 and (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < 1000:
######                 df['Move->'].loc[x]='[500-1K] Move UP->'
######                 df['Move'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]
######
######             if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > 0 and (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < 500:
######                 df['Move->'].loc[x]='[0-500] Move UP->'
######                 df['Move'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]       
######                
######            
######             if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < -5000:
######                 df['crash->'].loc[x]='** 5K crash-> **'
######                 df['crash'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]
######                 df['MSTR->'].loc[x]='MSTR->'
######                 df['MSTR'].loc[x]=(df['Close'].loc[x]-df['Close'].shift(1).loc[x])/73
######
######             if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < -3000 and (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > -5000:
######                 df['crash->'].loc[x]='** [3K-4.9K crash-> **'
######                 df['crash'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]
######                 df['MSTR->'].loc[x]='MSTR->'
######                 df['MSTR'].loc[x]=(df['Close'].loc[x]-df['Close'].shift(1).loc[x])/73
######
######
######             if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < -1000 and (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > -3000:
######                 df['crash->'].loc[x]='[1K-3K] Dwn->'
######                 df['crash'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]
######                 df['MSTR->'].loc[x]='MSTR->'
######                 df['MSTR'].loc[x]=(df['Close'].loc[x]-df['Close'].shift(1).loc[x])/73
######
######
######             if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < 0 and (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > -1000:
######                 df['crash->'].loc[x]='[0-1K] Dwn->'
######                 df['crash'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]
######                 df['MSTR->'].loc[x]='MSTR->'
######                 df['MSTR'].loc[x]=(df['Close'].loc[x]-df['Close'].shift(1).loc[x])/73    
######
######
######
######
######
######
######                ##ddd=(df['Volume']-df['Volume'].shift(1))
######                 tt=pd.concat([df['ff'],df['MOM->'],df['MOM'],df['direct'],df['HA'],df['Close'],df['Close_d_ch'],df['Volume'],
######                               df['Volumea'],df['CCI'],df['DX'],df['WILLR'],df['RSI'],df['adx'],df['WilliamsR'],
######                               df['ATR'],df['ULTOSC'],
######                               df['ROC'],df['PLUS_DI'],df['PLUS_DM'],
######                               df['HT_DCPERIOD'],
######                               df['HT_DCPHASE'],
######                               df['sine'],df['leadsine'],df['aroondown'], df['aroonup'],
######                               df['macd'], df['macdsignal'], df['macdhist'],df['PLUS_DI'],df['PLUS_DM'],df['PPO'],df['ROC'],df['ROCP'],
######                               df['ROCR'],df['ROCR100'],
######                               df['*'],
######                               df['CDLDOJI'],df['CDLDOJISTAR'],df['CDLDRAGONFLYDOJI'],df['CDLEVENINGDOJISTAR'],df['CDLGRAVESTONEDOJI'],
######                               df['CDLHAMMER'],df['CDLXSIDEGAP3METHODS'],
######                               df['*'],df['EMA_3'],df['EMA_5'],df['EMA_10'],df['EMA_21'],df['EMA_50'],df['EMA_100'],df['EMA_200'],df['EMA_3s'],
######                               df['EMA_5s'],df['EMA_10s'],df['EMA_21s'],df['EMA_50s'],df['EMA_100s'],df['EMA_200s'],df['ticker'],df['intervl'],
######                               df['Close_d'],df['compare_d'],df['Close_1d_ch'],df['Close_3d_ch'],df['Close_5d_ch'],df['Close_30d_ch'],df['swng'],
######                               df['MA->'],df['CCI/RSI->'],df['Close->'],df['HA->'],
######                               df['crash->'],df['crash'],df['MSTR->'],df['MSTR'],df['Move->'],df['Move'],
######                               df['signal'],df['signal->']
######                               ],axis=1)
######
######
######
######
######
######
######
######
######             
########                 k5=k5+1
########                 if k5 > 1:
########                     break
######             
######            
######             
######
########    print(tt.tail(4))
######    print('tt-columns:',tt.columns)
######
######
######    tt.reset_index(inplace=True)        
######    for x in tt.index:
######    ##    print(tt['Volume'])
######    ##    tt['Volume'].loc[x]=numerize.numerize(tt['Volume'].loc[x])
######    ##    tt['Volume'].loc[x]=numerize.numerize((tt['Volume'].iloc[x][1]))
######        tt['Volume'].loc[x]=numerize.numerize(np.float32(tt['Volume'].loc[x]).item())
######    tt.set_index('Datetime')
######
######    print('\n',tt.columns,'\n')
######    print('uuuuu')
######
######    print('stupid stupid azhar ',tt.columns.get_loc('Close_d_ch'))
######    print('stupid stupid azhar ',tt.columns.get_loc('Close_1d_ch'))
########    print('stupid stupid azhar ',tt.columns.get_loc('MOM'))
########    print('stupid stupid azhar ',tt.columns.get_loc('*'))
######
######
########    print('all --> ',tt)
######    gg33=tt.iloc[:,[0,3,27,46,6,64,80,79,5,4,73,74,77,78]]
########    gg33=tt.iloc[:,[24,25,26,29,31,32,33,8,9,11,13,14,
########                    35,36,37,38,39,40,41,77,76,68,3,61,78,43,46,1,2,70,71,72,73,74,75,57,0,58,60,3,59,65,4,61,62,63,64,4,68,3,61,69,1,2,67,7,10,66,43,44,45,46,47,48,49]].tail(335)
######    gg33a=pd.DataFrame(gg33)
######    print('\n','Close_delta_price_by_'+str(shiftbydays)+' days','\n',gg33)
######    gg33a.to_csv("/home/az2/Downloads/44/output_57g.csv")
######    
######    print('\n\n\n')
######    print(' --------------------------- Glossary ----------------------------------')
######    print('CCI:    CCI > 100 --> down   CCI < -100 ----> Up')
######    print('RSI :   RSI between 70, 20. > 70 overbought, < 20 oversold')
######    print('ULOST:  Buy signal ULOST < 30 , sell signal ULOS > 70')
######    
######    print('DX:     The DX is usually smoothed with a moving average (i.e. the ADX).The values range from 0 to 100, but rarely get above 60.To interpret the DX, consider a high number to be a strong trend, and a low number, a weak trend.')
######    print('WilliamR: between -20 and -80. -20 is overbought/highs of its recent range, -80 is oversold/lower end of its recent range.')
######    print('ADX :   Strength of trend, 0-25 -> Absent or Weak Trend,    25-50 --> Strong Trend, ? --> 50-75, 75-100-->Extremely Strong Trend')
######    print('ATR :   ATR indicates increased volatility in the market')
######    print(' ---------------------------End of Glossary ----------------------------------')
######
########    print('Daily CCI: ', tt.tail(4))
######    ##MA = ta.SMA(df['close'])
######    ##print('MA: ',MA)
######    #########################################################################################################################
######
######

##days()


######################################## end #############################################
def hourly_sell(k3,k4,m34):
    import warnings
    warnings.filterwarnings("ignore", category=FutureWarning)
    import sys

    
    from numerize import numerize
    import openpyxl
    m33=0
    x34=34
    x35=35
    

##    perda='635d'
##    intervla='1d'
##    yy=str(intervla).split('d')[0]
##    shiftbydays=3

    buy_order="no"
    perda='2d'
    intervla='1m'

    yy=str(intervla).split('d')[0]
    shiftbydays=3



    ##    g=input("Entr_Signal ticker: ")
    perd=perda
    intervl=intervla
    ticker='BTC-USD'
##    ticker='^NDX'
##    ticker='MSTR'
##    ticker='MRNA'

    # [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]



    #df=pd.DataFrame()
    #Interval required 5 minutes
    df = yf.download(ticker, period=perd, interval=intervl)
    df2=pd.DataFrame()
##    df['*']=''
##    for x in df.index:
##        df['*'].loc[x]='*'
##        df['Close_d_ch'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc(x)
    ##    print(df['Close'].loc[x])
        ########################################################

    ##close = numpy.random.random(100)
    
    df['CCI']=ta.CCI(df['High'],df['Low'],df['Close'],timeperiod=5)
    df['DX']=ta.DX(df['High'],df['Low'],df['Close'],timeperiod=5)
    df['WILLR']=ta.WILLR(df['High'],df['Low'],df['Close'],timeperiod=5)
    df['RSI']= ta.RSI(df['Close'], timeperiod=14)
    df['stoch_slowk'], df['stoch_slowd'] = ta.STOCH(df['High'],df['Low'],df['Close'], fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
    df['STOCHRSI_fastk'], df['STOCHRSI_fastd'] = ta.STOCHRSI(df['Close'], timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
    df['macd'], df['macdsignal'], df['macdhist'] = ta.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    df['adx']= ta.ADX(df['High'],df['Low'],df['Close'], timeperiod=14)
    df['WilliamsR']= ta.WILLR(df['High'],df['Low'],df['Close'], timeperiod=14)
    df['ATR']=ta.ATR(df['High'],df['Low'],df['Close'], timeperiod=14)
    df['ULTOSC'] = ta.ULTOSC(df['High'],df['Low'],df['Close'], timeperiod1=7, timeperiod2=14, timeperiod3=28)
    df['ROC'] = ta.ROC(df['Close'], timeperiod=4)
    df['PLUS_DI']=ta.PLUS_DI(df['High'],df['Low'],df['Close'], timeperiod=14)
    df['PLUS_DM']=ta.PLUS_DM(df['High'],df['Low'], timeperiod=14)
    df['aroondown'],df['aroonup']=ta.AROON(df['High'],df['Low'], timeperiod=14)
    df['HT_DCPERIOD']=ta.HT_DCPERIOD(df['Close'])
    df['HT_DCPHASE']=ta.HT_DCPHASE(df['Close'])
    df['sine'], df['leadsine']=ta.HT_SINE(df['Close'])
    
    df['macd'], df['macdsignal'], df['macdhist']=ta.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    df['PLUS_DI']=ta.PLUS_DI(df['High'],df['Low'],df['Close'], timeperiod=14)
    df['PLUS_DM']=ta.PLUS_DM(df['High'],df['Low'], timeperiod=14)
    df['PPO']=ta.PPO(df['Close'], fastperiod=12, slowperiod=26, matype=0)
    df['ROC']=ta.ROC(df['Close'], timeperiod=10)
    df['ROCP']=ta.ROCP(df['Close'], timeperiod=10)
    df['ROCR']=ta.ROCR(df['Close'], timeperiod=10)
    df['ROCR100']=ta.ROCR100(df['Close'], timeperiod=10)
    df['MOM']=ta.MOM(df['Close'], timeperiod=3)

    df['CDLDOJI']=ta.CDLDOJI(df['Open'], df['High'],df['Low'],df['Close'])
    df['CDLDOJISTAR']=ta.CDLDOJISTAR(df['Open'], df['High'],df['Low'],df['Close'])
    df['CDLDRAGONFLYDOJI']=ta.CDLDRAGONFLYDOJI(df['Open'], df['High'],df['Low'],df['Close'])
    df['CDLEVENINGDOJISTAR']=ta.CDLEVENINGDOJISTAR(df['Open'], df['High'],df['Low'],df['Close'], penetration=0)
    df['CDLGRAVESTONEDOJI']=ta.CDLGRAVESTONEDOJI(df['Open'], df['High'],df['Low'],df['Close'])
    df['CDLHAMMER']=ta.CDLHAMMER(df['Open'], df['High'],df['Low'],df['Close'])
    df['CDLXSIDEGAP3METHODS']=ta.CDLXSIDEGAP3METHODS(df['Open'], df['High'],df['Low'],df['Close'])
    aroondown, aroonup = ta.AROON(df['High'],df['Low'], timeperiod=3)

# switching from EMA to MA
    df['EMA_3']=df['Close']-ta.EMA(df['Close'], timeperiod=3)
    df['EMA_5']=df['Close']-ta.EMA(df['Close'], timeperiod=5)
    df['EMA_10']=df['Close']-ta.EMA(df['Close'], timeperiod=10)
    df['EMA_21']=df['Close']-ta.EMA(df['Close'], timeperiod=21)
    df['EMA_50']=df['Close']-ta.EMA(df['Close'], timeperiod=50)
    df['EMA_100']=df['Close']-ta.EMA(df['Close'], timeperiod=100)
    df['EMA_200']=df['Close']-ta.EMA(df['Close'], timeperiod=200)


    df['EMA_3s']=ta.EMA(df['Close'], timeperiod=3)
    df['EMA_5s']=ta.EMA(df['Close'], timeperiod=5)
    df['EMA_10s']=ta.EMA(df['Close'], timeperiod=10)
    df['EMA_21s']=ta.EMA(df['Close'], timeperiod=21)
    df['EMA_50s']=ta.EMA(df['Close'], timeperiod=50)
    df['EMA_100s']=ta.EMA(df['Close'], timeperiod=100)
    df['EMA_200s']=ta.EMA(df['Close'], timeperiod=200)

##    df['EMA_3']=df['Close']-ta.MA(df['Close'], timeperiod=3)
##    df['EMA_5']=df['Close']-ta.MA(df['Close'], timeperiod=5)
##    df['EMA_10']=df['Close']-ta.MA(df['Close'], timeperiod=10)
##    df['EMA_21']=df['Close']-ta.MA(df['Close'], timeperiod=21)
##    df['EMA_50']=df['Close']-ta.MA(df['Close'], timeperiod=50)
##    df['EMA_100']=df['Close']-ta.MA(df['Close'], timeperiod=100)
##    df['EMA_200']=df['Close']-ta.MA(df['Close'], timeperiod=200)
##
##
##    df['EMA_3s']=ta.MA(df['Close'], timeperiod=3)
##    df['EMA_5s']=ta.MA(df['Close'], timeperiod=5)
##    df['EMA_10s']=ta.MA(df['Close'], timeperiod=10)
##    df['EMA_21s']=ta.MA(df['Close'], timeperiod=21)
##    df['EMA_50s']=ta.MA(df['Close'], timeperiod=50)
##    df['EMA_100s']=ta.MA(df['Close'], timeperiod=100)
##    df['EMA_200s']=ta.MA(df['Close'], timeperiod=200)




    
##    df['day']=Datetimetime.Datetimetime(df['Datetime'])
    

    #############################
    ##for x in df.index:
    ##            df['Volume'].loc[x]=numerize.numerize(np.float32(df['Volume'].loc[x]).item())

    df2=df

    df['Opena']=''
    df['green']=''
    df['greenby']=''
    df['compare_d']=''
    buy = '3'
##    print('\n','****************************************************','\n')
##    print("jjjj ",df)
##    print('\n','****************************************************','\n')
    k3=0

    for x in df.index:

        df['Low'].loc[x]=df['Low'].loc[x]
        df['High'].loc[x]=df['High'].loc[x]
        df['compare_d'].loc[x]=str(shiftbydays)+'d'   
        df['Opena'].loc[x]=int(df['Open'].loc[x])
        if df['Close'].loc[x]-df['Open'].loc[x] > 0:



            df['green'].loc[x]='Green'
            df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
                                            #            print(x,'  ','Green','  ',df['ns'].loc[x])
        else:

            df['green'].loc[x]='Red'
            df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
    ##print(df)
    ##print('\n',' 1-day    ',g,'\n')

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
    df['Volumea']=''
    df['Close_d_ch']=''
    df['ticker']=''
    df['intervl']=''
    df['Close_d']=''
    df['Close_1d_ch']=''
    df['Close_3d_ch']=''
    df['Close_5d_ch']=''
    df['Close_30d_ch']=''
    df['swng']=''
    df['*']=''
    df['MA->']=''
    df['CCI/RSI->']=''
    df['HA->']=''
    df['Close->']=''

    df['pp']=''
    df['r1']=''
    df['r2']=''
    df['r3']=''
    df['s1']=''
    df['s2']=''
    df['s3']=''
    df['pivot']=''
    df['pivotx']=''

    df['ppx']=''
    df['r1x']=''
    df['r2x']=''
    df['r3x']=''
    df['s1x']=''
    df['s2x']=''
    df['s3x']=''
    df['crash']=''
    df['crash->']=''
    df['MSTR->']=''
    df['MSTR']=''
    df['Move->']=''
    df['Move']=''
    df['signal']=''
    df['signal->']=''
    df['MOM->']=''
    df['ff']=''
    df['uu']=''
    
   
##    df['MD->']=''
##    df['MD']=''
    
    q=0
    k=0
    k3s=0
    for x in df.index:
        k3s=k3s+1
        
##        df['CDLDRAGONFLYDOJI'].loc[x]=ta.CDLDRAGONFLYDOJI(df['Open'].loc[x], df['High'].loc[x],df['Low'].loc[x],df['Close'].loc[x])
        if df['MOM'].loc[x] < 0:
            k=k+1
            (df['ff']).append(df['MOM'])
####################### Start of HA ####################
        df['MOM->']='MOM->'
        df['HA->'].loc[x]='HA->'
        df['Close->'].loc[x]='Close->'
        df['*'].loc[x]='*'
        df['MA->'].loc[x]='MA->'
        df['CCI/RSI->']='CCI/RSI->'
        df['swng'].loc[x]=df['High'].loc[x]-df['Low'].loc[x]
##        df['Close_d'].loc[x]=df['Close'].loc[x]-df['Close'].loc[x].timedelta(1)
        
        df['Close_d'].loc[x]=df['Close'].shift(shiftbydays).loc[x]
        df['Close_1d_ch'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]
        df['Close_3d_ch'].loc[x]=df['Close'].loc[x]-df['Close'].shift(3).loc[x]
        df['Close_5d_ch'].loc[x]=df['Close'].loc[x]-df['Close'].shift(5).loc[x]
        df['Close_30d_ch'].loc[x]=df['Close'].loc[x]-df['Close'].shift(30).loc[x]
        df['intervl'].loc[x]=intervl
        df['ticker'].loc[x]=ticker
        df['Close_d_ch'].loc[x]=df['Close'].loc[x]-df['Close_d'].loc[x]
        df['Opena'].loc[x]=int(df['Open'].loc[x])
        if df['Close'].loc[x]-df['Open'].loc[x] > 0:
            df['green'].loc[x]='Green'
            df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
            #            print(x,'  ','Green','  ',df['ns'].loc[x])
    #    elif:
    #        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
            #            print(x,'  ','Green','  ',df['ns'].loc[x])
        else:
            df['green'].loc[x]='Red'
            df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]


        df['a_Close'].loc[x]=1/4*(df['Open'].loc[x]+df['High'].loc[x]+df['Low'].loc[x]+df['Close'].loc[x])
        df['a_Open'].loc[x]=1/2*(df['Open'].shift(1).loc[x]+df['Close'].shift(1).loc[x])
        df['High'].loc[x]=df['High'].loc[x]
        df['Low'].loc[x]=df['Low'].loc[x]

# old ones        
        df['a_High'].loc[x]=max(df['High'].loc[x],df['a_Open'].loc[x],df['a_Close'].loc[x])
        df['a_Low'].loc[x]=min(df['Low'].loc[x],df['a_Open'].loc[x],df['a_Close'].loc[x])
#new ones
##        df['a_High'].loc[x]=max(df['High'].loc[x],df['Open'].loc[x],df['Close'].loc[x])
##        df['a_Low'].loc[x]=min(df['Low'].loc[x],df['Open'].loc[x],df['Close'].loc[x])
#2146955245

        
     #   df2['a_Open'].loc[x]=1/2*(df2['Open'].shift(1).loc[x]+df2['Close'].shift(1).loc[x])
        df['HA'].loc[x]=df['a_Close'].loc[x]-df['a_Open'].loc[x]
    ##    df2['d']=df2['Datetime'].dt.day_name()
    #    print(df2)

    #   if df2['a_Close'].loc[x] > df2['a_Open'].loc[x]:
        if df['HA'].loc[x] > 0:
            df['direct'].loc[x]='HA_Green'
        elif df['HA'].loc[x] < 0:
            df['direct'].loc[x]='HA_Red'
##        df['day'].loc[x]=df['day'].loc[x]
##        df['Volumea']=(df['Volume']-df['Volume'].shift(1))

############################ end of ha ######################
##          df['Close_1d_ch'].shift(1).loc[x]  > 33 and\
##           df['macd'].loc[x]  > 10 and\
##           df['Close_1d_ch'].loc[x]  > 15  and\
##           df['HA'].loc[x] > 5 and\

        k4=0    
#########################################  buy ###################################
##                  
##        if (df['MOM'].loc[x])  > 30 and\
##           df['Close_1d_ch'].shift(1).loc[x]  > 33 and\
##           df['macd'].loc[x]  > 10 and\
##           df['Close_1d_ch'].loc[x]  > 15  and\
##           df['HA'].loc[x] > 5 and\
##           df['HA'].shift(1).loc[x] > 5 :
##            df['signal'].loc[x]='Buy_Signal'
##            print(k3,'  buy value: ', buy)
##
##            df['signal'].loc[x]='rr///Buy_Signal'
##            m33=df['Close'].loc[x]
##            print("**********************************************************",'\n')
##            print("buy ---->")      
##            print(k3, "longer=== buy ",df['Close'].loc[x])
##
####            k4=k4+1
####            q=k3
##            

############################################################################################################################################################            
          
            
#andrea boggs########################################### sell #############################


###############################################SELL########################################################################################################
        
  
        h=0
        if k3s > k3 and df['Close'].loc[x]-m34 < 80 and\
           (df['MOM'].loc[x])  < 5 or df['Close_1d_ch'].loc[x] < -60 and\
           (df['EMA_3'].loc[x]) < 0 and\
           (df['Close_1d_ch'].loc[x])  < -40:
             h=h+1
             df['signal'].loc[x]='** Major Sell_Signal'
             m33=df['Close'].loc[x]    
             df['signal'].loc[x]='///Sell_Signal'
##             print("sell ---->",)
##             print(x, "*** === sell ",df['Close'].loc[x],'   points: ',df['Close'].loc[x]-m33,'  (Profit) [m33-m34]-> ',m33-m34,' \n')
##             print('close_1day_ch==>  ',df['Close_1d_ch'].loc[x],'  close-m33-->  ',df['Close'].loc[x]-m33,'\n')
##             print('MOM: ',df['MOM'].loc[x], 'EMA(3): ',df['EMA_3'].loc[x],' EMA21: ',df['EMA_3'].loc[x])
##             print('**********************************************************************************')
##             print('\n\n')
             file1 = open("/home/az2/Downloads/bitcoin_stuff.txt","a")
             file1.write(str(1)+' m33  '+str(m33.round(2))+' m34  '+str(m34)+'  profit-->    '+str((m33-m34).round(2)))
             file1.write('\n')
             file1.close()
             break


print("complete")
             #######################################################################

##        if (df['Close_1d_ch'].loc[x])  > 17:
##            df['signal'].loc[x]='**Buy_Signal**' 
            
######        
######             if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > 5000:
######                 df['Move->'].loc[x]='**[5K >]** Move UP->'
######                 df['Move'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]
######
######
######             if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > 3000 and (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < 5000:
######                 df['Move->'].loc[x]='**[3K-5K]** Move UP->'
######                 df['Move'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]
######
######             if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > 1000 and (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < 3000:
######                 df['Move->'].loc[x]='[1K-3K] Move UP->'
######                 df['Move'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]
######
######
######             if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > 500 and (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < 1000:
######                 df['Move->'].loc[x]='[500-1K] Move UP->'
######                 df['Move'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]
######
######             if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > 0 and (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < 500:
######                 df['Move->'].loc[x]='[0-500] Move UP->'
######                 df['Move'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]       
######                
######            
######             if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < -5000:
######                 df['crash->'].loc[x]='** 5K crash-> **'
######                 df['crash'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]
######                 df['MSTR->'].loc[x]='MSTR->'
######                 df['MSTR'].loc[x]=(df['Close'].loc[x]-df['Close'].shift(1).loc[x])/73
######
######             if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < -3000 and (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > -5000:
######                 df['crash->'].loc[x]='** [3K-4.9K crash-> **'
######                 df['crash'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]
######                 df['MSTR->'].loc[x]='MSTR->'
######                 df['MSTR'].loc[x]=(df['Close'].loc[x]-df['Close'].shift(1).loc[x])/73
######
######
######             if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < -1000 and (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > -3000:
######                 df['crash->'].loc[x]='[1K-3K] Dwn->'
######                 df['crash'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]
######                 df['MSTR->'].loc[x]='MSTR->'
######                 df['MSTR'].loc[x]=(df['Close'].loc[x]-df['Close'].shift(1).loc[x])/73
######
######
######             if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < 0 and (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > -1000:
######                 df['crash->'].loc[x]='[0-1K] Dwn->'
######                 df['crash'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]
######                 df['MSTR->'].loc[x]='MSTR->'
######                 df['MSTR'].loc[x]=(df['Close'].loc[x]-df['Close'].shift(1).loc[x])/73    
######
######
######
######
######
######
######                ##ddd=(df['Volume']-df['Volume'].shift(1))
######                 tt=pd.concat([df['ff'],df['MOM->'],df['MOM'],df['direct'],df['HA'],df['Close'],df['Close_d_ch'],df['Volume'],
######                               df['Volumea'],df['CCI'],df['DX'],df['WILLR'],df['RSI'],df['adx'],df['WilliamsR'],
######                               df['ATR'],df['ULTOSC'],
######                               df['ROC'],df['PLUS_DI'],df['PLUS_DM'],
######                               df['HT_DCPERIOD'],
######                               df['HT_DCPHASE'],
######                               df['sine'],df['leadsine'],df['aroondown'], df['aroonup'],
######                               df['macd'], df['macdsignal'], df['macdhist'],df['PLUS_DI'],df['PLUS_DM'],df['PPO'],df['ROC'],df['ROCP'],
######                               df['ROCR'],df['ROCR100'],
######                               df['*'],
######                               df['CDLDOJI'],df['CDLDOJISTAR'],df['CDLDRAGONFLYDOJI'],df['CDLEVENINGDOJISTAR'],df['CDLGRAVESTONEDOJI'],
######                               df['CDLHAMMER'],df['CDLXSIDEGAP3METHODS'],
######                               df['*'],df['EMA_3'],df['EMA_5'],df['EMA_10'],df['EMA_21'],df['EMA_50'],df['EMA_100'],df['EMA_200'],df['EMA_3s'],
######                               df['EMA_5s'],df['EMA_10s'],df['EMA_21s'],df['EMA_50s'],df['EMA_100s'],df['EMA_200s'],df['ticker'],df['intervl'],
######                               df['Close_d'],df['compare_d'],df['Close_1d_ch'],df['Close_3d_ch'],df['Close_5d_ch'],df['Close_30d_ch'],df['swng'],
######                               df['MA->'],df['CCI/RSI->'],df['Close->'],df['HA->'],
######                               df['crash->'],df['crash'],df['MSTR->'],df['MSTR'],df['Move->'],df['Move'],
######                               df['signal'],df['signal->']
######                               ],axis=1)
######
######
######
######
######
######
######
######
######             
########                 k5=k5+1
########                 if k5 > 1:
########                     break
######             
######            
######             
######
########    print(tt.tail(4))
######    print('tt-columns:',tt.columns)
######
######
######    tt.reset_index(inplace=True)        
######    for x in tt.index:
######    ##    print(tt['Volume'])
######    ##    tt['Volume'].loc[x]=numerize.numerize(tt['Volume'].loc[x])
######    ##    tt['Volume'].loc[x]=numerize.numerize((tt['Volume'].iloc[x][1]))
######        tt['Volume'].loc[x]=numerize.numerize(np.float32(tt['Volume'].loc[x]).item())
######    tt.set_index('Datetime')
######
######    print('\n',tt.columns,'\n')
######    print('uuuuu')
######
######    print('stupid stupid azhar ',tt.columns.get_loc('Close_d_ch'))
######    print('stupid stupid azhar ',tt.columns.get_loc('Close_1d_ch'))
########    print('stupid stupid azhar ',tt.columns.get_loc('MOM'))
########    print('stupid stupid azhar ',tt.columns.get_loc('*'))
######
######
########    print('all --> ',tt)
######    gg33=tt.iloc[:,[0,3,27,46,6,64,80,79,5,4,73,74,77,78]]
########    gg33=tt.iloc[:,[24,25,26,29,31,32,33,8,9,11,13,14,
########                    35,36,37,38,39,40,41,77,76,68,3,61,78,43,46,1,2,70,71,72,73,74,75,57,0,58,60,3,59,65,4,61,62,63,64,4,68,3,61,69,1,2,67,7,10,66,43,44,45,46,47,48,49]].tail(335)
######    gg33a=pd.DataFrame(gg33)
######    print('\n','Close_delta_price_by_'+str(shiftbydays)+' days','\n',gg33)
######    gg33a.to_csv("/home/az2/Downloads/44/output_57g.csv")
######    
######    print('\n\n\n')
######    print(' --------------------------- Glossary ----------------------------------')
######    print('CCI:    CCI > 100 --> down   CCI < -100 ----> Up')
######    print('RSI :   RSI between 70, 20. > 70 overbought, < 20 oversold')
######    print('ULOST:  Buy signal ULOST < 30 , sell signal ULOS > 70')
######    
######    print('DX:     The DX is usually smoothed with a moving average (i.e. the ADX).The values range from 0 to 100, but rarely get above 60.To interpret the DX, consider a high number to be a strong trend, and a low number, a weak trend.')
######    print('WilliamR: between -20 and -80. -20 is overbought/highs of its recent range, -80 is oversold/lower end of its recent range.')
######    print('ADX :   Strength of trend, 0-25 -> Absent or Weak Trend,    25-50 --> Strong Trend, ? --> 50-75, 75-100-->Extremely Strong Trend')
######    print('ATR :   ATR indicates increased volatility in the market')
######    print(' ---------------------------End of Glossary ----------------------------------')
######
########    print('Daily CCI: ', tt.tail(4))
######    ##MA = ta.SMA(df['close'])
######    ##print('MA: ',MA)
######    #########################################################################################################################
######
######            

            
hourly_buy()
