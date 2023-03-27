
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



def hourly_buy(ticker,df):
    import warnings
    import talib as ta
    warnings.filterwarnings("ignore")
    import sys


    df=pd.DataFrame(df)
    df.reset_index(drop=False, inplace=True)
    
##    from numerize import numerize
##    import openpyxl

    x34=34
    x35=35
    h=0



    
##    df['CCI']=ta.CCI(df['High'],df['Low'],df['Close'],timeperiod=5)
##    df['DX']=ta.DX(df['High'],df['Low'],df['Close'],timeperiod=5)
##    df['WILLR']=ta.WILLR(df['High'],df['Low'],df['Close'],timeperiod=5)
##    df['RSI']= ta.RSI(df['Close'], timeperiod=14)
##    df['stoch_slowk'], df['stoch_slowd'] = ta.STOCH(df['High'],df['Low'],df['Close'], fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
##    df['STOCHRSI_fastk'], df['STOCHRSI_fastd'] = ta.STOCHRSI(df['Close'], timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
##    df['macd'], df['macdsignal'], df['macdhist'] = ta.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
##    df['adx']= ta.ADX(df['High'],df['Low'],df['Close'], timeperiod=14)
##    df['WilliamsR']= ta.WILLR(df['High'],df['Low'],df['Close'], timeperiod=14)
##    df['ATR']=ta.ATR(df['High'],df['Low'],df['Close'], timeperiod=14)
##    df['ULTOSC'] = ta.ULTOSC(df['High'],df['Low'],df['Close'], timeperiod1=7, timeperiod2=14, timeperiod3=28)
##    df['ROC'] = ta.ROC(df['Close'], timeperiod=4)
##    df['PLUS_DI']=ta.PLUS_DI(df['High'],df['Low'],df['Close'], timeperiod=14)
##    df['PLUS_DM']=ta.PLUS_DM(df['High'],df['Low'], timeperiod=14)
##    df['aroondown'],df['aroonup']=ta.AROON(df['High'],df['Low'], timeperiod=14)
##    df['HT_DCPERIOD']=ta.HT_DCPERIOD(df['Close'])
##    df['HT_DCPHASE']=ta.HT_DCPHASE(df['Close'])
##    df['sine'], df['leadsine']=ta.HT_SINE(df['Close'])
    df['upper'], df['middle'], df['lower'] = ta.BBANDS(df['Close'], timeperiod=10, nbdevup=2, nbdevdn=2)
##    
    df['macd'], df['macdsignal'], df['macdhist']=ta.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
##    df['PLUS_DI']=ta.PLUS_DI(df['High'],df['Low'],df['Close'], timeperiod=14)
##    df['PLUS_DM']=ta.PLUS_DM(df['High'],df['Low'], timeperiod=14)
##    df['PPO']=ta.PPO(df['Close'], fastperiod=12, slowperiod=26, matype=0)
##    df['ROC']=ta.ROC(df['Close'], timeperiod=10)
##    df['ROCP']=ta.ROCP(df['Close'], timeperiod=10)
##    df['ROCR']=ta.ROCR(df['Close'], timeperiod=10)
##    df['ROCR100']=ta.ROCR100(df['Close'], timeperiod=10)
    df['MOM']=ta.MOM(df['Close'], timeperiod=3)
##
##    df['CDLDOJI']=ta.CDLDOJI(df['Open'], df['High'],df['Low'],df['Close'])
##    df['CDLDOJISTAR']=ta.CDLDOJISTAR(df['Open'], df['High'],df['Low'],df['Close'])
##    df['CDLDRAGONFLYDOJI']=ta.CDLDRAGONFLYDOJI(df['Open'], df['High'],df['Low'],df['Close'])
##    df['CDLEVENINGDOJISTAR']=ta.CDLEVENINGDOJISTAR(df['Open'], df['High'],df['Low'],df['Close'], penetration=0)
##    df['CDLGRAVESTONEDOJI']=ta.CDLGRAVESTONEDOJI(df['Open'], df['High'],df['Low'],df['Close'])
##    df['CDLHAMMER']=ta.CDLHAMMER(df['Open'], df['High'],df['Low'],df['Close'])
##    df['CDLXSIDEGAP3METHODS']=ta.CDLXSIDEGAP3METHODS(df['Open'], df['High'],df['Low'],df['Close'])
##    aroondown, aroonup = ta.AROON(df['High'],df['Low'], timeperiod=3)

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
    

    
    q=0
    k=0
    k3=0
    k4=0
    for x in df.index:
        
        
        
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


############################ end of ha ######################

            
#########################################  buy Algoritham ###################################
##        df['MOM']=df['MOM'].replace(NaaN,0)  
        mom_min=df['MOM'].min()
        mom_max=df['MOM'].max()
        mom_avg=sum(df['MOM'])/len(df['MOM'])

        macd_min=df['macd'].min()
        macd_max=df['macd'].max()
        macd_avg=sum(df['macd'])/len(df['macd'])

        HA_min=df['macd'].min()
        HA_max=df['macd'].max()
        HA_avg=sum(df['macd'])/len(df['macd'])

        upper_min=df['upper'].min()
        upper_max=df['upper'].max()
        upper_avg=sum(df['upper'])/len(df['upper'])

##        Close_1d_ch_min=df['Close_1d_ch'].min()
##        Close_1d_ch_max=df['Close_1d_ch'].max()
##        Close_1d_ch_avg=sum(df['Close_1d_ch'])/len(df['Close_1d_ch'])
        

        
##        df['MOM'] = df['MOM'].fillna(0)

##
### mrna
##        if (df['MOM'].loc[x])  > 0 and\
##           df['HA'].loc[x] > 5:


# sabir test
        if df['Close'].loc[x] > 420 and df['Close'].loc[x] < 421:
            k3=x


##### Sabir 2                  
##        if df['MOM'].shift(1).loc[x]-df['MOM'].shift(2).loc[x] > mom_min+.30*mom_min and\
##           df['Close'].loc[x] > 430:

### Sabir 2                  
##        if df['MOM'].shift(1).loc[x]-df['MOM'].shift(2).loc[x] > 5 and\
##           df['MOM'].loc[x]-df['MOM'].shift(1).loc[x]  > 35 and\
##           (df['MOM'].loc[x])  > 10 and\
##           (df['macd'].loc[x])  > 10 and\
##           (df['Close_1d_ch'].loc[x])  > 15  and\
##           df['HA'].loc[x] > 5 and\
##           (df['HA'].shift(1).loc[x]) > 5 and\
##           df['upper'].loc[x]-df['upper'].shift(1).loc[x] > 10 and\
##           (df['Close_1d_ch'].shift(1).loc[x])  > 33:

##### Sabir 22
##        if df['MOM'].shift(1).loc[x]-df['MOM'].shift(2).loc[x] > 5 and\
##           df['MOM'].loc[x]-df['MOM'].shift(1).loc[x]  > 5 and\
##           (df['MOM'].loc[x])  > 10 and\
##           (df['macd'].loc[x])  > 10 and\
##           (df['Close_1d_ch'].loc[x])  > 15  and\
##           df['HA'].loc[x] > 5 and\
##           (df['HA'].shift(1).loc[x]) > 5 and\
##           df['upper'].loc[x]-df['upper'].shift(1).loc[x] > 25 :




# Sabir 3

##           df['Close_1d_ch'].shift(1).loc[x]  > 33 and\
##        if (df['MOM'].loc[x])  > 30 and\
##           df['macd'].loc[x]  > 10 and\
##           df['Close_1d_ch'].loc[x]  > 15  and\
##           df['HA'].loc[x] > 5 and\
##           df['HA'].shift(1).loc[x] > 5 :
##

# Sabir 4
##        if (df['Close_1d_ch'].loc[x])  < -17:
##            df['signal'].loc[x]='**Sell_Signal**'
##           df['Close_1d_ch'].shift(1).loc[x]  > 33 and\
##           df['EMA_3'].loc[x] > 0 and\
##           df['EMA_3'].loc[x] > df['EMA_5'].loc[x] and\
##           df['EMA_5'].loc[x] > df['EMA_21'].loc[x] and\
##           df['EMA_3'].shift(1).loc[x] > 0 and\   



########################################################################################



            
            df['signal'].loc[x]='Buy_Signal'
##            print(df['Close'].loc[x])
##            print(k3,'  buy value: ', buy)

            df['signal'].loc[x]='rr///Buy_Signal'
            m33=df['Close'].loc[x]
##            print("Buy **********************************************************",'\n')
##            print("buy ---->")      
##            print('\n\n\n',k3, "longer=== buy ",df['Close'].loc[x])
            h=h+1 
            k4=k4+1
##            print('\n','*************************************************')
##            print('\n\n\n',"buy script", h,'   ',k3,' buy price: ',m33)
            k3=x
            print('(buy signal--> )','  ',df['Datetime'].loc[x],'  ',k4, '  ',h,"buy signal --- (from buy signal script) m33= ", m33.round(2))
            hourly_sell(ticker,k3,k4,m33,df)
##            print("Calling sell")

            # where:
            # k3= line number of df.
            # k4= buy signal no.
            # m33=close price of buy signal.

##
##            k3=k3+1
##            q=k3
##    print(h,'  ',"buy complete , line no of df/buy refrence: ",k3)        

############################################################################################################################################################                        
#andrea boggs########################################### sell #############################
###############################################SELL########################################################################################################
    
######################################## end #############################################
def hourly_sell(ticker,k3,k4,m33,df):
    
    import warnings
    warnings.filterwarnings("ignore")
    import sys

    
    from numerize import numerize
    import openpyxl

    x34=34
    x35=35
    h=0



    df2=pd.DataFrame()

    
##    df['CCI']=ta.CCI(df['High'],df['Low'],df['Close'],timeperiod=5)
##    df['DX']=ta.DX(df['High'],df['Low'],df['Close'],timeperiod=5)
##    df['WILLR']=ta.WILLR(df['High'],df['Low'],df['Close'],timeperiod=5)
##    df['RSI']= ta.RSI(df['Close'], timeperiod=14)
##    df['stoch_slowk'], df['stoch_slowd'] = ta.STOCH(df['High'],df['Low'],df['Close'], fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
##    df['STOCHRSI_fastk'], df['STOCHRSI_fastd'] = ta.STOCHRSI(df['Close'], timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
##    df['macd'], df['macdsignal'], df['macdhist'] = ta.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
##    df['adx']= ta.ADX(df['High'],df['Low'],df['Close'], timeperiod=14)
##    df['WilliamsR']= ta.WILLR(df['High'],df['Low'],df['Close'], timeperiod=14)
##    df['ATR']=ta.ATR(df['High'],df['Low'],df['Close'], timeperiod=14)
##    df['ULTOSC'] = ta.ULTOSC(df['High'],df['Low'],df['Close'], timeperiod1=7, timeperiod2=14, timeperiod3=28)
##    df['ROC'] = ta.ROC(df['Close'], timeperiod=4)
##    df['PLUS_DI']=ta.PLUS_DI(df['High'],df['Low'],df['Close'], timeperiod=14)
##    df['PLUS_DM']=ta.PLUS_DM(df['High'],df['Low'], timeperiod=14)
##    df['aroondown'],df['aroonup']=ta.AROON(df['High'],df['Low'], timeperiod=14)
##    df['HT_DCPERIOD']=ta.HT_DCPERIOD(df['Close'])
##    df['HT_DCPHASE']=ta.HT_DCPHASE(df['Close'])
##    df['sine'], df['leadsine']=ta.HT_SINE(df['Close'])
##    
    df['macd'], df['macdsignal'], df['macdhist']=ta.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    df['upper'], df['middle'], df['lower'] = ta.BBANDS(df['Close'], timeperiod=10, nbdevup=2, nbdevdn=2)
##    df['PLUS_DI']=ta.PLUS_DI(df['High'],df['Low'],df['Close'], timeperiod=14)
##    df['PLUS_DM']=ta.PLUS_DM(df['High'],df['Low'], timeperiod=14)
##    df['PPO']=ta.PPO(df['Close'], fastperiod=12, slowperiod=26, matype=0)
##    df['ROC']=ta.ROC(df['Close'], timeperiod=10)
##    df['ROCP']=ta.ROCP(df['Close'], timeperiod=10)
##    df['ROCR']=ta.ROCR(df['Close'], timeperiod=10)
##    df['ROCR100']=ta.ROCR100(df['Close'], timeperiod=10)
    df['MOM']=ta.MOM(df['Close'], timeperiod=3)
##
##    df['CDLDOJI']=ta.CDLDOJI(df['Open'], df['High'],df['Low'],df['Close'])
##    df['CDLDOJISTAR']=ta.CDLDOJISTAR(df['Open'], df['High'],df['Low'],df['Close'])
##    df['CDLDRAGONFLYDOJI']=ta.CDLDRAGONFLYDOJI(df['Open'], df['High'],df['Low'],df['Close'])
##    df['CDLEVENINGDOJISTAR']=ta.CDLEVENINGDOJISTAR(df['Open'], df['High'],df['Low'],df['Close'], penetration=0)
##    df['CDLGRAVESTONEDOJI']=ta.CDLGRAVESTONEDOJI(df['Open'], df['High'],df['Low'],df['Close'])
##    df['CDLHAMMER']=ta.CDLHAMMER(df['Open'], df['High'],df['Low'],df['Close'])
##    df['CDLXSIDEGAP3METHODS']=ta.CDLXSIDEGAP3METHODS(df['Open'], df['High'],df['Low'],df['Close'])
##    aroondown, aroonup = ta.AROON(df['High'],df['Low'], timeperiod=3)

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



    df2=df

    df['Opena']=''
    df['green']=''
    df['greenby']=''
    df['compare_d']=''
    buy = '3'
##    print('\n','****************************************************','\n')
##    print("jjjj ",df)
##    print('\n','****************************************************','\n')
##    k3=0
    h=0
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
##    
##    q=0
##    k=0
####    k3s=0
    t=0
    t5=0 

    for x in df.index:
        t5=t5+1
        k3s=k3+t5
        h=h+1
##        if k3s == k3:
##            t=0
##        df['CDLDRAGONFLYDOJI'].loc[x]=ta.CDLDRAGONFLYDOJI(df['Open'].loc[x], df['High'].loc[x],df['Low'].loc[x],df['Close'].loc[x])
##        if df['MOM'].loc[x] < 0:
##            k=k+1
##            (df['ff']).append(df['MOM'])
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

##        k4=0    
#########################################  buy ###################################
  

############################################################################################################################################################            
          
            
#andrea boggs########################################### sell #############################
##           (df['MOM'].loc[x])  < 5 or df['Close_1d_ch'].loc[x] < -60 and\
##           (df['EMA_3'].loc[x]) < 0 and\

###############################################SELL########################################################################################################
        if x > k3:
            

##        print('k3s=',k3s,'  k3=',k3,'   ',df['Close'].loc[x],' t=',t)


            
#################################### SELL Algoritham ##################################################################

### Sabir 2            
##  
##        print(k3s, " in sell ", ticker,' k3=',k3,' k4=',k4,' m33=',m33)

            
            if  df['Close'].loc[x]-m33 > 5:
                
##               (df['Close_1d_ch'].loc[x])  < -3:
##                print(k3s,"  in sell function ",'k3=',k3,' k4=',k4,'m33=',m33)


##        if k3s >= k3 and df['Close'].loc[x]-m33 > 3 and\
##           (df['EMA_3'].loc[x]) < .12 and\
##           (df['MOM'].loc[x]) < 0 and\
##           (df['Close_1d_ch'].loc[x])  < -.7:


##### Sabir 2            
####
##        if k3s >= k3 and df['Close'].loc[x]-m33 > 50 and\
##           (df['EMA_3'].loc[x]) < 12 and\
##           (df['MOM'].loc[x]) < 0 and\
##           (df['Close_1d_ch'].loc[x])  < -7:


# Sabir 23    (df['MOM'].loc[x]) < 0 and\        (df['Close_1d_ch'].loc[x])  < 0

##        if k3s >= k3 and\
##           (df['MOM'].loc[x])-df['MOM'].shift(1).loc[x] < -90 and\
##           (df['EMA_3'].loc[x]) < 12 and\
##           (df['MOM'].loc[x]) < 0 and\
##           (df['Close_1d_ch'].loc[x])  < -20:

### Sabir 3
##        if k3s >= k3 and df['Close'].loc[x]-m33 > 80 and\
##           (df['MOM'].loc[x])  < 5 or df['Close_1d_ch'].loc[x] < -60 and\
##           (df['EMA_3'].loc[x]) < 0 and\
##           (df['Close_1d_ch'].loc[x])  < -40:
##
# Sabir 4
##
##        if k3s >= k3 and ((df['MOM'].loc[x])  < 0 and\
##           (df['EMA_3'].loc[x]) > 0 and\
##           (df['Close_1d_ch'].loc[x])  < 0) and\
##           df['HA'].loc[x] < 6 and\
##           df['Close'].loc[x]-m33 > 0:


#######################################################################################################            
            
                df['signal'].loc[x]='** Major Sell_Signal'
                m33n=df['Close'].loc[x]    
                df['signal'].loc[x]='///Sell_Signal'
##             print("sell ---->",)
##             print(x, "*** === sell ",df['Close'].loc[x],'   points: ',df['Close'].loc[x]-m33,'  (Profit) [m33-m34]-> ',m33-m34,' \n')
##             print('close_1day_ch==>  ',df['Close_1d_ch'].loc[x],'  close-m33-->  ',df['Close'].loc[x]-m33,'\n')
##             print('MOM: ',df['MOM'].loc[x], 'EMA(3): ',df['EMA_3'].loc[x],' EMA21: ',df['EMA_3'].loc[x])
##             print('**********************************************************************************')
##             print('\n\n')
##             file1 = open("/home/az2/Downloads/bitcoin_stuff.txt","a+")
##             file1.write(str(h)+' m33  '+str(m33.round(2))+' m34  '+str(m33s)+'  profit-->    '+str((m33-m33s).round(2)))
##             file1.write('\n')
##             file1.close()
##             h=h+1
##             
##             print(t," sell script sell=", m33n)

##             print("sell script sell=", m33n,'   buy= ',m33s, '  k3=',k3, '   [profit]=',m33n-m33s, '  in ',t ,' minutes')

##                print('(sell signal--> )','(from sell script)  ',ticker,'  ','[profit]=',(m33n-m33).round(2), '  in ',t ,' minutes', "sell= ", m33n.round(2),'sell row= ',
##                      k3s,'****   buy= ',m33.round(2), ' buy row no k3=',k3)

                print(x,' (sell signal--> )',df['Datetime'].loc[x],'  ',m33.round(2),'/',(m33n).round(2),'  ','[profit]=',(m33n-m33).round(2), '  in ',
                      t ,' minutes', "sell= ", m33n.round(2),'sell row= ',
                      k3s,'****   buy= ',m33.round(2), ' buy row no k3=',k3, ' sell row:',x )
                 
                print('**********************************************************************************')
    ##             print('from buy signal --- one min ts before ejecting  ',t)
                break

##        print("sell script complete ",h,' sell refrence no: ',k3)
             #######################################################################






from numerize import numerize
import openpyxl


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
##ticker='BTC-USD'
ticker='MRNA'
##    ticker='MSTR'
##    ticker='MRNA'

# [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]



#df=pd.DataFrame()
#Interval required 5 minutes
df = yf.download(ticker, period=perd, interval=intervl)
print(df)
df2=pd.DataFrame()


            
hourly_buy(ticker,df)
