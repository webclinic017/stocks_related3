import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import yfinance as yf
import talib as taa
from finta import TA
perda='2d'
intervla='30m'
x='BTC-USD'
##    x='spy'
##    x='tsla'
##    x='^dji'
##    x='^gspc'
##    x='ndx'
df=yf.download(x, period=perda, interval=intervla,prepost = False)
df.reset_index(inplace=True)
df['v']=df['Volume']
df['tp2']=''
df['tp2']=df['Close']+df['Low']+df['High']
df['tp2']=df['tp2'].div(3).values
df['v']=np.cumsum(df['v'])

df['vwap']=(df['tp2']*df['v']).cumsum()/df['v'].cumsum()
df['SAR']=TA.SAR(df,0.02,0.2)
df['EMA_7'] = taa.EMA(df['Close'], timeperiod=7)
df['EMA_21'] = taa.EMA(df['Close'], timeperiod=21)
df['EMA_50'] = taa.EMA(df['Close'], timeperiod=50)
df['EMA_100'] = taa.EMA(df['Close'], timeperiod=100)
df['EMA_200'] = taa.EMA(df['Close'], timeperiod=200)
df['BB_upperband'], df['BB_middleband'], df['BB_lowerband'] = taa.BBANDS(df['Close'], timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
fig, ax = plt.subplots()
print(type(fig),'   ',type(ax))
print(help(plt))
s1=plt.plot(df['vwap'],scalex=True,scaley=True)
s2=plt.plot(df['Close'],scalex=True,scaley=True)
plt.legend()
plt.gca()
plt.title('vwap/Close')
###############3
fig, ax = plt.subplots()
print(type(fig),'   ',type(ax))
print(help(plt))
s1a=plt.plot(df['Low'],scalex=True,scaley=True,label='Low')
s2a=plt.plot(df['High'],scalex=True,scaley=True,label='High')
plt.legend()
plt.gca()
plt.title('Low/High')
###############3
fig, ax = plt.subplots()
print(type(fig),'   ',type(ax))
print(help(plt))
s1=plt.plot(df['Open'],scalex=True,scaley=True,label='Open')
s2=plt.plot(df['Close'],scalex=True,scaley=True,label='Close')
plt.legend()
plt.gca()
plt.title('Open/Close')
#################
plt.show()
