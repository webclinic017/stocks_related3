from tda.auth import easy_client
from tda.client import Client
from selenium import webdriver as web
TOKEN_ENDPOINT = 'https://api.tdameritrade.com/v1/oauth2/token'


c = easy_client(
        api_key='CLIFWQTIZ6EBH0BD3BVY4TASYUXMINAN',
        redirect_uri='https://127.0.0.1')
##        access_type: offline
##        grant_type: refresh_token
##        token_path=web.Chrome('/usr/bin/chromium-browser'))
##        token_path='/tmp/token.json')

##grant_type: authorization_code
##access_type: offline
##client_id: {Consumer Key} (e.g. EXAMPLE@AMER.OAUTHAP)
##redirect_uri: {REDIRECT URI} (e.g. https://127.0.0.1)

resp = c.get_price_history('AAPL',
        period_type=Client.PriceHistory.PeriodType.YEAR,
        period=Client.PriceHistory.Period.TWENTY_YEARS,
        frequency_type=Client.PriceHistory.FrequencyType.DAILY,
        frequency=Client.PriceHistory.Frequency.DAILY)
assert resp.status_code == httpx.codes.OK
history = resp.json()
print('nnn')













##from dotenv import load_dotenv
##import td_ameritrade_api as td
##from os import getenv
##
##refresh_token=None
####print(td.accounts.available_funds('235471191','CLIFWQTIZ6EBH0BD3BVY4TASYUXMINAN'))
##print(td.auth.access_token(refresh_token,'CLIFWQTIZ6EBH0BD3BVY4TASYUXMINAN'))


##load_dotenv()
##print('nn')
##client = td.client(getenv(REFRESH_TOKEN), getenv(CONSUMER_KEY), getenv(ACCOUNT_ID))
##print('kk')
##print(client.quote("AAPL"))
