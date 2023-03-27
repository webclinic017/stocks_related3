import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import yfinance as yf
import talib as taa
from finta import TA
from numerize import numerize
import time

start = time.time()
print("hello")
end = time.time()
print(end - start)

perda='3d'
intervla='5m'


if end-start < .01:
    x=input("Ticker: ")
if end-start > .01:
##    x='ndx'
##    x='BTC-USD'
    
##    x='spy'
    x='mndy'
##    x='^dji'
##    x='^gspc'
##    x='ndx'
df=yf.download(x, period=perda, interval=intervla,prepost = False)
df.reset_index(inplace=True)

########################################################################

df['s4']=''
for x4 in df.index:
    df['s4'].loc[x4]=str(df['Datetime'].loc[x4]).split(' ')[0]


# s4 captures the time.
pp=[]
pp2=[]
df['s3']=''
for x4 in df.index:
    df['s3'].loc[x4]=str(df['Datetime'].loc[x4]).split(' ')[1][:5]
    if '16:00' in df['s3'].loc[x4]:
        pp.append(x4)
    if '09:30' in df['s3'].loc[x4]:
        pp2.append(x4)   

df['n']=''
df['c2']=''
df['c3']=''
df['s7']=''
df['Volumea']=''
df['Volume_buy_sold_g']=''
df['Volume_buy_sold_r']=''
df['Volume_buy_sold_m']=''


df['close_1d']=df['Close']-df['Close'].shift(1)


for c in df.index:
    df['n'].loc[c]=str(df['Datetime'].loc[c]).split('-')[2].split(' ')[0].strip()
##    df['n3'].loc[c]=str(df['Datetime'].loc[c]).split('-')[2].split(':00')[0].split(' ')[1]
    df['c2'].loc[c]=str(df['s3'].loc[c]).split(':')[0].strip()
    df['c3'].loc[c]=str(df['s3'].loc[c]).split(':')[1].strip()                    
    df['s7'].loc[c]=str(df['n'].loc[c])+str('_')+str(df['c2'].loc[c])+str('_')+str(df['c3'].loc[c])

##    if df['Volume'].loc[c] > 0:
##        df['Volume'].loc[c]=numerize.numerize(np.float64(df['Volume'].loc[c]).item())
    
    
    if df['Close'].loc[c] > df['Open'].loc[c]:
        df['Volume_buy_sold_g'].loc[c]=df['Volume'].loc[c]
    if df['Close'].loc[c] < df['Open'].loc[c]:
        df['Volume_buy_sold_r'].loc[c]=df['Volume'].loc[c]
    if df['Close'].loc[c] == df['Open'].loc[c]:
        df['Volume_buy_sold_m'].loc[c]=df['Volume'].loc[c]

########################################################################
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

df['RSI']=taa.RSI(df['Close'],timeperiod=4)
df['CCI']= taa.CCI(df['High'],df['Low'],df['Close'], timeperiod=14)
df['macd'], df['macdsignal'], df['macdhist'] = taa.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
df['MFI']=TA.MFI(df)
df['TRIX']=taa.TRIX(df['Close'], timeperiod=14)
df['ROC']=TA.ROC(df)
df['ADX']=TA.ADX(df)
df['VZO']=TA.VZO(df,14)
df['AO']=TA.AO(df,34,5)
df['ULTOSC']=taa.ULTOSC(df['High'],df['Low'],df['Close'],timeperiod1=7, timeperiod2=14, timeperiod3=28)
df['ATR']=taa.ATR(df['High'],df['Low'],df['Close'], timeperiod=14)

tt=[]
df['ss']=''
df['ss']=df['AO'].diff()
for x in df.index:
    if df['AO'].loc[x]>0 and df['AO'].shift(1).loc[x] <0 and (df['ss'].loc[x] > df['ss'].shift(1).loc[x]):
##                                                              and df['ss'].shift(1).loc[x] > \
##                                                          df['ss'].shift(2).loc[x] and df['ss'].shift(2).loc[x] > df['ss'].shift(3).loc[x]):
##    df['Close'].loc[x] > df['EMA_7'].loc[x] and df['Close'].shift(1).loc[x] < df['EMA_7'].shift(1).loc[x]
       
       
        tt.append(x)

        

fig, ax = plt.subplots()
print(type(fig),'   ',type(ax))
print(help(plt))
s1=plt.plot(df['vwap'],scalex=True,scaley=True,label='vwap',linewidth=.5, markersize=1.5,marker='o')
s2=plt.plot(df['Close'],scalex=True,scaley=True,label='Close')
s3=plt.plot(df['EMA_7'],scalex=True,scaley=True,label='EMA_7')
s4=plt.plot(df['EMA_21'],scalex=True,scaley=True,label='EMA_21')
s5=plt.plot(df['EMA_50'],scalex=True,scaley=True,label='EMA_50')
s6=plt.plot(df['EMA_100'],scalex=True,scaley=True,label='EMA_100')
s7=plt.plot(df['EMA_200'],scalex=True,scaley=True,label='EMA_200')
s8=plt.plot(df['SAR'],scalex=True,scaley=True,label='SAR',linewidth=.5,markersize=1.5,marker='o' )
s9=plt.plot(df['ATR']+df['Close'],label='ATR')
s9a=plt.plot(df['Close']-df['ATR'],label='ATR')
plt.autoscale(enable=True, axis='y')   
plt.legend()

plt.vlines(tt,df['Close'].min()-1,df['Close'].max()+1,colors='b',linestyles='solid')
plt.vlines(pp,df['Close'].min()-1,df['Close'].max()+1,colors='grey',linestyles='dashed',linewidth=3)
plt.vlines(pp2,df['Close'].min()-1,df['Close'].max()+1,colors='grey',linestyles='dashed')



plt.grid(which='major',axis='both')
plt.gca()
plt.title('vwap/Close'+str('  ----  ')+str(x)+str('   ')+str(intervla)+str(' ')+str(df['Close'].tail(1).to_string(index=False)))

###############3
##fig, ax = plt.subplots()
##print(type(fig),'   ',type(ax))
##print(help(plt))
##s1a=plt.plot(df['Low'],scalex=True,scaley=True,label='Low')
##s2a=plt.plot(df['High'],scalex=True,scaley=True,label='High')
##plt.legend()
##plt.grid(which='major',axis='both')
##plt.gca()
##plt.title('Low/High'+str(' ')+str(x))
###############3
##fig, ax = plt.subplots()
##print(type(fig),'   ',type(ax))
##print(help(plt))
##s1=plt.plot(df['Open'],scalex=True,scaley=True,label='Open')
##s2=plt.plot(df['Close'],scalex=True,scaley=True,label='Close')
##plt.legend()
##plt.grid(which='major',axis='both')
##plt.gca()
##plt.title('Open/Close'+str(' ')+str(x))
#################
############ 6th ################################## ---------->
fig, plt9 = plt.subplots()
p1=df.index
p5=df.iloc[:,df.columns.get_loc('macd')]

plt9.fill_between(p1, 0,p5,where= p5 > 0,  color='green',label='macd-Green') 
plt9.fill_between(p1, 0,p5,where= p5 < 0, color='red',label='macd-Red')
##    plt9.bar(df.index,df.iloc[:,df.columns.get_loc('macd')],color='red',width=5) 
##for p in df['s7'].index:
##    if '09_30' in df['s7'].loc[p]:
####            print('k33','  ',df['s7'].loc[p])
##        plt9.vlines(df['s7'].loc[p],df['macd'].min()-1,df['macd'].max()+1,colors='y',linestyles='solid')
####            w2.vlines(df['s7'].loc[p],df.index.min(),df.index.max(),colors='g',linestyles='solid')
##    if '16_00' in df['s7'].loc[p]:
####            print('16:00','  ',df['s7'].loc[p])
##        plt9.vlines(df['s7'].loc[p],df['macd'].min()-1,df['macd'].max()+1,colors='b',linestyles='solid')
##    if '15_00' in df['s7'].loc[p]:
####            print('15:00','  ',df['s7'].loc[p])
##        plt9.vlines(df['s7'].loc[p],df['macd'].min(),df['macd'].max()+.1,colors='k',linestyles='solid')       
##        if '15_00' in df['s7'].loc[p]:
##            print('15:00','  ',df['s7'].loc[p])
##            plt9.vlines(df['s7'].loc[p],df['macd'].min(),df['macd'].min()+2,colors='springgreen',linestyles='solid')     
##            w2.vlines(df['s7'].loc[p],df['Close'].min()-10,df['Close'].max()+10,colors='b',linestyles='solid')            
plt9.autoscale(enable=True, axis='y')        

plt9.legend(loc=2, fontsize = 'x-small')
plt9.legend()
plt9.grid(which='major',axis='both')
plt.vlines(pp,df['macd'],df['macd'].max(),colors='grey',linestyles='dashed',linewidth=3)
plt.vlines(pp2,df['macd'],df['macd'].max(),colors='grey',linestyles='dashed')

plt.plot((df['Close']-df['vwap'])/(df['Close'].max()-df['vwap'].max()),label='Close-vwap')
plt.plot((df['Close']-df['SAR'])/(df['Close'].max()-df['vwap'].max()),label='Close-SAr')


plt.vlines(pp,df['macd'].min(),df['macd'].max(),colors='grey',linestyles='dashed',linewidth=3)
plt.vlines(pp2,df['macd'].min(),df['macd'].max(),colors='grey',linestyles='dashed')
##plt.gca()
##plt.title('macd')

plt.title('macd'+str('  ----  ')+str(x)+str('   ')+str(intervla))
############ 7th ################################## ---------->
############ 6th ################################## ---------->
fig, plt10 = plt.subplots()
p1=df.index
p5=df.iloc[:,df.columns.get_loc('AO')]

plt10.fill_between(p1, 0,p5,where= p5 > 0,  color='green',label='AO-Green') 
plt10.fill_between(p1, 0,p5,where= p5 < 0, color='red',label='AO-Red')
##    plt9.bar(df.index,df.iloc[:,df.columns.get_loc('macd')],color='red',width=5) 
##for p in df['s7'].index:
##    if '09_30' in df['s7'].loc[p]:
####            print('k33','  ',df['s7'].loc[p])
##        plt9.vlines(df['s7'].loc[p],df['macd'].min()-1,df['macd'].max()+1,colors='y',linestyles='solid')
####            w2.vlines(df['s7'].loc[p],df.index.min(),df.index.max(),colors='g',linestyles='solid')
##    if '16_00' in df['s7'].loc[p]:
####            print('16:00','  ',df['s7'].loc[p])
##        plt9.vlines(df['s7'].loc[p],df['macd'].min()-1,df['macd'].max()+1,colors='b',linestyles='solid')
##    if '15_00' in df['s7'].loc[p]:
####            print('15:00','  ',df['s7'].loc[p])
##        plt9.vlines(df['s7'].loc[p],df['macd'].min(),df['macd'].max()+.1,colors='k',linestyles='solid')       
##        if '15_00' in df['s7'].loc[p]:
##            print('15:00','  ',df['s7'].loc[p])
##            plt9.vlines(df['s7'].loc[p],df['macd'].min(),df['macd'].min()+2,colors='springgreen',linestyles='solid')     
##            w2.vlines(df['s7'].loc[p],df['Close'].min()-10,df['Close'].max()+10,colors='b',linestyles='solid')            
plt10.autoscale(enable=True, axis='y')         

plt10.legend(loc=2, fontsize = 'x-small')
plt10.legend()
plt10.grid(which='major',axis='both')

plt.vlines(tt,df['AO'].min(),df['AO'].max(),colors='b',linestyles='solid')
plt.vlines(pp,df['AO'].min(),df['AO'].max(),colors='grey',linestyles='dashed',linewidth=3)
plt.vlines(pp2,df['AO'].min(),df['AO'].max(),colors='grey',linestyles='dashed')

plt.plot((df['Close']-df['vwap']),label='Close-vwap')
plt.plot((df['Close']-df['SAR']),label='Close-SAr')


##plt.gca()
##plt.title('AO')
plt.title('AO'+str('  ----  ')+str(x)+str('   ')+str(intervla))
############ 7th ################################## ---------->
############ 6th ################################## ---------->
fig, plt11 = plt.subplots()
p1=df.index
p5=df.iloc[:,df.columns.get_loc('TRIX')]

plt11.fill_between(p1, 0,p5,where= p5 > 0,  color='green',label='TRIX-Green') 
plt11.fill_between(p1, 0,p5,where= p5 < 0, color='red',label='TRIX-Red')
##    plt9.bar(df.index,df.iloc[:,df.columns.get_loc('macd')],color='red',width=5) 
##for p in df['s7'].index:
##    if '09_30' in df['s7'].loc[p]:
####            print('k33','  ',df['s7'].loc[p])
##        plt9.vlines(df['s7'].loc[p],df['macd'].min()-1,df['macd'].max()+1,colors='y',linestyles='solid')
####            w2.vlines(df['s7'].loc[p],df.index.min(),df.index.max(),colors='g',linestyles='solid')
##    if '16_00' in df['s7'].loc[p]:
####            print('16:00','  ',df['s7'].loc[p])
##        plt9.vlines(df['s7'].loc[p],df['macd'].min()-1,df['macd'].max()+1,colors='b',linestyles='solid')
##    if '15_00' in df['s7'].loc[p]:
####            print('15:00','  ',df['s7'].loc[p])
##        plt9.vlines(df['s7'].loc[p],df['macd'].min(),df['macd'].max()+.1,colors='k',linestyles='solid')       
##        if '15_00' in df['s7'].loc[p]:
##            print('15:00','  ',df['s7'].loc[p])
##            plt9.vlines(df['s7'].loc[p],df['macd'].min(),df['macd'].min()+2,colors='springgreen',linestyles='solid')     
##            w2.vlines(df['s7'].loc[p],df['Close'].min()-10,df['Close'].max()+10,colors='b',linestyles='solid')            
plt11.plot((df['Close']-df['vwap'])/(df['Close']+df['vwap']),label='Close-vwap')
plt11.plot((df['Close']-df['SAR'])/(df['Close']+df['SAR']),label='Close-SAr')

plt11.autoscale(enable=True, axis='y')        

plt11.legend(loc=2, fontsize = 'x-small')
plt11.legend()
plt11.grid(which='major',axis='both')
plt.vlines(pp,df['TRIX'].min(),df['TRIX'].max(),colors='grey',linestyles='dashed',linewidth=3)
plt.vlines(pp2,df['TRIX'].min(),df['TRIX'].max(),colors='grey',linestyles='dashed')
##plt.gca()
##plt.title('TRIX')
plt.title('TRIX'+str('  ----  ')+str(x)+str('   ')+str(intervla))
############ 7th ################################## ---------->
linewidth_E=.6
markersize_E=.9
fig, n2 = plt.subplots()
p1=df.index
p5=df.iloc[:,df.columns.get_loc('CCI')]

n2.plot(df.index,df['CCI'],color = 'lightcoral',label='CCI')
##
##p1=df.index
##p5a=df.iloc[:,df.columns.get_loc('CCI')]
n2.fill_between(p1, 100,p5,where= p5 > 100,  color='green') 
n2.fill_between(p1, -100,p5,where= p5 < -100, color='red')
n2.legend(loc=2, fontsize = 'x-small')
##
##n2.fill_between(100,p5a, color='green',label='CCI') 
##plt11.fill_between(p5a, 0,p5a,where= p5a < -100, color='red',label='TRIX-Red')
####n2.hlines(100,df.iloc[:,df.columns.get_loc('CCI')].min(),df.iloc[:,df.columns.get_loc('CCI')].max(), lw=1.0, color='teal',label='CCI 100 marker')    
####n2.hlines(-100,df.iloc[:,df.columns.get_loc('CCI')].min(),df.iloc[:,df.columns.get_loc('CCI')].max(), lw=1.0, color='teal',label='CCI-100 marker')
##

plt.vlines(pp,df['CCI'].min(),df['CCI'].max(),colors='grey',linestyles='dashed',linewidth=3)
plt.vlines(pp2,df['CCI'].min(),df['CCI'].max(),colors='grey',linestyles='dashed')

n2.plot((df['Close']-df['vwap']),label='Close-vwap')
n2.plot((df['Close']-df['SAR']),label='Close-SAR')

n2.autoscale(enable=True, axis='y')   
n2.grid(which='major',axis='both')
n2.legend(loc="upper left")
plt.title('CCI'+str('  ----  ')+str(x)+str('   ')+str(intervla))
############ 7th ################################## ---------->
############ 6th ################################## ---------->
fig, plt12 = plt.subplots()
p1=df.index
p5=df.iloc[:,df.columns.get_loc('RSI')]

plt12.plot(df.index,df['RSI'],color = 'lightcoral',label='RSI')

plt12.fill_between(p1, 70,p5,where= p5 > 70,  color='green',label='RSI-Red') 
plt12.fill_between(p1, 30,p5,where= p5 < 30, color='red',label='RSI-Green')



plt12.autoscale(enable=True, axis='y')        

plt12.legend(loc=2, fontsize = 'x-small')
plt12.legend()
plt12.grid(which='major',axis='both')
##plt.gca()
##plt.title('RSI')
plt.vlines(pp,df['RSI'].min(),df['RSI'].max(),colors='grey',linestyles='dashed',linewidth=3)
plt.vlines(pp2,df['RSI'].min(),df['RSI'].max(),colors='grey',linestyles='dashed')


plt.plot((df['Close']-df['vwap'])/(df['Close']+df['vwap']),label='Close-vwap')
plt.plot((df['Close']-df['SAR'])/(df['Close']+df['SAR']),label='Close-SAr')


plt.title('RSI'+str('  ----  ')+str(x)+str('   ')+str(intervla))

print(df['s3'])
############ 7th ################################## ---------->
############## 7th ################################## ---------->
############ 2nd ################################## ---------->


fig, plt5a = plt.subplots()
##p1=df.index


print(df.index,'------- ',df.iloc[:,df.columns.get_loc('Volume_buy_sold_g')])
    
##    plt5a.plot(df['s7'],df['pivot'],color = 'b',label='pivot',marker='o',markersize=3.6,  lw=1)
##    plt5a.plot(df['s7'],df['Close'],color = 'm',label='Close',marker='o',markersize=3.6,  lw=1)
####    plt.plot(df['s7'],df['pivot'],color = 'red',label='pivot',marker='o',markersize=3,  lw=1)
##    plt5a.fill_between(df['s7'],df['Close'],df['pivot'],where=df['pivot']>df['Close'], facecolor='wheat', interpolate=True)
##    plt5a.fill_between(df['s7'],df['Close'],df['pivot'],where=df['pivot']<df['Close'], facecolor='palegreen', interpolate=True)
##print(df.iloc[:,df.columns.get_loc('Volume_buy_sold_g')])

plt5a.bar(df.index,pd.to_numeric(df.iloc[:,df.columns.get_loc('Volume_buy_sold_g')]),  color='green')
plt5a.bar(df.index,pd.to_numeric(df.iloc[:,df.columns.get_loc('Volume_buy_sold_r')]), color='red')
##plt5a.bar(df.iloc[:,df.columns.get_loc('Volume_buy_sold_r')],df.iloc[:,df.columns.get_loc('Volume')],color='red',width=2)
##plt5a.autoscale()        

plt5a.legend(loc=2, fontsize = 'x-small')

plt5a.vlines(pp,df['Volume'].min(),df['Volume'].max(),colors='grey',linestyles='dashed',linewidth=3)
plt5a.vlines(pp2,df['Volume'].min(),df['Volume'].max(),colors='grey',linestyles='dashed',linewidth=1)
plt.autoscale(enable=True, axis='y')   
plt.grid(which='major',axis='both')
plt.legend(loc="upper left")
plt.title(str('Volume')+str(' ')+str(x)) 

##plt5a.autoscale()


############ 3rd ################################## ---------->  
############ 7th ################################## ---------->
##fig, n7 = plt.subplots()
plt.show()

##n7.bar(df.iloc[:,df.index,pd.to_numeric(df.iloc[:,df.columns.get_loc('Volume_buy_sold_g')]), width=1, color='green')
##n7.bar(df.iloc[:,df.index,pd.to_numeric(df.iloc[:,df.columns.get_loc('Volume_buy_sold_r')]), width=1, color='red')
##n7.bar(df.iloc[:,df.index,pd.to_numeric(df.iloc[:,df.columns.get_loc('Volume_buy_sold_m')]), width=1, color='blue')
##n7.legend(loc=2, fontsize = 'x-small')
##n7.title('nnnn')
############ 7th ################################## ---------->
plt.show()
