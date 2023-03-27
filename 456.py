import asyncio
import json
import tda
from selenium import webdriver
import time
token_path = '/usr/local/bin/chromedriver'
api_key = 'CLIFWQTIZ6EBH0BD3BVY4TASYUXMINAN'
redirect_url = 'https://127.0.0.1'
primary_account_id = 1234567890
driver = webdriver.Chrome()
##print(time,' ------------------')
##import logging
##logging.getLogger('').addHandler(logging.StreamHandler())

c=tda.auth.client_from_login_flow(webdriver, api_key, redirect_url, token_path,\
                                redirect_wait_time_seconds=0.1, max_waits=3000, asyncio=False, token_write_func=None, enforce_enums=True)
##d=tda.auth.client_from_manual_flow(api_key, redirect_url, token_path, asyncio=False, token_write_func=None, enforce_enums=True)

##v=tda.auth.client_from_token_file(token_path, api_key, asyncio=False, enforce_enums=True)

##n=tda.auth.easy_client(api_key, redirect_url, token_path, webdriver_func=None, asyncio=False, enforce_enums=True)
##from selenium import webdriver
##import chromedriver_binary  # Adds chromedriver binary to path
##
##driver = webdriver.Chrome()
##driver.get("http://www.python.org")
