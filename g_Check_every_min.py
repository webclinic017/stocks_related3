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
import f16_buy
import f17_buy
import f17_sell
import f16_sell
from f16_buy import f16_buyp
from f16_sell import f16_sellp
from f17_buy import f17_buyp
from f17_sell import f17_sellp
import f16_condt
from f16_condt import tickersp

##f16_buy (df,buy_price_gg) 

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
##file_path = '/home/az2/66.txt'
##sys.stdout = open(file_path, "w")


##m=['t','oxy','amgn','arkk','tsla','x','googl','aapl','uso','oil']

def final(df,xs):
    import f16_buy
    from f16_buy import f16_buyp
    import f17_buy
    from f17_buy import f17_buyp
    
    import f16_condt
    import sys
    from f16_condt import buy_call
    from f16_condt import buy_put
    
    from f16_condt import test33
    from f16_condt import test34
    buy_price_gg=0

################ buy call (stock moving up) ##############    
##    Buy   azhar
##    df,xs,buy_status,b6,buy_price_gg=f16_condt.buy_call(df,buy_price_gg,xs)
################ end of buy call (stock moving up) ############## 

################ buy put (stock moving down) ##############

# sell azhar
    xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status=f16_condt.buy_put(df,buy_price_gg,xs)
##    print(xs,df,buy_price_gg,sell_price_gg,b6,s7)
##    print('hhhhh 6666')
##    sys.exit()





def ta(m):
    
    import yfinance as yf
    import pandas as pd
    import talib as taa
    import finta as f
    from numerize import numerize
    ##import pandas_ta as ta2

    import pandas_ta as ta
    
    b=15
    k=4
    for xs in m:
        
        df = yf.download(xs,period='6d',interval='1m')
        df['ticker']=xs

        ##df['p2']=ta.adx(df
        st = ta.supertrend(df['High'], df['Low'], df['Close'], 7, 3)
        v = df['Volume'].values
        tp = (df['Low'] + df['Close'] + df['High']).div(3).values
        df = df.assign(vwap=(tp * v).cumsum() / v.cumsum())

        df['macd'], df['macdsignal'], df['macdhist'] = taa.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
        df['AD'] = taa.ADOSC(df['High'], df['Low'], df['Close'], df['Volume'])
        df['adx'] = taa.ADX(df['High'], df['Low'], df['Close'], timeperiod=5)
        upmove=df['High']-df['High'].shift(1)
        downmove=df['Low'].shift(1)-df['Low']

    ##    if upmove > downmove and upmove > 0:
    ##        DM+=up
    ##    else:
    ##        DM+=0
    ##
    ##    if downmove > upmove  and downmove > 0:
    ##        DM-=down
    ##    else:
    ##        DM-=0    
    ##        
        
        df['ADL']=f.TA.ADL(df)/100000
        df['RSI']= taa.RSI(df['Close'], timeperiod=14)
        df['STOCHRSI_fastk'], df['STOCHRSI_fastd'] = taa.STOCHRSI(df['Close'], timeperiod=3, fastk_period=5, fastd_period=3, fastd_matype=0)
        
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
        df['buy']=''
        df['sell']=''
        i=0
        df['Close_vwap_up']=''

        df['bolinger']=''
        df['bolinger_n']=''



        for x in df.index:
            df['s3'].loc[x]=str(df['Datetime'].loc[x]).split(' ')[0]
            df['s2'].loc[x]=str(df['Datetime'].loc[x]).split(' ')[1][0:5]

            if df['Close'].loc[x] < df['Boling_upper2'].loc[x]:
                
                
            #df['Close'].loc[x] <= df['Boling_upper'].loc[x]:
                df['bolinger'].loc[x]='bolinger_middle < close < bolinger_upper'       
                df['bolinger_n'].loc[x]=str(round(df['Boling_middle'].loc[x],2))+ str(' < ') + str(round(df['Close'].loc[x],2)) + str(' < ') +  str(round(df['Boling_upper'].loc[x],2)) 

            if df['Close'].loc[x]  > df['Boling_upper'].loc[x]:
                df['bolinger'].loc[x]='close > bolinger_upper'
                df['bolinger_n'].loc[x]=str(round(df['Close'].loc[x],2)) + str(' > ') + str(round(df['Boling_upper'].loc[x],2))
                
            if df['Close'].loc[x]  < df['Boling_lower'].loc[x]:
                df['bolinger'].loc[x]='close < bolinger_lower'
                df['bolinger_n'].loc[x]= str(round(df['Close'].loc[x],2)) + str(' < ')+ str(round(df['Boling_lower'].loc[x],2))
                
            if df['Close'].loc[x] > df['Boling_upper2'].loc[x]:
                df['bolinger'].loc[x]='Boling_lower < close < bolinger_middle'
                df['bolinger_n'].loc[x]=str(round(df['Boling_lower'].loc[x],2))+str(' < ') + str(round(df['Close'].loc[x],2))+ str('< ')+ str(round(df['Boling_middle'].loc[x],2)) 

    ################## from sell ##############################################
          

    ##        if df['Boling_middle'].loc[z] <= df['Close'].loc[z] <= df['Boling_upper'].loc[z]:
    ##            df['bolinger'].loc[z]='bolinger_middle < close < bolinger_upper'
    ##            
    ##            df['bolinger_n'].loc[z]=str(round(df['Boling_middle'].loc[z],2))+ str(' < ') + str(round(df['Close'].loc[z],2)) + str(' < ') +  str(round(df['Boling_upper'].loc[z],2)) 
    ##
    ##        if df['Close'].loc[z]  > df['Boling_upper'].loc[z]:
    ##            df['bolinger'].loc[z]='close > bolinger_upper'
    ##            df['bolinger_n'].loc[z]=str(round(df['Close'].loc[z],2)) + str(' > ') + str(round(df['Boling_upper'].loc[z],2))
    ##            
    ##        if df['Close'].loc[z]  < df['Boling_lower'].loc[z]:
    ##            df['bolinger'].loc[z]='close < bolinger_lower'
    ##            df['bolinger_n'].loc[z]= str(round(df['Close'].loc[z],2)) + str(' < ')+ str(round(df['Boling_lower'].loc[z],2))
    ##            
    ##        if df['Boling_lower'].loc[z]  <= df['Close'].loc[z] <= df['Boling_middle'].loc[z]:
    ##            df['bolinger'].loc[z]='Boling_lower < close < bolinger_middle'
    ##            df['bolinger_n'].loc[z]=str(round(df['Boling_lower'].loc[z],2))+str(' < ') + str(round(df['Close'].loc[z],2))+ str('< ')+ str(round(df['Boling_middle'].loc[z],2)) 

    #############################################################################

            
            ######################## squeeze 55

            if df['lower_band'].loc[x] > df['lower_keltner'].loc[x] and df['upper_band'].loc[x] < df['upper_keltner'].loc[x]:
                
                df['squeeze_on'].loc[x]='in_squeeze'
                p=p+1
        ##                print(x,"  in 1 min Squeeze, ATR=",dfq['ATR'].loc[z])
            else:
                df['squeeze_on'].loc[x]=' '

        bb=df.columns.get_loc('s2')


    ##    print(help(ta.adx))
        df['chop']=ta.trend.chop(df['High'], df['Low'], df['Close'], length=14, atr_length=None, scalar=100, drift=1, offset=None)

        final(df,xs)

##        return(df,xs)
        



m=tickersp()
ta(m)
##ta(m)
##df,xs=ta(m)
##final(df,xs)












