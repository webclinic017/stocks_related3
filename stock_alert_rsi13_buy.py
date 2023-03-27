import os, pandas
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

# create a Trace object, telling it what to ignore, and whether to
# do tracing or line-counting or both.
tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=0,
    count=1)






frameinfo = getframeinfo(currentframe())

#https://pythonrepo.com/repo/peerchemist-finta-python-finance

pd.options.display.float_format = '{:.2f}'.format
pd.options.display.max_columns=255
pd.options.display.max_rows=6500000

pd.options.display.max_rows=9999
pd.options.display.max_columns=76
pd.set_option("display.max_columns", 200)
pd.set_option('display.width', 1000)
######pd.set_option('display.max_colwidth', 200)
pd.set_option('display.max_columns', 0)
pd.set_option('display.expand_frame_repr', False)

def s5(ss):
    import os, pandas
    import finta as f
    import plotly.graph_objects as go
    import yfinance as yf
    import pandas as pd
    import datetime as dt
    import talib as ta
    import sys
    import warnings
    import inspect
    pd.options.display.float_format = '{:.2f}'.format
    pd.options.display.max_columns=255
    pd.options.display.max_rows=6500000

    pd.options.display.max_rows=9999
    pd.options.display.max_columns=76
    pd.set_option("display.max_columns", 200)
    pd.set_option('display.width', 1000)
    pd.set_option('display.expand_frame_repr', False)

    gg5=[]

    frameinfo = getframeinfo(currentframe())
    warnings.filterwarnings("ignore")

    pd.options.display.float_format = '{:.2f}'.format
    pd.options.display.max_columns=255
    pd.options.display.max_rows=6500000

    pd.options.display.max_rows=9999
    pd.options.display.max_columns=36
    pd.set_option("display.max_columns", 100)
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_colwidth', 200)
    pd.set_option('display.max_columns', 0)
    pd.set_option('display.max_columns', None)

    nasdaq100=['AAPL', 'ADBE', 'ADI', 'ADP', 'ADSK', 'AEP', 'ALGN', 'AMAT', 'AMD', 'AMGN', 'AMZN', 'ANSS', 'ASML',\
               'ATVI', 'AVGO', 'BIDU', 'BIIB', 'BKNG', 'CDNS', 'CDW', 'CERN', 'CHKP', 'CHTR', 'CMCSA', 'COST', 'CPRT',\
               'CSCO', 'CSX', 'CTAS', 'CTSH', 'DLTR', 'DOCU', 'DXCM', 'EA', 'EBAY', 'EXC', 'FAST', 'FB', 'FISV', 'FOX', \
               'FOXA', 'GILD', 'GOOG', 'GOOGL', 'IDXX', 'ILMN', 'INCY', 'INTC', 'INTU', 'ISRG', 'JD', 'KDP', 'KHC', 'KLAC', \
               'LRCX', 'LULU', 'MAR', 'MCHP', 'MDLZ', 'MELI', 'MNST', 'MRNA', 'MRVL', 'MSFT', 'MU', 'NFLX', 'NTES', 'NVDA',\
               'NXPI', 'OKTA', 'ORLY', 'PAYX', 'PCAR', 'PDD', 'PEP', 'PTON', 'PYPL', 'QCOM', 'REGN', 'ROST', 'SBUX', 'SGEN', \
               'SIRI', 'SPLK', 'SWKS', 'TCOM', 'TEAM', 'TMUS', 'TSLA', \
               'TXN', 'VRSK', 'VRSN', 'VRTX', 'WBA', 'WDAY', 'XEL', 'XLNX', 'ZM' ]

    gg6=nasdaq100
    i=0
    gt4=[]
    
    i2=0
    x6=0
    
    for x in gg6: # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
        
        dfqq=pd.DataFrame()
        dfq=pd.DataFrame()
        x5=[]
        print(i, x, gg6[i])
        df=yf.Ticker(gg6[i]).history(period ='4d', interval = '1m',prepost = False)
        df=df.drop(columns=[ 'Dividends', 'Stock Splits'])
        

        df=df[df.index.astype(str).str.contains('2021-12-17')]
        df = df.dropna(axis=0, how='all')
##        print(df)
##        print(df[df['column name'].isnull()])

        df['ticker']=x

        

        df['ATR']=ta.ATR(df['High'],df['Low'],df['Close'], timeperiod=14)
        df['adx']= ta.ADX(df['High'],df['Low'],df['Close'], timeperiod=14)

        df3=df.tail(3)        
        mm=df3['ATR'].mean()
        nn7=df3['adx'].mean()
##        nn=df3['Close'].mean()
##        nn2=df3['Close_EMA3'].mean()
##        nn3=df3['Close_EMA5'].mean()
##        nn4=df3['Close_vwap'].mean()
##        nn5=df3['EMA_3'].mean()
##        nn6=df3['EMA_5'].mean()
        
##############################################################################        
        i=i+1
##        print(x,'no ',i, 'of', len(gg6))

        if mm > 2 and nn7 > 25 :
            gt4.append(x)
            print(i,'  ',x,'---------------------- met -------------------')

    print(gt4)
##    bb(gt4)

         
            
###############################################################################            

def bb(gt4):
    import warnings
    warnings.filterwarnings("ignore")

    
    
    i=0
    for x in gt4:
        i2=0 
        df=yf.Ticker(gt4[i]).history(period ='4d', interval = '1m',prepost = False)
        df=df.drop(columns=[ 'Dividends', 'Stock Splits'])
        

        df=df[df.index.astype(str).str.contains('2021-12-17')]
        df = df.dropna(axis=0, how='all')
##        print(df)
##        print(df[df['column name'].isnull()])
        df['ticker']=x

###############################################################################   
        
        df['TRANGE'] = ta.TRANGE(df['High'],df['Low'],df['Close'])
        df['TR'] = abs(df['High'] - df['Low'])        
        df['EMA_3']=ta.EMA(df['Close'], timeperiod=3)
        df['EMA_5']=ta.EMA(df['Close'], timeperiod=5)
        df['macd'], df['macdsignal'], df['macdhist'] = ta.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
        df['Close_EMA3']=df['Close']-df['EMA_3']
        df['Close_EMA5']=df['Close']-df['EMA_5']                

          
                
        ##        df['Close_vwap']=df['Close']-df['vwap']
        df['EMA-35']=df['EMA_3']-df['EMA_5']
        df['MOM']=ta.MOM(df['Close'], timeperiod=14)
        df['MOM_slope']=df['MOM']-df['MOM'].shift(1)
        df['LINEARREG'] = ta.LINEARREG(df['Close'], timeperiod=14)
        df['LINEARREG_ANGLEG'] = ta.LINEARREG_ANGLE(df['Close'], timeperiod=14)
        df['LINEARREG_INTERCEPT'] =  ta.LINEARREG_INTERCEPT(df['Close'], timeperiod=14)
        df['LINEARREG_SLOPE'] = ta.LINEARREG_SLOPE(df['Close'], timeperiod=14)
        df['TSF'] = ta.TSF(df['Close'], timeperiod=14)
        
        v = df['Volume'].values
        tp = (df['Low'] + df['Close'] + df['High']).div(3).values
        df = df.assign(vwap=(tp * v).cumsum() / v.cumsum())
        
        df['ATR']=ta.ATR(df['High'],df['Low'],df['Close'], timeperiod=14)
        df['TRANGE'] = ta.TRANGE(df['High'],df['Low'],df['Close'])
        df['adx']= ta.ADX(df['High'],df['Low'],df['Close'], timeperiod=14)
        df['TR'] = abs(df['High'] - df['Low'])
        df['EMA_3']=ta.EMA(df['Close'], timeperiod=3)
        df['EMA_5']=ta.EMA(df['Close'], timeperiod=5)
        df['macd'], df['macdsignal'], df['macdhist'] = ta.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
        df['Close_EMA3']=df['Close']-df['EMA_3']
        df['Close_EMA5']=df['Close']-df['EMA_5']
    ##        df['Close_vwap']=df['Close']-df['vwap']
        df['EMA-35']=df['EMA_3']-df['EMA_5']
        df['MOM']=ta.MOM(df['Close'], timeperiod=14)
        df['MOM_slope']=df['MOM']-df['MOM'].shift(1)
        df['LINEARREG'] = ta.LINEARREG(df['Close'], timeperiod=14)
        df['LINEARREG_ANGLEG'] = ta.LINEARREG_ANGLE(df['Close'], timeperiod=14)
        df['LINEARREG_INTERCEPT'] =  ta.LINEARREG_INTERCEPT(df['Close'], timeperiod=14)
        df['LINEARREG_SLOPE'] = ta.LINEARREG_SLOPE(df['Close'], timeperiod=14)
        df['TSF'] = ta.TSF(df['Close'], timeperiod=14)

        df['Boling_upper2']=''
        df['Boling__middle2']=''
        df['Boling_lower2']=''
        df['x']=''
        df['SARx']=''
        df['signal']=''
        df['Red']=''
        df['tail']=''

        df['20sma'] = ''
        df['stddev'] = ''
        df['lower_band'] = ''
        df['upper_band'] = ''

        df['TR'] = ''
        df['ATR'] = ''

        df['lower_keltner'] = ''
        df['upper_keltner'] = ''
        df['vwap_bw_bolinger']=''
        df['EMA50_bw_bolinger']=''

    ##        df['ADX_over25_strong_less25_weak_trend']=''                
        df['Red']=df['Open']-df['Close']
        df['tail']=df['High']-df['Low']
        df['aroondown'],df['aroonup']=ta.AROON(np.asarray(df['High']),np.asarray(df['Low']), timeperiod=14)

        df['CCI']=ta.CCI(df['High'], df['Low'], df['Close'], timeperiod=14)
        df['RSI']= ta.RSI(df['Close'], timeperiod=14)
        df['ATR']=ta.ATR(df['High'],df['Low'],df['Close'], timeperiod=14) 
        df['TR'] = abs(df['High'] - df['Low'])

        df['EMA_3']=ta.EMA(df['Close'], timeperiod=3)
        df['EMA_5']=ta.EMA(df['Close'], timeperiod=5)
        df['EMA_10']=ta.EMA(df['Close'], timeperiod=10)
        df['EMA_50']=ta.EMA(df['Close'], timeperiod=50)
        df['EMA_21']=ta.EMA(df['Close'], timeperiod=21)
        df['EMA_slope']=df['EMA_3']-df['EMA_3'].shift(1)
        df['macd'], df['macdsignal'], df['macdhist'] = ta.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
        df['macd_slope']=df['macd']-df['macd'].shift(1)
        df['adx']= ta.ADX(df['High'],df['Low'],df['Close'], timeperiod=14)
        df['mama'], df['fama'] = ta.MAMA(df['Close'], fastlimit=0.5, slowlimit=0.05)
    ## new ones        
        df['KAMA'] = ta.KAMA(df['Close'], timeperiod=30)
        df['AD'] = ta.ADOSC(df['High'], df['Low'],df['Close'],df['Volume'])
        df['ADOSC'] = ta.ADOSC(df['High'], df['Low'],df['Close'] , df['Volume'], fastperiod=3, slowperiod=10)
        df['DEMA']=ta.DEMA(df['Close'], timeperiod=30)

        df['HT_DCPERIOD'] = ta.HT_DCPERIOD(df['Close'])
        df['HT_DCPHASE'] = ta.HT_DCPHASE(df['Close'])
        df['CMO'] = ta.CMO(df['Close'], timeperiod=14)
        df['KAMA'] = ta.KAMA(df['Close'], timeperiod=30)
        df['PLUS_DI'] = ta.PLUS_DI(df['High'],df['Low'],df['Close'], timeperiod=14)
        df['MINUS_DI'] = ta.MINUS_DI(df['High'],df['Low'],df['Close'], timeperiod=14)
        df['PLUS_DM'] = ta.PLUS_DM(df['High'],df['Low'], timeperiod=14)
        df['MINUS_DM'] = ta.MINUS_DM(df['High'],df['Low'], timeperiod=14)

        df['EMA-35']=df['EMA_3']-df['EMA_5']
        df['EMA-510']=df['EMA_5']-df['EMA_10']
        df['EMA-1021']=df['EMA_10']-df['EMA_21']
        df['EMA-2150']=df['EMA_21']-df['EMA_50']
        df['EMA_3_vwap']=df['EMA_3']-df['vwap']
        df['EMA_5_vwap']=df['EMA_5']-df['vwap']
        df['EMA_10_vwap']=df['EMA_10']-df['vwap']
        df['EMA_21_vwap']=df['EMA_21']-df['vwap']
        df['EMA_50_vwap']=df['EMA_50']-df['vwap']
        df['macd_35'], df['macdsignal'], df['macdhist'] = ta.MACD(df['Close'], fastperiod=3, slowperiod=5, signalperiod=3)
        df['Close_EMA3']=df['Close']-df['EMA_3']
        df['Close_EMA5']=df['Close']-df['EMA_5']
        df['Close_EMA10']=df['Close']-df['EMA_10']
        df['Close_EMA21']=df['Close']-df['EMA_21']
        df['Close_EMA50']=df['Close']-df['EMA_50']
        df['Close_vwap']=df['Close']-df['vwap']
        


        df['fastk'], df['fastd'] = ta.STOCHRSI(df['Close'], timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
        df['MA'] = ta.EMA(df['fastd'], timeperiod=14)
        df['MA2'] = ta.EMA(df['fastk'], timeperiod=14)
    #original        df['SAR'] = ta.SAR(df['High'], df['Low'], acceleration=90, maximum=5)
        df['SAR'] = ta.SAR(df['High'], df['Low'], acceleration=300, maximum=5)
        df['Boling_upper'], df['Boling__middle'], df['Boling_lower'] = ta.BBANDS(df['High'], timeperiod=20, nbdevup=2, nbdevdn=2)
        df['Boling_upper2'], df['Boling__middle2'], df['Boling_lower2'] = ta.BBANDS(df['Low'], timeperiod=20, nbdevup=2, nbdevdn=2)
        df['SARx']=df['Close']-df['SAR']
        df['ADX_over25_strong_less25_weak_trend']=ta.ADX(df['High'], df['Low'], df['Close'], timeperiod=3).round(2)
        df['ticker']=x

        df['bolinger_width']=df['Boling_upper2']-df['Boling_lower2']
        
    ########################## squeeze ####################################
        df['20sma'] = df['Close'].rolling(window=20).mean()
        df['stddev'] = df['Close'].rolling(window=20).std()
        df['lower_band'] = df['20sma'] - (2 * df['stddev'])
        df['upper_band'] = df['20sma'] + (2 * df['stddev'])

        df['TR'] = abs(df['High'] - df['Low'])
        df['ATR'] = df['TR'].rolling(window=20).mean()

        df['lower_keltner'] = df['20sma'] - (df['ATR'] * 1.5)
        df['upper_keltner'] = df['20sma'] + (df['ATR'] * 1.5)
    ##        df=df[['ticker','Open', 'High', 'Low', 'Close', 'Volume', 'lower_band','upper_band','upper_keltner','lower_keltner']]
    ##    print(df)

    ##    def in_squeeze(df):
    ##        return df['lower_band'] > df['lower_keltner'] and df['upper_band'] < df['upper_keltner']

##        print(df,'kk55',x)
       
        df['squeeze_on'] =''
        df['cross']=''
        df['mama_fama']=''
        df['DM_delta']=''
        df['DI_delta']=''
        df['open_close']=''
        df['DM_delta']=df['PLUS_DM']-df['MINUS_DM'] 
        df['DI_delta']=df['PLUS_DI']-df['MINUS_DI']

        i=i+1

        p=0
        profit=0



    ###############################################################################                                                             

##        print(df,'kkkkkkkkk',x)

        for z in df.index:
            


            if  df['Boling_lower2'].loc[z] < df['vwap'].loc[z] <  df['Boling_upper2'].loc[z]:
                df['vwap_bw_bolinger'].loc[z]='vwap_inside_bolinger'
            elif df['vwap'].loc[z] > df['Boling_upper2'].loc[z]:
                df['vwap_bw_bolinger'].loc[z]='VWAP > upper_bolinger'
            elif df['Boling_lower2'].loc[z] < df['vwap'].loc[z]:
                df['vwap_bw_bolinger'].loc[z]='VWAP < lower_bolinger'

            if  df['Boling_lower2'].loc[z] < df['EMA_50'].loc[z] <  df['Boling_upper2'].loc[z]:
                df['EMA50_bw_bolinger'].loc[z]='EMA50_inside_Bolinger'
            elif df['EMA_50'].loc[z] >  df['Boling_upper2'].loc[z]:
                df['EMA50_bw_bolinger'].loc[z]='EMA50 > upper_Bolinger'
            elif df['EMA_50'].loc[z] < df['Boling_lower2'].loc[z]:
                df['EMA50_bw_bolinger'].loc[z]='EMA50 < lower_Bolinger'

  
            
            if df['Red'].loc[z]>0:
                df['Red'].loc[z]='Green'
            elif df['Red'].loc[z]<0:
                df['Red'].loc[z]='Red'
            if df['mama'].loc[z] > df['fama'].loc[z]:
                df['mama_fama'].loc[z]='up'
            elif df['mama'].loc[z] < df['fama'].loc[z]:
                df['mama_fama'].loc[z]='down'


            
            if df['lower_band'].loc[z] > df['lower_keltner'].loc[z]:
                df['squeeze_on'].loc[z]='in_squeeze_upper'
            elif df['upper_band'].loc[z] < df['upper_keltner'].loc[z]:
                df['squeeze_on'].loc[z]='in_squeeze_lower'
            elif df['lower_band'].loc[z] > df['lower_keltner'].loc[z] and df['upper_band'].loc[z] < df['upper_keltner'].loc[z]:
                df['squeeze_on'].loc[z]='in_squeeze_BOTH'
            else:
                df['squeeze_on'].loc[z]='NO_squeeze_BOTH'
           
                
            p=p+1


            if df['EMA-35'].loc[z] > 0:
                df['cross'].loc[z]='up'+str(df['macd'].loc[z])
            elif df['EMA-35'].loc[z] < 0:
                df['cross'].loc[z]='down'+str(df['macd'].loc[z])  
               
                
    ##
    ##        if p > 0:
    ##            print(x,' Squeeze Alert','  ','lineno',  inspect.getframeinfo(inspect.currentframe()).lineno)
    ##      


        print(df,'flight 202 bb/def bb ',x,'\n\n\n')
        cc(df)
    ###############################################################################

def cc(df):

        df_short=pd.DataFrame()
        df4=pd.DataFrame()
        df5=pd.DataFrame()
    ##            df3=df
        g6=pd.DataFrame()
        g7=pd.DataFrame()
        
            ##        SAR reversal
        df.reset_index(inplace=True)            
        m2=[];m3=[];m4=[]

##        print(df.index,'ddddddddddddddddddd')

########################## buy condition ######################################        
##        print(df.index,'kkkkkkkkkkkkkkkkkkkkkkkkkkk')
        for z in df.index:
               
            buy_condition=df['MOM'].loc[z]-df['MOM'].shift(1).loc[z] > 0 and df['macd'].loc[z]>0 and df['adx'].loc[z]>24 and df['ATR'].loc[z]>.9\
                     and df['TR'].loc[z]>.5   

                
            if buy_condition:
##                print("kkkkkkkkkkkdddddd",len(df.index))
                ss.append(z)
##                print('line no ',z,'buy cond')
                v5=df['Close'].loc[z] #v5 is buy
                v6=df['CCI'].loc[z]
                t_buy=df['Datetime'].loc[z]
                v8=df['ticker'].loc[z]
##                print(v5,'          ',v6)
                g43=z
##                print("------------------",z,'  ',df.shape)
##                    print(i2,'  ',x,'  ',z, '----appended',round(df['MOM'].loc[z]-df['MOM'].shift(1).loc[z],2),'  ',\
##                             round(df['macd'].loc[z],2),'  ',round(df['ATR'].loc[z],2),'   ',round(df['TR'].loc[z],2))
##                print('buy condition')

                ##                    if uu3:
##                    t_buy=df['Datetime'].loc[z]
##                    df['signal'].loc[z]='buymmmmmmmmmmm'
##                    
##                    v5=df['Close'].loc[z] #v5 is buy
##                    v6=df['CCI'].loc[z]
                i2='51'
############################################################################################                    
######################## SELL CONDITION ####################################################
                i=0
                mm3='MOM'

                for z in range(g43,len(df.index)):
                    sell_condition=(df[mm3].loc[z] < 0 and (df[mm3].loc[z]-df[mm3].shift(1).loc[z] <00) and df['Close'].loc[z] > v5 )
                    
                    if sell_condition:
##                        print(' sell cond')
                        
                        
                        
##                    sell_condition=df[mm3].loc[z] < 0
                    
                        t_sell=df['Datetime'].loc[z]
                        v4=df['Close'].loc[z]
                        v7=df['ticker'].loc[z]
##                        print(v7,'  ',v4,'/',v5,'  ',v4-v5,'  ',t_sell,'/',t_buy)
                        xm=v7
                        x2=v5
                        x3=v4
                        x5=v6
                        x4=v4-v5
                        
                        g6=g6.append([[xm,v5,v4,x4,v7,t_buy,t_sell]])
                        
                        i=i+1
##                    else:
##                        v7=df['ticker'].loc[z]
##                        t_sell=df['Datetime'].loc[z]
##                        v4=df['Close'].loc[z]
##                        xm=v7
##                        x2=v5
##                        x3=v4
##                        x5=v6
##                        x4=v4-v5
##                        print(v8,'  ','Loss','/',v5,'  ','Loss','  ','Loss''/',t_buy)
##                        g6=g6.append([[xm,v5,v4,x4,v7,t_buy,t_sell]])
##                        
##
        g6.drop_duplicates(subset=None, keep='last', inplace=True)                
        print(g6)
                        
##                    print(z,' ---------------------------------')


##                print('\n\n\n')
##
##                print('Sell--> ',v5,'\n','     Buy--> ',v4,'\n','    CCI--> ',v6,'\n','  sell-->',t_sell,'\n',' buy-->',t_buy,'\n',)
##
##                print(v5, '  v5  ',type(v5),
##                      v4, '  v4  ',type(v4),
##                      (v4-v5),' v4-v5 ',type(v4-v5),
##                      v6,'  v6  ',type(v6),
##                      t_sell,' t_sell ', type(t_sell),
##                      t_buy,' t_buy ',type(t_buy))


##                        profit=(v4-v5)
##                        t2_buy=pd.Series(str(t_buy))
##                        t2_sell=pd.Series(str(t_sell))
##                        xm=pd.Series(v7)
##                        x2=pd.Series(v5.round(2))  # buy
##                        x3=pd.Series(v4.round(2))  # sell
##                        x4=pd.Series(profit.round(2))
##                        x5=pd.Series(v6.round(2))  #CCI
##
##
##                        g6=g6.append([xm,x2,x3,x4,x5,t2_buy,t2_sell])
####                        g6=pd.concat([xm,x2,x3,x4,x5,t2_buy,t2_sell],axis=1)
##                        g7a=g6




##                        
##        print(g7a,x+' nnnnn')        
##
##                        g7=g7.append(g7a,ignore_index=True)
##                        print(g7)
    ##

                
##                df_short2=pd.concat([v5,v4,(v4-v5),v6,t_sell,t_buy],axis=0)
##               
##
##
##        print(df_short,'\n','pppp')        
##                    if i > 2:
##                        break
'''                    
                    if i2=='51':
                                      
                        mm3='MOM'                   
        ##                sell_condition=(df[mm3].loc[z] < 0 and (df[mm3].loc[z]-df[mm3].shift(1).loc[z] <00)\
        ##                  and df['Close'].loc[z] > v5 )  # original

                        sell_condition=df['macd'].loc[z] < 0 
                        
                         
                        if sell_condition:
                            ss.append(z)
                            t_sell=df['Datetime'].loc[z]
                            v4=df['Close'].loc[z]
                               # v4 is sell
                            print(v4,'  ',type(v4))

                        else:
                            print("Loss",'  ',v5,'   ',v4)
                        
                        
                        print('sell condition','  ',profit)
                        i2='53'

###########################################################################################3             
                  


    ## azhar adding stuff:
                
##                if i2 == '53':
                   
                    



        ######################################################################################################################################
##
##                if i2 is '51':
##                    print("inside sell")
##               
                    
                 
                                                            
                    # Sell condition

    ##                sellk=df['MOM_slope'].loc[x] > -.6 and df['CCI'].loc[x] > -50

    #####################################################################################################
    ## ***************************************************************************************************
    ## ***************************************************************************************************
    ## ***************************************************************************************************
    ## ***************************************************************************************************                
                    #sell condition
    ##                sell2=df['Close'].loc[x]<v5 and\
    ##                      df['EMA_10'].loc[x] < df['EMA_21'].loc[x] and\
    ##                      df['MOM'].loc[x] < df['MOM'].shift(1).loc[x] and\
    ##                      df['Low'].loc[x] < df['Low'].shift(1).loc[x]

                           

    ##                sell=df['MOM'].loc[x]<df['MOM'].shift(1).loc[x]-.3
                    #orig
    ##                    sell=(df['MOM'].loc[x] >0 and (df['MOM'].loc[x]-df['MOM'].shift(1).loc[x] <00) and df['Close'].loc[x]>v5)   #Algo 2.2s (orig) MOM based



                mm3='MOM'   
                sell=(df[mm3].loc[z] < 0 and (df[mm3].loc[z]-df[mm3].shift(1).loc[z] <00)\
                          and df['Close'].loc[z] > v5 )  # original
                print("inside sell")
                    

    ##                    sell= df['Close_EMA50'].loc[x] > df['Close'].loc[x]  #fail and df['Close'].loc[x] < df['Close_EMA50'].loc[x]

                    #Algo 2.3s  Macd based

    ##                df['macd'].loc[x]<0 and df['macd'].shift(1).loc[x]>0 and\
    ##                      df['Close'].loc[x]<v5

    ##                df['EMA-35'].loc[x] <0 and\
    ##                 df['EMA-35'].shift(1).loc[x]>0 and df['EMA-35'].shift(2).loc[x]>0 and df['EMA-35'].shift(3).loc[x]>0
    ##                and\
    ##                 df['macd'].loc[x]<0 and\
    ##                 df['macd'].shift(1).loc[x]>0 and df['macd'].shift(2).loc[x]>0 and df['macd'].shift(3).loc[x]>0


                
    ## ***************************************************************************************************
    ## ***************************************************************************************************
    ## ***************************************************************************************************
    ## ***************************************************************************************************  
                    
                k=0 
                if sell:
                    print("jjjjjjjjjjjjjjjjjjjjjjjj")

    ##                        print('\n\n')
                    print('**************************************************************************************************************')


    ##                        print(df3.columns)


    ##                        print(df3,'\n',df3.iloc[-1,1],'  ','[df3] buy signal condition met @',v5,'   line no:', inspect.getframeinfo(inspect.currentframe()).lineno)
    ##                        print('\n\n')
    ##                        print(df3.columns)
    ##                        print(df,'\n',df.iloc[-1,1],'   ','[df] buy signal condition met @',v5,'  line no:', inspect.getframeinfo(inspect.currentframe()).lineno)
                    df['signal'].loc[z]='selllllllllllllllll'
                    dfqq=dfqq.append(df3)

      
                    k=k+1
                    t_sell=df['Datetime'].loc[z]

    ##                    df['signal'].loc[x]=="sellmjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj"
                        
    ##                        print('\n\n')
                    i2='53'
                 
                    v4=df['Close'].loc[z]   # v4 is sell

                    print('kkkkk888888',v4,'    ',v5)

                       












                        df =df[['Datetime','ticker',
                                    
                                'Open', 
                                'High', 
                                'Low', 
                                'Close', 
                                'Volume', 
                                'Red', 
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
                                'signal', 
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
                                'macd', 
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
                        df = df.loc[:,~df.columns.duplicated()]

                  
                        df_buy=df[['signal','Close','MOM','macd','adx','ATR','TR','Close_vwap','ticker','Datetime','ticker',\
                                     'macd', 
                                'macdsignal', 
                                'macdhist',
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
                                'Close_vwap'
                                     ]]

                        print(df_buy,'\n','buy_condition','\n\n', 'lineno', inspect.getframeinfo(inspect.currentframe()).lineno)
                        print('***',df.iloc[-1,1],df,'\n','   ',\
                              'df sell signal condition met @',v4,'    ','buy signal condition met @',
                              v5,

                              '\n',df.shape,'     line no:', 'lineno', inspect.getframeinfo(inspect.currentframe()).lineno)


    ##                        print('**************************************************************************************************************','\n')





    ##
    ##                        print('\n\n')
    ##
    ##                        print('*****************************',df.iloc[-1,1],' Profit/Loss summary **************************\
    ##                              ********************************','\n')
    ##                        print('\n')


                        profit=(v4-v5)
                        if profit < 0:
    ##                            print('5555555*',df[-1,:],'if profit <0')
                            print('\n',df.iloc[-1,1],'-------Last tranacation was a loss-------------',\
                                  profit,'  ','lineno', inspect.getframeinfo(inspect.currentframe()).lineno)
                        elif profit > 0:
    ##                            print('66666*',df[-1,:],'if profit > 0')
                            print('\n',df.iloc[-1,1],'---------Last tranacation was a Profit-------------',profit,'  ','lineno',  inspect.getframeinfo(inspect.currentframe()).lineno)
                            
    ##                        print(df3,'\n',df.iloc[-1,1] ,'sell signal condition met','  ', inspect.getframeinfo(inspect.currentframe()).lineno)
    ##                        print('\n')
    ##                        print(df,'\n',df.iloc[-1,1],'sell sell signal condition met','  ', inspect.getframeinfo(inspect.currentframe()).lineno)

                        
        ##                print(df['ticker'].loc[x],v4.round(2),v5.round(2),' profit-----> ',profit.round(2))
        ##                pp=pp.append(df['ticker'].loc[x],v4.round(2),v5.round(2),profit.round(2))

                        t2_buy=pd.Series(str(t_buy))
                        t2_sell=pd.Series(str(t_sell))
                        xm=pd.Series(str(df['ticker'].loc[x]))
                        x2=pd.Series(v5.round(2))  # buy
                        x3=pd.Series(v4.round(2))  # sell
                        x4=pd.Series(profit.round(2))
                        x5=pd.Series(v6.round(2))  #CCI

                        g6=pd.concat([xm,x2,x3,x4,x5,t2_buy,t2_sell],axis=1)
                        g7a=g6
                        

                        g7=g7.append(g7a,ignore_index=True)

                    
    ################n############################################################

            print(g7)




            if g7.shape[0] < 1:
                print("Exit")
                sys.exit()
                
            b=g7
            tickers_not_meeting_buy_criteria=[]
    ##        if b.shape[0]>1:
    ##            b.sort_values(by=[3])
            if b.shape[0]>0:
                print('\n','**************************************************************************************************************','\n')

                df4=df4.append(b)
    ##                print(df4.iloc[-1,1],df4,'  ', inspect.getframeinfo(inspect.currentframe()).lineno)
                
                dfq=dfq.append(df4)

                
    ##                print('  dfq concat', inspect.getframeinfo(inspect.currentframe()).lineno)
    ##                print('\n','Profit on',df4.iloc[0,0],': ',df4.iloc[:,3].sum(),'  ', inspect.getframeinfo(inspect.currentframe()).lineno)
    ##                print('\n','Min Profit on',df4.iloc[0,0],': ',df4.iloc[:,3].min(),'  ', inspect.getframeinfo(inspect.currentframe()).lineno)
    ##                print('\n','Max Profit on',df4.iloc[0,0],': ',df4.iloc[:,3].max(),'  ', inspect.getframeinfo(inspect.currentframe()).lineno)
                x6=x6+df4.iloc[:,3].sum()
                print(df4.iloc[0,0],'  ',x6,'<<<< Total Profit >>>>>','  ','lineno', inspect.getframeinfo(inspect.currentframe()).lineno)
    ##            df4=df4.append(b.iloc[:,[0,1,2,3,4,5,6]],ignore_index=True)
                print(df4.iloc[-1,1],'ppppppppppppppppppppppppppppppppp')
    ##            print(b)
                print('\n')
            elif b.shape[0] < 1:
                tickers_not_meeting_buy_criteria.append(x)


    ##            print(')))))))))))))))))))))))))))','\n',df4,'\n','df4','\n',inspect.getframeinfo(inspect.currentframe()).lineno)
    ##            print(df4.columns)
    ##            print(df4.get_loc('ticker'))
    ##            sys.exit()
            print('\n\n')
            gg5.append(df4.iloc[-1,1])
    ##            return(df4.iloc[-1,1])


            
    ##
    ##        else:
    ##            pass
    ##



    ##    dfqq =dfqq[['ticker','Open', 'High', 'Low', 'Close', 'Volume', 'vwap', 'ATR', 'TRANGE','TR', 'adx',
    ##               'MOM', 'MOM_slope', 'Boling_upper2', 'Boling__middle2', 'Boling_lower2', 'x',
    ##               'SAR','SARx', 'signal', 'Red', 'tail', '20sma', 'stddev', 'lower_band',
    ##               'upper_band', 'lower_keltner', 'upper_keltner','vwap_bw_bolinger',
    ##               'EMA50_bw_bolinger','bolinger_width','squeeze_on',
    ##               'aroondown', 'aroonup', 'CCI', 'RSI',
    ####               'EMA_3', 'EMA_5', 'EMA_10', 'EMA_50', 'EMA_21', 
    ##               'EMA_slope',
    ##               'fastk', 'fastd','MA', 'MA2',
    ##               'macd_slope', 'mama', 'fama', 'KAMA', 'AD', 'ADOSC', 'DEMA', 'HT_DCPERIOD', 'HT_DCPHASE', 'CMO', 'PLUS_DI', 'MINUS_DI', 'PLUS_DM', 'MINUS_DM',
    ##               'macd', 'macdsignal', 'macdhist',
    ##               'EMA-35','EMA-510', 'EMA-1021', 'EMA-2150',
    ##               'EMA_3_vwap', 'EMA_5_vwap', 'EMA_10_vwap', 'EMA_21_vwap', 'EMA_50_vwap',
    ##               'Close_EMA3', 'Close_EMA5','Close_EMA10', 'Close_EMA21', 'Close_EMA50',
    ##               'Close_vwap',
    ##               'LINEARREG','LINEARREG_ANGLEG','LINEARREG_INTERCEPT','LINEARREG_SLOPE','TSF', 'cross',
    ##               'mama_fama', 'DM_delta', 'DI_delta','mama',
    ##                   'fama', 'KAMA', 'AD', 'ADOSC', 'DEMA', 'HT_DCPERIOD' ]]







        dfqq =dfqq[['ticker',
                    
                'Open', 
                'High', 
                'Low', 
                'Close', 
                'Volume', 
                'Red', 
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
                'signal', 
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
                'macd', 
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

        dfqq.drop_duplicates(subset=None, keep='last', inplace=True)
        ##    print(dfqq.columns,'dddddd','  ','\n', inspect.getframeinfo(inspect.currentframe()).lineno)
        ##
        ##    print(dfqq.columns,'after','  ','\n', inspect.getframeinfo(inspect.currentframe()).lineno)





        print(dfqq,'\n',' dfqq ','lineno', inspect.getframeinfo(inspect.currentframe()).lineno)
        ##    print('\n',dfqq.columns,'\n')
        print('\n\n')
        print(dfq,'\n','dfq ','lineno', inspect.getframeinfo(inspect.currentframe()).lineno)

        print('\n\n')
        print('************************ Profit ***********************************')
        print(df4,'\n','Profit=',x6)
        print('\n\n')
        ##    for c in dfqq.columns:
        ##        print("'"+str(c)+"', ")

        ##    return(gg5)
        ##        print('\n')
        ##        print('===================================== Total profit:' , x6,' =============================================')
        ##        print('\n')
        ##    ##    print(x5)
        ##        
        ##        
        ##        print('tickers that did not meet buy criteria:')
        ##        print(len(tickers_not_meeting_buy_criteria),'    ',tickers_not_meeting_buy_criteria)        
        ##    df5=df5.append(df4)
            

                    
    
          
'''
#######################################################################################################################3

         

gt4=['GOOGL', 'TSLA']   
ss=[]
##s5(ss)
bb(gt4)
### run the new command using the given tracer
##tracer.run('s4()')
##
### make a report, placing output in the current directory
##r = tracer.results()
##r.write_results(show_missing=True, coverdir="/home/az2/")

print(__file__,'  ','lineno', inspect.getframeinfo(inspect.currentframe()).lineno)
##print(gg5)
print('\n\n\n')
print('***************************************************************************')
print('this is coming from bottom/main','\n')
##b=columns['purchase_price','Sell_price','Profot']





