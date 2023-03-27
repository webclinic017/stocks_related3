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
##pd.options.display.max_columns = 36  ,'spy','msft','tsla','docu','mrna'
pd.set_option("display.max_columns", 100)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 200)
pd.set_option('display.max_columns', 0)
pd.set_option('display.max_columns', None)
pd.set_option("expand_frame_repr", True)


##fg=open('/home/az2/66.txt','w+')
file_path = '/home/az2/66.txt'
sys.stdout = open(file_path, "w")


def inputs(df):
    buy_condition=(df['ADL'].loc[x] > 0) 
##    fg.write(buy_condition)
    return(buy_condition)


def inputs2(df):
    sell_condition=(df['ADL'].loc[z] < 0)
##    fg.write(sell_condition)
    return(sell_condition)

m=['mrna']

##m=['tsla','psa','meli','skin','shop']
b=15
k=4
for xs in m:
    
    df = yf.download(xs,period='1d',interval='1m')
    df['ticker']=xs

    ##df['p2']=ta.adx(df
    st = ta.supertrend(df['High'], df['Low'], df['Close'], 7, 3)
    v = df['Volume'].values
    tp = (df['Low'] + df['Close'] + df['High']).div(3).values
    df = df.assign(vwap=(tp * v).cumsum() / v.cumsum())

    df['macd'], df['macdsignal'], df['macdhist'] = taa.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    df['AD'] = taa.ADOSC(df['High'], df['Low'], df['Close'], df['Volume'])
    df['adx'] = taa.ADX(df['High'], df['Low'], df['Close'], timeperiod=14)
    df['ADL']=f.TA.ADL(df)/100000
    df['RSI']= taa.RSI(df['Close'], timeperiod=14)
    df['STOCHRSI_fastk'], df['STOCHRSI_fastd'] = taa.STOCHRSI(df['Close'], timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
    
    df['Boling_upper'], df['Boling_middle'], df['Boling_lower'] = taa.BBANDS(df['Close'], timeperiod=10, nbdevup=2, nbdevdn=2)

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
##    print(df.columns)
##    
##    print(df,'5555')
    print('\n')
    b6=0
    s7=0
    buy_price_gg=0
    pg5=0
    print(buy_price_gg)
 
    ############# Buy condition for Uptrend ########################
    for x in df.index:
##        df['i'].loc[x]=i
        df['s3'].loc[x]=str(df['Datetime'].loc[x]).split(' ')[0]
        df['s2'].loc[x]=str(df['Datetime'].loc[x]).split(' ')[1][0:5]


##        buy_condition=(df['ADL'].loc[x] > 0)
        buy_condition=inputs(df)



        if buy_condition:
##
##        if (df['macd'].loc[x] > 0) and (df['Close_vwap'].loc[x] > 0) and (df['Close_vwap'].shift(1).loc[x] < 0)\
##           and (df['ADL'].loc[x] > 0):
##            or \
##           (df['EMA-2150'].loc[x] > 0) or (df['EMA-35'].loc[x] > 0) and (df['EMA-510'].loc[x] > 0) or\
##           (df['EMA-1021'].loc[x] > 0) :

##           (df['EMA_3_vwap'].loc[x] > 0):
##           (df['EMA_5_vwap'].loc[x] > 0) and \
##           (df['EMA-2150'].loc[x] > 0):
##            (df['Close_vwap'].loc[x] > 0) and (df['Close_vwap'].shift(1).loc[x] < 0) and \
            
            pg5=df['Close_vwap'].loc[x]+df['EMA_3_vwap'].loc[x]+df['EMA_5_vwap'].loc[x]+df['EMA-2150'].loc[x]

            buy_price_gg = df['Close'].loc[x]
            sell_price_gg = 0
            
            b=df['adx'].loc[x]
            b6=x
            break

        elif x==df.shape[0] and buy_price_gg==0:
            buy_price_gg = 0


##    print(buy_price_gg,' n  ',pg5)
##    sys.exit()            


    sell_price_gg = 0
    print(buy_price_gg)


    ############# Sell condition for uptrend ########################
    for z in range(b6,df.shape[0],1):
##        if df['Close'].loc[z] - buy_price_gg > 0:

##        if (df['Close'].loc[b6] < df['Close'].loc[z]  or df['Close'].loc[z]<df['vwap'].loc[z]  or\
##               df['ADL'].loc[z] < 0) or (df['MOM'].loc[z] < df['MOM'].shift(1).loc[z] and df['MOM'].shift(1).loc[z]< df['MOM'].shift(2).loc[z]):


        sell_condition=inputs2(df)
        
        if  sell_condition:

##        if df['Close'].loc[z] - buy_price_gg > 0 or (df['ADL'].loc[x] < 0) and df['macd'].loc[z] < 0 or \
##           (df['EMA-35'].loc[z] < 0 and df['EMA-510'].loc[z] < 0)  or\
##           (df['EMA-1021'].loc[z] < 0) :
            
##(df['macd'].loc[z] < 0) or (df['Close_vwap'].loc[z] < 0) or (df['Close_vwap'].shift(1).loc[z] < 0\
##           or df['EMA-2150'].loc[z] < 0)\
##
##           
            sell_price_gg=df['Close'].loc[z]
            
            s7=z
    if  buy_price_gg == 0:
        sell_price_gg == 0
        print(m)
        print(xs,' == NOTREND ==','  5 ')


                
    if sell_price_gg > 0 and sell_price_gg > buy_price_gg and buy_price_gg != 0:
        print(m)
        print(xs,'   UPTREND','  5 ',pg5)
        print('\n')
        print('71 profit/uptrend [sell-buy] =',round((sell_price_gg - buy_price_gg),2),'   ',sell_price_gg,'   ',buy_price_gg)
        print('71 profit/uptrend [sell-buy] ===========================================================> ',round((sell_price_gg - buy_price_gg),2),'  ',xs)
        print('\n')
        print('Close[buy/sell]',round(df['Close'].loc[b6],2),'/',round(df['Close'].loc[s7],2))
        
        print(df['s2'].loc[b6],' / ',df['s2'].loc[s7])
        print('adx',round(df['adx'].loc[b6],1),'/',round(df['adx'].loc[s7],1))
        print('vzo ',round(df['VZO'].loc[b6],1),' / ',round(df['VZO'].loc[s7],1),'    ','CCI ')
        print('ADL ',round(df['ADL'].loc[b6],1),' / ',round(df['ADL'].loc[s7],1),'    ','MOM ',round(df['MOM'].loc[b6],1),'/',round(df['MOM'].loc[s7],1))
        print('AD ',round(df['AD'].loc[b6],1),' / ',round(df['AD'].loc[s7],1),'    ','macd ',round(df['macd'].loc[b6],1),'/',round(df['macd'].loc[s7],1))



        print('\n')  
        if  round(df['Boling_middle'].loc[b6],1) < round(df['Close'].loc[b6],1) < round(df['Boling_upper'].loc[b6],1):
            print('buy [Boling_upper < close < Boling_middle] ',\
                  round(df['Boling_upper'].loc[b6],1),' < ',round(df['Close'].loc[b6],1),\
                  ' < ',round(df['Boling_middle'].loc[b6],1))
        if round(df['Boling_lower'].loc[b6],1) < round(df['Close'].loc[b6],1) < round(df['Boling_middle'].loc[b6],1):
            print('buy [Boling_middle < close < Boling_lower] ',round(df['Boling_middle'].loc[b6],1),' < ',round(df['Close'].loc[b6],1),' < ',round(df['Boling_lower'].loc[b6],1))
        if round(df['Boling_upper'].loc[b6],1) == round(df['Close'].loc[b6],1):
            print('buy [Boling_upper = close] ',round(df['Boling_upper'].loc[b6],1),' = ',round(df['Close'].loc[b6],1))
        if round(df['Boling_lower'].loc[b6],1) == round(df['Close'].loc[b6],1):          
            print('buy [Boling_lower = close] ',round(df['Boling_lower'].loc[b6],1),' = ',round(df['Close'].loc[b6],1))
        if round(df['Close'].loc[b6],1) > df['Boling_upper'].loc[b6]:
            print('buy [close  > Boling_upper] ',round(df['Close'].loc[b6],1) > round(df['Boling_upper'].loc[b6],1))         
        if round(df['Close'].loc[b6],1) < df['Boling_lower'].loc[b6]:
            print('buy [close  < Boling_lower] ',round(df['Close'].loc[b6],1),' < ',round(df['Boling_lower'].loc[b6],1))    

##        print('\n')
##        print('77777777777',df['Boling_upper'].loc[s7],'  ',round(df['Close'].loc[s7],1),'  ',round(df['Boling_middle'].loc[s7],1))
        if  round(df['Boling_middle'].loc[s7],1) < round(df['Close'].loc[s7],1) < round(df['Boling_upper'].loc[s7],1):
            print('sell [Boling_upper < close < Boling_middle] ',\
                  round(df['Boling_upper'].loc[s7],1),' < ',round(df['Close'].loc[s7],1),\
                  ' < ',round(df['Boling_middle'].loc[s7],1))
        elif round(df['Boling_lower'].loc[s7],1) < round(df['Close'].loc[s7],1) < round(df['Boling_middle'].loc[s7],1):
            print('sell [Boling_middle < close < Boling_lower] ',round(df['Boling_middle'].loc[s7],1),' < ',round(df['Close'].loc[s7],1),' < ',round(df['Boling_lower'].loc[s7],1))

        elif round(df['Boling_upper'].loc[s7],1) == round(df['Close'].loc[s7],1):
            print('sell [Boling_upper = close] ',round(df['Boling_upper'].loc[s7],1),' = ',round(df['Close'].loc[s7],1))
        elif round(df['Boling_lower'].loc[s7],1) == round(df['Close'].loc[s7],1):          
            print('sell [Boling_lower = close] ',round(df['Boling_lower'].loc[s7],1),' = ',round(df['Close'].loc[s7],1))
        elif round(df['Close'].loc[s7],1) > df['Boling_upper'].loc[s7]:
            print('sell [close  > Boling_upper] ',round(df['Close'].loc[s7],1) > round(df['Boling_upper'].loc[s7],1))         
        elif round(df['Close'].loc[s7],1) < df['Boling_lower'].loc[s7]:
            print('sell [close  < Boling_lower] ',round(df['Close'].loc[s7],1),' < ',round(df['Boling_lower'].loc[s7],1)) 
        print('\n') 



    elif sell_price_gg < buy_price_gg and sell_price_gg > 0:
        print(m)
        print(xs,'   UPTREND',' 6  ',pg5)
        print('72 Loss/uptrend [sell-buy] =',round((sell_price_gg - buy_price_gg),2),'   ',sell_price_gg,'   ',buy_price_gg)
        print('72 profit/uptrend [sell-buy] =============================================================================> ',\
              round((sell_price_gg - buy_price_gg),2),'  ',xs)
        print('Close[buy/sell]',round(df['Close'].loc[b6],2),'/',round(df['Close'].loc[s7],2))
        print(df['s2'].loc[b6],' / ',df['s2'].loc[s7])
        print('adx',round(df['adx'].loc[b6],1),'/',round(df['adx'].loc[s7],1))
        print('vzo ',round(df['VZO'].loc[b6],1),' / ',round(df['VZO'].loc[s7],1),'    ','CCI ')
        print('ADL ',round(df['ADL'].loc[b6],1),' / ',round(df['ADL'].loc[s7],1),'    ','MOM ',round(df['MOM'].loc[b6],1),'/',round(df['MOM'].loc[s7],1))
        print('AD ',round(df['AD'].loc[b6],1),' / ',round(df['AD'].loc[s7],1),'    ','macd ',round(df['macd'].loc[b6],1),'/',round(df['macd'].loc[s7],1))

        print('\n')  
        if  round(df['Boling_middle'].loc[b6],1) < round(df['Close'].loc[b6],1) < round(df['Boling_upper'].loc[b6],1):
            print('buy [Boling_upper < close < Boling_middle] ',\
                  round(df['Boling_upper'].loc[b6],1),' < ',round(df['Close'].loc[b6],1),\
                  ' < ',round(df['Boling_middle'].loc[b6],1))
        if round(df['Boling_lower'].loc[b6],1) < round(df['Close'].loc[b6],1) < round(df['Boling_middle'].loc[b6],1):
            print('buy [Boling_middle < close < Boling_lower] ',round(df['Boling_middle'].loc[b6],1),' < ',round(df['Close'].loc[b6],1),' < ',round(df['Boling_lower'].loc[b6],1))
        if round(df['Boling_upper'].loc[b6],1) == round(df['Close'].loc[b6],1):
            print('buy [Boling_upper = close] ',round(df['Boling_upper'].loc[b6],1),' = ',round(df['Close'].loc[b6],1))
        if round(df['Boling_lower'].loc[b6],1) == round(df['Close'].loc[b6],1):          
            print('buy [Boling_lower = close] ',round(df['Boling_lower'].loc[b6],1),' = ',round(df['Close'].loc[b6],1))
        if round(df['Close'].loc[b6],1) > df['Boling_upper'].loc[b6]:
            print('buy [close  > Boling_upper] ',round(df['Close'].loc[b6],1) > round(df['Boling_upper'].loc[b6],1))         
        if round(df['Close'].loc[b6],1) < df['Boling_lower'].loc[b6]:
            print('buy [close  < Boling_lower] ',round(df['Close'].loc[b6],1),' < ',round(df['Boling_lower'].loc[b6],1))    

##        print('\n')
##        print('77777777777',df['Boling_upper'].loc[s7],'  ',round(df['Close'].loc[s7],1),'  ',round(df['Boling_middle'].loc[s7],1))
        if  round(df['Boling_middle'].loc[s7],1) < round(df['Close'].loc[s7],1) < round(df['Boling_upper'].loc[s7],1):
            print('sell [Boling_upper < close < Boling_middle] ',\
                  round(df['Boling_upper'].loc[s7],1),' < ',round(df['Close'].loc[s7],1),\
                  ' < ',round(df['Boling_middle'].loc[s7],1))
        elif round(df['Boling_lower'].loc[s7],1) < round(df['Close'].loc[s7],1) < round(df['Boling_middle'].loc[s7],1):
            print('sell [Boling_middle < close < Boling_lower] ',round(df['Boling_middle'].loc[s7],1),' < ',round(df['Close'].loc[s7],1),' < ',round(df['Boling_lower'].loc[s7],1))

        elif round(df['Boling_upper'].loc[s7],1) == round(df['Close'].loc[s7],1):
            print('sell [Boling_upper = close] ',round(df['Boling_upper'].loc[s7],1),' = ',round(df['Close'].loc[s7],1))
        elif round(df['Boling_lower'].loc[s7],1) == round(df['Close'].loc[s7],1):          
            print('sell [Boling_lower = close] ',round(df['Boling_lower'].loc[s7],1),' = ',round(df['Close'].loc[s7],1))
        elif round(df['Close'].loc[s7],1) > df['Boling_upper'].loc[s7]:
            print('sell [close  > Boling_upper] ',round(df['Close'].loc[s7],1) > round(df['Boling_upper'].loc[s7],1))         
        elif round(df['Close'].loc[s7],1) < df['Boling_lower'].loc[s7]:
            print('sell [close  < Boling_lower] ',round(df['Close'].loc[s7],1),' < ',round(df['Boling_lower'].loc[s7],1)) 
        print('\n') 

    elif sell_price_gg == 0 or sell_price_gg == ' ' :
        print(m)
        print(xs,'   UPTREND','   ',pg5)
        print('no sell, only buy *********************************************===========================================================')
         
    ##print('b6=',buy_price_gg,'  s7=',sell_price_gg)
    print('buy_price [buy - sell] =',round(buy_price_gg,2),' sell_price=',round(sell_price_gg,2))
    print('b6 index=',b6,'   s7 index=',s7)

    df['profit']=sell_price_gg-buy_price_gg
    print('\n\n')
##    print(df.iloc[s7,[df.columns.get_loc('profit'),df.columns.get_loc('ticker'),df.columns.get_loc('Close'),df.columns.get_loc('macd'),df.columns.get_loc('MOM'),df.columns.get_loc('adx'),\
##                      df.columns.get_loc('Close_vwap'),df.columns.get_loc('AD'),df.columns.get_loc('ADL'),df.columns.get_loc('VZO'),\
##                      df.columns.get_loc('STOCHRSI_fastk'), df.columns.get_loc('RSI'),\
##                      df.columns.get_loc('SAR'), df.columns.get_loc('SARx')\
##                      ,df.columns.get_loc('s3'),df.columns.get_loc('s2'),df.columns.get_loc('Close_EMA3')\
##                      ,df.columns.get_loc('Close_EMA5'),df.columns.get_loc('Close_EMA10')\
##                      ,df.columns.get_loc('Close_EMA21'),df.columns.get_loc('EMA_3_vwap')\
##                      ,df.columns.get_loc('EMA_5_vwap'),df.columns.get_loc('EMA_10_vwap')\
##                      ,df.columns.get_loc('EMA_21_vwap'),df.columns.get_loc('EMA_10_vwap')]],'695')
##
##    print(df.iloc[b6,[df.columns.get_loc('profit'),df.columns.get_loc('ticker'),df.columns.get_loc('Close'),df.columns.get_loc('macd'),df.columns.get_loc('MOM'),df.columns.get_loc('adx'),\
##                      df.columns.get_loc('Close_vwap'),df.columns.get_loc('AD'),df.columns.get_loc('ADL'),df.columns.get_loc('VZO'),\
##                      df.columns.get_loc('STOCHRSI_fastk'), df.columns.get_loc('RSI'),\
##                      df.columns.get_loc('SAR'), df.columns.get_loc('SARx')\
##                      ,df.columns.get_loc('s3'),df.columns.get_loc('s2'),df.columns.get_loc('Close_EMA3')\
##                      ,df.columns.get_loc('Close_EMA5'),df.columns.get_loc('Close_EMA10')\
##                      ,df.columns.get_loc('Close_EMA21'),df.columns.get_loc('EMA_3_vwap')\
##                      ,df.columns.get_loc('EMA_5_vwap'),df.columns.get_loc('EMA_10_vwap')\
##                      ,df.columns.get_loc('EMA_21_vwap'),df.columns.get_loc('EMA_10_vwap')]],'695')

    dfp=df.iloc[s7,[df.columns.get_loc('profit'),df.columns.get_loc('ticker'),df.columns.get_loc('Close'),df.columns.get_loc('macd'),df.columns.get_loc('MOM'),df.columns.get_loc('adx'),\
                      df.columns.get_loc('Close_vwap'),df.columns.get_loc('AD'),df.columns.get_loc('ADL'),df.columns.get_loc('VZO'),\
                      df.columns.get_loc('STOCHRSI_fastk'), df.columns.get_loc('RSI'),\
                      df.columns.get_loc('SAR'), df.columns.get_loc('SARx')\
                      ,df.columns.get_loc('s3'),df.columns.get_loc('s2'),df.columns.get_loc('Close_EMA3')\
                      ,df.columns.get_loc('Close_EMA5'),df.columns.get_loc('Close_EMA10')\
                      ,df.columns.get_loc('Close_EMA21'),df.columns.get_loc('EMA_3_vwap')\
                      ,df.columns.get_loc('EMA_5_vwap'),df.columns.get_loc('EMA_10_vwap')\
                      ,df.columns.get_loc('EMA_21_vwap'),df.columns.get_loc('EMA_10_vwap')]]

    dfg=df.iloc[b6,[df.columns.get_loc('profit'),df.columns.get_loc('ticker'),df.columns.get_loc('Close'),df.columns.get_loc('macd'),df.columns.get_loc('MOM'),df.columns.get_loc('adx'),\
                      df.columns.get_loc('Close_vwap'),df.columns.get_loc('AD'),df.columns.get_loc('ADL'),df.columns.get_loc('VZO'),\
                      df.columns.get_loc('STOCHRSI_fastk'), df.columns.get_loc('RSI'),\
                      df.columns.get_loc('SAR'), df.columns.get_loc('SARx')\
                      ,df.columns.get_loc('s3'),df.columns.get_loc('s2'),df.columns.get_loc('Close_EMA3')\
                      ,df.columns.get_loc('Close_EMA5'),df.columns.get_loc('Close_EMA10')\
                      ,df.columns.get_loc('Close_EMA21'),df.columns.get_loc('EMA_3_vwap')\
                      ,df.columns.get_loc('EMA_5_vwap'),df.columns.get_loc('EMA_10_vwap')\
                      ,df.columns.get_loc('EMA_21_vwap'),df.columns.get_loc('EMA_10_vwap')]]
    
    gg=pd.concat([dfp,dfg],axis=1)
    print(gg)
    print('\n\n')
    ## $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    ## $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


    print(' ------------------------------------------------------------------------------------')
  
    sell_price_ggb=0
    b6=0
    s7=0

    '''
    
                                     ## Downtrend
    ############# Buy condition for Dwntrend ########################
    for x in df.index:
        df['i'].loc[x]=i
        df['s3'].loc[x]=str(df['Datetime'].loc[x]).split(' ')[0]
        df['s2'].loc[x]=str(df['Datetime'].loc[x]).split(' ')[1][0:5]
        
        if  df['Close'].loc[x]-df['vwap'].loc[x] < 0 and df['Close'].shift(1).loc[x]-df['vwap'].shift(1).loc[x] > 0:
##           df['Close'].loc[x]-df['vwap'].loc[x] < 0 and df['Close'].shift(1).loc[x] > df['vwap'].shift(1).loc[x]:

            pg6=df['Close'].loc[x]-df['vwap'].loc[x] + df['Close'].shift(1).loc[x] - df['vwap'].shift(1).loc[x]
        
            buy_price_gg=df['Close'].loc[x]
            print(df['Close'].loc[x]-df['vwap'].loc[x] < 0 and df['Close'].shift(1).loc[x]-df['vwap'].shift(1).loc[x],'buy --------   > ===========',buy_price_gg)
            b6=x
            break
                
      
    #####################################################
    sell_price_ggb=0
    ############# Sell condition for Dwntrend ########################
    for z in range(b6,df.shape[0]):
        if buy_price_gg > 0:

            if (df['Close'].loc[b6] < df['Close'].loc[z]  or df['Close'].loc[z]>df['vwap'].loc[z]  or\
               df['ADL'].loc[z] > 0) or df['MOM'].loc[z] > df['MOM'].shift(1).loc[z]:    
                
                sell_price_gg=df['Close'].loc[z]
                s7=z

    if  buy_price_gg == 0:
        sell_price_gg == 0
        print(m)
        print(xs,'  === No TREND ===','  ')

    #####################################################
    if buy_price_gg > sell_price_gg and buy_price_gg > 0 and sell_price_gg > 0:
        print(m)
        print(xs,'   DownTREND','  ',pg6)
        print(' 55 profit/downtrend [buy - sell] =',round((buy_price_gg - sell_price_gg),2),'   ',sell_price_gg,'   ',buy_price_gg)
        print(' 55 profit/downtrend [buy - sell] ========================================================> ',round((buy_price_gg - sell_price_gg),2),' ',xs)
        print('Close[buy/sell]',round(df['Close'].loc[b6],2),'/',round(df['Close'].loc[s7],2))
        print(df['s2'].loc[b6],' / ',df['s2'].loc[s7])
        print('adx',round(df['adx'].loc[b6],1),'/',round(df['adx'].loc[s7],1))
        print('vzo ',round(df['VZO'].loc[b6],1),' / ',round(df['VZO'].loc[s7],1),'    ','CCI ')
        print('ADL ',round(df['ADL'].loc[b6],1),' / ',round(df['ADL'].loc[s7],1),'    ','MOM ',round(df['MOM'].loc[b6],1),'/',round(df['MOM'].loc[s7],1))
        print('AD ',round(df['AD'].loc[b6],1),' / ',round(df['AD'].loc[s7],1),'    ','macd ',round(df['macd'].loc[b6],1),'/',round(df['macd'].loc[s7],1))


        print('\n')  
        if  round(df['Boling_middle'].loc[b6],1) < round(df['Close'].loc[b6],1) < round(df['Boling_upper'].loc[b6],1):
            print('buy [Boling_upper < close < Boling_middle] ',\
                  round(df['Boling_upper'].loc[b6],1),' < ',round(df['Close'].loc[b6],1),\
                  ' < ',round(df['Boling_middle'].loc[b6],1))
        if round(df['Boling_lower'].loc[b6],1) < round(df['Close'].loc[b6],1) < round(df['Boling_middle'].loc[b6],1):
            print('buy [Boling_middle < close < Boling_lower] ',round(df['Boling_middle'].loc[b6],1),' < ',round(df['Close'].loc[b6],1),' < ',round(df['Boling_lower'].loc[b6],1))
        if round(df['Boling_upper'].loc[b6],1) == round(df['Close'].loc[b6],1):
            print('buy [Boling_upper = close] ',round(df['Boling_upper'].loc[b6],1),' = ',round(df['Close'].loc[b6],1))
        if round(df['Boling_lower'].loc[b6],1) == round(df['Close'].loc[b6],1):          
            print('buy [Boling_lower = close] ',round(df['Boling_lower'].loc[b6],1),' = ',round(df['Close'].loc[b6],1))
        if round(df['Close'].loc[b6],1) > df['Boling_upper'].loc[b6]:
            print('buy [close  > Boling_upper] ',round(df['Close'].loc[b6],1) > round(df['Boling_upper'].loc[b6],1))         
        if round(df['Close'].loc[b6],1) < df['Boling_lower'].loc[b6]:
            print('buy [close  < Boling_lower] ',round(df['Close'].loc[b6],1),' < ',round(df['Boling_lower'].loc[b6],1))   

##        print('\n')
##        print('77777777777',df['Boling_upper'].loc[s7],'  ',round(df['Close'].loc[s7],1),'  ',round(df['Boling_middle'].loc[s7],1))
        if  round(df['Boling_middle'].loc[s7],1) < round(df['Close'].loc[s7],1) < round(df['Boling_upper'].loc[s7],1):
            print('sell [Boling_upper < close < Boling_middle] ',\
                  round(df['Boling_upper'].loc[s7],1),' < ',round(df['Close'].loc[s7],1),\
                  ' < ',round(df['Boling_middle'].loc[s7],1))
        elif round(df['Boling_lower'].loc[s7],1) < round(df['Close'].loc[s7],1) < round(df['Boling_middle'].loc[s7],1):
            print('sell [Boling_middle < close < Boling_lower] ',round(df['Boling_middle'].loc[s7],1),' < ',round(df['Close'].loc[s7],1),' < ',round(df['Boling_lower'].loc[s7],1))

        elif round(df['Boling_upper'].loc[s7],1) == round(df['Close'].loc[s7],1):
            print('sell [Boling_upper = close] ',round(df['Boling_upper'].loc[s7],1),' = ',round(df['Close'].loc[s7],1))
        elif round(df['Boling_lower'].loc[s7],1) == round(df['Close'].loc[s7],1):          
            print('sell [Boling_lower = close] ',round(df['Boling_lower'].loc[s7],1),' = ',round(df['Close'].loc[s7],1))
        elif round(df['Close'].loc[s7],1) > df['Boling_upper'].loc[s7]:
            print('sell [close  > Boling_upper] ',round(df['Close'].loc[s7],1) > round(df['Boling_upper'].loc[s7],1))         
        elif round(df['Close'].loc[s7],1) < df['Boling_lower'].loc[s7]:
            print('sell [close  < Boling_lower] ',round(df['Close'].loc[s7],1),' < ',round(df['Boling_lower'].loc[s7],1)) 
        print('\n') 


    elif buy_price_gg < sell_price_gg and buy_price_gg > 0 and sell_price_gg > 0:
        print(m)
##        print(xs,'   DownTREND','  ',pg6)
        print(xs,'   DownTREND')
        print('56 Loss/downtrend =',round((buy_price_gg - sell_price_gg),2),'   ',sell_price_gg,'   ',buy_price_gg)
        print('56 Loss/downtrend ===========================================================================>',round((buy_price_gg - sell_price_gg),2),' ',xs)
        print('Close[buy/sell]',round(df['Close'].loc[b6],2),'/',round(df['Close'].loc[s7],2))
        print(df['s2'].loc[b6],' / ',df['s2'].loc[s7])
        print('adx',round(df['adx'].loc[b6],1),'/',round(df['adx'].loc[s7],1))
        print('vzo ',round(df['VZO'].loc[b6],1),' / ',round(df['VZO'].loc[s7],1),'    ','CCI ')
        print('ADL ',round(df['ADL'].loc[b6],1),' / ',round(df['ADL'].loc[s7],1),'    ','MOM ',round(df['MOM'].loc[b6],1),'/',round(df['MOM'].loc[s7],1))
        print('AD ',round(df['AD'].loc[b6],1),' / ',round(df['AD'].loc[s7],1),'    ','macd ',round(df['macd'].loc[b6],1),'/',round(df['macd'].loc[s7],1))

        print('\n') 
        if  round(df['Boling_middle'].loc[b6],1) < round(df['Close'].loc[b6],1) < round(df['Boling_upper'].loc[b6],1):
            print('buy [Boling_upper < close < Boling_middle] ',\
                  round(df['Boling_upper'].loc[b6],1),' < ',round(df['Close'].loc[b6],1),\
                  ' < ',round(df['Boling_middle'].loc[b6],1))
        if round(df['Boling_lower'].loc[b6],1) < round(df['Close'].loc[b6],1) < round(df['Boling_middle'].loc[b6],1):
            print('buy [Boling_middle < close < Boling_lower] ',round(df['Boling_middle'].loc[b6],1),' < ',round(df['Close'].loc[b6],1),' < ',round(df['Boling_lower'].loc[b6],1))
        if round(df['Boling_upper'].loc[b6],1) == round(df['Close'].loc[b6],1):
            print('buy [Boling_upper = close] ',round(df['Boling_upper'].loc[b6],1),' = ',round(df['Close'].loc[b6],1))
        if round(df['Boling_lower'].loc[b6],1) == round(df['Close'].loc[b6],1):          
            print('buy [Boling_lower = close] ',round(df['Boling_lower'].loc[b6],1),' = ',round(df['Close'].loc[b6],1))
        if round(df['Close'].loc[b6],1) > df['Boling_upper'].loc[b6]:
            print('buy [close  > Boling_upper] ',round(df['Close'].loc[b6],1) > round(df['Boling_upper'].loc[b6],1))         
        if round(df['Close'].loc[b6],1) < df['Boling_lower'].loc[b6]:
            print('buy [close  < Boling_lower] ',round(df['Close'].loc[b6],1),' < ',round(df['Boling_lower'].loc[b6],1))  


##        print('77777777777',df['Boling_upper'].loc[s7])
        if  round(df['Boling_middle'].loc[s7],1) < round(df['Close'].loc[s7],1) < round(df['Boling_upper'].loc[s7],1):
            print('sell [Boling_upper < close < Boling_middle] ',\
                  round(df['Boling_upper'].loc[s7],1),' < ',round(df['Close'].loc[s7],1),\
                  ' < ',round(df['Boling_middle'].loc[s7],1))
        elif round(df['Boling_lower'].loc[s7],1) < round(df['Close'].loc[s7],1) < round(df['Boling_middle'].loc[s7],1):
            print('sell [Boling_middle < close < Boling_lower] ',round(df['Boling_middle'].loc[s7],1),' < ',round(df['Close'].loc[s7],1),' < ',round(df['Boling_lower'].loc[s7],1))

        elif round(df['Boling_upper'].loc[s7],1) == round(df['Close'].loc[s7],1):
            print('sell [Boling_upper = close] ',round(df['Boling_upper'].loc[s7],1),' = ',round(df['Close'].loc[s7],1))
        elif round(df['Boling_lower'].loc[s7],1) == round(df['Close'].loc[s7],1):          
            print('sell [Boling_lower = close] ',round(df['Boling_lower'].loc[s7],1),' = ',round(df['Close'].loc[s7],1))
        elif round(df['Close'].loc[s7],1) > df['Boling_upper'].loc[s7]:
            print('sell [close  > Boling_upper] ',round(df['Close'].loc[s7],1) > round(df['Boling_upper'].loc[s7],1))         
        elif round(df['Close'].loc[s7],1) < df['Boling_lower'].loc[s7]:
            print('sell [close  < Boling_lower] ',round(df['Close'].loc[s7],1),' < ',round(df['Boling_lower'].loc[s7],1)) 
        print('\n')

        #vwap
        print('vwap')  
        if  round(df['Boling_middle'].loc[b6],1) < round(df['vwap'].loc[b6],1) < round(df['Boling_upper'].loc[b6],1):
            print('buy [Boling_upper < vwap < Boling_middle] ',\
                  round(df['Boling_upper'].loc[b6],1),' < ',round(df['vwap'].loc[b6],1),\
                  ' < ',round(df['Boling_middle'].loc[b6],1))
        if round(df['Boling_lower'].loc[b6],1) < round(df['vwap'].loc[b6],1) < round(df['Boling_middle'].loc[b6],1):
            print('buy [Boling_middle < vwap < Boling_lower] ',round(df['Boling_middle'].loc[b6],1),' < ',round(df['vwap'].loc[b6],1),' < ',round(df['Boling_lower'].loc[b6],1))
        if round(df['Boling_upper'].loc[b6],1) == round(df['vwap'].loc[b6],1):
            print('buy [Boling_upper = vwap] ',round(df['Boling_upper'].loc[b6],1),' = ',round(df['vwap'].loc[b6],1))
        if round(df['Boling_lower'].loc[b6],1) == round(df['vwap'].loc[b6],1):          
            print('buy [Boling_lower = vwap] ',round(df['Boling_lower'].loc[b6],1),' = ',round(df['vwap'].loc[b6],1))
        if round(df['vwap'].loc[b6],1) > df['Boling_upper'].loc[b6]:
            print('buy [vwap  > Boling_upper] ',round(df['vwap'].loc[b6],1) > round(df['Boling_upper'].loc[b6],1))         
        if round(df['vwap'].loc[b6],1) < df['Boling_lower'].loc[b6]:
            print('buy [vwap  < Boling_lower] ',round(df['vwap'].loc[b6],1),' < ',round(df['Boling_lower'].loc[b6],1))    

##        print('\n')
##        print('77777777777',df['Boling_upper'].loc[s7],'  ',round(df['vwap'].loc[s7],1),'  ',round(df['Boling_middle'].loc[s7],1))
        if  round(df['Boling_middle'].loc[s7],1) < round(df['vwap'].loc[s7],1) < round(df['Boling_upper'].loc[s7],1):
            print('sell [Boling_upper < vwap < Boling_middle] ',\
                  round(df['Boling_upper'].loc[s7],1),' < ',round(df['vwap'].loc[s7],1),\
                  ' < ',round(df['Boling_middle'].loc[s7],1))
        elif round(df['Boling_lower'].loc[s7],1) < round(df['vwap'].loc[s7],1) < round(df['Boling_middle'].loc[s7],1):
            print('sell [Boling_middle < vwap < Boling_lower] ',round(df['Boling_middle'].loc[s7],1),' < ',round(df['vwap'].loc[s7],1),' < ',round(df['Boling_lower'].loc[s7],1))

        elif round(df['Boling_upper'].loc[s7],1) == round(df['vwap'].loc[s7],1):
            print('sell [Boling_upper = vwap] ',round(df['Boling_upper'].loc[s7],1),' = ',round(df['vwap'].loc[s7],1))
        elif round(df['Boling_lower'].loc[s7],1) == round(df['vwap'].loc[s7],1):          
            print('sell [Boling_lower = vwap] ',round(df['Boling_lower'].loc[s7],1),' = ',round(df['vwap'].loc[s7],1))
        elif round(df['vwap'].loc[s7],1) > df['Boling_upper'].loc[s7]:
            print('sell [vwap  > Boling_upper] ',round(df['vwap'].loc[s7],1) > round(df['Boling_upper'].loc[s7],1))         
        elif round(df['vwap'].loc[s7],1) < df['Boling_lower'].loc[s7]:
            print('sell [vwap  < Boling_lower] ',round(df['vwap'].loc[s7],1),' < ',round(df['Boling_lower'].loc[s7],1)) 
        print('\n')


        
    ##print('b6=',buy_price_gg,'  s7=',sell_price_gg)
    print('buy_price=',round(buy_price_gg,2),' sell_price=',round(sell_price_gg,2))
    print('b6 index=',b6,'   s7 index=',s7)

    '''
##fg.close()
























