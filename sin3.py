import datetime
from dateutil import parser
import sys
import time
import os
import plotly.graph_objects as go
import yfinance as yf
import pandas as pd
import datetime as dt
import talib as ta
import finta as f
import inspect
from inspect import currentframe, getframeinfo
import numpy as np
import sys,trace
import warnings
import sys
from datetime import date
import datetime
from datetime import timedelta
import random
from dateutil import parser



 
pd.options.display.float_format = '{:.2f}'.format
pd.options.display.max_columns = 255
pd.options.display.max_rows = 6500000

pd.options.display.max_rows = 9999
pd.options.display.max_columns = 76
pd.set_option("display.max_columns", 200)
pd.set_option('display.width', 1000)
pd.set_option('display.expand_frame_repr', False)

gg5 = []


warnings.filterwarnings("ignore")

pd.options.display.float_format = '{:.2f}'.format
pd.options.display.max_columns = 255
pd.options.display.max_rows = 6500000

pd.options.display.max_rows = 9999
pd.options.display.max_columns = 36
pd.set_option("display.max_columns", 100)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 200)
pd.set_option('display.max_columns', 0)
pd.set_option('display.max_columns', None)




def s4(u33,y , x2,ATR_target,adx_target,d2,d3):
    
    
        
        


    proxies = [
##        'http://138.197.222.35:80',
##        'http://1138.197.222.35:8080'
    '103.105.49.53:80'
    '167.172.248.53:3128',
    '194.226.34.132:5555',
    '203.202.245.62:80',
    '141.0.70.211:8080',
    '118.69.50.155:80',
    '201.55.164.177:3128',
    '51.15.166.107:3128',
    '91.205.218.64:80',
    '128.199.237.57:8080',
    '206.253.164.146:80', 
    '206.253.164.122:80', 
    '206.253.164.101:80', 
    '69.75.122.146:39593', 
    '103.105.49.53:80', 
    '67.201.33.9:25280', 
    '47.254.89.30:7328', 
    '23.251.138.105:8080', 
    '67.201.33.10:25283', 
    '47.56.69.11:8000', 
    '132.145.103.245:8118', 
    '4.53.28.242:80', 
    '47.242.116.120:59394', 
    '47.242.6.186:59394',
    '65.20.187.60:5678', 
    '65.20.155.226:5678', 
    '159.65.69.186:9200', 
    '65.21.183.114:3232', 
    '54.193.134.2:20030', 
    '165.225.114.76:10605', 
    '138.68.18.219:9050', 
    '47.90.132.228:8081', 
    '47.242.86.153:59394', 
    '193.123.227.220:59394', 
    '161.82.252.35:4153', 
    '35.184.126.42:80', 
    '165.225.124.97:10605', 
    '154.212.5.190:5678', 
    '184.105.134.166:48324', 
    '47.242.158.41:8080', 
    '68.183.130.112:19053', 
    '47.242.5.82:5678', 
    '35.232.186.191:3128'

    ]
    
    proxyb = random.choice(proxies)

    df = yf.download(x2,start=d3,end=d2,interval='1m',auto_adjust = True,threads = True,prepost=True,progress=False, proxies=proxyb)
    df['ticker']=''
    for x in df.index:
        df['ticker'].loc[x]=x2
        
        
##    print(df,x2,' === ',u33,' ===')
    return(u33,y,d2,d3,df)


def s5c(u33,y,d2,d3,gt4):
    import pandas as pd
    import talib as ta
    import finta as f
    from finta import TA as ff
    df=gt4
# https://pythonrepo.com/repo/peerchemist-finta-python-finance
    v = df['Volume'].values
    tp = (df['Low'] + df['Close'] + df['High']).div(3).values
    df = df.assign(vwap=(tp * v).cumsum() / v.cumsum())
      
    for x in df.index:


        df['VZO']=f.TA.VZO(df,14)
##        df['CTI']=f.TA.CTI(df,14)
        df['ADL']=f.TA.ADL(df)
##        VZO=ff.VZO(df,10)
##        PZO=ff.PZO(df,14)
##        VFI=ff.VFI(df,14)
##        SQZMI=ff.SQZMI(df,14)
##        BASP=ff.BASP(df,14)
##        CHANDELIER=ff.CHANDELIER(df,14)
##        ZLEMA=ff.ZLEMA(df,14)
##        EVWMA=ff.EVWMA(df,14)
##        SAR=ff.SAR(df,14)
##        DMI=ff.DMI(df,14)
##        VORTEX=ff.VORTEX(df,14)
##        STC=ff.STC(df,14)
##        df['VW_MACD']=f.finta.TA['VW_MACD'](df['Close'],signal=9,period_slow=26, period_fast=12)
        df['CCI'] = ta.CCI(df['High'], df['Low'], df['Close'], timeperiod=14)
        df['RSI'] = ta.RSI(df['Close'], timeperiod=14)
        df['macd'], df['macdsignal'], df['macdhist'] = ta.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
        df['signal'] = ''
        df['EMA_3'] = ta.EMA(df['Close'], timeperiod=3)
        df['EMA_5'] = ta.EMA(df['Close'], timeperiod=5)
        df['EMA_10'] = ta.EMA(df['Close'], timeperiod=10)
        df['EMA_50'] = ta.EMA(df['Close'], timeperiod=50)
        df['EMA_100'] = ta.EMA(df['Close'], timeperiod=100)
        df['EMA_200'] = ta.EMA(df['Close'], timeperiod=200)
        
        df['EMA_21'] = ta.EMA(df['Close'], timeperiod=21)
        df['MOM'] = ta.MOM(df['Close'], timeperiod=14)
        df['Close_vwap'] = df['Close'] - df['vwap']
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
        df['EMA_200_vwap'] = df['EMA_200'] - df['vwap']
        df['macd_35'], df['macdsignal'], df['macdhist'] = ta.MACD(
        df['Close'], fastperiod=3, slowperiod=5, signalperiod=3)
        df['Close_EMA3'] = df['Close'] - df['EMA_3']
        df['Close_EMA5'] = df['Close'] - df['EMA_5']
        df['Close_EMA10'] = df['Close'] - df['EMA_10']
        df['Close_EMA21'] = df['Close'] - df['EMA_21']
        df['Close_EMA50'] = df['Close'] - df['EMA_50']
        df['Close_vwap'] = df['Close'] - df['vwap']

        df['EMA_3s']=ta.MA(df['Close'], timeperiod=3)
        df['EMA_5s']=ta.MA(df['Close'], timeperiod=5)
        df['EMA_10s']=ta.MA(df['Close'], timeperiod=10)
        df['EMA_21s']=ta.MA(df['Close'], timeperiod=21)
        df['EMA_50s']=ta.MA(df['Close'], timeperiod=50)
        df['EMA_100s']=ta.MA(df['Close'], timeperiod=100)
        df['EMA_200s']=ta.MA(df['Close'], timeperiod=200)

        df['adx'] = ta.ADX(df['High'], df['Low'], df['Close'], timeperiod=14)
        df['ATR'] = ta.ATR(df['High'], df['Low'], df['Close'], timeperiod=14)
        df['TR'] = abs(df['High'] - df['Low'])
        df['AD'] = ta.ADOSC(df['High'], df['Low'], df['Close'], df['Volume'])

        df['SAR'] = ta.SAR(df['High'], df['Low'], acceleration=300, maximum=5)
        df['SARx'] = df['Close'] - df['SAR']
        df['PLUS_DI'] = ta.PLUS_DI(df['High'],df['Low'],df['Close'],timeperiod=14)
        df['MINUS_DI'] = ta.MINUS_DI(df['High'], df['Low'], df['Close'], timeperiod=14)
        df['PLUS_DM'] = ta.PLUS_DM(df['High'], df['Low'], timeperiod=14)
        df['MINUS_DM'] = ta.MINUS_DM(df['High'], df['Low'], timeperiod=14)
        df['DM_delta'] = df['PLUS_DM'] - df['MINUS_DM']
        df['DI_delta'] = df['PLUS_DI'] - df['MINUS_DI']
        ## squeeze info
        df['20sma'] = df['Close'].rolling(window=20).mean()
        df['stddev'] = df['Close'].rolling(window=20).std()
        df['lower_band'] = df['20sma'] - (2 * df['stddev'])
        df['upper_band'] = df['20sma'] + (2 * df['stddev'])
        df['lower_keltner'] = df['20sma'] - (df['ATR'] * 1.5)
        df['upper_keltner'] = df['20sma'] + (df['ATR'] * 1.5)

        df['Boling_upper2'], df['Boling__middle2'], df['Boling_lower2'] = ta.BBANDS(df['Low'], timeperiod=20, nbdevup=2, nbdevdn=2)
        




##        df['Boling_upper2'], df['Boling__middle2'], df['Boling_lower2'] = df['Boling_lower2'] = ta.BBANDS(df['Low'], timeperiod=20, nbdevup=2, nbdevdn=2)

        ##    df['EMA_3']=df['Close']-ta.MA(df['Close'], timeperiod=3)
##    df['EMA_5']=df['Close']-ta.MA(df['Close'], timeperiod=5)
##    df['EMA_10']=df['Close']-ta.MA(df['Close'], timeperiod=10)
##    df['EMA_21']=df['Close']-ta.MA(df['Close'], timeperiod=21)
##    df['EMA_50']=df['Close']-ta.MA(df['Close'], timeperiod=50)
##    df['EMA_100']=df['Close']-ta.MA(df['Close'], timeperiod=100)
##    df['EMA_200']=df['Close']-ta.MA(df['Close'], timeperiod=200)
##
##
##    df['EMA_3s']=ta.MA(df['Close'], timeperiod=3)
##    df['EMA_5s']=ta.MA(df['Close'], timeperiod=5)
##    df['EMA_10s']=ta.MA(df['Close'], timeperiod=10)
##    df['EMA_21s']=ta.MA(df['Close'], timeperiod=21)
##    df['EMA_50s']=ta.MA(df['Close'], timeperiod=50)
##    df['EMA_100s']=ta.MA(df['Close'], timeperiod=100)
##    df['EMA_200s']=ta.MA(df['Close'], timeperiod=200)

          

#######################
    df.reset_index(inplace=True)
##    print(x,'66',df.columns[0])
##    print(df,'663')
##    sys.exit()
    df['squeeze_on']=''
    p=0
    for x in df.index:
        ######################## squeeze 55


        if df['lower_band'].loc[x] > df['lower_keltner'].loc[x] and df['upper_band'].loc[x] < df['upper_keltner'].loc[x]:
            
            df['squeeze_on'].loc[x]='in_squeeze'
            p=p+1
##                print(x,"  in 1 min Squeeze, ATR=",df['ATR'].loc[z])
        else:
            df['squeeze_on'].loc[x]=' '

######################## squeeze 55
        
    df.set_index(df['Datetime'],inplace=True)
    df['s3']=''
    df['s2']=''
    df['i']=0
    i=0
    for x in df.index:
        df['i'].loc[x]=i
        df['s3'].loc[x]=str(df['Datetime'].loc[x]).split(' ')[0]
        df['s2'].loc[x]=str(df['Datetime'].loc[x]).split(' ')[1][0:5]
        i=i+1

    df.drop('Datetime', axis=1, inplace=True)
    
    df['Datetime']=df['s3']+'-'+df['s2']
    df.set_index(df['Datetime'],inplace=True)


##############################
##    print(df['VZO'],' with VZO values',' == ',u33,' == ')
    return(u33,df)
        
#
  
##import s7


import matplotlib.pyplot as plt
import sys
##print('s6-start 77')
##print('-------------------start of [s6] module-----------------------------')


def s6(df,u33,df7a):
##def cc(df,test,gt4,x,df9,ss):
    import time
    import matplotlib.pyplot as plt 
    import pandas as pd
    import sys
    from datetime import date
    from dateutil import parser
    ##print('-------------------start of [s6] module-----------------------------')

##
##    ##print(df,'88')

    
    print('\n\n\n\n')
    print('********************** summary Data frame df 7 **********************************')
##    print(df7,'df7')
    print('********************** summary Data frame df 7 **********************************')
##    sys.exit()
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

    df_short = pd.DataFrame()
    df4 = pd.DataFrame()
    df5 = pd.DataFrame()
    # df3=df
    g6 = pd.DataFrame()
    g7 = pd.DataFrame()

    # SAR reversal
##    df.reset_index(inplace=True)
    m2 = []
    m3 = []
    m4 = []
    t5=0
    t6=0

    p44=[]
    p45=[]
    i2='53'
    df['i2']=''
    df['i2a']=''





##    print(df,'from s4.py  55 kkkkkk')
##    print(test,'========== inside s6 ============')
# print(df.index,'ddddddddddddddddddd')

########################## buy condition ######################################
# print(df.index,'kkkkkkkkkkkkkkkkkkkkkkkkkkk')

    u=0
    g43=0;g44=0;g45=' ';g46=0.0;g47=0.0
    s43=0;s44=0;s45=' ';s46=0.0;s47=0.0
    v5=0.0
    v6=0.0
    buy_signal_counter=0
    buy_signal_counter_sig=0


##    df.set_index(df['counter'],inplace=True)
##    print(df,'888')
##    print(df.index,'jj')
##    df.reset_index(inplace=True,drop=True)
##    print('\n\n')
##    print(df.index,'jj22-------------------------')
##    df.set_index([s3,s2],inplace=True)
##    print(df.index,'jj22-------------------------')
##    print('\n\n')
##    df['i']=df.index
    df.reset_index(inplace=True,drop=True)
    df.set_index(df['i'],inplace=True)
##    print(df)


    #print(df,'4444444444444444444444444444444444444444444444444444444444444444444444444444444444444')
    
##    df.set_index(df['Datetime'])
    k57=0
##    print(df,'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')



    ##print('babu khan ', df,df.shape)
#################################################################################################
##    print('\n\n\n')
    
    dfm=df.loc[(df['s2'] > '09:00') & (df['s2'] < '16:01')]
    df=dfm
    ##print('\n\n\n')
    ##print('babu khan2 ', df,df.shape)
##    sys.exit()
#################################################################################################
    i=0
    g=0
##    c2=''
##    c3=''

##    for x in df['vwap'].index:    
    for x in df.index:
    
##        if df.loc[x,'s2']=='16:00':
##            c3=x
        if df['Close_vwap'].loc[x] > 0 and (df['Close_vwap'].shift(1).loc[x] > 0) and (df['Close_vwap'].shift(2).loc[x] < 0)\
           and df['macd'].loc[x] > 0 and df['EMA-510'].loc[x] > 0 :


            bg33=df['Close_vwap'].loc[x] > 0 and (df['Close_vwap'].shift(1).loc[x] > 0) and (df['Close_vwap'].shift(2).loc[x] < 0)\
                and df['macd'].loc[x] > 0 and df['EMA-510'].loc[x] > 0 
##           and df['EMA_3_vwap'].loc[x] > 0 and df['EMA_5_vwap'].loc[x] > 0 :
##           and df['EMA_21_vwap'].loc[x] > 0 and df['EMA_3s'].loc[x] > 0 and df['EMA_5s'].loc[x] > 0 and\
##           df['EMA_10s'].loc[x] > 0 :
            
            
            g=g+1             
##            print(x,'   ',u33,'   crossover - condidition satisfied','\n\n','Close_vwap = ',df['Close_vwap'].loc[x],'\n',\
##                  'macd=',df['macd'].loc[x] ,'\n',
##                  'adx=',df['adx'].loc[x])


##            print(u33,' v ',x,'   crossover - condidition satisfied')
##            print('\n\n')
            
##            print('              Buy signal condition met      ')
##            print('         ----------------------       ')
##            print('Close=',df['Close'].loc[x])
##            print('Close_vwap = ',df['Close_vwap'].loc[x])
##            print('macd=',df['macd'].loc[x])
##            print('adx=',df['adx'].loc[x])
##            print('         ----------------------       ')
##            print('\n\n')
####        else:    
##            print("crossover - condidition not satisfied")
        i=1+i
    if g < 1:
##        print(u33,' === Buy Condition not satisfied')
        pass
##    sys.exit()



##########################################################################################################    
##    print(df,'nn ',u33)
    for z in df.index:
        buy_signal_counter=buy_signal_counter+1
##        print(z,'azhar 2')
        u=u+1
        t5=t5+1
        k57=k57+1
        df['i2'].loc[z]=i2



##        buy_condition = df['macd'].loc[z] > 0 and df['macd'].shift(1).loc[z] < 0

        buy_condition = df['Close_vwap'].loc[z] > 0 and (df['Close_vwap'].shift(1).loc[z] > 0) and (df['Close_vwap'].shift(2).loc[z] < 0)\
                and df['macd'].loc[z] > 0 and df['EMA-510'].loc[z] > 0

        bg33=df['Close_vwap'].loc[x] > 0 and (df['Close_vwap'].shift(1).loc[x] > 0) and (df['Close_vwap'].shift(2).loc[x] < 0)\
                and df['macd'].loc[x] > 0 and df['EMA-510'].loc[x] > 0 

  


##        buy_condition = df['macd'].loc[z] > 0 and df['macd'].shift(1).loc[z] < 0 and df['macd'].shift(2).loc[z] < 0\
##                        and df['aroonup'].loc[z].round(1) > 85 

         

##        buy_condition = df['MOM'].loc[z] - df['MOM'].shift(1).loc[z] > 0 and\
##                        df['macd'].loc[z] > 0 and df['adx'].loc[z] > 24 and df['ATR'].loc[z] > .9 and df['TR'].loc[z] > .5

##        buy_condition = df['MOM'].loc[z] - df['MOM'].shift(1).loc[z] 
####################################################################################################################################
        '''
        if buy_condition == True:
            print('-------------------------------------------------------------------------------------------------------------------------------')
            print('index->', z,'  ',buy_condition,' tkr-> ',df['ticker'].loc[z],' macd-> ',df['macd'].loc[z].round(3),' adx-> ',df['adx'].loc[z].round(3),
              ' MOM-> ',df['MOM'].loc[z].round(1),' ATR->',df['ATR'].loc[z].round(1),' Close_vwap->',df['Close_vwap'].loc[z].round(1),' sqz_on->',\
                  df['squeeze_on'].loc[z],' aroonup->',df['aroonup'].loc[z].round(1),' CCI->',df['CCI'].loc[z].round(1),
                  '----------------------------------------------------------->')
            print('-------------------------------------------------------------------------------------------------------------------------------')
##            print(' Close_vwap->',df['Close_vwap'].loc[z].round(1),' squeeze_on->',
##                  df['squeeze_on'].loc[z],' aroonup->',df['aroonup'].loc[z].round(1),' CCI->',df['CCI'].loc[z].round(1),'EMA-35->',
##                  df['EMA-35'].loc[z].round(1),' EMA_5_vwap->',df['EMA_5_vwap'].loc[z].round(1),'EMA_50_vwap->',df['EMA_5_vwap'].loc[z].round(1),' ------------>')

        elif df['macd'].loc[z] > 0:
            print('-------------------------------------------------------------------------------------------------------------------------------')
            print('index->', z,'  ',buy_condition,' tkr-> ',df['ticker'].loc[z],' macd-> ',df['macd'].loc[z].round(3),' adx-> ',df['adx'].loc[z].round(3),
              ' MOM-> ',df['MOM'].loc[z].round(1),' ATR->',df['ATR'].loc[z].round(1),' Close_vwap->',df['Close_vwap'].loc[z].round(1),' sqz_on->',\
                  df['squeeze_on'].loc[z],' aroonup->',df['aroonup'].loc[z].round(1),' CCI->',df['CCI'].loc[z].round(1),
                  '----------------------------------------------------------->')

##            print('-------------------------------------------------------------------------------------------------------------------------------')
##            print(' Close_vwap->',df['Close_vwap'].loc[z].round(1),' squeeze_on->',
##                  df['squeeze_on'].loc[z],' aroonup->',df['aroonup'].loc[z].round(1),' CCI->',df['CCI'].loc[z].round(1),'EMA-35->',
##                  df['EMA-35'].loc[z].round(1),' EMA_5_vwap->',df['EMA_5_vwap'].loc[z].round(1),'EMA_50_vwap->',df['EMA_5_vwap'].loc[z].round(1),' ------------>')

        else:
            print('index->', z,' **** ',buy_condition,'**** tkr-> ',df['ticker'].loc[z],' macd-> ',df['macd'].loc[z].round(1),' adx-> ',df['adx'].loc[z].round(3),
              ' MOM-> ',df['MOM'].loc[z].round(1),' ATR->',df['ATR'].loc[z].round(1),' Close_vwap->',df['Close_vwap'].loc[z].round(1),' sqz_on->',\
                  df['squeeze_on'].loc[z],' aroonup->',df['aroonup'].loc[z].round(1),' CCI->',df['CCI'].loc[z].round(1))
##            print(' Close_vwap->',df['Close_vwap'].loc[z].round(1),' squeeze_on->',
##                  df['squeeze_on'].loc[z],' aroonup->',df['aroonup'].loc[z].round(1),' CCI->',df['CCI'].loc[z].round(1),'EMA-35->',
##                  df['EMA-35'].loc[z].round(1),' EMA_5_vwap->',df['EMA_5_vwap'].loc[z].round(1),'EMA_50_vwap->',df['EMA_5_vwap'].loc[z].round(1))
        '''
####################################################################################################################################            

        if buy_condition:
##        if buy_condition and i2=='53':
            i2 = '51'

##            print('\n')
##            print(u33,' 66 buy_condition=',buy_condition)
            ##print('\n')
            
            # ##print("kkkkkkkkkkkdddddd",len(df.index))
##            ss.append(z)
##                print('line no ',z,'buy cond')
            df['signal'].loc[z] = "Buy_signal"
##            print('\n')
##            print(u33,'  ',x,'   crossover - condidition satisfied','\n\n',
##                  'Close=',df['Close'].loc[z] ,'\n'
##                  'Close_vwap = ',df['Close_vwap'].loc[z],'\n',\
##                  'macd=',df['macd'].loc[z] ,'\n',
##                  'adx=',df['adx'].loc[z])

##            print(u33,' v ',z,'   Buy signal')
##            print('\n\n')
            print('              Buy signal         ')
            print('         ----------------------       ')
            print('Close=',df['Close'].loc[z])
            print('Close_vwap = ',df['Close_vwap'].loc[z])
            print('macd=',df['macd'].loc[z])
            print('adx=',df['adx'].loc[z])
            if df['VZO'].loc[z] > 100:
                print('VZO=',df['VZO'].loc[z],'   Will go down')
            if df['VZO'].loc[z] < -100:
                print('VZO=',df['VZO'].loc[z],'   Will go up')
            else:
                print('VZO=',df['VZO'].loc[z],'   sideways/not sure')
            print('CCI=',df['CCI'].loc[z])
            print('MOM=',df['MOM'].loc[z])
            print('         ----------------------       ')
            print('\n')

            b_Close_vwap=df['Close_vwap'].loc[z]
            b_macd=df['macd'].loc[z]
            b_mom=df['MOM'].loc[z]
            b_VZO=df['VZO'].loc[z]
            b_CCI=df['CCI'].loc[z]
            

##            =================================================== >>>>>
##            df['signal'].loc[z] = 55
            
            v5 = df['Close'].loc[z]  # v5 is buy
            v6 = df['CCI'].loc[z]
            t_buy = df['Datetime'].loc[z]

            v8 = df['ticker'].loc[z]
##            print(z,'  z vs u        ',u)
            g43 = z
            g44=df['Datetime'].loc[z]
            g45=df['ticker'].loc[z]
            g46=df['MOM'].loc[z]
            g47=df['macd'].loc[z]
            buy_signal_counter_sig==buy_signal_counter
            break
            
##########################################################################
######################## SELL CONDITION ##################################
##    print('g43=',g43,' 00000000000000000000000000000000000000000000000000000000000')
    i = 0
    mm3 = 'MOM'
    t6=0
##    print('\n')
    
##    print(g43,'   ',g44,'  ',df['ticker'][-1],'----------- buy signal received here --------------')
##    print(u33,'  Buy ',g43,'   at time: ',g44,'  ticker= ',g45,' MOM=',g46,'  MACD=',g47,' ----------- buy signal received here --------------')
##    print('\n')
    print(u33,'  index Buy ',g43,'  buy=',v5,'   at time: ',g44,'  ticker= ',g45,' MOM=',g46,'  MACD=',g47,' ----------- buy signal received here --------------')
    

    sell_signal_counter=0
    sell_signal_counter_sig=0

    df.dropna(subset=[mm3], how='all', inplace=True)
    ##print(df,df.shape,'8887')

    if v5 != 0:
        
        
        for z in range(g43, df.index[-1]):
    ##    for z in range(g43, df.index[-1]):
            sell_signal_counter=sell_signal_counter+1
    ##        print(g43,'------------------',df.index[-1])       
            t6=t6+1
            
            sell_condition = df['macd'].loc[z] < 0 and df['macd'].shift(1).loc[z] > 0
    ##        print(df['macd'].loc[z] < 0 and df['macd'].shift(1).loc[z] > 0,'  oooooooooooooooooooooooooooooo')
    ##        sell_condition = df['macd'].loc[z] < 0 and df['macd'].shift(1).loc[z] > 0


            
            
    ##        sell_condition = (df[mm3].loc[z] < 0 and (df[mm3].loc[z] - df[mm3].shift(1).loc[z] < 00) and df['Close'].loc[z] > v5)

            if sell_condition and i2=='51' and g43 != None:
                
                
                sell_signal_counter_sig==sell_signal_counter
                



                s_Close_vwap=df['Close_vwap'].loc[z]
                s_macd=df['macd'].loc[z]
                s_mom=df['MOM'].loc[z]
                s_VZO=df['VZO'].loc[z]
                s_CCI=df['CCI'].loc[z]







    ##        sell_condition = (df['Close'].loc[z] > v5) and df['macd'].loc[z] < 0
    ##        print(df['macd'].loc[z])
    ##        sell_condition = df['macd'].loc[z] 
            
    ##        sell_condition = df['Close'].loc[z] - df['Close'].shift(1).loc[z] < (.5) or df['Close'].loc[z] < v5-.1 
    ##                         (df['Close'].loc[z] < 0 and df['Close'].shift(1).loc[z] < 0 and df['Close'].shift(2).loc[z] < 0\
    ##                             and df['Close'].shift(3).loc[z] < 0)
            
    ##        sell_condition = (df[mm3].loc[z] < 0 and (df[mm3].loc[z] - df[mm3].shift(1).loc[z] < 00) and df['Close'].loc[z] > v5)
    ##        if float(df['macd'].loc[z])  < float(0):  
    ####        if sell_condition and i2=='51' and g43 != None:
    ##            sell_signal_counter_sig==sell_signal_counter
    ##            print('buy price: ',v5, ' exit price=',v5-.25)
                
                df['i2a'].loc[z]=i2
                i2='53'
                ##                        print(' sell cond')

                ##                    sell_condition=df[mm3].loc[z] < 0
                
                df['signal'].loc[z] = "Sell_signal"
                
    ##            ==================================================== >>>>
    ##            df['signal'].loc[z] = 56

                
                t_sell = df['Datetime'].loc[z]
                v4 = df['Close'].loc[z]
                v7 = df['ticker'].loc[z]
    ##                        print(v7,'  ',v4,'/',v5,'  ',v4-v5,'  ',t_sell,'/',t_buy)
                xm = v7
                x2 = v5
                x3 = v4
                x5 = v6
                x4 = v4 - v5

                g6 = g6.append([[xm, v5, v4, x4, v7, t_buy, t_sell]])

                i = i + 1

                s43 = z
                s44=df['Datetime'].loc[z]
                s45=df['ticker'].loc[z]
                s46=df['MOM'].loc[z]
                s47=df['macd'].loc[z]

            else:
                if z==df.index[-1]:
                    
                    ##print('No Sell')
                    pass

               

    ##                    print('============= Bought but sell condition not met during the day/Loss ===================')
    ##    print(s43,'   at time:  ticker= '' ----------- [sell] signal received here --------------')
    ##    print(u33,'  Sell ',s43,'   at time: ',s44,'  ticker= ',s45,' MOM=',s46,'  MACD=',s47,' ----------- [sell] signal received here --------------')
        print(u33,'  index Sell ',s43,'  buy=',v4,'   at time: ',s44,'  ticker= ',s45,' MOM=',s46,'  MACD=',s47,' ----------- [sell] signal received here --------------')
        
    ##    print(u33,'  index Buy ',g43,'  buy=',v5,'   at time: ',g44,'  ticker= ',g45,' MOM=',g46,'  MACD=',g47,' ----------- buy signal received here --------------')
        
        print('\n')
        if v4-v5 > 0:
            print('================= Profit=',round((v4-v5),2))
        else:
            print('================= Loss=',round((v4-v5),2))
        print('\n')

        print('\n\n\n\n\n')
    ##    print('Close market: ',df['Close'].loc['c2'],'/',df['Close'].loc['c3'],'  ')
        g6.drop_duplicates(subset=None, keep='last', inplace=True)
        

##        s5d={'f2':'34','f3':'55'}
        s5d={'stragety':'2','Date':str(u33),'ticker':s45,'Buy_at':v4,'Sell_at':v5,'Profit':v4-v5,\
             'b_Close_vwap':'dummy','b_macd':'dummy','b_mom':'dummy','b_VZO':'dummy','b_CCI':'dummy'}
        if v4==0:
            v5==0
            s45==df['ticker'][2]
            
            

        df7a=df7a.append(s5d,ignore_index=True)

##        print(df7,'--------------- gg55')
        
        '''
        df = df[['Datetime','i2',
                 's3',
                 's2',
                 'i',
                 'ticker',
                 'signal',
                 'Close',
                 'Close_delta',
                 'MOM',
                 'macd',
                 'adx',
                 'ATR',
                 'TR',
                 'Close_vwap',
                 'Open',
                 'Open_delta',
                 'High',
                 'High_delta',
                 'Low',
                 'Low_delta',
                 'Close',
                 'Volume',
                 'Red',
                 'Red_breath',
                 'vwap',
                 'ATR',
                 'TRANGE',
                 'TR',
                 'adx',
                 'MOM',
                 'MOM_slope',
                 'Boling_upper2',
                 'Boling__middle2',
                 'Boling_lower2',
                 'x',
                 'SAR',
                 'SARx',
                 'tail',
                 'lower_band',
                 'upper_band',
                 'bolinger_width',
                 'lower_keltner',
                 'upper_keltner',
                 'vwap_bw_bolinger',
                 'EMA50_bw_bolinger',
                 'squeeze_on',
                 'aroondown',
                 'aroonup',
                 'CCI',
                 'RSI',
                 'EMA_slope',
                 'fastk',
                 'fastd',
                 'TSF',
                 'cross',
                 'mama_fama',
                 'DM_delta',
                 'DI_delta',
                 'mama',
                 'fama',
                 'KAMA',
                 'AD',
                 'MA',
                 'MA2',
                 'macd_slope',
                 'mama',
                 'fama',
                 'KAMA',
                 'AD',
                 'ADOSC',
                 'DEMA',
                 'HT_DCPERIOD',
                 'HT_DCPHASE',
                 'CMO',
                 'PLUS_DI',
                 'MINUS_DI',
                 'PLUS_DM',
                 'MINUS_DM',
                 'ADOSC',
                 'DEMA',
                 'LINEARREG',
                 'LINEARREG_ANGLEG',
                 'LINEARREG_INTERCEPT',
                 'LINEARREG_SLOPE',
    ##             'macd',
                 'macdsignal',
                 'macdhist',
                 'EMA-35',
                 'EMA-510',
                 'EMA-1021',
                 'EMA-2150',
                 'EMA_3_vwap',
                 'EMA_5_vwap',
                 'EMA_10_vwap',
                 'EMA_21_vwap',
                 'EMA_50_vwap',
                 'Close_EMA3',
                 'Close_EMA5',
                 'Close_EMA10',
                 'Close_EMA21',
                 'Close_EMA50',
                 'Close_vwap']]
        '''

        ####print(df.shape,'sin34') 
        if s44 != 0:
            
            print(u33,'    45      ','df','      ','g45','  buy sell-signal  ','\n')

                  
        if s44==0:
            print(u33,'    46      ','df','      ','s45','  buy sell-signal  ==== [no sell] ====','\n')

        
        
        print(u33,' -------------------end of [s6] module-----------------------------')
        
        ####print(df.shape,'sin36')

##    x    return(df7,df5)
    return(df,df7a)
##    print('\n\n')
##    print(' df7 train ------------------------------------------------------------------------------------------------------')
##    print(df7)
##    print('------------------------------------------------------------------------------------------------------------------')
##    print('s6-end')  
##    print('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

####################################### no ploytting ###########################################


def plot3(df5,df7):
    # u33=date
    import matplotlib.pyplot as plt
    import matplotlib.pyplot as plt2
    from matplotlib.axis import Axis
    from matplotlib.widgets import Slider, Button, RadioButtons 
    import numpy as np    
    import sys

    print(df,' mm')

    df=df.loc[(df['s2'] > '09:00') & (df['s2'] < '16:01')] 
    
    print(df.columns.get_loc('s2'),'  ',df.iloc[3,df.columns.get_loc('s2')])
    print(df.columns.get_loc('Close'),'  ','Close')
    print(df.columns.get_loc('Close_vwap'),'Close_vwap')
    print(df.columns.get_loc('EMA-510'),'EMA-510')
    print(df.columns.get_loc('EMA-1021'),'EMA-1021')
    print(df.columns.get_loc('EMA-2150'),'EMA-2150')
    print('\n')
    print(df.columns.get_loc('EMA_3_vwap'),'EMA_3_vwap')
    print(df.columns.get_loc('EMA_5_vwap'),'EMA_5_vwap')
    print(df.columns.get_loc('EMA_10_vwap'),'EMA_10_vwap')
    print(df.columns.get_loc('EMA_21_vwap'),'EMA_21_vwap')
    print(df.columns.get_loc('EMA_50_vwap'),'EMA_50_vwap')
    print(df.columns.get_loc('MOM'),'MOM')
    print('EMAs','\n')
    print(df.columns.get_loc('EMA_3s'),'EMA_3s')
    print(df.columns.get_loc('EMA_5s'),'EMA_5s')
    print(df.columns.get_loc('EMA_10s'),'EMA_10s')
    print(df.columns.get_loc('EMA_21s'),'EMA_21s')
    print(df.columns.get_loc('EMA_50s'),'EMA_50s')
    print(df.columns.get_loc('EMA_100s'),'EMA_100s')
    print(df.columns.get_loc('EMA_200s'),'EMA_200s')
    print(df.columns.get_loc('macd'),'macd')
##    print(df.columns.get_loc('SARx'),'sarx')
    print(df.columns.get_loc('CCI'),'cci')
    print(df.columns.get_loc('RSI'),'rsi')
    print(df.columns.get_loc('adx'),'adx')
    print(df.columns.get_loc('ATR'),'ATR')
    print(df.columns.get_loc('AD'),'AD')
    print(df.columns.get_loc('SAR'),'SAR')
    print(df.columns.get_loc('SARx'),'SARx')
    print(df.columns.get_loc('TR'),'TR')
    print(df.columns.get_loc('squeeze_on'),'squeeze_on')
    

    print('\n',df.columns)


    
##    print(df.columns.get_loc('Boling_upper2'))
##    print(df.columns.get_loc('Boling__middle2'))
##    print(df.columns.get_loc('Boling_lower2'))                         
    
##    print(df.columns['s2'])
##    u=df.iloc[3,'ticker']
##    print(df['ticker'][4])
##    sys.exit()




##    df3b=df[df['MOM'] > 0 & (df['MOM']-df['MOM'].shift(1)) < 0]
    
    
    print(df.shape,' 44')
    df4=df[df['MOM']<0]
    df=df.loc[(df['s2'] > '09:00') & (df['s2'] < '16:01')]
    df3a=df[(df['MOM'] > 0) & ((df['MOM']-df['MOM'].shift(1)) > 0)]
    df3b=df[(df['MOM'] > 0) & ((df['MOM']-df['MOM'].shift(1)) < 0)]

    df4a=df[(df['MOM'] < 0) & ((df['MOM']-df['MOM'].shift(1)) > 0)]
    df4b=df[(df['MOM'] < 0) & ((df['MOM']-df['MOM'].shift(1)) < 0)]
    
    fig1, (ax1, ax2, ax3,ax4,ax5,ax6,ax7) = plt.subplots(7, 1,sharex=True)
    fig1.suptitle('baba5', fontsize=5)
    
    bb=df.columns.get_loc('s2')
    df.sort_values(['s2'],ascending=True,inplace=True)

    plt.rc('legend',fontsize=3) # using a size in points
    plt.rc('legend',fontsize='small') # using a named size
    plt2.rc('legend',fontsize=3) # using a size in points
    plt2.rc('legend',fontsize='small') # using a named size

    
    
    plt.suptitle(str(df.iloc[3,df.columns.get_loc('ticker')])+str('  ')+str(p2b)+str('  ')+str(p2d))
    plt2.suptitle(str(df.iloc[3,df.columns.get_loc('ticker')])+str('  ')+str(p2b)+str('  ')+str(p2d))
    mclrs5=[]
#########################
    for x in df.index:


    ####################################        
##        if df.iloc[x,df.columns.get_loc('MOM')] > 0 and df.iloc[x,df.columns.get_loc('MOM')] - df.shift(1).iloc[x,df.columns.get_loc('MOM')] > 0:
##            mclrs5.append('green')
##        elif df.iloc[x,df.columns.get_loc('MOM')] > 0 and  df.iloc[x,df.columns.get_loc('MOM')] - df.shift(1).iloc[x,df.columns.get_loc('MOM')] < 0:
##            mclrs5.append('cyan')        
##        elif df.iloc[x,df.columns.get_loc('MOM')] < 0 and df.iloc[x,df.columns.get_loc('MOM')] - df.shift(1).iloc[x,df.columns.get_loc('MOM')] > 0:
##            mclrs5.append('red')
##        elif df.iloc[x,df.columns.get_loc('MOM')] < 0 and  df.iloc[x,df.columns.get_loc('MOM')] - df.shift(1).iloc[x,df.columns.get_loc('MOM')] < 0:
##            mclrs5.append('green')

        if df.loc[x,'MOM'] > 0 and (df.loc[x,'MOM'] - df.shift(1).loc[x,'MOM']) > 0:
            mclrs5.append('green')
        elif df.loc[x,'MOM'] > 0 and (df.loc[x,'MOM'] - df.shift(1).loc[x,'MOM']) < 0:
            mclrs5.append('red')
        elif df.loc[x,'MOM'] < 0 and (df.loc[x,'MOM'] - df.shift(1).loc[x,'MOM']) > 0:
            mclrs5.append('red')
        elif df.loc[x,'MOM'] < 0 and (df.loc[x,'MOM'] - df.shift(1).loc[x,'MOM']) < 0:
            mclrs5.append('red')  

########################    
        
##    ax1.title.get_name('k')
    ax1.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('Close_vwap')]),color='green', marker='o', linestyle='dashed',
     linewidth=1, markersize=2)
    # adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p2a=df.iloc[:,df.columns.get_loc('Close_vwap')]
    ax1.fill_between(p1, p2a-65,p2a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')


    
    ax1.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA-510')]))
    ax1.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA-1021')]))
    ax1.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA-2150')]))
    
    ax1.bar(df3a.iloc[:,df3a.columns.get_loc('s2')],pd.to_numeric(df3a.iloc[:,df3a.columns.get_loc('MOM')]), width=2, color=mclrs5)
##    ax1.bar(df3b.iloc[:,df3a.columns.get_loc('s2')],pd.to_numeric(df3b.iloc[:,df3b.columns.get_loc('MOM')]), width=2, color='yellow')

    
    ax1.bar(df4a.iloc[:,df4a.columns.get_loc('s2')],pd.to_numeric(df4a.iloc[:,df4a.columns.get_loc('MOM')]), width=2, color='blue')
    ax1.bar(df4b.iloc[:,df4a.columns.get_loc('s2')],pd.to_numeric(df4b.iloc[:,df4b.columns.get_loc('MOM')]), width=2, color='cyan')

##    ax1.bar(df3b.iloc[:,df3b.columns.get_loc('s2')],pd.to_numeric(df3b.iloc[:,df3b.columns.get_loc('MOM')]), width=2, color='yellow')


##    ax1.bar(df3.iloc[:,df3.columns.get_loc('s2')],pd.to_numeric(df3.iloc[:,df3.columns.get_loc('MOM')]), width=2, color='yellow')
##    ax1.bar(df4.iloc[:,df4.columns.get_loc('s2')],pd.to_numeric(df4.iloc[:,df4.columns.get_loc('MOM')]), width=2, color='blue')
##    
    ax1.legend(['Close_vwap', 'EMA-510','EMA-1021','EMA-2150','MOM'],loc=3, fontsize = 'x-small')
##    ax1.hlines(0, df.iloc[:,43].min(), df.iloc[:,43].max(), lw=1, color='black')
    ax1.hlines(0, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')

##    ax1.get_animated
##    ax1.grid(which='minor',visible=None,axis='both')
##    ax1.grid()

    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    ax5.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('adx')]))
##    ax2.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,43]))
    ax5.fill_between(p1, p2, where=(pd.to_numeric(p2) > 25), color='#00FF00')
    ax5.fill_between(p1, p2, where=(pd.to_numeric(p2) < 25), color='#ff0000')
    ax5.fill_between(p1, p2, where=(pd.to_numeric(p2) > 40), color='#00e5ff')
    ax5.hlines(40, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')
    ax5.legend(['adx (adx >40/breakout'],loc=3, fontsize = 'x-small')


    ax2.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('Close')]),color='black', marker='o', linestyle='dashed',
     linewidth=1, markersize=2)
    ax2.plot(df.iloc[:,bb],(df.iloc[:,df.columns.get_loc('vwap')]),\
             color='blue', marker='o', linestyle='dashed',\
             linewidth=1, markersize=1)
    ax2.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA_3s')]))
    ax2.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA_5s')]))
    ax2.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA_10s')]))
    ax2.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA_21s')]))
    ax2.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA_50s')]))
    ax2.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA_100s')]))
    ax2.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA_200s')]))
    ax2.legend(['Close','vwap','EMA_3s','EMA_5s','EMA_10s','EMA_21s','EMA_50s','EMA_100s','EMA_200s'],loc=2, fontsize = 'x-small')
    # adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p2a=df.iloc[:,df.columns.get_loc('Close')]
    ax2.fill_between(p1, p2a-65,p2a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')

    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('SARx')]
    ax3.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('Close_vwap')]),color='green', marker='o', linestyle='dashed',
     linewidth=1, markersize=2)

    # adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p2a=df.iloc[:,df.columns.get_loc('Close_vwap')]
    ax3.fill_between(p1, p2a-65,p2a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')

    
    ax3.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA_3_vwap')]))
    ax3.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA_5_vwap')]))
    ax3.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA_10_vwap')]))
    ax3.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA_21_vwap')]))
    ax3.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA_50_vwap')]))
    ax3.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('SARx')]))
    ax3.fill_between(p1, p2, where=(pd.to_numeric(p2) > 0), color='#00FF00')
    ax3.fill_between(p1, p2, where=(pd.to_numeric(p2) < 0), color='#ff0000')
    ax3.legend(['Close_vwap','EMA_3_vwap','EMA_5_vwap','EMA_10_vwap','EMA_21_vwap','EMA_50_vwap','SARx'],loc=2, fontsize = 'x-small')
##    ax3.hlines(0, df.iloc[:,43].min(), df.iloc[:,43].max(), lw=1, color='black')
    ax3.hlines(0, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')



##    ax4.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,4]),color='green', marker='o', linestyle='dashed',
##     linewidth=1, markersize=2)
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('CCI')]
    p3=100
    p4=-100

    g1=df.iloc[:,df.columns.get_loc('s2')]
    g2=df.iloc[:,df.columns.get_loc('RSI')]
    g3=70
    g4=30
    
    ax4.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('CCI')]))
    ax4.set_title('CCI')
        
    ax4.fill_between(p1, p2,p3, where=(pd.to_numeric(p2) > p3), color='#00FF00')
    ax4.fill_between(p1, p2,p4, where=(pd.to_numeric(p2) < p4), color='#ff0000')

    ax4.fill_between(g1, g2,g3, where=(pd.to_numeric(g2) > g3), color='#00FF00')
    ax4.fill_between(g1, g2,g4, where=(pd.to_numeric(g2) < g4), color='#ff0000')
    
    ax4.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('RSI')]))         
    ax4.legend(['CCI','RSI'],loc=2, fontsize = 'x-small')
    ax4.hlines(0, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')
    ax4.hlines(100, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')
    ax4.hlines(-100, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')
    ax4.hlines(30, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='green')
    ax4.hlines(70, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='green')

    # adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p2a=df.iloc[:,df.columns.get_loc('CCI')]
    ax4.fill_between(p1, p2a-65,p2a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')

    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('macd')] 
    ax6.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('macd')]))

    ax6.legend(['macd'],loc=3, fontsize = 'x-small')
    ax6.fill_between(p1, p2, p2+325, where=(pd.to_numeric(p2) > 0), color='#00FF00')
    ax6.fill_between(p1, p2,p2-5, where=(pd.to_numeric(p2) < 0), color='#ff0000')
    ax6.legend(['macd'],loc=3, fontsize = 'x-small')
    ax6.hlines(70, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=4, color='green')


    # adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p2a=df.iloc[:,df.columns.get_loc('macd')]
    ax6.fill_between(p1, p2a.min()-2-65,p2a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')

    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('squeeze_on')]
    ax7.plot(df.iloc[:,bb],(df.iloc[:,df.columns.get_loc('squeeze_on')]))
    ax7.fill_between(p1, p2, where=(p2 =='in_squeeze'), color='#00FF00')
##    ax2.fill_between(p1, p2, where=(p2 is None), color='#ff0000')
    ax7.legend(['squeeze_on'],loc=3, fontsize = 'x-small')

##    # adx
##    p1=df.iloc[:,df.columns.get_loc('s2')]
##    p2=df.iloc[:,df.columns.get_loc('adx')]
##    p2a=df.iloc[:,df.columns.get_loc('squeeze_on')]
##    ax7.fill_between(p1, p2a-65,p2a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')

    
##    ax1.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA-510')]))
##    ax1.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA-1021')]))
##    ax1.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA-2150')]))
##    
##    ax1.bar(df3a.iloc[:,df3a.columns.get_loc('s2')],pd.to_numeric(df3a.iloc[:,df3a.columns.get_loc('MOM')]), width=2, color='blue')
##    ax1.bar(df3b.iloc[:,df3a.columns.get_loc('s2')],pd.to_numeric(df3b.iloc[:,df3b.columns.get_loc('MOM')]), width=2, color='yellow')
##'EMA-510','EMA-1021','EMA-2150'
    df=df.loc[(df['s2'] > '09:00') & (df['s2'] < '16:01')]
    fig3, (gp,gp2,gp3) = plt.subplots(3,1,sharex=True)
    fig3.suptitle('baba5', fontsize=5)

  # , ax2a, ax3a,ax4a
##    if df.loc[:,'vwap'] > 800 & (type(df.loc[:,'vwap']) == int or float):

 
    bb=df.columns.get_loc('s2')
    df.sort_values(['s2'],ascending=True,inplace=True)

    plt.rc('legend',fontsize=3) # using a size in points
    plt.rc('legend',fontsize='small') # using a named size
    plt2.rc('legend',fontsize=3) # using a size in points
    plt2.rc('legend',fontsize='small') # using a named size


    plt.suptitle(str(df.iloc[3,df.columns.get_loc('ticker')])+str('  ')+str(p2b)+str('  ')+str(p2d))
    plt2.suptitle(str(df.iloc[3,df.columns.get_loc('ticker')])+str('  ')+str(p2b)+str('  ')+str(p2d))

    dfs2=df.loc[(df['Close_vwap'] > 0)]
    dfs3=df.loc[(df['Close_vwap'] < 0)]
    df.to_csv('/home/az2/hh.txt')

##    ax1a.bar(df3a.iloc[:,dfs2.columns.get_loc('s2')],pd.to_numeric(dfs2.iloc[:,df3a.columns.get_loc('MOM')]), width=2, color='blue')
##    ax1a.bar(df3b.iloc[:,dfs3.columns.get_loc('s2')],pd.to_numeric(dfs3.iloc[:,df3b.columns.get_loc('MOM')]), width=2, color='yellow')
##    ax1.bar(df3a.iloc[:,df3a.columns.get_loc('s2')],pd.to_numeric(df3a.iloc[:,df3a.columns.get_loc('MOM')]), width=2, color='blue')
##    ax1.bar(df3b.iloc[:,df3a.columns.get_loc('s2')],pd.to_numeric(df3b.iloc[:,df3b.columns.get_loc('MOM')]), width=2, color='yellow')

    clrs=[];clrs2=[]
    for x in df.index:
    ##    print(df.loc[x,'Close_vwap'])
        if df.loc[x,'Close_vwap'] < 0:
            clrs.append('red')
        else:
##            df.loc[x,'Close_vwap'] > 0:
            clrs.append('green')


##        if df.loc[x,'EMA_510'] <= 0:
##            clrs2.append('red')
##        elif df.loc[x,'EMA_510'] > 0:
##            clrs2.append('green')      
## was up
    df['clrs']=clrs
    print(df,'88')
    df.drop(['clrs'],axis=1,inplace=True)

# adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p5a=df.iloc[:,df.columns.get_loc('Close_vwap')]
    gp.fill_between(p1, p5a.min(),p5a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')

    
    gp.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('Close_vwap')],color=clrs,width=2)
    gp.legend(['Close_vwap','ADX > 40'],loc=3, fontsize = 'x-small')
    for x in df.index:     
            
        if df.loc[x,'MOM'] < 0:
            clrs2.append('red')
        else:
            clrs2.append('green')


     # adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p5a=df.iloc[:,df.columns.get_loc('Close_vwap')]
    gp.fill_between(p1, p5a.min(),0, where=(pd.to_numeric(p2) > 25) & (pd.to_numeric(p2) < 40), color= '#ff9a00')
           
            
##    gp2.bar(df.iloc[:,df.columns.get_loc('MOM')],df.iloc[:,df.columns.get_loc('MOM')],color=clrs2,width=2)
##    gp2.legend(['MOM'],loc=3, fontsize = 'x-small')


# adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p5a=df.iloc[:,df.columns.get_loc('Close')]
    gp2.fill_between(p1, p5a.min(),p5a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')

    gp2.plot(df.iloc[:,bb],(df.iloc[:,df.columns.get_loc('vwap')]),\
             color='blue', marker='o', linestyle='dashed',\
             linewidth=1, markersize=1)
             
        

    gp2.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('Close')]),color='black', marker='o', linestyle='dashed',
     linewidth=1, markersize=2)

    dfp=df.loc[df['Close']>df['SAR']]
    dfg=df.loc[df['Close']<df['SAR']]
   
    gp2.plot(dfp.iloc[:,bb],pd.to_numeric(dfp.iloc[:,dfp.columns.get_loc('SAR')]),color='Green', marker='v', linestyle='dashed',\
                 linewidth=0, markersize=2)
    gp2.plot(dfg.iloc[:,bb],pd.to_numeric(dfg.iloc[:,dfg.columns.get_loc('SAR')]),color='Red', marker='^', linestyle='dashed',\
                 linewidth=0, markersize=2)


    # adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p5a=df.iloc[:,df.columns.get_loc('Close')]
    gp2.fill_between(p1, p5a.min(),p5a, where=(pd.to_numeric(p2) > 25) & (pd.to_numeric(p2) < 40), color= '#ff9a00')
    
        
##    gp2.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('SARx')]),color='red', marker='o', linestyle='dashed',
##     linewidth=1, markersize=2)

    gp2.legend(['Close','SAR','ADX > 40','vwap'],loc=2, fontsize = 'x-small')
##    gp2.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('SAR')],color='red',width=2)
##    gp2.legend(['SAR'],loc=3, fontsize = 'x-small')
##    gp2.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('SARx')],color='blue',width=2)
##    gp2.legend(['SARx'],loc=3, fontsize = 'x-small')



# adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p5a=df.iloc[:,df.columns.get_loc('VZO')]
    gp3.fill_between(p1, p5a.min(),p5a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')

# adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p5a=df.iloc[:,df.columns.get_loc('VZO')]
    gp3.fill_between(p1, p5a.min(),p5a, where=(pd.to_numeric(p2) > 25) & (pd.to_numeric(p2) < 40), color= '#ff9a00')
    

    gp3.plot(df.loc[:,'s2'],df.loc[:,'VZO'],color='black', marker='o', linestyle='dashed',linewidth=1, markersize=2)
    gp3.legend(['VZO','ADX > 40'],loc=3, fontsize = 'x-small')

    ##    ax1.hlines(0, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')
    gp3.hlines(60, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')
    gp3.hlines(40, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')
    gp3.hlines(-60, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='g')
    gp3.hlines(-40, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='g')
    gp3.hlines(-5, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=2, color='green',label='ddd')
    gp3.hlines(15, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=2, color='red')

    
##    gp3.bar(df.iloc[:,df.columns.get_loc('EMA_510')],df.iloc[:,df.columns.get_loc('EMA_510')],color=clrs,width=2)
##    gp3.legend(['EMA_510'],loc=3, fontsize = 'x-small')

##
##    dfs2=df.loc[(df['EMA-510'] > 0)]
##    dfs3=df.loc[(df['EMA-510'] < 0)]
##    ax2a.bar(dfs2.iloc[:,dfs2.columns.get_loc('s2')],pd.to_numeric(dfs2.iloc[:,dfs2.columns.get_loc('EMA-510')]), width=2, color='blue')
##    ax2a.bar(dfs3.iloc[:,dfs3.columns.get_loc('s2')],pd.to_numeric(dfs3.iloc[:,dfs3.columns.get_loc('EMA-510')]), width=2, color='cyan')
##    ax2a.legend(['EMA-510'],loc=3, fontsize = 'x-small')
##
##
##
##    dfs2=df.loc[(df['EMA-1021'] > 0)]
##    dfs3=df.loc[(df['EMA-1021'] < 0)]
##    ax3a.bar(dfs2.iloc[:,dfs2.columns.get_loc('s2')],pd.to_numeric(dfs2.iloc[:,dfs2.columns.get_loc('EMA-1021')]), width=2, color='blue')
##    ax3a.bar(dfs3.iloc[:,dfs3.columns.get_loc('s2')],pd.to_numeric(dfs3.iloc[:,dfs3.columns.get_loc('EMA-1021')]), width=2, color='cyan')
##    ax3a.legend(['EMA-1021'],loc=3, fontsize = 'x-small')
##
##    dfs2=df.loc[(df['EMA-2150'] > 0)]
##    dfs3=df.loc[(df['EMA-2150'] < 0)]
##    ax4a.bar(dfs2.iloc[:,dfs2.columns.get_loc('s2')],pd.to_numeric(dfs2.iloc[:,dfs2.columns.get_loc('EMA-2150')]), width=2, color='blue')
##    ax4a.bar(dfs3.iloc[:,dfs3.columns.get_loc('s2')],pd.to_numeric(dfs3.iloc[:,dfs3.columns.get_loc('EMA-2150')]), width=2, color='cyan')
##    ax4a.legend(['EMA-2150'],loc=3, fontsize = 'x-small')
##    ax4a.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('Close')]),color='black', marker='o', linestyle='dashed',
##     linewidth=1, markersize=2)
##    ax4a.legend(['Close'],loc=3, fontsize = 'x-small')



##    print(df.columns[43],'column 43')
##    ax2.title(df.iloc[3,df.columns.get_loc('ticker')])


##        df['adx'] = ta.ADX(df['High'], df['Low'], df['Close'], timeperiod=14)
##        df['ATR'] = ta.ATR(df['High'], df['Low'], df['Close'], timeperiod=14)
##        df['TR'] = abs(df['High'] - df['Low'])
##        df['AD'] = ta.ADOSC(df['High'], df['Low'], df['Close'], df['Volume'])
####        df['lower_keltner'] = df['20sma'] - (df['ATR'] * 1.5)
####        df['upper_keltner'] = df['20sma'] + (df['ATR'] * 1.5)
##        df['SAR'] = ta.SAR(df['High'], df['Low'], acceleration=300, maximum=5)
##        df['SARx'] = df['Close'] - df['SAR']
##        df['PLUS_DI'] = ta.PLUS_DI(df['High'],df['Low'],df['Close'],timeperiod=14)
##        df['MINUS_DI'] = ta.MINUS_DI(df['High'], df['Low'], df['Close'], timeperiod=14)
##        df['PLUS_DM'] = ta.PLUS_DM(df['High'], df['Low'], timeperiod=14)
##        df['MINUS_DM'] = ta.MINUS_DM(df['High'], df['Low'], timeperiod=14)
##        df['DM_delta'] = df['PLUS_DM'] - df['MINUS_DM']
##        df['DI_delta'] = df['PLUS_DI'] - df['MINUS_DI']

    df=df.loc[(df['s2'] > '09:00') & (df['s2'] < '16:01')]

    df.sort_values(['s2'],ascending=True,inplace=True)
    print(df,'5555555555555555555555555555555555  ')
    fig2, (ax3,ax5) = plt.subplots(2, 1,sharex=True)
    fig2.suptitle('baba6', fontsize=5)
     
    bb=df.columns.get_loc('s2')
    

    plt.rc('legend',fontsize=3) # using a size in points
    plt.rc('legend',fontsize='small') # using a named size
    plt2.rc('legend',fontsize=3) # using a size in points
    plt2.rc('legend',fontsize='small') # using a named size

    plt.suptitle(str(df.iloc[3,df.columns.get_loc('ticker')])+str('  ')+str(p2b)+str('  ')+str(p2d))
    plt2.suptitle(str(df.iloc[3,df.columns.get_loc('ticker')])+str('  ')+str(p2b)+str('  ')+str(p2d))

##    ax1.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,19]),color='green', marker='o', linestyle='dashed',
##     linewidth=1, markersize=2)

##    p1=df.iloc[:,df.columns.get_loc('s2')]
##    p2=df.iloc[:,df.columns.get_loc('macd')] 
##    ax1.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('macd')]))
##
##    ax1.legend(['macd'],loc=3, fontsize = 'x-small')
##    ax1.fill_between(p1, p2, where=(pd.to_numeric(p2) > 0), color='#00FF00')
##    ax1.fill_between(p1, p2, where=(pd.to_numeric(p2) < 0), color='#ff0000')
##    ax1.legend(['macd'],loc=3, fontsize = 'x-small')




##    ax1.hlines(0, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')
##    ax1.hlines(100, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')
##    ax1.hlines(-100, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')
##    ax1.hlines(20, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='g')
##    ax1.hlines(70, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='g')


##    p1=df.iloc[:,df.columns.get_loc('s2')]
##    p2=df.iloc[:,df.columns.get_loc('adx')]
##    ax2.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('adx')]))
####    ax2.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,43]))
##    ax2.fill_between(p1, p2, where=(pd.to_numeric(p2) > 25), color='#00FF00')
##    ax2.fill_between(p1, p2, where=(pd.to_numeric(p2) < 25), color='#ff0000')
##    ax2.legend(['adx'],loc=3, fontsize = 'x-small')


# adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p5a=df.iloc[:,df.columns.get_loc('ATR')]
    ax3.fill_between(p1, p5a.min(),p5a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')



    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('ATR')]
    ax3.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('ATR')]))
    ax3.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('TR')]))
    ax3.legend(['ATR','TR'],loc=3, fontsize = 'x-small')


    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('squeeze_on')]

##    for x in df.index:
##        if df.iloc[x,df.columns.get_loc('squeeze_on')]=='in_squeeze':
##            df.iloc[x,df.columns.get_loc('squeeze_on')]=int(7)


    
##    p1=df.iloc[:,df.columns.get_loc('s2')]
##    p2=df.iloc[:,df.columns.get_loc('squeeze_on')]
##    ax4.plot(df.iloc[:,bb],(df.iloc[:,df.columns.get_loc('squeeze_on')]))
##    ax4.fill_between(p1, p2, where=(p2 =='in_squeeze'), color='#00FF00')
####    ax2.fill_between(p1, p2, where=(p2 is None), color='#ff0000')
##    ax4.legend(['squeeze_on'],loc=3, fontsize = 'x-small')



# adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p5a=df.iloc[:,df.columns.get_loc('Boling_lower2')]
    ax5.fill_between(p1, p5a.min(),p5a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')




    d1=df.iloc[:,df.columns.get_loc('upper_keltner')]
    d2=df.iloc[:,df.columns.get_loc('Boling_upper2')]

    f1=df.iloc[:,df.columns.get_loc('lower_keltner')]
    f2=df.iloc[:,df.columns.get_loc('Boling_lower2')]                                

    ax5.plot(df.iloc[:,bb],(df.iloc[:,df.columns.get_loc('upper_keltner')]))
    ax5.plot(df.iloc[:,bb],(df.iloc[:,df.columns.get_loc('lower_keltner')]))
    ax5.plot(df.iloc[:,bb],(df.iloc[:,df.columns.get_loc('Close')]))
    ax5.plot(df.iloc[:,bb],(df.iloc[:,df.columns.get_loc('Boling_upper2')]))
    ax5.plot(df.iloc[:,bb],(df.iloc[:,df.columns.get_loc('Boling__middle2')]))
    ax5.plot(df.iloc[:,bb],(df.iloc[:,df.columns.get_loc('Boling_lower2')]))
    ax5.plot(df.iloc[:,bb],(df.iloc[:,df.columns.get_loc('vwap')]),\
             color='blue', marker='o', linestyle='dashed',\
             linewidth=1, markersize=1)
##    ax5.fill_between(pd.to_numeric(d2), pd.to_numeric(d1), where=(pd.to_numeric(d2) < pd.to_numeric(d1)), color='#00FF00')
    ax5.fill_between(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('Boling_upper2')], df.iloc[:,df.columns.get_loc('Boling_lower2')]
                     ,color='#00FF00')
    ax5.fill_between(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('upper_keltner')], df.iloc[:,df.columns.get_loc('lower_keltner')]
                     ,color='black')
##    ax5.fill_between(f1, f2, where=(pd.to_numeric(f2) < f1), color='#ff0000')
    ax5.legend(['upper_keltner','lower_keltner','Close','Boling_upper2','Boling__middle2','Boling_lower2','vwap'],loc=3, fontsize = 'x-small')


#######################################
## 44
    df['color']=""
    df['Volume_g']=""
    df['Volume_r']=""
    df['Close_r']=""
    df['Close_g']=""
    df['Close_h']=""

    for x in df.index:

    ##    df['ticker'].loc[x]=ticker
        if df['Close'].loc[x]-df['Open'].loc[x] >= 0:
            df['color'].loc[x]=='green'      
            df['Volume_g'].loc[x]=df['Volume'].loc[x]
        else:
            df['Volume_g'].loc[x]=0
    ##        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]+.1
        #            print(x,'  ','Green','  ',df['ns'].loc[x])
        if df['Close'].loc[x]-df['Open'].loc[x] < 0:
            df['color'].loc[x]=="Red"       
            df['Volume_r'].loc[x]=-1*df['Volume'].loc[x]

        if df['Close'].loc[x]-df['Close'].shift(1).loc[x] < 0:
            df['Close_r'].loc[x]=df['Close'].loc[x]

        if df['Close'].loc[x]-df['Close'].shift(1).loc[x] > 0:
            df['Close_g'].loc[x]=df['Close'].loc[x]

    ##    elif df['Close'].loc[x]-df['Close'].shift(1).loc[x] < 0.1 and df['Close'].loc[x]-df['Close'].shift(1).loc[x] > -0.1:
    ##        df['Close_h'].loc[x]=df['Close'].loc[x]

            
    for x in df.index:
        if df['Volume_g'].loc[x]=='':
            df['Volume_g'].loc[x]=0
        if df['Volume_r'].loc[x]=='':
            df['Volume_r'].loc[x]=0
        if df['Close_g'].loc[x]=='':
            df['Volume_g'].loc[x]=0
        if df['Close_r'].loc[x]=='':
            df['Close_g'].loc[x]=0
        if df['Close_h'].loc[x]=='':
            df['Close_h'].loc[x]=0
     
    df=df.loc[(df['s2'] > '09:00') & (df['s2'] < '16:01')]
    fig,(bx2,bx3,bx4,bx5,bx6,bx7,bx8,bx9) = plt.subplots(8,1,sharex=True)
    fig.suptitle('baba7', fontsize=9)
 
    mclrs=[];mclrs2=[];mclrs3=[];mclrs4=[];mclrs5=[];mclrs6=[]
    
    for x in df.index:

    ##    print(df.loc[x,'Close_vwap'])
        if df.loc[x,'Close_vwap'] < 0:
            mclrs.append('red')
        elif df.loc[x,'Close_vwap'] >= 0:
            mclrs.append('green')
            
        if df.loc[x,'EMA-510'] < 0:
            mclrs2.append('red')
        elif df.loc[x,'EMA-510'] >= 0:
            mclrs2.append('green')
            
        if df.loc[x,'EMA-1021'] < 0:
            mclrs3.append('red')
        elif df.loc[x,'EMA-1021'] >= 0:
            mclrs3.append('green')
            
        if df.loc[x,'EMA-2150'] < 0:
            mclrs4.append('red')
        elif df.loc[x,'EMA-2150'] >= 0:
            mclrs4.append('green')
    ####################################        
##        if df.iloc[x,df.columns.get_loc('MOM')] > 0 and df.iloc[x,df.columns.get_loc('MOM')] - df.shift(1).iloc[x,df.columns.get_loc('MOM')] > 0:
##            mclrs5.append('green')
##        elif df.iloc[x,df.columns.get_loc('MOM')] > 0 and  df.iloc[x,df.columns.get_loc('MOM')] - df.shift(1).iloc[x,df.columns.get_loc('MOM')] < 0:
##            mclrs5.append('cyan')        
##        elif df.iloc[x,df.columns.get_loc('MOM')] < 0 and df.iloc[x,df.columns.get_loc('MOM')] - df.shift(1).iloc[x,df.columns.get_loc('MOM')] > 0:
##            mclrs5.append('red')
##        elif df.iloc[x,df.columns.get_loc('MOM')] < 0 and  df.iloc[x,df.columns.get_loc('MOM')] - df.shift(1).iloc[x,df.columns.get_loc('MOM')] < 0:
##            mclrs5.append('green')

        if df.loc[x,'MOM'] > 0 and (df.loc[x,'MOM'] - df.shift(1).loc[x,'MOM']) > 0:
            mclrs5.append('green')
        elif df.loc[x,'MOM'] > 0 and (df.loc[x,'MOM'] - df.shift(1).loc[x,'MOM']) < 0:
            mclrs5.append('red')
        elif df.loc[x,'MOM'] < 0 and (df.loc[x,'MOM'] - df.shift(1).loc[x,'MOM']) > 0:
            mclrs5.append('red')
        elif df.loc[x,'MOM'] < 0 and (df.loc[x,'MOM'] - df.shift(1).loc[x,'MOM']) < 0:
            mclrs5.append('red')    
            
            
            
                     
##        if df.loc[x,'Close'] < df.shift(1).loc[x,'Close']:
##            mclrs6.append('blue')
##        elif df.loc[x,'Close'] >= df.shift(1).loc[x,'Close']:
##            mclrs6.append('green')    
        
    import math
    print((df.iloc[:25,df.columns.get_loc('Volume_g')]))
    print(type(df.iloc[25,df.columns.get_loc('Volume_g')]))
# 214


# adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p2a=df.iloc[:,df.columns.get_loc('Close')]
    p5a=df.iloc[:,df.columns.get_loc('Close_vwap')]
    bx2.fill_between(p1, p5a.min(),p5a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')

    bx2.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('Close_vwap')],color=mclrs,width=2,label='Close_vwap')
    bx2.legend(['Close_vwap'],loc=3, fontsize = 'x-small')
##    if m5.isdigit()==True and m6.isdigit()==True:
##    print(m5,m6,math.atan2(math.radians(m5),math.radians(m6)),'  jjj')
#214
##    dfp=df.loc[df['Close']>df['SAR']]
##    dfg=df.loc[df['Close']<df['SAR']]
##    dfp=df.loc[df.iloc[:,df.columns.get_loc('Close_vwap')] < 0 ]
##    dfg=df.loc[df.iloc[:,df.columns.get_loc('Close_vwap')] > 0 ]

    dfp=df.loc[df.iloc[:,df.columns.get_loc('Close_vwap')] >= 0]
    dfg=df.loc[df.iloc[:,df.columns.get_loc('Close_vwap')] < 0]

 
##    print(df.shape,'   ',dfp.shape,'   ',dfg.shape)
##    sys.exit()
##    dfg=df.loc[df.iloc[:,df.columns.get_loc('Close_vwap')]-df.shift(1).iloc[:,df.columns.get_loc('Close_vwap')] < 0 ]
##    bx2.bar(dfp.iloc[:,dfp.columns.get_loc('s2')],dfp.iloc[:,dfp.columns.get_loc('Close_vwap')],color='blue', marker='o', markersize=1)
##    bx2.bar(dfg.iloc[:,dfg.columns.get_loc('s2')],dfg.iloc[:,dfg.columns.get_loc('Close_vwap')],color='yellow', marker='o', markersize=1)
##    bx2.plot(dfg.iloc[:,dfg.columns.get_loc('s2')],dfg.iloc[:,dfg.columns.get_loc('Close_vwap')],color='yellow', marker='o', markersize=1)
##            
## 

# adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p2a=df.iloc[:,df.columns.get_loc('Close')]
    p5a=df.iloc[:,df.columns.get_loc('EMA-510')]
    bx3.fill_between(p1, p5a.min(),p5a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')

    
    bx3.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA-510')],color=mclrs2,width=2)
    bx3.legend(['EMA-510'],loc=3, fontsize = 'x-small')

# adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p5a=df.iloc[:,df.columns.get_loc('EMA-1021')]
    bx4.fill_between(p1, p5a.min(),p5a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')

    bx4.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA-1021')],color=mclrs3,width=2)
    bx4.legend(['EMA-1021'],loc=3, fontsize = 'x-small')

# adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p5a=df.iloc[:,df.columns.get_loc('EMA-2150')]
    bx5.fill_between(p1, p5a.min(),p5a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')
    bx5.legend(['EMA-2150'],loc=3, fontsize = 'x-small')

    bx5.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA-2150')],color=mclrs4,width=2)



# adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p5a=df.iloc[:,df.columns.get_loc('MOM')]
    bx6.fill_between(p1, p5a.min(),p5a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')



    bx6.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('MOM')],color=mclrs5,width=2)
    bx6.legend(['MOM/under const'],loc=3, fontsize = 'x-small')
############### ############### ############### ############### ############### ############### ############### 
############### ############### ############### ############### ############### ############### ###############
############### ############### ############### ############### ############### ############### ############### 
    bx7.plot(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('Close')])
    
###############  adding adx in close #################
    bx7.vlines(df.iloc[300,df.columns.get_loc('s2')],\
               df.iloc[:,df.columns.get_loc('Close')].min(), \
               df.iloc[:,df.columns.get_loc('Close')].max(),\
               linestyles ="dashed", colors ="k", label = 'test')

    # adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p2a=df.iloc[:,df.columns.get_loc('Close')]
    

##    print(p2)
##    sys.exit()

    bx7.fill_between(p1, p2a-65,p2a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')
    ## where:
    ## p2 = 'adx'
    ## p1 = 's2'
    ## p2a = 'Close'
    ## color #00e5ff = 'blue' [or 'adx' > 40]
## 66 #########################################
##    p1=df.iloc[:,df.columns.get_loc('s2')]
##    p2=df.iloc[:,df.columns.get_loc('macd')] 
##    ax6.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('macd')]))
##
##    ax6.legend(['macd'],loc=3, fontsize = 'x-small')
##    ax6.fill_between(p1, p2, where=(pd.to_numeric(p2) > 0), color='#00FF00')
##    ax6.fill_between(p1, p2, where=(pd.to_numeric(p2) < 0), color='#ff0000')
##    ax6.legend(['macd'],loc=3, fontsize = 'x-small')

    # macd
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('macd')]
    p2a=df.iloc[:,df.columns.get_loc('Close')]

    bx7.fill_between(p1, p2a-3,p2a, where=(pd.to_numeric(p2) > 0), color='#33ff00')
    bx7.fill_between(p1, p2a-3,p2a, where=(pd.to_numeric(p2) < 0), color='#c3c4c2')
    bx7.legend(['Close/macd/adx>40(breakout)/SAR'],loc=3, fontsize = 'x-small')
    ## where:
    ## p2 = 'macd'
    ## p1 = 's2'
    ## p2a = 'Close'  
    ## color=#33ff00' macd > 0 --- Green.
    ## color='#c3c4c2' macd < 0 -- Grey.


    dfp=df.loc[df['Close']>df['SAR']]
    dfg=df.loc[df['Close']<df['SAR']]
   
    bx7.plot(dfp.iloc[:,bb],pd.to_numeric(dfp.iloc[:,dfp.columns.get_loc('SAR')]+7),color='Green', marker='v', linestyle='dashed',\
                 linewidth=0, markersize=2)
    bx7.plot(dfg.iloc[:,bb],pd.to_numeric(dfg.iloc[:,dfg.columns.get_loc('SAR')]-7),color='Red', marker='^', linestyle='dashed',\
                 linewidth=0, markersize=2)
##    bx7.set_facecolor('xkcd:mint green')
############### ############### ############### ############### ############### ############### ############### 
############### ############### ############### ############### ############### ############### ###############
############### ############### ############### ############### ############### ############### ############### 
###########################################3

    

    bx8.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('Volume_r')],color='red',width=2)
    bx8.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('Volume_g')],color='green',width=2)
    bx8.legend(['Volume'],loc=3, fontsize = 'x-small')
###############  adding adx in close #################
##    bx8.vlines(df.iloc[300,df.columns.get_loc('s2')],\
##               df.iloc[:,df.columns.get_loc('Close')].min(), \
##               df.iloc[:,df.columns.get_loc('Close')].max(),\
##               linestyles ="dashed", colors ="k", label = 'test')

    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p2a=df.iloc[:,df.columns.get_loc('Volume_g')]
    p3a=df.iloc[:,df.columns.get_loc('Volume_r')]

    print(p3a,'  ',p2,'  ',p2a,' =========================================== fffff')
    
##    bx8.fill_between(p1,p3a-5,p3a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')
#########################################################
    bx9.plot(df.loc[:,'s2'],df.loc[:,'VZO'],color='black', marker='o', linestyle='dashed',linewidth=1, markersize=2)
    bx9.legend(['VZO/adx > 40(breakout)'],loc=3, fontsize = 'x-small')

    ##    ax1.hlines(0, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')
    bx9.hlines(60, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')
    bx9.hlines(40, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')
    bx9.hlines(-60, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='g')
    bx9.hlines(-40, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='g')
    bx9.hlines(-5, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=2, color='green',label='ddd')
    bx9.hlines(15, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=2, color='red')
    



    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p2a=df.iloc[:,df.columns.get_loc('VZO')]
    

##    print(p2)
##    sys.exit()
    bx9.fill_between(p1, -100,10, where=(pd.to_numeric(p2) > 40), color='#00e5ff')

###########################################################
    bp1=df.iloc[:,df.columns.get_loc('s2')]
    bp2=df.iloc[:,df.columns.get_loc('squeeze_on')]
    bp2a=df.iloc[:,df.columns.get_loc('VZO')]
    bx9.fill_between(bp1, -100,100, where=(bp2 =='in_squeeze'), color='#00FF00')
##    ax2.fill_between(p1, p2, where=(p2 is None), color='#ff0000')
##    bx9.legend(['squeeze_on'],loc=3, fontsize = 'x-small')



#########################################################
    bx2.set_ylabel('Cl_vwap',loc='top',labelpad=4)
    bx3.set_ylabel('EMA-510',loc='top',labelpad=4)
    bx4.set_ylabel('EMA-1021',loc='top',labelpad=4)
    bx5.set_ylabel('EMA-2150',loc='top',labelpad=4)
    bx6.set_ylabel('EMA-MOM',loc='top',labelpad=4)
    bx7.set_ylabel('Close',loc='top',labelpad=4)
    bx8.set_ylabel('Volume',loc='top',labelpad=4)


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
##    plt.show()
##    plt2.legend(['Close'])          
##    plt2.show()
    import time
    plt.show()
##    plt.show(block=False)
##    start=time.localtime()
##    plt.pause(3)
##    end=start+(20)
    input("hit[enter] to end.")
    plt.close('all')
    import gc
    gc.garbage.clear()


##            df['EMA-35'] = df['EMA_3'] - df['EMA_5']
##        df['EMA-510'] = df['EMA_5'] - df['EMA_10']
##        df['EMA-1021'] = df['EMA_10'] - df['EMA_21']
##        df['EMA-2150'] = df['EMA_21'] - df['EMA_50']
##        df['EMA_3_vwap'] = df['EMA_3'] - df['vwap']
##        df['EMA_5_vwap'] = df['EMA_5'] - df['vwap']
##        df['EMA_10_vwap'] = df['EMA_10'] - df['vwap']
##        df['EMA_21_vwap'] = df['EMA_21'] - df['vwap']
##        df['EMA_50_vwap'] = df['EMA_50'] - df['vwap']
##        df['macd_35'], df['macdsignal'], df['macdhist'] = ta.MACD(
##        df['Close'], fastperiod=3, slowperiod=5, signalperiod=3)
##        df['Close_EMA3'] = df['Close'] - df['EMA_3']
##        df['Close_EMA5'] = df['Close'] - df['EMA_5']
##        df['Close_EMA10'] = df['Close'] - df['EMA_10']
##        df['Close_EMA21'] = df['Close'] - df['EMA_21']
##        df['Close_EMA50'] = df['Close'] - df['EMA_50']
##        df['Close_vwap'] = df['Close'] - df['vwap']

        
    ##plt.text(df.iloc[:,0],pd.to_numeric(df.iloc[:,1]),'s',horizontalalignment='right')
    ##plt.annotate('k',df.iloc[:,0],pd.to_numeric(df.iloc[:,1]))

##plt.show()
##plt.show(block=False)
##plt.pause(3)
##plt.close()

def main(df7a,df8,df9,df9a):
    
    import gc
    import pandas as pd

    gc.garbage.clear()

    df9=pd.DataFrame()
    print('garbage cleared ==========================================================================')

    print('====================================================') 
    
    t5=['tsla']

    dict={
    ##      'nasdaq100':nasdaq100,
    ##      'dji':dji,
    ##      'djTransport':djTransport,
    ##      'etf':etf,
          't5':t5
    ##      't6':t6
    ##      's_p_500':s_p_500
          }


    b=[]

    u45=len(t5)
    global p2b
    global p2c
    import datetime as dt

    
##    print('start of mafin, 4444')   
    todays_date = dt.date.today 
    print(todays_date(),"-- Today's Date --")
    
    g=pd.date_range('2022-02-04', todays_date(),freq=pd.offsets.BDay())

    print(g,"-- Date array --")
    print('Script is going to check # of days = ',len(g))
    k=0
    for x in g:
        print('====================================================')
        u33=x.date()
        print(x.date(),' date in loop')

        p2b=x
        k=k+1     
        px=pd.Series(p2b)
        px=pd.to_datetime(px)
        p2c=px.dt.day_name()
        global p2d
        p2d=str(p2c).split(' ')[4]

        p2b=str(p2b)
    ##    p2b='2022-02-03'
    ##    p2c=datetime.datetime.strptime(p2b,'%Y-%m-%d').weekday()
    ##    p2c=pd.to_datetime(p2b).datetime.datetime.day_name()


        ATR_target=0
        adx_target=0


        p=d3=datetime.datetime.date(parser.parse(p2b))+datetime.timedelta(days=1)
        d2=str(p)

        pdate=p
        d3=datetime.datetime.date(parser.parse(d2))-datetime.timedelta(days=1)


##        print('end of main, 4444')  
        for y in dict:
                for x2 in dict[y]:
                        
##                        print(y,'  ',x2)

##                        print('start of s4, 4445') 
        # ===================================================================================================== >   [55]                
                        u33,y,d2,d3,gt4=s4(u33,y , x2,ATR_target,adx_target,d2,d3)
##                        print('end of s4, 4445')
##                        print('====================================================')
                        
##        print('====================================================') 



        print(" s4 ")
        print('s4 input [u33,y , x2,ATR_target,adx_target,d2,d3]', u33,y , x2,ATR_target,adx_target,d2,d3)
        print('s4 output [u33,y,d2,d3,gt4]',u33,y,d2,d3,gt4)
        print(" s4 ")
        print('\n\n\n')
        
        u33,dfd=s5c(u33,y,d2,d3,gt4)


        print(" s5c ")
        print('s5c input [u33,y,d2,d3,gt4]', u33,y,d2,d3,gt4)
        print('s5c output [u33,dfd] ',u33,dfd)
        print(" s5c ")
        print('\n\n\n')

##        df7a=pd.DataFrame(columns=['stragety','Date','ticker','Buy_at','Sell_at','Profit','b_Close_vwap','b_macd','b_mom','b_VZO','b_CCI'])
        print('\n\n\n\n\n')
##        print(df7a,' -------------------------------------------------------------- before')


        df=dfd
        print(dfd,'input to s6')
        df,df7=s6(df,u33,df7a)
        print(df,'output to s6')   
        df8=df7.append(df7)
        
        
##        print(df8,'/// df7')
##        print('s45=',s45,'   v4=',v4,'   sell_at:',v5)

##        print(df7,' df7 =========== from main ===========')
##        plot3(df5)
##        print(df,'s6')

    df9=df9.append(df8)
    return(df9)
    print(df9,'88')

df7a=pd.DataFrame()
df7a=pd.DataFrame(columns=['stragety','Date','ticker','Buy_at','Sell_at','Profit','b_Close_vwap','b_macd','b_mom','b_VZO','b_CCI'])

df8=pd.DataFrame()
df9=pd.DataFrame()
df9a=pd.DataFrame()

main(df7a,df8,df9,df9a)
df9a=df9a.append(df8)
print(df9a,' df9a ==================stupid ======================')
print('pppp')
