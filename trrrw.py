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

m=['spy','msft','tsla','ndx','docu','mrna']
b=15
k=4

df = yf.download(m[k],start=str('2022-02-')+str(b),end=str('2022-02-')+str(b+1),interval='1m')
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

############# Sell condition for uptrend ########################
for z in range(b6,df.shape[0]):
    if df['Close'].loc[z] - buy_price_gg > 2.5:
##    if (df['Close'].loc[z] < df['vwap'].loc[z] or\
##       df['ADL'].loc[z] < 0) or (df['Close'].loc[z] < df['Close'].loc[b6]) or \
##       df['MOM'].loc[z] < df['MOM'].shift(1).loc[z]\
##       :
        sell_price_gg=df['Close'].loc[z]
        
        s7=z
##    else:  df['Close'].loc[z] < df['Close'].loc[z]-df['Close'].shift(1).loc[z]*.2:
##        s7=''
##        print("nnnnn")
##print(df.iloc[2,df.columns.get_loc('ticker')])
#####################################################
##print(m[k],' uptrend',buy_price_ggb)
##print('\n\n\n')
if sell_price_gg > buy_price_gg:
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






































###<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Buy condition for Downtrend >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
##for x in df.index:
##    df['i'].loc[x]=i
##    df['s3'].loc[x]=str(df['Datetime'].loc[x]).split(' ')[0]
##    df['s2'].loc[x]=str(df['Datetime'].loc[x]).split(' ')[1][0:5]
##    if df['Close'].loc[x]-df['vwap'].loc[x] < 0 and df['Close'].shift(1).loc[x]-df['vwap'].shift(1).loc[x] > 0 and df['MOM'].loc[x] < 0\
##       df['ADL'].loc[x] < 0 and df['ADX'].loc[x] >25:
##        df['Close_vwap_up']=1
##        buy_price_gg=df['Close'].loc[x]
##        s6=x
#######################################################
##
############### Sell condition for Downtrend ########################
##for x in range(b6,df.shape[0]):        
##    if df['Close'].loc[x]-df['vwap'].loc[x] > 0 and df['Close'].shift(1).loc[x]-df['vwap'].shift(1).loc[x] > 0 and \
##       df['Close'].loc[x]-buy_price_gg > 0:    
##        df['Close_vwap_up']=-1
##        s7=x
##    else:
##        s7=''
##
#######################################################
##print('For uptrend b6=',s6,'  b7=',s7)
## $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
## $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$        
##sys.exit()

##df.drop('Datetime', axis=1, inplace=True)

##df['Datetime']=df['s3']+'-'+df['s2']
##df.set_index(df['Datetime'],inplace=True)








fig1, (ax1, ax2,ax3,ax4,ax6,bx5,bx6) = plt.subplots(7, 1,sharex=True)
##fig1.suptitle(df.iloc[1,df.columns.get_loc('ticker')], fontsize=5)
##fig1.suptitle(df.iloc[4,df.columns.get_loc('MOM')], fontsize=5)

##ax2.vlines(df.iloc[b6,df.columns.get_loc('s2')],\
##               df.iloc[:,df.columns.get_loc('Close')].min(), \
##               df.iloc[:,df.columns.get_loc('Close')].max(),\
##               linestyles ="dashed", colors ="k", label = 'uptrend')
##
##ax2.vlines(df.iloc[b7,df.columns.get_loc('s2')],\
##               df.iloc[:,df.columns.get_loc('Close')].min(), \
##               df.iloc[:,df.columns.get_loc('Close')].max(),\
##               linestyles ="dashed", colors ="r", label = 'downtrend')




ax1.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('adx')]))
ax1.legend(['adx'],loc=3, fontsize = 'x-small')
ax2.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('Close')]))
ax2.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('vwap')]),color='Green', marker='v', linestyle='dashed',\
             linewidth=0, markersize=2)
ax2.legend([['Close','vwap']],loc=3, fontsize = 'x-small')


##ax3.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('p2')]))
ax4.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('p2')],color='red',width=2)
ax4.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('MOM')],color='green',width=2)
ax4.legend([['MOM','p2','ADL']],loc=3, fontsize = 'x-small')

ax4.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('ADL')]))
ax3.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('chop')]))
ax3.legend(['chop'],loc=3, fontsize = 'x-small')
##############################################
p1=df.iloc[:,df.columns.get_loc('s2')]
p2=df.iloc[:,df.columns.get_loc('macd')] 
ax6.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('macd')]))

ax6.legend(['macd'],loc=3, fontsize = 'x-small')
ax6.fill_between(p1, p2, p2+325, where=(pd.to_numeric(p2) > 0), color='#00FF00')
ax6.fill_between(p1, p2,p2-5, where=(pd.to_numeric(p2) < 0), color='#ff0000')
ax6.legend(['macd'],loc=3, fontsize = 'x-small')
ax6.hlines(70, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=4, color='green')

#################################################
p1=df.iloc[:,df.columns.get_loc('s2')]
p2=df.iloc[:,df.columns.get_loc('adx')]
p5a=df.iloc[:,df.columns.get_loc('EMA-2150')]
bx5.fill_between(p1, p5a.min(),p5a, where=(pd.to_numeric(p2) > 25), color='#00e5ff')
bx5.legend([['EMA-2150','adx>25']],loc=3, fontsize = 'x-small')

bx5.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA-2150')],color='red',width=2)



##dfp=df.loc[df['Close']>df['SAR']]
##dfg=df.loc[df['Close']<df['SAR']]
##
##bx7.plot(dfp.iloc[:,bb],pd.to_numeric(dfp.iloc[:,dfp.columns.get_loc('SAR')]+7),color='Green', marker='v', linestyle='dashed',\
##             linewidth=0, markersize=2)
##bx7.plot(dfg.iloc[:,bb],pd.to_numeric(dfg.iloc[:,dfg.columns.get_loc('SAR')]-7),color='Red', marker='^', linestyle='dashed',\
##             linewidth=0, markersize=2)


ax1.set_ylabel('adx',loc='top',labelpad=4)
ax2.set_ylabel('Close',loc='top',labelpad=4)
ax3.set_ylabel('chop',loc='top',labelpad=4)
ax4.set_ylabel('p2',loc='top',labelpad=4)
##    bx4.set_ylabel('EMA-1021',loc='top',labelpad=4)

######################################################################
    # adx


print(df,' 888866v')    
p1=df.iloc[:,df.columns.get_loc('s2')]
p2=df.iloc[:,df.columns.get_loc('adx')]
p2a=df.iloc[:,df.columns.get_loc('Close_vwap')]
bx6.fill_between(p1, p2a-65,p2a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')


bx6.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA_3_vwap')]))
bx6.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA_5_vwap')]))
bx6.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA_10_vwap')]))
bx6.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA_21_vwap')]))
bx6.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA_50_vwap')]))
bx6.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('SARx')]))
bx6.fill_between(p1, p2, where=(pd.to_numeric(p2) > 0), color='#00FF00')
bx6.fill_between(p1, p2, where=(pd.to_numeric(p2) < 0), color='#ff0000')
bx6.legend(['Close_vwap','EMA_3_vwap','EMA_5_vwap','EMA_10_vwap','EMA_21_vwap','EMA_50_vwap','SARx'],loc=2, fontsize = 'x-small')
##    ax3.hlines(0, df.iloc[:,43].min(), df.iloc[:,43].max(), lw=1, color='black')
bx6.hlines(0, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')
bx6.set_ylabel('EMA_5_vwap',loc='top',labelpad=1,fontsize=5)
bx6.legend(['EMA_5_vwap'],loc=3, fontsize = 'x-small')

######################################################################
###############################################################################
fig2,(bx20,bx21,bx22,bx2,bx3,bx4,bx5,bx6,bx7,bx8,bx9) = plt.subplots(11,1,sharex=True)
fig2.suptitle('baba8', fontsize=5)

clrs2bb=[];clrsb=[];clrs2b=[];clrs3b=[];clrs4b=[];clrs5b=[];clrs6b=[];clrs7b=[]
for x in df.index:
##    print(df.loc[x,'Close_vwap'])
    if df.loc[x,'Close_vwap'] < 0:
        clrs2bb.append('red')
    elif df.loc[x,'Close_vwap'] >= 0:
        clrs2bb.append('green')


    
    if df.loc[x,'EMA_3_vwap'] < 0:
        clrsb.append('red')
    elif df.loc[x,'EMA_3_vwap'] >= 0:
        clrsb.append('green')
        
    if df.loc[x,'EMA_5_vwap'] < 0:
        clrs2b.append('red')
    elif df.loc[x,'EMA_5_vwap'] >= 0:
        clrs2b.append('green')
        
    if df.loc[x,'EMA_10_vwap'] < 0:
        clrs3b.append('red')
    elif df.loc[x,'EMA_10_vwap'] >= 0:
        clrs3b.append('green')
        
    if df.loc[x,'EMA_21_vwap'] < 0:
        clrs4b.append('red')
    elif df.loc[x,'EMA_21_vwap'] >= 0:
        clrs4b.append('green')

    if df.loc[x,'EMA_50_vwap'] < 0:
        clrs5b.append('red')
    elif df.loc[x,'EMA_50_vwap'] >= 0:
        clrs5b.append('green')

    if df.loc[x,'EMA_100_vwap'] < 0:
        clrs6b.append('red')
    elif df.loc[x,'EMA_100_vwap'] >= 0:
        clrs6b.append('green')

    if df.loc[x,'EMA_200_vwap'] < 0:
        clrs7b.append('red')
    elif df.loc[x,'EMA_200_vwap'] >= 0:
        clrs7b.append('green')      


bx21.plot(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('Close')])
bx21.plot(df.iloc[:,bb],(df.iloc[:,df.columns.get_loc('vwap')]),\
         color='blue', marker='o', linestyle='dashed',\
         linewidth=1, markersize=1)

bx21.legend(['vwap'],loc=3, fontsize = 'x-small')
bx20.plot(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_3')])
bx20.plot(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_5')])
bx20.plot(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_10')])
##bx20.plot(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_21')])
##bx20.plot(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_50')])
##bx20.plot(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_100')])
##bx20.plot(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_200')])
bx20.plot(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('Close')])
bx20.legend(['EMA3/EMA5/EMA10/Close'],loc=3, fontsize = 'x-small')

bx22.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('Close_vwap')],color=clrsb,width=2)
bx22.legend(['Close_vwap'],loc=3, fontsize = 'x-small')
bx2.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_3_vwap')],color=clrsb,width=2)
bx3.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_5_vwap')],color=clrs2b,width=2)
bx4.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_10_vwap')],color=clrs3b,width=2)
bx5.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_21_vwap')],color=clrs4b,width=2)
bx6.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_50_vwap')],color=clrs5b,width=2)
bx7.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_100_vwap')],color=clrs6b,width=2)
bx8.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_200_vwap')],color=clrs7b,width=2)              


bx2.legend(['EMA_3_vwap'],loc=3, fontsize = 'x-small')
bx3.legend(['EMA_5_vwap'],loc=3, fontsize = 'x-small')
bx4.legend(['EMA_10_vwap'],loc=3, fontsize = 'x-small')
bx5.legend(['EMA_21_vwap'],loc=3, fontsize = 'x-small')
bx6.legend(['EMA_50_vwap'],loc=3, fontsize = 'x-small')
bx7.legend(['EMA_100_vwap'],loc=3, fontsize = 'x-small')
bx8.legend(['EMA_200_vwap'],loc=3, fontsize = 'x-small')

bx21.set_ylabel(['Close','vwap'],loc='top',labelpad=1,fontsize=5)
bx22.set_ylabel('Close_vwap',loc='top',labelpad=1,fontsize=5)
bx2.set_ylabel('EMA_3_vwap',loc='top',labelpad=1,fontsize=5)
bx3.set_ylabel('EMA_5_vwap',loc='top',labelpad=1,fontsize=5)
bx4.set_ylabel('EMA_10_vwap',loc='top',labelpad=1,fontsize=5)
bx5.set_ylabel('EMA_21_vwap',loc='top',labelpad=1,fontsize=5)
bx6.set_ylabel('EMA_50_vwap',loc='top',labelpad=1,fontsize=5)
bx7.set_ylabel('EMA_100_vwap',loc='top',labelpad=1,fontsize=5)
bx7.set_ylabel('EMA_200_vwap',loc='top',labelpad=1,fontsize=5)



## 44
##################################################
###############################################################################
fig3,(cx20,cx21,cx22,cx2,cx3,cx4,cx5,cx6,cx7,cx8,cx9) = plt.subplots(11,1,sharex=True)
fig3.suptitle('baba8', fontsize=5)

clrs2bb=[];clrsb=[];clrs2b=[];clrs3b=[];clrs4b=[];clrs5b=[];clrs6b=[];clrs7b=[]
for x in df.index:
##    print(df.loc[x,'Close_vwap'])
    if df.loc[x,'Close_vwap'] < 0:
        clrs2bb.append('red')
    elif df.loc[x,'Close_vwap'] >= 0:
        clrs2bb.append('green')


    
    if df.loc[x,'EMA-35'] < 0:
        clrsb.append('red')
    elif df.loc[x,'EMA-35'] >= 0:
        clrsb.append('green')
        
    if df.loc[x,'EMA-510'] < 0:
        clrs2b.append('red')
    elif df.loc[x,'EMA-510'] >= 0:
        clrs2b.append('green')
        
    if df.loc[x,'EMA-1021'] < 0:
        clrs3b.append('red')
    elif df.loc[x,'EMA-1021'] >= 0:
        clrs3b.append('green')
        
    if df.loc[x,'EMA-2150'] < 0:
        clrs4b.append('red')
    elif df.loc[x,'EMA-2150'] >= 0:
        clrs4b.append('green')

    if df.loc[x,'SARx'] < 0:
        clrs5b.append('red')
    elif df.loc[x,'SARx'] >= 0:
        clrs5b.append('green')

    if df.loc[x,'EMA_100_vwap'] < 0:
        clrs6b.append('red')
    elif df.loc[x,'EMA_100_vwap'] >= 0:
        clrs6b.append('green')

    if df.loc[x,'EMA_200_vwap'] < 0:
        clrs7b.append('red')
    elif df.loc[x,'EMA_200_vwap'] >= 0:
        clrs7b.append('green')      


cx21.plot(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('Close')])
cx21.plot(df.iloc[:,bb],(df.iloc[:,df.columns.get_loc('vwap')]),\
         color='blue', marker='o', linestyle='dashed',\
         linewidth=1, markersize=1)

cx21.legend(['vwap'],loc=3, fontsize = 'x-small')
cx20.plot(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_3')])
cx20.plot(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_5')])
cx20.plot(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_10')])
##cx20.plot(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_21')])
##cx20.plot(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_50')])
##cx20.plot(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_100')])
##cx20.plot(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_200')])
cx20.plot(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('Close')])
cx20.legend(['EMA3/EMA5/EMA10/Close'],loc=3, fontsize = 'x-small')

cx22.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('Close_vwap')],color=clrsb,width=2)
cx22.legend(['Close_vwap'],loc=3, fontsize = 'x-small')
cx2.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA-35')],color=clrsb,width=2)
cx3.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA-510')],color=clrs2b,width=2)
cx4.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA-1021')],color=clrs3b,width=2)
cx5.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA-2150')],color=clrs4b,width=2)
cx6.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('SARx')],color=clrs5b,width=2)
cx7.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_100_vwap')],color=clrs6b,width=2)
cx8.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_200_vwap')],color=clrs7b,width=2)              


cx2.legend(['EMA-35'],loc=3, fontsize = 'x-small')
cx3.legend(['EMA-510'],loc=3, fontsize = 'x-small')
cx4.legend(['EMA-1021'],loc=3, fontsize = 'x-small')
cx5.legend(['EMA-2150'],loc=3, fontsize = 'x-small')
cx6.legend(['SARx'],loc=3, fontsize = 'x-small')
cx7.legend(['EMA_100_vwap'],loc=3, fontsize = 'x-small')
cx8.legend(['EMA_200_vwap'],loc=3, fontsize = 'x-small')

cx21.set_ylabel(['Close','vwap'],loc='top',labelpad=1,fontsize=5)
cx22.set_ylabel('Close_vwap',loc='top',labelpad=1,fontsize=5)
cx2.set_ylabel('EMA-35',loc='top',labelpad=1,fontsize=5)
cx3.set_ylabel('EMA-510',loc='top',labelpad=1,fontsize=5)
cx4.set_ylabel('EMA-1021',loc='top',labelpad=1,fontsize=5)
cx5.set_ylabel('EMA-2150',loc='top',labelpad=1,fontsize=5)
cx6.set_ylabel('SARx',loc='top',labelpad=1,fontsize=5)
cx7.set_ylabel('EMA_100_vwap',loc='top',labelpad=1,fontsize=5)
cx7.set_ylabel('EMA_200_vwap',loc='top',labelpad=1,fontsize=5)



## 45
################################################## 



##    plt.show()
##    plt2.legend(['Close'])          
##    plt2.show()
import time
##    plt.show()




plt.show()
    
##print(sti.columns)

##print(help(ta2.trend.adx))
##df = yf.download('tsla',start='2022-02-15',end='2022-02-16',interval='1m')
####df['sti'] = ta.supertrend(df['High'], df['Low'], df['Close'], 7, 3)
####df['kc'] = ta.mom(df['Close'])
####df['st']=ta.(df['High'], df['Low'], df['Close'], length=7, multiplier=3, offset=4)
##df['st']=ta2.trend.adx(df['High'], df['Low'], df['Close'], length=7, scalar=100, drift=1,offset=0 )
##print(df['kc'])
##'''
##print(help(f.TA.KAMA))
##
##df['ATR']=f.TA.ATR(df)
##
####df['Super_Up'] = (df['High'] + df['Low'] / 2 + 0.1  *  df['ATR'])
####df['Up'] = (df['High'] + df['Low'] / 2 + 0.1  *  df['ATR'])
####df['Down'] = (df['High'] + df['Low'] / 2 - 0.1  *  df['ATR'])
##
##df['KAMA']=f.TA.KAMA(df,15,True)
##
##
##
##
##
##df['ADX']=f.TA.ADX(df,14,True)
##df['MOM']=f.TA.MOM(df,10,'close')
##df['ADL']=f.TA.ADL(df)
##df['VFI']=f.TA.VFI(df,140,3,0.2,2.5,True)
####df['PSAR']=f.TA.PSAR(df,0.02,0.2)
####df['KC']=f.TA.KC(df,20,10,None,2)
####df['ICHIMOKU']=f.TA.ICHIMOKU(df,9,26,52,26)
####df['DMI']=f.TA.DMI(df,14,True)
##
####df=df[df['ADX']>40]
####df['KC']=f.TA.KC(20, 10,df['Close'], 2)
##
##
############ supertrend
##
##print(df)

