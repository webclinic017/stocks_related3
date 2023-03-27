import os
from binance.client import Client
import pandas as pd
import ccxt
import logging
import sys
import websocket, json, pprint, talib, numpy

pd.options.display.width = 0
pd.set_option('display.max_columns', None)
pd.options.display.float_format = '{:.2f}'.format
##pd.options.display.max_columns=255
pd.options.display.max_rows=6500000
pd.set_option('display.max_colwidth', 500)
pd.set_option('display.max_columns', 550)
pd.options.mode.chained_assignment = None  # default='warn'

# https://github.com/binance/binance-public-data/tree/master/python
########################################################

from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

x1='y9SvMHSmcHMw7wrGBF5SLKRGYBU8VjOJkGdwkN9XrnPelKeBcqXhyNKt28LDPxxG'
y1='BsKSkRvqtbvo2gmV5Brgjc3CujV724vfDCSuTES9DfhaZdVxQmR293tjtYVdTFcO'
####client = RequestClient(api_key=x1, secret_key=y1, https://fapi.binance.com')
##client = Client(x1, y1, url='https://testnet.binancefuture.com')
##client = SubscriptionClient(api_key=x1, secret_key=y1, uri='wss://fstream.binance.com/ws')
client = Client('y9SvMHSmcHMw7wrGBF5SLKRGYBU8VjOJkGdwkN9XrnPelKeBcqXhyNKt28LDPxxG', 'BsKSkRvqtbvo2gmV5Brgjc3CujV724vfDCSuTES9DfhaZdVxQmR293tjtYVdTFcO'
                , tld='us')

prices = client.get_all_tickers()
print(prices)
df=pd.DataFrame(prices)
pp=[]
##print(df['symbol'].shape[0])
for x in range(df['symbol'].shape[0]):
    pp.append(df['symbol'][x])
##print(df)
print(pp)
for x in pp:
    info = client.get_symbol_info(x)
    print('\n\n\n')
    print(info)
##for x in info:
##    print(x, '   ',info[x])
##################################################################3
##info = client.get_all_tickers()
##df=pd.DataFrame(info)
##pp=[]
####print(df['symbol'].shape[0])
##for x in range(df['symbol'].shape[0]):
##    pp.append(df['symbol'][x])
####print(df)
##print(pp)
##
##sys.exit()
######################################################################

############################################## start of play area #####################################3
##
##import requests 
##import json 
##import pandas as pd 
##import numpy as np  
##import datetime as dt  
##
####frequency = input("Please enter the frequency (1m/5m/30m/.../1h/6h/1d/ :  ")
##frequency ='1d'
##def get_bars(symbol):
##    frequency ='1d'
##    root_url = 'https://api.binance.com/api/v1/klines'
##    url = root_url + '?symbol=' + symbol + '&interval=' + interval
##    data = json.loads(requests.get(url).text)
##    df = pd.DataFrame(data)
##    df.columns = ['open_time',
##                  'open', 'high', 'low', 'close', 'volume',
##                  'close_time', 'qav', 'num_trades',
##                  'taker_base_vol', 'taker_quote_vol', 'ignore']
##    df.index = [dt.datetime.fromtimestamp(x / 1000.0) for x in df.close_time]
##    df['ticker']=''
##    for x in df.index:
##        df['ticker'].loc[x]=symbol
##
##    df=df[['ticker',  'open_time',
##                  'open', 'high', 'low', 'close', 'volume',
##                  'close_time', 'qav', 'num_trades',
##                  'taker_base_vol', 'taker_quote_vol', 'ignore']]  
##    return df
##
##ff=['SUSHIUSD',
##'ANKRUSD',
##'AMPUSD',
##'SHIBUSDT',
##'SHIBBUSD']
##
##for x in ff:
##    
##    btcusdt = get_bars(x)
##    print("historical data: ",btcusdt)
##sys.exit()

############################################## end of play area #####################################3
##
##'BTCUSD', 'ETHUSD', 'XRPUSD', 'BCHUSD', 'LTCUSD', 'USDTUSD', 'BTCUSDT', 'ETHUSDT', 'XRPUSDT', 'BCHUSDT', 'LTCUSDT',
##'BNBUSD', 'BNBUSDT', 'ETHBTC', 'XRPBTC', 'BNBBTC', 'LTCBTC', 'BCHBTC', 'ADAUSD', 'BATUSD', 'ETCUSD', 'XLMUSD',
##'ZRXUSD', 'ADAUSDT', 'BATUSDT', 'ETCUSDT', 'XLMUSDT', 'ZRXUSDT', 'LINKUSD', 'RVNUSD', 'DASHUSD', 'ZECUSD', 'ALGOUSD',
##'IOTAUSD', 'BUSDUSD', 'BTCBUSD', 'DOGEUSDT', 'WAVESUSD', 'ATOMUSDT', 'ATOMUSD', 'NEOUSDT', 'NEOUSD', 'VETUSDT', 'QTUMUSDT',
##'QTUMUSD', 'NANOUSD', 'ICXUSD', 'ENJUSD', 'ONTUSD', 'ONTUSDT', 'ZILUSD', 'ZILBUSD', 'VETUSD', 'BNBBUSD', 'XRPBUSD', 'ETHBUSD',
##'ALGOBUSD', 'XTZUSD', 'XTZBUSD', 'HBARUSD', 'HBARBUSD', 'OMGUSD', 'OMGBUSD', 'MATICUSD', 'MATICBUSD', 'XTZBTC', 'ADABTC', 'REPBUSD',
##'REPUSD', 'EOSBUSD', 'EOSUSD', 'DOGEUSD', 'KNCUSD', 'KNCUSDT', 'VTHOUSDT', 'VTHOUSD', 'USDCUSD', 'COMPUSDT', 'COMPUSD', 'MANAUSD',
##'HNTUSD', 'HNTUSDT', 'MKRUSD', 'MKRUSDT', 'DAIUSD', 'ONEUSDT', 'ONEUSD', 'BANDUSDT', 'BANDUSD', 'STORJUSDT', 'STORJUSD', 'BUSDUSDT',
##'UNIUSD', 'UNIUSDT', 'SOLUSD', 'SOLUSDT', 'LINKBTC', 'VETBTC', 'UNIBTC', 'EGLDUSDT', 'EGLDUSD', 'PAXGUSDT', 'PAXGUSD', 'OXTUSDT', 'OXTUSD',
##'ZENUSDT', 'ZENUSD', 'BTCUSDC', 'ONEBUSD', 'FILUSDT',
##'FILUSD', 'AAVEUSDT', 'AAVEUSD', 'GRTUSD', 'SUSHIUSD', 'ANKRUSD', 'AMPUSD', 'SHIBUSDT', 'SHIBBUSD', 'CRVUSDT', 'CRVUSD'


##'HBARUSD', 'HBARBUSD', 'OMGUSD', 'OMGBUSD'
    
##perda='635d'
##intervla='1d'
##yy=str(intervla).split('d')[0]
##shiftbydays=3
##import talib as ta
##from ta.utils import dropna
##import yfinance as yf
##import pandas as pd
##import sys
##import re
##import numpy as np
##from talib import stream
##from matplotlib import dates
##import matplotlib.pyplot as plt
####from datetime import date
####today = date.today().isoformat()
##import datetime
##import math
##import matplotlib.pyplot as plt
##import matplotlib.pyplot as plt2
##plt.style.use('fivethirtyeight')
##from millify import millify
####today = datetime.date.today() + datetime.timedelta(days=1)
##today = datetime.date.today()
####day = datetime.datetime.strptime(Date, '%d %m %Y').weekday()
####print(datetime.today().strftime('%Y-%m-%d'))
##import mpl_finance
##import matplotlib
####from matplotlib.finance import candlestick2_ohlc
####from mpl_finance import candlestick_ohlc
####from mplfinance.original_flavor import candlestick_ohlc
##from mplfinance.original_flavor import candlestick_ohlc
##from optionprice import Option
##from numerize import numerize
##import matplotlib.pyplot as plt
##pd.options.display.width = 0
##pd.set_option('display.max_columns', None)
##pd.options.display.float_format = '{:.2f}'.format
####pd.options.display.max_columns=255
##pd.options.display.max_rows=6500000
##pd.set_option('display.max_colwidth', 500)
##pd.set_option('display.max_columns', 550)
##pd.options.mode.chained_assignment = None  # default='warn'
##
##
##
####    g=input("Entr_Signal ticker: ")
##perd=perda
##intervl=intervla
####    ticker='BTC-USD'
####    ticker='^NDX'
####    ticker='MSTR'
####    ticker='MRNA'
####    ticker='AMZN'
####    ticker='TSLA'
##ticker='HBARBUSD'
### [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]
##
##
##
###df=pd.DataFrame()
###Interval required 5 minutes
##df = yf.download(ticker, period=perd, interval=intervl,prepost = True)
##df2=pd.DataFrame(df)
##print(df2)
##sys.exit()
########################################
##import requests 
##import json 
##import pandas as pd 
##import numpy as np  
##import datetime as dt  
##
####frequency = input("Please enter the frequency (1m/5m/30m/.../1h/6h/1d/ :  ")
##frequency='1d'
##def get_bars(symbol, interval=frequency):
##    root_url = 'https://api.binance.com/api/v1/klines'
##    url = root_url + '?symbol=' + symbol + '&interval=' + interval
##    print(symbol,' url  --->',url)
##    data=requests.get(url).json()
####    data = json.loads(requests.get(url).text)
##    print(symbol, ' data ----> ',data)
##    df = pd.DataFrame(data)
##    df.columns = ['open_time',
##                  'o', 'h', 'l', 'c', 'v',
##                  'close_time', 'qav', 'num_trades',
##                  'taker_base_vol', 'taker_quote_vol', 'ignore']
##    df.index = [dt.datetime.fromtimestamp(x / 1000.0) for x in df.close_time]
##    return df
##
##interval = '1d'
##f=['AAVEUSDT','ANKRUSD']
##df3=pd.DataFrame(f)
##df3.columns=['b']
##print(df3)
##
##for x in f:
##    btcusdt = get_bars(str(x))
####    btcusdt = get_bars('BTCUSDT')
##    print(btcusdt)
##
####ethusdt = get_bars('ETHUSDT')
##
##sys.exit()
######################################################################
'''
##
##print(client.get_symbol_info('USDCUSD'))
##
####for x in pp:
####    print(x,client.get_symbol_info(x)['orderTypes'])
##
##for x in pp:
##    print(x,client.get_symbol_info(x)['isMarginTradingAllowed'])

##info = client.get_symbol_info('BNBBTC')
##for x in info:
##    print(x, '   ',info[x])

##klines = client.get_historical_klines("ETHBTC", Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2020", "1 Jan, 2021")
##print(klines)
##df=pd.DataFrame(klines)
##print(df)

##klines = client.get_historical_klines("BNBBTC", AsyncClient.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
##print(klines)
##df=pd.DataFrame(klines)
##print(df)

##sys.exit()
##############
# https://stackoverflow.com/questions/55549499/how-to-retrieve-a-list-of-all-market-pairs-like-eth-btc-using-binance-api/69764567#69764567
##from binance.client import Client
##import pandas as pd
##
##api_key = ''
##api_secret = ''
##
##client = Client(api_key, api_secret)
##symbols = client.get_exchange_info()
##i = 0
##df = pd.DataFrame(columns=symbols[0].keys())
##for sym in symbols:
##    for key in sym.keys():
##        df.at[i, key] = sym[key]
##    i = i + 1
##
##
##df
##
##         symbol  ...     permissions
##0        ETHBTC  ...  [SPOT, MARGIN]
##1        LTCBTC  ...  [SPOT, MARGIN]
##2        BNBBTC  ...  [SPOT, MARGIN]
##3        NEOBTC  ...  [SPOT, MARGIN]
##4       QTUMETH  ...          [SPOT]
##         ...  ...             ...
##1710  CHESSBUSD  ...          [SPOT]
##1711  CHESSUSDT  ...          [SPOT]
##1712     FTMAUD  ...          [SPOT]
##1713     FTMBRL  ...          [SPOT]
##1714   SCRTBUSD  ...          [SPOT]
##[1715 rows x 17 columns]


# https://stackoverflow.com/questions/69684713/trigger-function-every-new-minute-w-websocket-data/69761530#69761530
################################################################
#############3 historical data    azhar
import requests 
import json 
import pandas as pd 
import numpy as np  
import datetime as dt  

##frequency = input("Please enter the frequency (1m/5m/30m/.../1h/6h/1d/ :  ")
frequency ='1d'
def get_bars(symbol, interval=frequency):
    root_url = 'https://api.binance.com/api/v1/klines'
    url = root_url + '?symbol=' + symbol + '&interval=' + interval
    data = json.loads(requests.get(url).text)
    df = pd.DataFrame(data)
    df.columns = ['open_time',
                  'open', 'high', 'low', 'close', 'volume',
                  'close_time', 'qav', 'num_trades',
                  'taker_base_vol', 'taker_quote_vol', 'ignore']
    df.index = [dt.datetime.fromtimestamp(x / 1000.0) for x in df.close_time]
    df['ticker']=''
    for x in df.index:
        df['ticker'].loc[x]=symbol

    df=df[['ticker',  'open_time',
                  'open', 'high', 'low', 'close', 'volume',
                  'close_time', 'qav', 'num_trades',
                  'taker_base_vol', 'taker_quote_vol', 'ignore']]  
    return df

btcusdt = get_bars('BTCUSDT')
print("historical data: ",btcusdt)
sys.exit()
##################################################################3

# https://stackoverflow.com/questions/66295187/how-do-i-get-all-the-prices-history-with-binance-api-for-a-crypto-using-python
import requests 
import json 
import pandas as pd 
import numpy as np  
import datetime as dt  

##frequency = input("Please enter the frequency (1m/5m/30m/.../1h/6h/1d/ :  ")

##def get_bars(symbol, interval=frequency):
##    root_url = 'https://api.binance.com/api/v1/klines'
##    url = root_url + '?symbol=' + symbol + '&interval=' + interval
##    data = json.loads(requests.get(url).text)
##    df = pd.DataFrame(data)
##    df.columns = ['open_time',
##                  'o', 'h', 'l', 'c', 'v',
##                  'close_time', 'qav', 'num_trades',
##                  'taker_base_vol', 'taker_quote_vol', 'ignore']
##    df.index = [dt.datetime.fromtimestamp(x / 1000.0) for x in df.close_time]
##    return df
##

##def get_bars(symbol, interval, start, end, limit=5000):
####def get_klines_iter(symbol, interval, start, end, limit=5000):
##    df = pd.DataFrame()
##    startDate = end
##    while startDate>start:
##        url = 'https://api.binance.com/api/v3/klines?symbol=' + \
##            symbol + '&interval=' + interval + '&limit='  + str(iteration)
##        if startDate is not None:
##            url += '&endTime=' + str(startDate)
##        
##        df2 = pd.read_json(url)
##        df2.columns = ['Opentime', 'Open', 'High', 'Low', 'Close', 'Volume', 'Closetime', 'Quote asset volume', 'Number of trades','Taker by base', 'Taker buy quote', 'Ignore']
##        df = pd.concat([df2, df], axis=0, ignore_index=True, keys=None)
##        startDate = df.Opentime[0]   
##    df.reset_index(drop=True, inplace=True)    
##    return df 

##btcusdt = get_bars('BTCUSDT')
##ethusdt = get_bars('ETHUSDT')
##
##
##df0=pd.DataFrame(btcusdt)
##df0.to_csv('_btcusdt.csv')
##
##df1=pd.DataFrame(ethusdt)
##print(df1)
##df1.to_csv('_ethusdt.csv')
##
##sys.exit()

############################
import os
from binance.client import Client
import pandas as pd
import datetime, time

def GetHistoricalData(self, howLong):
    self.howLong = howLong
    # Calculate the timestamps for the binance api function
    self.untilThisDate = datetime.datetime.now()
    self.sinceThisDate = self.untilThisDate - datetime.timedelta(days = self.howLong)
    # Execute the query from binance - timestamps must be converted to strings !
    self.candle = self.client.get_historical_klines("BNBBTC", Client.KLINE_INTERVAL_1MINUTE, str(self.sinceThisDate), str(self.untilThisDate))

    # Create a dataframe to label all the columns returned by binance so we work with them later.
    self.df = pd.DataFrame(self.candle, columns=['dateTime', 'open', 'high', 'low', 'close', 'volume', 'closeTime', 'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol', 'takerBuyQuoteVol', 'ignore'])
    # as timestamp is returned in ms, let us convert this back to proper timestamps.
    self.df.dateTime = pd.to_datetime(self.df.dateTime, unit='ms').dt.strftime(Constants.DateTimeFormat)
    self.df.set_index('dateTime', inplace=True)

    # Get rid of columns we do not need
    self.df = self.df.drop(['closeTime', 'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol','takerBuyQuoteVol', 'ignore'], axis=1)

    print(self.df)

self="BNBBTC"
howLong='2021-10-30'
GetHistoricalData(self, howLong)
sys.exit()
################################################
info = client.get_all_tickers()
df=pd.DataFrame(info)
##print('info---------------- ',info)
df.sort_values(by=['price'], ascending=True,inplace=True)
##df.sort_values(by='price',  key=lambda col: col.str.lower())


print(df)

sys.exit()
############################################################
##print('get account info: ', client.get_account())
##print('get_asset_balanc  ',client.get_asset_balance(asset='BTC'))
### get balances for futures account
##print(client.futures_account_balance())
### get balances for margin account
##print(client.get_margin_account())
###https://algotrading101.com/learn/binance-python-api-guide/
##
### get latest price from Binance API
##btc_price = client.get_symbol_ticker(symbol="BTCUSDT")
### print full output (dictionary)
##print(btc_price)
##print(btc_price["price"])
info = client.get_symbol_info('ETHUSDT')
print(info)
######################################################

##
##buy_order = client.create_test_order(symbol='ETHUSDT', side='BUY', type='MARKET', quantity=100)
##print(buy_order)



depth = client.get_order_book(symbol='BNBBTC')
for x in depth:
    print(x,'   ',depth)
##
##print('\n\n\n')
info = client.get_all_tickers()
print('info---------------- ',info)
##print('\n\n\n')
trades = client.get_recent_trades(symbol='BNBBTC')
print('trades -----  ',trades)
##print('\n\n\n')
candles = client.get_klines(symbol='BNBBTC', interval=Client.KLINE_INTERVAL_30MINUTE)
print('candles -----  ',candles)
##print('\n\n\n')

##sym = 'BTCUSDT'
##info = client.get_symbol_info(sym)
##print(info)


##
##accounts = client.create_order( symbol='BNBBTC',side='BUY',type='MARKET',timeInForce=TIME_IN_FORCE_GTC,quantity=1,price='0.00001')
##
import time
os.system("w32tm /resync")
print(int(time.time() * 1000)-client.get_server_time()['serverTime'])
##for i in range(1, 10):
##    local_time1 = int(time.time() * 1000)
##    server_time = client.get_server_time()
##    diff1 = server_time['serverTime'] - local_time1
##    local_time2 = int(time.time() * 1000)
##    diff2 = local_time2 - server_time['serverTime']
##    print("local1: %s server:%s local2: %s diff1:%s diff2:%s" % (local_time1, server_time['serverTime'], local_time2, diff1, diff2))
##    time.sleep(2)

    
gt = client.get_server_time()
tt=time.gmtime(int((gt["serverTime"])/1000))


_tickers = client.get_all_tickers()
print(_tickers)
##binance.fetch_balance({'recvWindow': 10000000})   ,
##    recvWindow=10000


print("kkkk")


print('\n\n')
print('#############################################################################################')
print("Enter Test Order >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ")
print('\n\n')
###############################################
#First get ETH price
eth_price = client.get_symbol_ticker(symbol="ETHUSDT")

# Calculate how much ETH $200 can buy
##buy_quantity = round(2066600 / float(eth_price['price']))
buy_quantity = round(2066600 / float(eth_price['price']))
##print('buy_quantity  ',buy_quantity, '  '  ,eth_price['price'] )

# Create test order
order = client.create_test_order(
        symbol='ETHUSDT',
        side=Client.SIDE_BUY,
        type=Client.ORDER_TYPE_MARKET,
        quantity=buy_quantity
    )

##########
import websocket, json, pprint, talib, numpy
##import config
from binance.client import Client
from binance.enums import *

SOCKET = "wss://stream.binance.com:9443/ws/btceur@kline_5m"

RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
TRADE_SYMBOL = 'BTCEUR'
TRADE_QUANTITY_BUY = 0.002

closes = []

##client = Client(config.API_KEY, config.API_SECRET)
client = Client('y9SvMHSmcHMw7wrGBF5SLKRGYBU8VjOJkGdwkN9XrnPelKeBcqXhyNKt28LDPxxG', 'BsKSkRvqtbvo2gmV5Brgjc3CujV724vfDCSuTES9DfhaZdVxQmR293tjtYVdTFcO'
                , tld='us')

balance = client.get_asset_balance(asset='BTC')
##FREEBTC = float(balance['free'])
FREEBTC = float(buy_quantity)
TRADE_QUANTITY_SELL = round(FREEBTC, 6)


#print(SELL_TOTAL)
def order(side, quantity, symbol, order_type=ORDER_TYPE_MARKET):
    try:
        print("sending order")
        order = client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
        print(order)
    except Exception as e:
        print("an exception occured - {}".format(e))
        return False

    return True

def on_open(ws):
    print('opened connection')

def on_close(ws):
    print('closed connection')

def on_message(ws, message):
    global closes
    
    print('received message')
    json_message = json.loads(message)
    pprint.pprint(json_message)

    candle = json_message['k']

    is_candle_closed = candle['x']
    close = candle['c']

    in_position = False

    #also tried to put the TRADE_QUANTITY_SELL params here, also does not work

    if is_candle_closed:
        print("candle closed at {}".format(close))
        closes.append(float(close))
        print("closes")
        print(closes)

        if len(closes) > RSI_PERIOD:
            np_closes = numpy.array(closes)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            print("all rsis calculated so far")
            print(rsi)
            last_rsi = rsi[-1]
            print("the current rsi is {}".format(last_rsi))         

            if last_rsi > RSI_OVERBOUGHT:
                if in_position:
                    print("Overbought! Sell! Sell! Sell!")
                    #put binance order logic here
                    order_succeeded = order(SIDE_SELL, TRADE_QUANTITY_SELL, TRADE_SYMBOL)
                    if order_succeeded:
                        in_position = False
                else:
                    print("It is overbought, but we don't own any. Nothing to do.")

            if last_rsi < RSI_OVERSOLD:
                if in_position:
                    print("Oversold! Buy! Buy! Buy!")
                    #print("It is oversold, but you already own it, nothing to do")
                    order_succeeded = order(SIDE_BUY, TRADE_QUANTITY_BUY, TRADE_SYMBOL)
                    if order_succeeded:
                        in_position = True                  
                else:
                    print("Oversold! Buy! Buy! Buy!")
                    #put binance order logic here
                    order_succeeded = order(SIDE_BUY, TRADE_QUANTITY_BUY, TRADE_SYMBOL)
                    if order_succeeded:
                        in_position = True

ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)   

ws.run_forever( )
#https://stackoverflow.com/questions/66742165/struggling-to-combine-two-working-functions

################################################################################################################
##client.futures_create_order(symbol=sym, side='BUY', type='MARKET', quantity=float(trade_quantity_str))
##https://stackoverflow.com/questions/65237367/how-to-place-a-futures-market-order-using-python-binance-apierrorcode-1111
####################################################################################################################
##order = client.create_test_order(
##    symbol = symbolTicker,
##    side = SIDE_BUY,
##    type = ORDER_TYPE_LIMIT,
##    quantity = quantity,
##    price = price,
##    timeInForce = "GTC")
##
##orders = client.get_order(
##    symbol="DOGEEUR",
##    orderId="orderId")
##print(orders)

#https://stackoverflow.com/questions/67258954/binance-trade-bot-python
####################################################################################################################
##imp
##https://stackoverflow.com/questions/60736731/what-is-the-problem-with-my-code-in-borrowing-cryptocurrency-with-api-in-binance
####################################################################################################################
##p1=client.create_test_order(
##    symbol='ETHUSD',
##    side=Client.SIDE_BUY,
##    type=Client.ORDER_TYPE_MARKET,
##    quantity=5,recvWindow=10000)
##print(p1)

##buy_order = client.create_test_order(symbol='OMGUSD', side='BUY', type='MARKET', quantity=1000)
##buy_order = client.create_test_order(symbol='OMGUSD', side='SELL', type='MARKET', quantity=1000)
##print(help(client.create_test_order))
##print(help(client.options_info))
##print(help(client.OPTIONS_API_VERSION))
##orders = client.get_open_orders(symbol='BTCUSDT')
##
##print(p)
##
##client.create_test_order(
##    symbol= 'BNBBUSD',
##    side=Client.SIDE_SELL,
##    type=Client.ORDER_TYPE_MARKET,
##    quantity=1,
##    recvWindow=10000)
##
##
##client.create_test_order(
##    symbol= 'XRPBUSD',
##    side=Client.SIDE_SELL,
##    type=Client.ORDER_TYPE_MARKET,
##    quantity=1,
##    recvWindow=10000)

'''
