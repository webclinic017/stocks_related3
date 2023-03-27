##import requests
##import pandas as pd
##import matplotlib.pyplot as plt
##import seaborn as sns
### https://tiao.io/post/exploring-the-binance-cryptocurrency-exchange-api-orderbook/
### https://medium.com/codex/10-best-resources-to-fetch-cryptocurrency-data-in-python-8400cf0d0136
### https://towardsdatascience.com/top-5-best-cryptocurrency-apis-for-developers-32475d2eb749
##https://www.cryptomaton.org/2021/04/05/how-to-analyse-daily-news-sentiment-for-cryptocurrency-with-python/
## https://coinmarketcap.com/all/views/all/
##
##r = requests.get("https://api.binance.com/api/v3/depth",
##                 params=dict(symbol="ETHBUSD"))
##results = r.json()
##
##frames = {side: pd.DataFrame(data=results[side], columns=["price", "quantity"],
##                             dtype=float)
##          for side in ["bids", "asks"]}
##
##frames_list = [frames[side].assign(side=side) for side in frames]
##data = pd.concat(frames_list, axis="index", 
##                 ignore_index=True, sort=True)
##
##price_summary = data.groupby("side").price.describe()
##price_summary.to_markdown()


### import the libraries we need
##import shrimpy
##import plotly.graph_objects as go
##
### insert your public and secret keys here
##public_key = '8x71n32d8cfbnnn1xzimjustkeyboardmashing8xn1t8jyv5098'
##secret_key = '771dc5nxct4709672v4n09xn0morekeyboardmashing9475c029374n0xx4n50'
##
### create the client
##client = shrimpy.ShrimpyApiClient(public_key, secret_key)
##
### get the candles
##candles = client.get_candles(
##    'binance',  # exchange
##    'XLM',      # base_trading_symbol
##    'BTC',      # quote_trading_symbol
##    '15m'       # interval
##)
##
### create lists to hold our different data elements
##dates = []
##open_data = []
##high_data = []
##low_data = []
##close_data = []
##
### convert from the Shrimpy candlesticks to the plotly graph objects format
##for candle in candles:
##    dates.append(candle['time'])
##    open_data.append(candle['open'])
##    high_data.append(candle['high'])
##    low_data.append(candle['low'])
##    close_data.append(candle['close'])
##
### construct the figure
##fig = go.Figure(data=[go.Candlestick(x=dates,
##                       open=open_data, high=high_data,
##                       low=low_data, close=close_data)])
##
### display our graph
##fig.show()


#!/usr/bin/python3

##import importlib
##import signal
##import sys
##import threading
##from decouple import config
##
##from services.backtest import Backtest
##from services.importer import Importer
##
##exchange_name = config('EXCHANGE')
##available_exchanges = config('AVAILABLE_EXCHANGES').split(',')
##mode: str = config('MODE')
##strategy: str = config('STRATEGY')
##trading_mode: str = config('TRADING_MODE')
##interval: int = int(config('CANDLE_INTERVAL'))
##currency: str = config('CURRENCY')
##asset: str = config('ASSET')
##
##if trading_mode == 'real':
##    print("*** Caution: Real trading mode activated ***")
##else:
##    print("Test mode")
##
### Parse symbol pair from first command argument
##if len(sys.argv) > 1:
##    currencies = sys.argv[1].split('_')
##    if len(currencies) > 1:
##        currency = currencies[0]
##        asset = currencies[1]
##
### Load exchange
##print("Connecting to {} exchange...".format(exchange_name[0].upper() + exchange_name[1:]))
##exchangeModule = importlib.import_module('exchanges.' + exchange_name, package=None)
##exchangeClass = getattr(exchangeModule, exchange_name[0].upper() + exchange_name[1:])
##exchange = exchangeClass(config(exchange_name.upper() + '_API_KEY'), config(exchange_name.upper() + '_API_SECRET'))
##
### Load currencies
##exchange.set_currency(currency)
##exchange.set_asset(asset)
##
### Load strategy
##strategyModule = importlib.import_module('strategies.' + strategy, package=None)
##strategyClass = getattr(strategyModule, strategy[0].upper() + strategy[1:])
##exchange.set_strategy(strategyClass(exchange, interval))
##
### mode
##print("{} mode on {} symbol".format(mode, exchange.get_symbol()))
##if mode == 'trade':
##    exchange.strategy.start()
##
##elif mode == 'live':
##    exchange.start_symbol_ticker_socket(exchange.get_symbol())
##
##elif mode == 'backtest':
##    period_start = config('PERIOD_START')
##    period_end = config('PERIOD_END')
##
##    print(
##        "Backtest period from {} to {} with {} seconds candlesticks.".format(
##            period_start,
##            period_end,
##            interval
##        )
##    )
##    Backtest(exchange, period_start, period_end, interval)
##
##elif mode == 'import':
##    period_start = config('PERIOD_START')
##    period_end = config('PERIOD_END')
##
##    print(
##        "Import mode on {} symbol for period from {} to {} with {} seconds candlesticks.".format(
##            exchange.get_symbol(),
##            period_start,
##            period_end,
##            interval
##        )
##    )
##    importer = Importer(exchange, period_start, period_end, interval)
##    importer.process()
##
##else:
##    print('Not supported mode.')
##
##
##def signal_handler(signal, frame):
##    if (exchange.socket):
##        print('Closing WebSocket connection...')
##        exchange.close_socket()
##        sys.exit(0)
##    else:
##        print('stopping strategy...')
##        exchange.strategy.stop()
##        sys.exit(0)
##
##
### Listen for keyboard interrupt event
##signal.signal(signal.SIGINT, signal_handler)
##forever = threading.Event()
##forever.wait()
##exchange.strategy.stop()
##sys.exit(0)

##import numpy as np
##import pandas as pd
##from binance.helpers import *
##from binance.client import Client
##from binance.websockets import BinanceSocketManager
##
####client = Client('API','SECRET')
##client = Client('y9SvMHSmcHMw7wrGBF5SLKRGYBU8VjOJkGdwkN9XrnPelKeBcqXhyNKt28LDPxxG', 'BsKSkRvqtbvo2gmV5Brgjc3CujV724vfDCSuTES9DfhaZdVxQmR293tjtYVdTFcO'
##                , tld='us')
##bm = BinanceSocketManager(client)
##
##def get_historical_candles():
##    record = client.get_historical_klines("ETHUSDT",client.KLINE_INTERVAL_30MINUTE, "30 minutes ago UTC")
##    myList = []
##
##    try:
##        for item in record:
##            n_item = []
##            int_ts = int(item[0] / 1000)
##            # nur neue timestamps anhängen
##
##            n_item.append(int_ts)  # open time
##            n_item.append(float(item[1]))  # open
##            n_item.append(float(item[2]))  # high
##            n_item.append(float(item[3]))  # low
##            n_item.append(float(item[4]))  # close
##            n_item.append(float(item[5]))  # volume
##            n_item.append(int(item[6] / 1000))  # close_time
##            n_item.append(float(item[7]))  # quote_assetv
##            n_item.append(int(item[8]))  # trades
##            n_item.append(float(item[9]))  # taker_b_asset_v
##            n_item.append(float(item[10]))  # taker_b_quote_v
##            n_item.append(datetime.fromtimestamp(n_item[0]))
##            myList.append(n_item)
##    except Exception as error:
##        debug_logger.debug(error)
##
##    new_ohlc = pd.DataFrame(myList, columns=['open_time', 'open', 'high', 'low',
##                                                'close', 'volume', 'close_time', 'quote_assetv', 'trades',
##                                                'taker_b_asset_v',
##                                                'taker_b_quote_v', 'datetime'])
##
##    return new_ohlc
##
##
##data_df = get_historical_candles()
##closes = []
##
##current_time = datetime.fromtimestamp(time.time())
##
##for each_close,close_time in zip(data_df['close'],data_df['datetime']):
##    closes.append(each_close)
##    np_closes = np.array(closes)
##    
##    # stochrsi
##    fastk, fastd = talib.STOCHRSI(np_closes, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
##
##    # macd
##    ShortEMA = talib.EMA(np_closes, 9)
##    LongEMA = talib.EMA(np_closes, 18)
##    MACD = ShortEMA - LongEMA
##    signal = talib.EMA(MACD, 5)
##
##    # bollinger bands
##    upperband, middleband, lowerband = talib.BBANDS(np_closes, timeperiod=18, nbdevup=2, nbdevdn=2,
##                                                    matype=0)
##    upperband_crossed = numpy.where((np_closes > upperband), 1, 0)
##    lowerband_crossed = numpy.where((np_closes < lowerband), 1, 0)
##    
##    last_upperband_crossed = upperband_crossed[-1]
##    last_lowerband_crossed = lowerband_crossed[-1]
##    last_macd = MACD[-1]
##    last_signal = signal[-1]
##    last_fastk = fastk[-1]
##    last_fastd = fastd[-1]
##    
##    #### decision trend : BUY OR SELL
##
##    if last_macd > last_signal:
##        should_buy += 1
##
##    if last_lowerband_crossed:
##        should_buy += 1
##
##    if last_macd < last_signal:
##        should_sell += 1
##
##    if last_upperband_crossed:
##        should_sell += 1
##
##    if last_fastd > 90 and last_fastk > 90:
##        should_buy += 1
##
##    if last_fastd <= 20 and last_fastk <= 20:
##        should_sell += 1
##        
##        
##    if should_buy > 0:
##        print("[ BUY ]",bcolors.OKGREEN,should_buy,bcolors.ENDC)
##    if should_sell > 0:
##        print("[ SELL ]",bcolors.FAIL,should_sell,bcolors.ENDC)
##
##    now = datetime.now()
##    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
##    print(dt_string)
##    
##    ### STRONG BUY/SELL, MEDIUM BUY/SELL, LOW BUY/SELL TRENDS: 
##
##    if should_buy == 2 and lowest_price < close < average_price and should_sell == 0:
##        print("{}{}{}".format(bcolors.OKGREEN,"[LOW BUY]",bcolors.ENDC," : ",close))
##    elif should_buy == 2 and lowest_price < close < average_price:
##        print("{}{}{}".format(bcolors.OKGREEN,"[MEDIUM BUY ]",bcolors.ENDC," : ",close))
##
##    if should_sell == 2 and max_price > close > average_price and should_buy == 0:
##        print("{}{}{}".format(bcolors.FAIL,"[MEDIUM SELL]",bcolors.ENDC," : ",close))
##    elif should_sell == 2 and max_price > close > average_price:
##        print("{}{}{}".format(bcolors.FAIL,"[LOW SELL]",bcolors.ENDC," : ",close))
##
##    if should_sell == 3 and max_price > close > average_price:
##        print("{}{}{}{}".format(bcolors.BOLD,bcolors.FAIL,"[STRONG SELL]",bcolors.ENDC," : ",close))
##
##
##    if should_buy == 3 and lowest_price < close < average_price:
##        print("{}{}{}{}".format(bcolors.BOLD,bcolors.OKGREEN,"STRONG BUY]",bcolors.ENDC," : ",close))
##
####except Exception as e:
####     print("[!!] EXCEPTION : ",e)

##
##import os
##import numpy as np
##import pandas as pd
##import pickle
##import quandl
##from datetime import datetime
##
##import plotly.offline as py
##import plotly.graph_objs as go
##import plotly.figure_factory as ff
##py.init_notebook_mode(connected=True)
##
##def get_quandl_data(quandl_id):
##    '''Download and cache Quandl dataseries'''
##    cache_path = '{}.pkl'.format(quandl_id).replace('/','-')
##    try:
##        f = open(cache_path, 'rb')
##        df = pickle.load(f)   
##        print('Loaded {} from cache'.format(quandl_id))
##    except (OSError, IOError) as e:
##        print('Downloading {} from Quandl'.format(quandl_id))
##        df = quandl.get(quandl_id, returns="pandas")
##        df.to_pickle(cache_path)
##        print('Cached {} at {}'.format(quandl_id, cache_path))
##    return df
##
### Pull pricing data for3 more BTC exchanges
##exchanges = ['COINBASE','BITSTAMP','ITBIT']
##exchange_data = {}
##exchange_data['KRAKEN'] = btc_usd_price_kraken
##for exchange in exchanges:
##    exchange_code = 'BCHARTS/{}USD'.format(exchange)
##    btc_exchange_df = get_quandl_data(exchange_code)
##    exchange_data[exchange] = btc_exchange_df
##
##
##def merge_dfs_on_column(dataframes, labels, col):
##    '''Merge a single column of each dataframe into a new combined dataframe'''
##    series_dict = {}
##    for index in range(len(dataframes)):
##        series_dict[labels[index]] = dataframes[index][col]
##    return pd.DataFrame(series_dict)
##
##
### Merge the BTC price dataseries' into a single dataframe
##btc_usd_datasets = merge_dfs_on_column(list(exchange_data.values()), list(exchange_data.keys()), 'Weighted Price')
##
##btc_usd_datasets.tail()

perda='635d'
intervla='1d'
yy=str(intervla).split('d')[0]
shiftbydays=3
import talib as ta
from ta.utils import dropna
import yfinance as yf
import pandas as pd
import sys
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
import mpl_finance
import matplotlib
##from matplotlib.finance import candlestick2_ohlc
##from mpl_finance import candlestick_ohlc
##from mplfinance.original_flavor import candlestick_ohlc
from mplfinance.original_flavor import candlestick_ohlc
from optionprice import Option
from numerize import numerize
import matplotlib.pyplot as plt
pd.options.display.width = 0
pd.set_option('display.max_columns', None)
pd.options.display.float_format = '{:.2f}'.format
##pd.options.display.max_columns=255
pd.options.display.max_rows=6500000
pd.set_option('display.max_colwidth', 500)
pd.set_option('display.max_columns', 550)
pd.options.mode.chained_assignment = None  # default='warn'



##    g=input("Entr_Signal ticker: ")
perd=perda
intervl=intervla
##    ticker='BTC-USD'
##    ticker='^NDX'
##    ticker='MSTR'
##    ticker='MRNA'
##    ticker='AMZN'
##    ticker='TSLA'
ticker=['HIVE-USD','JDC-USD','DOGE-USD']
# [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]

print(ticker[2])

#df=pd.DataFrame()
#Interval required 5 minutes
df2 = yf.download(ticker[0], period=perd, interval=intervl,prepost = True)
df3 = yf.download(ticker[1], period=perd, interval=intervl,prepost = True)
df4 = yf.download(ticker[2], period=perd, interval=intervl,prepost = True)
df2.reset_index()
df3.reset_index()
df4.reset_index()

print(ticker[0],ticker[1],ticker[2])
###########################################
df2['xx']=''
for x in df2.index:
    df2['xx'].loc[x]=ticker[0]
df2=pd.DataFrame(df2,columns=('xx','Close','Volume'))
df2.columns=['xx',ticker[0]+'_'+'Close',ticker[0]+'_'+'Volume']
##################3
df3['xx']=''
for x in df3.index:
    df3['xx'].loc[x]=ticker[1]
df3=pd.DataFrame(df3,columns=('xx','Close','Volume'))
df3.columns=['xx',ticker[1]+'_'+'Close',ticker[1]+'_'+'Volume']
##################3
df4['xx']=''
for x in df4.index:
    df4['xx'].loc[x]=ticker[2]
df4=pd.DataFrame(df4,columns=('xx','Close','Volume'))
df4.columns=['xx',ticker[2]+'_'+'Close',ticker[2]+'_'+'Volume']
##print(df4)
##################3



dfa=pd.concat([df2,df3,df4],axis=1)
print(dfa)
sys.exit()
######################################
import requests 
import json 
import pandas as pd 
import numpy as np  
import datetime as dt  

##frequency = input("Please enter the frequency (1m/5m/30m/.../1h/6h/1d/ :  ")
frequency='1d'
def get_bars(symbol, interval=frequency):
    root_url = 'https://api.binance.com/api/v1/klines'
    url = root_url + '?symbol=' + symbol + '&interval=' + interval
    print(symbol,' url  --->',url)
    data=requests.get(url).json()
##    data = json.loads(requests.get(url).text)
    print(symbol, ' data ----> ',data)
    df = pd.DataFrame(data)
    df.columns = ['open_time',
                  'o', 'h', 'l', 'c', 'v',
                  'close_time', 'qav', 'num_trades',
                  'taker_base_vol', 'taker_quote_vol', 'ignore']
    df.index = [dt.datetime.fromtimestamp(x / 1000.0) for x in df.close_time]
    return df

