from yahoo_fin import options 
import pandas as pd
import yfinance as yf
from yahoo_fin import stock_info as f
import numpy as np 
from numerize import numerize 
import sys
import datetime
import re

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
response = urllib.request.urlopen('https://www.python.org')
print(response.read().decode('utf-8'))


from datetime import date
from termcolor import colored
pd.options.display.max_columns = 50
pd.options.display.max_rows = 1000
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



ticker='MRNA'
g=yf.Ticker(ticker)
####print(g.analysis())
##print('\n')
##
##print(g.recommendations)
##print('\n')
##print(g.analysis)
##print('\n')
##print(g.cashflow)
##print('\n')
##print(g.get_earnings)
##print('\n')
##print(g.get_institutional_holders)
##print('\n')
##print(g.major_holders)
##print('\n')
##print(g.get_mutualfund_holders)
##print('\n')
##print(g.mutualfund_holders)
##print('\n')
##print(g.cashflow)
##print('\n')
##print(g.quarterly_cashflow)
##print('\n')
##print(g.calendar)
##print('\n')
##print(g.options)
##df=pd.DataFrame(g.option_chain(g.options[0]))
####print(g.option_chain(g.options[0]))
##print(g.option_chain(g.options[0]))

gg = options.get_expiration_dates(ticker)
print(gg)
chain = options.get_calls('MRNA')
print(chain)
