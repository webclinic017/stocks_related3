##
##import webbrowser 
##new = 2 # open in a new tab, if possible
##
### open a public URL, in this case, the webbrowser docs
##url = "http://docs.python.org"
##webbrowser.get(using='google-chrome').open(url,new=new)

import tda
from tda.auth import easy_client
from tda.client import Client

c = easy_client(
        api_key='CLIFWQTIZ6EBH0BD3BVY4TASYUXMINAN',
        redirect_uri='https://localhost',
        token_path='/usr/local/bin/chromedriver')

resp = c.get_price_history('AAPL',
        period_type=Client.PriceHistory.PeriodType.YEAR,
        period=Client.PriceHistory.Period.TWENTY_YEARS,
        frequency_type=Client.PriceHistory.FrequencyType.DAILY,
        frequency=Client.PriceHistory.Frequency.DAILY)
assert resp.status_code == httpx.codes.OK
history = resp.json()


##from selenium import webdriver
##
####url = "https://www.google.com/"
##
####driver.get(url)
####driver.maximize_window()
####time.sleep(15)
####
####driver.close()
##
####driver = webdriver.Firefox()
####driver = webdriver.Chrome("/usr/local/bin/chromedriver") # WINDOWS
####driver.get("http://www.google.com")
##
##
##URL = "http://www.google.com"
##
##driver = webdriver.Chrome()
##
##
### go to the google home page
##driver.get(URL);
