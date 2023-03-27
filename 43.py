import pandas as pd
import talib as taa
##import finta as f
from finta import TA 
import pandas_ta as ta
from numerize import numerize
import yfinance as yf
import pandas as pd
import talib as taa
import finta as f
import pandas_ta as ta
from numerize import numerize
import random
import matplotlib.pyplot as plt

##import pandas_ta as ta2
##import pandas_ta as ta2
pd.set_option('display.max_rows', None)

##import matplotlib.pyplot as plt
##import matplotlib.pyplot as plt2
##from matplotlib.axis import Axis
##from matplotlib.widg    for z in df.index:ets import Slider, Button, RadioButtons 
import numpy as np    
import sys
import warnings
import ffn


m4=['GME','TSLA']

for x in m4:
    print('\n')
    print('*****************************************************')
    print('no of tickers= ',len(m4),'    m4= ',m4)
    print(' processing ',x ,' of ',len(m4))

    
    df=yf.download(x,'2020-12-01','2024-03-30')
    df['u2']=''
    df['u3']=''

    df['upper'], df['middle'], df['lower'] = taa.BBANDS(df['Close'], timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    df['20sma'] = df['Close'].rolling(window=20).mean()
    df['stddev'] =df['Close'].rolling(window=20).std()
    df['lower_band'] = df['20sma'] - (2 * df['stddev'])
    df['upper_band'] = df['20sma'] + (2 * df['stddev'])

    df['TR'] = abs(df['High'] - df['Low'])
    df['ATR'] = df['TR'].rolling(window=20).mean()
    df['lower_keltner'] = df['20sma'] - (df['ATR'] * 1.5)
    df['upper_keltner'] = df['20sma'] + (df['ATR'] * 1.5)
    df['upper'], df['middle'], df['lower'] = taa.BBANDS(df['Close'], timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    df['ticker']=x
    

df['up']=''
df['low']=''
df['u2']=0.0
df['u3']=0.0
df['squeeze_on']=''
##    df['squeeze_on']=''
df.reset_index(inplace=True)
df.set_index('Date',inplace=True)
print(df)
##import numpy as np

for z in df.index:
    df['u2'].loc[z]=df['upper'].loc[z]-df['upper_keltner'].loc[z]
    df['u3'].loc[z]=float(df['lower'].loc[z])-float(df['lower_keltner'].loc[z])

    if df['lower_band'].loc[z] > df['lower_keltner'].loc[z] and df['upper_band'].loc[z] < df['upper_keltner'].loc[z]:
        df['squeeze_on'].loc[z]='in_squeeze'
    else:
        df['squeeze_on'].loc[z]=' '   
##df['squeeze_upper']=''
df['squeeze_lower']=''
df['squeeze_upper']=''
df['n']=''
df['p']=''
df['gm']=df.iloc[:,df.columns.get_loc('Close')].max()
df['gm']=df['gm']+20
gm2=df.shape[0]



##for z in df.index:
##if df['u2'].loc[z] < 0:
##    df['n'].loc[z]='squeeze_upper'
##else:
##    df['n'].loc[z]=''
##
##if df['u3'].loc[z] < 0:
##    df['p'].loc[z]=''
##else:
##    df['p'].loc[z]='squeeze_lower'
##    

##df=df[['Close','u2','n','u3','p','squeeze_on']]
##print(df,'jjj')

df.reset_index(inplace=True)
df.dropna(axis=0)
print(df,'jjj')
import matplotlib.pyplot as plt
p1=df.iloc[:,df.columns.get_loc('Date')]
p2=df.iloc[:,df.columns.get_loc('squeeze_on')]
p3=df.iloc[:,df.columns.get_loc('Close')]
##p5=1200-df.iloc[:,df.columns.get_loc('Close')]
p5=df['gm']
##plt.bar(df.index,df.iloc[:,df.columns.get_loc('squeeze_on')],color='cyan',width=55)
##    bx6.fill_between(p1, p2, where=(pd.to_numeric(p2) > 0), color='#00FF00')
##    bx6.fill_between(p1, p2, where=(pd.to_numeric(p2) < 0), color='#ff0000')
##plt.fill_between(p1, p2,2*p2, color='#00FF00')
plt.plot(df.iloc[:,df.columns.get_loc('Date')],df.iloc[:,df.columns.get_loc('Close')], 'darkviolet', label='Close',linewidth=1)
plt.plot(p1,p2)
plt.fill_between(p1, p3,p5,where= df.iloc[:,df.columns.get_loc('squeeze_on')] != ' ',  color='cyan')
plt.xlabel("Date")
plt.ylabel("Total Population")
plt.tight_layout()



plt.show()    
    
