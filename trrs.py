import talib as ta
import yfinance as yf
import pandas as pd
import datetime as dt
import sys
import numpy as np
from talib import stream
import matplotlib.pyplot as plt
def m(x):
    x='pupu yar'
    return(x)


pd.options.display.max_columns=155
pd.options.display.max_rows=6500000
ticker='TSLA'
u=[]
df = yf.download(ticker, '2021-05-1','2021-05-27', index=False)
##print(df.shape)
df.reset_index(inplace = True)

df['day'] = df['Date'].dt.day_name()
df['ticker']=ticker
##df['Volume']=(df['Volume']/1000)
##df['Date'] = df['Date'].resample(rule='D').mean()
df['Volume']=df['Volume'].round(1)
df['Simple MA_3'] = ta.SMA(df['Close'].astype(int),3)
df['Simple MA_10'] = ta.SMA(df['Close'].astype(int),10)
df['Day_swing']=df['High']-df['Low']
df['Yest_Close']=df['Close'].shift(+1)
df['delta']=df['Close']-df['Yest_Close']
df['delta_cl_op']=df['Open']-df['Yest_Close']
df['*']='*'
##df['CCI']=ta.CCI(df['High'], df['Low'], df['Close'], timeperiod=3)
#Commodity Channel Index (Momentum Indicators)
df['ADX']=ta.ADX(df['High'], df['Low'], df['Close'], timeperiod=3)
##Average Directional Movement Index (Momentum Indicators)
df['CDLSHORTLINE']=ta.CDLSHORTLINE(df['Open'],df['High'],df['Low'],df['Close'])
#Aroon (Momentum Indicators)
##df['CDL2CROWS']=ta.CDL2CROWS(df['High'], df['Low'], df['Close'], timeperiod=3)
#Two Crows (Pattern Recognition)
##df['CDLHARAMI']=ta.CDLHARAMI(df['High'], df['Low'], df['Close'], timeperiod=3)
#Two Crows (Pattern Recognition)


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
print(df)




'''
CDL2CROWS(df['Open'],df['High'], df['Low'], df['Close'])
CDL3BLACKCROWS(df['Open'],df['High'], df['Low'], df['Close'])
CDL3INSIDE(df['Open'],df['High'], df['Low'], df['Close'])
CDL3LINESTRIKE(df['Open'],df['High'], df['Low'], df['Close'])
CDL3OUTSIDE(df['Open'],df['High'], df['Low'], df['Close'])
CDL3STARSINSOUTH(df['Open'],df['High'], df['Low'], df['Close'])
CDL3WHITESOLDIERS(df['Open'],df['High'], df['Low'], df['Close'])
CDLABANDONEDBABY(df['Open'],df['High'], df['Low'], df['Close'])
CDLADVANCEBLOCK(df['Open'],df['High'], df['Low'], df['Close'])
CDLBELTHOLD(df['Open'],df['High'], df['Low'], df['Close'])
CDLBREAKAWAY(df['Open'],df['High'], df['Low'], df['Close'])
CDLCLOSINGMARUBOZU(df['Open'],df['High'], df['Low'], df['Close'])
CDLCONCEALBABYSWALL(df['Open'],df['High'], df['Low'], df['Close'])
CDLCOUNTERATTACK(df['Open'],df['High'], df['Low'], df['Close'])
CDLDARKCLOUDCOVER(df['Open'],df['High'], df['Low'], df['Close'])
CDLDOJI(df['Open'],df['High'], df['Low'], df['Close'])
CDLDOJISTAR(df['Open'],df['High'], df['Low'], df['Close'])
CDLDRAGONFLYDOJI(df['Open'],df['High'], df['Low'], df['Close'])
CDLENGULFING(df['Open'],df['High'], df['Low'], df['Close'])
CDLEVENINGDOJISTAR(df['Open'],df['High'], df['Low'], df['Close'])
CDLEVENINGSTAR(df['Open'],df['High'], df['Low'], df['Close'])
CDLGAPSIDESIDEWHITE(df['Open'],df['High'], df['Low'], df['Close'])
CDLGRAVESTONEDOJI(df['Open'],df['High'], df['Low'], df['Close'])
CDLHAMMER(df['Open'],df['High'], df['Low'], df['Close'])
CDLHANGINGMAN(df['Open'],df['High'], df['Low'], df['Close'])
CDLHARAMI(df['Open'],df['High'], df['Low'], df['Close'])
CDLHARAMICROSS(df['Open'],df['High'], df['Low'], df['Close'])
CDLHIGHWAVE(df['Open'],df['High'], df['Low'], df['Close'])
CDLHIKKAKE(df['Open'],df['High'], df['Low'], df['Close'])
CDLHIKKAKEMOD(df['Open'],df['High'], df['Low'], df['Close'])
CDLHOMINGPIGEON(df['Open'],df['High'], df['Low'], df['Close'])
CDLIDENTICAL3CROWS(df['Open'],df['High'], df['Low'], df['Close'])
CDLINNECK(df['Open'],df['High'], df['Low'], df['Close'])
CDLINVERTEDHAMMER(df['Open'],df['High'], df['Low'], df['Close'])
CDLKICKING(df['Open'],df['High'], df['Low'], df['Close'])
CDLKICKINGBYLENGTH(df['Open'],df['High'], df['Low'], df['Close'])
CDLLADDERBOTTOM(df['Open'],df['High'], df['Low'], df['Close'])

CDLLONGLEGGEDDOJI(df['Open'],df['High'], df['Low'], df['Close'])
CDLLONGLINE(df['Open'],df['High'], df['Low'], df['Close'])
CDLMARUBOZU(df['Open'],df['High'], df['Low'], df['Close'])
CDLMATCHINGLOW(df['Open'],df['High'], df['Low'], df['Close'])
CDLMATHOLD(df['Open'],df['High'], df['Low'], df['Close'])
CDLMORNINGDOJISTAR(df['Open'],df['High'], df['Low'], df['Close'])
CDLMORNINGSTAR(df['Open'],df['High'], df['Low'], df['Close'])
CDLONNECK(df['Open'],df['High'], df['Low'], df['Close'])
CDLPIERCING(df['Open'],df['High'], df['Low'], df['Close'])
CDLRICKSHAWMAN(df['Open'],df['High'], df['Low'], df['Close'])
CDLRISEFALL3METHODS(df['Open'],df['High'], df['Low'], df['Close'])
CDLSEPARATINGLINES(df['Open'],df['High'], df['Low'], df['Close'])
CDLSHOOTINGSTAR(df['Open'],df['High'], df['Low'], df['Close'])
CDLSHORTLINE(df['Open'],df['High'], df['Low'], df['Close'])
CDLSPINNINGTOP(df['Open'],df['High'], df['Low'], df['Close'])
CDLSTALLEDPATTERN(df['Open'],df['High'], df['Low'], df['Close'])
CDLSTICKSANDWICH(df['Open'],df['High'], df['Low'], df['Close'])
CDLTAKURI(df['Open'],df['High'], df['Low'], df['Close'])
CDLTASUKIGAP(df['Open'],df['High'], df['Low'], df['Close'])
CDLTHRUSTING(df['Open'],df['High'], df['Low'], df['Close'])
CDLTRISTAR(df['Open'],df['High'], df['Low'], df['Close'])
CDLUNIQUE3RIVER(df['Open'],df['High'], df['Low'], df['Close'])
CDLUPSIDEGAP2CROWS(df['Open'],df['High'], df['Low'], df['Close'])
CDLXSIDEGAP3METHODS(df['Open'],df['High'], df['Low'], df['Close'])



##ADX is momentum strength.
##ADX Value	Trend Strength
##0-25	Absent or Weak Trend
##25-50	Strong Trend
##50-75	Very Strong Trend
##75-100	Extremely Strong Trend

'''
