import os, pandas
import plotly.graph_objects as go
import yfinance as yf
import pandas as pd
import datetime as dt
import talib as ta

pd.options.display.float_format = '{:.2f}'.format
pd.options.display.max_columns=255
pd.options.display.max_rows=6500000

pd.options.display.max_rows=9999
pd.options.display.max_columns=36
pd.set_option("display.max_columns", 100)
pd.set_option('display.width', 1000)
######pd.set_option('display.max_colwidth', 200)
pd.set_option('display.max_columns', 0)




def s4():
    import os, pandas
    import plotly.graph_objects as go
    import yfinance as yf
    import pandas as pd
    import datetime as dt
    import talib as ta
    import sys
    import warnings
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


##    print('jjj')
##    alln=['aapl','t']
    all=['AAPL', 'AFRM', 'AMAT', 'AMC', 'AMD', 'BA', 'BABA', 'DIS', 'FB', 'FUTU', 'IWM', 'JD', 'JPM', 'LCID', 'LGVN', 'MARA', 'MRNA', 'MRVL', 'MSFT', 'MU', 'NVDA', 'PDD', 'PLUG', 'PTON', 'PYPL', 'QCOM', 'QQQ', 'RBLX', 'RIOT', 'SAVA', 'SOXL', 'SPXL', 'SPY', 'SQ', 'TNA', 'TQQQ', 'TSLA', 'TSM', 'V', 'XLK', 'XOP', 'XPEV', 'Z', 'MRNA', 'BNTX'
    ,'A', 'AAP', 'AAPL', 'ABMD', 'ACN', 'ADBE', 'ADI', 'ADP', 'ADSK', 'AIZ', 'AJG', 'ALB', 'ALGN', 'ALLE', 'AMAT', 'AMD', 'AMGN', 'AMP', 'AMT', 'AMZN', 'ANET', 'ANSS', 'ANTM', 'AON', 'APD', 'APTV', 'ARE', 'AVB', 'AVGO', 'AVY', 'AWK', 'AXP', 'AZO', 'BA', 'BBY', 'BDX', 'BIIB', 'BIO', 'BKNG', 'BLK', 'BR', 'BXP', 'CAT', 'CB', 'CBOE', 'CBRE', 'CCI', 'CDNS', 'CDW', 'CE', 'CHTR', 'CI', 'CLX', 'CME', 'CMG', 'CMI', 'COF', 'COO', 'COST', 'CPRT', 'CRL', 'CRM', 'CTAS', 'CTLT', 'CZR', 'DE', 'DFS', 'DG', 'DGX', 'DHR', 'DIS', 'DLR', 'DLTR', 'DOV', 'DPZ', 'DRI', 'DVA', 'DXCM', 'EA', 'ECL', 'EFX', 'EL', 'EMN', 'ENPH', 'EOG', 'EQIX', 'ESS', 'ETN', 'ETSY', 'EW', 'EXPD', 'EXPE', 'EXR', 'FANG', 'FB', 'FDX', 'FFIV', 'FIS', 'FLT', 'FRC', 'FRT', 'FTNT', 'GD', 'GNRC', 'GOOG', 'GOOGL', 'GPN', 'GRMN', 'GS', 'GWW', 'HCA', 'HD', 'HES', 'HII', 'HLT', 'HON', 'HUM', 'IDXX', 'IEX', 'IFF', 'ILMN', 'INFO', 'INTU', 'IPGP', 'IQV', 'ISRG', 'IT', 'ITW', 'J', 'JBHT', 'JKHY', 'JPM', 'KEYS', 'KLAC', 'KMX', 'LEN', 'LH', 'LHX', 'LIN', 'LLY', 'LMT', 'LOW', 'LRCX', 'LYV', 'MA', 'MAA', 'MAR', 'MCD', 'MCK', 'MCO', 'MHK', 'MKTX', 'MLM', 'MMC', 'MMM', 'MPWR', 'MSCI', 'MSFT', 'MSI', 'MTB', 'MTD', 'MU', 'NDAQ', 'NFLX', 'NKE', 'NOC', 'NOW', 'NSC', 'NTRS', 'NUE', 'NVDA', 'NVR', 'NXPI', 'ODFL', 'ORLY', 'PAYC', 'PH', 'PKI', 'PLD', 'PNC', 'POOL', 'PPG', 'PSA', 'PTC', 'PVH', 'PWR', 'PXD', 'PYPL', 'QCOM', 'QRVO', 'RCL', 'RE', 'REGN', 'RL', 'RMD', 'ROK', 'ROP', 'ROST', 'SBAC', 'SHW', 'SIVB', 'SNA', 'SNPS', 'SPG', 'SPGI', 'STE', 'STX', 'STZ', 'SWK', 'SWKS', 'SYK', 'TDG', 'TDY', 'TEL', 'TER', 'TFX', 'TGT', 'TMO', 'TROW', 'TRV', 'TSCO', 'TSLA', 'TTWO', 'TXN', 'TYL', 'UHS', 'ULTA', 'UNH', 'UNP', 'UPS', 'URI', 'V', 'VMC', 'VRSK', 'VRSN', 'VRTX', 'WAT', 'WHR', 'WLTW', 'WST', 'WYNN', 'XLNX', 'ZBH', 'ZBRA', 'ZTS'
    ,'AAPL', 'AMGN', 'AXP', 'BA', 'CAT', 'CRM', 'DIS', 'GS', 'HD', 'HON', 'JPM', 'MCD', 'MMM', 'MSFT', 'NKE', 'TRV', 'UNH', 'V'
    ,'AAPL', 'ADBE', 'ADI', 'ADP', 'ADSK', 'ALGN', 'AMAT', 'AMD', 'AMGN', 'AMZN', 'ANSS', 'ASML', 'AVGO', 'BIDU', 'BIIB', 'BKNG', 'CDNS', 'CDW', 'CHTR', 'COST', 'CPRT', 'CTAS', 'DLTR', 'DOCU', 'DXCM', 'EA', 'FB', 'GOOG', 'GOOGL', 'IDXX', 'ILMN', 'INTU', 'ISRG', 'JD', 'KLAC', 'LRCX', 'LULU', 'MAR', 'MELI', 'MRNA', 'MRVL', 'MSFT', 'MU', 'NFLX', 'NTES', 'NVDA', 'NXPI', 'OKTA', 'ORLY', 'PDD', 'PTON', 'PYPL', 'QCOM', 'REGN', 'ROST', 'SGEN', 'SPLK', 'SWKS', 'TEAM', 'TSLA', 'TXN', 'VRSK', 'VRSN', 'VRTX', 'WDAY', 'XLNX', 'ZM'
    ,'CAR', 'EXPD', 'FDX', 'JBHT', 'LSTR', 'NSC', 'UNP', 'UPS'
    ,'ARKG', 'ARKK', 'ARKW', 'BOIL', 'DIA', 'FAS', 'GUSH', 'IBB', 'IGV', 'IJH', 'IVV', 'IWB', 'IWF', 'IWM', 'IWN', 'IWO', 'JNUG', 'LABU', 'MDY', 'MTUM', 'OIH', 'QLD', 'QQQ', 'SMH', 'SOXL', 'SPXL', 'SPY', 'SSO', 'TAN', 'TECL', 'TNA', 'TQQQ', 'UPRO', 'VB', 'VOO', 'VTI', 'VUG', 'XBI', 'XLK', 'XLY', 'XOP']


    allv=['spy','tna','mstr','coin','tsla']
    alln=['ba','adbe','tsla']
    pp_buy=[]
    pp_sell=[]


    
    

    print('# of stocks being checked: ',len(all))
    i=0
    i2=0
    for x in all:
##        print(x)
        df=yf.Ticker(x).history(period ='4d', interval = '1m',prepost = False)
        df=pd.DataFrame(df)
##        if df.empty==True:
##            pass
        
##        print(df)

        v = df['Volume'].values
        tp = (df['Low'] + df['Close'] + df['High']).div(3).values
        df = df.assign(vwap=(tp * v).cumsum() / v.cumsum())
       
        i=i+1

        df=df[df.index.astype(str).str.contains('2021-12-17')]
        df = df.dropna(axis=0, how='all')
##        print(df)

##        sys.exit()

        df['Boling_upper2']=''
        df['Boling__middle2']=''
        df['Boling_lower2']=''
        df['x']=''
        df['SARx']=''

##        df['ADX_over25_strong_less25_weak_trend']=''


            

        df['aroondown'],df['aroonup']=ta.AROON(df['High'],df['Low'], timeperiod=14)

        df['CCI']=ta.CCI(df['High'], df['Low'], df['Close'], timeperiod=14)
        df['RSI']= ta.RSI(df['Close'], timeperiod=14)
        df['ATR']=ta.ATR(df['High'],df['Low'],df['Close'], timeperiod=14)
        df['TR'] = abs(df['High'] - df['Low'])
        df['MOM']=ta.MOM(df['Close'], timeperiod=3)
        df['MOM_slope']=df['MOM']-df['MOM'].shift(1)
        df['EMA_3']=ta.EMA(df['Close'], timeperiod=3)
        df['EMA_5']=ta.EMA(df['Close'], timeperiod=5)
        df['EMA_10']=ta.EMA(df['Close'], timeperiod=10)
        df['EMA_50']=ta.EMA(df['Close'], timeperiod=50)
        df['EMA_21']=ta.EMA(df['Close'], timeperiod=21)
        df['EMA_slope']=df['EMA_3']-df['EMA_3'].shift(1)
        df['macd'], df['macdsignal'], df['macdhist'] = ta.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
        df['adx']= ta.ADX(df['High'],df['Low'],df['Close'], timeperiod=14)

        df['EMA-35']=df['EMA_3']-df['EMA_5']



        df['fastk'], df['fastd'] = ta.STOCHRSI(df['Close'], timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
        df['MA'] = ta.EMA(df['fastd'], timeperiod=14)
        df['MA2'] = ta.EMA(df['fastk'], timeperiod=14)
        df['SAR'] = ta.SAR(df['High'], df['Low'], acceleration=90, maximum=5)
        df['Boling_upper'], df['Boling__middle'], df['Boling_lower'] = ta.BBANDS(df['High'], timeperiod=20, nbdevup=2, nbdevdn=2)
        df['Boling_upper2'], df['Boling__middle2'], df['Boling_lower2'] = ta.BBANDS(df['Low'], timeperiod=20, nbdevup=2, nbdevdn=2)
        df['SARx']=df['Close']-df['SAR']
        df['ADX_over25_strong_less25_weak_trend']=ta.ADX(df['High'], df['Low'], df['Close'], timeperiod=3).round(2)
        df['ticker']=x

##        print(df)


            
        df=df[['ticker','High','Close','Low','x','SARx','Boling_upper','Boling_lower2','SAR','CCI','ATR','MOM','MOM_slope',\
               'ADX_over25_strong_less25_weak_trend',\
               'macd', 'macdsignal', 'macdhist','adx','EMA-35','EMA_3','EMA_5','EMA_21','EMA_10','EMA_50',
                'aroondown','aroonup','RSI','vwap'
               ]]

        df3=df
        g6=pd.DataFrame()
        g7=pd.DataFrame()

        i2='53'
        ##        SAR reversal
        df.reset_index(inplace=True)

        m2=[];m3=[];m4=[]

        for x in df.index:

#####################################################################################################
## ***************************************************************************************************
## ***************************************************************************************************
## ***************************************************************************************************
## ***************************************************************************************************               
#################### case 1 #########################            
            # Buy condition
            uu3=df['High'].loc[x] < df['EMA_3'].loc[x] and\
                 df['High'].loc[x] < df['Low'].shift(1).loc[x] and\
                 df['EMA_3'].loc[x] < df['EMA_5'].loc[x] and\
                 df['EMA_5'].loc[x] < df['EMA_10'].loc[x]and\
                 df['EMA_10'].loc[x] < df['EMA_21'].loc[x] and\
                 df['EMA_21'].loc[x] < df['EMA_50'].loc[x] and\
                 df['High'].loc[x] < df['EMA_10'].loc[x] and\
                 df['High'].loc[x] < df['EMA_21'].loc[x]and\
                 df['High'].loc[x] < df['EMA_50'].loc[x] and\
                 df['High'].loc[x] < df['vwap'].loc[x] and\
                 df['EMA_3'].loc[x] < df['vwap'].loc[x] and\
                 df['EMA_5'].loc[x] < df['vwap'].loc[x]and\
                 df['EMA_10'].loc[x] < df['vwap'].loc[x] and\
                 df['EMA_21'].loc[x] < df['vwap'].loc[x] and\
                 df['EMA_50'].loc[x] < df['vwap'].loc[x] and \
                 df['High'].loc[x] < df['vwap'].loc[x]
                 

#####################################################################################################
## ***************************************************************************************************
## ***************************************************************************************************
## ***************************************************************************************************
## ***************************************************************************************************   
    
#################################################################


    #########################################################################################################################################################
            if i2=='53':    # Buy algoritham

                if uu3:
                    t_buy=df['Datetime'].loc[x]

    ##            if df['aroonup'].loc[x] == 100:
    ###############################################################################################################################################                
    ##                print(i2,' Sell %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
                    v5=df['Close'].loc[x] #v5 is buy
                    v6=df['CCI'].loc[x]

                    i2='51'



    ######################################################################################################################################
            if i2=='51':   # Sell condition

                sellk=df['MOM_slope'].loc[x] > -.6 and df['CCI'].loc[x] > -50


#####################################################################################################
## ***************************************************************************************************
## ***************************************************************************************************
## ***************************************************************************************************
## ***************************************************************************************************                
                #sell condition
                sell=df['MOM'].loc[x] < df['MOM'].shift(1).loc[x] and\
                      df['High'].loc[x] < df['High'].shift(1).loc[x] and\
                      df['Close'].loc[x]<v5-.8
## ***************************************************************************************************
## ***************************************************************************************************
## ***************************************************************************************************
## ***************************************************************************************************  


                if sell:
                    t_sell=df['Datetime'].loc[x]
                    
    ##            if df['aroonup'].loc[x] < 70:
    ##            if df['MOM'].loc[x]-df['MOM'].shift(1).loc[x]>.1 and\
    ##               df['CCI'].loc[x]<-70:
    #######################################################################################################################################               
          


                    i2='53'

                    print('------------------------------------------------------------------------------------------------------------')
    ##                
                    v4=df['Close'].loc[x]   # v4 is sell
                    profit=(v5-v4)


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



############################################################################


        b=g7
        tickers_not_meeting_buy_criteria=[]
##        if b.shape[0]>1:
##            b.sort_values(by=[3])
        if b.shape[0]>0:
            print(b)
            print('\n')
        elif b.shape[0] < 1:
            tickers_not_meeting_buy_criteria.append(x)
    print('\n')        
    print('tickers that did not meet buy criteria:')
    print(len(tickers_not_meeting_buy_criteria),'    ',tickers_not_meeting_buy_criteria)        



s4()


print('\n\n\n')
print('***************************************************************************')
print('this is coming from bottom/main','\n')
##b=columns['purchase_price','Sell_price','Profot']





