def bb32():
    import requests
    from urllib.parse import unquote

    geturl=r'https://www.barchart.com/futures/quotes/CLJ19/all-futures'
    apiurl=r'https://www.barchart.com/proxies/core-api/v1/quotes/get'


    getheaders={

        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
        }

    getpay={
        'page': 'all'
    }

    s=requests.Session()
    r=s.get(geturl,params=getpay, headers=getheaders)



    headers={
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'referer': 'https://www.barchart.com/futures/quotes/CLJ19/all-futures?page=all',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        'x-xsrf-token': unquote(unquote(s.cookies.get_dict()['XSRF-TOKEN']))

    }
    payload={
        'fields': 'symbol,contractSymbol,lastPrice,priceChange,openPrice,highPrice,lowPrice,previousPrice,volume,openInterest,tradeTime,symbolCode,symbolType,hasOptions',
        'list': 'futures.contractInRoot',
        'root': 'CL',
        'meta': 'field.shortName,field.type,field.description',
        'hasOptions': 'true',
        'raw': '1'

    }

def bb33():
    import json
    import requests
    from urllib.parse import unquote
    import pandas as pd
    df=pd.DataFrame()
    print('This one works')

        
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



    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0"
    }

    url = "https://www.barchart.com/proxies/core-api/v1/quotes/get?list=options.mostActive.us&fields=symbol,symbolName,lastPrice,priceChange,percentChange,optionsTotalVolume,optionsWeightedImpliedVolatility,optionsImpliedVolatilityRank1y,optionsImpliedVolatilityPercentile1y,optionsWeightedImpliedVolatilityHigh1y,tradeTime,symbolCode,symbolType,hasOptions&between(lastPrice,.10,)=&between(tradeTime,2021-03-22,2021-03-23)=&orderBy=optionsTotalVolume&orderDir=desc&meta=field.shortName,field.type,field.description&hasOptions=true&page=1&limit=100&raw=1"

    with requests.Session() as s:
        # get all cookies
        s.get(
            "https://www.barchart.com/options/iv-rank-percentile/stocks",
            headers=headers,
        )
        # use one cookie as HTTP header
        headers["X-XSRF-TOKEN"] = unquote(s.cookies["XSRF-TOKEN"])
        data = s.get(url, headers=headers).json()


    # uncomment this to print all data:
    # print(json.dumps(data, indent=4))

    df=pd.DataFrame()
    df2=pd.DataFrame()
    for d in data["data"]:
##        print('\n')
##        print('****************************************************')
##        print(type(d))
        df2=df2.append(d, ignore_index=True)
##        k=0
##        for x,y in d.items():
##
##
##            
##            
####            print(df2)
##            
##            k=k+1
##            df=pd.concat((df2,df),axis=1)

##            if k==3:
##                break
            
##            print(df.shape,df)
##            print(x,'   ',y)
##        print('\n')
##        print("{:<8}{:<50}{}".format(d["symbol"], d["symbolName"], d["lastPrice"]))
##        df=df.append(df2)
    df=pd.concat((df2,df),axis=1)
    print('\n\n\n')        
    print(df)


def bb44():
    import pandas as pd
    from selenium import webdriver


    sp400_url= "https://www.barchart.com/stocks/indices/sp/sp400?page=all"
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    driver.get(sp400_url)

    html = driver.page_source

    df = pd.read_html(html)[-1]

    driver.close()

    symbolsList = list(df['Symbol'])
    print(symbolsList)

bb33()
bb44()


##import pandas as pd
##from bs4 import BeautifulSoup
##import matplotlib.pyplot as plt
##from urllib.request import urlopen
##from urllib.request import Request
##import nltk
##from nltk.sentiment.vader import SentimentIntensityAnalyzer
##import sys
##import ssl
##ssl._create_default_https_context = ssl._create_unverified_context
##
##
### Parameters 
##n = 3 #the # of article headlines displayed per ticker
##tickers = ['AMGN', 'AXP', 'BA', 'CAT', 'CRM', 'CSCO', 'CVX', 'DIS', 'DOW', 'GS', 'HD', 'HON', 'IBM',\
##            'WMT']
##
##nasdaq100=['AAPL', 'ADBE', 'ADI', 'ADP', 'ADSK', 'AEP', 'ALGN', 'AMAT', 'AMD', 'AMGN', 'AMZN', 'ANSS', 'ASML', 'ATVI', 'AVGO', 'BIDU', 'BIIB', 'BKNG', 'CDNS', 'CDW', 'CERN', 'CHKP', 'CHTR', 'CMCSA', 'COST', 'CPRT', 'CSCO', 'CSX', 'CTAS', 'CTSH', 'DLTR', 'DOCU', 'DXCM', 'EA', 'EBAY', 'EXC', 'FAST', 'FB', 'FISV', 'FOX', 'FOXA', 'GILD', 'GOOG', 'GOOGL', 'IDXX', 'ILMN', 'INCY', 'INTC', 'INTU', 'ISRG', 'JD', 'KDP', 'KHC', 'KLAC', 'LRCX', 'LULU', 'MAR', 'MCHP', 'MDLZ', 'MELI', 'MNST', 'MRNA', 'MRVL', 'MSFT', 'MU', 'NFLX', 'NTES', 'NVDA', 'NXPI', 'OKTA', 'ORLY', 'PAYX', 'PCAR', 'PDD', 'PEP', 'PTON', 'PYPL', 'QCOM', 'REGN', 'ROST', 'SBUX', 'SGEN', 'SIRI', 'SPLK', 'SWKS', 'TCOM', 'TEAM', 'TMUS', 'TSLA', 
##'TXN', 'VRSK', 'VRSN', 'VRTX', 'WBA', 'WDAY', 'XEL', 'XLNX', 'ZM']
##
### Get Data
####finviz_url = 'https://finviz.com/quote.ashx?t='
##
##news_tables = {}
##
##for ticker in tickers:
##    finviz_url='https://www.barchart.com/stocks/quotes/AMD/overview'
####    finviz_url=str('https://www.barchart.com/stocks/quotes/')+str(tickers)+str('/overview')
##    url = finviz_url
##    req = Request(url=url,headers={'user-agent': 'my-app/0.0.1'}) 
##    resp = urlopen(req)    
##    html = BeautifulSoup(resp, features="lxml")
##    print(html)
####    news_table = html.find(id='news-table')
####    news_tables[ticker] = news_table
##


'''
##try:
##    for ticker in tickers:
##        df = news_tables[ticker]
##        df_tr = df.findAll('tr')
##    
####        print ('\n')
####        print ('Recent News Headlines for {}: '.format(ticker))
##        
##        for i, table_row in enumerate(df_tr):
##            a_text = table_row.a.text
##            td_text = table_row.td.text
##            td_text = td_text.strip()
####            print(i,'   ',a_text,'(',td_text,')')
##            if i == n-1:
##                break
##except KeyError:
##    pass
##import sys
##print(df)
##print(df.shape)
##print(news_tables,' 555')
##
##sys.exit()



# Iterate through the news
parsed_news = []
i=0
k=0

##for file_name, news_table in df.items():
for file_name, news_table in news_tables.items():
    k=0
##    print('\n\n')
    print('************************* ',file_name,'   ', news_table,' ************************************************************************************************')
##    print('\n')
####    print(news_table,'   ',file_name)
    for x in news_table.findAll('tr'):
##        print('i= ',i, '  file_name=',file_name, '   k=',k, ' -------------------------------------------------------------------------------')
##        print(file_name,' --- ',x,'   ',)
##        print('\n')    
        text = x.a.get_text()
    ##        print('\n\n')
    ##        print(i,'    ',text)
    ##        print('\n\n')
        date_scrape = x.td.text.split()

        if len(date_scrape) == 1:
            time = date_scrape[0]
            
        else:
            date = date_scrape[0]
            time = date_scrape[1]

        ticker = file_name.split('_')[0]
##        print('000000000000 ',date,'   ',text,'   ',x,'   ',file_name)
##        print(news_table,'   ',file_name)
        if date=='May-27-22':
            parsed_news.append([ticker, date, time, text])
##        print('ssss   ---- > ',parsed_news)
##        print('\n')
##        print('\n\n')
##        print(parsed_news[0][1])
##        print(len(parsed_news),'    ',parsed_news[0][1],parsed_news[0][0])
##        print('*************************************************************************************************************************')
##        print('\n')
        k=k+1

    print(parsed_news,' ----------77 ---- nnnnn')
    i=i+1

    print('******************************************************************************************************************************')

'''
