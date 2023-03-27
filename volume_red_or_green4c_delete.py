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
import sys
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
import time
from datetime import datetime

import sys
import time


start=time.time()


perda='1d'
intervla='2m'
yy=str(intervla).split('d')[0]
shiftbydays=3



##    g=input("Entr_Signal ticker: ")
perd=perda

pp=6
##pp=input("How many records? (example 5,10,12,15) over 1m,5min,15mins: ")
intervl='1m'

##ticker=input("===========  Enter ticker: =========== ")
ticker='BTC-USD'
##ticker='TSLA'
##ticker='NVDA'
#ticker='AMZN'
df = yf.download(ticker, period='2d', interval=intervla,prepost = True)
df=pd.DataFrame(df)
print(df.tail(5),'last 5 records' )
df.reset_index(inplace=True,drop=False)
df.rename(columns={'index': 'Datetime'}, inplace=True)
print(ticker)
##print(df.tail(5),'last 5 records' )
print('\n\n')
################## delete this

###################### delete this end
df['green']=""
df['greenby']=""
#################################################################


for x in df.index:

##    df['ticker'].loc[x]=ticker
    if df['Close'].loc[x]-df['Open'].loc[x] >= 0:
        df['green'].loc[x]='green33'
##        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]+.1
    #            print(x,'  ','Green','  ',df['ns'].loc[x])
    if df['Close'].loc[x]-df['Open'].loc[x] < 0:
        df['green'].loc[x]="Red33"          
##        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
##print(df,'888')
########################################################################
# getting hours,mins,date
df['s3']=''
for x in df.index:
    df['s3'].loc[x]=str(df['Datetime'].loc[x]).split(' ')[0]


# s4 captures the time.
df['s4']=''
for x in df.index:
    df['s4'].loc[x]=str(df['Datetime'].loc[x]).split(' ')[1][:5]
          

cc=df.groupby(['s3', 's4','green','Close']).sum()
df3=pd.DataFrame(cc['Volume'])
##
##df3=pd.DataFrame(cc)
df.reset_index(inplace=True,drop=False)



df3['delta']=0.0


##print(df3, '65 sing') ######### ====================================================>
df3.reset_index(inplace=True)
##print(df3, '66 sing') ######### ====================================================>
df4=df3.pivot(index=['s3','s4','Close'],columns=['green'],values=['Volume'])

df4.fillna('',inplace=True)


##print('\n\n')
##print(df4,' ------ sam')
df4=pd.DataFrame(df4)
df4.reset_index(inplace=True,drop=False) #=================================================>



##
df4['weekday']= ''
####print('\n\n')
df4['s3'] =pd.to_datetime(df4['s3'])
##df4['s3'] = df['s3'].dt.strftime('%m/%d')
df4['weekday'] =df4['s3'].dt.day_name()
df4.reset_index(inplace=True,drop=False)
df4['ticker']=''

df4['ticker']=ticker
df4['intervla']=intervla

Green_V_cts=[]
Red_V_cts=[]


##print(df4.shape)
##print(df4.iloc[:,6])

##print('\n')
for x in df4.index:
    if df4.iloc[x,5] is not '' and df4.iloc[x,5] != 0:
        Green_V_cts.append(df4.iloc[x,5])
    if df4.iloc[x,4] is not '' and df4.iloc[x,4] != 0:
        Red_V_cts.append(df4.iloc[x,4])

#################################################################################################################
print('Ticker=',ticker,'     interval=',intervla,'     current_Price=',df4['Close'].loc[df4.shape[0]-1])
d2=round(len(Green_V_cts)/df4.shape[0]*100,2)
d3=round(len(Red_V_cts)/df4.shape[0]*100,2)
print('# of Greens entire dataset: ',len(Green_V_cts),'/',df4.shape[0],'/',d2,' %')
print('# of Reds entire dataset: ',len(Red_V_cts),'/',df4.shape[0] ,'/',d3,' %')
print('# of reecords not available',round(100-(d2+d3),2),' %')
print('\n')
if round(len(Green_V_cts)/df4.shape[0]*100,2) - round(len(Red_V_cts)/df4.shape[0]*100,2) > 0:
      print("Buy_Volume more in entire Dataset, [Green-Red]=",round(d2-d3,2), '%')
else:
    print("Sell_Volume low in entire Datase, [Green-Red]=",round(d2-d3,2), '%')
print('\n\n')

for x in Green_V_cts:
    b=sum(Green_V_cts)


for x in Red_V_cts:
    c=sum(Red_V_cts)
##print('Red_sell_Volume: ',c)
print('Ticker=',ticker,'     interval=',intervla,'     current_Price=',df4['Close'].loc[df4.shape[0]-1])
d2=round(b/(b+c)*100,2)
d3=round(c/(b+c)*100,2)
d4=numerize.numerize(b-c)
print('Entire_data_records, Total Volume=', numerize.numerize(b+c))
print('Buy-Entire_data_records_Sum_of_total_Green_Vol=: ',numerize.numerize(b),'/',d2,' %')
print('Sell-Entire_data_records_Sum_of_total_Red_Vol=',numerize.numerize(c),'/',d3,' %')
print('delta_volume=',d4)
print('\n')
if round(d2-d3) > 0:
    print("Buy_Volume more in entire Dataset, [Green-Red]=",round(d2-d3,2),' %','/',d4)
else:
    print("Sell_Volume low in entire Datase, [Green-Red]=",round(d2-d3,2),' %','/',d4)

#################################################################################################################
##print(Green_cts[len(Green_cts)-5:])

print('\n\n')
##pp=input("How many records? (example 5,10,12,15) over 1m,5min,15mins: ")
ff=0
y=0
yp=0
##
for x in Green_V_cts[len(Green_V_cts)-int(pp):]:
    y +=x
##print('sum of Greens/Vol in last 5 mins:',y)

for xp in Red_V_cts[len(Red_V_cts)-int(pp):]:
    yp +=xp
##
print('Ticker=',ticker,'     interval=',intervla,'     current_Price=',df4['Close'].loc[df4.shape[0]-1])
d2=round(y/(y+yp)*100,2)
d3=round(yp/(y+yp)*100,2)
d4=numerize.numerize(y-yp)
print('Last', int(pp),' records, Total Volume=', numerize.numerize(y+yp))    
print('Buy-Last', int(pp),'_records_Sum_of_total_Green_Vol=',numerize.numerize(y),d2,'/',' %')
print('Sell-Last', int(pp),'_records_Sum_of_total_Red_Vol=', numerize.numerize(yp),d3,'/',d3,' %')
print('Last ',int(pp),' records,delta_Vol=',d4)
print('\n')
if round(d2-d3) > 0:
    print("Buy_Volume more in entire Dataset, [Green-Red]=",round(d2-d3,2),' %','/',d4)
else:
    print("Sell_Volume low in entire Datase, [Green-Red]=",round(d2-d3,2),' %','/',d4)

print('\n\n')    
#################################################################################################################

df4.columns=['l','m','b','n','i','h','f','r','x']


for x in df4.index:
    if df4['h'].loc[x] !='' and df4['h'].loc[x] != 0:
##        print('kkkk  ', df4['h'].loc[x])
        df4['h'].loc[x]=numerize.numerize(np.int64(df4['h'].loc[x]).item())
##        print('bbbb  ', df4['h'].loc[x])
        
    if df4['i'].loc[x] !='' and df4['i'].loc[x] != 0:
##        print('kkkk  ', df4['i'].loc[x])
        df4['i'].loc[x]=numerize.numerize(np.int64(df4['i'].loc[x]).item())
##        print('bbbb  ', df4['i'].loc[x])  

df4.columns=['index','s3','s4','Close','Red3','green','weekday','ticker','intervla']
print(df4,'  nnn')
