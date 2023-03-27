
import talib as ta
from ta.utils import dropna
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
import matplotlib.pyplot as plt
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
from datetime import time
import matplotlib.pyplot as plt

pd.options.display.width = 0
pd.set_option('display.max_columns', None)
pd.options.display.float_format = '{:.2f}'.format
##pd.options.display.max_columns=255
pd.options.display.max_rows=6500000
pd.set_option('display.max_colwidth', 500)
pd.set_option('display.max_columns', 550)
pd.options.mode.chained_assignment = None  # default='warn'

print('100% confirm---stoch/fastd is 100. Stock will be green, if 0 meaning stock will be red')

def days():

    
    perda='635d'
    intervla='1d'
    yy=str(intervla).split('d')[0]
    shiftbydays=3



    ##    g=input("Entr_Signal ticker: ")
    perd=perda
    intervl=intervla
##    ticker='BTC-USD'
    ticker='^NDX'
##    ticker='MSTR'
##    ticker='MRNA'

    # [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]

    

    #df=pd.DataFrame()
    #Interval required 5 minutes
    df = yf.download(ticker, period=perd, interval=intervl,prepost = True)
    df2=pd.DataFrame()
    df['*']=''
    df['Candlea']=''
    print(df.columns)
    for x in df.index:
        df['Candlea'].loc[x]=df['High'].loc[x]-df['Open'].loc[x]
        df['*'].loc[x]='*'
##        df['Close_d_ch'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc(x)
    ##    print(df['Close'].loc[x])
        ########################################################

    ##close = numpy.random.random(100)
    df['SAR']=ta.SAR(df['High'],df['Low'], acceleration=0.02, maximum=0.2)
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
    
##    df['day']=datetime.datetime(df['Date'])
    

    #############################
    ##for x in df.index:
    ##            df['Volume'].loc[x]=numerize.numerize(np.float32(df['Volume'].loc[x]).item())

    df2=df
    df['d']=''
##    df['Candlea']=''
    df['Opena']=''
    df['green']=''
    df['greenby']=''
    df['compare_d']=''
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
    df['bol_wd']=''
    df['up_bol_wd']=''
    df['lw_bol_wd']=''
    df['status']=''
    df['status2']=''

    
 
    
    for x in df.index:
        
        df['bol_wd'].loc[x]=df['BB_upperband'].loc[x]-df['BB_lowerband'].loc[x]
        df['up_bol_wd'].loc[x]=df['BB_upperband'].loc[x]-df['BB_middleband'].loc[x]
        df['lw_bol_wd'].loc[x]=df['BB_upperband'].loc[x]-df['BB_middleband'].loc[x]
        df['pivot'].loc[x]='pivot->'

        df['pp'].loc[x]=df['Close'].loc[x]
        df['pp'].loc[x]=(df['Close'].loc[x]+df['Low'].loc[x]+df['High'].loc[x])/3
        df['r1'].loc[x]=2*df['pp'].loc[x]-df['Low'].loc[x].round(0)
        df['r2'].loc[x]=df['pp'].loc[x]+(df['High'].loc[x]-df['Low'].loc[x])
        df['r3'].loc[x]=df['High'].loc[x]+2*(df['pp'].loc[x]-df['Low'].loc[x])

        df['s1'].loc[x]=2*df['pp'].loc[x]-df['High'].loc[x]
        df['s2'].loc[x]=df['pp'].loc[x]-(df['High'].loc[x]-df['Low'].loc[x])
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



        
        df['volatility'].loc[x]=df['BB_upperband'].loc[x]-df['BB_lowerband'].loc[x]
        df['Bolinger'].loc[x]='Bolinger'
        df['BB_up'].loc[x]=df['Close'].loc[x]-df['BB_upperband'].loc[x]
        df['BB_low'].loc[x]=df['Close'].loc[x]-df['BB_lowerband'].loc[x]
        df['BB_mid'].loc[x]=df['Close'].loc[x]-df['BB_middleband'].loc[x]
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
    df['Close->']=''
    df['swng->']='swng->'
    df['open/close']='open/close->'
    df['HA->']=''
    df['CCI/RSI->']=''
    df['MA->']=''
   
    for x in df.index:
        
##        df['Candle'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
        df['MA->'].loc[x]='MA'
        df['CCI/RSI->'].loc[x]='CCI/RSI->'
        
        df['HA->'].loc[x]='HA->'
        df['open/close'].loc[x]='open/close'
        df['swng->'].loc[x]='swng->'
        df['Close->'].loc[x]='Close->'
        df['*'].loc[x]='*'
        df['swng'].loc[x]=df['High'].loc[x]-df['Low'].loc[x]
        df['Close_d'].loc[x]=df['Close'].shift(shiftbydays).loc[x]
        df['Close_1d_ch'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]
        df['Close_3d_ch'].loc[x]=df['Close'].loc[x]-df['Close'].shift(3).loc[x]
        df['Close_5d_ch'].loc[x]=df['Close'].loc[x]-df['Close'].shift(5).loc[x]
        df['Close_30d_ch'].loc[x]=df['Close'].loc[x]-df['Close'].shift(30).loc[x]

##########################
        if df['pp'].loc[x] < df['Close'].loc[x] :
            df['status'].loc[x]='Pass/UP'
        elif  df['pp'].loc[x] > df['Close'].loc[x]:
            df['status'].loc[x]='Fail/Down'

        if df['Close_1d_ch'].loc[x] > 0 :
            df['status2'].loc[x]='Pass/Green'
        elif  df['Close_1d_ch'].loc[x] < 0 :
            df['status2'].loc[x]='Fail/Red'    

        
##########################      


        
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

    ############################ end of ha




    ##ddd=(df['Volume']-df['Volume'].shift(1))
    tt=pd.concat([df['status'],df['status2'],df['MOM'],df['Candlea'],df['bol_wd'],df['up_bol_wd'],df['lw_bol_wd'],
                  df['BB_upperband'], df['BB_middleband'], df['BB_lowerband'],
                  df['direct'],df['HA'],df['Close'],df['Close_d_ch'],df['Volume'],
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
                  df['Close->'],df['swng->'],df['Low'],df['High'],df['Open'],df['open/close'],df['CCI/RSI->'],df['HA->'],
                  df['MA->'],df['BB_up'],df['BB_low'],df['BB_mid'],df['Bolinger'],df['volatility'],
                  df['pivot'],df['pp'],df['r1'],df['r2'],df['r3'],df['s1'],df['s2'],df['s3'],df['pivotx'],
                  df['ppx'],df['r1x'],df['r2x'],df['r3x'],df['s1x'],df['s2x'],df['s3x']
                  ],axis=1)

##    print(tt.tail(4))
    print('tt-columns:',tt.columns)



    
##    sys.exit()
    tt.columns=['status','status2','MOM','bol_wd','up_bol_wd','lw_bol_wd','Candlea','BB_upperband','BB_middleband','BB_lowerband','direct', 'HA', 'Close', 'Close_d_ch', 'Volume', 'Volumea', 'CCI', 'DX',
       'WILLR', 'RSI', 'adx', 'WilliamsR', 'ATR', 'ULTOSC', 'ROC', 'PLUS_DI',
       'PLUS_DM', 'HT_DCPERIOD', 'HT_DCPHASE', 'sine', 'leadsine', 'aroondown',
       'aroonup', 'macd', 'macdsignal', 'macdhist', 'PLUS_DI', 'PLUS_DM',
       'PPO', 'ROC', 'ROCP', 'ROCR', 'ROCR100', '*', 'CDLDOJI', 'CDLDOJISTAR',
       'CDLDRAGONFLYDOJI', 'CDLEVENINGDOJISTAR', 'CDLGRAVESTONEDOJI',
       'CDLHAMMER', 'CDLXSIDEGAP3METHODS', '*', 'EMA_3', 'EMA_5', 'EMA_10',
       'EMA_21', 'EMA_50', 'EMA_100', 'EMA_200', 'EMA_3s', 'EMA_5s', 'EMA_10s',
       'EMA_21s', 'EMA_50s', 'EMA_100s', 'EMA_200s','ticker' ,'intervl','Close_d','compare_d','Close_1d_ch','Close_3d_ch','Close_5d_ch','Close_30d_ch',
                'swng','Close->','swng->','Low','High','Open','open/close','CCI/RSI->','HA->','MA->',
                'BB_up','BB_low','BB_mid','Bolinger','volatility'
                ,'pivot','pp','r1','r2','r3','s1','s2','s3','pivotx',
                'ppx','r1x','r2x','r3x','s1x','s2x','s3x'
                ]

    


    
    
    tt.reset_index(inplace=True)        
    for x in tt.index:
    ##    print(tt['Volume'])
    ##    tt['Volume'].loc[x]=numerize.numerize(tt['Volume'].loc[x])
    ##    tt['Volume'].loc[x]=numerize.numerize((tt['Volume'].iloc[x][1]))  4
        tt['Volume'].loc[x]=numerize.numerize(np.float32(tt['Volume'].loc[x]).item())

##    print(tt.index)
####    tt.reset_index()    
##    tt.set_index('Date',inplace=True)
    
    print('\n',tt.columns,'\n')
    print('tt.columns.get_loc-------Date------------------------ ',tt.columns.get_loc('Date'))
    print('tt.columns.get_loc---EMA_200----------------------------- ',tt.columns.get_loc('EMA_200'))

    tt = tt.dropna()
##    gg33=tt.iloc[:,[57,0,58,60,66,3,61,67,65,68,69,71,3,70,59,61,62,63,64,4,67,65,
##                    66,3,61,73,1,2,72,7,10,49,78,75,76,77,79,74,43,44,45,46,47,48,49,
##                    80,88,81,87,86,85,82,83,84
##                    ,80,89,95,94,93,90,91,92
##                    ]].tail(235)


    
    gg33=tt[[ 'Date','ticker', 'pivot','pivotx','pp','*','status','status2','*','Close_1d_ch','*','*','r1','r2','r3','*','s1','s2','s3','*',
              'volatility','*','intervl','Close','Close_1d_ch','Candlea', 'MOM', 'swng','direct', 'HA','Volume','*','*',
               'EMA_3','EMA_5', 'EMA_10', 'EMA_21', 'EMA_50', 'EMA_100', 'EMA_200','*','*',
             'EMA_3s','EMA_5s', 'EMA_10s', 'EMA_21s', 'EMA_50s', 'EMA_100s', 'EMA_200s','*','*',
              'volatility','bol_wd', 'up_bol_wd', 'lw_bol_wd', 'BB_upperband','BB_middleband', 'BB_lowerband','*','*',
             'Low', 'High','Open','Close','*','*','Close_d', 'compare_d','Close_3d_ch', 'Close_5d_ch', 'Close_30d_ch','Close_d_ch','*','*',
            'CDLDOJI','CDLDOJISTAR', 'CDLDRAGONFLYDOJI', 'CDLEVENINGDOJISTAR','CDLGRAVESTONEDOJI', 'CDLHAMMER', 'CDLXSIDEGAP3METHODS','*','*','CCI','DX', 'WILLR', 'RSI', 'adx', 'WilliamsR', 'ATR', 'ULTOSC', 'ROC','PLUS_DI', 'PLUS_DM', 'HT_DCPERIOD', 'HT_DCPHASE', 'sine',
             'leadsine','aroondown', 'aroonup', 'macd', 'macdsignal', 'macdhist', 'PLUS_DI','PLUS_DM', 'PPO', 'ROC', 'ROCP', 'ROCR', 'ROCR100', '*','*',
             
            'pivot','pp','*','r1','r2','r3','*','s1','s2','s3','*','*',
            'pivotx',
            'ppx','*','r1x','r2x','r3x','*','s1x','s2x','s3x','*','*'



              ]]




    

##    gg33=tt[['Date','ticker', 'intervl','Close','Close_1d_ch','Candle', 'MOM', 'swng','direct', 'HA','Volume','Volumea']]
    
##    plt.axhline(y=0, color='r', linestyle='-')
##    fig = plt.figure()
##    ax = plt.axes()
##    plt.plot(gg33['BB_upperband'])
    


##    t=tt[tt.aroonup == 0]
##    print('ddddd',t)

##
##    print(tta)
##
##    gg33=gg33[['EMA_50s', 'Date', 'EMA_100s', 'ticker']]

    
    
    print('\n','Close_delta_price_by_'+str(shiftbydays)+' days','\n',gg33)
    print(gg33.columns)
    
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

##    print('Daily CCI: ', tt.tail(4))
    ##MA = ta.SMA(df['close'])
    ##print('MA: ',MA)
    #########################################################################################################################

    ##from talib import MA_Type
    ##upper, middle, lower = talib.BBANDS(close, matype=MA_Type.T3)
    ##print('bolinger_bands: ', upper,'  ', middle,'  ',lower)

def hourly():
    from numerize import numerize

##    perda='635d'
##    intervla='1d'
##    yy=str(intervla).split('d')[0]
##    shiftbydays=3

##    perda='75d'
    perda='23d'
    intervla='60m'

    yy=str(intervla).split('d')[0]
    shiftbydays=3



    ##    g=input("Entr_Signal ticker: ")
    perd=perda
    intervl=intervla
##    ticker='BTC-USD'
    ticker='^NDX'
##    ticker='MSTR'
##    ticker='MRNA'

    # [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]



    #df=pd.DataFrame()
    #Interval required 5 minutes
    df = yf.download(ticker, period=perd, interval=intervl,prepost = False)
    df2=pd.DataFrame()
##    df['*']=''
##    for x in df.index:
##        df['*'].loc[x]='*'
##        df['Close_d_ch'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc(x)
    ##    print(df['Close'].loc[x])
        ########################################################

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
    
##    df['day']=Datetimetime.Datetimetime(df['Datetime'])
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
    
    
##    
##
    
    for x in df.index:
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
        df['5_10_crossovr'].loc[x]=df['EMA_5'].loc[x]-df['EMA_10'].loc[x]
        df['10_21_crossovr'].loc[x]=df['EMA_10'].loc[x]-df['EMA_21'].loc[x]
        df['21_50_crossovr'].loc[x]=df['EMA_21'].loc[x]-df['EMA_50'].loc[x]
        df['50_100_crossovr'].loc[x]=df['EMA_50'].loc[x]-df['EMA_100'].loc[x]

    ############################ end of ha




    ##ddd=(df['Volume']-df['Volume'].shift(1))
    tt=pd.concat([df['bol_wd'],df['up_bol_wd'],df['lw_bol_wd'],
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
                  df['3_5_crossovr'],df['5_10_crossovr'],df['10_21_crossovr'],df['21_50_crossovr'],df['50_100_crossovr']


                  ],axis=1)

##    print(tt.tail(4))     df['Buy_50EMA_100EMA']=''


##    
##    sys.exit()
##    tt.columns=[['direct','HA','Close','Close_d_ch','Volume',
##                  'Volumea','CCI','DX','WILLR','RSI','adx','WilliamsR',
##                  'ATR','ULTOSC',
##                  'ROC','PLUS_DI','PLUS_DM',
##                  'HT_DCPERIOD',
##                  'HT_DCPHASE',
##                  'sine','leadsine','aroondown', 'aroonup',
##                  'macd', 'macdsignal', 'macdhist','PLUS_DI','PLUS_DM','PPO','ROC','ROCP',
##                  'ROCR','ROCR100',
##                  '*',
##                  'CDLDOJI','CDLDOJISTAR','CDLDRAGONFLYDOJI','CDLEVENINGDOJISTAR','CDLGRAVESTONEDOJI',
##                  'CDLHAMMER','CDLXSIDEGAP3METHODS',
##                  '*','EMA_3','EMA_5','EMA_10','EMA_21','EMA_50','EMA_100','EMA_200','EMA_3s',
##                  'EMA_5s','EMA_10s','EMA_21s','EMA_50s','EMA_100s','EMA_200s','ticker','intervl',
##                  'Close_d','compare_d','Close_1d_ch','Close_3d_ch','Close_5d_ch','Close_30d_ch','swng',
##                  'MA->','CCI/RSI->','Close->','HA->',
##                  'Close->','swng->','Low','High','Open']]


##        'direct', 'HA', 'Close', 'Close_d_ch', 'Volume', 'Volumea', 'CCI', 'DX',
##       'WILLR', 'RSI', 'adx', 'WilliamsR', 'ATR', 'ULTOSC', 'ROC', 'PLUS_DI',
##       'PLUS_DM', 'HT_DCPERIOD', 'HT_DCPHASE', 'sine', 'leadsine', 'aroondown',
##       'aroonup', 'macd', 'macdsignal', 'macdhist', 'PLUS_DI', 'PLUS_DM',
##       'PPO', 'ROC', 'ROCP', 'ROCR', 'ROCR100', '*', 'CDLDOJI', 'CDLDOJISTAR',
##       'CDLDRAGONFLYDOJI', 'CDLEVENINGDOJISTAR', 'CDLGRAVESTONEDOJI',
##       'CDLHAMMER', 'CDLXSIDEGAP3METHODS'
##                '*', 'EMA_3', 'EMA_5', 'EMA_10',
##       'EMA_21', 'EMA_50', 'EMA_100', 'EMA_200', 'EMA_3s', 'EMA_5s', 'EMA_10s'
##       'EMA_21s', 'EMA_50s', 'EMA_100s', 'EMA_200s','ticker' ,'intervl','Close_d','compare_d','Close_1d_ch','Close_3d_ch','Close_5d_ch','Close_30d_ch'
##                'swng','MA->','CCI/RSI->','Close->','HA->'
##
    tt.reset_index(inplace=True)
    tt.set_index=('Datetime')
    print('tt-columns:',tt.columns)
    print('tt length:', len(tt.columns))
    tt.reset_index(inplace=True)        
    for x in tt.index:
    ##    print(tt['Volume'])
    ##    tt['Volume'].loc[x]=numerize.numerize(tt['Volume'].loc[x])
    ##    tt['Volume'].loc[x]=numerize.numerize((tt['Volume'].iloc[x][1]))
        tt['Volume'].loc[x]=numerize.numerize(np.float32(tt['Volume'].loc[x]).item())



# 666
##    tt.set_index('Datetime')
##
##    t6=pd.DataFrame(tt)
##    print('\n777',t6.columns,'\n')
##    print('\n',t6.index,'\n')
##    t6.reset_index(inplace=True)
##    t6.set_index('Datetime')
##    print('\n',t6.columns,'\n')
##    print('uuuuu')
##
##    print(tt.columns.get_loc('s1'))

# 666
##    df2 = tt.loc[:3, :]
    print('kkkk')
##    print(tt.columns.get_loc("ATR"))
##    print(tt['Close_d'])
##    print(tt.columns.get_loc("EMA_3"))


    print(tt.shape[1])
##    print(tt.iloc[:0,:])

## andrea boggs
        
##    gg33=tt.iloc[:,[57,0,58,60,3,59,65,4,61,62,63,64,4,68,3,61,69,1,2,3,4,7,66,10,43,73,67,44,45,46,47,48,49,57,58]].tail(335)
##    gg33=tt.iloc[:,[1,0,52,65,79,6,77,78,62,63,64,68,4,3,69,2,3,4,73,67,
##                    69,9,12,13,11,10,43,44,16,
##                    68,45,46,47,6,70,2,4,5,3,48,49,50,51,52,53,54]].tail(115)


##    gg33=tt.iloc[:,[45,68,1,12,8,9,10,11,15,14,76,69,82,45,
##                    45,83,84,85,12,45,
##                    45,2,3,4,5,6,7,45,
##                    45,54,55,56,57,58,59,60,45,
##                    45,46,47,48,49,50,51,52,53,45,
##                    45,70,71,13,72,73,74,75,45,
##                    45,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]].tail(115)

##    gg33=tt[['index', 'Datetime', 'bol_wd', 'up_bol_wd', 'lw_bol_wd', 'BB_upperband',
##       'BB_middleband', 'BB_lowerband', 'Candle', 'MOM', 'direct', 'HA',
##       'Close', 'Close_d_ch', 'Volume', 'swng->', 'adx->', 'Volumea', 'CCI',
##       'DX', 'WILLR', 'RSI', 'adx', 'WilliamsR', 'ATR', 'ULTOSC', 'ROC',
##       'PLUS_DI', 'PLUS_DM', 'HT_DCPERIOD', 'HT_DCPHASE', 'sine', 'leadsine',
##       'aroondown', 'aroonup', 'macd', 'macdsignal', 'macdhist', 'PLUS_DI',
##       'PLUS_DM', 'PPO', 'ROC', 'ROCP', 'ROCR', 'ROCR100', '*', 'CDLDOJI',
##       'CDLDOJISTAR', 'CDLDRAGONFLYDOJI', 'CDLEVENINGDOJISTAR',
##       'CDLGRAVESTONEDOJI', 'CDLHAMMER', 'CDLXSIDEGAP3METHODS', '*', 'EMA_3',
##       'EMA_5', 'EMA_10', 'EMA_21', 'EMA_50', 'EMA_100', 'EMA_200', 'EMA_3s',
##       'EMA_5s', 'EMA_10s', 'EMA_21s', 'EMA_50s', 'EMA_100s', 'EMA_200s',
##       'ticker', 'intervl', 'Close_d', 'compare_d', 'Close_1d_ch',
##       'Close_3d_ch', 'Close_5d_ch', 'Close_30d_ch', 'swng', 'MA->',
##       'CCI/RSI->', 'Close->', 'HA->', 'Close->', 'swng->', 'Low', 'High',
##       'Open']]


##    gg33=tt[['index', 'Datetime','ticker', 'intervl','Close','Close_1d_ch','Candle', 'MOM', 'swng','direct', 'HA','Volume','Volumea','*','*',
##             'Low', 'High','Open','Close','*','*','Close_d', 'compare_d','Close_3d_ch', 'Close_5d_ch', 'Close_30d_ch','Close_d_ch','*','*',
##             'bol_wd', 'up_bol_wd', 'lw_bol_wd', 'BB_upperband','BB_middleband', 'BB_lowerband', '*','*','EMA_3','EMA_5', 'EMA_10', 'EMA_21', 'EMA_50', 'EMA_100', 'EMA_200', 'EMA_3s','*','*',
##             'EMA_3s','EMA_5s', 'EMA_10s', 'EMA_21s', 'EMA_50s', 'EMA_100s', 'EMA_200s','*','*','CDLDOJI','CDLDOJISTAR', 'CDLDRAGONFLYDOJI', 'CDLEVENINGDOJISTAR','CDLGRAVESTONEDOJI', 'CDLHAMMER', 'CDLXSIDEGAP3METHODS','*','*','CCI','DX', 'WILLR', 'RSI', 'adx', 'WilliamsR', 'ATR', 'ULTOSC', 'ROC','PLUS_DI', 'PLUS_DM', 'HT_DCPERIOD', 'HT_DCPHASE', 'sine',
##             'leadsine','aroondown', 'aroonup', 'macd', 'macdsignal', 'macdhist', 'PLUS_DI','PLUS_DM', 'PPO', 'ROC', 'ROCP', 'ROCR', 'ROCR100', '*','*']]

    print(tt.columns)
    gg33=tt[['index', 'Datetime','ticker', 'pivot','pivotx','pp','*','Close_1d_ch','*','r1','r2','r3','*','s1','s2','s3','*','volatility','*',
             'intervl','Close','Close_1d_ch','Candle', 'MOM', 'swng','direct', 'HA','Volume','*','*',
               'EMA_3','EMA_5', 'EMA_10', 'EMA_21', 'EMA_50', 'EMA_100', 'EMA_200','*','*',
             'EMA_3s','EMA_5s', 'EMA_10s', 'EMA_21s', 'EMA_50s', 'EMA_100s', 'EMA_200s','*','*',
              'volatility','bol_wd', 'up_bol_wd', 'lw_bol_wd', 'BB_upperband','BB_middleband', 'BB_lowerband','*','*',
             'Low', 'High','Open','Close','*','*','Close_d', 'compare_d','Close_3d_ch', 'Close_5d_ch', 'Close_30d_ch','Close_d_ch','*','*',
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
              '3_5_crossovr','5_10_crossovr','10_21_crossovr','21_50_crossovr','50_100_crossovr'

            

             ]]

##

   
##print('100% confirm---stoch/fastd is 100. Stock will be green, if 0 meaning stock will be red')
##print('rsi range 0-100, over 70 stock to go down/pullback/bearish, under 30 stock to go up/bullish/upside')
##print('macdhist has to be positive. Meaning 21 vs 26 crossover is +ve')
##print('mom')
##print('PLUS_DM-PLUS_DM if is +ve meaning bullish, -ve meaning -ve')


##    print('stupid',tt.columns)

##    for x in tt.columns:
##        print(x,'   ---->  ', tt.columns.get_loc(x))

##    print('tt.columns.get_loc------bol_wd----------------------- ',tt.columns.get_loc('bol_wd'))

    
##    print('tt.columns.get_loc--- BB_middleband---------------------------- ',tt.columns.get_loc('BB_middleband'))
##    print('tt.columns.get_loc--- BB_lowerband----------------------------- ',tt.columns.get_loc('BB_lowerband'))
##    print('tt.columns.get_loc--- direct---------------------------- ',tt.columns.get_loc('direct'))
##    print('tt.columns.get_loc--- direct---------------------------- ',tt.columns.get_loc('direct'))
##    print('tt.columns.get_loc--- HA---------------------------- ',tt.columns.get_loc('HA'))

##    gg33=tt.iloc[:,[57,0,58,60,66,3,61,67,65,68,69,71,3,70,59,61,62,63,64,4,67,65,
##                    66,3,61,73,1,2,72,7,10,49,78,75,76,77,79,74,43,44,45,46,47,48,49,
##                    80,88,81,87,86,85,82,83,84
##                    ,80,89,95,94,93,90,91,92
##                    ]].tail(235)


##
##    i=0
##    for c in (gg33.iloc[:0,:]):
##        print(i,'   ',c,'  gg33')
##        i=i+1
##    print('\n\n\n\n')
##    i=0
##    for c in (tt.iloc[:0,:]):
##        print(i,'   ',c,' tt ')
##        i=i+1
##        

    s3=str(gg33['Datetime']).split(' ')
    for x in gg33.index:
        print(str(gg33['Datetime'].loc[x]).split(' '))
##    gg33=gg33[gg33['Datetime']=='2021-09-20']
    print('\n','Close_delta_price_by_'+str(shiftbydays)+' days','\n',gg33)


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

    
    
    print(df.columns)
    
    
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

##    print('Daily CCI: ', tt.tail(4))
    ##MA = ta.SMA(df['close'])
    ##print('MA: ',MA)
    #########################################################################################################################

    ##from talib import MA_Type
    ##upper, middle, lower = talib.BBANDS(close, matype=MA_Type.T3)
    ##print('bolinger_bands: ', upper,'  ', middle,'  ',lower)

##    tt=pd.DataFrame(tt)
##
##    for x in df.index:
##        if len(df['Volume'].loc[x])>9:
##            df['Volume'].loc[x]=str(np.float64(df['Volume'].loc[x])/np.float64(100000000))+' Billion'
##        elif len(df['Volume'].loc[x]) < 7:
##            df['Volume'].loc[x]=str(np.float64(df['Volume'].loc[x])/np.float64(1000000))+' Million'    
####        print(x,'   ',tt2['Close'].loc[x],'   ',tt2['Close'].loc[x]+tt2['Close'].loc[x])
##        
##          
####        tt['Close'].loc[x]=tt['Close'].loc[x]/5
####        np.float64(tt2['Close'].loc[x])==5
##        
####        tt['Volume'].loc[x]=np.float64(tt['Volume'].loc[x])/55555
##        
####        print(tt['Volume'])
####        tt['Volume'].loc[x]=numerize.numerize(np.float64(tt['Volume']).loc[x].item())
####        tt['Volume'].loc[x]=numerize.numerize(tt['Volume'].loc[x])
##    ##    tt['Volume'].loc[x]=numerize.numerize((tt['Volume'].iloc[x][1]))
####        if (tt['Volume'].loc[x]) > 4:
####        tt['Volume'].loc[x]=numerize.numerize(np.float(tt['Volume']).loc[x].item())
##    df.set_index('Datetime')
##
##
####    tt=pd.concat([df2['direct'],df2['HA'],df['Close'],(df['Close']-df['Close'].shift(1)),df['Volume'],df['Volumea'],CCI,DX,WILLR,df['*'],CDLDOJI,CDLDOJISTAR,CDLDRAGONFLYDOJI,CDLEVENINGDOJISTAR,CDLGRAVESTONEDOJI,CDLHAMMER,CDLXSIDEGAP3METHODS,
####                  df['*'],EMA_3,EMA_5,EMA_10,EMA_21,EMA_50,EMA_100,EMA_200],axis=1)
####
####    tt.columns=['direct','HA','Close','Close_d_ch','Volume','Volumea','CCI','DX','WILLR',"*",'CDLDOJI','CDLDOJISTAR','CDLDRAGONFLYDOJI','CDLEVENINGDOJISTAR','CDLGRAVESTONEDOJI','CDLHAMMER','CDLXSIDEGAP3METHODS',
####                '*','EMA_3','EMA_5','EMA_10','EMA_21','EMA_50','EMA_100','EMA_20']
####


##    print('CCI: ', tt)
##    print('Close: ', tt['Volume'])


      
##    for x in tt.index:
##    ##    print(tt['Volume'])
##    ##    tt['Volume'].loc[x]=numerize.numerize(tt['Volume'].loc[x])
##    ##    tt['Volume'].loc[x]=numerize.numerize((tt['Volume'].iloc[x][1]))
##        tt['Volume'].loc[x]=numerize.numerize(np.float32(tt['Volume'].loc[x]).item())
##    tt.set_index('Datetime')
##
##    print(intervla,' Hourly CCI: ', tt)
    ##MA = ta.SMA(df['close'])
    ##print('MA: ',MA)    
##days()
hourly()

print('100% confirm---stoch/fastd is 100. Stock will be green, if 0 meaning stock will be red')
print('rsi range 0-100, over 70 stock to go down/pullback/bearish, under 30 stock to go up/bullish/upside')
print('macdhist has to be positive. Meaning 21 vs 26 crossover is +ve')
