import talib as ta
from ta.utils import dropna
import yfinance as yf
import pandas as pd
import sys,os
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
import mplfinance
import matplotlib
##from matplotlib.finance import candlestick2_ohlc
##from mpl_finance import candlestick_ohlc
##from mplfinance.original_flavor import candlestick_ohlc
from mplfinance.original_flavor import candlestick_ohlc
from optionprice import Option
from numerize import numerize
import matplotlib.pyplot as plt
import sys
pd.options.display.width = 0
pd.set_option('display.max_columns', None)
pd.options.display.float_format = '{:.2f}'.format
##pd.options.display.max_columns=255
pd.options.display.max_rows=6500000
pd.set_option('display.max_colwidth', 500)
pd.set_option('display.max_columns', 550)
pd.options.mode.chained_assignment = None  # default='warn'



def alert(x,dp):
    ticker=x

    df = yf.download(ticker, period='65d', interval='1d',prepost = True)
    df=pd.DataFrame(df)

    df.reset_index(inplace=True,drop=False)
    df.rename(columns={'index': 'Datetime'}, inplace=True)


    v = df['Volume'].values
    tp = (df['Low'] + df['Close'] + df['High']).div(3).values
    df = df.assign(vwap=(tp * v).cumsum() / v.cumsum())

    df['pp']=''
    df['HL']=df['High']-df['Low']    
    df['ATRa']=''
    
    df['CCI']=ta.CCI(df['High'],df['Low'],df['Close'],timeperiod=14)
    df['adx']= ta.ADX(df['High'],df['Low'],df['Close'], timeperiod=14)
    df['RSI']= ta.RSI(df['Close'], timeperiod=14)
    df['macd'], df['macdsignal'], df['macdhist']=ta.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    df['PLUS_DI']=ta.PLUS_DI(df['High'],df['Low'],df['Close'], timeperiod=14)
    df['PLUS_DM']=ta.PLUS_DM(df['High'],df['Low'], timeperiod=14)
    df['aroondown'],df['aroonup']=ta.AROON(df['High'],df['Low'], timeperiod=14)
    df['MOM']=ta.MOM(df['Close'], timeperiod=10)
    df['STOCHRSI_fastk'], df['STOCHRSI_fastd'] = ta.STOCHRSI(df['Close'], timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
    df['ATRa']=ta.ATR(df['High'],df['Low'],df['Close'], timeperiod=14)

       
    df['EMA_3s']=ta.EMA(df['Close'], timeperiod=3)
    df['EMA_5s']=ta.EMA(df['Close'], timeperiod=5)
    df['EMA_10s']=ta.EMA(df['Close'], timeperiod=10)
    df['EMA_21s']=ta.EMA(df['Close'], timeperiod=21)
    df['EMA_50s']=ta.EMA(df['Close'], timeperiod=50)
    df['EMA_100s']=ta.EMA(df['Close'], timeperiod=100)
    df['EMA_200s']=ta.EMA(df['Close'], timeperiod=200)
    df['BB_upperband'], df['BB_middleband'], df['BB_lowerband'] = ta.BBANDS(df['Close'], timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
    df['ULTOSC'] = ta.ULTOSC(df['High'],df['Low'],df['Close'], timeperiod1=7, timeperiod2=14, timeperiod3=28)
    df['ROC'] = ta.ROC(df['Close'], timeperiod=10)

    df['PLUS_DI']=ta.PLUS_DI(df['High'],df['Low'],df['Close'], timeperiod=14)
    df['PLUS_DM']=ta.PLUS_DM(df['High'],df['Low'], timeperiod=14)
##    df['MOM']=ta.MOM(df['Close'], timeperiod=3)



    df['5>10']=''
    df['10>21']=''
    df['21>50']=''
    df['50>100']=''
    df['Close>5']=''
    df['Close>10']=''
    df['Close>21']=''
    df['Close>50']=''
    df['Close>100']=''
    df['Close>200']=''
    df['Close>vwap']=''
    df['5>vwap']=''
    df['10>vwap']=''
    df['21>vwap']=''
    df['50>vwap']=''
    df['100>vwap']=''
    df['200>vwap']=''
    df['Colse_UpBol']=''
    df['Colse_LowBol']=''
    df['Colse_MidBol']=''

    for x in df.index:
        
        df['5>10'].loc[x]=df['EMA_5s'].loc[x]-df['EMA_10s'].loc[x]
        df['10>21'].loc[x]=df['EMA_10s'].loc[x]-df['EMA_21s'].loc[x]
        df['21>50'].loc[x]=df['EMA_21s'].loc[x]-df['EMA_50s'].loc[x]
        df['50>100'].loc[x]=df['EMA_50s'].loc[x]-df['EMA_100s'].loc[x]
        df['Close>5'].loc[x]=df['Close'].loc[x]-df['EMA_5s'].loc[x]
        df['Close>10'].loc[x]=df['Close'].loc[x]-df['EMA_10s'].loc[x]
        df['Close>21'].loc[x]=df['Close'].loc[x]-df['EMA_21s'].loc[x]
        df['Close>50'].loc[x]=df['Close'].loc[x]-df['EMA_50s'].loc[x]
        df['Close>100'].loc[x]=df['Close'].loc[x]-df['EMA_100s'].loc[x]
        df['Close>200'].loc[x]=df['Close'].loc[x]-df['EMA_200s'].loc[x]
        df['Close>vwap'].loc[x]=df['Close'].loc[x]-df['vwap'].loc[x]
        df['5>vwap'].loc[x]=df['EMA_5s'].loc[x]-df['vwap'].loc[x]
        df['10>vwap'].loc[x]=df['EMA_10s'].loc[x]-df['vwap'].loc[x]
        df['21>vwap'].loc[x]=df['EMA_21s'].loc[x]-df['vwap'].loc[x]
        df['50>vwap'].loc[x]=df['EMA_50s'].loc[x]-df['vwap'].loc[x]
        df['100>vwap'].loc[x]=df['EMA_100s'].loc[x]-df['vwap'].loc[x]
        df['200>vwap'].loc[x]=df['EMA_200s'].loc[x]-df['vwap'].loc[x]
        df['Colse_UpBol'].loc[x]=df['Close'].loc[x]-df['BB_upperband'].loc[x]
        df['Colse_LowBol'].loc[x]=df['Close'].loc[x]-df['BB_lowerband'].loc[x]
        df['Colse_MidBol'].loc[x]=df['Close'].loc[x]-df['BB_middleband'].loc[x]

    ##    df['MOM_slope'].loc[x]=df['MOM'].loc[x]-df['MOM'].loc[x].shift(1)
    ##        print(df['BB_upperband'].loc[x], df['BB_middleband'].loc[x], df['BB_lowerband'].loc[x])
        
    ##    print(df['Colse_UpBol'].loc[x],'  ',df['Colse_LowBol'].loc[x],'  ',df['Colse_MidBol'].loc[x])
    ##    sys.exit()
        #######################################################################
        ### squeeze
        if df['Close'].loc[x] > 0:
            print(df['Close'].loc[x],'    ',type(df['Close'].loc[x]))
            print(int(df['Close'].loc[x]),'  ',type(int(df['Close'].loc[x])))
##            df['20sma'].loc[x] = df['Close'].loc[x].rolling(window=20)
            ts_log = df.loc(axis=1)[:,'Close']
            m=ts_log.mean()
            print(m,'  jjjjjjjjjjjjjjjjjj')

            sys.exit()                                           
##            p6=ts_log.rolling(20).mean()
##            p7=ts_log.rolling(20).std()
            print(m,' p6 jjjjjjjjjjjjjjjjjj', p7)
##
##            numpy.roll(your_array, shift, axis = None)
##            sys.exit()

            df['20sma'].loc[x]=p6
##            df['20sma'].loc[x] = np.int(df['Close'].loc[x]).rolling(window=20).mean()
##            df['stddev'].loc[x] = (int(df['Close'].loc[x])).rolling(window=20).std()

            df['stddev'].loc[x] =p7
            
            df['lower_band'].loc[x] = df['20sma'].loc[x] - (2 * df['stddev'].loc[x])
            df['upper_band'].loc[x] = df['20sma'].loc[x] + (2 * df['stddev'].loc[x])

            df['TR'].loc[x] = abs(df['High'].loc[x] - df['Low'].loc[x])
            df['ATR'].loc[x] = df['TR'].loc[x].rolling(window=20).mean()

            df['lower_keltner'].loc[x] = df['20sma'].loc[x] - (df['ATR'].loc[x] * 1.5)
            df['upper_keltner'].loc[x] = df['20sma'].loc[x] + (df['ATR'].loc[x] * 1.5)
            df['squeeze_on'].loc[x]=''
            df['MOM_slope'].loc[x]=''
            df['Red'].loc[x]=''
            df['Red'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
            df['Redby'].loc[x]=''

    for z in df.index:
        if df['Close'].loc[z]-df['Open'].loc[z] > 0:
            df['Redby'].loc[z]='Green'
        elif df['Close'].loc[z]-df['Open'].loc[z] < 0:
            df['Redby'].loc[z]='Red'
            
            
        df['pp'].loc[z]=df['HL'].loc[z]-df['ATRa'].loc[z]
        df['MOM_slope'].loc[z]=df['MOM'].loc[z]-df['MOM'].shift(1).loc[z]
        if df['lower_band'].loc[z] > df['lower_keltner'].loc[z] and df['upper_band'].loc[z] < df['upper_keltner'].loc[z]:
            df['squeeze_on'].loc[z]='in_squeeze'
        else:
            df['squeeze_on'].loc[z]='no'


    #################################################################
    ##print(df,'\n','pppppp')
    df['Close_Up_kelt']=df['Close']- df['upper_keltner']
    df['Close_Low_kelt']=df['Close']-df['upper_keltner']



    
    
            
    df['DM_DI_Signal']=''
##
##    df=df[df['adx'] > 25]
    ##df=df[(df['adx'] > 25) & (df['PLUS_DM'] < df['PLUS_DI'])]
    ##print(df.columns)

    df['weekday']=''
    df['weekday'] =df['Date'].dt.day_name()

    df=df[['Date','weekday','ATRa','pp','HL','Close', 'Adj Close', 'Volume','High','Low',
           'adx', 'RSI','CCI', 'macd', 'macdsignal', 'macdhist','PLUS_DI',
           'PLUS_DM','DM_DI_Signal','aroondown','aroonup','STOCHRSI_fastk','5>10','10>21','21>50','50>100','Close>5','Close>10',
           'Close>21','Close>50','Close>100','vwap','Close>vwap','5>vwap','21>vwap','50>vwap','100>vwap','200>vwap','squeeze_on',
           'ULTOSC','ROC','MOM','EMA_5s','EMA_10s','EMA_21s','EMA_50s','EMA_100s','EMA_200s','MOM_slope',
           'Colse_UpBol','Colse_LowBol','Colse_MidBol','Close_Up_kelt','Close_Low_kelt','Redby','Red']]




    df['Colse_UpBol'] = df['Colse_UpBol'].replace({np.nan: None})
    df['Colse_LowBol'] = df['Colse_LowBol'].replace({np.nan: None})
    df['Colse_MidBol'] = df['Colse_LowBol'].replace({np.nan: None})
  
    
##    df['Bol_dist']=min((df['Colse_UpBol'],(df['Colse_LowBol']),(df['Colse_MidBol'])))
##    df['Colse_UpBol'] = df['Colse_UpBol'].fillna(0)
##    df['Colse_LowBol'] = df['Colse_LowBol'].fillna(0)
##    df['Colse_MidBol'] = df['Colse_MidBol'].fillna(0)

    
    df['delta']=''
    df['DM_DI']=''
    df['ticker']=''
    df['Aroon_signal']=''
    for x in df.index:
        df['ticker'].loc[x]=ticker
        df['Aroon_signal'].loc[x]=df['aroonup'].loc[x]-df['aroondown'].loc[x]
        df['DM_DI'].loc[x]=df['PLUS_DM'].loc[x]-df['PLUS_DI'].shift(1).loc[x]
        df['delta'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]

    for x in df.index:
        if df['DM_DI'].loc[x] > 0:
            df['DM_DI_Signal'].loc[x]='uptrend'
        elif df['DM_DI'].loc[x] < 0:
            df['DM_DI_Signal'].loc[x]='Downtrend'
        else:
            df['DM_DI_Signal'].loc[x]='No_Trend'
##        print(df['Colse_UpBol'].loc[x])
##
##        if str(df['Colse_UpBol'].loc[x]) != None or str(df['Colse_LowBol'].loc[x]) != None or df['Colse_MidBol'].loc[x]!=None:
##            dd=[int(df['Colse_UpBol'].loc[x]),int(df['Colse_LowBol'].loc[x]),int(df['Colse_MidBol'].loc[x])]
##            print(min(dd))
            
    ##        
    ##    if df['PLUS_DM'].loc[x] < df['PLUS_DI'].loc[x]:
    ##        df['DM_DI_Signal'].loc[x]='Downtrend'        
    ##    elif df['PLUS_DM'].loc[x] > df['PLUS_DI'].loc[x]:
    ##        df['DM_DI_Signal'].loc[x]='Uptrend'
    ##    else:
    ##        df['DM_DI_Signal'].loc[x]='No Trend'

    df=df[['Date','weekday','ATRa','pp','HL','High','Low','ticker','DM_DI_Signal','Close','delta', 'Aroon_signal','aroonup','aroondown','adx','Volume',
           'DM_DI','PLUS_DI',
           'PLUS_DM','RSI','CCI','STOCHRSI_fastk','5>10','10>21','21>50','50>100','Close>5','Close>10',
           'Close>21','Close>50','Close>100','vwap','Close>vwap','5>vwap','21>vwap','50>vwap','100>vwap','200>vwap','squeeze_on',
           'ULTOSC','ROC','MOM','EMA_5s','EMA_10s','EMA_21s','EMA_50s','EMA_100s','EMA_200s','MOM_slope',
           'Colse_UpBol','Colse_LowBol','Colse_MidBol','Close_Up_kelt','Close_Low_kelt',
           'macd','macdsignal','macdhist','Redby','Red']]

##################################################################################################
##    df=df[df['adx'] > 25 & df['STOCHRSI_fastk'] > 99 & df['Date'] == '2021-12-02']
##    df=df[df['adx'] > 25 & df['STOCHRSI_fastk'] > 99]
##    df=df.tail(1)
    df=df.iloc[-2]
##    df=df[(df['adx'] > 25) & (df['MOM'] > 30)]
##    df=df[(df['adx'] > 45)]

##################################################################################################    
    



       
##    print(df)
    dp=dp.append(df)
    print(dp.shape)
    
##    df.sort_values(by=['HL'],axis=0)
##    print('\n\n\n') 
##    print(df)
##    print('\n\n\n')
##    print(dp)
    return(dp)

##    if (df5.empty!=True):
##        print('\n')
##        print('\n')
##        print('**************** ', x,' *****************************************')
##        print('\n')
##        print('\n',df5,'\n\n','df5','\n\n\n',df5aa,'\n','df5aa','\n\n\n',df6,'\n','df6','\n\n\n',df7,'\n','df7','\n',ticker,' -------------------------------->','\n')    
##        


uu=['vg','astr','ispc','mpln','nbev','avya','cei','nvts','now','snow','amc','aapl','f','asml','zm',
    'tsla','nio','plug','lcid','rivn','fsr','blnk','mrna','bntx','nvax','bntx','isrg','biib','pfe','abt',
    'qcom','nvda','avgo','qrvo','gfs','tsm',
    'adbe','gme','nvda','nflx','asml','mu','avgo','amd','asml','qcom','mrvl','txn','intc','dltr','penn','coin','mstr','uber','lyft','z',
    '^ndx','RSX','AUPH','BHP', 'DUST', 'EWY', 'NYCB', 'QID', 'SQQQ', 'SVRA', 'AEP',
    'BHP', 'DUST', 'EWY', 'NYCB', 'QID', 'SQQQ', 'SVRA', 'AEP',
    'bby','zm','dks','anf','docu','dltr','xpev','arkk','^ndx','^gspc','^dji','spy','tna','qqq','tsla','^dji','pfe','f','intc','spy']
    
mm=['adbe','gme','nvda','nflx','asml','mu','avgo','amd','asml','qcom','mrvl']
m33=['^ndx','^gspc','^dji','qqq','spy','tna','arkk','amzn','googl','tsla','adbe','mrna','zm']
m3=['t','e']
dp = pd.DataFrame() 

for x in m33:
    print(x)
    dp=alert(x,dp)


##dpx.to_csv('/home/az2/Dwonloads/bb444a', sep='\t', encoding='utf-8', header='true')
##print(dp[['Date','ticker','Close']],'\n', 'reading from df')

os.remove('/home/az2/nnna44444.txt')
dp.sort_values(by=['delta','adx'],inplace=True)
dp.to_csv('/home/az2/nnna44444.txt')


s=pd.read_csv('/home/az2/nnna44444.txt')
print(s[['Date', 'weekday','ticker', 'Close', 'delta','adx','STOCHRSI_fastk','ATRa', 'pp', 'HL', 'High', 'Low',
        'DM_DI_Signal', 'Aroon_signal', 'aroonup',
       'aroondown']],'\n','p2')
print('\n\n')
      

print(s[['Date', 'weekday','ticker', 'Close', 'delta',  'Volume', 'DM_DI', 'PLUS_DI', 'PLUS_DM', 'RSI',
       'CCI','Redby','Red','Close>vwap','Close>21']],'\n','p3')

print('\n\n')




print(s[['Date', 'weekday','ticker', 'Close', 'delta','Volume', 'DM_DI', 'PLUS_DI', 'PLUS_DM', 'RSI',
       'CCI']],'\n','p4')
print('\n\n')



print(s[['Date', 'weekday','ticker', 'Close', 'delta',
       'Colse_UpBol','Colse_LowBol','Colse_MidBol','Close_Up_kelt','Close_Low_kelt'
         ]],'\n','p5')

print('\n\n')

print(s[['Date', 'weekday','ticker', 'Close', 'delta','5>10', '10>21', '21>50', '50>100'
         ]],'\n','p6')
print('\n\n')


print('\n\n')
print(s[['Date', 'weekday','ticker', 'Close', 'delta',
         'Close>5','Close>10', 'Close>21', 'Close>50', 'Close>100']],'\n','p5')
print('\n\n')
print(s[['Date', 'weekday','ticker', 'Close', 'delta',
       '5>vwap', '21>vwap', '50>vwap', '100>vwap', '200>vwap', 'vwap', 'Close>vwap','squeeze_on',
       'ULTOSC', 'ROC', 'MOM']],'\n','p7')


print('\n\n')
print(s[['Date', 'weekday','ticker', 'Close', 'delta',
         'EMA_5s', 'EMA_10s', 'EMA_21s', 'EMA_50s', 'MOM_slope']],'\n','p8')

##
##dp=pd.read_csv('/home/az2/Dwonloads/bb444a.txt')
##dp=pd.DataFrame(dp)
##print(dp,'\n','reading from file')
##print('\n\n','exiting','\n',dp)






  
########################################################### clear the cache #######################3
import sys  #system specific parameters and names
import gc   #garbage collector interface

memory_usage_by_variable=pd.DataFrame({k:sys.getsizeof(v) for (k,v) in locals().items()},index=['Size'])
memory_usage_by_variable=memory_usage_by_variable.T
memory_usage_by_variable=memory_usage_by_variable.sort_values(by='Size',ascending=False).head(10)
##print(memory_usage_by_variable.head())

def obj_size_fmt(num):
    if num<10**3:
        return "{:.2f}{}".format(num,"B")
    elif ((num>=10**3)&(num<10**6)):
        return "{:.2f}{}".format(num/(1.024*10**3),"KB")
    elif ((num>=10**6)&(num<10**9)):
        return "{:.2f}{}".format(num/(1.024*10**6),"MB")
    else:
        return "{:.2f}{}".format(num/(1.024*10**9),"GB")


def memory_usage():
    memory_usage_by_variable=pd.DataFrame({k:sys.getsizeof(v)\
    for (k,v) in globals().items()},index=['Size'])
    memory_usage_by_variable=memory_usage_by_variable.T
    memory_usage_by_variable=memory_usage_by_variable\
   .sort_values(by='Size',ascending=False).head(10)
    memory_usage_by_variable['Size']=memory_usage_by_variable['Size'].apply(lambda x: obj_size_fmt(x))
    return memory_usage_by_variable

memory_usage()
##print(memory_usage_by_variable)

##print('\n''kaku khan','\n\n')
##
##print('2) gc.get_count()',gc.get_count())
##
##print('3) memory_usage-->: ',memory_usage())
##print('\n\n')
##print('4) gc.collect',gc.collect())
##print('5) gc.get_count() ',gc.get_count())
##print('memory_usage():',memory_usage())
##print('tota hoai baba')
##
##print('--------------------------------------------------','\n\n')
##print('\n')
##print('plotting loop', end4-start4)
##print('mpf plotting time',end3-start3)
##print('read from api/read from y.finance',end2-start2)


##print('--------------------------------------------------','\n\n')

##del gg
##del xz


#triggering collection
##print('After deleting df,df33,gg ,gc.collect()---',gc.collect())

#finally check memory usage
##print('\n')
##print('After deleting df,df33,gg,memory.usage()',memory_usage())




##['binance',
## 'blueskies',
## ,
## 'charles',
## 'checkers',
## 'classic',
## 'default',
## 'mike',
## 'nightclouds',
## 'sas',
## 'starsandstripes',
## 'yahoo']



######################################################
##import pandas as pd
##import mplfinance as mpf
##import datetime as dt
##import yfinance as yf
##
##
### Load data file.
##g='t'
##ticker=g
##no_of_days=365
##
##df = pd.DataFrame()
##
##
##start = dt.datetime.today() - dt.timedelta(no_of_days)
##end = dt.datetime.today()
##df = yf.download(ticker, start, end,prepost = True)
##
### Plot candlestick.
### Add volume.
### Add moving averages: 3,6,9.
### Save graph to *.png.
##mpf.plot(df, type='candle', style='charles',
##        title='',
##        ylabel='',
##        ylabel_lower='',
##        volume=True, 
##        mav=(200,100,50,20,10,3,5))
##
##
####################################
##import matplotlib.pyplot as plt
##from mpl_finance import candlestick_ohlc
##import pandas as pd
##import matplotlib.dates as mpl_dates
##import yfinance as yf
##import mplfinance as mpf
##
##plt.style.use('ggplot')
##
### Extracting Data for plotting
##df = yf.download('tsla', '2021-01-1','2021-06-28', index=False)
### Plot candlestick.
### Add volume.
### Add moving averages: 3,6,9.
### Save graph to *.png.
##mpf.plot(df, type='candle', style='charles',
##        title='',
##        ylabel='',
##        ylabel_lower='',
##        volume=True, 
##        mav=(3,6,9), 
##        savefig='test-mplfiance.png')





