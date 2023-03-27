


import webbrowser 
new = 2 # open in a new tab, if possible

# open a public URL, in this case, the webbrowser docs
url = "http://docs.python.org"
webbrowser.get(using='google-chrome').open(url,new=new)






























##from tda import auth,utils,client
##import json
##from selenium import webdriver
##from selenium.webdriver.chrome.options import Options
####options = webdriver.ChromeOptions()
####options.binary_location = which('google-chrome') or which('chrome') or which('chromium')
####url = 'https://auth.tdameritrade.com/auth?response_type=code&redirect_uri=' + up.quote(redirect_uri) + '&client_id=' + up.quote(client_id)
##chrome_driver_binary =  "/usr/local/bin/chromedriver"
##driver = webdriver.Chrome(chrome_driver_binary, options=Options())
##
##
####url='http://www.yahoo.com'
####driver.get(url)
##redirect_uri='https://127.0.0.1:8080'
##client_id='CLIFWQTIZ6EBH0BD3BVY4TASYUXMINAN'
##accountId='235471191'
####client_id = client_id + '@AMER.OAUTHAP'
####url = 'https://api.tdameritrade.com/v1/accounts/{accountId}/orders'
####driver.get(url)
##id='india'
##r = requests.get(f'https://example.com/')
##content = json.loads(r.content)
##print(content)

##
##
##token_path="/usr/local/bin/chromedriver"
##api_key='CLIFWQTIZ6EBH0BD3BVY4TASYUXMINAN'
##
##
##try:
##    c = auth.client_from_token_file(token_path, api_key)
##except FileNotFoundError:
##    print('nnnnn')
####    from selenium import webdriver
####    with webdriver.Chrome() as driver:
####        browser = webdriver.Chrome()
####
####        c = auth.client_from_login_flow(
####            driver, config.api_key, config.redirect_uri, config.token_path)
##
##print(c,' nnnnn')            
##print(c.get_quote("SPDR").json())
##











##import os
##import os.path
##import sys
##import time
##import urllib.parse as up
##from shutil import which
##from selenium import webdriver
##import requests
##options.binary_location = which('google-chrome') or which('chrome') or which('chromium')
##chrome_driver_binary = which('chromedriver') or "/usr/local/bin/chromedriver"
##driver = webdriver.Chrome(chrome_driver_binary, options=Options())
##
##
##from tda import auth,utils,client
####from tda.orders.equities
####from tda.client.Client.Account.Field
####from tda.client import Client
##
##c=auth.client_from_token_file('token','CLIFWQTIZ6EBH0BD3BVY4TASYUXMINAN')
##

##c = easy_client(
##        api_key='CLIFWQTIZ6EBH0BD3BVY4TASYUXMINAN',
####        redirect_uri='https://localhost',
##        redirect_uri='https://localhost.com',
####        token_path='/tmp/token.json'),
##        CHROMEDRIVER_PATH=web.Chrome('/usr/bin/chromedriver')
##        token_path='token')
##
##        api_key='CLIFWQTIZ6EBH0BD3BVY4TASYUXMINAN',
##        redirect_uri='https://localhost.com',
##        token_path=config.TOKEN_PATH)
##stream_client = StreamClient(client, account_id=config.ACCOUNT_ID)
##        
##resp = c.get_price_history('HSTO',
##        period_type=Client.PriceHistory.PeriodType.YEAR,
##        period=Client.PriceHistory.Period.TWENTY_YEARS,
##        frequency_type=Client.PriceHistory.FrequencyType.DAILY,
##        frequency=Client.PriceHistory.Frequency.DAILY)
##assert resp.status_code == httpx.codes.OK
##history = resp.json()
##
##print(history)
