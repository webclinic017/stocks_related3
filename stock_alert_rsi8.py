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
    allb=['AAPL', 'AFRM', 'AMAT', 'AMC', 'AMD', 'BA', 'BABA', 'DIS', 'FB', 'FUTU', 'IWM', 'JD', 'JPM', 'LCID', 'LGVN', 'MARA', 'MRNA', 'MRVL', 'MSFT', 'MU', 'NVDA', 'PDD', 'PLUG', 'PTON', 'PYPL', 'QCOM', 'QQQ', 'RBLX', 'RIOT', 'SAVA', 'SOXL', 'SPXL', 'SPY', 'SQ', 'TNA', 'TQQQ', 'TSLA', 'TSM', 'V', 'XLK', 'XOP', 'XPEV', 'Z', 'MRNA', 'BNTX'
    ,'A', 'AAP', 'AAPL', 'ABMD', 'ACN', 'ADBE', 'ADI', 'ADP', 'ADSK', 'AIZ', 'AJG', 'ALB', 'ALGN', 'ALLE', 'AMAT', 'AMD', 'AMGN', 'AMP', 'AMT', 'AMZN', 'ANET', 'ANSS', 'ANTM', 'AON', 'APD', 'APTV', 'ARE', 'AVB', 'AVGO', 'AVY', 'AWK', 'AXP', 'AZO', 'BA', 'BBY', 'BDX', 'BIIB', 'BIO', 'BKNG', 'BLK', 'BR', 'BXP', 'CAT', 'CB', 'CBOE', 'CBRE', 'CCI', 'CDNS', 'CDW', 'CE', 'CHTR', 'CI', 'CLX', 'CME', 'CMG', 'CMI', 'COF', 'COO', 'COST', 'CPRT', 'CRL', 'CRM', 'CTAS', 'CTLT', 'CZR', 'DE', 'DFS', 'DG', 'DGX', 'DHR', 'DIS', 'DLR', 'DLTR', 'DOV', 'DPZ', 'DRI', 'DVA', 'DXCM', 'EA', 'ECL', 'EFX', 'EL', 'EMN', 'ENPH', 'EOG', 'EQIX', 'ESS', 'ETN', 'ETSY', 'EW', 'EXPD', 'EXPE', 'EXR', 'FANG', 'FB', 'FDX', 'FFIV', 'FIS', 'FLT', 'FRC', 'FRT', 'FTNT', 'GD', 'GNRC', 'GOOG', 'GOOGL', 'GPN', 'GRMN', 'GS', 'GWW', 'HCA', 'HD', 'HES', 'HII', 'HLT', 'HON', 'HUM', 'IDXX', 'IEX', 'IFF', 'ILMN', 'INFO', 'INTU', 'IPGP', 'IQV', 'ISRG', 'IT', 'ITW', 'J', 'JBHT', 'JKHY', 'JPM', 'KEYS', 'KLAC', 'KMX', 'KSU', 'LEN', 'LH', 'LHX', 'LIN', 'LLY', 'LMT', 'LOW', 'LRCX', 'LYV', 'MA', 'MAA', 'MAR', 'MCD', 'MCK', 'MCO', 'MHK', 'MKTX', 'MLM', 'MMC', 'MMM', 'MPWR', 'MSCI', 'MSFT', 'MSI', 'MTB', 'MTD', 'MU', 'NDAQ', 'NFLX', 'NKE', 'NOC', 'NOW', 'NSC', 'NTRS', 'NUE', 'NVDA', 'NVR', 'NXPI', 'ODFL', 'ORLY', 'PAYC', 'PH', 'PKI', 'PLD', 'PNC', 'POOL', 'PPG', 'PSA', 'PTC', 'PVH', 'PWR', 'PXD', 'PYPL', 'QCOM', 'QRVO', 'RCL', 'RE', 'REGN', 'RL', 'RMD', 'ROK', 'ROP', 'ROST', 'SBAC', 'SHW', 'SIVB', 'SNA', 'SNPS', 'SPG', 'SPGI', 'STE', 'STX', 'STZ', 'SWK', 'SWKS', 'SYK', 'TDG', 'TDY', 'TEL', 'TER', 'TFX', 'TGT', 'TMO', 'TROW', 'TRV', 'TSCO', 'TSLA', 'TTWO', 'TXN', 'TYL', 'UHS', 'ULTA', 'UNH', 'UNP', 'UPS', 'URI', 'V', 'VMC', 'VRSK', 'VRSN', 'VRTX', 'WAT', 'WHR', 'WLTW', 'WST', 'WYNN', 'XLNX', 'ZBH', 'ZBRA', 'ZTS'
    ,'AAPL', 'AMGN', 'AXP', 'BA', 'CAT', 'CRM', 'DIS', 'GS', 'HD', 'HON', 'JPM', 'MCD', 'MMM', 'MSFT', 'NKE', 'TRV', 'UNH', 'V'
    ,'AAPL', 'ADBE', 'ADI', 'ADP', 'ADSK', 'ALGN', 'AMAT', 'AMD', 'AMGN', 'AMZN', 'ANSS', 'ASML', 'AVGO', 'BIDU', 'BIIB', 'BKNG', 'CDNS', 'CDW', 'CHTR', 'COST', 'CPRT', 'CTAS', 'DLTR', 'DOCU', 'DXCM', 'EA', 'FB', 'GOOG', 'GOOGL', 'IDXX', 'ILMN', 'INTU', 'ISRG', 'JD', 'KLAC', 'LRCX', 'LULU', 'MAR', 'MELI', 'MRNA', 'MRVL', 'MSFT', 'MU', 'NFLX', 'NTES', 'NVDA', 'NXPI', 'OKTA', 'ORLY', 'PDD', 'PTON', 'PYPL', 'QCOM', 'REGN', 'ROST', 'SGEN', 'SPLK', 'SWKS', 'TEAM', 'TSLA', 'TXN', 'VRSK', 'VRSN', 'VRTX', 'WDAY', 'XLNX', 'ZM'
    ,'CAR', 'EXPD', 'FDX', 'JBHT', 'KSU', 'LSTR', 'NSC', 'UNP', 'UPS'
    ,'ARKG', 'ARKK', 'ARKW', 'BOIL', 'DIA', 'FAS', 'GUSH', 'IBB', 'IGV', 'IJH', 'IVV', 'IWB', 'IWF', 'IWM', 'IWN', 'IWO', 'JNUG', 'LABU', 'MDY', 'MTUM', 'OIH', 'QLD', 'QQQ', 'SMH', 'SOXL', 'SPXL', 'SPY', 'SSO', 'TAN', 'TECL', 'TNA', 'TQQQ', 'UPRO', 'VB', 'VOO', 'VTI', 'VUG', 'XBI', 'XLK', 'XLY', 'XOP']


    allv=['spy','tna','mstr','coin','tsla']
    all=['ba','adbe','tsla']
    pp_buy=[]
    pp_sell=[]


    
    

    print('# of stocks being checked: ',len(all))
    i=0
    i2=0
    for x in all:
        print(x)
        df=yf.Ticker(x).history(period ='6d', interval = '1m',prepost = False)
        df=pd.DataFrame(df)
##        print(df)

        v = df['Volume'].values
        tp = (df['Low'] + df['Close'] + df['High']).div(3).values
        df = df.assign(vwap=(tp * v).cumsum() / v.cumsum())
       
        i=i+1

        df=df[df.index.astype(str).str.contains('2021-12-08')]
        print(df)

##        sys.exit()

        df['Boling_upper2']=''
        df['Boling__middle2']=''
        df['Boling_lower2']=''
        df['x']=''
        df['SARx']=''
        df['ADX_over25_strong_less25_weak_trend']=''

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
#################### case 1 #########################            
            # Buy condition
            uu3=df['Low'].loc[x] > df['EMA_3'].loc[x] and\
                 df['Low'].loc[x] > df['Low'].shift(1).loc[x] and\
                 df['EMA_3'].loc[x] > df['EMA_5'].loc[x] and\
                 df['EMA_5'].loc[x] > df['EMA_10'].loc[x]and\
                 df['EMA_10'].loc[x] > df['EMA_21'].loc[x] and\
                 df['Low'].loc[x] > df['EMA_10'].loc[x] and\
                 df['Low'].loc[x] > df['EMA_21'].loc[x]and\
                 df['Low'].loc[x] > df['EMA_50'].loc[x] and\
                 df['High'].loc[x] > df['vwap'].loc[x] 
                 
            


##            #sell condition
##            sell=df['MOM'].loc[x] < df['MOM'].shift(1).loc[x] and\
##                  df['Low'].loc[x] < df['Low'].shift(1).loc[x] and\
##                  df['Close'].loc[x]<v5
##                  
##            
##            sell=df['EMA_3'].loc[x] < df['EMA_10'].loc[x] 
#####################################################
##            # Buy condition
##            uu3=df['Low'].loc[x] > df['EMA_5'].loc[x] and\
##                 df['Close'].loc[x]>df['vwap'].loc[x] and\
##                 df['Low'].loc[x]>df['vwap'].loc[x] and\
##                 df['EMA_5'].loc[x]-df['EMA_10'].loc[x]>0 and\
##                 df['EMA_10'].loc[x]-df['EMA_21'].loc[x]>0 and\
##                 df['EMA_21'].loc[x]-df['EMA_50'].loc[x]>0 and\
##                 df['EMA_21'].shift(1).loc[x]-df['EMA_50'].shift(1).loc[x]>0
##                 
##            
##
####            uu3=df['Low'].loc[x] > df['EMA_5'].loc[x] or\
####                 (df['EMA_5'].loc[x]-df['EMA_10'].loc[x]>0 and df['EMA_5'].shift(1).loc[x]-df['EMA_10'].shift(1).loc[x]<0) or\
####                 df['EMA_10'].loc[x]-df['EMA_21'].loc[x]>0 and df['EMA_10'].shift(1).loc[x]-df['EMA_21'].shift(1).loc[x]<0 or\
####                 df['EMA_21'].loc[x]-df['EMA_50'].loc[x]>0 and df['EMA_21'].loc[x]-df['EMA_50'].loc[x]<0 
####         
####             
####            
####
####
##            #sell condition
##            sell=df['Low'].loc[x] < df['EMA_5'].loc[x]
####            or\
####                  df['EMA_5'].loc[x]-df['EMA_10'].loc[x]<0 or\
####                   df['EMA_10'].loc[x]-df['EMA_21'].loc[x]<0 or\
####                   df['EMA_21'].loc[x]-df['EMA_50'].loc[x]<0
####                   
                   
            
#################################################################
            

    ##        print(df['ticker'].loc[x],df['Datetime'].loc[x],round(df['Close'].loc[x],2),i2,' SAR ',\
    ##                  round(df['SARx'].loc[x],2),' MOM ',round(df['MOM'].loc[x],2),' CCI',\
    ##                  round(df['CCI'].loc[x],2),\
    ##                  '  macd ',round(df['macd'].loc[x],2), round(df['macdsignal'].loc[x],2),round(df['macdhist'].loc[x],2),\
    ##                  '  adx',round(df['adx'].loc[x],2),' ema35',round(df['EMA-35'].loc[x],2),
    ##                  round(df['aroondown'].loc[x],2),round(df['aroonup'].loc[x],2)

    ##              )
            
    ##        if  df['SAR'].loc[x] - df['Close'].loc[x] < 0 and df['SAR'].shift(1).loc[x] - df['Close'].shift(1).loc[x] > 0 and\
    ##        df['CCI'].loc[x] > 100 :

    #########################################################################################################################################################
            if i2=='53':    # Buy algoritham
                uu=df['Low'].loc[x] < df['EMA_50'].loc[x] and df['Low'].loc[x] < df['EMA_21'].loc[x] and df['Low'].loc[x] < df['Low'].shift(1).loc[x]
                uu2=df['Low'].loc[x]<df['Low'].shift(1).loc[x] and df['Low'].shift(1).loc[x]  < df['Low'].shift(2).loc[x] and df['High'].loc[x] <\
                    df['EMA_50'].loc[x]

    # downtred
                uu3b=df['Close'].loc[x] < df['Close'].shift(1).loc[x]  and df['EMA_50'].loc[x] < df['EMA_50'].shift(1).loc[x] and\
                     df['MOM'].loc[x] < df['MOM'].shift(1).loc[x]
##                
##                uu3=df['Close'].loc[x] < df['Close'].shift(1).loc[x] and df['Close'].loc[x] < df['EMA_21'].loc[x] \
##                     and df['Close'].loc[x] < df['EMA_10'].loc[x] and df['Close'].loc[x] > df['EMA_50'].loc[x]\
##                     and df['MOM'].loc[x] < df['MOM'].shift(1).loc[x] and df['CCI'].loc[x] < 130 and (round(df['SAR'].loc[x],2) > df['Close'].loc[x]) 

                if uu3:
                    t_buy=df['Datetime'].loc[x]

    ##            if df['aroonup'].loc[x] == 100:
    ###############################################################################################################################################                
                    
    ##               df['MOM'].loc[x] < df['MOM'].shift(1).loc[x] and\
    ##               df['SAR'].loc[x]<df['SAR'].shift(1).loc[x]:
                
    ##            if df['macdsignal'].loc[x] < 0 :
    ##                print('\n')
    ##                print(i2,' Sell %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
                    v5=df['Close'].loc[x] #v5 is buy
                    v6=df['CCI'].loc[x]
        ##                    profit=(v5-v4)
        ##
        ##    ##                print(df['ticker'].loc[x],v4.round(2),v5.round(2),' profit-----> ',profit.round(2))
        ##    ##                pp=pp.append(df['ticker'].loc[x],v4.round(2),v5.round(2),profit.round(2))
        ##
        ##                    t2_buy=pd.Series(str(t_buy))
        ##                    t2_sell=pd.Series(str(t_sell))
        ##                    xm=pd.Series(str(df['ticker'].loc[x]))
        ##                    x2=pd.Series(v5.round(2))  # buy
        ##                    x3=pd.Series(v4.round(2))  # sell
        ##                    x4=pd.Series(profit.round(2))
        ##                    x5=pd.Series(v6.round(2))  #CCI


    ##                time.sleep(2)

                    
                        
                    
    ##                if profit < 0:
    ####                    time.sleep(4)
                    i2='51'

##                    g6=pd.concat([xm,x2,x3,x4,x5,t2_buy,t2_sell],axis=1)
##                    g7a=g6
##                    
##
##                    g7=g7.append(g7a,ignore_index=True)
    ##                print(g7)
                    
##        return(g7)

    ######################################################################################################################################
            if i2=='51':   # Sell condition
    ##            pb=df['MOM'].loc[x]-df['MOM'].shift(1).loc[x] > 0
##                sell=df['macd'].loc[x] < 0
                sellk=df['MOM_slope'].loc[x] > -.6 and df['CCI'].loc[x] > -50
##                (round(df['SAR'].loc[x],2) < df['High'].loc[x]) 
##                df['MOM'].loc[x] > df['MOM'].shift(1).loc[x]
##                df['Low'].loc[x]>df['Low'].shift(1).loc[x]
##                and df['MOM'].loc[x]>df['MOM'].shift(1).loc[x] and\
##                    df['EMA_5'].loc[x]>df['EMA_5'].shift(1).loc[x] and df['MOM'].loc[x]>df['MOM'].shift(2).loc[x] and\
##                    (round(df['SAR'].loc[x],2) < df['Close'].loc[x]) 
                
                
    ##            uu=df['Low'].loc[x]-df['Low'].shift(1).loc[x] > 0 and df['Low'].shift(1).loc[x]-df['Low'].shift(2).loc[x]>0

#####################################################################################################
## ***************************************************************************************************
## ***************************************************************************************************
## ***************************************************************************************************
## ***************************************************************************************************                
                #sell condition
                sell=df['MOM'].loc[x] < df['MOM'].shift(1).loc[x] and\
                      df['Low'].loc[x] < df['Low'].shift(1).loc[x] and\
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
    ##               df['SAR'].loc[x]>df['SAR'].shift(1).loc[x]and\
                   
                
                
    ####               df['Low'].loc[x]-df['EMA_3'].loc[x] > 0\
    ####               and\
    ##            if df['Close'].loc[x]-df['EMA_3'].loc[x] > 0\
    ##               and\
    ##               df['Close'].shift(1).loc[x]-df['EMA_5'].shift(1).loc[x] < 0 and\
    ##               df['MOM'].loc[x]>df['MOM'].shift(1).loc[x]\
    ##               and\
    ##               df['SAR'].loc[x]-df['Close'].loc[x] <0 :
                ##            df['EMA_10'].loc[x]-df['EMA_21'].loc[x] > 0 and df['EMA_10'].shift(1).loc[x]-df['EMA_21'].shift(1).loc[x]>0
    ##            and
    ##            df['EMA_21'].loc[x]-df['EMA_50'].loc[x] > 0 and df['EMA_21'].shift(1).loc[x]-df['EMA_50'].shift(1).loc[x]>0
    ##            and
            

                

    ##            if df['SAR'].loc[x] - df['Close'].loc[x] < 0 and df['MOM'].loc[x] - df['MOM'].shift(1).loc[x] > 0 and df['Close'].loc[x] > df['EMA_3'].loc[x]\
    ##               and df['Close'].loc[x] > df['EMA_5'].loc[x] and df['Close'].loc[x] > df['EMA_10'].loc[x] and df['Close'].loc[x] > df['EMA_21'].loc[x]\
    ##               and df['Close'].loc[x] > df['EMA_3'].shift(1).loc[x]\
    ##               and df['EMA_3'].loc[x]>df['EMA_5'].loc[x] and df['EMA_5'].loc[x]>df['EMA_10'].loc[x]and df['EMA_10'].loc[x]>df['EMA_21'].loc[x]:
    ##            
                
                    
    ##            if df['macdsignal'].loc[x] > 0 and (df['macdsignal'].shift(1).loc[x] < 0 and df['macdsignal'].shift(2).loc[x] < 0  and df['CCI'].loc[x] < -100):
           


                    i2='53'

    ##                print('\n')
    ##                print('------BUY------------------------------------------------------------------------------------------------------')
    ##                print(i2,'****macd up -- cci100-sar-reversal-down*********',df['Datetime'].loc[x],round(df['Close'].loc[x],2),i2,' SAR ',\
    ##                      round(df['SARx'].loc[x],2),' MOM ',round(df['MOM'].loc[x],2),' CCI',\
    ##                      round(df['CCI'].loc[x],2),\
    ##                      '  macd ',round(df['macd'].loc[x],2), round(df['macdsignal'].loc[x],2),round(df['macdhist'].loc[x],2),\
    ##                      '  adx',round(df['adx'].loc[x],2),' ema35',round(df['EMA-35'].loc[x],2),'    UP')
    ##
    ##                print('------------------------------------------------------------------------------------------------------------')
    ##                
                    v4=df['Close'].loc[x]   # v4 is sell
                    profit=(v5-v4)

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



############################################################################















        b=g7
        b.sort_values(by=[3])
        print(b)
        print('\n\n')

    ##        elif df['High'].loc[x] < df['Boling_upper'].loc[x]:
    ##            print(x,' cci100-sar-reversal-down   ',df['ticker'].loc[x],' No  ',df['Close'].loc[x],i2,' / ',round(df['SAR'].loc[x],2))
    ##

    ##        if  df['SAR'].loc[x] - df['Close'].loc[x] > 0 and df['SAR'].shift(1).loc[x] - df['Close'].shift(1).loc[x] < 0 and\
    ##                df['CCI'].loc[x] < -100 :

    ##                    elif df['macdsignal'].loc[x] < 0 and (df['macdsignal'].shift(1).loc[x] > 0 and df['macdsignal'].shift(2).loc[x] > 0):
    ##                        print('c3b  ',len(c3b))
    ##                        if len(c3) >0:
    ##                            print('************************************************************8 c4=',df['Close'][c4[0]],'  ',df['Close'][c4[-1]])
    ##                        c3=[] 
    ##                        profit3=df['Close'].loc[x]
    ##
    ##                        
    ##                        print('----profit/loss--------------------------------------------------------------------------------------------------------')
    ##            ##            print(profit3-profit2)
    ##                        print('----D--------------------------------------------------------------------------------------------------------')
    ##                        
    ##                    
    ##            ##        and df['Close'].loc[x]> df['Close'].shift(1).loc[x] and df['CCI'].loc[x]< -200 \
    ##            ##           and df['ATR'].loc[x] > 2
    ##            ##        :
    ##                        i2=i2+1
    ##                        sell.append(x)
    ##                        print('----D--------------------------------------------------------------------------------------------------------')
    ##                        print('********macd down*****SAR reversal up**********''',df['Datetime'].loc[x],round(df['Close'].loc[x],2),i2,' SAR ',\
    ##                              round(df['SARx'].loc[x],2),' MOM ',round(df['MOM'].loc[x],2),' CCI',\
    ##                              round(df['CCI'].loc[x],2),\
    ##                              '  macd ',round(df['macd'].loc[x],2), round(df['macdsignal'].loc[x],2),round(df['macdhist'].loc[x],2),\
    ##                              '  adx',round(df['adx'].loc[x],2),' ema35',round(df['EMA-35'].loc[x],2),'    Down')
    ##                        print('------------------------------------------------------------------------------------------------------------')
    ##                        k2=1
    ##                    elif df['macdsignal'].loc[x] < 0 and (df['macdsignal'].shift(1).loc[x] < 0 and df['macdsignal'].shift(2).loc[x] < 0 ):
    ##                        k2=k2+1
    ##                        c3.append(x)
    ##                        print('U',df['Datetime'].loc[x],round(df['Close'].loc[x],2),i2,' SAR ',\
    ##                              round(df['SARx'].loc[x],2),' MOM ',round(df['MOM'].loc[x],2),' CCI',\
    ##                              round(df['CCI'].loc[x],2),\
    ##                              '  macd ',round(df['macd'].loc[x],2), round(df['macdsignal'].loc[x],2),round(df['macdhist'].loc[x],2),\
    ##                              '  adx',round(df['adx'].loc[x],2),' ema35',round(df['EMA-35'].loc[x],2),'    Down')

                
    ##        elif df['High'].loc[x] > df['Boling_lower2'].loc[x]:
    ##            
    ##            print(x,'    ',df['ticker'].loc[x],' No ',df['Close'].loc[x],i2,'  ',round(df['SAR'].loc[x],2))
    ##


            
    ##        if df['High'].loc[x] >= df['Boling_upper'].loc[x] and df['SAR'].loc[x] - df['Close'].loc[x] < 0:
    ####        and df['Close'].loc[x]<df['Close'].shift(1).loc[x] and\
    ####        df['CCI'].loc[x] > 200 and df['ATR'].loc[x]>2
    ####        :
    ##            i2=i2+1
    ##            cc=df['Close']
    ##            buy.append(x)
    ##            print('************** Bolinger_High ',df['Close'].loc[x],i2,'  ',x,'  ',round(df['High'].loc[x]-df['Boling_upper'].loc[x],2),'  ',round(df['High'].loc[x],2),'/',round(df['Boling_upper'][-1],2))
    ##        elif df['High'].loc[x] < df['Boling_upper'].loc[x]:
    ##            print(x,'    ',df['ticker'].loc[x],' No  ',round(df['Close'].loc[x],2),'  ',round(df['SAR'].loc[x] - df['Close'].loc[x],2),
    ##                  '  ',round(df['High'].loc[x]-df['Boling_upper'].loc[x],2))
    ##
    ##
    ##        if df['Low'].loc[x] <= df['Boling_lower2'].loc[x] and df['SAR'].loc[x]> df['Close'].loc[x]:
    ####        and df['Close'].loc[x]> df['Close'].shift(1).loc[x] and df['CCI'].loc[x]< -200 \
    ####           and df['ATR'].loc[x] > 2
    ####        :
    ##            i2=i2+1
    ##            sell.append(x)
    ##            print('################### Bolinger_Low ',i2,'  ',x,'  ',round(df['Low'].loc[x]-df['Boling_lower2'].loc[x],2),'  ',
    ##                  round(df['Low'].loc[x],2),'/',round(df['Boling_lower2'].loc[x],2))
    ##        elif df['High'].loc[x] > df['Boling_lower2'].loc[x]:
    ##            
    ##            print(x,'    ',df['ticker'].loc[x],' No ',round(df['Close'].loc[x],2),'  ',round(df['SAR'].loc[x] - df['Close'].loc[x],2))


    ##    sleep(10)    



    ##
    ##    for x in df.index:
    ##        
    ##        if df['High'].loc[x] >= df['Boling_upper'].loc[x] and df['SAR'].loc[x] - df['Close'].loc[x] < 0 and df['Close'].loc[x]<df['Close'].shift(1).loc[x] and\
    ##        df['CCI'].loc[x] > 200 and df['ATR'].loc[x]>2 :
    ##            i2=i2+1
    ##            buy.append(x)
    ##            print('Bolinger_High ',i2,'  ',x,'  ',round(df['High'].loc[x]-df['Boling_upper'].loc[x],2),'  ',round(df['High'].loc[x],2),'/',round(df['Boling_upper'][-1],2))
    ##        elif df['High'].loc[x] < df['Boling_upper'].loc[x]:
    ##            print(x,'    ',df['ticker'].loc[x],' No')
    ##
    ##
    ##        if df['Low'].loc[x] <= df['Boling_lower2'].loc[x] and df['SAR'].loc[x]> df['Close'].loc[x] and df['Close'].loc[x]> df['Close'].shift(1).loc[x] and df['CCI'].loc[x]< -200 \
    ##           and df['ATR'].loc[x] > 2 :
    ##            i2=i2+1
    ##            sell.append(x)
    ##            print('Bolinger_Low ',i2,'  ',x,'  ',round(df['Low'].loc[x]-df['Boling_lower2'].loc[x],2),'  ',
    ##                  round(df['Low'].loc[x],2),'/',round(df['Boling_lower2'].loc[x],2))
    ##        elif df['High'].loc[x] > df['Boling_lower2'].loc[x]:
    ##            print(x,'    ',df['ticker'].loc[x],' No')



    ##    return(buy,sell)  

s4()


print('\n\n\n')
print('***************************************************************************')
print('this is coming from bottom/main','\n')
##b=columns['purchase_price','Sell_price','Profot']





