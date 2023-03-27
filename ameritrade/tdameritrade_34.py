from tda.auth import easy_client
from tda.client import Client
from tda.streaming import StreamClient

import asyncio
import json
import config

client = easy_client(
        api_key=config.API_KEY,
        redirect_uri=config.REDIRECT_URI,
        token_path=config.TOKEN_PATH)
stream_client = StreamClient(client, account_id=config.ACCOUNT_ID)

def order_book_handler(msg):
    print(json.dumps(msg, indent=4))

async def read_stream():
    await stream_client.login()
    await stream_client.quality_of_service(StreamClient.QOSLevel.DELAYED)
    await stream_client.nasdaq_book_subs(['GOOG'])

    stream_client.add_nasdaq_book_handler(order_book_handler)

    while True:
        await stream_client.handle_message()

asyncio.get_event_loop().run_until_complete(read_stream())




















##from tda import auth, client
##from selenium import webdriver as web
##import json
##import config
##
### authenticate
##try:
##    c = auth.client_from_token_file(config.TOKEN_PATH, config.API_KEY)
##except FileNotFoundError:
##    from selenium import webdriver
##    with webdriver.Chrome(executable_path=config.CHROMEDRIVER_PATH) as driver:
##        c = auth.client_from_login_flow(
##            driver, config.API_KEY, config.REDIRECT_URI, config.TOKEN_PATH)


######################################################################
##from tda import auth, client
##import json
##import os
##from selenium import webdriver
##from selenium.webdriver.chrome.options import Options
##from selenium import webdriver as web
##
####token_path = '/path/to/token.json'
####token_path = 'https://api.tdameritrade.com/v1/oauth2/token'
##token_path = 'token'
##api_key = 'CLIFWQTIZ6EBH0BD3BVY4TASYUXMINAN'
##redirect_uri = 'https://localhost.com'
##chromedriver_path = web.Chrome('/usr/bin/chromedriver')
####chromedriver_path = os.getenv('$HOME')
##CHROMEDRIVER_PATH=chromedriver_path
##options = webdriver.ChromeOptions()
##driver = webdriver.Chrome(executable_path=str(chromedriver_path), options=options)
##try:
##    c = auth.client_from_token_file(token_path, api_key)
##except FileNotFoundError:
##    from selenium import webdriver
##    with webdriver.Chrome() as driver:
##        c = auth.client_from_login_flow(\
##            
##            driver, api_key, redirect_uri, token_path)
##
##r = c.get_price_history('AAPL',\
##        period_type=client.Client.PriceHistory.PeriodType.YEAR,\
##        period=client.Client.PriceHistory.Period.TWENTY_YEARS,\
##        frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,\
##        frequency=client.Client.PriceHistory.Frequency.DAILY)
##assert r.status_code == 200, r.raise_for_status()
##print(json.dumps(r.json(), indent=4))

######################################################################
##import selenium
##from selenium import webdriver as web
##
####url = 'https://www.wta.org/go-outside/hikes/hike_search? sort=&rating=0&mileage:float:list=0.0&mileage:float:list=25.0&title=&region=all&searchabletext=&filter=Search&subregion=all&b_start:int=0&show_incomplete=on&elevationgain:int:list=0&elevationgain:int:list=5000&highpoint='
##url = 'http://www.yahoo.com'
##
##driver = web.Chrome('/usr/bin/chromedriver')
##
##driver.get(url)
##
##driver.current_url()    

