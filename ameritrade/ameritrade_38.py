##import requests
##import pandas as pd
##import time
##import datetime
##
### tickers_list= ['AAPL', 'AMGN', 'AXP']
### print(len(tickers_list))
####historical=pd.DataFrame()
##key = 'CLIFWQTIZ6EBH0BD3BVY4TASYUXMINAN'
##def get_price_history(**kwargs):
##
##    url = 'https://api.tdameritrade.com/v1/marketdata/{}/pricehistory'.format(kwargs.get('symbol'))
##    params = {}
##    params.update({'apikey': key})
##
##    for arg in kwargs:
##        parameter = {arg: kwargs.get(arg)}
##        params.update(parameter)
##
##    return requests.get(url, params=params).json()
##
##tickers_list= ['AAPL', 'AMGN','WMT']
##for i in tickers_list:
##
##    # get data 1 year 1 day frequency -- good
##    # data=get_price_history(symbol=i, period=1, periodType='year', frequency=1, frequencyType='daily')
##    
##    data=get_price_history(symbol=i, endDate=1612418400000 , startDate=1612159200000,  frequency=1, frequencyType='daily')
##    print(i,'  ',data)
####    historical['date'] = pd.to_datetime(historical['datetime'], unit='ms')
####    info=pd.DataFrame(data['candles'])
####
####    historical=pd.concat([historical,info])
##
####historical
###################
##import requests
##import pandas as pd
##import numpy as np
##import datetime
##import tensorflow as tf
##from numpy import loadtxt
####from keras.models import Sequential
####from keras.layers import Dense
##import json
##print('ddd')
##apikey = 'CLIFWQTIZ6EBH0BD3BVY4TASYUXMINAN'

#The prices endpoint

#define endpoint

##endpoint = r"https://api.tdameritrade.com/v1/marketdata/{}/pricehistory".format('GOOG')
##
### define our payload
##
##payload = {'apikey': apikey,\
##          'endDate':'1648780967000',\
##          'startDate': '1207017767000',\
##           'periodType': 'year',\
##           'period':'1',\
##           'frequency': '1',\
####           'frequencyType': 'weekly'}
##           'frequencyType': 'daily'}
##
###make a request
##content = requests.get(url = endpoint, params = payload)
##
###convert it to a dictionary
##data = content.json()
##print(data)
##print(content)

#3333
##accountId = '235471191'
##
##acct_endpt = f"https://api.tdameritrade.com/v1/accounts/{accountId}"
####acct_endpt = 'https://api.tdameritrade.com/v1/accounts/{accountId}'
##full_url_acct = acct_endpt.format(accountId=accountId)
##
##account = requests.get(url=full_url_acct,
##                       params={'fields' : 'positions', 'apikey' : 'apikey'})
##
##acct_content = json.loads(account.content)
##print(acct_content)
print('ddd')
##import pprint
import pandas as pd
##import td
from config import consumer_key, redirect_uri, credentials_path
from tda import client
##from tda import TDClient
from selenium import webdriver as web

# Create a new instance of the client
td_client = client(client_id = 'CLIFWQTIZ6EBH0BD3BVY4TASYUXMINAN', \
                     redirect_uri = 'https://localhost.com', credentials_path = web.Chrome('/usr/bin/chromium-browser'))

# Login to a new session
td_client.login()

# Positions and Orders for an account or account(s)
positions = td_client.get_accounts(account = 'all', fields = ['positions'])
print('d44445 ',positions)
##pprint.pprint(positions)
