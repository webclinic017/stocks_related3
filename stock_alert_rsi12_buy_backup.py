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

    nasdaq100=['AAPL', 'ADBE', 'ADI', 'ADP', 'ADSK', 'AEP', 'ALGN', 'AMAT', 'AMD', 'AMGN', 'AMZN', 'ANSS', 'ASML', 'ATVI', 'AVGO', 'BIDU', 'BIIB', 'BKNG', 'CDNS', 'CDW', 'CERN', 'CHKP', 'CHTR', 'CMCSA', 'COST', 'CPRT', 'CSCO', 'CSX', 'CTAS', 'CTSH', 'DLTR', 'DOCU', 'DXCM', 'EA', 'EBAY', 'EXC', 'FAST', 'FB', 'FISV', 'FOX', 'FOXA', 'GILD', 'GOOG', 'GOOGL', 'IDXX', 'ILMN', 'INCY', 'INTC', 'INTU', 'ISRG', 'JD', 'KDP', 'KHC', 'KLAC', 'LRCX', 'LULU', 'MAR', 'MCHP', 'MDLZ', 'MELI', 'MNST', 'MRNA', 'MRVL', 'MSFT', 'MU', 'NFLX', 'NTES', 'NVDA', 'NXPI', 'OKTA', 'ORLY', 'PAYX', 'PCAR', 'PDD', 'PEP', 'PTON', 'PYPL', 'QCOM', 'REGN', 'ROST', 'SBUX', 'SGEN', 'SIRI', 'SPLK', 'SWKS', 'TCOM', 'TEAM', 'TMUS', 'TSLA', 
        'TXN', 'VRSK', 'VRSN', 'VRTX', 'WBA', 'WDAY', 'XEL', 'XLNX', 'ZM' ]

    gg6=nasdaq100
    i=0
    for x in gg6: # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
        
        dfqq=pd.DataFrame()
        dfq=pd.DataFrame()
        x5=[]
        print(i, x, gg6[i])
        df=yf.Ticker(gg6[i]).history(period ='4d', interval = '1m',prepost = False)
        df=df.drop(columns=[ 'Dividends', 'Stock Splits'])
        i=i+1


        

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

        for z in df.index:
           uu3=df['MOM'].loc[z]-df['MOM'].shift(1).loc[z] > 0 and df['macd'].loc[z]>0 and df['adx'].loc[z]>24 and df['ATR'].loc[z]>.9\
                and df['TR'].loc[z]>.5   
##
##        
           if uu3:
               ss.append(z)
               print(x,'  ',z, '----appended',round(df['MOM'].loc[z]-df['MOM'].shift(1).loc[z],2),'  ',\
                     round(df['macd'].loc[z],2),'  ',round(df['ATR'].loc[z],2),'   ',round(df['TR'].loc[z],2))
##
        print("complete")
        print('No of stocks=',len(ss))

    
def s4():
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
##    from inspect import currentframe, getframeinfo,Traceback

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


##    print('jjj')
##    alln=['aapl','t']
    allnnp=['AAPL', 'AFRM', 'AMAT', 'AMC', 'AMD', 'BA', 'BABA', 'DIS', 'FB', 'FUTU', 'IWM', 'JD', 'JPM', 'LCID', 'LGVN', 'MARA', 'MRNA', 'MRVL', 'MSFT', 'MU', 'NVDA', 'PDD', 'PLUG', 'PTON', 'PYPL', 'QCOM', 'QQQ', 'RBLX', 'RIOT', 'SAVA', 'SOXL', 'SPXL', 'SPY', 'SQ', 'TNA', 'TQQQ', 'TSLA', 'TSM', 'V', 'XLK', 'XOP', 'XPEV', 'Z', 'MRNA', 'BNTX'
    ,'A', 'AAP', 'AAPL', 'ABMD', 'ACN', 'ADBE', 'ADI', 'ADP', 'ADSK', 'AIZ', 'AJG', 'ALB', 'ALGN', 'ALLE', 'AMAT', 'AMD', 'AMGN', 'AMP', 'AMT', 'AMZN', 'ANET', 'ANSS', 'ANTM', 'AON', 'APD', 'APTV', 'ARE', 'AVB', 'AVGO', 'AVY', 'AWK', 'AXP', 'AZO', 'BA', 'BBY', 'BDX', 'BIIB', 'BIO', 'BKNG', 'BLK', 'BR', 'BXP', 'CAT', 'CB', 'CBOE', 'CBRE', 'CCI', 'CDNS', 'CDW', 'CE', 'CHTR', 'CI', 'CLX', 'CME', 'CMG', 'CMI', 'COF', 'COO', 'COST', 'CPRT', 'CRL', 'CRM', 'CTAS', 'CTLT', 'CZR', 'DE', 'DFS', 'DG', 'DGX', 'DHR', 'DIS', 'DLR', 'DLTR', 'DOV', 'DPZ', 'DRI', 'DVA', 'DXCM', 'EA', 'ECL', 'EFX', 'EL', 'EMN', 'ENPH', 'EOG', 'EQIX', 'ESS', 'ETN', 'ETSY', 'EW', 'EXPD', 'EXPE', 'EXR', 'FANG', 'FB', 'FDX', 'FFIV', 'FIS', 'FLT', 'FRC', 'FRT', 'FTNT', 'GD', 'GNRC', 'GOOG', 'GOOGL', 'GPN', 'GRMN', 'GS', 'GWW', 'HCA', 'HD', 'HES', 'HII', 'HLT', 'HON', 'HUM', 'IDXX', 'IEX', 'IFF', 'ILMN', 'INFO', 'INTU', 'IPGP', 'IQV', 'ISRG', 'IT', 'ITW', 'J', 'JBHT', 'JKHY', 'JPM', 'KEYS', 'KLAC', 'KMX', 'LEN', 'LH', 'LHX', 'LIN', 'LLY', 'LMT', 'LOW', 'LRCX', 'LYV', 'MA', 'MAA', 'MAR', 'MCD', 'MCK', 'MCO', 'MHK', 'MKTX', 'MLM', 'MMC', 'MMM', 'MPWR', 'MSCI', 'MSFT', 'MSI', 'MTB', 'MTD', 'MU', 'NDAQ', 'NFLX', 'NKE', 'NOC', 'NOW', 'NSC', 'NTRS', 'NUE', 'NVDA', 'NVR', 'NXPI', 'ODFL', 'ORLY', 'PAYC', 'PH', 'PKI', 'PLD', 'PNC', 'POOL', 'PPG', 'PSA', 'PTC', 'PVH', 'PWR', 'PXD', 'PYPL', 'QCOM', 'QRVO', 'RCL', 'RE', 'REGN', 'RL', 'RMD', 'ROK', 'ROP', 'ROST', 'SBAC', 'SHW', 'SIVB', 'SNA', 'SNPS', 'SPG', 'SPGI', 'STE', 'STX', 'STZ', 'SWK', 'SWKS', 'SYK', 'TDG', 'TDY', 'TEL', 'TER', 'TFX', 'TGT', 'TMO', 'TROW', 'TRV', 'TSCO', 'TSLA', 'TTWO', 'TXN', 'TYL', 'UHS', 'ULTA', 'UNH', 'UNP', 'UPS', 'URI', 'V', 'VMC', 'VRSK', 'VRSN', 'VRTX', 'WAT', 'WHR', 'WLTW', 'WST', 'WYNN', 'XLNX', 'ZBH', 'ZBRA', 'ZTS'
    ,'AAPL', 'AMGN', 'AXP', 'BA', 'CAT', 'CRM', 'DIS', 'GS', 'HD', 'HON', 'JPM', 'MCD', 'MMM', 'MSFT', 'NKE', 'TRV', 'UNH', 'V'
    ,'AAPL', 'ADBE', 'ADI', 'ADP', 'ADSK', 'ALGN', 'AMAT', 'AMD', 'AMGN', 'AMZN', 'ANSS', 'ASML', 'AVGO', 'BIDU', 'BIIB', 'BKNG', 'CDNS', 'CDW', 'CHTR', 'COST', 'CPRT', 'CTAS', 'DLTR', 'DOCU', 'DXCM', 'EA', 'FB', 'GOOG', 'GOOGL', 'IDXX', 'ILMN', 'INTU', 'ISRG', 'JD', 'KLAC', 'LRCX', 'LULU', 'MAR', 'MELI', 'MRNA', 'MRVL', 'MSFT', 'MU', 'NFLX', 'NTES', 'NVDA', 'NXPI', 'OKTA', 'ORLY', 'PDD', 'PTON', 'PYPL', 'QCOM', 'REGN', 'ROST', 'SGEN', 'SPLK', 'SWKS', 'TEAM', 'TSLA', 'TXN', 'VRSK', 'VRSN', 'VRTX', 'WDAY', 'XLNX', 'ZM'
    ,'CAR', 'EXPD', 'FDX', 'JBHT', 'LSTR', 'NSC', 'UNP', 'UPS'
    ,'ARKG', 'ARKK', 'ARKW', 'BOIL', 'DIA', 'FAS', 'GUSH', 'IBB', 'IGV', 'IJH', 'IVV', 'IWB', 'IWF', 'IWM', 'IWN', 'IWO', 'JNUG', 'LABU', 'MDY', 'MTUM', 'OIH', 'QLD', 'QQQ', 'SMH', 'SOXL', 'SPXL', 'SPY', 'SSO', 'TAN', 'TECL', 'TNA', 'TQQQ', 'UPRO', 'VB', 'VOO', 'VTI', 'VUG', 'XBI', 'XLK', 'XLY', 'XOP']


    alsl=['spy','tna','mstr','coin','tsla']
    alln=['ba','adbe','tsla']
    all=['AAPL', 'AFRM', 'AMAT', 'AMC', 'AMD', 'BA', 'BABA', 'DIS', 'FB', 'FUTU', 'IWM', 'JD', 'JPM', 'LCID', 'LGVN', 'MARA', 'MRNA', 'MRVL', 'MSFT', 'MU', 'NVDA', 'PDD', 'PLUG', 'PTON', 'PYPL', 'QCOM', 'QQQ', 'RBLX', 'RIOT', 'SAVA', 'SOXL', 'SPXL', 'SPY', 'SQ', 'TNA', 'TQQQ', 'TSLA', 'TSM', 'V', 'XLK', 'XOP', 'XPEV', 'Z', 'MRNA', 'BNTX'
    ,'A', 'AAP', 'AAPL', 'ABMD', 'ACN', 'ADBE', 'ADI', 'ADP', 'ADSK', 'AIZ', 'AJG', 'ALB', 'ALGN', 'ALLE', 'AMAT', 'AMD', 'AMGN', 'AMP', 'AMT', 'AMZN', 'ANET', 'ANSS', 'ANTM', 'AON', 'APD', 'APTV', 'ARE', 'AVB', 'AVGO', 'AVY', 'AWK', 'AXP', 'AZO', 'BA', 'BBY', 'BDX', 'BIIB', 'BIO', 'BKNG', 'BLK', 'BR', 'BXP', 'CAT', 'CB', 'CBOE', 'CBRE', 'CCI', 'CDNS', 'CDW', 'CE', 'CHTR', 'CI', 'CLX', 'CME', 'CMG', 'CMI', 'COF', 'COO', 'COST', 'CPRT', 'CRL', 'CRM', 'CTAS', 'CTLT', 'CZR', 'DE', 'DFS', 'DG', 'DGX', 'DHR', 'DIS', 'DLR', 'DLTR', 'DOV', 'DPZ', 'DRI', 'DVA', 'DXCM', 'EA', 'ECL', 'EFX', 'EL', 'EMN', 'ENPH', 'EOG', 'EQIX', 'ESS', 'ETN', 'ETSY', 'EW', 'EXPD', 'EXPE', 'EXR', 'FANG', 'FB', 'FDX', 'FFIV', 'FIS', 'FLT', 'FRC', 'FRT', 'FTNT', 'GD', 'GNRC', 'GOOG', 'GOOGL', 'GPN', 'GRMN', 'GS', 'GWW', 'HCA', 'HD', 'HES', 'HII', 'HLT', 'HON', 'HUM', 'IDXX', 'IEX', 'IFF', 'ILMN', 'INFO', 'INTU', 'IPGP', 'IQV', 'ISRG', 'IT', 'ITW', 'J', 'JBHT', 'JKHY', 'JPM', 'KEYS', 'KLAC', 'KMX', 'LEN', 'LH', 'LHX', 'LIN', 'LLY', 'LMT', 'LOW', 'LRCX', 'LYV', 'MA', 'MAA', 'MAR', 'MCD', 'MCK', 'MCO', 'MHK', 'MKTX', 'MLM', 'MMC', 'MMM', 'MPWR', 'MSCI', 'MSFT', 'MSI', 'MTB', 'MTD', 'MU', 'NDAQ', 'NFLX', 'NKE', 'NOC', 'NOW', 'NSC', 'NTRS', 'NUE', 'NVDA', 'NVR', 'NXPI', 'ODFL', 'ORLY', 'PAYC', 'PH', 'PKI', 'PLD', 'PNC', 'POOL', 'PPG', 'PSA', 'PTC', 'PVH', 'PWR', 'PXD', 'PYPL', 'QCOM', 'QRVO', 'RCL', 'RE', 'REGN', 'RL', 'RMD', 'ROK', 'ROP', 'ROST', 'SBAC', 'SHW', 'SIVB', 'SNA', 'SNPS', 'SPG', 'SPGI', 'STE', 'STX', 'STZ', 'SWK', 'SWKS', 'SYK', 'TDG', 'TDY', 'TEL', 'TER', 'TFX', 'TGT', 'TMO', 'TROW', 'TRV', 'TSCO', 'TSLA', 'TTWO', 'TXN', 'TYL', 'UHS', 'ULTA', 'UNH', 'UNP', 'UPS', 'URI', 'V', 'VMC', 'VRSK', 'VRSN', 'VRTX', 'WAT', 'WHR', 'WLTW', 'WST', 'WYNN', 'XLNX', 'ZBH', 'ZBRA', 'ZTS'
    ,'AAPL', 'AMGN', 'AXP', 'BA', 'CAT', 'CRM', 'DIS', 'GS', 'HD', 'HON', 'JPM', 'MCD', 'MMM', 'MSFT', 'NKE', 'TRV', 'UNH', 'V'
    ,'AAPL', 'ADBE', 'ADI', 'ADP', 'ADSK', 'ALGN', 'AMAT', 'AMD', 'AMGN', 'AMZN', 'ANSS', 'ASML', 'AVGO', 'BIDU', 'BIIB', 'BKNG', 'CDNS', 'CDW', 'CHTR', 'COST', 'CPRT', 'CTAS', 'DLTR', 'DOCU', 'DXCM', 'EA', 'FB', 'GOOG', 'GOOGL', 'IDXX', 'ILMN', 'INTU', 'ISRG', 'JD', 'KLAC', 'LRCX', 'LULU', 'MAR', 'MELI', 'MRNA', 'MRVL', 'MSFT', 'MU', 'NFLX', 'NTES', 'NVDA', 'NXPI', 'OKTA', 'ORLY', 'PDD', 'PTON', 'PYPL', 'QCOM', 'REGN', 'ROST', 'SGEN', 'SPLK', 'SWKS', 'TEAM', 'TSLA', 'TXN', 'VRSK', 'VRSN', 'VRTX', 'WDAY', 'XLNX', 'ZM'
    ,'CAR', 'EXPD', 'FDX', 'JBHT', 'LSTR', 'NSC', 'UNP', 'UPS'
    ,'ARKG', 'ARKK', 'ARKW', 'BOIL', 'DIA', 'FAS', 'GUSH', 'IBB', 'IGV', 'IJH', 'IVV', 'IWB', 'IWF', 'IWM', 'IWN', 'IWO', 'JNUG', 'LABU', 'MDY', 'MTUM', 'OIH', 'QLD', 'QQQ', 'SMH', 'SOXL', 'SPXL', 'SPY', 'SSO', 'TAN', 'TECL', 'TNA', 'TQQQ', 'UPRO', 'VB', 'VOO', 'VTI', 'VUG', 'XBI', 'XLK', 'XLY', 'XOP']


    nasdaq100=['AAPL', 'ADBE', 'ADI', 'ADP', 'ADSK', 'AEP', 'ALGN', 'AMAT', 'AMD', 'AMGN', 'AMZN', 'ANSS', 'ASML', 'ATVI', 'AVGO', 'BIDU', 'BIIB', 'BKNG', 'CDNS', 'CDW', 'CERN', 'CHKP', 'CHTR', 'CMCSA', 'COST', 'CPRT', 'CSCO', 'CSX', 'CTAS', 'CTSH', 'DLTR', 'DOCU', 'DXCM', 'EA', 'EBAY', 'EXC', 'FAST', 'FB', 'FISV', 'FOX', 'FOXA', 'GILD', 'GOOG', 'GOOGL', 'IDXX', 'ILMN', 'INCY', 'INTC', 'INTU', 'ISRG', 'JD', 'KDP', 'KHC', 'KLAC', 'LRCX', 'LULU', 'MAR', 'MCHP', 'MDLZ', 'MELI', 'MNST', 'MRNA', 'MRVL', 'MSFT', 'MU', 'NFLX', 'NTES', 'NVDA', 'NXPI', 'OKTA', 'ORLY', 'PAYX', 'PCAR', 'PDD', 'PEP', 'PTON', 'PYPL', 'QCOM', 'REGN', 'ROST', 'SBUX', 'SGEN', 'SIRI', 'SPLK', 'SWKS', 'TCOM', 'TEAM', 'TMUS', 'TSLA', 
        'TXN', 'VRSK', 'VRSN', 'VRTX', 'WBA', 'WDAY', 'XEL', 'XLNX', 'ZM' ]

    dji=['AAPL', 'AMGN', 'AXP', 'BA', 'CAT', 'CRM', 'CSCO', 'CVX', 'DIS', 'DOW', 'GS', 'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'JPM', 'KO', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PG', 'TRV', 'UNH', 'V', 'VZ', 'WBA', 'WMT']

    djTransport=['AAL', 'ALK', 'CAR', 'CHRW', 'CSX', 'DAL', 'EXPD', 'FDX', 'JBHT', 'JBLU', 'KEX', 'LSTR', 'LUV', 'MATX', 'NSC', 'R', 'UAL', 'UNP', 'UPS' ]

    etf=['AAXJ', 'ACWI', 'ACWX', 'AGG', 'AGQ', 'AMLP', 'ANGL', 'ARKF', 'ARKG', 'ARKK', 'ARKW', 'ASHR', 'BDRY', 'BIL', 'BITO', 'BKLN', 'BLOK', 'BND', 'BNDX', 'BNO', 'BOIL', 'BOTZ', 'BSJM', 'BSV', 'CIBR', 'CTRU', 'CWB', 'CWEB', 'CWI', 'DBA', 'DBC', 'DBO', 'DFAC', 'DFEN', 'DGRO', 'DIA', 'DOG', 'DRIP', 'DRIV', 'DUST', 'DVY', 'DXD', 'DXJ', 'ECH', 'EEM', 'EFA', 'EFG', 'EFV', 'EMB', 'EMLC', 'ERX', 'ERY', 'ESGE', 'ESGU', 'EUFN', 'EWA', 'EWC', 'EWG', 'EWH', 'EWJ', 'EWL', 'EWS', 'EWT', 'EWU', 'EWW', 'EWY', 'EWZ', 'EZU', 'FALN', 'FAS', 'FAZ', 'FCG', 'FEZ', 'FLOT', 'FPE', 'FTXN', 'FVD', 'FXI', 'FXN', 'GDX', 'GDXJ', 'GLD', 'GLDM','GSG', 'GUSH', 'HDV', 'HNDL', 'HYEM', 'HYG', 'HYLB', 'IAU', 'IBB', 'ICLN', 'IDV', 'IEF', 'IEFA', 'IEI', 'IEMG', 'IGIB', 'IGLB', 'IGSB', 'IGV', 'IHI', 'IJH', 'IJR', 'ILF', 'INDA', 'ISTB', 'ITB', 'ITOT', 'IUSB', 'IUSG', 'IUSV', 'IVOL', 'IVV', 'IVW', 'IWB', 'IWD', 'IWF', 'IWM', 'IWN', 'IWO', 'IWP', 'IWR', 'IWS', 'IXC', 'IXUS', 'IYE', 'IYR', 'JDST', 'JETS', 'JMST', 'JNK', 'JNUG', 'JPST', 'KBE', 'KBWB', 'KOLD', 'KRBN', 'KRE', 'KWEB', 'LABD', 'LABU', 'LIT', 'LMBS', 'LQD', 'MBB', 'MCHI', 'MDY', 'META', 'MINT', 'MJ', 'MSOS', 'MTUM', 'MUB', 'NEAR', 'NUGT', 'OIH', 'PAVE', 'PCY', 'PDBC', 'PFF', 'PFFD', 'PGX', 'PSQ', 'QID', 'QLD', 'QQQ', 'QUAL', 'QYLD', 'RDVY', 'REET', 'RSP', 'RSX', 'RWM','RYLD', 'SARK', 'SCHD', 'SCHE', 'SCHF', 'SCHO', 'SCHP', 'SCHX', 'SCHZ', 'SCO', 'SCZ', 'SDOW', 'SDS', 'SGOL', 'SH', 'SHV', 'SHY', 'SHYG', 'SILJ', 'SJNK', 'SLV','SMH', 'SOXL', 'SOXS', 'SPAB', 'SPDW', 'SPEM', 'SPHB', 'SPIB', 'SPIP', 'SPLB', 'SPLG', 'SPLV', 'SPMB', 'SPMD', 'SPSB', 'SPSM', 'SPTI', 'SPTL', 'SPTM', 'SPXL', 'SPXS', 'SPXU', 'SPY', 'SPYD', 'SPYG', 'SPYV', 'SQQQ', 'SRLN', 'SRTY', 'SSO', 'STIP', 'SVXY', 'TAN', 'TBF', 'TBT', 'TECL', 'TIP', 'TIPX', 'TLT', 'TMF', 'TMV','TNA', 'TOTL', 'TQQQ', 'TWM', 'TZA', 'UDOW', 'UNG', 'UPRO', 'URA', 'USHY', 'USMV', 'USO', 'UUP', 'UVXY', 'UWM', 'VB', 'VCIT', 'VCLT', 'VCSH', 'VDE', 'VEA','VEU', 'VGIT', 'VGK', 'VGLT', 'VGSH', 'VIG', 'VIXY', 'VLUE', 'VMBS', 'VNQ', 'VOO', 'VPL', 'VT', 'VTEB', 'VTI', 'VTIP', 'VTV', 'VTWO', 'VUG', 'VV', 'VWO', 'VXUS', 'VYM', 'XBI', 'XHB', 'XLB', 'XLC', 'XLE', 'XLF', 'XLI', 'XLK', 'XLP', 'XLRE', 'XLU', 'XLV', 'XLY', 'XME', 'XOP', 'XRT', 'YANG', 'YINN']
   

    s_p_500=['A', 'AAL', 'AAP', 'AAPL', 'ABBV', 'ABC', 'ABMD', 'ABT', 'ACN', 'ADBE', 'ADI', 'ADM', 'ADP',
             'ADSK', 'AEE', 'AEP', 'AES', 'AFL', 'AIG', 'AIZ', 'AJG', 'AKAM', 'ALB', 'ALGN', 'ALK', 'ALL',
             'ALLE', 'AMAT', 'AMCR', 'AMD', 'AME', 'AMGN', 'AMP', 'AMT', 'AMZN', 'ANET', 'ANSS', 'ANTM', 'AON',
             'AOS', 'APA', 'APD', 'APH', 'APTV', 'ARE', 'ATO', 'ATVI', 'AVB', 'AVGO', 'AVY', 'AWK', 'AXP', 'AZO',
             'BA', 'BAC', 'BAX', 'BBWI', 'BBY', 'BDX', 'BEN', 'BIIB', 'BIO', 'BK', 'BKNG', 'BKR', 'BLK', 'BLL',
             'BMY', 'BR', 'BSX', 'BWA', 'BXP', 'C', 'CAG', 'CAH', 'CARR', 'CAT', 'CB', 'CBOE', 'CBRE', 'CCI',
             'CDNS', 'CDW', 'CE', 'CERN', 'CF', 'CFG', 'CHD', 'CHRW', 'CHTR', 'CI', 'CINF', 'CL', 'CLX', 'CMA', 'CMCSA',
             'CME', 'CMG', 'CMI', 'CMS', 'CNC', 'CNP', 'COF', 'COO', 'COP', 'COST', 'CPB', 'CPRT', 'CRL', 'CRM', 'CSCO',
             'CSX', 'CTAS', 'CTLT', 'CTRA', 'CTSH', 'CTVA', 'CTXS', 'CVS', 'CVX', 'CZR', 'D', 'DAL', 'DD', 'DE', 'DFS',
             'DG', 'DGX', 'DHI', 'DHR', 'DIS', 'DISCA', 'DISCK', 'DISH', 'DLR', 'DLTR', 'DOV', 'DOW', 'DPZ', 'DRE',
             'DRI', 'DTE', 'DUK', 'DVA', 'DVN', 'DXC', 'DXCM', 'EA', 'EBAY', 'ECL', 'ED', 'EFX', 'EIX', 'EL', 'EMN', 'EMR', 'ENPH', 'EOG', 'EQIX', 'EQR', 'ES', 'ESS', 'ETN', 'ETR', 'ETSY', 'EVRG', 'EW', 'EXC', 'EXPD', 'EXPE', 'EXR', 'F', 'FANG', 'FAST', 'FB', 'FBHS', 'FCX', 'FDX', 'FE', 'FFIV', 'FIS', 'FISV', 'FITB', 'FLT', 'FMC', 'FOX', 'FOXA', 'FRC', 'FRT', 'FTNT', 'FTV','GD', 'GE', 'GILD', 'GIS', 'GL', 'GLW', 'GM', 'GNRC', 'GOOG', 'GOOGL', 'GPC', 'GPN', 'GPS', 'GRMN', 'GS', 'GWW', 'HAL', 'HAS', 'HBAN', 'HBI',
             'HCA', 'HD', 'HES', 'HIG', 'HII', 'HLT', 'HOLX', 'HON', 'HPE', 'HPQ', 'HRL', 'HSIC', 'HST', 'HSY', 'HUM', 'HWM', 'IBM', 'ICE', 'IDXX', 'IEX', 'IFF', 'ILMN', 'INCY', 'INFO','INTC', 'INTU', 'IP', 'IPG', 'IPGP', 'IQV', 'IR', 'IRM', 'ISRG', 'IT', 'ITW', 'IVZ', 'J', 'JBHT', 'JCI', 'JKHY', 'JNJ', 'JNPR', 'JPM', 'K', 'KEY', 'KEYS', 'KHC', 'KIM', 'KLAC', 'KMB', 'KMI', 'KMX', 'KO', 'KR', 'L', 'LDOS', 'LEG', 'LEN', 'LH', 'LHX', 'LIN', 'LKQ', 'LLY', 'LMT', 'LNC', 'LNT', 'LOW', 'LRCX', 'LUMN', 'LUV', 'LVS', 'LW', 'LYB', 'LYV', 'MA', 'MAA', 'MAR', 'MAS', 'MCD', 'MCHP', 'MCK', 'MCO', 'MDLZ', 'MDT', 'MET', 'MGM', 'MHK', 'MKC', 'MKTX', 'MLM', 'MMC', 'MMM', 'MNST', 'MO', 'MOS', 'MPC', 'MPWR', 'MRK', 'MRO', 'MS', 'MSCI', 'MSFT', 'MSI', 'MTB', 'MTD', 'MU', 'NCLH', 'NDAQ', 'NEE',
             'NEM', 'NFLX','NI', 'NKE', 'NLOK', 'NLSN', 'NOC', 'NOV', 'NOW', 'NRG', 'NSC', 'NTAP', 'NTRS', 'NUE', 'NVDA', 'NVR', 'NWL', 'NWS', 'NWSA',
             'NXPI', 'ONL', 'ODFL', 'OGN', 'OKE','OMC', 'ORCL', 'ORLY', 'OTIS', 'OXY', 'PAYC', 'PAYX', 'PBCT', 'PCAR', 'PEAK', 'PEG', 'PENN',
             'PEP', 'PFE', 'PFG', 'PG', 'PGR', 'PH', 'PHM', 'PKG', 'PKI', 'PLD', 'PM', 'PNC', 'PNR', 'PNW', 'POOL', 'PPG', 'PPL', 'PRGO', 'PRU',
             'PSA', 'PSX', 'PTC', 'PVH', 'PWR', 'PXD', 'PYPL', 'QCOM', 'QRVO', 'RCL', 'RE', 'REG', 'REGN', 'RF', 'RHI', 'RJF', 'RL', 'RMD', 'ROK',
             'ROL', 'ROP', 'ROST', 'RSG', 'RTX', 'SBAC', 'SBUX', 'SCHW', 'SEE', 'SHW', 'SIVB', 'SJM', 'SLB', 'SNA', 'SNPS', 'SO', 'SPG', 'SPGI',
             'SRE', 'STE', 'STT', 'STX', 'STZ', 'SWK', 'SWKS', 'SYF', 'SYK', 'SYY', 'T', 'TAP', 'TDG', 'TDY', 'TEL', 'TER', 'TFC', 'TFX', 'TGT',
             'TJX', 'TMO', 'TMUS', 'TPR', 'TRMB', 'TROW', 'TRV', 'TSCO', 'TSLA', 'TSN', 'TTWO', 'TWTR', 'TXN', 'TXT', 'TYL', 'UA', 'UAA', 'UAL',
             'UDR', 'UHS', 'ULTA', 'UNH', 'UNM', 'UNP', 'UPS', 'URI', 'USB', 'V', 'VFC', 'VIAC', 'VLO', 'VMC', 'VNO', 'VRSK', 'VRSN', 'VRTX', 'VTR',
             'VTRS', 'VZ', 'WAB', 'WAT', 'WBA', 'WDC', 'WEC', 'WELL', 'WFC', 'WHR', 'WLTW', 'WM', 'WMB', 'WMT', 'WRB', 'WRK', 'WST', 'WU', 'WY', 'WYNN',
             'XEL', 'XLNX', 'XOM', 'XRAY', 'XYL', 'YUM', 'ZBH', 'ZBRA', 'ZION', 'ZTS' ]


##    allnn=np.unique(allnnp)
    alln=['CAR', 'EXPD', 'FDX', 'JBHT', 'LSTR', 'NSC', 'UNP', 'UPS','googl']
    gg6=nasdaq100
    

    
    

    dd=['tsla']
    pp_buy=[]
    pp_sell=[]


    
    

    print('# of stocks being checked: ',len(gg6),'  ', inspect.getframeinfo(inspect.currentframe()).lineno)
    i=0
    i2=0
    x6=0
    
    


##    gg6=[dji,allnnp,all,nasdaq100,djTransport,etf,s_p_500,alln]

    
    for x in gg6: # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
        dfqq=pd.DataFrame()
        dfq=pd.DataFrame()
        x5=[]
        print(i, x, gg6[i])
        df=yf.Ticker(gg6[i]).history(period ='4d', interval = '1m',prepost = False)
        df=df.drop(columns=[ 'Dividends', 'Stock Splits'])
##        df=pd.DataFrame(df)


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

        df['squeeze_on'] =''
        df['cross']=''
        df['mama_fama']=''
        df['DM_delta']=''
        df['DI_delta']=''
        df['open_close']=''
##        if df['Open']-df['Close']>0:
##            df['Lowx']=df['Open']-df['Close']
##            df['Highx']=df['High']-df['Close']
##        elif  df['Open']-df['Close']<0:
##            df['Lowx']=df['Close']-df['Low']
##            df['Highx']=df['Close']-df['High']

##        df['EMA-35']=0
##        df['EMA-510']=0
##        df['EMA-1021']=0
##        df['EMA-2150']=0 
##        df['EMA_3_vwap']=0 
##        df['EMA_5_vwap']=0  
##        df['EMA_10_vwap']=0
##        df['EMA_21_vwap']=0 
##        df['EMA_50_vwap']=0 
##        df['macdsignal']=0  
##        df['Close_EMA3']=0 
##        df['Close_EMA5']=0  
##        df['Close_EMA10']=0 
##        df['Close_EMA21']=0
##        df['Close_EMA50']=0  
##        df['Close_vwap']=0 
        

        p=0
        for z in df.index:
            df['DM_delta'].loc[z]=df['PLUS_DM'].loc[z]-df['MINUS_DM'].loc[z]
            df['DI_delta'].loc[z]=df['PLUS_DI'].loc[z]-df['MINUS_DI'].loc[z]

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
                
                
                                                               

               
                
                

##            if df['EMA-35'].loc[z] > 0:
##                df['EMA-35'].loc[z]='up'
##                
##            if df['EMA-510'].loc[z] > 0:
##                df['EMA-510'].loc[z]='up'
##                
##            if df['EMA-1021'].loc[z] > 0:
##                df['EMA-1021'].loc[z]='up'
##            if df['EMA-2150'].loc[z] > 0:
##                df['EMA-2150'].loc[z]='up'
##            if df['EMA_3_vwap'].loc[z] > 0:
##                df['EMA_3_vwap'].loc[z]='up'
##            if df['EMA_5_vwap'].loc[z] > 0:
##                df['EMA_5_vwap'].loc[z]='up'
##            if df['EMA_10_vwap'].loc[z] > 0:
##                df['EMA_10_vwap'].loc[z]='up'
##                
##            if df['EMA_21_vwap'].loc[z] > 0:
##                df['EMA_21_vwap'].loc[z]='up'
##            if df['EMA_50_vwap'].loc[z] > 0:
##                df['EMA_50_vwap'].loc[z]='up'
##            if df['macdsignal'].loc[z] > 0:
##                df['macdsignal'].loc[z]='up'
##            if df['Close_EMA3'].loc[z] > 0:
##                df['Close_EMA3'].loc[z]='up'
##            if df['Close_EMA5'].loc[z] > 0:
##                df['Close_EMA5'].loc[z]='up'
##            if df['Close_EMA10'].loc[z] > 0:
##                df['Close_EMA10'].loc[z]='up'
##            if df['Close_EMA21'].loc[z] > 0:
##                df['Close_EMA21'].loc[z]='up'
##            if df['Close_EMA50'].loc[z] > 0:
##                df['Close_EMA50'].loc[z]='up'
##                
##            if df['Close_vwap'].loc[z] > 0 :
##                df['Close_vwap'].loc[z]='up'


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
##                print(x,"  in 1 min Squeeze, ATR=",df['ATR'].loc[z])
##            else:
##                df['squeeze_on'].loc[z]=' '


##            if df['upper_band'].loc[z] > df['upper_keltner'].loc[z]:
##                df['cross'].loc[z]='up'+str(df['EMA-35'].loc[z])
##            elif df['upper_band'].loc[z] < df['upper_keltner'].loc[z]:
##                df['cross'].loc[z]='down'+str(df['EMA-35'].loc[z])

            if df['EMA-35'].loc[z] > 0:
                df['cross'].loc[z]='up'+str(df['macd'].loc[z])
            elif df['EMA-35'].loc[z] < 0:
                df['cross'].loc[z]='down'+str(df['macd'].loc[z])  
                
                

        if p > 0:
            print(x,' Squeeze Alert','  ','lineno',  inspect.getframeinfo(inspect.currentframe()).lineno)
      

        
    

        
        df=df[df.index.astype(str).str.contains('2021-12-17')]
        df = df.dropna(axis=0, how='all')
##        print(df)
##        print(df[df['column name'].isnull()])

        df['ticker']=x
##        for s in df.index:
##            df['ticker'].loc
            

        df3=df.tail(3)



           
 
        
        mm=df3['ATR'].mean()
        nn=df3['Close'].mean()
        nn2=df3['Close_EMA3'].mean()
        nn3=df3['Close_EMA5'].mean()
        nn4=df3['Close_vwap'].mean()
        nn5=df3['EMA_3'].mean()
        nn6=df3['EMA_5'].mean()
        nn7=df3['adx'].mean()
        
        i=i+1
        print(x,'no ',i, 'of', len(gg6))

        if mm > 2 and nn7 > 25 :
            
            print(x,' match')
##            and nn2>0 and nn3>0 and nn4>0 and nn5>0 and nn6>0 and
            
                
    ##
    ##
    ##
    ##            
    ##            print(mm)
    ##        df3=df3[df3['Close'].astype(str)[-1]> '5']
            
    ##    print(df)
    ##        df=df[df['Close'][-1] >= 5]
    ##        print(x,'   ',df)
##            sys.exit()

    ####################################################
    ##        df['VZO']=f.TA.VZO(df)
    ##        df['ZLEMA']=f.TA.ZLEMA(df)
    ##        df['KAMA']=f.TA.KAMA(df)
    ##        df['MOBO']=f.TA.MOBO(df)
    ##        df['TSI']=f.TA.TSI(df)
    ##        df['EBBP']=f.TA.EBBP(df)
    ##        df['BASP']=f.TA.BASP(df)
    ##        df['CHANDELIER']=f.TA.CHANDELIER(df)
    ##        df['STC']=f.TA.STC(df)
    ##        df['FISH']=f.TA.FISH(df)
    ##        df['SQZMI']=f.TA.SQZMI(df)
            
            
            #print(df,'mmmmmmmmmmm')
            


    ###################################################
            tick=x
    ##        if df.empty==True:
    ##            pass
            
    ##        print(df)


            


        


            df=df[df.index.astype(str).str.contains('2021-12-17')]
##            df['High'].dropna(axis=0, how='all')
##            df['Low'].dropna(axis=0, how='all')
##            df = df['High'].dropna(axis=0, how='all')
            print(x,'  ',df)






            

            
            



    ##        real = AD(high, low, close, volume)  #AD - Chaikin A/D Line # https://mrjbq7.github.io/ta-lib/func_groups/volume_indicators.html
    ##        real = ADOSC(high, low, close, volume, fastperiod=3, slowperiod=10) #ADOSC - Chaikin A/D Oscillator
    ##        real = DX(high, low, close, timeperiod=14)
    ##        real = DEMA(close, timeperiod=30)
    ##        real = HT_DCPERIOD(close)
    ##        real = HT_DCPHASE(close)
    ##        real = CMO(close, timeperiod=14)
    ##        real = KAMA(close, timeperiod=30)
    ##        real = PLUS_DI(high, low, close, timeperiod=14)
    ##        real = MINUS_DI(high, low, close, timeperiod=14)
    ##        real = PLUS_DM(high, low, timeperiod=14)
    ##        real = MINUS_DM(high, low, timeperiod=14)
    ##        https://pythonrepo.com/repo/twopirllc-pandas-ta-python-deep-learning#pandas-ta-strategy
    ##        https://stackoverflow.com/questions/28477222/python-pandas-calculate-ichimoku-chart-components

            df['delta_Close_1day']=df['Close']-df['Close'].shift(1)
            df['delta_open_1day']=df['Open']-df['Open'].shift(1)
            df['delta_Low_1day']=df['Low']-df['Low'].shift(1)
            df['delta_High_1day']=df['High']-df['High'].shift(1)
            
            

      

    ###############################################        

    ##        print(df)


                
##            df=df[['ticker','mama','fama','mama_fama',
##                   'KAMA', 'ADOSC','DEMA','HT_DCPERIOD','HT_DCPHASE','CMO','KAMA','DI_delta','DM_delta',
##
##
##                   'Red','AD','adx','ATR','fastk','fastd','squeeze_on','macd_slope','cross','Open','Close','Low','High','signal',
##                   'delta_Close_1day','delta_open_1day','delta_Low_1day','delta_High_1day',
##                   'x',
##                   'SARx','EMA-35','aroondown','aroonup','CCI','MOM','MOM_slope',\
##                   'Boling_upper','Boling_lower2','SAR',
##    ##               'CCI','ATR','MOM','MOM_slope',\
##                   'ADX_over25_strong_less25_weak_trend',\
##                   'macd', 'macdsignal', 'macdhist',
##    ##               'EMA-35',
##                   'EMA_3','EMA_5','EMA_21','EMA_10','EMA_50',
##                    'aroondown','aroonup','RSI','vwap','TR',
##                   
##                   'EMA-35','EMA-510','EMA-1021','EMA-2150',
##                   
##                   'Close_EMA3','Close_EMA5','Close_EMA10','Close_EMA21','Close_EMA50','EMA_3_vwap','EMA_5_vwap','EMA_10_vwap','EMA_21_vwap','EMA_50_vwap',
##                   'Close_vwap','LINEARREG','LINEARREG_ANGLEG','LINEARREG_INTERCEPT','LINEARREG_SLOPE','TSF'
##
##    ##               ,,,,,,'macd_35'
##                   
##                   
##            
##                   ]]

    ##        df=df[df['Close'].mean(axis=0, skipna=True) > 1]

    ##        df['EMA-35']=df['EMA_3']-df['EMA_5']
    ##        df['EMA-510']=df['EMA_5']-df['EMA_10']
    ##        df['EMA-1021']=df['EMA_10']-df['EMA_21']
    ##        df['EMA-2150']=df['EMA_21']-df['EMA_50']
    ##        df['EMA_3_vwap']=df['EMA_3']-df['vwap']
    ##        df['EMA_5_vwap']=df['EMA_5']-df['vwap']
    ##        df['EMA_10_vwap']=df['EMA_10']-df['vwap']
    ##        df['EMA_21_vwap']=df['EMA_21']-df['vwap']
    ##        df['EMA_50_vwap']=df['EMA_50']-df['vwap']
    ##        df['macd_35'], df['macdsignal'], df['macdhist'] = ta.MACD(df['Close'], fastperiod=3, slowperiod=5, signalperiod=3)
    ##        df['Close_EMA3']=df['Close']-df['EMA_3']
    ##        df['Close_EMA5']=df['Close']-df['EMA_5']
    ##        df['Close_EMA10']=df['Close']-df['EMA_10']
    ##        df['Close_EMA21']=df['Close']-df['EMA_21']
    ##        df['Close_EMA50']=df['Close']-df['EMA_50']
    ##        df['Close_vwap']=df['Close']-df['vwap']        

##            print(df3,'\n',x)
##            print('\n')
##            print(df,'\n',x)
    ##        sys.exit()
            df4=pd.DataFrame()
            df5=pd.DataFrame()
##            df3=df
            g6=pd.DataFrame()
            g7=pd.DataFrame()

            i2='53'
            ##        SAR reversal
            df.reset_index(inplace=True)
            

            m2=[];m3=[];m4=[]

##            print(df.columns,' line 625  ')

                  
            for x in df.index:
                
                
    ##            print(df['EMA-35'].loc[x])

    ## ***************************************************************************************************
    ## ***************************************************************************************************
    ## ***************************************************************************************************
    ## ***************************************************************************************************              
    #################### case 1 #########################            
    ##            # Buy condition
    ##            uu3=df['Low'].loc[x] > df['EMA_3'].loc[x] and\
    ##                 df['Low'].loc[x] > df['Low'].shift(1).loc[x] and\
    ##                 df['EMA_3'].loc[x] > df['EMA_5'].loc[x] and\
    ##                 df['EMA_5'].loc[x] > df['EMA_10'].loc[x]and\
    ##                 df['EMA_10'].loc[x] > df['EMA_21'].loc[x] and\
    ##                 df['EMA_21'].loc[x] > df['EMA_50'].loc[x] and\
    ##                 df['Low'].loc[x] > df['EMA_10'].loc[x] and\
    ##                 df['Low'].loc[x] > df['EMA_21'].loc[x]and\
    ##                 df['Low'].loc[x] > df['EMA_50'].loc[x] and\
    ##                 df['Low'].loc[x] > df['vwap'].loc[x] and\
    ##                 df['EMA_3'].loc[x] > df['vwap'].loc[x] and\
    ##                 df['EMA_5'].loc[x] > df['vwap'].loc[x]and\
    ##                 df['EMA_10'].loc[x] > df['vwap'].loc[x] and\
    ##                 df['EMA_21'].loc[x] > df['vwap'].loc[x] and\
    ##                 df['EMA_50'].loc[x] > df['vwap'].loc[x]

    ##
    ##            uu3=df['Low'].loc[x] > df['EMA_3'].loc[x] and\
    ##                 df['Low'].loc[x] > df['Low'].shift(1).loc[x] and\
    ##                 df['EMA_3'].loc[x] > df['EMA_5'].loc[x] and\
    ##                 df['EMA_5'].loc[x] > df['EMA_10'].loc[x]and\
    ##                 df['EMA_10'].loc[x] > df['EMA_21'].loc[x] and\
    ##                 df['EMA_3'].loc[x] > df['vwap'].loc[x] and\
    ##                 df['EMA_5'].loc[x] > df['vwap'].loc[x]and\
    ##                 df['EMA_10'].loc[x] > df['vwap'].loc[x] and\
    ##                 df['EMA_21'].loc[x] > df['vwap'].loc[x] and\
    ##                 df['EMA_50'].loc[x] > df['vwap'].loc[x]

                uu3=df['MOM'].loc[x]-df['MOM'].shift(1).loc[x] > 0 and\
                     df['macd'].loc[x]>0 and df['adx'].loc[x]>24 and df['ATR'].loc[x]>.9 and df['TR'].loc[x]>.5   # Algo 2.2b,orig 
                

                
    ##                df['Low'].loc[x] > df['EMA_3'].loc[x] 
    ##                df['MOM'].loc[x]-df['MOM'].shift(1).loc[x] > 2 and\ 
    ##                df['Low'].loc[x] > df['Low'].shift(1).loc[x] and\
    ##                df['EMA_3'].loc[x] > df['EMA_5'].loc[x] and\
    ##                df['EMA_5'].loc[x] > df['EMA_10'].loc[x]and\
    ##                df['EMA_3'].loc[x] > df['vwap'].loc[x] and\
    ##                df['EMA_5'].loc[x] > df['vwap'].loc[x] 

    ##
    ##            uu3=
    ##            df['MOM'].loc[x] > 0 and df['EMA-35'].loc[x] >0 and\
    ##                 df['EMA-35'].shift(1).loc[x]<0 and df['EMA-35'].shift(2).loc[x]<0 and df['EMA-35'].shift(3).loc[x]<0 and\
    ##            uu3= df['macd'].loc[x]>0 and\
    ##                 df['macd'].shift(1).loc[x]>0 and df['macd'].shift(2).loc[x]<0 and df['macd'].shift(3).loc[x]<0
    ######                 
    ##                 
                           
    ## ***************************************************************************************************
    ## ***************************************************************************************************
    ## ***************************************************************************************************
    ## ***************************************************************************************************  
        #########################################################################################################################################################


                if i2=='53':    # Buy algoritham

                    if uu3:
                        t_buy=df['Datetime'].loc[x]
                        df['signal'].loc[x]='buymmmmmmmmmmm'



        ##            if df['aroonup'].loc[x] == 100:
        ###############################################################################################################################################                
        ##                print(i2,' Sell %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
                        v5=df['Close'].loc[x] #v5 is buy
                        v6=df['CCI'].loc[x]
##                        print('\n\n')
##                        print('**************************************************************************************************************','\n')
##                        print(df3,'\n',df3.iloc[-1,1],'  ','df3 buy signal condition met','  ', inspect.getframeinfo(inspect.currentframe()).lineno)
##                        print('\n')
##                        print(df,'\n',df.iloc[-1,1],'df buy signal condition met','  ', inspect.getframeinfo(inspect.currentframe()).lineno)
    ##                    print(df,'buy ',tick)
            ##                    profit=(v5-v4)

                        i2='51'

        ######################################################################################################################################

    ##        for x in df.index:
                if i2=='51':
                    
                    
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

                    mm3='Close_vwap'
                    sell=(df[mm3].loc[x] < 0 and (df[mm3].loc[x]-df[mm3].shift(1).loc[x] <00)\
                          and df['Close'].loc[x] > v5 )  # original

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

##                        print('\n\n')
                        print('**************************************************************************************************************')


##                        print(df3.columns)


##                        print(df3,'\n',df3.iloc[-1,1],'  ','[df3] buy signal condition met @',v5,'   line no:', inspect.getframeinfo(inspect.currentframe()).lineno)
##                        print('\n\n')
##                        print(df3.columns)
##                        print(df,'\n',df.iloc[-1,1],'   ','[df] buy signal condition met @',v5,'  line no:', inspect.getframeinfo(inspect.currentframe()).lineno)
                        df['signal'].loc[x]='selllllllllllllllll'
                        dfqq=dfqq.append(df3)

      
                        k=k+1
                        t_sell=df['Datetime'].loc[x]

    ##                    df['signal'].loc[x]=="sellmjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj"
                        
##                        print('\n\n')
                        i2='53'
                 
                        v4=df['Close'].loc[x]   # v4 is sell


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

    
            

    else:
        pass


    

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
        
ss=[]
s5(ss)
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





