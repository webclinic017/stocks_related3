import yfinance as yf
import mplfinance as mpf
import yfinance as yf, datetime as dt
import pandas as pd
import  datetime as dt
import json

##ticker=input("Enter stock ticker: ")

ticker='amzn'
no_of_days=180

df = pd.DataFrame()


start = dt.datetime.today() - dt.timedelta(no_of_days)


end = dt.datetime.today()


df = yf.download(ticker, start, end)
'''
print(df)

df.fillna(method='bfill', axis=0, inplace=True)    
df['200-day Exponential MA'] = df['Adj Close'].ewm(span=200, adjust=False).mean()
df['100-day Exponential MA'] = df['Adj Close'].ewm(span=100, adjust=False).mean()
df['50-day Exponential MA'] = df['Adj Close'].ewm(span=50, adjust=False).mean()

df['20-day Exponential MA'] = df['Adj Close'].ewm(span=20, adjust=False).mean()
df['10-day Exponential MA'] = df['Adj Close'].ewm(span=10, adjust=False).mean()
df['3-day Exponential MA'] = df['Adj Close'].ewm(span=3, adjust=False).mean()

##    df['200-day Exponential MA'] = df['Adj Close'].ewm(span=200, adjust=False).mean()
##    df['100-day Exponential MA'] = df['Adj Close'].ewm(span=200, adjust=False).mean()
##    df['50-day Exponential MA'] = df['Adj Close'].ewm(span=50, adjust=False).mean()
print(df)
##    mpf.plot(df, volume=True, tight_layout=True, style="yahoo", type="candle", mav=(3,5,7,13,50),title=ticker+' - ('+perd + ' - '+intervl+')')
##    mpf.plot(df, volume=True, tight_layout=True, style="yahoo", type="candle", mav=(3,5,7,13,50),title=ticker +' (Daily)',show_nontrading=True)

mpf.plot(df, volume=True, tight_layout=True, style="yahoo", type="candle", mav=(200,100,50,20,10,3),title=ticker +' (Daily)',show_nontrading=True)
##    df.plot()
##################################
perd='3d'
intervl='1m'
dfi = pd.DataFrame()
##    ticker='amc'
print('--- Running ---')
### [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]
##
####g=input("Enter Ticker :")
###perd=input("Enter no of days '5d','2d','1d' :")
###intervl=input("Enter mins '5m','1m' :")
##
##
###df=pd.DataFrame()
###Interval required 5 minutes
data = yf.download(tickers=ticker, period=perd, interval=intervl)
dfi=pd.DataFrame(data)
print(dfi)

##    intraday = pd.read_csv('examples/data/SP500_NOV2019_IDay.csv',index_col=0,parse_dates=True)

##    intraday = intraday.drop('Volume',axis=1) # Volume is zero anyway for this intraday data set
##    print(intraday.index)
##    intraday.index.name = 'Datetime'
##    print(intraday.index)
##    intraday.shape
##    intraday.head(3)
##    intraday.tail(3)
##
##
####    iday = intraday.loc[1:30,:]
iday = dfi.loc[:,:]
##    iday = intraday.loc[:63,:]
print(iday)

##    mpf.plot(iday, type='candle', volume=True, figratio=(15, 15), style='yahoo', mav=(200,100,50,20,10,3), title=ticker+' - ('+perd + ' - '+intervl+')')
mpf.plot(iday, type='candle', volume=True, figratio=(15, 15), style='yahoo', mav=(200,100,50,20,10,3), title=ticker+' oo')
'''
