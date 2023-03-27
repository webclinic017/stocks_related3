import talib as ta
from ta.utils import dropna
import yfinance as yf
from yahoo_fin import stock_info as f
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


def most_active():

        active=pd.DataFrame(f.get_day_most_active())
        losers=pd.DataFrame(f.get_day_losers())
        gainers=pd.DataFrame(f.get_day_gainers())

        ##active.sort_values(by='Volume',ascending=False,inplace=True)
        ##losers.sort_values(by='Volume',ascending=False,inplace=True)
        ##gainers.sort_values(by='Volume',ascending=False,inplace=True)
        ##
        
        active=active[active['Volume'] >= 3000000]
        losers=losers[active['Volume']>3000000]
        gainers=gainers[active['Volume']>3000000]

        for x in active.index:
                active['Volume'].loc[x]=numerize.numerize(np.float32(active['Volume'].loc[x]).item())
                active['Avg Vol (3 month)'].loc[x]=numerize.numerize(np.float32(active['Avg Vol (3 month)'].loc[x]).item())

        for x in losers.index:
                losers['Volume'].loc[x]=numerize.numerize(np.float32(losers['Volume'].loc[x]).item())
                losers['Avg Vol (3 month)'].loc[x]=numerize.numerize(np.float32(losers['Avg Vol (3 month)'].loc[x]).item())
        for x in gainers.index:
                gainers['Volume'].loc[x]=numerize.numerize(np.float32(gainers['Volume'].loc[x]).item())
                gainers['Avg Vol (3 month)'].loc[x]=numerize.numerize(np.float32(gainers['Avg Vol (3 month)'].loc[x]).item())

                


        active.sort_values(by='Change',ascending=True,inplace=True)
        losers.sort_values(by='Change',ascending=True,inplace=True)
        gainers.sort_values(by='Change',ascending=False,inplace=True)



        print(active,'---------->','most active')
        print(losers,'---------->','most losers')
        print(gainers,'---------->','most gaiers')


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
    df['MOM_Prev']=''
    df['adx_Prev']=''
    
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

    df['5>10']=df['EMA_5s']-df['EMA_10s']
    df['10>21']=df['EMA_10s']-df['EMA_21s']
    df['21>50']=df['EMA_21s']-df['EMA_50s']
    df['50>100']=df['EMA_50s']-df['EMA_100s']
    df['Close>5']=df['Close']-df['EMA_5s']
    df['Close>10']=df['Close']-df['EMA_10s']
    df['Close>21']=df['Close']-df['EMA_21s']
    df['Close>50']=df['Close']-df['EMA_50s']
    df['Close>100']=df['Close']-df['EMA_100s']
    df['Close>200']=df['Close']-df['EMA_200s']
    df['Close>vwap']=df['Close']-df['vwap']
    df['5>vwap']=df['EMA_5s']-df['vwap']
    df['10>vwap']=df['EMA_10s']-df['vwap']
    df['21>vwap']=df['EMA_21s']-df['vwap']
    df['50>vwap']=df['EMA_50s']-df['vwap']
    df['100>vwap']=df['EMA_100s']-df['vwap']
    df['200>vwap']=df['EMA_200s']-df['vwap']
    df['MOM_Prev']=df['MOM'].shift(1)
    df['adx_Prev']=df['adx'].shift(1)

##    df['MOM_slope']=df['MOM']-df['MOM'].shift(1)
##        print(df['BB_upperband'], df['BB_middleband'], df['BB_lowerband'])
    
##    print(df['Close_UpBol'],'  ',df['Close_LowBol'],'  ',df['Close_MidBol'])
##    sys.exit()
    #######################################################################
    ### squeeze
    df['20sma'] = df['Close'].rolling(window=20).mean()
    df['stddev'] = df['Close'].rolling(window=20).std()
    df['lower_band'] = df['20sma'] - (2 * df['stddev'])
    df['upper_band'] = df['20sma'] + (2 * df['stddev'])

    df['TR'] = abs(df['High'] - df['Low'])
    df['ATR'] = df['TR'].rolling(window=20).mean()

    df['lower_keltner'] = df['20sma'] - (df['ATR'] * 1.5)
    df['upper_keltner'] = df['20sma'] + (df['ATR'] * 1.5)
    df['squeeze_on']=''
    df['MOM_slope']=''
    df['Red']=''
    df['Red']=df['Close']-df['Open']
    df['Redby']=''

    df['Close_UpBol']=''
    df['Close_LowBol']=''
    df['Close_MidBol']=''
    df['ATRa_prev']=''

    
    for z in df.index:
        df['Close_UpBol'].loc[z]=df['Close'].loc[z]-df['BB_upperband'].loc[z]
        df['Close_LowBol'].loc[z]=df['Close'].loc[z]-df['BB_lowerband'].loc[z]
        df['Close_MidBol'].loc[z]=df['Close'].loc[z]-df['BB_middleband'].loc[z]

        
        if df['Close'].loc[z]-df['Open'].loc[z] > 0:
            df['Redby'].loc[z]='Green'
        elif df['Close'].loc[z]-df['Open'].loc[z] < 0:
            df['Redby'].loc[z]='Red'
            
            
        df['pp'].loc[z]=df['HL'].loc[z]-df['ATRa'].loc[z]
        df['MOM_slope'].loc[z]=df['MOM'].loc[z]-df['MOM'].shift(1).loc[z]
##        if df['lower_band'].loc[z] > df['lower_keltner'].loc[z] and df['upper_band'].loc[z] < df['upper_keltner'].loc[z]:
##            df['squeeze_on'].loc[z]='in_squeeze'
##        else:
##            df['squeeze_on'].loc[z]='no'

    df['Close_Up_kelt']=''
    df['Close_Low_kelt']=''
    df['MOM_slope_Prev']=''
    df['CCI_Prev']=''
    df['RSI_Prev']=''
    df['Red_Prev']=''
    df['Close>vwap_Prev']=''
    df['Close>21_Prev']=''
    df['5>10_Prev']=''
    df['10>21_Prev']=''
    df['21>50_Prev']=''
    df['50>100_Prev']=''
    df['Close_UpBol_Prev']=''
    df['Close_MidBol_Prev']=''
    df['Close>5_Prev']=''
    df['Close>10_Prev']=''
    df['Close>21_Prev']=''
    df['Close>50_Prev']=''
    df['Close>100_Prev']=''    
       



##    
    #################################################################
    ##print(df,'\n','pppppp')
    df['Close_Up_kelt']=df['Close']- df['upper_keltner']
    df['Close_Low_kelt']=df['Close']-df['lower_keltner']
    df['ATRa_prev']=df['ATRa'].shift(1)
    df['MOM_slope_Prev']=df['MOM_slope'].shift(1)
    df['CCI_Prev']=df['CCI'].shift(1)
    df['RSI_Prev']=df['RSI'].shift(1)
    df['Red_Prev']=df['Red'].shift(1)
    df['Close>vwap_Prev']=df['Close>vwap'].shift(1)
    df['Close>21_Prev']=df['Close>21'].shift(1)
    df['5>10_Prev']=df['5>10'].shift(1)
    df['10>21_Prev']=df['10>21'].shift(1)
    df['21>50_Prev']=df['21>50'].shift(1)
    df['50>100_Prev']=df['50>100'].shift(1)
    df['Close_UpBol_Prev']=df['Close_UpBol'].shift(1)
    df['Close_MidBol_Prev']=df['Close_MidBol'].shift(1)
    df['Close>5_Prev']=df['Close>5'].shift(1)
    df['Close>10_Prev']=df['Close>10'].shift(1)
    df['Close>21_Prev']=df['Close>21'].shift(1)
    df['Close>50_Prev']=df['Close>50'].shift(1)
    df['Close>100_Prev']=df['Close>100'].shift(1)    
 
    
            
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
           'Close_UpBol','Close_LowBol','Close_MidBol','Close_Up_kelt','Close_Low_kelt','Redby','Red','lower_keltner','upper_keltner',
           'BB_upperband', 'BB_middleband', 'BB_lowerband','MOM_Prev','adx_Prev','ATRa_prev','MOM_slope_Prev',
           'CCI_Prev','RSI_Prev','Red_Prev','Close>vwap_Prev','Close>21_Prev',
           '5>10_Prev', '10>21_Prev', '21>50_Prev', '50>100_Prev','Close_UpBol_Prev','Close_MidBol_Prev',

           ]]




  
    
##    df['Bol_dist']=min((df['Close_UpBol'],(df['Close_LowBol']),(df['Close_MidBol'])))
##    df['Close_UpBol'] = df['Close_UpBol'].fillna(0)
##    df['Close_LowBol'] = df['Close_LowBol'].fillna(0)
##    df['Close_MidBol'] = df['Close_MidBol'].fillna(0)

    
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
##        print(df['Close_UpBol'].loc[x])
##
##        if str(df['Close_UpBol'].loc[x]) != None or str(df['Close_LowBol'].loc[x]) != None or df['Close_MidBol'].loc[x]!=None:
##            dd=[int(df['Close_UpBol'].loc[x]),int(df['Close_LowBol'].loc[x]),int(df['Close_MidBol'].loc[x])]
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
           'Close_UpBol','Close_LowBol','Close_MidBol','Close_Up_kelt','Close_Low_kelt',
           'macd','macdsignal','macdhist','Redby','Red','lower_keltner','upper_keltner',
            'BB_upperband', 'BB_middleband', 'BB_lowerband','MOM_Prev','adx_Prev','ATRa_prev','MOM_slope_Prev',
           'CCI_Prev','RSI_Prev','Red_Prev','Close>vwap_Prev','Close>21_Prev',
           '5>10_Prev', '10>21_Prev', '21>50_Prev', '50>100_Prev','Close_UpBol_Prev','Close_MidBol_Prev'
           
           ]]

##################################################################################################
##    df=df[df['adx'] > 25 & df['STOCHRSI_fastk'] > 99 & df['Date'] == '2021-12-02']
##    df=df[df['adx'] > 25 & df['STOCHRSI_fastk'] > 99]
##    df=df.tail(1)
    df=df.iloc[-1]
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


def alert55():
        
        uu=['vg','astr','ispc','mpln','nbev','avya','cei','nvts','now','snow','amc','aapl','f','asml','zm',
            'tsla','nio','plug','lcid','rivn','fsr','blnk','mrna','bntx','nvax','bntx','isrg','biib','pfe','abt',
            'qcom','nvda','avgo','qrvo','gfs','tsm',
            'adbe','gme','nvda','nflx','asml','mu','avgo','amd','asml','qcom','mrvl','txn','intc','dltr','penn','coin','mstr','uber','lyft','z',
            '^ndx','RSX','AUPH','BHP', 'DUST', 'EWY', 'NYCB', 'QID', 'SQQQ', 'SVRA', 'AEP',
            'BHP', 'DUST', 'EWY', 'NYCB', 'QID', 'SQQQ', 'SVRA', 'AEP',
            'bby','zm','dks','anf','docu','dltr','xpev','arkk','^ndx','^gspc','^dji','spy','tna','qqq','tsla','^dji','pfe','f','intc','spy']


        mc=['AA','ABR','AEG','AEO','AEVA','AG','AGI','AGL','AGNC','AI','ALIT','ALK','AM','AMRS','ANGI','APA',
            'APLE','APPS','AQN','AR','ARCC','ARMK','ARRY','ARVL','ASO','ASTR','ATUS','AU','AUPH','AUY','BB','BBBY',
            'BCRX','BE','BHC','BHG','BIGC','BIRD','BLDP','BOX','BRFS','BROS','BRX','BSIG','BTG','BWXT','BXMT','BYD',
            'BYND','CCJ','CD','CEF','CFX','CGC','CHGG','CHK','CHPT','CIEN','CIG','CIM','CLOV','CNX','COLD','COMM',
            'COMP','COR','CORT','COTY','CPE','CPG','CPRI','CRK','CVA','CX','CXP','DBRG','DBX','DDD','DM','DNB','DNUT'
            ,'DOC','DQ','DRNA','DXC','EDU','EGHT','ELY','ENLC','EQT','EQX','ERF','ERJ','ETRN','ETWO','FCEL','FHN',
            'FIGS','FIVN','FL','FLEX','FLR','FNB','FOUR','FSK','FSLY','FSR','FTI','FUBO','FUTU','GFI','GGB','GOEV',
            'GOOS','GPK','GPS','GSAT','GT','HBI','HFC','HIPO','HL','HMY','HP','HRB','HTA','HUN','HUT','HXL','IBRX',
            'IGT','IONQ','IQ','IS','JBLU','JOBY','JWN','KC','KD','KGC','KIND','KSS','LAC','LAZR','LC','LMND','LPSN',
            'LTHM','LW','LXP','LZ','M','MAC','MARA','MAT','MBT','MCFE','MDRX','ME','MGNI','MGY','MLCO','MNDT','MOMO',
            'MP','MPLN','MTDR','MTG','MTTR','MUR','NAVI','NCLH','NCNO','NI','NKLA','NLSN','NOV','NOVA','NRG','NRZ',
            'NTCO','NVTA','NWL','NYCB','OGN','OHI','OLLI','OLN','OMF','ONEM','OPK','ORCC','OSCR','OTLY','OVV','OWL',
            'PAA','PAAS','PACB','PAGP','PAGS','PAYO','PBCT','PEB','PENN','PK','PLAN','PNM','PRG','PRGO','PSFE','PSTG',
            'PVG','PVH','QRTEA','RDN','RIOT','RKLB','RKT','RLX','RRC','RRR','RUN','SABR','SAVA','SAVE','SBRA','SBS',
            'SBSW','SEAS','SFIX','SFM','SG','SGMS','SHO','SID','SIG','SITC','SIX','SKIN','SKLZ','SLM','SM','SMAR',
            'SONO','SPCE','SPR','SPWR','SSRM','STEM','STNE','STWD','SWCH','SWN','TAL','TAP','TEVA','TGTX','TLRY',
            'TPX','TRIP','TSP','TUYA','TV','TWO','UFS','UGP','UNIT','UNM','UPWK','URBN','USFD','VEON','VG','VIAV',
            'VIPS','VIR','VMEO','VNO','VOYA','VRM','VRT','VST','VVV','WB','WE','WEN','WISH','WOOF','WU','WYNN',
            'X','XPO','XRX','YY','ZH','ZIM','ZNGA','ZUO']

            
        mm=['adbe','gme','nvda','nflx','asml','mu','avgo','amd','asml','qcom','mrvl']
        m33=['docu','^ndx','^gspc','^dji','qqq','spy','tna','arkk','amzn','googl','tsla','adbe','mrna','zm']
        m3=['t','e']
        dp = pd.DataFrame() 

        for x in mc:
            print(x)
            dp=alert(x,dp)


        ##dpx.to_csv('/home/az2/Dwonloads/bb444a', sep='\t', encoding='utf-8', header='true')
        ##print(dp[['Date','ticker','Close']],'\n', 'reading from df')


            

        os.remove('/home/az2/nnna44444.txt')
        dp.sort_values(by=['delta','adx'],inplace=True)
        dp.to_csv('/home/az2/nnna44444.txt')


        s=pd.read_csv('/home/az2/nnna44444.txt')
        print(s[['Date', 'weekday','ticker', 'Close', 'delta','adx','adx_Prev','STOCHRSI_fastk','ATRa','ATRa_prev', 'pp', 'HL', 'High', 'Low',
                'DM_DI_Signal']],'\n','p2')
        print('\n\n')


        print(s[['Date', 'weekday','ticker', 'Close', 'delta','Aroon_signal', 'aroonup',
               'aroondown','MOM','MOM_Prev','MOM_slope','MOM_slope_Prev']],'\n','p2')
        print('\n\n')
              

        print(s[['Date', 'weekday','ticker', 'Close', 'delta',  'Volume', 'DM_DI', 'PLUS_DI', 'PLUS_DM', 'RSI',
               'CCI','Redby','Red','Close>vwap','Close>21']],'\n','p3')

        print('\n\n')

        print('\n\n')
              

        print(s[['Date', 'weekday','ticker', 'Close', 'delta','RSI','RSI_Prev',
               'CCI','CCI_Prev','Redby','Red','Red_Prev','Close>vwap','Close>vwap_Prev','Close>21','Close>21_Prev']],'\n','p3d')

        print('\n\n')



        print(s[['Date', 'weekday','ticker', 'Close', 'delta','Volume', 'DM_DI', 'PLUS_DI', 'PLUS_DM', 'RSI',
               'CCI','Close_Up_kelt','Close_Low_kelt']],'\n','p4')
        print('\n\n')



        print(s[['Date', 'weekday','ticker', 'Close', 'delta',
               'Close_UpBol','Close_MidBol','Close_LowBol','BB_upperband', 'BB_middleband', 'BB_lowerband'
                 ]],'\n','p5')

        print('\n\n')

        print(s[['Date', 'weekday','ticker', 'Close', 'delta','5>10', '5>10_Prev', '10>21','10>21_Prev', '21>50','21>50_Prev','50>100_Prev', '50>100',
                
                 ]],'\n','p6')
        print('\n\n')


        print('\n\n')

        print(s[['Date', 'weekday','ticker', 'Close', 'delta', 'Close_UpBol', 'Close_UpBol_Prev', 'Close_MidBol','Close_MidBol_Prev','Close_LowBol','Close_LowBol'
                 ]],'\n','p6b')
        print('\n\n')


        print('\n\n')
        print(s[['Date', 'weekday','ticker', 'Close', 'delta',
                 'Close>5','Close>10', 'Close>21', 'Close>50', 'Close>100']],'\n','p5')
        print('\n\n')

        ##print('\n\n')
        ##print(s[['Date', 'weekday','ticker', 'Close', 'delta',
        ##         'Close>5_Prev','Close>10_Prev', 'Close>21_Prev', 'Close>50_Prev', 'Close>100_Prev']],'\n','p5b')
        ##print('\n\n')



        print(s[['Date', 'weekday','ticker', 'Close', 'delta',
               '5>vwap', '21>vwap', '50>vwap', '100>vwap', '200>vwap', 'vwap', 'Close>vwap','squeeze_on',
               'ULTOSC', 'ROC', 'MOM']],'\n','p7')


        print('\n\n')
        print(s[['Date', 'weekday','ticker', 'Close', 'delta',
                 'EMA_5s', 'EMA_10s', 'EMA_21s', 'EMA_50s', 'lower_keltner','upper_keltner']],'\n','p8')

        ##
        ##dp=pd.read_csv('/home/az2/Dwonloads/bb444a.txt')
        ##dp=pd.DataFrame(dp)
        ##print(dp,'\n','reading from file')
        ##print('\n\n','exiting','\n',dp)


##most_active()
alert55()


  
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






