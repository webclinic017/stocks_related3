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




def s4(u33,y , x2,ATR_target,adx_target,d2,d3,g):
    import datetime
    import pandas as pd
    
    
    
        
        


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
##    df = yf.download(x2,start=d3,end=d2,interval='1m',auto_adjust = True,threads = True,prepost=True,progress=False, proxies=proxyb)

    print(x2)

    df3=pd.DataFrame()
    d2=str(g[0]).split(' ')[0]
    d3=str(g[len(g)-1]).split(' ')[0]

    gf=pd.DataFrame()
           
    for x in g:
        p=str(x).split(' ')[0]   
        df = yf.download(x2,start=d2,end=d3,interval='1m',auto_adjust = True,threads = True,prepost=True,progress=False, proxies=proxyb)
        df3=df3.append(df)
        gf=gf.append(df)
##        print(df,' 55')

    print(gf)    
    df=gf


    import pandas as pd
    import talib as ta
    import finta as f
    from finta import TA as ff
##    df=gt4
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
    df.to_csv('/home/az2/557/df_input.csv')
    tt=df['s3'].unique()
    print(len(tt),' no of days/dates')    


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
    
    g=pd.date_range('2022-02-10', todays_date(),freq=pd.offsets.BDay())

    print(g,"-- Date array --")
    print('Script is going to check # of days = ',len(g))
    k=0
    for x in g:
        
        print('====================================================')
        u33=x.date()
##        print(x.date(),' date in loop')

        p2b=x
             
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
                        u33,y,d2,d3,gt4=s4(u33,y , x2,ATR_target,adx_target,d2,d3,g)

##                        print('end of s4, 4445')
##                        print('====================================================')
                        
##        print('====================================================') 



##        print(" s4 ")
##        print('s4 input [u33,y , x2,ATR_target,adx_target,d2,d3]', u33,y , x2,ATR_target,adx_target,d2,d3)
##        print('s4 output [u33,y,d2,d3,gt4]',u33,y,d2,d3,gt4)
##        print(" s4 ")
##        print('\n\n\n')

   
        u33,dfd=s5c(u33,y,d2,d3,gt4)
       




        df=dfd
##        print(dfd,'input to s6')

        df=pd.DataFrame(df)
        print('\n')
        print('jjjj')
        print('\n')
        print(df7a,'666/df7a','  ',u33)
        print(df,'667/df','  ',u33)
        df7a=s6(df,u33,df7a)

        print(df7a,'df7a')
##        print(df7.columns,' hhhhhh')
##        sys.exit()
        

##
##        if df7a==empty:
##   
##            s5d={'stragety':'-1','Date':str(u33),'ticker':s45,'Buy_at':'50','Sell_at':'50','Profit':0,\
##             'b_Close_vwap':'55','b_macd':'dummy','b_mom':'dummy','b_VZO':'dummy','b_CCI':'dummy'}
##            df7a=df7a.append(s5d,ignore_index=True)
            
##        print(df7,'output_df7')
##        print('\n\n')
##        print(df,'output_df')
##        print('\n\n')
        
'''            
        df8=df8.append(df7)
        print('\n\n')
        print('k=',k,' len(g)=',len(g),'   ',g[k],'  ',u33)
        if k==len(g)-1:
            print(k,'haaalo')
            print(df8.iloc[:,:6],'output_df8')
            print('\n')
            print(t5,'  dates array',g,'    ',len(g))


            print('\n\n\n')
            print(df8.columns)
            
##        print('\n')
##        print('sell_condition=',sell_condition)
##        print('\n')
##        print('buy_condition=',buy_condition)

        k=k+1

        
        
        
##        print(df8,'/// df7')
##        print('s45=',s45,'   v4_sell=',v4_sell,'   sell_at:',v5_buy)

##        print(df7,' df7 =========== from main ===========')
##        plot3(df5)
##        print(df,'s6')

    df9=df8.append(df8)
    return(df9)
    print(df9,'====df9')

'''


df7a=pd.DataFrame()


        
df7a=pd.DataFrame(columns=['stragety','Date','ticker','Buy_at','Sell_at','Profit'\
             'b_Time','s_Time',\
             'b_Close_vwap','b_macd','b_mom','b_VZO','b_CCI',
             'b_break',\
             's_Close_vwap','s_macd','s_mom','s_VZO','s_CCI'])




df8=pd.DataFrame()
df9=pd.DataFrame()
df9a=pd.DataFrame()

main(df7a,df8,df9,df9a)
df9a=df9a.append(df8)
print(df9a,' df9a ==================stupid ======================')
print('pppp')
