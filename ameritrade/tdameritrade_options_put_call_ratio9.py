import requests
import json
import pandas as pd
import Technicals



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

# summary
# loop via all tickers: ----> get_option_prices -->[call2,put2] ,get_option_prices_from_files*,one_min_stats
# price_quote (floating/not called)
# call2,put2,


def one_min_stats(i,datep_option_expiration,td_consumer_key,accountId):
    import datetime
    import time
    import pandas as pd
    from datetime import datetime as dt

    #####################################################################################################

    endpoint = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/pricehistory'
    full_url = endpoint.format(stock_ticker=i)
    page = requests.get(url=full_url,
                        params={'apikey' : td_consumer_key})
    params={'apikey' : td_consumer_key}
    content = json.loads(page.content)
    df=pd.DataFrame()
##    df['tick']=i
##    print(content, type(content))
##    print(content['candles'], type(content))
##    df=pd.DataFrame(content['candles'])
    
    for x in content['candles']:
        dfq=pd.DataFrame()
       
        
        ##        m=content['symbol']
##        print(x.items(),'   ',x.values())
##        print(content['symbol'],'   ')
        dfq=pd.DataFrame(x.values()).T
        df=pd.concat([dfq,df],axis=0,ignore_index=True)
        
        
        
        df['tick']=i
##        print(df.shape,' ppp')

##    ts = int(df['datetime'])
##    df['datetime']=datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
##    df['datetime']=datetime.datetime.utcfromtimestamp(df['datetime']).strftime('%Y-%m-%dT%H:%M:%SZ')
##    df['dd']=df['datetime']* 365 * 24 * 3600
##    import datetime    
##    from datetime import datetime
##    df['dd']=datetime.fromtimestamp(df['datetime']).strftime("%A, %B %d, %Y %I:%M:%S")

    
##    df['datetime'] = df['datetime']*3600*24*365
##    df['b']=''
##    import time
##    df['b']=time.ctime(df['datetime']*365*24*3600)
##    df['red']=df['close']-df['open']    
    df.columns =['open','high','low','close','volume','datetime','tick']
    df=df[['tick','datetime','open','high','low','close','volume']]
    df['red']=''
    df['vol_red']=''
    df['red']=df['close']-df['open']
    df['hourp']=''
    df['min']=''
    df['hour_min']=''
    df['s2']=''
    df['s3']=''
    red_p=[]
    red_n=[]
    red_g=[]
    red_total=[]
    for x in df.index:
        

##
        df['datetime'].loc[x]=pd.to_datetime(df['datetime'].loc[x], unit='ms').tz_localize('utc').tz_convert('US/Eastern')
        df['s2'].loc[x]=str(df['datetime'].loc[x]).split(' ')[0]
        df['s3'].loc[x]=str(df['datetime'].loc[x]).split(' ')[1]
####        df['datetime'].loc[x]=pandas.to_datetime(df['datetime'].loc[x],unit='ms')
####        df['datetime'].loc[x] = df['datetime'].loc[x].dt.strftime('%d-%m-%Y %I:%M:%S')
####        df['datetime'].loc[x]=time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(int(df['datetime'].loc[x])))
####        df['datetime'].loc[x]= pd.to_datetime(df['datetime'].loc[x], unit='ms')
##
##
####        print(df['datetime'].loc[x].hour,'     ',df['datetime'].loc[x].minute,' 9999999999999999999999')
##        df['hourp'].loc[x]=df['datetime'].loc[x].hour
##        df['min'].loc[x]=df['datetime'].loc[x].minute
##        df['hour_min'].loc[x]=str(df['hourp'].loc[x])+str('_')+str(df['min'].loc[x])
##
##        
##        df=df[df['datetime'].loc[x].minute=='9']
##        df['datetimec'].loc[x]=df.loc[df['datetime'].loc[x].hour isbetween '11']
##        print(df['datetimec'].loc[x])
        
        df['red'].loc[x]=df['close'].loc[x]-df['open'].loc[x]
        red_total.append(df['volume'].loc[x])
        if df['red'].loc[x] < 0:
            df['vol_red'].loc[x]=(df['volume'].loc[x])*-1
            red_n.append(df['volume'].loc[x])
        elif df['red'].loc[x] > 0:
            df['vol_red'].loc[x]=df['volume'].loc[x]
            red_p.append(df['volume'].loc[x])
        elif df['red'].loc[x] == 0:
            red_g.append(df['volume'].loc[x])

##        df.loc[df['hourp'] >= '09'] & df.loc[df['hourp'] <= '17']

    
    
    print(df,'9999')
##    print(df.columns)
##    print(df.head(24*60),'last 30 mins')
    
##    df.loc[df['datetime'] > str('2022-05-25 15:11:00-04:00')]
##    df.loc[df['datetime'] < str('2022-05-25 12:05:00-04:00')]
    
    print(df['s2'].unique(),' ======================== ppp7777')
    dfm=df.loc[df['s2'] == df['s2'].unique()[0]]
    print(dfm,' filtered for today --- 4442')
    pp=sum(red_p)-sum(red_n)
    
    print('Volume ','  More shares old or bought(x)=',pp,'\n','   shares nuetral(y)=',sum(red_g),'\n','   delta (x-y)',pp-sum(red_g))
    print('Total Volume=',sum(red_total))
    print('Volume_Bought=',sum(red_p),' / ',sum(red_p)/sum(red_total)*100,' %')
    print('Volume_Sold=',sum(red_n),'  / ',sum(red_n)/sum(red_total)*100,' %')
    print('volume_neutral=',sum(red_g),'  / ',sum(red_g)/sum(red_total)*100,' %')

##    df.loc[df['s2'].isin([df['s2'].unique()[0],df['s2'].unique()[1]])]
           
##    df.loc[df['datetime'].isin([str('2022-05-30 01:00:00-04:00'),str('2022-05-31 16:05:00-04:00')])]
##    print(df,'   filtered')

    return(df)
    print('\n\n')

##    print(df['vol_red'].head(60).sum(),'  30 mins red')
##    print(df['vol_red'].head(30).sum(),'  30 mins red')
##    try:
##        print(i,'   ',df['vol_red'].head(15).sum(),'  15 mins red')
##        print(i,'    ',df['vol_red'].head(5).sum(),'   5 mins red')
##        print(i,'     ',df['vol_red'].head(2).sum(),'   2 mins red')
##    except:
##        print('')
##    print('\n\n')
##    print('\n\n')
##    df=pd.DataFrame()
##    for x in content.keys():
##        print(content.values())
##        
####        print(x,'   ',type(content[x]))
##        df=pd.DataFrame(content[x].values())
##        print(x,'   ',content[x])
##        print('\n\n\n')
##    print(content.values())
##    print(df)
##    print('\n',df.shape)


    
#####################################################################################################



def price_quote(i,datep_option_expiration,td_consumer_key,accountId):
        #####################################################################################################
    endpoint = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/quotes?'
    full_url = endpoint.format(stock_ticker=i)
    page = requests.get(url=full_url,
    params={'apikey' : td_consumer_key})
    content = json.loads(page.content)
    ####print(content)
    ####print(type(content))
    for x in content.keys():
        print(content[x].keys())
        print('\n\n')
        df=pd.DataFrame()
    ####    print(x,'   ',content[x])
##        if content[x].keys() is 'cusip':
        print('\n')
##        print(content[x].keys())
        df=pd.DataFrame(content[x].values()).T
        print(df.shape,'ddd')
        
        try: df.columns=['assetType', 'assetMainType', 'cusip', 'symbol', \
                    'description', 'bidPrice', 'bidSize', 'bidId', 'askPrice', \
                    'askSize', 'askId', 'lastPrice', 'lastSize', 'lastId', 'openPrice',\
                    'highPrice', 'lowPrice', 'bidTick', 'closePrice', 'netChange', 'totalVolume', \
                    'quoteTimeInLong', 'tradeTimeInLong', 'mark', 'exchange', 'exchangeName', \
                    'marginable', 'shortable', 'volatility', 'digits', '52WkHigh', '52WkLow', \
                    'nAV', 'peRatio', 'divAmount', 'divYield', 'divDate', 'securityStatus', \
                    'regularMarketLastPrice', 'regularMarketLastSize', 'regularMarketNetChange',\
                    'regularMarketTradeTimeInLong', 'netPercentChangeInDouble', 'markChangeInDouble',\
                    'markPercentChangeInDouble', 'regularMarketPercentChangeInDouble', 'delayed', 'realtimeEntitled']
        except:
            df.columns=['assetType', 'assetMainType', 'cusip', 'assetSubType', 'symbol', 'description', 'bidPrice', 'bidSize', 'bidId', 'askPrice',\
                        'askSize', 'askId', 'lastPrice', 'lastSize', 'lastId', 'openPrice', 'highPrice', 'lowPrice', 'bidTick', 'closePrice',\
                        'netChange', 'totalVolume', 'quoteTimeInLong', 'tradeTimeInLong', 'mark', 'exchange', 'exchangeName', 'marginable',\
                        'shortable', 'volatility', 'digits', '52WkHigh', '52WkLow', 'nAV', 'peRatio', 'divAmount', 'divYield', 'divDate', \
                        'securityStatus', 'regularMarketLastPrice', 'regularMarketLastSize', 'regularMarketNetChange', 'regularMarketTradeTimeInLong',\
                        'netPercentChangeInDouble', 'markChangeInDouble', 'markPercentChangeInDouble', 'regularMarketPercentChangeInDouble', 'delayed',\
                        'realtimeEntitled']
            
        print('\n')

##        print(df)
        print(df[['symbol','mark','regularMarketLastPrice','regularMarketNetChange','totalVolume','openPrice','lowPrice','highPrice','closePrice','52WkHigh', '52WkLow','volatility']])    
##            print(x,' ----  ',content[x].keys(),'   ',content[x].values())
##            print('\n\n\n')
##    print(content.values())

    #####################################################################################################


def call2(ticker,datep_option_expiration,td_consumer_key,accountId):
    import requests
    import json
    import pandas as pd
##    print('--  ',ticker)
##    print('inside call2========================================================================================================================')    
    stock_ticker = ticker
    contractType = 'CALL'
    date=datep_option_expiration
##    print(date)
##    print(stock_ticker)
    base_url = 'https://api.tdameritrade.com/v1/marketdata/chains?&symbol={stock_ticker}&contractType={contractType}&fromDate={date}&toDate={date}'
    endpoint = base_url.format(stock_ticker = ticker,contractType = 'CALL',date=datep_option_expiration)
    page = requests.get(url=endpoint,params={'apikey' : td_consumer_key})
    try:
        print(page.status_code)
        content = json.loads(page.content)
##        print(content,'   ',ticker)
        return(content)
    except:
        pass
        
##    content = json.loads(page.content)
####    print(content,'   calls ',ticker,'   expiration: ',datep_option_expiration)
####    print(type(content),'   ',ticker)
##    return(content)

def put2(ticker,datep_option_expiration,td_consumer_key,accountId):
    import requests
    import json
    import pandas as pd
##    print('\n')
##    print('======= inside put2 ===============','   ',ticker)
    
    stock_ticker = ticker
    contractType = 'PUT'
    date=datep_option_expiration

    base_url = 'https://api.tdameritrade.com/v1/marketdata/chains?&symbol={stock_ticker}&contractType={contractType}&fromDate={date}&toDate={date}'
    

##    
##    base_url = 'https://api.tdameritrade.com/v1/marketdata/chains?&symbol={stock_ticker}&contractType=PUT&fromDate={date}&toDate={date}'
    endpoint = base_url.format(stock_ticker = ticker,contractType = 'PUT',date=datep_option_expiration)
    page = requests.get(url=endpoint, params={'apikey' : td_consumer_key})
    try:
##        print(page.status_code)
        content = json.loads(page.content)
        return(content)
    except:
##        print('nnnnnn')
        pass
  
    
    
##    print(content, '   puts',ticker,'   expiration: ',datep_option_expiration)
##    print('\n\n')
    


import time
td_consumer_key=str('CLIFWQTIZ6EBH0BD3BVY4TASYUXMINAN')
accountId = '235471191'


def get_option_prices(z,datep_option_expiration):
    import json
    import _pickle as pickle
    import requests
    import pandas as pd

    dir = '/home/az2/Downloads/44pp'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
    
    td_consumer_key='CLIFWQTIZ6EBH0BD3BVY4TASYUXMINAN'
    df_calls=pd.DataFrame()
    df_puts=pd.DataFrame()

    df3=call2(z,datep_option_expiration,td_consumer_key,accountId)  ########################################################################## fucn call
        

##        print(df3)
    f= open(str('/home/az2/Downloads/44pp/')+str(z)+str('_')+str('calls.txt'), 'w+')
    f.write(str(df3))
    f.close()



    
##    df3.to_csv('/home/az2/Downloads/44pp'+str(m)+str('_')+str('calls.csv'))
    ##time.strftime(str(45))
    ##    time.sleep(2)
    df4=put2(z,datep_option_expiration,td_consumer_key,accountId) ############################################################################# func call
    f=open(str('/home/az2/Downloads/44pp/')+str(z)+str('_')+str('puts.txt'), 'w+')
    f.write(str(df4))
    f.close()

##    print('files saved at ','/home/az2/Downloads/44pp/')
    return(df3,df4)




def get_option_prices_from_files(QQQ,datep_option_expiration):        
    import json
    import ast
    import requests
    import pandas as pd
##    print('starting part 2')
    f=open(str('/home/az2/Downloads/44pp/')+str(QQQ)+str('_calls.txt'))
##    with open(str('/home/az2/Downloads/44pp/')+str(QQQ)+str('_calls.txt')) as f:
##    with open('/home/az2/Downloads/44pp/{QQQ}_calls.txt') as f:
    data = f.read()

    js = ast.literal_eval(data)
##    print(js)
##    print('\n\n')
    k=0

    import pandas as pd
    dfc=pd.DataFrame()
    for idx, rowm in js.items():
##        print(k,'   ',idx,'  ',rowm)
        if k==12 or k==13:
            k2=0
            for p1,p2 in rowm.items():
##                print(k2,'  ',p1,'   ',p2,'   ',ticker)
                k3=0
                for s2,s3 in p2.items():
##                    print(k3,'  ',s2,'     ',s3)
##                    print('\n')
                    k5=0
                    for n2b in s3:
##                        print(k3,'   ',s2,'   ','  ',n2b)
##                        print(type(n2b))
                        df3=pd.DataFrame([n2b])
                        dfc=pd.concat((dfc,df3),axis=0)
##                        print('\n')
                    k3=k3+1
                k2=k2+1
        k=k+1

##    print(dfc[['strikePrice','putCall','symbol','description','mark','bidSize','askSize','lastSize','theoreticalVolatility','totalVolume','daysToExpiration']])
##    print('Total Call Volume    ',dfc['totalVolume'].sum())
    f.close()




    

    f=open(str('/home/az2/Downloads/44pp/')+str(QQQ)+str('_puts.txt'))
##    print(f)
    data = f.read()
##    print(data,' nnn')
    ##    js = json.loads(data)
    ##    js = json.loads(data)
##        print(data)


    ##    for r,c in data.items():
    ##        print(r,'   ',c)

    ##js = json.loads(str(data))
    js = ast.literal_eval(data)
##    print(js)
##    print('\n\n')
    k=0

    import pandas as pd
    dfp=pd.DataFrame()
    for idx, rowm in js.items():
##        print(k,'   ',idx,'  ',rowm)
        if k==12 or k==13:
            k2=0
            for p1,p2 in rowm.items():
##                print(k2,'  ',p1,'   ',p2,'  ',ticker)
                k3=0
                for s2,s3 in p2.items():
##                    print(k3,'  ',s2,'     ',s3)
##                    print('\n')
                    k5=0
                    for n2b in s3:
##                        print(k3,'   ',s2,'   ','  ',n2b)
##                        print(type(n2b))
                        df3=pd.DataFrame([n2b])
                        dfp=pd.concat((dfp,df3),axis=0)
##                        print('\n')
                    k3=k3+1
                k2=k2+1
        k=k+1

##    print(dfp[['strikePrice','putCall','symbol','description','mark','bidSize','askSize','lastSize','theoreticalVolatility','totalVolume','daysToExpiration']])
##    print(dfp.shape,'44')
##    print(QQQ,'      expiration',datep_option_expiration,' ====================')
##    print('Total put volume: ',dfp['totalVolume'].sum())
    print(dfp,' puts 77', QQQ)
    print(dfc,' calls 77', QQQ)
    p=dfp['totalVolume'].sum()
    c=dfc['totalVolume'].sum()
    d=p/c
##    print('PCR=',round(d,3))
    return(QQQ,d,p-c,p,c)
##    print('Total put volume    ',dfp['totalVolume'].sum())     ,
    f.close()

import os

# 'TSLA','NVDA','TOL','SNOW','SPLK','DKS','DLTR','BIDU','DG','NTNX','NIO','BABA','ADSK','COST','MRVL','WDAY','ZS']

m=['AMC']
#m=['SPY','CHPT','GME','MULN','AVGO','LULU','CRWD','CHWY','APPS','HPQ','MDB']
##m=['NVDA','SPY','BABA','JD','WMT']
##m=['SPY','WMT','TSLA','NVDA','TOL','SNOW','SPLK','DKS','DLTR','BIDU','DG','NTNX','NIO','BABA','ADSK','COST','MRVL','WDAY','ZS']
##m=['toll','t']
##m=['spy','tsla','wmt','nvda','splk','dks','nio','adsk','cost','mrvl','wday','zs']

datep_option_expiration='2022-06-03'
##datep_option_expiration='2022-06-03'
##i='T'
##for i in m:
##    get_option_prices(str(i).upper(),'2022-05-27')
##    get_option_prices_from_files(i,datep_option_expiration)


##
gm2=[]
gm3=[]
gm4=[]
gm5=[]
gm6=[]


print(m,'   ',len(m))
for i in m:
##    print('\n')
    print(i)   
##    datep_option_expiration='2022-06-03'
##    QQQ=str(i)
### options    
##    df3,df4=get_option_prices(str(i).lower().upper(),datep_option_expiration)   ############ calls functions calls2,puts2 and get data as df3, df4
####    print(df3, ' call')
####    print(df4,'  put')
##    f2,f3,f4,f5,f6=get_option_prices_from_files(str(i).upper(),datep_option_expiration)
    df=one_min_stats(i,datep_option_expiration,td_consumer_key,accountId)
    Technicals(df)

##    
    gm2.append(f2)
    gm3.append(f3.round(2))
    gm4.append("{:,}".format(f4))
    gm5.append("{:,}".format(f5))
    gm6.append("{:,}".format(f6))



#### options
####print('\n\n')
##dff=pd.DataFrame({'ticker':gm2,'pcr':gm3,'delta_vol':gm4,'put_vol': gm5, 'call_vol':gm6})
####print(dff)
##print('\n')
##dff=dff.sort_values(by='pcr')
####dff['delta_vol'] = dff['delta_vol'].map('${:,}'.format)
####dff['put_vol'] = dff['put_vol'].map('${:,}'.format)
####dff['call_vol'] = dff['call_vol'].map('${:,}'.format)
##print(dff)
##
####print('\n')
####print(dff.sort_values(by='put_vol'))


    

