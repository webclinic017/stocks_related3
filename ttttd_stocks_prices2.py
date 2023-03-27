
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


def days():
    
    perda='635d'
    intervla='1d'
    yy=str(intervla).split('d')[0]
    shiftbydays=3



    ##    g=input("Entr_Signal ticker: ")
    perd=perda
    intervl=intervla
##    ticker='^NDX'
    ticker='BTC-USD'
##    ticker='MSTR'
##    ticker='MRNA'

    # [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]



    #df=pd.DataFrame()
    #Interval required 5 minutes
    df = yf.download(ticker, period=perd, interval=intervl,prepost = True)
    df2=pd.DataFrame()
    df['*']=''
    for x in df.index:
        df['*'].loc[x]='*'
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
    df['crash']=''
    df['crash->']=''
    df['MSTR->']=''
    df['MSTR']=''
    df['Move->']=''
    df['Move']=''

    
    

    for x in df.index:
        df['pivot'].loc[x]='pivot->'

        if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > 5000:
            df['Move->'].loc[x]='**[5K >]** Move UP->'
            df['Move'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]


        if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > 3000 and (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < 5000:
            df['Move->'].loc[x]='**[3K-5K]** Move UP->'
            df['Move'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]

        if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > 1000 and (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < 3000:
            df['Move->'].loc[x]='[1K-3K] Move UP->'
            df['Move'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]


        if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > 500 and (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < 1000:
            df['Move->'].loc[x]='[500-1K] Move UP->'
            df['Move'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]

        if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > 0 and (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < 500:
            df['Move->'].loc[x]='[0-500] Move UP->'
            df['Move'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]       
            
        
        if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < -5000:
            df['crash->'].loc[x]='** 5K crash-> **'
            df['crash'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]
            df['MSTR->'].loc[x]='MSTR->'
            df['MSTR'].loc[x]=(df['Close'].loc[x]-df['Close'].shift(1).loc[x])/73

        if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < -3000 and (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > -5000:
            df['crash->'].loc[x]='** [3K-4.9K crash-> **'
            df['crash'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]
            df['MSTR->'].loc[x]='MSTR->'
            df['MSTR'].loc[x]=(df['Close'].loc[x]-df['Close'].shift(1).loc[x])/73


        if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < -1000 and (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > -3000:
            df['crash->'].loc[x]='[1K-3K] Dwn->'
            df['crash'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]
            df['MSTR->'].loc[x]='MSTR->'
            df['MSTR'].loc[x]=(df['Close'].loc[x]-df['Close'].shift(1).loc[x])/73


        if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < 0 and (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > -1000:
            df['crash->'].loc[x]='[0-1K] Dwn->'
            df['crash'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]
            df['MSTR->'].loc[x]='MSTR->'
            df['MSTR'].loc[x]=(df['Close'].loc[x]-df['Close'].shift(1).loc[x])/73    
            
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
    tt=pd.concat([df['direct'],df['HA'],df['Close'],df['Close_d_ch'],df['Volume'],
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
                  df['ppx'],df['r1x'],df['r2x'],df['r3x'],df['s1x'],df['s2x'],df['s3x'],
                  df['crash->'],df['crash'],df['MSTR->'],df['MSTR'],df['Move->'],df['Move']
                  ],axis=1)

##    print(tt.tail(4))
    print('tt-columns:',tt.columns)
    
##    sys.exit()
    tt.columns=['direct', 'HA', 'Close', 'Close_d_ch', 'Volume', 'Volumea', 'CCI', 'DX',
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
                'ppx','r1x','r2x','r3x','s1x','s2x','s3x','crash->','crash','MSTR->','MSTR','Move->','Move'
                ]

    tt.reset_index(inplace=True)        
    for x in tt.index:
    ##    print(tt['Volume'])
    ##    tt['Volume'].loc[x]=numerize.numerize(tt['Volume'].loc[x])
    ##    tt['Volume'].loc[x]=numerize.numerize((tt['Volume'].iloc[x][1]))  4
        tt['Volume'].loc[x]=numerize.numerize(np.float32(tt['Volume'].loc[x]).item())
    tt.set_index('Date')
    print('\n',tt.columns,'\n')
    print('stupid azhar ',tt.columns.get_loc('Move->'))
    
    gg33=tt.iloc[:,[100,101,96,97,98,99,57,0,58,60,66,3,61,67,65,68,69,71,3,70,59,61,62,63,64,4,67,65,
                    
                    66,3,61,73,1,2,72,7,10,49,78,75,76,77,79,74,43,44,45,46,47,48,49,
                    80,88,81,87,86,85,82,83,84
                    ,80,89,95,94,93,90,91,92
                    ]].tail(235)
    
    print('\n','Close_delta_price_by_'+str(shiftbydays)+' days','\n',gg33)
    
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
    import openpyxl
    m33=0
    x34=34
    x35=35
    

##    perda='635d'
##    intervla='1d'
##    yy=str(intervla).split('d')[0]
##    shiftbydays=3

    
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
    print('\n','****************************************************','\n')
    print("jjjj ",df)
    print('\n','****************************************************','\n')
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
    
    
    k=0
    k3=0
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





            
################################################## and (df['EMA_3'].loc[x]-df['EMA_3'].shift(1).loc[x]) > 0 and (df['EMA_3'].shift(2).loc[x]-df['EMA_3'].shift(1).loc[x]) > 0

##        if df['HA'].loc[x]-df['HA'].shift(1).loc[x] > 100 and\
##           (df['Close'].loc[x] - df['Close'].shift(1).loc[x]) > 0 and\
##           (df['Close'].loc[x]-df['EMA_21s'].loc[x]) > 100 and\
##           (df['EMA_3s'].loc[x]-df['EMA_3s'].shift(2).loc[x]) > 0 and\
##           (df['EMA_21s'].loc[x]- df['EMA_21s'].shift(1).loc[x]) >  0  and\
##           (df['EMA_21s'].shift(1).loc[x]- df['EMA_21s'].shift(2).loc[x]) > 0 and\
##           (df['EMA_50s'].loc[x]- df['EMA_50s'].shift(1).loc[x]) > 0 and\
##           (df['EMA_100s'].loc[x]- df['EMA_100s'].shift(1).loc[x]) > 0 and\
##           (df['EMA_200s'].loc[x]- df['EMA_200s'].shift(1).loc[x]) > 0 :
##            df['signal'].loc[x]='Buy_Signal'

##        if (df['Close'].shift(1).loc[x] - df['Close'].loc[x]) < 0 and\
##           df['Close'].loc[x]- df['EMA_3s'].loc[x] > 0 and\
##           df['Close'].loc[x]- df['EMA_21s'].loc[x] > 0 and\
##           df['EMA_3'].loc[x] > 0 and\
##           df['EMA_3'].loc[x]-df['EMA_3'].shift(1).loc[x] > 0 and\
##           df['HA'].loc[x] > 0 and\
##           (df['EMA_3s'].shift(1).loc[x] - df['EMA_3s'].loc[x]) < 0 and\
##           (df['EMA_21s'].shift(1).loc[x] - df['EMA_21s'].loc[x]) < 0 and\
##           (df['EMA_10s'].shift(1).loc[x] - df['EMA_10s'].loc[x]) < 0 and\
##           (df['EMA_50s'].shift(1).loc[x] - df['EMA_50s'].loc[x]) < 0 and\
##           (df['EMA_100s'].shift(1).loc[x] - df['EMA_100s'].loc[x]) < 0 and\
##           (df['EMA_200s'].shift(1).loc[x] - df['EMA_200s'].loc[x]) < 0 and\
##           (df['HA'].shift(1).loc[x] - df['HA'].loc[x]) < 0:
##            df['signal'].loc[x]='Buy_Signal'

####           (df['EMA_3s'].shift(1).loc[x] - df['EMA_3s'].loc[x]) < 0 and\
##       ##            df['CCI'].loc[x] > 100 and\      


##        df['MD->'].loc[x]='->'
##        df['MD'].loc[x]=df['EMA_10s'].loc[x]-df['EMA_21s'].loc[x]
            
##        if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > 0 and\
##           (df['Close'].loc[x]-df['Close'].shift(2).loc[x]) > 0 and\
##           (df['Close'].loc[x]-df['Close'].shift(3).loc[x]) > 0 and\
##           (df['Close'].shift(1).loc[x]-df['Close'].shift(2).loc[x]) > 0 and\
##           df['HA'].loc[x] > 200 and\
##           df['HA'].shift(1).loc[x] > 0 and\
##           df['HA'].shift(2).loc[x] > 0 and\
##           df['HA'].loc[x]-df['HA'].shift(1).loc[x] > 200 and\
##           df['HA'].shift(1).loc[x]-df['HA'].shift(2).loc[x] > 200 and\
##           df['Close'].loc[x]- df['EMA_3s'].loc[x] > 200 and\
##           df['Close'].loc[x]- df['EMA_21s'].loc[x] > 200 and\
##           df['EMA_3'].loc[x] > 0 and\
##           df['EMA_3'].loc[x]-df['EMA_3'].shift(1).loc[x] > 200 and\
##           (df['EMA_21s'].shift(1).loc[x] - df['EMA_21s'].loc[x]) < -200 and\
##           (df['EMA_10s'].shift(1).loc[x] - df['EMA_10s'].loc[x]) < 0 and\
##           (df['EMA_50s'].shift(1).loc[x] - df['EMA_50s'].loc[x]) < 0 and\
##           (df['EMA_100s'].shift(1).loc[x] - df['EMA_100s'].loc[x]) < 0 and\
##           (df['EMA_200s'].shift(1).loc[x] - df['EMA_200s'].loc[x]) < 0 and\
##           (df['HA'].shift(1).loc[x] - df['HA'].loc[x]) < -200:
##            df['signal'].loc[x]='Buy_Signal'

            
 ##           (df['CCI'].loc[x]  > -120) and\
            ##           df['EMA_3'].loc[x] < 0 and\
##           df['HA'].loc[x] < 0 and\
##        if (df['Low'].loc[x] - df['Low'].shift(1).loc[x]) < 0 and\
##           (df['High'].loc[x] - df['High'].shift(1).loc[x]) < 0 and\
##           (df['Open'].loc[x] - df['Open'].shift(1).loc[x]) < 0 and\
##           (df['Close'].loc[x] - df['Close'].shift(1).loc[x]) < -40 and\
##           (df['Close'].loc[x] - df['Close'].shift(2).loc[x]) < 0 and\
##           (df['Close'].loc[x]- df['EMA_3s'].loc[x] < 0 or\
##           df['Close'].loc[x]- df['EMA_21s'].loc[x] < 0 or
##           df['EMA_3s'].loc[x]-df['EMA_3s'].shift(1).loc[x] < 0 ) and\
##           (df['HA'].shift(1).loc[x] - df['HA'].loc[x]) > 0 and\
##           (abs(df['macd'].loc[x])  < 1) and\
##           (df['HA'].shift(2).loc[x] - df['HA'].shift(1).loc[x]) > 0:
##            df['signal'].loc[x]='Sell_Signal'

#(df['macd'].loc[x])  < 23) and\
            #            (df['EMA_3'].shift(2).loc[x] - df['EMA_3'].shift(1).loc[x]) > 0:
            #           (df['EMA_3'].shift(1).loc[x] - df['EMA_3'].loc[x]) > 0:

##
##'''
##           df['EMA_3'].shift(1).loc[x]-df['EMA_3'].loc[x] < 0 and\
##           df['EMA_5'].shift(1).loc[x]-df['EMA_5'].loc[x] < 0 and\
##           df['EMA_10'].shift(1).loc[x]-df['EMA_10'].loc[x] < 0 and\
##           df['EMA_21'].shift(1).loc[x]-df['EMA_21'].loc[x] < 0 and\
##           df['EMA_50'].shift(1).loc[x]-df['EMA_50'].loc[x] < 0 and\
##           df['EMA_100'].shift(1).loc[x]-df['EMA_100'].loc[x] < 0 and\
##           df['EMA_200'].shift(1).loc[x]-df['EMA_200'].loc[x] < 0 and\
##'''
##           df['EMA_5'].loc[x] < 0 and\
##           df['EMA_10'].loc[x] < 0 and\
##           df['EMA_21'].loc[x] < 0 and\
##           df['EMA_50'].loc[x] < 0 and\
##           df['EMA_100'].loc[x] < 0 and\
##           df['EMA_200'].loc[x] < 0 and\            

##           df['EMA_3'].shift(1).loc[x]-df['EMA_3'].loc[x] < 0 and\
##           df['EMA_3'].shift(2).loc[x]-df['EMA_3'].shift(1).loc[x] < 0 and\
#########################################  buy ###################################
##        if (df['Close_1d_ch'].loc[x])  < -17:
##            df['signal'].loc[x]='**Sell_Signal**'
##           df['Close_1d_ch'].shift(1).loc[x]  > 33 and\
##           df['EMA_3'].loc[x] > 0 and\
##           df['EMA_3'].loc[x] > df['EMA_5'].loc[x] and\
##           df['EMA_5'].loc[x] > df['EMA_21'].loc[x] and\
##           df['EMA_3'].shift(1).loc[x] > 0 and\   

        

                  
        if (df['MOM'].loc[x])  > 30 and\
           df['Close_1d_ch'].shift(1).loc[x]  > 33 and\
           df['macd'].loc[x]  > 10 and\
           df['Close_1d_ch'].loc[x]  > 15  and\
           df['HA'].loc[x] > 5 and\
           df['HA'].shift(1).loc[x] > 5 :
            df['signal'].loc[x]='Buy_Signal'
            print(k3,'  buy value: ', buy)

            df['signal'].loc[x]='rr///Buy_Signal'
            m33=df['Close'].loc[x]
            print("**********************************************************",'\n')
            print("buy ---->")      
            print(k3, "longer=== buy ",df['Close'].loc[x])
            buy_order="yes"

            

##        if (df['MOM'].loc[x])  > 50 and\
##           df['MOM'].shift(1).loc[x]  > 20 and\
##           df['EMA_3'].loc[x] > 30 and\
##           (df['Close_1d_ch'].loc[x])  > 90 and\
##           df['HA'].loc[x] > 25 :
##            df['signal'].loc[x]='** Major Buy_Signal'
##            if buy == '3':
##                
##                buy = '9'
##                df['signal'].loc[x]='short///Buy_Signal'
##                m33=df['Close'].loc[x]
##                print(x, "qq=== buy ",df['Close'].loc[x])

##        if (df['MOM'].loc[x])  > 0 and\
##               df['MOM'].shift(1).loc[x]  > 0 and\
##               df['EMA_3'].loc[x] > 0 and\
##               (df['Close_1d_ch'].loc[x])  > 90 and\
##               df['HA'].loc[x] > 0 :
##                df['signal'].loc[x]='** Major Buy_Signal'
##                if buy == '3':
##                    
##                    buy = '9'
##                    df['signal'].loc[x]='short///Buy_Signal'
##                    m33=df['Close'].loc[x]
##                    print(x, "qq=== buy ",df['Close'].loc[x])           
            
############################################ sell #############################
##        if df['Close'].loc[x]-m33 > 80:
##             df['signal'].loc[x]='** Major Sell_Signal'
##             if buy is '9':                
##                df['signal'].loc[x]='///Sell_Signal'
##                buy = '3'
##                print(x, "*** === sell ",df['Close'].loc[x],'   points: ',df['Close'].loc[x]-m33,'   m33',m33,' \n')
##             

        
            
        if df['Close'].loc[x]-m33 > 80 and\
           (df['MOM'].loc[x])  < 5 or df['Close_1d_ch'].loc[x] < -60 and\
           (df['EMA_3'].loc[x]) < 0 and\
           (df['Close_1d_ch'].loc[x])  < -40:
             df['signal'].loc[x]='** Major Sell_Signal'
                 
             df['signal'].loc[x]='///Sell_Signal'
             print("sell ---->",)
             print(x, "*** === sell ",df['Close'].loc[x],'   points: ',df['Close'].loc[x]-m33,'   m33',m33,' \n')
             print('close_1day_ch==>  ',df['Close_1d_ch'].loc[x],'  close-m33-->  ',df['Close'].loc[x]-m33,'\n')
             print('MOM: ',df['MOM'].loc[x], 'EMA(3): ',df['EMA_3'].loc[x],' EMA21: ',df['EMA_3'].loc[x])
             print('**********************************************************************************')
             print('\n\n')

##
##        if ((df['MOM'].loc[x])  < 0 and\
##           (df['EMA_3'].loc[x]) > 0 and\
##           (df['Close_1d_ch'].loc[x])  < 0) and\
##           df['HA'].loc[x] < 6 and\
##           df['Close'].loc[x]-m33 > 0:
##            df['signal'].loc[x]='Sell_Signal'
##            if buy is '9':                
##                df['signal'].loc[x]='///Sell_Signal'
##                buy = '3'
##                print(x, "uu=== sell ",df['Close'].loc[x],'   points: ',df['Close'].loc[x]-m33,' \n')
##                

##
##        if (df['MOM'].loc[x])  < 5 or df['Close_1d_ch'].loc[x] < -60 and\
##           (df['EMA_3'].loc[x]) < 0 and\
##           (df['Close_1d_ch'].loc[x])  < 5 and\
##           (df['Close_1d_ch'].shift(1).loc[x])  < 5 and\
##           df['Close'].loc[x]-m33 > 50:
##             df['signal'].loc[x]='** Major Sell_Signal'
##             if buy is '9':                
##                df['signal'].loc[x]='///Sell_Signal'
##                buy = '3'
##                print(x, "*** === sell ",df['Close'].loc[x],'   points: ',df['Close'].loc[x]-m33,'   m33',m33,' \n')
             
#######################################################################

##        if (df['Close_1d_ch'].loc[x])  > 17:
##            df['signal'].loc[x]='**Buy_Signal**' 
            
        
        if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > 5000:
            df['Move->'].loc[x]='**[5K >]** Move UP->'
            df['Move'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]


        if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > 3000 and (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < 5000:
            df['Move->'].loc[x]='**[3K-5K]** Move UP->'
            df['Move'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]

        if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > 1000 and (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < 3000:
            df['Move->'].loc[x]='[1K-3K] Move UP->'
            df['Move'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]


        if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > 500 and (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < 1000:
            df['Move->'].loc[x]='[500-1K] Move UP->'
            df['Move'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]

        if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > 0 and (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < 500:
            df['Move->'].loc[x]='[0-500] Move UP->'
            df['Move'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]       
            
        
        if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < -5000:
            df['crash->'].loc[x]='** 5K crash-> **'
            df['crash'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]
            df['MSTR->'].loc[x]='MSTR->'
            df['MSTR'].loc[x]=(df['Close'].loc[x]-df['Close'].shift(1).loc[x])/73

        if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < -3000 and (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > -5000:
            df['crash->'].loc[x]='** [3K-4.9K crash-> **'
            df['crash'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]
            df['MSTR->'].loc[x]='MSTR->'
            df['MSTR'].loc[x]=(df['Close'].loc[x]-df['Close'].shift(1).loc[x])/73


        if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < -1000 and (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > -3000:
            df['crash->'].loc[x]='[1K-3K] Dwn->'
            df['crash'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]
            df['MSTR->'].loc[x]='MSTR->'
            df['MSTR'].loc[x]=(df['Close'].loc[x]-df['Close'].shift(1).loc[x])/73


        if (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) < 0 and (df['Close'].loc[x]-df['Close'].shift(1).loc[x]) > -1000:
            df['crash->'].loc[x]='[0-1K] Dwn->'
            df['crash'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]
            df['MSTR->'].loc[x]='MSTR->'
            df['MSTR'].loc[x]=(df['Close'].loc[x]-df['Close'].shift(1).loc[x])/73    






    ##ddd=(df['Volume']-df['Volume'].shift(1))
    tt=pd.concat([df['ff'],df['MOM->'],df['MOM'],df['direct'],df['HA'],df['Close'],df['Close_d_ch'],df['Volume'],
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
                  df['crash->'],df['crash'],df['MSTR->'],df['MSTR'],df['Move->'],df['Move'],
                  df['signal'],df['signal->']
                  ],axis=1)

##    print(tt.tail(4))
    print('tt-columns:',tt.columns)
    
##    sys.exit()
##    tt.columns=['MOM->','MOM','direct', 'HA', 'Close', 'Close_d_ch', 'Volume', 'Volumea', 'CCI', 'DX',
##       'WILLR', 'RSI', 'adx', 'WilliamsR', 'ATR', 'ULTOSC', 'ROC', 'PLUS_DI',
##       'PLUS_DM', 'HT_DCPERIOD', 'HT_DCPHASE', 'sine', 'leadsine', 'aroondown',
##       'aroonup', 'macd', 'macdsignal', 'macdhist', 'PLUS_DI', 'PLUS_DM',
##       'PPO', 'ROC', 'ROCP', 'ROCR', 'ROCR100', '*', 'CDLDOJI', 'CDLDOJISTAR',
##       'CDLDRAGONFLYDOJI', 'CDLEVENINGDOJISTAR', 'CDLGRAVESTONEDOJI',
##       'CDLHAMMER', 'CDLXSIDEGAP3METHODS', '*', 'EMA_3', 'EMA_5', 'EMA_10',
##       'EMA_21', 'EMA_50', 'EMA_100', 'EMA_200', 'EMA_3s', 'EMA_5s', 'EMA_10s',
##       'EMA_21s', 'EMA_50s', 'EMA_100s', 'EMA_200s','ticker' ,'intervl','Close_d','compare_d','Close_1d_ch','Close_3d_ch','Close_5d_ch','Close_30d_ch',
##                'swng','MA->','CCI/RSI->','Close->','HA->',
##                'crash->','crash','MSTR->','MSTR','Move->','Move','signal','signal->'
##                ]

    tt.reset_index(inplace=True)        
    for x in tt.index:
    ##    print(tt['Volume'])
    ##    tt['Volume'].loc[x]=numerize.numerize(tt['Volume'].loc[x])
    ##    tt['Volume'].loc[x]=numerize.numerize((tt['Volume'].iloc[x][1]))
        tt['Volume'].loc[x]=numerize.numerize(np.float32(tt['Volume'].loc[x]).item())
    tt.set_index('Datetime')

    print('\n',tt.columns,'\n')
    print('uuuuu')

    print('stupid stupid azhar ',tt.columns.get_loc('Close_d_ch'))
    print('stupid stupid azhar ',tt.columns.get_loc('Close_1d_ch'))
##    print('stupid stupid azhar ',tt.columns.get_loc('MOM'))
##    print('stupid stupid azhar ',tt.columns.get_loc('*'))
##    print('stupid stupid azhar ',tt.columns.get_loc('signal->'))
##    print('stupid stupid azhar ',tt.columns.get_loc('signal'))
##    print('stupid stupid azhar ',tt.columns.get_loc('HA'))
##    print('stupid stupid azhar ',tt.columns.get_loc('direct'))
##    print('stupid stupid azhar ',tt.columns.get_loc('*'))
##    print('stupid stupid azhar ',tt.columns.get_loc('direct'))
##    print('stupid stupid azhar ',tt.columns.get_loc('HA'))
##    print('stupid stupid azhar ',tt.columns.get_loc('*'))
##    print('stupid stupid azhar ',tt.columns.get_loc('macd'))
##    print('stupid stupid azhar ',tt.columns.get_loc('EMA_3'))
##    print('stupid stupid azhar ',tt.columns.get_loc('*'))
##    print('stupid stupid azhar ',tt.columns.get_loc('crash->'))
##    print('stupid stupid azhar ',tt.columns.get_loc('crash'))
##    print('stupid stupid azhar ',tt.columns.get_loc('Move->'))
##    print('stupid stupid azhar ',tt.columns.get_loc('Move'))
    
##    print('stupid stupid azhar ',tt.columns.get_loc('PPO'))
##    print('stupid stupid azhar ',tt.columns.get_loc('ROC'))
##    print('stupid stupid azhar ',tt.columns.get_loc('ROCP'))
##    print('stupid stupid azhar ',tt.columns.get_loc('ROCR'))
##    print('stupid stupid azhar ',tt.columns.get_loc('ROCR100'))
##    
##    print('stupid stupid azhar ',tt.columns.get_loc('DX'))
##    print('stupid stupid azhar ',tt.columns.get_loc('WILLR'))
##    print('stupid stupid azhar ',tt.columns.get_loc('adx'))
##    print('stupid stupid azhar ',tt.columns.get_loc('ATR'))
##    print('stupid stupid azhar ',tt.columns.get_loc('ULTOSC'))
##    print('stupid stupid azhar ',tt.columns.get_loc('ROC'))
##
##    print('stupid stupid azhar ',tt.columns.get_loc('PLUS_DI'))
##    print('stupid stupid azhar ',tt.columns.get_loc('PLUS_DM'))
##    print('stupid stupid azhar ',tt.columns.get_loc('aroondown'))
##    print('stupid stupid azhar ',tt.columns.get_loc('aroonup'))

##    print('all --> ',tt)
    gg33=tt.iloc[:,[0,3,27,46,6,64,80,79,5,4,73,74,77,78]]
##    gg33=tt.iloc[:,[24,25,26,29,31,32,33,8,9,11,13,14,
##                    35,36,37,38,39,40,41,77,76,68,3,61,78,43,46,1,2,70,71,72,73,74,75,57,0,58,60,3,59,65,4,61,62,63,64,4,68,3,61,69,1,2,67,7,10,66,43,44,45,46,47,48,49]].tail(335)
    gg33a=pd.DataFrame(gg33)
    print('\n','Close_delta_price_by_'+str(shiftbydays)+' days','\n',gg33)
    gg33a.to_csv("/home/az2/Downloads/44/output_57g.csv")
    
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
