import ccxt
from pprint import pprint
import datetime
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import pandas as pd


pd.options.display.float_format = '{:.2f}'.format
pd.options.display.max_columns = 255
pd.options.display.max_rows = 6500000
pd.set_option('display.max_rows', None)

##pd.options.display.max_rows = 999999
pd.options.display.max_columns = 76
pd.set_option("display.max_columns", 200)
pd.set_option('display.width', 1000)
pd.set_option('display.expand_frame_repr', False)



pd.options.display.float_format = '{:.2f}'.format
pd.options.display.max_columns = 255
pd.options.display.max_rows = 6500000

##pd.options.display.max_rows =999999 
##pd.options.display.max_columns = 36  ,'spy','msft','tsla','docu','mrna'
pd.set_option("display.max_columns", 100)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 200)
pd.set_option('display.max_columns', 0)
pd.set_option('display.max_columns', None)
pd.set_option("expand_frame_repr", True)

print('CCXT Version:', ccxt.__version__)
u='APE/USDT'
exchange = ccxt.binance()
timestamp = int(datetime.datetime.strptime("2022-04-24 11:20:00+00:00", "%Y-%m-%d %H:%M:%S%z").timestamp() * 1000)
response = exchange.fetch_ohlcv(str(u), '1m', timestamp, 1)
btc_ticker = exchange.fetch_ticker(str(u))

btc_usdt_ohlcv = exchange.fetch_ohlcv(str(u),'1d',limit=100)
print(btc_usdt_ohlcv)

##print(response)
##print(btc_ticker)
##for x in btc_ticker:
##    print(x,'  ',x.item)

orderbook_binance_btc_usdt =exchange.fetch_order_book(str(u))
##orderbook_ftx_btc_usdt = ftx.fetch_order_book('BTC/USDT')
##bids_binance = orderbook_binance_btc_usdt['bids']
##asks_binanace = orderbook_binance_btc_usdt['asks']
##df_bid_binance = pd.DataFrame(bids_binance, columns=['price','qty'])
##df_ask_binance = pd.DataFrame(asks_binanace, columns=['price','qty'])

print(orderbook_binance_btc_usdt)
####################
##client = Client('y9SvMHSmcHMw7wrGBF5SLKRGYBU8VjOJkGdwkN9XrnPelKeBcqXhyNKt28LDPxxG', 'BsKSkRvqtbvo2gmV5Brgjc3CujV724vfDCSuTES9DfhaZdVxQmR293tjtYVdTFcO'
##                , tld='us')

exchange = Client('y9SvMHSmcHMw7wrGBF5SLKRGYBU8VjOJkGdwkN9XrnPelKeBcqXhyNKt28LDPxxG', 'BsKSkRvqtbvo2gmV5Brgjc3CujV724vfDCSuTES9DfhaZdVxQmR293tjtYVdTFcO'
                , tld='us')

depth = exchange.get_order_book(symbol=str(u))
for x in depth:
    print(x,'   ',depth)
##
##print('\n\n\n')


'''
info = client.get_all_tickers()
print('info---------------- ',info)
##print('\n\n\n')

trades = client.get_recent_trades(symbol='BNBBTC')
print('trades -----  ',trades)
##print('\n\n\n')
candles = client.get_klines(symbol='BNBBTC', interval=Client.KLINE_INTERVAL_30MINUTE)
print('candles -----  ',candles)


order = client.create_test_order(
symbol='BNBBTC',
quantity=1)
'''



































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
