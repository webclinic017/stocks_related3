# Import libraries
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import os
import pandas as pd
import matplotlib.pyplot as plt
##matplotlib inline
# NLTK VADER for sentiment analysis
import nltk
##import sys
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# 

nltk.downloader.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer



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




finwiz_url = 'https://finviz.com/quote.ashx?t='
news_tables = {}
tickersm = ['wmt', 'TSLA', 'GOOG']
tickers=['AAPL', 'AFRM', 'AMAT', 'AMC', 'AMD', 'BA', 'BABA', 'DIS', 'FB', 'FUTU', 'IWM', 'JD', 'JPM', 'LCID', 'LGVN',
                         'MARA', 'MRNA', 'MRVL','MSFT', 'MU', 'NVDA', 'ORCL', 'PDD', 'PLUG', 'PTON', 'PYPL', 'QCOM', 'QQQ', 'RBLX', 'RIOT',
                         'SAVA', 'SOXL', 'SPXL', 'SPY', 'SQ', 'TNA', 'TQQQ', 'TSLA', 'TSM', 'V', 'XLK', 'XOP', 'XPEV', 'Z', 'MRNA', 'BNTX']



for ticker in tickers:
    url = finwiz_url + ticker
    req = Request(url=url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}) 
    response = urlopen(req)    
    # Read the contents of the file into 'html'
    html = BeautifulSoup(response)
    # Find 'news-table' in the Soup and load it into 'news_table'
    news_table = html.find(id='news-table')
    # Add the table to our dictionary
    news_tables[ticker] = news_table


parsed_news = []
# Iterate through the news
for file_name, news_table in news_tables.items():
    # Iterate through all tr tags in 'news_table'
    for x in news_table.findAll('tr'):
        # read the text from each tr tag into text
        # get text from a only
        text = x.a.get_text() 
        # splite text in the td tag into a list 
        date_scrape = x.td.text.split()
        # if the length of 'date_scrape' is 1, load 'time' as the only element
        if len(date_scrape) == 1:
            time = date_scrape[0]
            
        # else load 'date' as the 1st element and 'time' as the second    
        else:
            date = date_scrape[0]
            time = date_scrape[1]
        # Extract the ticker from the file name, get the string up to the 1st '_'  
        ticker = file_name.split('_')[0]
        
        # Append ticker, date, time and headline as a list to the 'parsed_news' list
        parsed_news.append([ticker, date, time, text])
        
        parsed_news[:15] # print first 5 rows of news

# Instantiate the sentiment intensity analyzer
vader = SentimentIntensityAnalyzer()
# Set column names
columns = ['ticker', 'date', 'time', 'headline']
# Convert the parsed_news list into a DataFrame called 'parsed_and_scored_news'
parsed_and_scored_news = pd.DataFrame(parsed_news, columns=columns)
# Iterate through the headlines and get the polarity scores using vader
scores = parsed_and_scored_news['headline'].apply(vader.polarity_scores).tolist()
# Convert the 'scores' list of dicts into a DataFrame
scores_df = pd.DataFrame(scores)
# Join the DataFrames of the news and the list of dicts
parsed_and_scored_news = parsed_and_scored_news.join(scores_df, rsuffix='_right')
# Convert the date column from string to datetime
parsed_and_scored_news['date'] = pd.to_datetime(parsed_and_scored_news.date).dt.date
##parsed_and_scored_news.head()
##print(parsed_and_scored_news.head())
df=parsed_and_scored_news
##print(df.loc[(df['date']=='2022-05-28')])
#df.loc[(df[['A', 'B', 'C']] < 0.5).any(axis=1)]
print(type(df['date']))
##print(df[df.date.str.match('2022-05-28')])
print(df.loc[df['date'].astype(str) == '2022-05-28'])
print(df.columns)

##parsed_and_scored_news=parsed_and_scored_news[(parsed_and_scored_news['date'] == '2022-05-28')]

##print(parsed_and_scored_news)
##
##
plt.rcParams['figure.figsize'] = [10, 6]
# Group by date and ticker columns from scored_news and calculate the mean
mean_scores = parsed_and_scored_news.groupby(['ticker','date']).mean()
# Unstack the column ticker
mean_scores = mean_scores.unstack()
# Get the cross-section of compound in the 'columns' axis
mean_scores = mean_scores.xs('compound', axis="columns").transpose()
# Plot a bar chart with pandas
mean_scores.plot(kind = 'bar')
plt.grid()
##plt.show()
##    
##















##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
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
##finviz_url = 'https://finviz.com/quote.ashx?t='
##news_tables = {}
##
##for ticker in tickers:
##    url = finviz_url + ticker
##    req = Request(url=url,headers={'user-agent': 'my-app/0.0.1'}) 
##    resp = urlopen(req)    
##    html = BeautifulSoup(resp, features="lxml")
##    news_table = html.find(id='news-table')
##    news_tables[ticker] = news_table
##
####try:
####    for ticker in tickers:
####        df = news_tables[ticker]
####        df_tr = df.findAll('tr')
####    
######        print ('\n')
######        print ('Recent News Headlines for {}: '.format(ticker))
####        
####        for i, table_row in enumerate(df_tr):
####            a_text = table_row.a.text
####            td_text = table_row.td.text
####            td_text = td_text.strip()
######            print(i,'   ',a_text,'(',td_text,')')
####            if i == n-1:
####                break
####except KeyError:
####    pass
####import sys
####print(df)
####print(df.shape)
####print(news_tables,' 555')
####
####sys.exit()
##
##
###''' 2nd
### Iterate through the news
##parsed_news = []
##i=0
##k=0
##
####for file_name, news_table in df.items():
##for file_name, news_table in news_tables.items():
##    k=0
####    print('\n\n')
##    print('************************* ',file_name,'   ', news_table,' ************************************************************************************************')
####    print('\n')
######    print(news_table,'   ',file_name)
##    for x in news_table.findAll('tr'):
####        print('i= ',i, '  file_name=',file_name, '   k=',k, ' -------------------------------------------------------------------------------')
####        print(file_name,' --- ',x,'   ',)
####        print('\n')    
##        text = x.a.get_text()
##    ##        print('\n\n')
##    ##        print(i,'    ',text)
##    ##        print('\n\n')
##        date_scrape = x.td.text.split()
##
##        if len(date_scrape) == 1:
##            time = date_scrape[0]
##            
##        else:
##            date = date_scrape[0]
##            time = date_scrape[1]
##
##        ticker = file_name.split('_')[0]
####        print('000000000000 ',date,'   ',text,'   ',x,'   ',file_name)
####        print(news_table,'   ',file_name)
##        if date=='May-27-22':
##            parsed_news.append([ticker, date, time, text])
####        print('ssss   ---- > ',parsed_news)
####        print('\n')
####        print('\n\n')
####        print(parsed_news[0][1])
####        print(len(parsed_news),'    ',parsed_news[0][1],parsed_news[0][0])
####        print('*************************************************************************************************************************')
####        print('\n')
##        k=k+1
##
##    print(parsed_news,' ----------77 ---- nnnnn')
##    i=i+1
##
##    print('******************************************************************************************************************************')
##
##        
####          
##
##
##
##
##import nltk
##import ssl
##
##try:
##    _create_unverified_https_context = ssl._create_unverified_context
##except AttributeError:
##    pass
##else:
##    ssl._create_default_https_context = _create_unverified_https_context
##
##
##
##for ticker in tickers:
##    nltk.download(ticker)
##
##    # Sentiment Analysis
##    analyzer = SentimentIntensityAnalyzer()
##
##    columns = ['Ticker', 'Date', 'Time', 'Headline']
##    news = pd.DataFrame(parsed_news, columns=columns)
##    scores = news['Headline'].apply(analyzer.polarity_scores).tolist()
##
##    df_scores = pd.DataFrame(scores)
##    news = news.join(df_scores, rsuffix='_right')
##
##
##    # View Data 
##    news['Date'] = pd.to_datetime(news.Date).dt.date
##
##    unique_ticker = news['Ticker'].unique().tolist()
##    news_dict = {name: news.loc[news['Ticker'] == name] for name in unique_ticker}
##
##    values = []
##    for ticker in tickers: 
##        dataframe = news_dict[ticker]
##        dataframe = dataframe.set_index('Ticker')
##        dataframe = dataframe.drop(columns = ['Headline'])
####        print ('\n')
####        print (dataframe.head(),'\n','***************************************** 4444 **********8')
##        
##        mean = round(dataframe['compound'].mean(), 2)
##        values.append(mean)
##        
##    df = pd.DataFrame(list(zip(tickers, values)), columns =['Ticker', 'Mean Sentiment']) 
##    df = df.set_index('Ticker')
##    df = df.sort_values('Mean Sentiment', ascending=False)
##    print ('\n')
##    print (df,'\n\n',' view data')
##
##
##
##
##
##''' # 2nd
##
##
################# possible repeat ###################################
##'''    
### Import libraries
##import pandas as pd
##from bs4 import BeautifulSoup
##import matplotlib.pyplot as plt
##from urllib.request import urlopen, Request
##from nltk.sentiment.vader import SentimentIntensityAnalyzer
##
### Parameters 
##n = 3 #the # of article headlines displayed per ticker
##tickers = ['AAPL', 'TSLA', 'AMZN']
##
### Get Data
##finwiz_url = 'https://finviz.com/quote.ashx?t='
##news_tables = {}
##
##for ticker in tickers:
##    url = finwiz_url + ticker
##    req = Request(url=url,headers={'user-agent': 'my-app/0.0.1'}) 
##    resp = urlopen(req)    
##    html = BeautifulSoup(resp, features="lxml")
##    news_table = html.find(id='news-table')
##    news_tables[ticker] = news_table
##
##try:
##    for ticker in tickers:
##        df = news_tables[ticker]
##        df_tr = df.findAll('tr')
##    
##        print ('\n')
##        print ('Recent News Headlines for {}: '.format(ticker))
##        
##        for i, table_row in enumerate(df_tr):
##            a_text = table_row.a.text
##            td_text = table_row.td.text
##            td_text = td_text.strip()
##            print(a_text,'(',td_text,')')
##            if i == n-1:
##                break
##except KeyError:
##    pass
##
### Iterate through the news
##parsed_news = []
##for file_name, news_table in news_tables.items():
##    for x in news_table.findAll('tr'):
##        text = x.a.get_text() 
##        date_scrape = x.td.text.split()
##
##        if len(date_scrape) == 1:
##            time = date_scrape[0]
##            
##        else:
##            date = date_scrape[0]
##            time = date_scrape[1]
##
##        ticker = file_name.split('_')[0]
##        
##        parsed_news.append([ticker, date, time, text])
##    
##    print(parsed_news.append,' ============ azhar ===========')
##
##
##'''        
### Sentiment Analysis
##analyzer = SentimentIntensityAnalyzer()
##
##columns = ['Ticker', 'Date', 'Time', 'Headline']
##news = pd.DataFrame(parsed_news, columns=columns)
##scores = news['Headline'].apply(analyzer.polarity_scores).tolist()
##
##df_scores = pd.DataFrame(scores)
##news = news.join(df_scores, rsuffix='_right')
##
##
### View Data 
##news['Date'] = pd.to_datetime(news.Date).dt.date
##
##unique_ticker = news['Ticker'].unique().tolist()
##news_dict = {name: news.loc[news['Ticker'] == name] for name in unique_ticker}
##
##values = []
##for ticker in tickers: 
##    dataframe = news_dict[ticker]
##    dataframe = dataframe.set_index('Ticker')
##    dataframe = dataframe.drop(columns = ['Headline'])
##    print ('\n')
##    print (dataframe.head())
##    
##    mean = round(dataframe['compound'].mean(), 2)
##    values.append(mean)
##    
##df = pd.DataFrame(list(zip(tickers, values)), columns =['Ticker', 'Mean Sentiment']) 
##df = df.set_index('Ticker')
##df = df.sort_values('Mean Sentiment', ascending=False)
##print ('\n')
##print (df)
##'''
