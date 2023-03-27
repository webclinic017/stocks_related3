import os
import os.path
import sys
import time
import urllib.parse as up
from shutil import which
from selenium import webdriver
import requests


def authentication(client_id, redirect_uri, tdauser=None, tdapass=None):
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time
    from selenium.webdriver.common.keys import Keys
    from selenium import webdriver
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By

    
    options = webdriver.ChromeOptions()
    chrome_driver_binary =  "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(chrome_driver_binary, options=options)
##    driver.Chrome.start_client('https://192.168.1.70') 

    
    client_id = client_id + '@AMER.OAUTHAP'
##    url = 'https://auth.tdameritrade.com/auth?response_type=code&redirect_uri=' + up.quote(redirect_uri) + '&client_id=' + up.quote(client_id)
    
    url = 'https://auth.tdameritrade.com/auth?response_type=code&redirect_uri=' + redirect_uri + '&client_id=' + client_id
    print('\n')
    print((url),'                  ppppp'
          )

    driver.get(url)
    ubox = driver.find_element_by_id('username0').send_keys("azhar5245")
    ubox = driver.find_element_by_id('password1').send_keys("Karachi33")
    ubox = driver.find_element_by_id('accept').click()


##    print(driver.get('http://www.yahoo.com'),' 8888')
##    ubox = driver.find_element_by_id('ybar-sbq').send_keys("Linda Bromley,orange county")
##    ubox = driver.find_element_by_id('ybar-search').click()
##    driver.find_element_by_xpath("//unique_parent//input[@type="submit" and @value='something']").click()


'''
    print(driver.get('https://auth.tdameritrade.com/auth?response_type=code&redirect_uri=' + up.quote(redirect_uri) + '&client_id=' + up.quote(client_id)),' gggg')

    print(driver.get(url),'nnnn')
    if sys.platform == 'darwin':
        # MacOS
        if os.path.exists("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"):
            options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        elif os.path.exists("/Applications/Chrome.app/Contents/MacOS/Google Chrome"):
            options.binary_location = "/Applications/Chrome.app/Contents/MacOS/Google Chrome"
    elif 'linux' in sys.platform:
        # Linux
        options.binary_location = which('google-chrome') or which('chrome') or which('chromium')

    url = 'https://auth.tdameritrade.com/auth?response_type=code&redirect_uri=' + up.quote(redirect_uri) + '&client_id=' + up.quote(client_id)




    driver.get(url)

    # Set tdauser and tdapass from environemnt if TDAUSER and TDAPASS environment variables were defined
##    tdauser = tdauser or os.environ.get('TDAUSER', '')
##    tdapass = tdapass or os.environ.get('TDAPASS', '')
    tdauser='azhar5245'
    tdapass='Karachi33'

    # Fully automated oauth2 authentication (if tdauser and tdapass were intputed into the function, or found as
    # environment variables)
##    if tdauser and tdapass:

    print('enterrrrr')
    print(driver.get(url),'nnnn')
    ubox = driver.find_element_by_id('username').send_keys("azhar5245")
    
    pbox = driver.find_element_by_id('password').send_keys("Karachi33")
    ubox.click()
    ubox.send_keys("azhar5245")
    pbox.click()
    pbox.send_keys("Karachi33")
    driver.find_element_by_id('accept').click()

    driver.find_element_by_id('accept').click()
    while True:
        try:
            code = up.unquote(driver.current_url.split('code=')[1])
            if code != '':
                break
            else:
                time.sleep(5)
        except (TypeError, IndexError):
            pass
    else:
        input('Azhar --- after giving access, hit enter to continue')
        code = up.unquote(driver.current_url.split('code=')[1])

    driver.close()

    resp = requests.post('https://api.tdameritrade.com/v1/oauth2/token',
                         headers={'Content-Type': 'application/x-www-form-urlencoded'},
                         data={'grant_type': 'authorization_code',
                               'refresh_token': '',
                               'access_type': 'offline',
                               'code': code,
                               'client_id': client_id,
                               'redirect_uri': redirect_uri})
    if resp.status_code != 200:
        raise Exception('Could not authenticate!')
    return resp.json()


def access_token(refresh_token, client_id):
    resp = requests.post('https://api.tdameritrade.com/v1/oauth2/token',
                         headers={'Content-Type': 'application/x-www-form-urlencoded'},
                         data={'grant_type': 'refresh_token',
                               'refresh_token': refresh_token,
                               'client_id': client_id})
    if resp.status_code != 200:
        raise Exception('azhar what the heck --- Could not authenticate!')
    return resp.json()

'''
def main():
##    client_id = input('client id:')
##    redirect_uri = input('redirect uri:')
    client_id ='CLIFWQTIZ6EBH0BD3BVY4TASYUXMINAN'
##    redirect_uri ='https://127.0.0.1'
    redirect_uri ='https://192.168.1.70'
    print(authentication(client_id, redirect_uri))

main()
