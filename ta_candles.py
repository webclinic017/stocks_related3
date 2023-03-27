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


def m(x):
    x='pupu yar'
    return(x)

pd.options.display.float_format = '{:.2f}'.format
pd.options.display.max_columns=155
pd.options.display.max_rows=6500000
pd.set_option('display.max_colwidth', 200)
pd.set_option('display.max_columns', 0)
pd.set_option('display.expand_frame_repr', False)
##ticker=input("Enter ticker:")
##ticker='MRNA'
#ticker='^NDX'
##ticker='Amc'
ticker='TSLA'
u=[]

##df = yf.download(ticker, '2021-05-1','2021-06-16', index=False)
##df = yf.download(ticker, '2021-05-1',str(today), index=False)

##df = yf.download(ticker, '2021-05-1','2021-06-19', index=False)

#####################################################################3
perd='2d'
intervl='1m'
ticker='T'
### [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]
##
####g=input("Enter Ticker :")
###perd=input("Enter no of days '5d','2d','1d' :")
###intervl=input("Enter mins '5m','1m' :")
##
##
###df=pd.DataFrame()
###Interval required 5 minutes
data = yf.download(tickers=ticker, period=perd, interval=intervl)
df=pd.DataFrame(data)
##df3=pd.DataFrame()
##k=1
##
##for x in range(df.shape[0]):
##    df3[x]=([df.iloc[x,2],df.iloc[x,1],df.iloc[x,3]])
##    
##    k=k+1
##    if k > 7:
##        break
##
##df3=df3.T
##print(df3)

##
##print(df)

#######################################################################

  


##df=df.iloc[6:,:]
##print(df)
##print('baba',df.shape)

df.reset_index(inplace = True)
print(df)
df['day'] = df['Date'].dt.day_name()
df['ticker']=ticker
##df['Volume']=(df['Volume']/1000)
##df['Date'] = df['Date'].resample(rule='D').mean()


##
##if df['Volume'][0]  > 100:
##    df['Volume'][0]=df['Volume'][0]/10000
##else:
##    pass
##print(millify(df['Volume']))

df['xaa']=df['Volume']
df['Volume_yest']=df['Volume'].shift(1)
##df['Volume_last3days']=pd.mean(df['Volume'], window=3, min_periods=1).shift(3)
##df['ddd']=df['Volume'].mean(df['Volume']

df['Avg_3day_vol'] = df['Volume'].groupby(df['ticker']).shift(2).rolling(3).mean()
df.reset_index()

df['Avg_5day_vol'] = df['Volume'].groupby(df['ticker']).shift(5).rolling(5).mean().round(2)
df.reset_index()

df['today_vol_vs_3day_vol']=(100*df['Volume']/df['Avg_3day_vol']).round(2)-100
##df['D'] = df['Volume'].groupby(df['Date']).shift(2).rolling(2).mean()


df['Simple MA_3'] = ta.SMA(df['Close'].astype(int),3).round(2)
df['Simple MA_10'] = ta.SMA(df['Close'].astype(int),10)
df['MA_3 > MA_10']=df['Simple MA_3']-df['Simple MA_10']
df['Price > MA_3']= df['Close']-df['Simple MA_3']
##if df['MA_3 > MA_10'] > 0:
##    df['MA_3 > MA_10']='Y'
    
df['Day_swing']=df['High']-df['Low']
df['Yest_Close']=df['Close']
df['Yest_Close']=df['Yest_Close'].shift(1)
df['delta']=df['Close']-df['Yest_Close'].round(2)
df['delta_cl_op']=df['Open']-df['Yest_Close'].round(2)
df['*']='*'
##df['CCI']=ta.CCI(df['High'], df['Low'], df['Close'], timeperiod=3)
#Commodity Channel Index (Momentum Indicators)
df['ADX_over25_strong_less25_weak_trend']=ta.ADX(df['High'], df['Low'], df['Close'], timeperiod=3).round(2)
df['rsi_trend'] = ta.RSI(df['Close'], timeperiod=14).round(2)
df['BOP*_trend']=ta.BOP(df['Open'],df['High'],df['Low'],df['Close']).round(2)
df['ADXR*_trend']=ta.ADX(df['High'], df['Low'], df['Close'], timeperiod=3).round(2)
df['AROONOSC*_trend']=ta.AROONOSC(df['High'],df['Low'], timeperiod=3).round(2)
df['DX*_trend']=ta.DX(df['High'],df['Low'],df['Close'], timeperiod=3).round(2)
##df['AROON']=ta.AROON(df['High'],df['Low'], timeperiod=3)
df['MFI*_trend']=ta.MFI(df['High'],df['Low'],df['Close'],df['Volume'], timeperiod=3).round(2)
df['CCI*_trend']=ta.CCI(df['High'],df['Low'],df['Close'], timeperiod=3).round(2)
df['MINUS_DI']=ta.MINUS_DI(df['High'],df['Low'],df['Close'], timeperiod=3).round(2)
df['MINUS_DM']=ta.MINUS_DM(df['High'],df['Low']).round(2)
df['MINUS_DI_MINUS_DM_(-ve-dwn_+ve_up)_*']=df['MINUS_DI']-df['MINUS_DM']
df['PPO__*_trend'] = ta.PPO(df['Close']).round(2)
df['MOM_*_Signal']=ta.MOM(df['Close'], timeperiod=3).round(2)
df['ROCP_*_trend']=ta.ROCP(df['Close'], timeperiod=3).round(2)
df['ROCP_<0_downtrnd_>0uptrend']=df['ROCP_*_trend']
df['ULTOSC']=ta.ULTOSC(df['High'],df['Low'],df['Close'], timeperiod1=3, timeperiod2=5, timeperiod3=7).round(2)
df['ULTOSC_[less_30_buy]_[grt_70_sell']=df['ULTOSC']

df['PLUS_DI']=ta.PLUS_DI(df['High'],df['Low'],df['Close'], timeperiod=3).round(2)
df['PLUS_DM']=ta.PLUS_DM(df['High'],df['Low'], timeperiod=3).round(2)

##df['CCI']=ta.CCI(df['Open'],df['High'],df['Low'],df['Close'], timeperiod=3)
##Average Directional Movement Index (Momentum Indicators)
df['CDLSHORTLINE']=ta.CDLSHORTLINE(df['Open'],df['High'],df['Low'],df['Close']).round(2)




df['ROCR100']=ta.ROCR100(df['Close'], timeperiod=3).round(2)
df['WILLR']=ta.WILLR(df['High'],df['Low'],df['Close'], timeperiod=3).round(2)

#Aroon (Momentum Indicators)
##df['CDL2CROWS']=ta.CDL2CROWS(df['High'], df['Low'], df['Close'], timeperiod=3)
#Two Crows (Pattern Recognition)
##df['CDLHARAMI']=ta.CDLHARAMI(df['High'], df['Low'], df['Close'], timeperiod=3)
#Two Crows (Pattern Recognition)

#Miscl
df['TRIX']=ta.TRIX(df['Close'], timeperiod=3).round(2)
df['SAREXT']=ta.SAREXT(df['High'],df['Low'],startvalue=0, offsetonreverse=0, accelerationinitlong=0.02, accelerationlong=0.02, accelerationmaxlong=.2,
                       accelerationinitshort=.02, accelerationshort=.02, accelerationmaxshort=.2).round(2)

#Trendline
df['HT_TRENDLINE'] = ta.HT_TRENDLINE(df['Close']).round(2)
df['HT_TRENDMODE'] = ta.HT_TRENDMODE(df['Close']).round(2)


df['Cum_Vol'] = df['Volume'].cumsum()
df['Cum_Vol_Price'] = (df['Volume'] * (df['High'] + df['Low'] + df['Close'] ) /3).cumsum()
##df['VWAP'] = df['Cum_Vol_Price'] / df['Cum_Vol']
df['VWAP'] = df['Cum_Vol_Price'] / df['Cum_Vol']
df['Close > VWAP']=df['Close']-df['VWAP']
##df['VWAP'] = df['Close']
df['VWAP > Simple MA_10']=df['VWAP']-df['Simple MA_10']



df['VWAP > Simple MA_3']=df['VWAP']-df['Simple MA_3']
df['VWAP_signal--> buy_(+ve)_sell_(-ve)']=df['Close']-df['VWAP']
##df['sell_Buy_above_VWAP_(+ve)']=df['VWAP']-df['Close']


df['stream_WILLR']=ta.stream_WILLR(df['High'], df['Low'], df['Close'], timeperiod=3)
df['CDLDOJI']=ta.CDLDOJI(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLHAMMER']=ta.CDLHAMMER(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLDOJISTAR']=ta.CDLDOJISTAR(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLENGULFING']=ta.CDLENGULFING (df['Open'],df['High'], df['Low'], df['Close'])
df['CDLBREAKAWAY']=ta.CDLBREAKAWAY (df['Open'],df['High'], df['Low'], df['Close'])
df['CDLGRAVESTONEDOJI']=ta.CDLGRAVESTONEDOJI (df['Open'],df['High'], df['Low'], df['Close'])
df['CDLINVERTEDHAMMER']=ta.CDLINVERTEDHAMMER (df['Open'],df['High'], df['Low'], df['Close'])


df['CDL2CROWS']=ta.CDL2CROWS(df['Open'],df['High'], df['Low'], df['Close'])
df['CDL3BLACKCROWS']=ta.CDL3BLACKCROWS(df['Open'],df['High'], df['Low'], df['Close'])
df['CDL3INSIDE(']=ta.CDL3INSIDE(df['Open'],df['High'], df['Low'], df['Close'])
df['CDL3LINESTRIKE']=ta.CDL3LINESTRIKE(df['Open'],df['High'], df['Low'], df['Close'])
df['CDL3OUTSIDE']=ta.CDL3OUTSIDE(df['Open'],df['High'], df['Low'], df['Close'])
df['CDL3STARSINSOUTH']=ta.CDL3STARSINSOUTH(df['Open'],df['High'], df['Low'], df['Close'])
df['CDL3WHITESOLDIERS']=ta.CDL3WHITESOLDIERS(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLABANDONEDBABY']=ta.CDLABANDONEDBABY(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLADVANCEBLOCK']=ta.CDLADVANCEBLOCK(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLBELTHOLD']=ta.CDLBELTHOLD(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLBREAKAWAY']=ta.CDLBREAKAWAY(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLCLOSINGMARUBOZU']=ta.CDLCLOSINGMARUBOZU(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLCONCEALBABYSWALL']=ta.CDLCONCEALBABYSWALL(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLCOUNTERATTACK']=ta.CDLCOUNTERATTACK(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLDARKCLOUDCOVER']=ta.CDLDARKCLOUDCOVER(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLDOJI']=ta.CDLDOJI(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLDOJISTAR']=ta.CDLDOJISTAR(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLDRAGONFLYDOJI']=ta.CDLDRAGONFLYDOJI(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLENGULFING']=ta.CDLENGULFING(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLEVENINGDOJISTAR']=ta.CDLEVENINGDOJISTAR(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLEVENINGSTAR']=ta.CDLEVENINGSTAR(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLGAPSIDESIDEWHITE']=ta.CDLGAPSIDESIDEWHITE(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLGRAVESTONEDOJI']=ta.CDLGRAVESTONEDOJI(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLHAMMER']=ta.CDLHAMMER(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLHANGINGMAN']=ta.CDLHANGINGMAN(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLHARAMI']=ta.CDLHARAMI(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLHARAMICROSS']=ta.CDLHARAMICROSS(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLHIGHWAVE']=ta.CDLHIGHWAVE(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLHIKKAKE']=ta.CDLHIKKAKE(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLHIKKAKEMOD']=ta.CDLHIKKAKEMOD(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLHOMINGPIGEON']=ta.CDLHOMINGPIGEON(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLIDENTICAL3CROWS']=ta.CDLIDENTICAL3CROWS(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLINNECK']=ta.CDLINNECK(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLINVERTEDHAMMER']=ta.CDLINVERTEDHAMMER(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLKICKING']=ta.CDLKICKING(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLKICKINGBYLENGTH']=ta.CDLKICKINGBYLENGTH(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLLADDERBOTTOM']=ta.CDLLADDERBOTTOM(df['Open'],df['High'], df['Low'], df['Close'])

df['CDLLONGLEGGEDDOJI']=ta.CDLLONGLEGGEDDOJI(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLLONGLINE']=ta.CDLLONGLINE(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLMARUBOZU']=ta.CDLMARUBOZU(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLMATCHINGLOW']=ta.CDLMATCHINGLOW(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLMATHOLD']=ta.CDLMATHOLD(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLMORNINGDOJISTAR']=ta.CDLMORNINGDOJISTAR(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLMORNINGSTAR']=ta.CDLMORNINGSTAR(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLONNECK']=ta.CDLONNECK(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLPIERCING(']=ta.CDLPIERCING(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLRICKSHAWMAN']=ta.CDLRICKSHAWMAN(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLRISEFALL3METHODS']=ta.CDLRISEFALL3METHODS(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLSEPARATINGLINES']=ta.CDLSEPARATINGLINES(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLSHOOTINGSTAR']=ta.CDLSHOOTINGSTAR(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLSHORTLINE']=ta.CDLSHORTLINE(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLSPINNINGTOP']=ta.CDLSPINNINGTOP(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLSTALLEDPATTERN']=ta.CDLSTALLEDPATTERN(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLSTICKSANDWICH']=ta.CDLSTICKSANDWICH(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLTAKURI']=ta.CDLTAKURI(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLTASUKIGAP']=ta.CDLTASUKIGAP(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLTHRUSTING']=ta.CDLTHRUSTING(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLTRISTAR']=ta.CDLTRISTAR(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLUNIQUE3RIVER']=ta.CDLUNIQUE3RIVER(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLUPSIDEGAP2CROWS']=ta.CDLUPSIDEGAP2CROWS(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLXSIDEGAP3METHODS']=ta.CDLXSIDEGAP3METHODS(df['Open'],df['High'], df['Low'], df['Close'])

df['CDLBELTHOLD']=ta.CDLBELTHOLD(df['Open'],df['High'], df['Low'], df['Close'])
df['CDLRICKSHAWMAN']=ta.CDLRICKSHAWMAN(df['Open'],df['High'], df['Low'], df['Close'])
df['Reversal']=ta.CDLLONGLEGGEDDOJI(df['Open'],df['High'], df['Low'], df['Close'])
df['b']='*'


################################################
##MA_3= df.columns.get_loc('Simple MA_3')
##MA_10=df.columns.get_loc('Simple MA_10')
##MA_3_gr_MA_10=MA_3-MA_10
##price=df.columns.get_loc('Close')
##
##if MA_3_gr_MA_10 > 0 and price > MA_3:
##    print("BUY  Price > MA_3,MA_10)
          

##print('\n\n\n')
##print(df.shape[0])
##u=df.shape[0]
##print(u,' cc  ',mn)
##print(df.iloc[(u-1),df.columns.get_loc('MA_3 > MA_10')].round(2))
##print('\n\n\n')
##
print(df)
print(df)
df2=df

###################print(df.columns.get_loc('VWAP > Simple MA_10'))
##print('oooo ',df.columns.get_loc('VWAP'))
#################
def VWAP(x,t):
    df2.iloc[x,51]=t
    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,51])
#######################
##'Close > VWAP'

print('fff',df.columns.get_loc('Close > VWAP'))
###################
def Close_gr_VWAP(x,t):
    df2.iloc[x,52]=t
    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,52])
#########################

##print('gggg',df.columns.get_loc('VWAP > Simple MA_10'))
#################
def VWAP_great_Simple_MA_10(x,t):
    df2.iloc[x,53]=t
    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,53])
#######################
##print('pp',df.columns.get_loc('VWAP > Simple MA_3'))
#################
def VWAP_great_Simple_MA_3(x,t):
    df2.iloc[x,54]=t
    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,54])
#######################
#######################
print(df.columns.get_loc('VWAP_signal--> buy_(+ve)_sell_(-ve)'))
#################
def VWAP_signal(x,t):
    df2.iloc[x,55]=t
    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,55])
#######################
#################
def ticker(x,t):
    df2.iloc[x,8]=t
    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,8])
#######################

#################
def RSI(x,t):
    if t > 70:
        df2.iloc[x,24]='down(buy_call)'
    elif t < 30:
        df2.iloc[x,24]='up(buy_put)'
    else:
        pass
    return(df2.iloc[x,24])
##print(df2.columns)

##print('VWAP','   ',df.columns.get_loc('VWAP'))
#######################
#########################
def ADX(x,t):

##df['ADX_over25_strong_less25_weak_trend']
##def ADX(x,t):                
    if 0 < t < 25:
        df2.iloc[x,23]='weak_trend/may reverse'
    elif 25 < t < 50:
        df2.iloc[x,23]='strong_trend'
    elif 50 < t < 75:
        df2.iloc[x,23]='Very Strong Trend'
    elif 75 < t < 101:
        df2.iloc[x,23]='Extremely Strong Trend'
    else:
        pass    
    return(df2.iloc[x,23])

########################################
################################
##df['BOP*_trend']
##print(df.columns.get_loc('ROCP_*_trend'))
def ROCP(x,t):
    if t < 0:
        df2.iloc[x,36]='downtrend'
    else: 
        df2.iloc[x,36]='uptrend'
    return(df2.iloc[x,36])
##############################
################################
##df['BOP*_trend']
##print(df.columns.get_loc('MOM_*_Signal'))
def MOM(x,t):
    if t < 0:
        df2.iloc[x,35]='downtrend'
    else: 
        df2.iloc[x,35]='uptrend'
    return(df2.iloc[x,35])
##############################
##print(df.columns.get_loc('ULTOSC_[less_30_buy]_[grt_70_sell'))
def ULTOSC(x,t):
    if t < 30:
        df2.iloc[x,39]='Buy'

    elif t > 70:
        df2.iloc[x,39]='sell'
    else: 
        pass
    return(df2.iloc[x,39])

############################
################################
##df['BOP*_trend']
##print(df.columns.get_loc('AROONOSC*_trend'))
def AROONOSC(x,t):
    if t < 0:
        df2.iloc[x,27]='downtrend'
    else: 
        df2.iloc[x,27]='uptrend'
    return(df2.iloc[x,27])
##############################

##print(df.columns.get_loc('MINUS_DI_MINUS_DM_(-ve-dwn_+ve_up)_*'))
def MINUS_DI_MINUS_DM(x,t):
    df2.iloc[x,33]=t
    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,33])
##############################
##############################

##print(df.columns.get_loc('VWAP_signal--> buy_(+ve)_sell_(-ve)'))
def VWAP_signal(x,t):
    df2.iloc[x,54]=t
    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,54])
##############################
##############################

##print(df.columns.get_loc('TRIX'))
def TRIX(x,t):
    df2.iloc[x,54]=t
    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,54])
##############################
##############################

##print(df.columns.get_loc('PLUS_DI'))
def PLUS_DI(x,t):
    df2.iloc[x,40]=t
    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,40])
##############################
##############################

##print(df.columns.get_loc('PLUS_DM'))
def PLUS_DM(x,t):
    df2.iloc[x,41]=t
    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,41])
##############################

##############################

##print(df.columns.get_loc('CCI*_trend'))
def CCI(x,t):
    df2.iloc[x,30]=t
    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,30])
##############################
##############################

##print(df.columns.get_loc('Date'))
def Date(x,t):
    df2.iloc[x,0]=t
    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,0])
##############################
##############################

##print(df.columns.get_loc('day'))
def day(x,t):
    df2.iloc[x,7]=t
    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,7])
##############################
##############################

##print(df.columns.get_loc('Volume'))
def Volume(x,t):
##    t=t*33333

##    print('kkkk',t)
    df2.iloc[x,6]=t
    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,6])
##############################
##Volume_yest  Avg_3day_vol  Avg_5day_vol

##print(df.columns.get_loc('Volume_yest'))
def Volume_yest(x,t):
    df2.iloc[x,10]=t
    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,10])
##############################
##############################
##Volume_yest  Avg_3day_vol  Avg_5day_vol

##print(df.columns.get_loc('Avg_3day_vol'))
def Avg_3day_vol(x,t):
    df2.iloc[x,11]=t
    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,11])
##############################
##############################
##Volume_yest  Avg_3day_vol  Avg_5day_vol

##print(df.columns.get_loc('Avg_5day_vol'))
def Avg_5day_vol(x,t):
    df2.iloc[x,12]=t
    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,12])
##############################
##############################
##Volume_yest  Avg_3day_vol  Avg_5day_vol

##print(df.columns.get_loc('Close'))
def Close(x,t):
    df2.iloc[x,4]=t
    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,4])
##############################
##############################
##Volume_yest  Avg_3day_vol  Avg_5day_vol

##print(df.columns.get_loc('Yest_Close'))
def Yest_Close(x,t):
    df2.iloc[x,19]=t
    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,19])
##############################
##############################
##Volume_yest  Avg_3day_vol  Avg_5day_vol

##print(df.columns.get_loc('Day_swing'))
def Day_swing(x,t):
    df2.iloc[x,18]=t
    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,18])
##############################
##############################
##Volume_yest  Avg_3day_vol  Avg_5day_vol

##print(df.columns.get_loc('delta'))
def delta(x,t):
    df2.iloc[x,20]=t
    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,20])
##############################
##Volume_yest  Avg_3day_vol  Avg_5day_vol

##print(df.columns.get_loc('delta_cl_op'))
def delta_cl_op(x,t):
    df2.iloc[x,21]=t
    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,21])
##############################
##############################
##Volume_yest  Avg_3day_vol  Avg_5day_vol

##print(df.columns.get_loc('Open'))
def Open(x,t):
    df2.iloc[x,1]=t
    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,1])
##############################
##############################
##Volume_yest  Avg_3day_vol  Avg_5day_vol

##print(df.columns.get_loc('High'))
def High(x,t):
    df2.iloc[x,2]=t
    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,2])
##############################
##############################
##Volume_yest  Avg_3day_vol  Avg_5day_vol

##print(df.columns.get_loc('Low'))
def Low(x,t):
    df2.iloc[x,3]=t
    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,3])
##############################
##############################
##Volume_yest  Avg_3day_vol  Avg_5day_vol

##print(df.columns.get_loc('Simple MA_3'))
def Simple_MA_3(x,t):
    df2.iloc[x,14]=t
    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,14])
##############################
##############################
##Volume_yest  Avg_3day_vol  Avg_5day_vol

print('dddddd',df.columns.get_loc('Simple MA_10'))
def Simple_MA_10(x,t):
    df2.iloc[x,15]=t

    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,15])
##############################
##############################
##Volume_yest  Avg_3day_vol  Avg_5day_vol

##print(df.columns.get_loc('Low'))
def MA_3_grtr_MA_10(x,t):
    df2.iloc[x,3]=t
    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,3])
##############################
##############################
##Volume_yest  Avg_3day_vol  Avg_5day_vol

##print(df.columns.get_loc('Price > MA_3'))
def Price_gr_MA_3(x,t):
    df2.iloc[x,17]=t
    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,17])
##############################
print(df.columns.get_loc('b'))
##############################
##Volume_yest  Avg_3day_vol  Avg_5day_vol

##print(df.columns.get_loc('Price > MA_3'))
def b(x,t):
    df2.iloc[x,117]='**'
    
       
##    if t < 30:
##        df2.iloc[x,33]='Buy'
##
##    elif t > 70:
##        df2.iloc[x,33]='sell'
##    else: 
##        pass
    return(df2.iloc[x,117])
##############################

k=0
VWAP_c=[];Close_gr_VWAP_c=[];
RSI_c=[];ADX_c=[];ROCP_c=[];MOM_c=[];ULTOSC_c=[];AROONOSC_c=[];MINUS_DI_MINUS_DM_c=[];VWAP_signal_c=[];PLUS_DM_c=[]
TRIX_c=[];PLUS_DI_c=[];CCI_c=[];Date_c=[];day_c=[];Volume_c=[];Volume_yest_c=[];Avg_3day_vol_c=[];Avg_5day_vol_c=[]
Close_c=[];Yest_Close_c=[];Day_swing_c=[];delta_c=[];delta_cl_op_c=[];Open_c=[];Low_c=[];High_c=[]
ticker_c=[];Simple_MA_3_c=[];Simple_MA_10_c=[];MA_3_grtr_MA_10_c=[];Price_less_MA_3_c=[];Price_gr_MA_3_c=[]
b_c=[];VWAP_great_Simple_MA_10_c=[];VWAP_great_Simple_MA_3_c=[];VWAP_signal_c=[]






for x in range(df2.shape[0]):
    t=Close_gr_VWAP(x,df2.iloc[x,52])
##    print('rsi',x,'  ',t)
    Close_gr_VWAP_c.append(t)


for x in range(df2.shape[0]):
    t=VWAP(x,df2.iloc[x,51])
##    print('rsi',x,'  ',t)
    VWAP_c.append(t)

for x in range(df2.shape[0]):
    t=VWAP_signal(x,df2.iloc[x,54])
##    print('rsi',x,'  ',t)
    VWAP_signal_c.append(t)

for x in range(df2.shape[0]):
    t=VWAP_great_Simple_MA_3(x,df2.iloc[x,53])
##    print('rsi',x,'  ',t)
    VWAP_great_Simple_MA_3_c.append(t)    

for x in range(df2.shape[0]):
    t=VWAP_great_Simple_MA_10(x,df2.iloc[x,52])
##    print('rsi',x,'  ',t)
    VWAP_great_Simple_MA_10_c.append(t)

    
for x in range(df2.shape[0]):
    t=b(x,df2.iloc[x,117])
##    print('rsi',x,'  ',t)
    b_c.append(t)
    
for x in range(df2.shape[0]):
    t=ticker(x,df2.iloc[x,8])
##    print('rsi',x,'  ',t)
    ticker_c.append(t)


for x in range(df2.shape[0]):
    t=RSI(x,df2.iloc[x,24])
##    print('rsi',x,'  ',t)
    RSI_c.append(t)
    
for x in range(df2.shape[0]):    
    t2=ADX(x,df2.iloc[x,23])   
##    print('adx',x,'  ',t2)
    ADX_c.append(t2)
##    

for x in range(df2.shape[0]):    
    t3=ROCP(x,df2.iloc[x,36])   
##    print('adx',x,'  ',t2)
    ROCP_c.append(t3)

for x in range(df2.shape[0]):    
    t4=MOM(x,df2.iloc[x,35])   
##    print('adx',x,'  ',t2)
    MOM_c.append(t4)

for x in range(df2.shape[0]):    
    t5=ULTOSC(x,df2.iloc[x,39])   
##    print('adx',x,'  ',t2)
    ULTOSC_c.append(t5)

for x in range(df2.shape[0]):    
    t6=AROONOSC(x,df2.iloc[x,27])   
##    print('adx',x,'  ',t2)
    AROONOSC_c.append(t6)  
    
for x in range(df2.shape[0]):    
    t7=MINUS_DI_MINUS_DM(x,df2.iloc[x,33])   
##    print('adx',x,'  ',t2)
    MINUS_DI_MINUS_DM_c.append(t7)

for x in range(df2.shape[0]):    
    t8=VWAP_signal(x,df2.iloc[x,54])   
##    print('adx',x,'  ',t2)
    VWAP_signal_c.append(t8)

for x in range(df2.shape[0]):    
    t9=TRIX(x,df2.iloc[x,45])   
##    print('adx',x,'  ',t2)
    TRIX_c.append(t9)  

for x in range(df2.shape[0]):    
    t10=PLUS_DI(x,df2.iloc[x,40])   
##    print('adx',x,'  ',t2)
    PLUS_DI_c.append(t10)     
##    k=k+1

for x in range(df2.shape[0]):    
    t11=PLUS_DM(x,df2.iloc[x,40])   
##    print('adx',x,'  ',t2)
    PLUS_DM_c.append(t11)     
##    k=k+1

for x in range(df2.shape[0]):    
    t12=df2.iloc[x,30]   
##    print('adx',x,'  ',t2)
    CCI_c.append(t12)     
##    k=k+1

for x in range(df2.shape[0]):    
    t13=df2.iloc[x,0]   
##    print('adx',x,'  ',t2)
    Date_c.append(t13)     
##    k=k+1
        
for x in range(df2.shape[0]):    
    t14=df2.iloc[x,7]   
##    print('adx',x,'  ',t2)
    day_c.append(t14)     
##    k=k+1

for x in range(df2.shape[0]):    
    t15=millify(df2.iloc[x,6])
##    print('adx',x,'  ',t2)
    Volume_c.append(t15)     
##    k=k+1
    

for x in range(df2.shape[0]):    
    t16=(df2.iloc[x,10])
    if math.isnan(t16):
        pass
    else:
        t16=millify(t16)
##    print('adx',x,'  ',t2)
    Volume_yest_c.append(t16)     
##    k=k+1


for x in range(df2.shape[0]):    
    t17=df2.iloc[x,11]
    if math.isnan(t17):
        pass
    else:
        t17=millify(t17)
##    print('adx',x,'  ',t2)
    Avg_3day_vol_c.append(t17)     
##    k=k+1   
    
##for x in range(df2.shape[0]):    
##    t18=(x,df2.iloc[x,11])   
####    print('adx',x,'  ',t2)
##    Avg_3day_vol_c.append(t18)     
##    k=k+1

for x in range(df2.shape[0]):    
    t18=df2.iloc[x,12]
    if math.isnan(t18):
        pass
    else:
        t18=millify(t18)
##    print('adx',x,'  ',t2)
    Avg_5day_vol_c.append(t18)     
##    k=k+1

for x in range(df2.shape[0]):    
    t19=df2.iloc[x,4]   
##    print('adx',x,'  ',t2)
    Close_c.append(t19)     
##    k=k+1

for x in range(df2.shape[0]):    
    t20=df2.iloc[x,19]   
##    print('adx',x,'  ',t2)
    Yest_Close_c.append(t20)     
##    k=k+1

    
for x in range(df2.shape[0]):    
    t21=df2.iloc[x,18]   
##    print('adx',x,'  ',t2)
    Day_swing_c.append(t21)     
##    k=k+1

for x in range(df2.shape[0]):    
    t22=df2.iloc[x,20]   
##    print('adx',x,'  ',t2)
    delta_c.append(t22)     
##    k=k+1


for x in range(df2.shape[0]):    
    t23=df2.iloc[x,21]   
##    print('adx',x,'  ',t2)
    delta_cl_op_c.append(t23)     
##    k=k+1

for x in range(df2.shape[0]):    
    t24=df2.iloc[x,1]   
##    print('adx',x,'  ',t2)
    Open_c.append(t24)     
##    k=k+1

for x in range(df2.shape[0]):    
    t25=df2.iloc[x,2]   
##    print('adx',x,'  ',t2)
    High_c.append(t25)     
##    k=k+1

for x in range(df2.shape[0]):    
    t26=df2.iloc[x,3]   
##    print('adx',x,'  ',t2)
    Low_c.append(t26)     
##    k=k+1

for x in range(df2.shape[0]):    
    t27=df2.iloc[x,14]   
##    print('adx',x,'  ',t2)
    Simple_MA_3_c.append(t27)     
##    k=k+1    


for x in range(df2.shape[0]):    
    t27=df2.iloc[x,14]   
##    print('adx',x,'  ',t2)
    Simple_MA_3_c.append(t27)     
##    k=k+1    



for x in range(df2.shape[0]):    
    t27=df2.iloc[x,15]   
##    print('adx',x,'  ',t2)
    Simple_MA_10_c.append(t27)     
##    k=k+1    


for x in range(df2.shape[0]):    
    t27=df2.iloc[x,16]   
##    print('adx',x,'  ',t2)
    MA_3_grtr_MA_10_c.append(t27)     
##    k=k+1 

for x in range(df2.shape[0]):    
    t27=df2.iloc[x,17]   
##    print('adx',x,'  ',t2)
    Price_gr_MA_3_c.append(t27)     
##    k=k+1



    
df5=pd.DataFrame([b_c,ticker_c,RSI_c,ADX_c,ROCP_c,MOM_c,ULTOSC_c,AROONOSC_c,MINUS_DI_MINUS_DM_c,
                  VWAP_c,Close_gr_VWAP_c,
                  VWAP_signal_c,VWAP_great_Simple_MA_3_c,VWAP_great_Simple_MA_10_c,
                  TRIX_c,PLUS_DI_c,PLUS_DM_c,CCI_c,Date_c,day_c,Volume_c
                  ,Volume_yest_c,Avg_3day_vol_c,Avg_5day_vol_c,Close_c,Yest_Close_c,Day_swing_c,
                  delta_c,delta_cl_op_c,Low_c,High_c,Open_c,
                  Simple_MA_3_c,Simple_MA_10_c,MA_3_grtr_MA_10_c,Price_gr_MA_3_c])



df5=df5.T

df5.columns=['b','ticker','RSI','ADX','ROCP','MOM','ULTOSC','AROONOSC','MINUS_DI_MINUS_DM',
             'VWAP','Close_gr_VWAP',
             'VWAP_signal','VWAP_great_Simple_MA_3','VWAP_great_Simple_MA_10',
             'TRIX','PLUS_DI','PLUS_DM','CCI','Date','day','Volume',
             'Volume_yest','Avg_3day_vol','Avg_5day_vol','Close','Yest_Close','Day_swing',
             'delta','delta_cl_op','Low','High','Open','Simple_MA_3','Simple_MA_10','MA_3_grtr_MA_10','Price_gr_MA_3']


cols = df5.columns.tolist()
print(cols)

##df5b=df5[[
##    'b',
##    'ticker', 'RSI', 'ADX', 'ROCP', 'MOM', 'ULTOSC', 'AROONOSC', 'MINUS_DI_MINUS_DM', 'VWAP_signal', 'TRIX', 'PLUS_DI', 'PLUS_DM', 'CCI', 'Date', 'day', 'Volume', 'Volume_yest', 'Avg_3day_vol', 'Avg_5day_vol', 'Close', 'Yest_Close', 'Day_swing', 'delta', 'delta_cl_op', 'Low', 'High', 'Open', 'Simple_MA_3', 'Simple_MA_10', 'MA_3_grtr_MA_10', 'Price_gr_MA_3']
##         

df5b=df5[['ticker', 'Date', 'day',
          'b', 'delta',
          'b','Close',
          'b','Volume','Volume_yest','Avg_3day_vol', 'Avg_5day_vol',
          'b','Close','Yest_Close',
          'b','Day_swing','delta', 'delta_cl_op',
          'b','Close','Low', 'High', 'Open',
          'b', 'MA_3_grtr_MA_10', 'Price_gr_MA_3','Simple_MA_3', 'Simple_MA_10',
          'b','VWAP','Close_gr_VWAP','VWAP_signal','VWAP_great_Simple_MA_3','VWAP_great_Simple_MA_10',
          'b','TRIX',
          'b', 'RSI', 'ADX', 'ROCP', 'MOM', 'ULTOSC', 'AROONOSC','MINUS_DI_MINUS_DM', 'PLUS_DI',
          'PLUS_DM', 'CCI']]
          
##dfc=pd.DataFrame('RSI_c')
gg=df2.shape
df5b=df5b.iloc[:gg[0],:]
      
print(df5b)
print('df5, df2 ',df5.shape, '  c  ',df2.shape)
print('baba - df5 ',df5.shape)
##print(RSI)
##print(dfc.shape)
##
##df5b=df5[['b','ticker', 'RSI', 'ADX', 'ROCP', 'MOM', 'ULTOSC', 'AROONOSC', 'MINUS_DI_MINUS_DM', 'VWAP_signal', 'TRIX',
##          'PLUS_DI', 'PLUS_DM', 'CCI', 'Date', 'day', 'Volume', 'Volume_yest', 'Avg_3day_vol', 'Avg_5day_vol', 'Close',
##          'Yest_Close', 'Day_swing', 'delta', 'delta_cl_op', 'Low', 'High', 'Open', 'Simple_MA_3', 'Simple_MA_10',
##          'MA_3_grtr_MA_10', 'Price_gr_MA_3']]
##
##print(df5b)
        
##df=pd.concat([RSI_c,ADX_c],axis=0)
##df5=pd.DataFrame(RSI_c,ADX_c,columns=['RSI','ADX'])   
##print(df5)

'''
##ADX is momentum strength.
##ADX Value	Trend Strength
##0-25	Absent or Weak Trend
##25-50	Strong Trend
##50-75	Very Strong Trend
##75-100	Extremely Strong Trend


RSI
RSI>70 overbought. Down.
RSI<30 oversold. Up

ADX
The direction of the ADX line is important for reading trend strength.
When the ADX line is rising, trend strength is increasing, and the price moves in the direction of the trend.
When the line is falling, trend strength is decreasing, and the price enters a period of retracement or consolidation.
The Best ADX Strategy
Step #1: Wait for the ADX indicator to show a reading above 25. ...
Step #2: Use the last 50 candlesticks to determine the trend. ...
Step #3: Sell when the RSI indicator breaks and show a reading below 30. ...
Step #4: Protective Stop Loss should be placed at the last ADX high.

ADX Interpretations Explained
Below 20: ---- Non-trending market.
Crosses above 20: Signal that a trend might be emerging; traders might consider initiating buy or sell orders in the
direction of the prevailing stock, future, or currency price movement.
Between 20 & 40: ------------ If ADX is increasing between 20 and 40, then it is considered a further confirmation of an emerging trend.
Traders might consider buying or short selling in the direction of the current market direction.
Furthermore, traders might avoid using oscillator technical indicators and instead consider using trend following indicators
like moving averages. Above 40: Very strong trend.
Crosses above 50:----- Extremely strong trend.
Crosses above 70: ------ “Power Trend”; very rare occurrence

Read more at: https://commodity.com/technical-analysis/adx/
Read more at: https://commodity.com/technical-analysis/adx/

RSI:
RSI > 70: Trend reversal or pullback.
RSI < 30: Trend reversal or up.
Traditional interpretation and usage of the RSI are that values of 70 or above indicate that a security is becoming overbought or overvalued and may be primed for a trend reversal or corrective pullback in price.
An RSI reading of 30 or below indicates an oversold or undervalued condition.

AROONOSC Aroon Oscillator :
0 line crossover, trend reversal.
Above 0 -- uptrend.
below 0 -- downtrend.
The Aroon Oscillator is a trend-following indicator that uses aspects of the Aroon Indicator (Aroon Up and Aroon Down)
to gauge the strength of a current trend and the likelihood that it will continue. Readings above zero indicate that an
uptrend is present, while readings below zero indicate that a downtrend is present. Traders watch for zero line crossovers
to signal potential trend changes.
They also watch for big moves, above 50 or below -50 to signal strong price
moves.


BOP
A rising BOP line indicates an upward trend and
a falling BOP line indicates a downward trend.
The zero-line crossover confirms the trend change.
look at the trend

CCI:
The indicator is also lagging, which means at times it will provide poor signals.
A rally to 100 or -100 to signal a new trend may come too late,
as the price has had its run and is starting to correct already.

ULTOSC
buy signal < 30.
sell signal > 70
Buy signals occur when there is bullish divergence, the divergence low is below 30 on the indicator, and the oscillator
then rises above the divergence high.
A sell signal occurs when there is bearish divergence, the divergence high is above 70, and the oscillator then falls below the divergence low.

ROCP:
ROCP_< 0_downtrnd
ROCP > 0_uptrend'

DX:
+ve is uptrend
-ve is negative

MFI:
up=increasing.
down=decreasing
MFI > 80 strong upward trend
MFI > 90 oversold...reverse.
MFI < 20 strong downward trend.m
MFI < 10 oversold.....reverse.

CCI: (0 to 100):
CCI>100:new uptrend,reverse.
CCI<0:a buying opportunity.


info_MINUS_DI_MINUS_DM:
MINUS_DI>MINUS_DM:downtrend.
MINSU_ID<MINUS_DM:uptrend


ppo:
ppo>0:
uptrend
ppo<0:
downtrend


MOM:
Sell signal 
When the momentum indicator crosses below the zero line,
it can slowly mean two things; the price of the future,
currency pair, or stock has topped out and
is reversing or that the price has broken below recent lows.
Either way, traders mostly interpret these events as bearish signals.

Exit signals 
Generally, the potential buy and sell signals are poor exits;
either selling out of a long position or buying to cover a
short position. By the time the momentum indicator comes
back to the zero line, most or all of the profits might have
eroded, or even worse, the trader has let a winning position
turn into a losing position.

When the momentum is reversing course and is getting back to the
zero line, that indicates that profits have been eroded. How much
of a retracement back towards the zero line before an exit is
triggered is up to the trader. Another possible alternative is
to draw a trend line;when the trend line is broken, that might
be the exit indication. Like other technical analysis indicators,
interpreting them is part science and part art form


ROC:
ROC > 0: uptrend
ROC < 0: downtrend
ROC near 0...change in trend.


TRIX:
What Is TRIX?
The triple exponential average (TRIX) indicator is an oscillator used to identify oversold and overbought markets, and it can also be used as a momentum indicator. Like many oscillators, TRIX oscillates around a zero line. When it is used as an oscillator, a positive value indicates an overbought market while a negative value indicates an oversold market. When TRIX is used as a momentum indicator, a positive value suggests momentum is increasing while a negative value suggests momentum is decreasing. Many analysts believe that when the TRIX crosses above the zero line it gives a buy signal, and when it closes below the zero line, it gives a sell signal. 
'''
