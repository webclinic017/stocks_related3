import os
from binance.client import Client
import pandas as pd
import ccxt 
import sys


##
##client = Client('y9SvMHSmcHMw7wrGBF5SLKRGYBU8VjOJkGdwkN9XrnPelKeBcqXhyNKt28LDPxxG','BsKSkRvqtbvo2gmV5Brgjc3CujV724vfDCSuTES9DfhaZdVxQmR293tjtYVdTFcO')
####api_secret = os.environ.get('binance_secret')
####api_key = os.environ.get('binance_api')
####client = Client(api_key, api_secret)
##btc_price = client.get_symbol_ticker(symbol="BTCUSDT")
##print(btc_price["price"].encode('utf-8'))
####print(client.get_account())
####print(help(client))
##print(ccxt.exchanges)



# get latest price from Binance API
##btc_price = client.get_symbol_ticker(symbol="BTCUSDT")
### print full output (dictionary)
##print(btc_price)


###################
##binance = ccxt.binance()
##binance.options = {'defaultType': 'delivery', 'adjustForTimeDifference': True}
##
##securities = pd.DataFrame(binance.load_markets()).transpose()
##print(securities)

#######################
##
##print('CCXT version:', ccxt.__version__)  # requires CCXT version > 1.20.31
##exchange = ccxt.binance({
##    'apiKey': api_key,
##    'secret': api_secret,
##    'enableRateLimit': True,
##    'options': {
##        'defaultType': 'future',  # ←-------------- quotes and 'future'
##    },
##})
##
##markets = exchange.load_markets()  # Load the futures markets
##
##for market in markets: 
##    print(market)
#######################
import ccxt
from pprint import pprint

c = ccxt.binance()
print(c.account)
print(c.accounts)
print('\n\n\n\n')
ticker = c.fetch_ticker('BTC/USDT')

pprint(c.last_http_response)
pprint(c.last_json_response)
print('\n')
print('kaku')
print('\n\n\n')
############################
##
##import ccxt
##import pandas as pd
##
##exch = 'binance' # initial exchange
##t_frame = '1d' # 1-day timeframe, usually from 1-minute to 1-week depending on the exchange
##symbol = 'ADA/BTC' # initial symbol
##exchange_list = ['binance','bitfinex','bytetrade','ftx','kraken','poloniex','upbit','acx','bequant','bigone','bitforex','bitkk','bitz','btcalpha','coinex','crex24','digifinex','gateio','hitbtc2','huobipro','huobiru','kucoin','lbank','okex','okex3','stex','upbit','whitebit','zb']
## 
### Get our Exchange
##try:
##    exchange = getattr (ccxt, exch) ()
##except AttributeError:
##    print('-'*36,' ERROR ','-'*35)
##    print('Exchange "{}" not found. Please check the exchange is supported.'.format(exch))
##    print('-'*80)
##    quit()
## 
### Check if fetching of OHLC Data is supported
##if exchange.has["fetchOHLCV"] != True:
##    print('-'*36,' ERROR ','-'*35)
##    print('{} does not support fetching OHLC data. Please use another  exchange'.format(exch))
##    print('-'*80)
##    quit()
## 
### Check requested timeframe is available. If not return a helpful error.
##if (not hasattr(exchange, 'timeframes')) or (t_frame not in exchange.timeframes):
##    print('-'*36,' ERROR ','-'*35)
##    print('The requested timeframe ({}) is not available from {}\n'.format(t_frame,exch))
##    print('Available timeframes are:')
##    for key in exchange.timeframes.keys():
##        print('  - ' + key)
##    print('-'*80)
##    quit()
## 
### Check if the symbol is available on the Exchange
##exchange.load_markets()
##if symbol not in exchange.symbols:
##    print('-'*36,' ERROR ','-'*35)
##    print('The requested symbol ({}) is not available from {}\n'.format(symbol,exch))
##    print('Available symbols are:')
##    for key in exchange.symbols:
##        print('  - ' + key)
##    print('-'*80)
##    quit()
## 
## 
### Get data
##data = exchange.fetch_ohlcv(symbol, t_frame)
##header = ['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume']
##df = pd.DataFrame(data, columns=header).set_index('Timestamp')
##df['symbol'] = symbol
##syms = [symbol]
##filename = '{}.csv'.format(t_frame)
##
##for exch in exchange_list:
##    try:
##        exchange = getattr (ccxt, exch) ()
##    except AttributeError:
##        print('-'*36,' ERROR ','-'*35)
##        print('Exchange "{}" not found. Please check the exchange is supported.'.format(exch))
##        print('-'*80)
##        quit()
##    if exchange.has["fetchOHLCV"] != True:
##        print('-'*36,' ERROR ','-'*35)
##        print('{} does not support fetching OHLC data. Please use another exchange'.format(exch))
##        print('-'*80)
##        quit()
##    if (not hasattr(exchange, 'timeframes')) or (t_frame not in exchange.timeframes):
##        print('-'*36,' ERROR ','-'*35)
##        print('The requested timeframe ({}) is not available from {}\n'.format(t_frame,exch))
##        print('Available timeframes are:')
##        for key in exchange.timeframes.keys():
##            print('  - ' + key)
##        print('-'*80)
##        quit()
##    exchange.load_markets()
##    for coin in exchange.symbols:
##        if coin in syms or coin[-3:] != 'BTC':
##            continue
##        else:
##            try:
##                data = exchange.fetch_ohlcv(coin, t_frame)
##            except:
##                continue
##            data_df = pd.DataFrame(data, columns=header).set_index('Timestamp')
##            data_df['symbol'] = coin
##            df = df.append(data_df)
##            syms.append(coin)
##df.index = df.index/1000 #Timestamp is 1000 times bigger than it should be in this case
##df['Date'] = pd.to_datetime(df.index,unit='s')
##df.to_csv(filename)

########################################################

from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
##client = Client(api_key, api_secret, testnet=True)
##client = Client(api_key, api_secret, testnet=True)
##client = Client('y9SvMHSmcHMw7wrGBF5SLKRGYBU8VjOJkGdwkN9XrnPelKeBcqXhyNKt28LDPxxG',
##                'BsKSkRvqtbvo2gmV5Brgjc3CujV724vfDCSuTES9DfhaZdVxQmR293tjtYVdTFcO', testnet=True, tld='us')

x1='y9SvMHSmcHMw7wrGBF5SLKRGYBU8VjOJkGdwkN9XrnPelKeBcqXhyNKt28LDPxxG'
y1='BsKSkRvqtbvo2gmV5Brgjc3CujV724vfDCSuTES9DfhaZdVxQmR293tjtYVdTFcO'
####client = RequestClient(api_key=x1, secret_key=y1, https://fapi.binance.com')
##client = Client(x1, y1, url='https://testnet.binancefuture.com')
##client = SubscriptionClient(api_key=x1, secret_key=y1, uri='wss://fstream.binance.com/ws')
client = Client('y9SvMHSmcHMw7wrGBF5SLKRGYBU8VjOJkGdwkN9XrnPelKeBcqXhyNKt28LDPxxG', 'BsKSkRvqtbvo2gmV5Brgjc3CujV724vfDCSuTES9DfhaZdVxQmR293tjtYVdTFcO'
                , tld='us')


r = client.get_historical_klines('ETHBTC', client.KLINE_INTERVAL_1DAY, '1-Dec-2021', '31-Dec-2021')
##print(r)

spot = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "24 Mar, 2021", "23 Apr, 2021")
print(spot)

sys.exit()

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
##
##accounts = client.create_order( symbol='BNBBTC',side='BUY',type='MARKET',timeInForce=TIME_IN_FORCE_GTC,quantity=1,price='0.00001')
##



order = client.create_test_order(
symbol='BNBBTC',
quantity=1)

##from binance.enums import *
##order = client.create_test_order(
##symbol='BNBBTC',
##side=SIDE_BUY,
##type=ORDER_TYPE_LIMIT,
##timeInForce=TIME_IN_FORCE_GTC,
##quantity=100,
##price='0.00001')
##
##accounts = client.get_sub_account_list()
##for x in accounts:
##    print(x,'  ')

##price = float(client.futures_symbol_ticker(symbol = 'ETHUSDT')['price'])
##orderstop= client.futures_create_order(
##    symbol='ETHUSDT',
##    side= Client.SIDE_SELL,
##    type = 'STOP_MARKET',
##    stopLimitTimeInForce='GTC',
##    stopPrice = price-stop,
##    closePosition= True,
##    quantity=lot)


##twm = ThreadedWebsocketManager()
##twm.start()

#############################3
##from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
##try:
##    buy_limit = client.create_order(
##        symbol='ETHUSDT',
##        side='BUY',
##        type='LIMIT',
##        timeInForce='GTC',
##        quantity=100,
##        price=200)
##
##except BinanceAPIException as e:
##    # error handling goes here
##    print(e)
##except BinanceOrderException as e:
##    # error handling goes here
##    print(e)
##

