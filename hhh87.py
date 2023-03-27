##from rauth import OAuth1Service
##import webbrowser 
##
##def getSession():
##    print("jjj")
##    # Create a session
##    # Use actual consumer secret and key in place of 'foo' and 'bar'
##    service = OAuth1Service(
##              name = 'etrade',
##              consumer_key = '1974d0d9c9a1b6a303b5802f3dcba880',
##              consumer_secret = 'e62975961e15375b3abbbeb9946835b0b41e888bcb51fd9d9903f714d2374eac',
##              request_token_url = 'https://etws.etrade.com/oauth/request_token',
##              access_token_url = 'https://etws.etrade.com/oauth/access_token',
##              authorize_url = 'https://us.etrade.com/e/t/etws/authorize?key={}&token={}',
##              base_url = 'https://etws.etrade.com')
##
##    # Get request token and secret    
##    oauth_token, oauth_token_secret = service.get_request_token(params = 
##                                  {'oauth_callback': 'oob', 
##                                   'format': 'json'})
##    print("uuuu")
##   # Get request token and secret    
##    oauth_token, oauth_token_secret = service.get_request_token(params = 
##                                  {'oauth_callback': 'oob', 
##                                   'format': 'json'})
##    print("ooojj") 
##    auth_url = service.authorize_url.format(consumer_key, oauth_token)
##
##    # Get verifier (direct input in console, still working on callback)
##    webbrowser.open(auth_url)
##    verifier = input('Please input the verifier: ')
##
##    return service.get_auth_session(oauth_token, oauth_token_secret, params = {'oauth_verifier': verifier})
##
### Create a session
##session = getSession()
##print("step 1") 
### After authenticating a session, use sandbox urls
##url = 'https://etwssandbox.etrade.com/accounts/sandbox/rest/accountlist.json'
##
##resp = session.get(url, params = {'format': 'json'})
##
##print(resp)
##

################### ########## worked
from rauth import OAuth1Service
import webbrowser 

service = OAuth1Service(
          name = 'etrade',
          consumer_key = '1974d0d9c9a1b6a303b5802f3dcba880',
          consumer_secret = 'e62975961e15375b3abbbeb9946835b0b41e888bcb51fd9d9903f714d2374eac',
          request_token_url = 'https://apisb.etrade.com/oauth/request_token',
          access_token_url = 'https://apisb.etrade.com/oauth/access_token',
##          authorize_url = 'https://us.etrade.com/e/t/etws/authorize?key={}&token={}',
          authorize_url = 'https://us.etrade.com/e/t/etws/authorize?key={}&token={}',
##          base_url = 'https://apisb.etrade.com')
          base_url = 'https://us.etrade.com'),
          
##          base_url = 'https://etws.etrade.com')
##          request_token_url = 'https://etws.etrade.com/oauth/request_token',
        
##          authorize_url = 'https://us.etrade.com/e/t/etws/authorize?key={}&token={}',
##          base_url = 'https://etws.etrade.com')


oauth_token, oauth_token_secret = service.get_request_token(params =
       {'oauth_callback': 'oob', 
        'format': 'json'})
print(oauth_token)
print(oauth_token_secret)


auth_url = service.authorize_url.format('1974d0d9c9a1b6a303b5802f3dcba880', oauth_token)
webbrowser.open(auth_url)
verifier = input('Please input the verifier: ')

##session = service.get_auth_session(oauth_token, oauth_token_secret,verifier)
session = service.get_auth_session(oauth_token, oauth_token_secret, params = {'oauth_verifier': verifier})
print('cc ',oauth_token,'  ',verifier,'  ',oauth_token_secret)
url='https://api.etrade.com/v1/accounts/list'
##url = 'https://apisb.etrade.com/v1/accounts/list'
resp = session.get(url, params = {'format': 'json'})

print(resp.text)

###############
##
##import pyetrade
### Obtained secrets from Etrade for Sandbox or Live
##consumer_key = "1974d0d9c9a1b6a303b5802f3dcba880"
##consumer_secret = "e62975961e15375b3abbbeb9946835b0b41e888bcb51fd9d9903f714d2374eac"
### Using the EtradeOAuth object to retrive the URL to request tokens
##oauth = pyetrade.ETradeOAuth(consumer_key, consumer_secret)
##print(oauth.get_request_token()) # Use the printed URL
### Use the printed URL to retrive Verification code
##
##verifier_code = input("Enter verification code: ")
##tokens = oauth.get_access_token(verifier_code)
##print(tokens)


######################## 66
##from rauth import OAuth1Service
##import webbrowser 
##
##def getSession():
##    # Create a session
##    # Use actual consumer secret and key in place of 'foo' and 'bar'
##    service = OAuth1Service(
##              name = 'etrade',
##              consumer_key = "1974d0d9c9a1b6a303b5802f3dcba880",
##              consumer_secret = "e62975961e15375b3abbbeb9946835b0b41e888bcb51fd9d9903f714d2374eac",
##              request_token_url = 'https://etws.etrade.com/oauth/request_token',
##              access_token_url = 'https://etws.etrade.com/oauth/access_token',
##              authorize_url = 'https://us.etrade.com/e/t/etws/authorize?key={}&token={}',
##              base_url = 'https://etws.etrade.com')
##
##    # Get request token and secret    
##    oauth_token, oauth_token_secret = service.get_request_token(params = 
##                                  {'oauth_callback': 'oob', 
##                                   'format': 'json'})
##
##    auth_url = service.authorize_url.format(consumer_key, oauth_token)
##
##
##
##    # Get verifier (direct input in console, still working on callback)
##    webbrowser.open(auth_url)
##    verifier = input('Please input the verifier: ')
##
##    return service.get_auth_session(oauth_token, oauth_token_secret, params = {'oauth_verifier': verifier})
##
### Create a session
##session = getSession()
##
### After authenticating a session, use sandbox urls
##url = 'https://etwssandbox.etrade.com/accounts/sandbox/rest/accountlist.json'
##
##resp = session.get(url, params = {'format': 'json'})
##
##print(resp)
######################################################################
##
##from rauth import OAuth1Service
##import webbrowser 
##
##def getSession():
##    print("jere")
##    # Create a session
##    # Use actual consumer secret and key in place of 'foo' and 'bar'
##    service = OAuth1Service(
##              name = 'etrade',
##              consumer_key = '1974d0d9c9a1b6a303b5802f3dcba880',
##              consumer_secret = 'e62975961e15375b3abbbeb9946835b0b41e888bcb51fd9d9903f714d2374eac',
##              request_token_url = 'https://etws.etrade.com/oauth/request_token',
##              access_token_url = 'https://etws.etrade.com/oauth/access_token',
##              authorize_url = 'https://us.etrade.com/e/t/etws/authorize?key={}&token={}',
##              base_url = 'https://etws.etrade.com')
##
##
##    # Get request token and secret    
##    oauth_token, oauth_token_secret = service.get_request_token(params = 
##                                  {'oauth_callback': 'oob', 
##                                   'format': 'json'})
##
##    auth_url = service.authorize_url.format(consumer_key, oauth_token)
##
##    # Get verifier (direct input in console, still working on callback)
##    webbrowser.open(auth_url)
##    verifier = input('Please input the verifier: ')
##
##    return service.get_auth_session(oauth_token, oauth_token_secret, params = {'oauth_verifier': verifier})
##
### Main Create a session
##session = getSession()
##
### After authenticating a session, use sandbox urls
##url = 'https://etwssandbox.etrade.com/accounts/sandbox/rest/accountlist.json'
##
##resp = session.get(url, params = {'format': 'json'})
##
##print(resp)


##from rauth import OAuth1Service
##import webbrowser 
##
##service = OAuth1Service(
##          name = 'etrade',
##          consumer_key = '1974d0d9c9a1b6a303b5802f3dcba880',
##          consumer_secret = 'e62975961e15375b3abbbeb9946835b0b41e888bcb51fd9d9903f714d2374eac',
####          consumer_key = '85b4f5c99e7bbcb6e4f06f2f8fa703d5',
####          consumer_secret = '76b2f46f79e1b21e4a2ab88ee071e7d2e7587a5ad646d0a5332cc083360cc44',
##          request_token_url = 'https://apisb.etrade.com/oauth/request_token',
##          
##          
##          authorize_url = 'https://us.etrade.com/e/t/etws/authorize?key={}&token={}',
##
####          base_url = 'https://apisb.etrade.com')
##          base_url="https://api.etrade.com")
##
##
##oauth_token, oauth_token_secret = service.get_request_token(params =
##       {'oauth_callback': 'oob', 
##        'format': 'json'})
##
##auth_url = service.authorize_url.format('foo again', oauth_token)
##webbrowser.open(auth_url)
##verifier = input('Please input the verifier: ')
##session = service.get_auth_session(oauth_token, oauth_token_secret, params = {'oauth_verifier': verifier})
##
##url='https://api.etrade.com/v1/accounts/list'
####url = 'https://apisb.etrade.com/v1/accounts/list'
##resp = session.get(url, params = {'format': 'json'})
##
##print(resp.text)



##from rauth import OAuth1Service
##import webbrowser 
##
##def getSession():
##    print("# Create a session")
##    # Use actual consumer secret and key in place of 'foo' and 'bar'
##    service = OAuth1Service(
##              name = 'etrade',
##              consumer_key = '1974d0d9c9a1b6a303b5802f3dcba880',
##              consumer_secret = 'e62975961e15375b3abbbeb9946835b0b41e888bcb51fd9d9903f714d2374eac',
####              request_token_url = 'https://etws.etrade.com/oauth/request_token',
##              request_token_url = 'https://api.etrade.com/oauth/request_token',
##              access_token_url = 'https://api.etrade.com/oauth/access_token',
####              access_token_url = 'https://etws.etrade.com/oauth/access_token',
##              authorize_url = 'https://us.etrade.com/e/t/etws/authorize?key={}&token={}',
##              base_url = 'https://etws.etrade.com')
##
##    
##    print(service)
##    # Get request token and secret    
##    oauth_token, oauth_token_secret = service.get_request_token(params = 
##                                  {'oauth_callback': 'oob', 
##                                   'format': 'json'})
##    print(oauth_token)
##    auth_url = service.authorize_url.format(consumer_key, oauth_token)
##
##    # Get verifier (direct input in console, still working on callback)
##    print(auth_url)
##    webbrowser.open(auth_url)
##    verifier = input('Please input the verifier: ')
##
##    return service.get_auth_session(oauth_token, oauth_token_secret, params = {'oauth_verifier': verifier})
##
### Create a session
##session = getSession()
##
### After authenticating a session, use sandbox urls
##url = 'https://etwssandbox.etrade.com/accounts/sandbox/rest/accountlist.json'
##
##resp = session.get(url, params = {'format': 'json'})
##
##print(resp)
