import talib as ta
from ta.utils import dropna
import yfinance as yf
import pandas as pd
import sys
import re
import numpy as np
from talib import stream
from matplotlib import dates
import matplotlib.pyplot as plt
##from datetime import date
##today = date.today().isoformat()
import datetime
import math
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
plt.style.use('fivethirtyeight')
from millify import millify
##today = datetime.date.today() + datetime.timedelta(days=1)
today = datetime.date.today()
##day = datetime.datetime.strptime(Date, '%d %m %Y').weekday()
##print(datetime.today().strftime('%Y-%m-%d'))
import mpl_finance
import matplotlib
import sys
##from matplotlib.finance import candlestick2_ohlc
##from mpl_finance import candlestick_ohlc
##from mplfinance.original_flavor import candlestick_ohlc
from mplfinance.original_flavor import candlestick_ohlc
from optionprice import Option
from numerize import numerize
import matplotlib.pyplot as plt
pd.options.display.width = 0
pd.set_option('display.max_columns', None)
pd.options.display.float_format = '{:.2f}'.format
##pd.options.display.max_columns=255
pd.options.display.max_rows=6500000
pd.set_option('display.max_colwidth', 500)
pd.set_option('display.max_columns', 550)
pd.options.mode.chained_assignment = None  # default='warn'



def days():
    import sys
    

    
    perda='1d'
    intervla='1m'
    yy=str(intervla).split('d')[0]
    shiftbydays=3



    ##    g=input("Entr_Signal ticker: ")
    perd=perda
    intervl=intervla
##    ticker='BTC-USD'
##    ticker='^NDX'
##    ticker='MSTR'
    ticker='MRNA'
##    ticker='AMZN'
##    ticker='TSLA'
##    ticker='DOCU'
    # [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]

    

    #df=pd.DataFrame()
    #Interval required 5 minutes
    df = yf.download(ticker, period=perd, interval=intervl,prepost = True)
    df=pd.DataFrame(df)
##    print(df.tail(4))
    print('========== running ===========')

    
    df2=pd.DataFrame()
    df['*']=''
    df['Candlea']=''
##    print(df.columns)
    for x in df.index:
        df['Candlea'].loc[x]=df['High'].loc[x]-df['Open'].loc[x]
        df['*'].loc[x]='*'
##        df['Close_d_ch'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc(x)
    ##    print(df['Close'].loc[x])
        ################################################################################################################
    ##close = numpy.random.random(100)

##    df['SAR']=ta.SAR(df['High'],df['Low'], acceleration=0.02, maximum=0.2)
    
    df['SAREXT']=df['Close']-ta.SAREXT(df['High'], df['Low'],startvalue=0, offsetonreverse=0,
               accelerationinitlong=0.02, accelerationlong=0.02,
               accelerationmaxlong=0.20, accelerationinitshort=0.02,
               accelerationshort=0.02, accelerationmaxshort=0.20)
##    df['SAREXT']=ta.SAREXT(df['High'], df['Low'],startvalue=0, offsetonreverse=0, accelerationinitlong=0, accelerationlong=0, accelerationmaxlong=0, accelerationinitshort=0, accelerationshort=0, accelerationmaxshort=0)
    df['SAR']=df['Close']-ta.SAR(df['High'], df['Low'],acceleration=0.02, maximum=0.2)    
    df['AROONOSC']=ta.AROONOSC(df['High'], df['Low'], timeperiod=14)
    df['MOM']=ta.MOM(df['Close'], timeperiod=10)
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
    df['ROC'] = ta.ROC(df['Close'], timeperiod=10)
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

    df['CDLDOJI']=ta.CDLDOJI(df['Open'], df['High'],df['Low'],df['Close'])
    df['CDLDOJISTAR']=ta.CDLDOJISTAR(df['Open'], df['High'],df['Low'],df['Close'])
    df['CDLDRAGONFLYDOJI']=ta.CDLDRAGONFLYDOJI(df['Open'], df['High'],df['Low'],df['Close'])
    df['CDLEVENINGDOJISTAR']=ta.CDLEVENINGDOJISTAR(df['Open'], df['High'],df['Low'],df['Close'], penetration=0)
    df['CDLGRAVESTONEDOJI']=ta.CDLGRAVESTONEDOJI(df['Open'], df['High'],df['Low'],df['Close'])
    df['CDLHAMMER']=ta.CDLHAMMER(df['Open'], df['High'],df['Low'],df['Close'])
    df['CDLXSIDEGAP3METHODS']=ta.CDLXSIDEGAP3METHODS(df['Open'], df['High'],df['Low'],df['Close'])
    aroondown, aroonup = ta.AROON(df['High'],df['Low'], timeperiod=3)



    
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
    df['BB_upperband'], df['BB_middleband'], df['BB_lowerband'] = ta.BBANDS(df['Close'], timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
    
##    df['day']=Date.Date(df['Datetime'])
##    df['BB_upperband'], df['BB_middleband'], df['BB_lowerband'] = ta.BBANDS(df['Close'], timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
##    
    

    #############################
    ##for x in df.index:
    ##            df['Volume'].loc[x]=numerize.numerize(np.float32(df['Volume'].loc[x]).item())

    df2=df

    df['Opena']=''
    df['green']=''
    df['greenby']=''
    df['compare_d']=''
    
    df['Candle']=''
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
    df['swng->']=''
    df['*']=''
    df['MA->']=''
    df['CCI/RSI->']=''
    df['HA->']=''
    df['Close->']=''

    df['BB_up']=''
    df['BB_low']=''
    df['BB_mid']=''
    df['Bolinger']=''
    df['volatility']=''
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
    df['adx->']=''
    df['bol_wd']=''
    df['up_bol_wd']=''
    df['lw_bol_wd']=''
    df['Buy_50EMA_100EMA']=''
    df['Buy_21EMA_50EMA']=''
    df['Buy_5EMA_21EMA']=''
    df['Buy_100EMA_200EMA']=''
    df['Buy_5EMA_10EMA']=''
    df['delta_Low']=''
    df['delta_High']=''
    df['delta_Open']=''
    df['delta_Close']=''
    df['Price_from_BBUP']=''
    df['Price_from_BBLWR']=''
    df['Price_from_BBMid']=''
    df['3_5_crossovr']=''
    df['5_10_crossovr']=''
    df['10_21_crossovr']=''
    df['21_50_crossovr']=''
    df['50_100_crossovr']=''
    df['100_200_crossovr']=''
    df['Price_3_crossovr']=''
    df['upward_pressure']=''
    df['downward_pressure']=''
    df['Closev']=''
    df['3_5_crossovr_c']=''
    df['signal4']=''
    df['f']=''

##    print("Jjjjjj  ",type(df['f']),'  ',type(df['f'].values.tolist()))
##    print("Jjjjjj  ",type(df['f']),'  ',type(df['f'].to_string()))
##    print("Jjjjjj  ",type(df['f']),'  ',type(df['f'].astype('int')))
##    print("Jjjjjj  ",type(df['f']),'  ',type(df['f'].apply(int)))
##    df['f'] = df['f'].astype(int)
##    df['f'] = df['f'].astype(str).astype(int)
##    print(type(df['f']))
#################################################################
    for x in df.index:
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

########################################################################
    df['Closev'] = (1/df['Close'])*(100)
    for x in df.index:
        df['Closev'].loc[x]=df['Closev'].loc[x]
        df['upward_pressure'].loc[x]=df['PLUS_DM'].loc[x]-df['PLUS_DI'].loc[x]
        df['downward_pressure'].loc[x]=df['PLUS_DI'].loc[x]-df['PLUS_DM'].loc[x]
        df['Candle'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
        df['swng->'].loc[x]='swng->'
        df['adx->'].loc[x]='adx->'
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
        df['a_High'].loc[x]=max(df['High'].loc[x],df['a_Open'].loc[x],df['a_Close'].loc[x])
        df['a_Low'].loc[x]=min(df['Low'].loc[x],df['a_Open'].loc[x],df['a_Close'].loc[x])


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


        df['delta_Low'].loc[x]=df['Low'].loc[x]-df['Low'].shift(1).loc[x]
        df['delta_High'].loc[x]=df['High'].loc[x]-df['High'].shift(1).loc[x]
        df['delta_Open'].loc[x]=df['Open'].loc[x]-df['Open'].shift(1).loc[x]
        df['delta_Close'].loc[x]=df['High'].loc[x]-df['High'].shift(1).loc[x]



        
        df['pivot'].loc[x]='pivot->'

        df['pp'].loc[x]=df['Close'].loc[x]
        df['pp'].loc[x]=(df['Close'].loc[x]+df['Low'].loc[x]+df['High'].loc[x])/3
        df['r1'].loc[x]=2*df['pp'].loc[x]-df['Low'].loc[x].round(0)
        df['r2'].loc[x]=df['pp'].loc[x]+(df['High'].loc[x]-df['Low'].loc[x])
        df['s1'].loc[x]=2*df['pp'].loc[x]-df['High'].loc[x]
        df['s2'].loc[x]=df['pp'].loc[x]-(df['High'].loc[x]-df['Low'].loc[x])
        df['r3'].loc[x]=df['High'].loc[x]+2*(df['pp'].loc[x]-df['Low'].loc[x])
        df['s3'].loc[x]=df['Low'].loc[x]-2*(df['High'].loc[x]-df['pp'].loc[x])
        df['pivotx'].loc[x]=df['Close'].loc[x]-df['pp'].loc[x]
        if df['pivotx'].loc[x] > 0:
            df['pivotx'].loc[x]='Price > pivot'
        else:
            df['pivotx'].loc[x]='Price < pivot'

        df['ppx'].loc[x]=df['Close'].loc[x]-df['pp'].loc[x]
        df['r1x'].loc[x]=-1*(df['Close'].loc[x]-df['r1'].loc[x])
        df['r2x'].loc[x]=-1*(df['Close'].loc[x]-df['r2'].loc[x])
        df['r3x'].loc[x]=-1*(df['Close'].loc[x]-df['r3'].loc[x])
        
        df['s1x'].loc[x]=-1*(df['s1'].loc[x]-df['Close'].loc[x])
        df['s2x'].loc[x]=-1*(df['s2'].loc[x]-df['Close'].loc[x])
        df['s3x'].loc[x]=-1*(df['s3'].loc[x]-df['Close'].loc[x])
        df['bol_wd'].loc[x]=df['BB_upperband'].loc[x]-df['BB_lowerband'].loc[x]
        df['up_bol_wd'].loc[x]=df['BB_upperband'].loc[x]-df['BB_middleband'].loc[x]
        df['lw_bol_wd'].loc[x]=df['BB_upperband'].loc[x]-df['BB_middleband'].loc[x]

        
        df['volatility'].loc[x]=df['BB_upperband'].loc[x]-df['BB_lowerband'].loc[x]
        df['Bolinger'].loc[x]='Bolinger'
        df['BB_up'].loc[x]=df['Close'].loc[x]-df['BB_upperband'].loc[x]
        df['BB_low'].loc[x]=df['Close'].loc[x]-df['BB_lowerband'].loc[x]
        df['BB_mid'].loc[x]=df['Close'].loc[x]-df['BB_middleband'].loc[x]
        df['Buy_50EMA_100EMA'].loc[x]=df['EMA_50s'].loc[x]-df['EMA_100s'].loc[x]
        df['Buy_21EMA_50EMA'].loc[x]=df['EMA_21s'].loc[x]-df['EMA_50s'].loc[x]
        df['Buy_5EMA_21EMA'].loc[x]=df['EMA_5s'].loc[x]-df['EMA_21s'].loc[x]
        df['Buy_100EMA_200EMA'].loc[x]=df['EMA_100s'].loc[x]-df['EMA_200s'].loc[x]
        df['Buy_5EMA_10EMA'].loc[x]=df['EMA_5s'].loc[x]-df['EMA_10s'].loc[x]
        df['Price_from_BBUP'].loc[x]=df['BB_upperband'].loc[x]-df['Close'].loc[x]
        df['Price_from_BBLWR'].loc[x]=df['Close'].loc[x]-df['BB_lowerband'].loc[x]
        df['Price_from_BBMid'].loc[x]=df['BB_middleband'].loc[x]-df['Close'].loc[x]
        df['3_5_crossovr'].loc[x]=df['EMA_3'].loc[x]-df['EMA_5'].loc[x]
        
        df['5_10_crossovr'].loc[x]=df['EMA_5s'].loc[x]-df['EMA_10s'].loc[x]
        df['10_21_crossovr'].loc[x]=df['EMA_10s'].loc[x]-df['EMA_21s'].loc[x]
        df['21_50_crossovr'].loc[x]=df['EMA_21s'].loc[x]-df['EMA_50s'].loc[x]
        df['50_100_crossovr'].loc[x]=df['EMA_50s'].loc[x]-df['EMA_100s'].loc[x]
        df['100_200_crossovr'].loc[x]=df['EMA_100s'].loc[x]-df['EMA_200s'].loc[x]
        df['Price_3_crossovr'].loc[x]=df['Close'].loc[x]-df['EMA_3s'].loc[x]

#########################################################################
##    print(" =========== Before concat /running =========== ")
    ##ddd=(df['Volume']-df['Volume'].shift(1))
    tt=pd.concat([df['bol_wd'],df['up_bol_wd'],df['lw_bol_wd'],df['Closev'],
                  df['BB_upperband'], df['BB_middleband'], df['BB_lowerband'],
                  df['Candle'],df['MOM'],df['direct'],df['HA'],df['Close'],df['Close_d_ch'],df['Volume'],df['swng->'],df['adx->'],
                  df['Volumea'],df['CCI'],df['DX'],df['WILLR'],df['RSI'],df['adx'],df['WilliamsR'],
                  df['ATR'],df['ULTOSC'],
                  df['ROC'],df['PLUS_DI'],df['PLUS_DM'],
                  df['HT_DCPERIOD'],
                  df['HT_DCPHASE'],
                  df['sine'],df['leadsine'],df['aroondown'], df['aroonup'],
                  df['macd'], df['macdsignal'], df['macdhist'],df['PLUS_DI'],df['PLUS_DM'],df['PPO'],df['ROC'],df['ROCP'],
                  df['ROCR'],df['ROCR100'],
                  df['*'],
                  df['CDLDOJI'],df['CDLDOJISTAR'],df['CDLDRAGONFLYDOJI'],df['CDLEVENINGDOJISTAR'],df['CDLGRAVESTONEDOJI'],
                  df['CDLHAMMER'],df['CDLXSIDEGAP3METHODS'],
                  df['*'],df['EMA_3'],df['EMA_5'],df['EMA_10'],df['EMA_21'],df['EMA_50'],df['EMA_100'],df['EMA_200'],df['EMA_3s'],
                  df['EMA_5s'],df['EMA_10s'],df['EMA_21s'],df['EMA_50s'],df['EMA_100s'],df['EMA_200s'],df['ticker'],df['intervl'],
                  df['Close_d'],df['compare_d'],df['Close_1d_ch'],df['Close_3d_ch'],df['Close_5d_ch'],df['Close_30d_ch'],df['swng'],
                  df['MA->'],df['CCI/RSI->'],df['Close->'],df['HA->'],
                  df['Close->'],df['swng->'],df['Low'],df['High'],df['Open'],
##                  df['open/close'],
##                  df['CCI/RSI->'],df['HA->'],
##                  df['MA->']
                  df['BB_up'],df['BB_low'],df['BB_mid'],df['Bolinger'],df['volatility'],
                  df['pivot'],df['pp'],df['r1'],df['r2'],df['r3'],df['s1'],df['s2'],df['s3'],df['pivotx'],
                  df['ppx'],df['r1x'],df['r2x'],df['r3x'],df['s1x'],df['s2x'],df['s3x'],
                   df['stoch_slowk'], df['stoch_slowd'],df['STOCHRSI_fastk'], df['STOCHRSI_fastd'],df['macd'], df['macdsignal'], df['macdhist'] ,
                  df['macd'], df['macdsignal'], df['macdhist'],
                  df['Buy_5EMA_10EMA'],df['Buy_5EMA_21EMA'],df['Buy_21EMA_50EMA'],

                  df['Buy_50EMA_100EMA']
                  ,df['Buy_100EMA_200EMA'],df['AROONOSC'],df['SAR'],df['SAREXT'],
                  df['delta_Low'],df['delta_High'],df['delta_Open'],df['delta_Close'],
                  df['Price_from_BBUP'],df['Price_from_BBLWR'],df['Price_from_BBMid'],
                  df['3_5_crossovr'],df['5_10_crossovr'],df['10_21_crossovr'],df['21_50_crossovr'],df['50_100_crossovr'],df['Price_3_crossovr']
                  ,df['upward_pressure'],df['downward_pressure'],df['Closev'],
                  df['3_5_crossovr_c'],df['f'],df['100_200_crossovr']

                  ],axis=1)


    tt.reset_index(inplace=True)
    tt.set_index=('Datetime')
##    print('tt-columns:',tt.columns)
##    print('tt length:', len(tt.columns))
    tt.reset_index(inplace=True)        
    for x in tt.index:
    ##    print(tt['Volume'])
    ##    tt['Volume'].loc[x]=numerize.numerize(tt['Volume'].loc[x])
    ##    tt['Volume'].loc[x]=numerize.numerize((tt['Volume'].iloc[x][1]))
        tt['Volume'].loc[x]=numerize.numerize(np.float32(tt['Volume'].loc[x]).item())


##    print(tt.columns)
    gg33=tt[['index', 'Datetime','ticker', 'pivot','pivotx','pp','*','Close_1d_ch','*','r1','r2','r3','*','s1','s2','s3','*','volatility','*',
             'intervl','Close','Close_1d_ch','Candle', 'MOM', 'swng','direct', 'HA','Volume','*','*',
               'EMA_3','EMA_5', 'EMA_10', 'EMA_21', 'EMA_50', 'EMA_100', 'EMA_200','*','*',
             'EMA_3s','EMA_5s', 'EMA_10s', 'EMA_21s', 'EMA_50s', 'EMA_100s', 'EMA_200s','*','*',
              'volatility','bol_wd', 'up_bol_wd', 'lw_bol_wd', 'BB_upperband','BB_middleband', 'BB_lowerband','*','*',
             'Low', 'High','Open','Close','*','*','Close_1d_ch','Close_d', 'compare_d','Close_3d_ch', 'Close_5d_ch', 'Close_30d_ch','Close_d_ch','*','*',
            'CDLDOJI','CDLDOJISTAR', 'CDLDRAGONFLYDOJI', 'CDLEVENINGDOJISTAR','CDLGRAVESTONEDOJI', 'CDLHAMMER', 'CDLXSIDEGAP3METHODS','*','*','CCI','DX', 'WILLR', 'RSI', 'adx', 'WilliamsR', 'ATR', 'ULTOSC', 'ROC','PLUS_DI', 'PLUS_DM', 'HT_DCPERIOD', 'HT_DCPHASE', 'sine',
             'leadsine','aroondown', 'aroonup', 'macd', 'macdsignal', 'macdhist', 'PLUS_DI','PLUS_DM', 'PPO', 'ROC', 'ROCP', 'ROCR', 'ROCR100', '*','*',
             
            'pivot','pp','*','r1','r2','r3','*','s1','s2','s3','*','*',
            'pivotx',
            'ppx','*','r1x','r2x','r3x','*','s1x','s2x','s3x','*','*',
              'stoch_slowk', 'stoch_slowd','STOCHRSI_fastk', 'STOCHRSI_fastd','RSI','CCI','ULTOSC','WILLR',
             'macd','macdsignal', 'macdhist' ,'MOM','PLUS_DI','PLUS_DM', 'PPO', 'ROC',
             'ROCP', 'ROCR', 'ROCR100',
             'Buy_5EMA_10EMA','Buy_5EMA_21EMA','Buy_21EMA_50EMA','Buy_50EMA_100EMA','Buy_100EMA_200EMA',
             'adx','aroondown','aroonup','AROONOSC','SAR','SAREXT',
             'delta_Low','delta_High','delta_Open','delta_Close','Candle','Close_1d_ch','Volume',
             'Price_from_BBUP','Price_from_BBLWR','Price_from_BBMid','bol_wd',
              '3_5_crossovr','5_10_crossovr','10_21_crossovr','21_50_crossovr','50_100_crossovr','Price_3_crossovr'
              ,'upward_pressure','downward_pressure','Closev','5_10_crossovr','f'
             
            

             ]]

############################################################

    
# if STOCHRSI_fastk=100, stock will be green.
    gg33=gg33[np.float64(gg33['STOCHRSI_fastk']) == 100]
##    print('STOCHRSI_fastk=100 ----> ',gg33)


# if aroonup=100, stock will be green.
    gg33=gg33[np.float64(gg33['aroonup']) == 100]
##    print('aroonup=100 ----> ',gg33)
    
# if aroonup=0, stock will be red.
    gg33=gg33[np.float64(gg33['aroonup']) == 0]
##    print('aroonup=0 ----> ',gg33)


# if macdhist > 0, stock will be Green.
    gg33=gg33[np.float64(gg33['macdhist']) > 0]
##    print('macdhist > 0 ----> ',gg33)

# if macdhist < 0, stock will be Red.
    gg33=gg33[np.float64(gg33['macdhist']) < 0]
##    print('macdhist < 0 ----> ',gg33)

# if ROC > 0, stock will be Green.
    gg33=gg33[np.float64(gg33['ROC']) > 0]
##    print('macdhist > 0 ----> ',gg33)

# if ROC < 0, stock will be Red.
    gg33=gg33[np.float64(gg33['ROC']) < 0]
##    print('macdhist < 0 ----> ',gg33)    

##    s3=str(gg33b['Datetime']).split(' ')
##    for x in gg33b.index:
##        print(gg33b['5_10_crossovr'].loc[x])
##        print(str(gg33b['Datetime'].loc[x]).split(' '))




##    print('\n')
##    print('*************************************************************************************************************')
##    print('\n')
    gg33b=tt[['index', 'Datetime','ticker', 'pivot','pivotx','pp','*','Close_1d_ch','Candle', 'MOM', 'swng','direct', 'HA','Volume','*','*',
           'EMA_3','EMA_5', 'EMA_10', 'EMA_21', 'EMA_50', 'EMA_100', 'EMA_200','*','*',
         'EMA_3s','EMA_5s', 'EMA_10s', 'EMA_21s', 'EMA_50s', 'EMA_100s', 'EMA_200s','*','*',
          'volatility','bol_wd', 'up_bol_wd', 'lw_bol_wd', 'BB_upperband','BB_middleband', 'BB_lowerband','*','*',
         'Low', 'High','Open','Close','*','Close_30d_ch','Close_d_ch','*','*',
        'CDLDOJI','CDLDOJISTAR', 'CDLDRAGONFLYDOJI', 'CDLEVENINGDOJISTAR','CDLGRAVESTONEDOJI', 'CDLHAMMER', 'CDLXSIDEGAP3METHODS','*','*','CCI','DX', 'WILLR', 'RSI', 'adx', 'WilliamsR', 'ATR', 'ULTOSC', 'ROC','PLUS_DI', 'PLUS_DM', 'HT_DCPERIOD', 'HT_DCPHASE', 'sine',
         'leadsine','aroondown', 'aroonup', 'macd', 'macdsignal', 'macdhist', 'PLUS_DI','PLUS_DM', 'PPO', 'ROC', 'ROCP', 'ROCR', 'ROCR100', '*','*',
          'stoch_slowk', 'stoch_slowd','STOCHRSI_fastk', 'STOCHRSI_fastd','RSI','CCI','ULTOSC','WILLR',
         'macd','macdsignal', 'macdhist' ,'MOM','PLUS_DI','PLUS_DM', 'PPO', 'ROC',
         'ROCP', 'ROCR', 'ROCR100',
         'Buy_5EMA_10EMA','Buy_5EMA_21EMA','Buy_21EMA_50EMA','Buy_50EMA_100EMA','Buy_100EMA_200EMA',
         'adx','aroondown','aroonup','AROONOSC','SAR','SAREXT',
         'delta_Low','delta_High','delta_Open','delta_Close','Candle','Close_1d_ch','Volume',
         'Price_from_BBUP','Price_from_BBLWR','Price_from_BBMid','bol_wd',
          '3_5_crossovr','5_10_crossovr','10_21_crossovr','21_50_crossovr','50_100_crossovr','Price_3_crossovr','100_200_crossovr'
           ,'upward_pressure','downward_pressure','Closev','5_10_crossovr'
        

         ]]
    gg33b=tt[['index', 'Datetime','ticker', 'pivot','pivotx','pp','*','Close_1d_ch','Candle', 'MOM', 'swng','direct', 'HA', 'EMA_3','EMA_5', 'EMA_10', 'EMA_21', 'EMA_50', 'EMA_100', 'EMA_200','CCI','DX', 'WILLR', 'RSI', 'adx', 'WilliamsR', 'ATR', 'ULTOSC', 'ROC','PLUS_DI', 'PLUS_DM', 'HT_DCPERIOD', 'HT_DCPHASE', 'sine',
         'leadsine','aroondown', 'aroonup',  'macdhist', 'PLUS_DI','PLUS_DM', 'PPO', 'ROC', 'ROCP', 'ROCR', 'ROCR100', '*','*','STOCHRSI_fastk',
               'Buy_5EMA_10EMA','Buy_5EMA_21EMA','Buy_21EMA_50EMA','Buy_50EMA_100EMA','Buy_100EMA_200EMA',
         'adx','aroondown','aroonup','AROONOSC','SAR','SAREXT',
         'delta_Low','delta_High','delta_Open','delta_Close','Candle','Close_1d_ch','Volume',
         'Price_from_BBUP','Price_from_BBLWR','Price_from_BBMid','bol_wd','Close_1d_ch',
          'Price_3_crossovr',    
          '3_5_crossovr','10_21_crossovr','21_50_crossovr','50_100_crossovr',
          'Close','EMA_3s','EMA_5s', 'EMA_10s', 'EMA_21s', 'EMA_50s', 'EMA_100s', 'EMA_200s','100_200_crossovr'
           ,'upward_pressure','downward_pressure' ,'Closev','5_10_crossovr'

         ]]


##    gg33b=tt[['index', 'Datetime','ticker', 'pivot','pivotx','pp','*','Close_1d_ch','Candle', 'MOM', 'swng','direct', 'HA', 'EMA_3','EMA_5', 'EMA_10', 'EMA_21', 'EMA_50', 'EMA_100', 'EMA_200','CCI','DX', 'WILLR', 'RSI', 'adx', 'WilliamsR', 'ATR', 'ULTOSC', 'ROC','PLUS_DI', 'PLUS_DM', 'HT_DCPERIOD', 'HT_DCPHASE', 'sine',
##         'leadsine','aroondown', 'aroonup',  'macdhist', 'PLUS_DI','PLUS_DM', 'PPO', 'ROC', 'ROCP', 'ROCR', 'ROCR100', '*','*','STOCHRSI_fastk',
##               'Buy_5EMA_10EMA','Buy_5EMA_21EMA','Buy_21EMA_50EMA','Buy_50EMA_100EMA','Buy_100EMA_200EMA',
##         'adx','aroondown','aroonup','AROONOSC','SAR','SAREXT',
##         'delta_Low','delta_High','delta_Open','delta_Close','Candle','Close_1d_ch','Volume',
##         'Price_from_BBUP','Price_from_BBLWR','Price_from_BBMid','bol_wd','Close_1d_ch',
##          'Price_3_crossovr',    
##          '3_5_crossovr','10_21_crossovr','21_50_crossovr','50_100_crossovr',
##          'Close','EMA_3s','EMA_5s', 'EMA_10s', 'EMA_21s', 'EMA_50s', 'EMA_100s', 'EMA_200s','100_200_crossovr'
##           ,'upward_pressure','downward_pressure' ,'Closev','5_10_crossovr','f','EMA_3','EMA_5'
##
##         ]]


    gg33b=tt[['index', 'Datetime','ticker', 'pivot','pivotx','pp','*','Close_1d_ch','Candle', 'MOM', 'swng','direct', 'HA', 'EMA_3','EMA_5', 'EMA_10', 'EMA_21', 'EMA_50', 'EMA_100', 'EMA_200','CCI','DX', 'WILLR', 'RSI', 'adx', 'WilliamsR', 'ATR', 'ULTOSC', 'ROC','PLUS_DI', 'PLUS_DM', 'HT_DCPERIOD', 'HT_DCPHASE', 'sine',
     'leadsine','aroondown', 'aroonup',  'macdhist', 'PLUS_DI','PLUS_DM', 'PPO', 'ROC', 'ROCP', 'ROCR', 'ROCR100', '*','*','STOCHRSI_fastk',
           'Buy_5EMA_10EMA','Buy_5EMA_21EMA','Buy_21EMA_50EMA','Buy_50EMA_100EMA','Buy_100EMA_200EMA',
     'adx','aroondown','aroonup','AROONOSC','SAR','SAREXT',
     'delta_Low','delta_High','delta_Open','delta_Close','Candle','Close_1d_ch','Volume',
     'Price_from_BBUP','Price_from_BBLWR','Price_from_BBMid','bol_wd','Close_1d_ch',
      'Price_3_crossovr',    
      '3_5_crossovr','10_21_crossovr','21_50_crossovr','50_100_crossovr',
      'Close','EMA_3s','EMA_5s', 'EMA_10s', 'EMA_21s', 'EMA_50s', 'EMA_100s', 'EMA_200s','100_200_crossovr'
       ,'upward_pressure','downward_pressure' ,'Closev','5_10_crossovr'
       ,'*',
        'delta_Low','delta_High','delta_Open','delta_Close','Candle','Close_1d_ch','Volume',
        'Price_from_BBUP','Price_from_BBLWR','Price_from_BBMid','bol_wd',
        'aroonup','aroondown','adx','STOCHRSI_fastk','ROC','macdhist', 'WilliamsR','CCI','direct' ,'HA','MOM', 'Close_1d_ch' ,'swng','Candle',
              'EMA_3','EMA_5'

     ]]

##    gg33b=tt[['index', 'Datetime','ticker', 'pivot','pivotx','pp','*',
##                        'Price_3_crossovr',    
##          '3_5_crossovr','10_21_crossovr','21_50_crossovr','50_100_crossovr',
##          'Close','EMA_3s','EMA_5s', 'EMA_10s', 'EMA_21s', 'EMA_50s', 'EMA_100s', 'EMA_200s','100_200_crossovr'
##
##              'delta_Low','delta_High','delta_Open','delta_Close','Candle','Close_1d_ch','Volume',
##         'Price_from_BBUP','Price_from_BBLWR','Price_from_BBMid','bol_wd',
##              'aroonup','aroondown','adx','STOCHRSI_fastk','ROC','macdhist', 'WilliamsR','CCI','direct' ,'HA','MOM', 'Close_1d_ch' ,'swng','Candle']]


##    print(" =========== Last section /running =========== ")
    gg33b['f']=''
    s3=str(gg33b['Datetime']).split(' ')
    for x in gg33b.index:
##        print(gg33b['5_10_crossovr'].loc[x])
##        print(str(gg33b['Datetime'].loc[x]).split(' '))
        gg33b['Datetime'].loc[x]=str(gg33b['Datetime'].loc[x]).split(' ')[0]
        f1=str(gg33b['Datetime'].loc[x]).split(' ')[0][5:10]
        f2=str(gg33b['Datetime'].loc[x]).split(' ')[1][0:5]
        f=str(f1)+'_'+str(f2)
        gg33b['f'].loc[x]=str(f1)+'_'+str(f2)
##        gg33b['Datetime'].loc[x]==str(f)
##        print(f)
##        print(f,'    ',gg33b['5_10_crossovr'].loc[x])
##        print(str(gg33b['Datetime'].loc[x]).split(' ')[1][0:5])
        
##    gg33=gg33[gg33['Datetime']=='2021-09-20']
##    print('\n','Close_delta_price_by_'+str(shiftbydays)+' days','\n',gg33b.tail(200))

##    gg33b=gg33b.set_index('Datetime')
##      tt.reset_index(inplace=True)
##    tt.set_index=('Datetime')
    
##    print(df.columns)
    

##    gg33b=gg33b.tail(90)
    
##    print('lllllll ----> ',gg33b)

    
    print('\n\n\n')
    print(' --------------------------- Glossary ----------------------------------')
    print('CCI:    CCI > 100 --> down   CCI < -100 ----> Up')
    print('RSI :   RSI between 70, 20. > 70 overbought, < 20 oversold')
    print('ULOST:  Buy signal ULOST < 30 , sell signal ULOS > 70')
    
    print('DX:     The DX is usually smoothed with a moving average (i.e. the ADX).The values range from 0 to 100, but rarely get above 60.To interpret the DX, consider a high number to be a strong trend, and a low number, a weak trend.')
    print('WilliamR: between -20 and -80. -20 is overbought/highs of its recent range, -80 is oversold/lower end of its recent range.')
    print('ADX :   Strength of trend, 0-25 -> Absent or Weak Trend,    25-50 --> Strong Trend, ? --> 50-75, 75-100-->Extremely Strong Trend')
    print('ATR :   ATR indicates increased volatility in the market')
    print(' ---------------------------End of Glossary ----------------------------------')

    
##    sys.exit()
###############################################################################
###############################################################################
####################### Signals 214 ##################################################
## ##################################################################################
    
    df=pd.DataFrame(gg33b)
    gg33b.reset_index(inplace=True,drop=False)


    import matplotlib.pyplot as plt
    from matplotlib import rc

## >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
####################### 5-10 crossover ###########################3
    gg33b['signal44']=''
    p8=[]

    for x in gg33b.index:  
        if gg33b['5_10_crossovr'].loc[x] > 0:
            if gg33b['5_10_crossovr'].shift(1).loc[x] < 0:
                p8.append(x)
    print('5_10_crossovr ---> ',p8)
    for x in gg33b.index:
        for y in p8:
            if x==y:
                gg33b.loc[x,'signal44']='buy_5_10'
##    print(gg33b)


####################### 5-10 crossover ###########################3
    p8=[]

    for x in gg33b.index:  
        if gg33b['5_10_crossovr'].loc[x] < 0:
            if gg33b['5_10_crossovr'].shift(1).loc[x] > 0:
                p8.append(x)
    print('5_10_crossovr ---> ',p8)
    for x in gg33b.index:
        for y in p8:
            if x==y:
                gg33b.loc[x,'signal44']='Sell_5_10'
##    print(gg33b)

##################################################################   
## >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
## >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#######################  10-21 crossover ###########################3
    gg33b['signal45']=''
    p8=[]

    for x in gg33b.index:  
        if gg33b['10_21_crossovr'].loc[x] > 0:
            if gg33b['10_21_crossovr'].shift(1).loc[x] < 0:
                p8.append(x)
    print('10_21_crossovr --> ',p8)
    for x in gg33b.index:
        for y in p8:
            if x==y:
                gg33b.loc[x,'signal45']='buy_10_21'
##    print(gg33b)


####################### 10-21 crossover ###########################3
    p8=[]

    for x in gg33b.index:  
        if gg33b['10_21_crossovr'].loc[x] < 0:
            if gg33b['10_21_crossovr'].shift(1).loc[x] > 0:
                p8.append(x)
    print('10_21_crossovr --> ',p8)
    for x in gg33b.index:
        for y in p8:
            if x==y:
                gg33b.loc[x,'signal45']='Sell_10_21'
##    print(gg33b)

##################################################################   
## >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
## >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#######################  '21_50_crossovr' ###########################3
    gg33b['signal46']=''
    p8=[]

    for x in gg33b.index:  
        if gg33b['21_50_crossovr'].loc[x] > 0:
            if gg33b['21_50_crossovr'].shift(1).loc[x] < 0:
                p8.append(x)
    print('21_50_crossovr --> ',p8)
    for x in gg33b.index:
        for y in p8:
            if x==y:
                gg33b.loc[x,'signal46']='buy_21_50'
##    print(gg33b)


####################### 21-50 crossover ###########################3
    p8=[]

    for x in gg33b.index:  
        if gg33b['21_50_crossovr'].loc[x] < 0:
            if gg33b['21_50_crossovr'].shift(1).loc[x] > 0:
                p8.append(x)
    print('21_50_crossovr --> ',p8)
    for x in gg33b.index:
        for y in p8:
            if x==y:
                gg33b.loc[x,'signal46']='Sell_21_50'
##    print(gg33b)

##################################################################   
## >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
## >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#######################  '50_100_crossovr' ###########################3
    gg33b['signal47']=''
    p8=[]

    for x in gg33b.index:  
        if gg33b['50_100_crossovr'].loc[x] > 0:
            if gg33b['50_100_crossovr'].shift(1).loc[x] < 0:
                p8.append(x)
    print('50_100_crossovr --> ',p8)
    for x in gg33b.index:
        for y in p8:
            if x==y:
                gg33b.loc[x,'signal47']='buy_50_100'
##    print(gg33b)


####################### '50_100_crossovr' ###########################3
    p8=[]

    for x in gg33b.index:  
        if gg33b['50_100_crossovr'].loc[x] < 0:
            if gg33b['50_100_crossovr'].shift(1).loc[x] > 0:
                p8.append(x)
    print('500_100_crossovr --> ',p8)
    for x in gg33b.index:
        for y in p8:
            if x==y:
                gg33b.loc[x,'signal47']='Sell_50_100'
##    print(gg33b)

##################################################################
    ## >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#######################  '100_200_crossovr' ###########################3
    gg33b['signal48']=''
    p8=[]

    for x in gg33b.index:  
        if gg33b['100_200_crossovr'].loc[x] > 0:
            if gg33b['100_200_crossovr'].shift(1).loc[x] < 0:
                p8.append(x)
    print('100_200_crossovr --> ',p8)
    for x in gg33b.index:
        for y in p8:
            if x==y:
                gg33b.loc[x,'signal48']='buy_100_200'
##    print(gg33b)


####################### '100_200_crossovr' ###########################3
    p8=[]

    for x in gg33b.index:  
        if gg33b['100_200_crossovr'].loc[x] < 0:
            if gg33b['100_200_crossovr'].shift(1).loc[x] > 0:
                p8.append(x)
    print('100_200_crossovr --> ',p8)
    for x in gg33b.index:
        for y in p8:
            if x==y:
                gg33b.loc[x,'signal48']='Sell_100_200'
    print(gg33b)




    
days()
print("script ran was ******************     stocks_Technicals56_with_signals22_v2.py    ")
