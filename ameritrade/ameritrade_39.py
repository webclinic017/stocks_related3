import requests
import json
td_consumer_key='CLIFWQTIZ6EBH0BD3BVY4TASYUXMINAN'
endpoint = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/quotes?'
full_url = endpoint.format(stock_ticker='spy')
page = requests.get(url=full_url,
                    params={'apikey' : td_consumer_key})
content = json.loads(page.content)
##print(content)
##print(type(content))
for x in content.keys():
##    print(x,'   ',content[x])
    print(x,'   ',content[x])
    print('\n\n\n')
print(content.values())
