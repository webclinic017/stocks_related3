import yfinance as yf
import pandas as pd
import talib as taa
import finta as f
from numerize import numerize
##import pandas_ta as ta2

import pandas_ta as ta
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
from matplotlib.axis import Axis
from matplotlib.widgets import Slider, Button, RadioButtons 
import numpy as np    
import sys
import warnings

warnings.filterwarnings("ignore")


pd.options.display.float_format = '{:.2f}'.format
pd.options.display.max_columns = 255
pd.options.display.max_rows = 6500000

##pd.options.display.max_rows = 999999
pd.options.display.max_columns = 76
pd.set_option("display.max_columns", 200)
pd.set_option('display.width', 1000)
pd.set_option('display.expand_frame_repr', False)


pd.options.display.float_format = '{:.2f}'.format
pd.options.display.max_columns = 255
pd.options.display.max_rows = 6500000

##pd.options.display.max_rows =999999 
##pd.options.display.max_columns = 36
pd.set_option("display.max_columns", 100)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 200)
pd.set_option('display.max_columns', 0)
pd.set_option('display.max_columns', None)
pd.set_option("expand_frame_repr", True)

m=['spy','msft','tsla','docu','mrna']
b=15
k=4
for xs in m:
    
    df = yf.download(xs,period='1d',interval='1m')


    ##df['p2']=ta.adx(df
    st = ta.supertrend(df['High'], df['Low'], df['Close'], 7, 3)
    v = df['Volume'].values
    tp = (df['Low'] + df['Close'] + df['High']).div(3).values
    df = df.assign(vwap=(tp * v).cumsum() / v.cumsum())

    df['macd'], df['macdsignal'], df['macdhist'] = taa.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    df['AD'] = taa.ADOSC(df['High'], df['Low'], df['Close'], df['Volume'])
    df['adx'] = taa.ADX(df['High'], df['Low'], df['Close'], timeperiod=14)
    df['ADL']=f.TA.ADL(df)/100000
    df['ATR'] = taa.ATR(df['High'], df['Low'], df['Close'], timeperiod=14)
    df['VZO']=f.TA.VZO(df,14)
    df['EMA_3'] = taa.EMA(df['Close'], timeperiod=3)
    df['EMA_5'] = taa.EMA(df['Close'], timeperiod=5)
    df['EMA_10'] = taa.EMA(df['Close'], timeperiod=10)
    df['EMA_21'] = taa.EMA(df['Close'], timeperiod=21)
    df['EMA_50'] = taa.EMA(df['Close'], timeperiod=50)
    df['EMA_100'] = taa.EMA(df['Close'], timeperiod=100)
    df['MOM'] = taa.MOM(df['Close'], timeperiod=14)
    df['EMA_200'] = taa.EMA(df['Close'], timeperiod=200)
    df['EMA_200_vwap'] = df['EMA_200'] - df['vwap']

    df['EMA-35'] = df['EMA_3'] - df['EMA_5']
    df['EMA-510'] = df['EMA_5'] - df['EMA_10']
    df['EMA-1021'] = df['EMA_10'] - df['EMA_21']
    df['EMA-2150'] = df['EMA_21'] - df['EMA_50']


    df['EMA_3_vwap'] = df['EMA_3'] - df['vwap']
    df['EMA_5_vwap'] = df['EMA_5'] - df['vwap']
    df['EMA_10_vwap'] = df['EMA_10'] - df['vwap']
    df['EMA_21_vwap'] = df['EMA_21'] - df['vwap']
    df['EMA_50_vwap'] = df['EMA_50'] - df['vwap']
    df['EMA_100_vwap'] = df['EMA_100'] - df['vwap']

    df['Close_EMA3'] = df['Close'] - df['EMA_3']
    df['Close_EMA5'] = df['Close'] - df['EMA_5']
    df['Close_EMA10'] = df['Close'] - df['EMA_10']
    df['Close_EMA21'] = df['Close'] - df['EMA_21']
    df['Close_EMA50'] = df['Close'] - df['EMA_50']

    df['SAR'] = taa.SAR(df['High'], df['Low'], acceleration=300, maximum=5)
    df['SARx'] = df['Close'] - df['SAR']

    ## squeeze info
    df['20sma'] = df['Close'].rolling(window=20).mean()
    df['stddev'] = df['Close'].rolling(window=20).std()
    df['lower_band'] = df['20sma'] - (2 * df['stddev'])
    df['upper_band'] = df['20sma'] + (2 * df['stddev'])
    df['lower_keltner'] = df['20sma'] - (df['ATR'] * 1.5)
    df['upper_keltner'] = df['20sma'] + (df['ATR'] * 1.5)

    df['Boling_upper2'], df['Boling__middle2'], df['Boling_lower2'] = taa.BBANDS(df['Low'], timeperiod=20, nbdevup=2, nbdevdn=2)

    df['Close_vwap'] = df['Close'] - df['vwap']
    ##stt=ta.supertrend(df['High'], df['Low'], df['Close'], 7, 3)
    df['p2']=st.iloc[:,1]
    ##print(stt.columns)
    ##print(df)



    df['squeeze_on']=''
    p=0


    ##df.set_index(df['Datetime'],inplace=True)
    df.reset_index(inplace=True)
    df['s3']=''
    df['s2']=''
    df['i']=0
    i=0
    df['Close_vwap_up']=''





    for x in df.index:
        
        ######################## squeeze 55

        if df['lower_band'].loc[x] > df['lower_keltner'].loc[x] and df['upper_band'].loc[x] < df['upper_keltner'].loc[x]:
            
            df['squeeze_on'].loc[x]='in_squeeze'
            p=p+1
    ##                print(x,"  in 1 min Squeeze, ATR=",dfq['ATR'].loc[z])
        else:
            df['squeeze_on'].loc[x]=' '

    bb=df.columns.get_loc('s2')


    print(help(ta.adx))
    df['chop']=ta.trend.chop(df['High'], df['Low'], df['Close'], length=14, atr_length=None, scalar=100, drift=1, offset=None)

    ##print(df[['Close','p2','chop','macd','adx','ADL','ATR','VZO','Close_vwap',\
    ##          'EMA-35','EMA-510','EMA-1021','EMA-2150',\
    ##          'EMA_3_vwap','EMA_5_vwap','EMA_10_vwap','EMA_21_vwap','EMA_50_vwap','EMA_100_vwap',\
    ##          'Close_EMA3','Close_EMA5','Close_EMA10','Close_EMA21','Close_EMA50',\
    ##          'squeeze_on'
    ##          
    ##          ]])

    ##print(df.iloc[2,df.columns.get_loc('ticker')],'  ddddddddddddddddddddd')

    print(df,'5555')
    print('\n')
    b6=0
    s7=0

    ############# Buy condition for Uptrend ########################
    for x in df.index:
        df['i'].loc[x]=i
        df['s3'].loc[x]=str(df['Datetime'].loc[x]).split(' ')[0]
        df['s2'].loc[x]=str(df['Datetime'].loc[x]).split(' ')[1][0:5]

        if (df['Close_vwap'].loc[x] > 0) and (df['Close_vwap'].shift(1).loc[x] < 0) and \
           (df['EMA_3_vwap'].loc[x] > 0) and \
           (df['EMA_5_vwap'].loc[x] > 0) and \
           (df['EMA-2150'].loc[x] > -.50):
    ##       (df['EMA_10_vwap'].loc[x] > 0):
    ##       (df['EMA_21_vwap'].loc[x] > 0):
    ##       df['adx'].loc[x] > 20 :

        
    ##    if df['Close'].loc[x] > df['vwap'].loc[x]  and df['Close'].shift(1).loc[x] < df['vwap'].shift(1).loc[x]\
    ##       and df['adx'].loc[x] > 20:

        
    ##    if df['Close'].loc[x] > df['vwap'].loc[x]  and df['Close'].shift(1).loc[x] < df['vwap'].shift(1).loc[x]\
    ##       and df['Close'].shift(2).loc[x] < df['vwap'].shift(2).loc[x] and\
    ##       df['Close'].shift(3).loc[x] < df['vwap'].shift(3).loc[x]:
    ##        
    ##       df['MOM'].loc[x] > 0 and (df['MOM'].loc[x]-df['MOM'].shift(1).loc[x]) > 0 and\
    ##       df['ADL'].loc[x] > 0
    ##    :
    ##       df['adx'].loc[x] > 10 and df['adx'].shift(1).loc[x] < 0

            buy_price_gg=df['Close'].loc[x]
            b=df['adx'].loc[x]
            b6=x



    sell_price_gg=0
    ############# Sell condition for uptrend ########################
    for z in range(b6,df.shape[0]):
        if df['Close'].loc[z] - buy_price_gg > 2.5:
    ##    if (df['Close'].loc[z] < df['vwap'].loc[z] or\
    ##       df['ADL'].loc[z] < 0) or (df['Close'].loc[z] < df['Close'].loc[b6]) or \
    ##       df['MOM'].loc[z] < df['MOM'].shift(1).loc[z]\
    ##       :
            sell_price_gg=df['Close'].loc[z]
            
            s7=z
    ##    else:
    ##        s7=''
    ##        print("nnnnn")
    ##print(df.iloc[2,df.columns.get_loc('ticker')])
    #####################################################
    ##print(m[k],' uptrend',buy_price_ggb)
    ##print('\n\n\n')
            
    if sell_price_gg > 0 and sell_price_gg > buy_price_gg:
        print(m,'  ','profit/uptrend=',round(sell_price_gg-buy_price_gg),'  ',m[k])
    elif sell_price_gg < buy_price_gg:
        print(m,'  ','Loss/uptrend=',round(sell_price_gg-buy_price_gg),'  ',m[k])
    ##print('b6=',buy_price_gg,'  s7=',sell_price_gg)
    print('buy_price=',round(buy_price_gg,2),' sell_price=',round(sell_price_gg,2))
    print('b6 index=',b6,'   s7 index=',s7)

    ## $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    ## $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


    print('\n\n ------------------------------------------------------------------------------------')
    buy_price_ggb=0
    sell_price_ggb=0
    b6=0
    s7=0
                                     ## Downtrend
    ############# Buy condition for Dwntrend ########################
    for x in df.index:
        df['i'].loc[x]=i
        df['s3'].loc[x]=str(df['Datetime'].loc[x]).split(' ')[0]
        df['s2'].loc[x]=str(df['Datetime'].loc[x]).split(' ')[1][0:5]
        if df['Close'].loc[x]-df['vwap'].loc[x] < 0 and df['Close'].shift(1).loc[x] > df['vwap'].shift(1).loc[x]:
    ##        and\
    ##       df['ADL'].loc[x] < 0:
            
           
    ##       df['MOM'].loc[x] < 0 and (df['MOM'].loc[x]-df['MOM'].shift(1).loc[x]) < 0 and\
           
               
    ##       df['adx'].loc[x] > 17 and df['adx'].shift(1).loc[x] - (df['adx'].loc[x] > 1)\
        
            buy_price_gg=df['Close'].loc[x]
            b6=x
    #####################################################

    ############# Sell condition for Dwntrend ########################
    for z in range(b6,df.shape[0]):        
    ##    if (df['Close'].loc[b6] < df['Close'].loc[z]  or df['Close'].loc[z]-df['vwap'].loc[z] > 0 and\
    ##        df['Close'].shift(1).loc[z]-df['vwap'].shift(1).loc[z] < 0\
    ##       and df['ADL'].loc[z] > 0):

        if (df['Close'].loc[b6] < df['Close'].loc[z]  or df['Close'].loc[z]>df['vwap'].loc[z]  or\
           df['ADL'].loc[z] > 0) or df['MOM'].loc[z] > df['MOM'].shift(1).loc[z]:    



            
            sell_price_gg=df['Close'].loc[z]
            s7=z
    ##    else:
    ##        s7=''
    ##        print("nnnnn")
    ##print(df.iloc[2,df.columns.get_loc('ticker')])
    #####################################################
    print(m[k],' downtrend',buy_price_gg)
    print('------------------------------------------------------------------------')
    print('\n')
    if buy_price_gg > sell_price_gg :
        print(m,'  ',' 55 profit/downtrend=',round(buy_price_gg-sell_price_gg),'  ',m[k])
        print(df['s2'].loc[b6],' / ',df['s2'].loc[s7],'adx',df['adx'].loc[b6])
    elif buy_price_gg < sell_price_gg:
        print(m,'  ','Loss/downtrend=',round(buy_price_gg-sell_price_gg),'  ',m[k])
        print(df['s2'].loc[b6],' / ',df['s2'].loc[s7],'adx',df['adx'].loc[b6])


    ##print('b6=',buy_price_gg,'  s7=',sell_price_gg)
    print('buy_price=',round(buy_price_gg,2),' sell_price=',round(sell_price_gg,2))
    print('b6 index=',b6,'   s7 index=',s7)






























