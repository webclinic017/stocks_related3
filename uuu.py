import yfinance as yf
import pandas as pd
m = yf.Ticker("MSFT")
df=pd.DataFrame(m.cashflow)
print(df.head(3))
df=df.reset_index()
print(df.iloc[4,0])


##tickers = gt.get_tickers()
##print(tickers[:5])


##import requests
##key = '2DHC1EFVR3EOQ33Z' # free key from https://www.alphavantage.co/support/#api-key -- no registration required
##result = requests.get('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=NKLA&apikey='+ key).json()
##
##print(f'The price for NKLA right now is ${result["Global Quote"]["05. price"]}.')

##print(list_of_tickers)

##from yahoo_finance import Share
##h=Share('T')
##yahoo = Share('A')
##print (yahoo.get_open())
##print (yahoo.get_price())
##print (yahoo.get_trade_datetime())




##import backtrader as bt
##import datetime as datetime
####import YahooFinanceData
##
##if __name__ == '__main__':
##    cerebro = bt.Cerebro()
##    cerebro.broker.setcash(1337.0)
##
##    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
##
##    cerebro.run()
##
##    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

## 

##data = bt.feeds.YahooFinanceData(dataname='AAPL',
##                                  fromdate=datetime(2017, 1, 1),
##                                  todate=datetime(2017, 12, 31))



##from get_all_tickers import get_tickers as gt
##from get_all_tickers.get_tickers import Region
### tickers of all exchanges
##hh()
