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
intervla='1m'
yy=str(intervla).split('d')[0]
shiftbydays=3



##    g=input("Entr_Signal ticker: ")
perd=perda
intervl='1m'

##ticker=input("===========  Enter ticker: =========== ")
ticker='BTC-USD'
##ticker='TSLA'
##ticker='NVDA'
#ticker='AMZN'
df = yf.download(ticker, period='1d', interval='1m',prepost = True)
df=pd.DataFrame(df)

df.reset_index(inplace=True,drop=False)
df.rename(columns={'index': 'Datetime'}, inplace=True)
print(ticker)
print(df.tail(5),'last 5 records' )
print('\n\n')
################## delete this
##df['s3']=''
##i=0
##for x in df.index:
##    df['s3'].loc[x]=str(df['Datetime'].loc[x]).split(' ')[1][:5]
##    print('nnnnnn  ',df['s3'].loc[x])
##    i=i+1
##    if i > 5:
##        break
##
##sys.exit()

###################### delete this end
df['Candlea']=''
df['*']=''
for x in df.index:    
    df['Candlea'].loc[x]=df['High'].loc[x]-df['Open'].loc[x]
    df['*'].loc[x]='*'

df['Opena']=''
df['green']=''
df['greenby']=''
df['compare_d']=''

df['Candle']=''
df['direct']=''
df['down']=''
df['a_Close']=''
df['a_High']=''
df['a_Low']=''
df['a_Open']=''
df['HA']=''
df['upward_pressure']=''
df['downward_pressure']=''
df['HA->']=''
df['MA->']=''
df['CCI/RSI->']=''
df['Close->']=''
df['intervl']=''
df['ticker']=''



df['PLUS_DI']=ta.PLUS_DI(df['High'],df['Low'],df['Close'], timeperiod=14)
df['PLUS_DM']=ta.PLUS_DM(df['High'],df['Low'], timeperiod=14)
#################################################################
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


########################################################################
df['Closev'] = (1/df['Close'])*(100)
for x in df.index:
    df['Closev'].loc[x]=df['Closev'].loc[x]
    df['upward_pressure'].loc[x]=df['PLUS_DM'].loc[x]-df['PLUS_DI'].loc[x]
    df['downward_pressure'].loc[x]=df['PLUS_DI'].loc[x]-df['PLUS_DM'].loc[x]
    df['Candle'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]

    df['HA->'].loc[x]='HA->'
    df['Close->'].loc[x]='Close->'
    df['*'].loc[x]='*'
    df['MA->'].loc[x]='MA->'
    df['CCI/RSI->']='CCI/RSI->'
    
    

    df['intervl'].loc[x]=intervl
    df['ticker'].loc[x]=ticker
##    df['Close_d_ch'].loc[x]=df['Close'].loc[x]-df['Close_d'].loc[x]
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


df['s3']=''
for x in df.index:
    df['s3'].loc[x]=str(df['Datetime'].loc[x]).split(' ')[0]


# s4 captures the time.
df['s4']=''
for x in df.index:
    df['s4'].loc[x]=str(df['Datetime'].loc[x]).split(' ')[1][:5]
          
##print(df)
cc=df.groupby(['s3', 'green','s4','Close']).sum()
df3=pd.DataFrame(cc['Volume'])
df3.reset_index(inplace=True,drop=False)
##print(df3, '?? sing')
df3['delta']=0.0
df3['ticker']=''
##df3['Closex']=''
df3['sold_buy_%']=''


############## calculate % of volume ###############3333
##for x in df3.index:
##    if df3['s3'].loc[x]==df3['s3'].shift(1).loc[x]:
##        df3['delta'].loc[x]=df3['Volume'].shift(1).loc[x]-df3['Volume'].loc[x]
##        if df3['delta'].loc[x] < 0:
##            df3['sold_buy_%'].loc[x]=-1*(df3['Volume'].loc[x]/df3['Volume'].shift(1).loc[x])*100
##        if df3['delta'].loc[x] > 0:
##            df3['sold_buy_%'].loc[x]=(df3['Volume'].loc[x]/df3['Volume'].shift(1).loc[x])*100    
##        df3['ticker'].loc[x]=ticker
## ############ calculate % of volume ###############3333

############ calculate % of volume ###############3333
for x in df3.index:
    
##    if df3['s3'].loc[x]==df3['s3'].shift(1).loc[x]:
    if df3['Volume'].shift(1).loc[x] > 0:
        df3['delta'].loc[x]=df3['Volume'].shift(1).loc[x]-df3['Volume'].loc[x]
    else:
        df3['delta'].loc[x]=0
    if df3['delta'].loc[x] < 0:
        if df3['Volume'].shift(1).loc[x]*100 < .0001 or df3['Volume'].shift(1).loc[x]*100 is None:
            pass
##            df3['sold_buy_%'].loc[x]=-1*(df3['Volume'].loc[x])/(df3['Volume'].shift(1).loc[x]+1)*100
        if df3['Volume'].shift(1).loc[x]*100 > 0:
            df3['sold_buy_%'].loc[x]=-1*(df3['Volume'].loc[x])/df3['Volume'].shift(1).loc[x]*100

    if df3['delta'].loc[x] > 0 :
        if df3['Volume'].shift(1).loc[x]*100 < .0001 or df3['Volume'].shift(1).loc[x]*100 is None:
            pass
##            df3['sold_buy_%'].loc[x]=(df3['Volume'].loc[x])/(df3['Volume'].shift(1).loc[x]+1)*100 
        if df3['Volume'].shift(1).loc[x]*100 > 0:
            df3['sold_buy_%'].loc[x]=(df3['Volume'].loc[x])/df3['Volume'].shift(1).loc[x]*100    
    df3['ticker'].loc[x]=ticker
 ############ calculate % of volume ###############3333
##print(df3,' ggg')
##sys.exit()


df3.reset_index(inplace=True)

df4=df3.pivot(index=['s3','s4','ticker','Volume','Close'],columns=['green'],values=['sold_buy_%','Volume','delta'])

df4.fillna('',inplace=True)

##print('\n\n')
##print(df4,' ------ sam')
df4=pd.DataFrame(df4)
df4.reset_index(inplace=True,drop=False)

##print(df4,' cccc')
##print(df4.shape,' 32cccc')
##print(df4.iloc[:,4],' dffnnnn')
df4.drop(df4.columns[[6,5,9,10]], axis=1,inplace=True)

############## @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
##to_datetime()


df4["s5"] = ''
##print('\n\n')
df4['s3'] =pd.to_datetime(df4['s3'])
##df4['s3'] = df['s3'].dt.strftime('%m/%d')
df4['weekday'] =df4['s3'].dt.day_name()



Green_V_cts=[]
Red_V_cts=[]


##print(df4.shape)
##print(df4.iloc[:,6])

##print('\n')
for x in df4.index:
    if df4.iloc[x,6] is not '' and df4.iloc[x,6] != 0:
        Green_V_cts.append(df4.iloc[x,6])
    if df4.iloc[x,5] is not '' and df4.iloc[x,6] != 0:
        Red_V_cts.append(df4.iloc[x,5])

##print(Green_V_cts,' sunno')
##print('\n\n')
print(ticker)
print('# of Greens entire dataset: ',len(Green_V_cts),'/',df4.shape[0],'/',round(len(Green_V_cts)/df4.shape[0]*100,2),' %')
print('# of Reds entire dataset: ',len(Red_V_cts),'/',df4.shape[0] ,'/',round(len(Red_V_cts)/df4.shape[0]*100,2),' %')
print('\n\n')

for x in Green_V_cts:
    b=sum(Green_V_cts)


for x in Red_V_cts:
    c=sum(Red_V_cts)
##print('Red_sell_Volume: ',c)
print(ticker)
print('Entire_data_records, Total Volume=', numerize.numerize(b+c))
print('Buy-Entire_data_records_Sum_of_total_Green_Vol=: ',numerize.numerize(b),'/',round(b/(b+c)*100,2),' %')
print('Sell-Entire_data_records_Sum_of_total_Red_Vol=',numerize.numerize(c),'/',round(c/(b+c)*100,2),' %')
print('delta_volume=',numerize.numerize(b-c))
##########################################################################################
##print(Green_cts[len(Green_cts)-5:])

print('\n\n')

ff=0
y=0
yp=0
##
for x in Green_V_cts[len(Green_V_cts)-5:]:
    y +=x
##print('sum of Greens/Vol in last 5 mins:',y)

for xp in Red_V_cts[len(Red_V_cts)-5:]:
    yp +=xp
##
print(ticker)
print('Last 5 records, Total Volume=', numerize.numerize(y+yp))    
print('Buy-Last 5_records_Sum_of_total_Green_Vol=',numerize.numerize(y),'/',round(y/(y+yp)*100,2),' %')
print('Sell-Last 5_records_Sum_of_total_Red_Vol=', numerize.numerize(yp),'/',round(yp/(y+yp)*100,2),' %')
print('Last 5 records,delta_Vol=',numerize.numerize(y-yp))



df4.columns=['v','b','i','t','j','n','jg','kk','jjff']
##print(df4)
##print('\n\n')
##sys.exit()
##df4.rename(columns={df4.columns[3]: 'new'})
##df4.columns=['a','Ticker','%','Vol_Buy_Green','Vol_Sold_Red','Delta','Day']
df4.reset_index(inplace=True)

for x in df4.index:
    df4['t'].loc[x]=numerize.numerize(np.int64(df4['t'].loc[x]).item())
    if df4['jg'].loc[x] !='':
        df4['jg'].loc[x]=numerize.numerize(np.int64(df4['jg'].loc[x]).item())
    if df4['n'].loc[x] !='':
        df4['n'].loc[x]=numerize.numerize(np.int64(df4['n'].loc[x]).item())    


print(df4)
