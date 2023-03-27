import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

import matplotlib.animation as ani
import matplotlib.pyplot as plt2
import numpy as np
import pandas as pd
import yfinance as yf
import pandas as pd
import datetime as dt
import sys
import Technicals
from Technicals import Techinicalsbb
import warnings
warnings.filterwarnings("ignore")

import pandas
from sklearn import linear_model
from sklearn import naive_bayes


def p2(ticker,n5):
    import warnings

    
    warnings.filterwarnings("ignore")
    
    #######################################################################

    df = yf.download(ticker, period='300d', interval='1d',prepost = False)
    df=pd.DataFrame(df)


    df=df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]
    df.columns=['open', 'high', 'low', 'close', 'adj Close', 'volume']
    df=Technicals.Techinicalsbb(df)
##    print(df.columns)
    df=df[['open', 'high', 'low', 'close', 'adj Close', 'volume','SAR','ADX','TRIX','EMA_100','EMA_200','EMA_50','EMA_10','EMA_21','CCI','RSI','VZO',\
           'MFI','ROC']]

    df.index = pd.to_datetime(df.index)
    ##df.dropna()
    df=df[200:]
##    print(df.head(3))
    ##x=df.index
    ##y=df[['close','vwap','EMA_100','EMA_200','EMA_50','EMA_5','EMA_10','EMA_21','SAR','volume','red']]

    from datetime import datetime
    from datetime import date


    d=str(df.index[0]).split(' ')[0]
    d2 = datetime.strptime(d, '%Y-%m-%d')
    d3=datetime.date(d2)
    import sys
    print(df.shape,' df.shape')


    #######################################################################
    ##df = pandas.read_csv("cars.csv")
##    print(df['close'][0],' xxxx ',df['open'][-2],'  ', df['volume'][-2], '   ',df['SAR'][-2],' gggg ',df['close'][-1])

    X = df[['open', 'volume','low','high','SAR','ADX','TRIX','EMA_100','EMA_200','EMA_50','EMA_10','EMA_21','CCI','RSI','VZO','MFI','ROC']]
    y = df['close']

    X=df.iloc[:,:-1].values
    

    

    regr = linear_model.LinearRegression()
