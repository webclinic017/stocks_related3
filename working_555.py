import requests
import json
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



td_consumer_key='CLIFWQTIZ6EBH0BD3BVY4TASYUXMINAN'
accountId = '235471191'

##########################################################################################################
base_url = 'https://api.tdameritrade.com/v1/accounts/'+accountId+'/transactions'
endpoint=base_url.format(accountId)

account = requests.get(base_url)
##endpoint = base_url.format(stock_ticker = 'SPY',\
##    contractType = 'CALL',\
##    date='2022-05-30')
##page = requests.get(url=endpoint, 
##            params={'apikey' : td_consumer_key})
content = json.loads(account.content)
print(content)
############################################################################################################

##########################################################################################################
##base_url = 'https://api.tdameritrade.com/v1/accounts/{accountId}/transactions'
##endpoint = base_url.format(stock_ticker = 'SPY',\
##    contractType = 'CALL',\
##    date='2022-05-30')
##page = requests.get(url=endpoint, 
##            params={'apikey' : td_consumer_key})
##content = json.loads(page.content)
##print(content)
############################################################################################################
##5 Day / 1 Minute, including today's data:
##https://api.tdameritrade.com/v1/marketdata/XYZ/pricehistory?periodType=day&period=5&frequencyType=minute&frequency=1&endDate=1464825600000
## 
##5 Day / 1 Minute, excluding today's data:
##https://api.tdameritrade.com/v1/marketdata/XYZ/pricehistory?periodType=day&period=5&frequencyType=minute&frequency=1 
##
##6 Months / 1 Day, including today's data:
##https://api.tdameritrade.com/v1/marketdata/XYZ/pricehistory?periodType=month&frequencyType=daily&endDate=1464825600000
##Note that periodType=month is specified because the default periodType is day which is not compatible with the frequencyType daily
##
##Daily from May 25th, 2016 to today:
##https://api.tdameritrade.com/v1/marketdata/XYZ/pricehistory?periodType=month&frequencyType=daily&startDate=1464148800000&endDate=1464825600000
##

#####################################################################################################

##endpoint = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/pricehistory'
##full_url = endpoint.format(stock_ticker='AAL')
##page = requests.get(url=full_url,
##                    params={'apikey' : td_consumer_key})
##content = json.loads(page.content)
####print(content)
####print(type(content))
##for x in content.keys():
####    print(x,'   ',content[x])
##    print(x,'   ',content[x])
##    print('\n\n\n')
##print(content.values())
#####################################################################################################
