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

##print('100% confirm---stoch/fastd is 100. Stock will be green, if 0 meaning stock will be red')

def days():

    
    perda='635d'
    intervla='1d'
    yy=str(intervla).split('d')[0]
    shiftbydays=3



    ##    g=input("Entr_Signal ticker: ")
    perd=perda
    intervl=intervla
##    ticker='BTC-USD'
##    ticker='^NDX'
##    ticker='MSTR'
##    ticker='MRNA'
##    ticker='AMZN'
##    ticker='TSLA'
    ticker='DOCU'
    # [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]

    

    #df=pd.DataFrame()
    #Interval required 5 minutes
    df = yf.download(ticker, period=perd, interval=intervl,prepost = True)
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
    
##    df['day']=Date.Date(df['Date'])
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
    df['Price_3_crossovr']=''
    df['upward_pressure']=''
    df['downward_pressure']=''
    df['Closev']=''
    df['3_5_crossovr_c']=''
    
    
##    
##
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
    ##    df2['d']=df2['Date'].dt.day_name()
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
        df['Price_3_crossovr'].loc[x]=df['Close'].loc[x]-df['EMA_3s'].loc[x]
##        df['3_5_crossovr_c'].loc[x]=df['EMA_3'].loc[x]

    ############################ end of ha



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
                  df['3_5_crossovr_c']

                  ],axis=1)


    tt.reset_index(inplace=True)
    tt.set_index=('Date')
##    print('tt-columns:',tt.columns)
##    print('tt length:', len(tt.columns))
    tt.reset_index(inplace=True)        
    for x in tt.index:
    ##    print(tt['Volume'])
    ##    tt['Volume'].loc[x]=numerize.numerize(tt['Volume'].loc[x])
    ##    tt['Volume'].loc[x]=numerize.numerize((tt['Volume'].iloc[x][1]))
        tt['Volume'].loc[x]=numerize.numerize(np.float32(tt['Volume'].loc[x]).item())



##    print('kkkk')
##    print(tt.columns.get_loc("ATR"))
##    print(tt['Close_d'])
##    print(tt.columns.get_loc("EMA_3"))


##    print(tt.shape[1])
##    print(tt.iloc[:0,:])


    print(tt.columns)
    gg33=tt[['index', 'Date','ticker', 'pivot','pivotx','pp','*','Close_1d_ch','*','r1','r2','r3','*','s1','s2','s3','*','volatility','*',
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
              ,'upward_pressure','downward_pressure','Closev','3_5_crossovr_c'
             
            

             ]]


# if STOCHRSI_fastk=100, stock will be green.
    gg33=gg33[np.float64(gg33['STOCHRSI_fastk']) == 100]
    print('STOCHRSI_fastk=100 ----> ',gg33)


# if aroonup=100, stock will be green.
    gg33=gg33[np.float64(gg33['aroonup']) == 100]
    print('aroonup=100 ----> ',gg33)
    
# if aroonup=0, stock will be red.
    gg33=gg33[np.float64(gg33['aroonup']) == 0]
    print('aroonup=0 ----> ',gg33)


# if macdhist > 0, stock will be Green.
    gg33=gg33[np.float64(gg33['macdhist']) > 0]
    print('macdhist > 0 ----> ',gg33)

# if macdhist < 0, stock will be Red.
    gg33=gg33[np.float64(gg33['macdhist']) < 0]
    print('macdhist < 0 ----> ',gg33)

# if ROC > 0, stock will be Green.
    gg33=gg33[np.float64(gg33['ROC']) > 0]
    print('macdhist > 0 ----> ',gg33)

# if ROC < 0, stock will be Red.
    gg33=gg33[np.float64(gg33['ROC']) < 0]
    print('macdhist < 0 ----> ',gg33)    




    print('\n')
    print('*************************************************************************************************************')
    print('\n')
    gg33b=tt[['index', 'Date','ticker', 'pivot','pivotx','pp','*','Close_1d_ch','Candle', 'MOM', 'swng','direct', 'HA','Volume','*','*',
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
          '3_5_crossovr','5_10_crossovr','10_21_crossovr','21_50_crossovr','50_100_crossovr','Price_3_crossovr'
           ,'upward_pressure','downward_pressure','Closev','3_5_crossovr_c'
        

         ]]
    gg33b=tt[['index', 'Date','ticker', 'pivot','pivotx','pp','*','Close_1d_ch','Candle', 'MOM', 'swng','direct', 'HA', 'EMA_3','EMA_5', 'EMA_10', 'EMA_21', 'EMA_50', 'EMA_100', 'EMA_200','CCI','DX', 'WILLR', 'RSI', 'adx', 'WilliamsR', 'ATR', 'ULTOSC', 'ROC','PLUS_DI', 'PLUS_DM', 'HT_DCPERIOD', 'HT_DCPHASE', 'sine',
         'leadsine','aroondown', 'aroonup',  'macdhist', 'PLUS_DI','PLUS_DM', 'PPO', 'ROC', 'ROCP', 'ROCR', 'ROCR100', '*','*','STOCHRSI_fastk',
               'Buy_5EMA_10EMA','Buy_5EMA_21EMA','Buy_21EMA_50EMA','Buy_50EMA_100EMA','Buy_100EMA_200EMA',
         'adx','aroondown','aroonup','AROONOSC','SAR','SAREXT',
         'delta_Low','delta_High','delta_Open','delta_Close','Candle','Close_1d_ch','Volume',
         'Price_from_BBUP','Price_from_BBLWR','Price_from_BBMid','bol_wd','Close_1d_ch',
          'Price_3_crossovr',    
          '3_5_crossovr','5_10_crossovr','10_21_crossovr','21_50_crossovr','50_100_crossovr',
          'Close','EMA_3s','EMA_5s', 'EMA_10s', 'EMA_21s', 'EMA_50s', 'EMA_100s', 'EMA_200s'
           ,'upward_pressure','downward_pressure' ,'Closev','3_5_crossovr_c'

         ]]

    s3=str(gg33b['Date']).split(' ')
    for x in gg33b.index:
##        print(str(gg33b['Date'].loc[x]).split(' '))
        gg33b['Date'].loc[x]=str(gg33b['Date'].loc[x]).split(' ')[0]
##    gg33=gg33[gg33['Date']=='2021-09-20']
    print('\n','Close_delta_price_by_'+str(shiftbydays)+' days','\n',gg33b.tail(200))

    gg33b=gg33b.set_index('Date')
##      tt.reset_index(inplace=True)
##    tt.set_index=('Datetime')
    
##    print(df.columns)
    

    gg33b=gg33b.tail(90)
    
    print('lllllll ----> ',gg33b)

    
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

############################3
    
####################################################################################
####################### Signals 214 ##################################################
## ##################################################################################
    
    df=pd.DataFrame(gg33b)
    gg33b.reset_index(inplace=True,drop=False)

##    print('pppppp  ',gg33b)
##
##    for x in gg33b.columns:
##        print(x,'     ',gg33b[x],'   ',type(gg33b[x]))
##    
####    sys.exit()
    
##    gg33b.index=gg33b.index.split(' ')[0]
    print(gg33b)
    import matplotlib.pyplot as plt
    from matplotlib import rc
##    plt.axvline(x='2021-10-12', color='k', linewidth=1.0, linestyle='--')
##    plt.axvline(x='2021-04-15', color='r', linewidth=1.0, linestyle='--')
##    plt.axvline(x='2021-08-15', color='r', linewidth=1.0, linestyle='--')
##    axvline(x='2021-10-12', ymin=0, ymax=8998.75)
##    plt.rc('text', usetex=True)
##    plt.rc('font', family='serif')
##    plt.plot('2021-10-12', label='MF Spin-UP', linestyle=':',color='r')


####################### 5-10 crossover ###########################3
    pp44=[]
    for x in range(gg33b.shape[0]):
##        print(gg33b['5_10_crossovr'].loc[x])
        if gg33b['5_10_crossovr'].loc[x] < 0 and gg33b['5_10_crossovr'].shift(1).loc[x] > 0:
            pp44.append(gg33b['Date'].loc[x])
    pp45=[]
    for x in range(gg33b.shape[0]):
##        print(gg33b['5_10_crossovr'].loc[x])
        if gg33b['5_10_crossovr'].loc[x] > 0 and gg33b['5_10_crossovr'].shift(1).loc[x] < 0:
            pp45.append(gg33b['Date'].loc[x])
##################################################################
####################### 10-21 crossover ###########################3
    pp46=[]
    for x in range(gg33b.shape[0]):
##        print(gg33b['10_21_crossovr'].loc[x])
        if gg33b['10_21_crossovr'].loc[x] < 0 and gg33b['10_21_crossovr'].shift(1).loc[x] > 0:
            pp46.append(gg33b['Date'].loc[x])
    pp47=[]
    for x in range(gg33b.shape[0]):
##        print(gg33b['5_10_crossovr'].loc[x])
        if gg33b['10_21_crossovr'].loc[x] > 0 and gg33b['10_21_crossovr'].shift(1).loc[x] < 0:
            pp47.append(gg33b['Date'].loc[x])
##################################################################    
####################### '21_50_crossovr' ###########################3
    pp48=[]
    for x in range(gg33b.shape[0]):
##        print(gg33b['10_21_crossovr'].loc[x])
        if gg33b['21_50_crossovr'].loc[x] < 0 and gg33b['21_50_crossovr'].shift(1).loc[x] > 0:
            pp46.append(gg33b['Date'].loc[x])
    pp49=[]
    for x in range(gg33b.shape[0]):
##        print(gg33b['5_10_crossovr'].loc[x])
        if gg33b['21_50_crossovr'].loc[x] > 0 and gg33b['21_50_crossovr'].shift(1).loc[x] < 0:
            pp47.append(gg33b['Date'].loc[x])
################################################################## 
####################### '50_100_crossovr'###########################3
    pp50=[]
    for x in range(gg33b.shape[0]):
##        print(gg33b['10_21_crossovr'].loc[x])
        if gg33b['50_100_crossovr'].loc[x] < 0 and gg33b['50_100_crossovr'].shift(1).loc[x] > 0:
            pp46.append(gg33b['Date'].loc[x])
    pp51=[]
    for x in range(gg33b.shape[0]):
##        print(gg33b['5_10_crossovr'].loc[x])
        if gg33b['50_100_crossovr'].loc[x] > 0 and gg33b['50_100_crossovr'].shift(1).loc[x] < 0:
            pp47.append(gg33b['Date'].loc[x])
################################################################## 





            
    gg33b.set_index('Date',inplace=True)

##    k=0 '50_100_crossovr'
##    for x in pp44:
##        print(k,'  ',str(x).split(' ')[1])
##        k=k+1

##    for xc in pp44:
##        print(xc)
##        plt.axvline(x=xc, color='k', linewidth=1.0, linestyle='--')
    
##            
####            print(gg33b['3_5_crossovr'].loc[x])
##            p44.append(gg33b['3_5_crossovr'].loc[x])
##        
####        print(gg33b['3_5_crossovr'].loc[x])
##
##    print('oooooo ',p44) '21_50_crossovr'

#########################5-10 crossover#######################################
    for xc in pp44:
        plt.axvline(x=xc, color='r', linewidth=0.5, linestyle='--',label='5-10x-dwn')
##        plt.vlines(x = xc, ymin = 0, ymax = 40000, 
##           colors = 'purple', 
##           label = 'vline_multiple - full height') 
        print(xc)

    for xc in pp45:
        plt.axvline(x=xc, color='g', linewidth=0.5, linestyle='--',label='5-10x-up')
        print(xc)
#################################################################
##########################10-21 crossover######################################
    for xc in pp46:
        plt.axvline(x=xc, color='r', linewidth=1.0, linestyle='--',label='10-21x-dwn')
        print(xc)

    for xc in pp47:
        plt.axvline(x=xc, color='g', linewidth=1.0, linestyle='--',label='10-21x-up')
        print(xc)
#################################################################
##########################'21_50_crossovr'######################################
    for xc in pp48:
        plt.axvline(x=xc, color='r', linewidth=2.0, linestyle='--',label='21_50x-dwn')
        print(xc)

    for xc in pp49:
        plt.axvline(x=xc, color='g', linewidth=2.0, linestyle='--',label='21_50x-up')
        print(xc)
#################################################################
##########################'50_100_crossovr'######################################
    for xc in pp50:
        plt.axvline(x=xc, color='r', linewidth=3.0, linestyle='--',label='50_100x-dwn')
        print(xc)

    for xc in pp51:
        plt.axvline(x=xc, color='g', linewidth=3.0, linestyle='--',label='50_100x-up')
        print(xc)
################################################################# 

        
####        if df['3_5_crossovr_c'].loc[x]==1:'50_100_crossovr'
####        plt.axvline(x=xc, color='g')


##    print(pp44)    

        
    
##    print('kkkkkkkkkkkkkkkkkkkkk    ', gg33b['3_5_crossovr'].loc[x])

##    if gg33b['3_5_crossovr'].loc[x] < 0:
####            gg33b['3_5_crossovr_c'].loc[x]==1
####            pp44.append(df['3_5_crossovr_c'].loc[x])print("toystory-----> ",pp44)
##        pp44.append[x]
####    if gg33b['3_5_crossovr'].shift(1).loc[x] < 0 and gg33b['3_5_crossovr'].loc[x] > 0:
####        gg33b['3_5_crossovr_c'].loc[x]==2
####            pp44.append(df['3_5_crossovr_c'].loc[x])
##        pp44.append(x)
####################################################################################
    
##    plt.xticks(df['Date'],values)
##    plt.xticks(np.arange(min(df['Date']), max(df['Date'])+1, 1.0))
      
    
    plt.grid(True)
##    fig, (ax1, ax2) = plt.subplots(2)
##    fig.suptitle('kaku33' + ticker + '  Daily')
##    plt.xlabel('Dates')
##    plt.ylabel(ticker+' Close Prices')
##    plt.plot(gg33b[['Price_3_crossovr','aroonup']])
# https://www.tug.org/pracjourn/2007-4/walden/color.pdf
##    plt.legend(loc='best')
    plt.title('kaku99 '+ticker + '  Daily')
##plt.axhline(14000, color='g', linestyle='-', label='75-100 - Extremely Strong Trend',linewidth=1)
    
####    plt.text(14000,'Extremely',rotation=0)
##    plt.text(3, 8, 'boxed italics text in data coords', style='italic',
##        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

    
    plt.plot(gg33b['EMA_3s'], color ="blue", label = 'EMA_3',linewidth=1)
    plt.plot(gg33b['EMA_5s'], color ="green", label = 'EMA_5',linewidth=1)
    plt.plot(gg33b['EMA_10s'], color ="cyan", label = 'EMA_10',linewidth=1)
    plt.plot(gg33b['EMA_21s'], color ="yellow", label = 'EMA_21',linewidth=1)
    plt.plot(gg33b['EMA_50s'], color=(1.0,0.2,0.3), label = 'EMA_50',linewidth=1.2, linestyle = '--')
    plt.plot(gg33b['EMA_100s'], color='C0', label = 'EMA_100',linewidth=1, linestyle = '--')
    plt.plot(gg33b['EMA_200s'], color='C4', label = 'EMA_200',linewidth=1, linestyle = '--')
    plt.plot(gg33b['Close'], color="black", label = 'Close',linewidth=3)


##    xposition = [0.3, 0.4, 0.45]
##    for xc in xposition:
##        plt.axvline(x=xc, color='k', linestyle='--')

##    pp44  214



##    
##    print("toystory-----> ",pp44)
##    for xc in pp44:
####        if df['3_5_crossovr_c'].loc[x]==1:
##        plt.axvline(x=xc, color='g')
##            
        
##
##    plt.plot(gg33b['aroonup'], color=(0,0.2,0.4), label = 'aroonup',linewidth=1)
##    plt.plot(gg33b['aroondown'], color=(0,0.5,0.1), label = 'aroondown',linewidth=1)
##    plt.plot(gg33b['macdhist'], color=(1.0,0.2,0.3), label = 'macdhist',linewidth=1)
##    plt.plot(gg33b['ROC'], color=(0.5,0.0,0.6), label = 'ROC',linewidth=1)
##    plt.plot(gg33b['STOCHRSI_fastk'], color=(0.4,0.9,0.3), label = 'STOCHRSI_fastk',linewidth=1)
##    plt.plot(gg33b['CCI'], color=(0.4,0.7,0.9), label = 'CCI',linewidth=1)
##    plt.plot(gg33b['RSI'], color=(0.7,0.9,0), label = 'RSI',linewidth=1)
##    plt.plot(gg33b['ULTOSC'], color=(0.8,0.0,0.8), label = 'ULTOSC',linewidth=1)
##    plt.xticks(fontsize= 7)
##    plt.yticks(fontsize= 7)
##    plt.legend(fontsize=6)

##    ax1.plot(y=gg33b['EMA_3s'],color ="blue", label = 'EMA_3',linewidth=1)
##    ax2.plot(y=gg33b['EMA_5s'],color ="blue", label = 'EMA_3',linewidth=1)

    
##    plt.plot(gg33b['EMA_3s'], color ="blue", label = 'EMA_3',linewidth=1)
##    plt.plot(gg33b['EMA_5s'], color ="green", label = 'EMA_5',linewidth=1)
##    plt.plot(gg33b['EMA_10s'], color ="cyan", label = 'EMA_10',linewidth=1)
##    plt.plot(gg33b['EMA_21s'], color ="yellow", label = 'EMA_21',linewidth=1)
##    plt.plot(gg33b['EMA_50s'], color=(1.0,0.2,0.3), label = 'EMA_50',linewidth=1.2, linestyle = '--')
##    plt.plot(gg33b['EMA_100s'], color='C0', label = 'EMA_100',linewidth=1, linestyle = '--')
##    plt.plot(gg33b['EMA_200s'], color='C4', label = 'EMA_200',linewidth=1, linestyle = '--')
##    plt.plot(gg33b['Close'], color="black", label = 'Close',linewidth=3)
##
##    plt.plot(gg33b['aroonup'], color=(0,0.2,0.4), label = 'aroonup',linewidth=1)
##    plt.plot(gg33b['aroondown'], color=(0,0.5,0.1), label = 'aroondown',linewidth=1)
##    plt.plot(gg33b['macdhist'], color=(1.0,0.2,0.3), label = 'macdhist',linewidth=1)
##    plt.plot(gg33b['ROC'], color=(0.5,0.0,0.6), label = 'ROC',linewidth=1)
##    plt.plot(gg33b['STOCHRSI_fastk'], color=(0.4,0.9,0.3), label = 'STOCHRSI_fastk',linewidth=1)
##    plt.plot(gg33b['CCI'], color=(0.4,0.7,0.9), label = 'CCI',linewidth=1)
##    plt.plot(gg33b['RSI'], color=(0.7,0.9,0), label = 'RSI',linewidth=1)
##    plt.plot(gg33b['ULTOSC'], color=(0.8,0.0,0.8), label = 'ULTOSC',linewidth=1)
    plt.xticks(fontsize= 7)
    plt.yticks(fontsize= 7)
    plt.legend(fontsize=6)


##########################################################################################
##    plt.grid(True)
##    plt.title('kaku34 new one special ' + ticker + '  Daily2')
####plt.axhline(14000, color='g', linestyle='-', label='75-100 - Extremely Strong Trend',linewidth=1)
##    
######    plt.text(14000,'Extremely',rotation=0)
####    plt.text(3, 8, 'boxed italics text in data coords', style='italic',
####        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
##
##    plt.plot(gg33b['aroonup'], color=(0,0.2,0.4), label = 'aroonup',linewidth=2)
####    plt.plot(gg33b['aroondown'], color=(0,0.5,0.1), label = 'aroondown',linewidth=1)
##    plt.plot(gg33b['macdhist'], color=(1.0,0.2,0.3), label = 'macdhist',linewidth=2)
##    plt.plot(gg33b['ROC']*10, color=(0.5,0.0,0.6), label = 'ROC',linewidth=1)
##    plt.plot(gg33b['STOCHRSI_fastk'], color=(0.4,0.9,0.3), label = 'STOCHRSI_fastk',linewidth=1)
##    plt.plot(gg33b['CCI'],color=(0.5,0.3,0.3), label = 'CCI',linewidth=2)
##    plt.plot(gg33b['RSI'], color=(0.7,0.9,0), label = 'RSI',linewidth=3)
##    plt.plot(gg33b['ULTOSC'], color=(0.5,0.0,0.7), label = 'ULTOSC',linewidth=1)
####    plt2.plot(gg33b['Closev']*100, color="green",linewidth=3,label = 'Closev')
##    plt.xticks(fontsize= 7)
##    plt.yticks(fontsize= 7)
##    plt.legend(fontsize=6)
##    plt.show()

##########################################################################################
    

##    plt.axhline(14000, color='g', linestyle='-', label='75-100 - Extremely Strong Trend',linewidth=1)
##    plt.text(14000,'Extremely',rotation=0)
##    plt.text(14000, 'boxed italics text in data coords', style='italic')
##    plt.text(0, 14500, 'kk',fontsize=8)
##    plt.text(2021-03,14000,"Some text")
##    plt.annotate('pixel offset from axes fraction',
##            xy=(2019-7-4, 14000), xycoords='axes fraction',
##            xytext=(2019-7-4, 14000), textcoords='offset pixels',
##            horizontalalignment='right',
##            verticalalignment='bottom')
##    ax.annotate('pixel offset from axes fraction',
##            xy=(1, 0), xycoords='axes fraction',
##            xytext=(-20, 20), textcoords='offset pixels',
##            horizontalalignment='right',
##            verticalalignment='bottom'
##                                                   )

    
##    plt.legend(fontsize=6)
##    plt.xticks(rotation=90,fontsize= 5)
##    plt.grid(True)
##    plt.show()
##    plt.grid(True,axis='both')
##    plt.axis([0, 1800, 20000,2200])
# This gives an interval of 200



##SMALL_SIZE = 8
##MEDIUM_SIZE = 10
##BIGGER_SIZE = 12
##
##plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
##plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
##plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
##plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
##plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
##plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
##plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

###########################################################################################
##    fig, axs = plt.subplots(11, 2,sharex=True, sharey=False)
    fig, axs = plt.subplots(11, 2)
##    fig, axs =plt.subplot(112)
##    fig, axs =plt.subplot(11,2,sharex=True, sharey=False,autoscaley_on=True)

###########################################################################################   
    
##    counts, bins = np.histogram(gg33b['aroonup'])
##    plt.hist(bins[:-1], bins, weights=counts)
##    axs[0,0].hist(gg33b['aroonup'])

##f ,ax = plt.subplots(1,2,figsize = (30, 13),gridspec_kw={'width_ratios': [5, 1]})


##    bins = np.arange(gg33b.shape[0])

##    axs[0, 0].hist(gg33b['aroonup'],gg33b.shape[0], facecolor='blue',edgecolor='black')

##    axs[0, 1].hist(gg33b['aroonup'], bins = gg33b.index)

    axs[0, 0].plot(gg33b[['aroonup','macdhist']], 'tab:blue',linewidth=.5,label = 'aroonup')
    axs[0,0].set_ylabel('aroonup', fontsize=7)
    for tick in axs[0, 0].xaxis.get_major_ticks():
        tick.label.set_fontsize(6)
        tick.label.set_rotation('vertical')
    for tick in axs[0, 0].yaxis.get_major_ticks():
        tick.label.set_fontsize(6)    
    axs[0, 0].set_title('aroonup', fontsize=7)    

    
    axs[0, 1].plot(gg33b['aroondown'], 'tab:orange',linewidth=.5,label = 'aroondown')
    axs[0,1].set_ylabel('aroondown', fontsize=7)
    axs[0,1].set_title('aroondown', fontsize=7)
    for tick in axs[0, 1].xaxis.get_major_ticks():
        tick.label.set_fontsize(6)
        tick.label.set_rotation('vertical')
    for tick in axs[0, 1].yaxis.get_major_ticks():
        tick.label.set_fontsize(6)        
    axs[0, 1].set_title('aroondown', fontsize=7  )

##################################    
    axs[2, 0].plot(gg33b['macdhist'], 'tab:green', linewidth=.5,label = 'macdhist')
    axs[2,0].set_ylabel('macdhist', fontsize=7)
    axs[2,0].set_title('macdhist', fontsize=7)
    for tick in axs[2, 0].xaxis.get_major_ticks():
        tick.label.set_fontsize(6)
        tick.label.set_rotation('vertical')
    for tick in axs[2, 0].yaxis.get_major_ticks():
        tick.label.set_fontsize(6)       
    axs[2, 0].set_title('macdhist', fontsize=7)
    axs[2, 0].axhline(y=0, color='r', linestyle='-', label='50-75 Very Strong Trend',linewidth=1)
    
    axs[2, 1].plot(gg33b['ROC'], 'tab:red', label = 'ROC',linewidth=.5)
    axs[2,1].set_ylabel('ROC', fontsize=7)
    axs[2,1].set_title('ROC', fontsize=7)
    for tick in axs[2, 1].xaxis.get_major_ticks():
        tick.label.set_fontsize(6)
        tick.label.set_rotation('vertical')
    for tick in axs[2, 1].yaxis.get_major_ticks():
        tick.label.set_fontsize(6)       
    axs[2, 1].set_title('ROC', fontsize=7)


################################## 

    axs[3, 0].plot(gg33b['adx'], 'tab:blue', label = 'adx',linewidth=1)
    axs[3,0].set_ylabel('adx', fontsize=7)
    axs[3,0].set_title('adx', fontsize=7)
    axs[3, 0].axhline(y=75, color='r', linestyle='-', label='75-100 - Extremely Strong Trend',linewidth=1)
##    axs[3, 0].text(y=75,x=0,'Extremely Strong Trend',rotation=0)
    axs[3, 0].axhline(y=50, color='g', linestyle='-', label='50-75 Very Strong Trend',linewidth=1)
    axs[3, 0].axhline(y=25, color='b', linestyle='-', label='25-50 Strong Trend',linewidth=1)
    axs[3, 0].axhline(y=0, color ='y', linestyle='-', label='0-25 Absent or Weak Trend',linewidth=1)
    
    for tick in axs[3, 0].xaxis.get_major_ticks():
        tick.label.set_fontsize(6)
        tick.label.set_rotation('vertical')
    for tick in axs[3, 0].yaxis.get_major_ticks():
        tick.label.set_fontsize(6)       
    axs[3, 0].set_title('adx', fontsize=7)
    

    axs[3, 1].plot(gg33b['ULTOSC'], 'tab:red', label = 'ULTOSC',linewidth=.5)
    axs[3,1].set_ylabel('ULTOSC', fontsize=7)
    axs[3,1].set_title('ULTOSC', fontsize=7)
    for tick in axs[3, 1].xaxis.get_major_ticks():
        tick.label.set_fontsize(6)
        tick.label.set_rotation('vertical')
    for tick in axs[3, 1].yaxis.get_major_ticks():
        tick.label.set_fontsize(6)       
    axs[3, 1].set_title('ULTOSC (buy <30, sell >70', fontsize=7)
    axs[3, 1].axhline(y=30, color='r', linestyle='-', label='50-75 Very Strong Trend',linewidth=1)
    axs[3, 1].axhline(y=70, color='g', linestyle='-', label='25-50 Strong Trend',linewidth=1)


################################## 

    axs[4, 0].plot(gg33b['ATR'], 'tab:red', label = 'ATR',linewidth=.5)
    axs[4,0].set_ylabel('ATR', fontsize=7)
    axs[4,0].set_title('ATR', fontsize=7)
    for tick in axs[4, 0].xaxis.get_major_ticks():
        tick.label.set_fontsize(6)
        tick.label.set_rotation('vertical')
    for tick in axs[4, 0].yaxis.get_major_ticks():
        tick.label.set_fontsize(6)       
    axs[4, 0].set_title('ATR', fontsize=7)


    axs[4, 1].plot(gg33b['CCI'], 'tab:red', label = 'CCI',linewidth=.5)
    axs[4,1].set_ylabel('CCI', fontsize=7)
    for tick in axs[4, 1].xaxis.get_major_ticks():
        tick.label.set_fontsize(6)
        tick.label.set_rotation('vertical')
    for tick in axs[4, 1].yaxis.get_major_ticks():
        tick.label.set_fontsize(6)       
    axs[4, 1].set_title('CCI', fontsize=7)
    axs[4, 1].axhline(y=100, color='r', linestyle='-', label='25-50 Strong Trend',linewidth=1)
    axs[4, 1].axhline(y=-100, color='g', linestyle='-', label='0-25 Absent or Weak Trend',linewidth=1)
    


################################## 

    axs[5, 0].plot(gg33b['RSI'], 'tab:red', label = 'RSI',linewidth=.5)
    axs[5,0].set_ylabel('RSI', fontsize=7)
    for tick in axs[5, 0].xaxis.get_major_ticks():
        tick.label.set_fontsize(6)
        tick.label.set_rotation('vertical')
    for tick in axs[5, 0].yaxis.get_major_ticks():
        tick.label.set_fontsize(6)       
    axs[5, 0].set_title('RSI', fontsize=7)
    axs[5, 0].axhline(y=70, color='r', linestyle='-', label='70 - sell',linewidth=1)
    axs[5, 0].axhline(y=50, color='r', linestyle='-', label='30 - buy',linewidth=1)

    axs[5, 1].plot(gg33b['WilliamsR'], 'tab:red', label = 'WilliamsR',linewidth=.5)
    axs[5,1].set_ylabel('WilliamsR', fontsize=7)                    
    for tick in axs[5, 1].xaxis.get_major_ticks():
        tick.label.set_fontsize(6)
        tick.label.set_rotation('vertical')
    for tick in axs[5, 1].yaxis.get_major_ticks():
        tick.label.set_fontsize(6)       
    axs[5, 1].set_title('WilliamsR', fontsize=7)
    axs[5, 1].axhline(y=-20, color='r', linestyle='-', label='70 - sell',linewidth=1)
    axs[5, 1].axhline(y=-80, color='g', linestyle='-', label='30 - buy',linewidth=1)

################################## 
    axs[6, 0].plot(gg33b['Candle'], 'tab:red', label = 'Candle',linewidth=.5)
    axs[6,0].set_ylabel('Candle', fontsize=7)
    for tick in axs[6, 0].xaxis.get_major_ticks():
        tick.label.set_fontsize(6)
        tick.label.set_rotation('vertical')
    for tick in axs[6, 0].yaxis.get_major_ticks():
        tick.label.set_fontsize(6)       
    axs[6, 0].set_title('Candle', fontsize=7)

    axs[6, 1].plot(gg33b['MOM'], 'tab:blue', label = 'MOM',linewidth=.5)
    axs[6,1].set_ylabel('MOM', fontsize=7)
    for tick in axs[6, 1].xaxis.get_major_ticks():
        tick.label.set_fontsize(6)
        tick.label.set_rotation('vertical')
    for tick in axs[6, 1].yaxis.get_major_ticks():
        tick.label.set_fontsize(6)       
##    axs[6, 1].set_title('MOM', fontsize=7,horizontalalignment='left', verticalalignment='bottom')

    axs[6, 1].set_title('MOM', fontsize=7, loc='right')
    axs[6, 1].axhline(y=0, color='r', linestyle='-', label='70 - sell',linewidth=1)

################################## 

##    axs[7, 0].plot(gg33b['Close_1d_ch'], 'tab:red', label = 'Close_1d_ch',linewidth=.5)
##    axs[7,0].set_ylabel('Close_1d_ch', fontsize=7)
##    for tick in axs[7, 0].xaxis.get_major_ticks():
##        tick.label.set_fontsize(6)
##        tick.label.set_rotation('vertical')
##    for tick in axs[7, 0].yaxis.get_major_ticks():
##        tick.label.set_fontsize(6)       
##    axs[7, 0].set_title('Close_1d_ch', fontsize=7)

    axs[7, 0].plot(gg33b['Close'],  'tab:blue', label = 'Close',linewidth=1)
    axs[7,0].set_ylabel('Close', fontsize=7)
    for tick in axs[7, 0].xaxis.get_major_ticks():
        tick.label.set_fontsize(6)
        tick.label.set_rotation('vertical')
    for tick in axs[7, 0].yaxis.get_major_ticks():
        tick.label.set_fontsize(6)       
    axs[7, 0].set_title('Close', fontsize=7)

    axs[7, 1].plot(gg33b['Close'],  'tab:blue', label = 'Close',linewidth=1)
    axs[7,1].set_ylabel('Close', fontsize=7)
    for tick in axs[7, 1].xaxis.get_major_ticks():
        tick.label.set_fontsize(6)
        tick.label.set_rotation('vertical')
    for tick in axs[7, 1].yaxis.get_major_ticks():
        tick.label.set_fontsize(6)       
    axs[7, 1].set_title('Close', fontsize=7)


################################## 

    axs[8, 0].plot(gg33b['STOCHRSI_fastk'], 'tab:red', label = 'STOCHRSI_fastk',linewidth=.5)
    axs[8,0].set_ylabel('STOCHRSI_fastk', fontsize=7)
    for tick in axs[8, 0].xaxis.get_major_ticks():
        tick.label.set_fontsize(6)
        tick.label.set_rotation('vertical')
    for tick in axs[8, 0].yaxis.get_major_ticks():
        tick.label.set_fontsize(6)       
    axs[8, 0].set_title('STOCHRSI_fastk', fontsize=7)
    axs[8, 0].axhline(y=100, color='g', linestyle='-', label='0-25 Absent or Weak Trend',linewidth=1)
    axs[8, 0].axhline(y=0, color='r', linestyle='-', label='0-25 Absent or Weak Trend',linewidth=1)

    axs[8, 1].plot(gg33b['PLUS_DM'], 'tab:red', label = 'PLUS_DM',linewidth=.5)
    axs[8,1].set_ylabel('PLUS_DM', fontsize=7)
    for tick in axs[8, 1].xaxis.get_major_ticks():
        tick.label.set_fontsize(6)
        tick.label.set_rotation('vertical')
    for tick in axs[8, 1].yaxis.get_major_ticks():
        tick.label.set_fontsize(6)       
    axs[8, 1].set_title('PLUS_DM', fontsize=7)  


################################## 


    axs[9, 0].plot(gg33b['PLUS_DI'], 'tab:red', label = 'PLUS_DI',linewidth=.5)
    axs[9,0].set_ylabel('PLUS_DI', fontsize=7)
    for tick in axs[9, 0].xaxis.get_major_ticks():
        tick.label.set_fontsize(6)
        tick.label.set_rotation('vertical')
    for tick in axs[9, 0].yaxis.get_major_ticks():
        tick.label.set_fontsize(6)       
    axs[9, 0].set_title('PLUS_DI', fontsize=7)

    axs[9, 1].plot(gg33b['HA'], 'tab:red', label = 'HA',linewidth=.5)
    axs[9,1].set_ylabel('HA', fontsize=7)
    for tick in axs[9, 1].xaxis.get_major_ticks():
        tick.label.set_fontsize(6)
        tick.label.set_rotation('vertical')
    for tick in axs[9, 1].yaxis.get_major_ticks():
        tick.label.set_fontsize(6)       
    axs[9, 1].set_title('HA', fontsize=7)

##################################

    axs[10, 0].plot(gg33b['upward_pressure'], 'tab:red', label ='upward_pressure',linewidth=.5)
    axs[10,0].set_ylabel('upward_pressure', fontsize=7)
    for tick in axs[10, 0].xaxis.get_major_ticks():
        tick.label.set_fontsize(6)
        tick.label.set_rotation('vertical')
    for tick in axs[10, 0].yaxis.get_major_ticks():
        tick.label.set_fontsize(6)       
    axs[10, 0].set_title('upward_pressure (above zero)', fontsize=7)
    axs[10, 0].axhline(y=10, color='g', linestyle='-', label='70 - sell',linewidth=2)

    axs[10, 1].plot(gg33b['downward_pressure'], 'tab:red', label = 'downward_pressure',linewidth=.5)
    axs[10,1].set_ylabel('downward_pressure', fontsize=7)
    for tick in axs[10, 1].xaxis.get_major_ticks():
        tick.label.set_fontsize(6)
        tick.label.set_rotation('vertical')
    for tick in axs[10, 1].yaxis.get_major_ticks():
        tick.label.set_fontsize(6)       
    axs[10, 1].set_title('downward_pressure (above zero)', fontsize=7)
    axs[10, 1].axhline(y=10, color='g', linestyle='-', label='70 - sell',linewidth=2)


##################################     

##
##    axs[8, 1].plot(gg33b['Close_1d_ch'], 'tab:red', label = 'WilliamsR',linewidth=.5)
##    for tick in axs[1, 1].xaxis.get_major_ticks():
##        tick.label.set_fontsize(6)
##        tick.label.set_rotation('vertical')
##    for tick in axs[1, 1].yaxis.get_major_ticks():
##        tick.label.set_fontsize(6)       
##    axs[8, 1].set_title('Close_1d_ch', fontsize=7)

    
##    fig.show()
##    plt.subplots_adjust(wspace=0, hspace=0)
##    matplotlib.pyplot.subplots_adjust(wspace=.2, hspace=.9)
##    axs.set_xticks(gg33b['index'])
    
##    plt.xticks(gg33b['index'])
    plt.show()
    
days()




