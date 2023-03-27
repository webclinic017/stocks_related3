import requests
import json
import pandas as pd


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



##td_consumer_key='CLIFWQTIZ6EBH0BD3BVY4TASYUXMINAN'
##accountId = '235471191'
##
##ticker='DOCU'
##datep='2022-05-27'

##ticker=input(str("Enter Ticker ['ndx','^gspc','^dji','spy','arkk','qqq'] : "))
##datep=input(str('Enter Weekly option Date (example: "2022-05-16"): '))

#####################################################################################################
##endpoint = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/quotes?'
##full_url = endpoint.format(stock_ticker='spy')
##page = requests.get(url=full_url,
##                    params={'apikey' : td_consumer_key})
##content = json.loads(page.content)
####print(content)
####print(type(content))
##for x in content.keys():
####    print(x,'   ',content[x])
##    print(x,'   ',content[x])
##    print('\n\n\n')
##print(content.values())

#####################################################################################################

##endpoint = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/pricehistory'
##full_url = endpoint.format(stock_ticker='AAL')
##page = requests.get(url=full_url,
##                    params={'apikey' : td_consumer_key})
##content = json.loads(page.content)
####print(content)
####print(type(content))
##for x in content.keys():
####    print(x,'   ',content[x])
##    print(x,'   ',content[x])
##    print('\n\n\n')
##print(content.values())
#####################################################################################################


##endpoint = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/pricehistory?periodType={periodType}&period={period}&frequencyType={frequencyType}&frequency={frequency}'
##full_url = endpoint.format(stock_ticker='AAL',periodType='year',period=1,frequencyType='weekly',frequency=1)
##page = requests.get(url=full_url,
##                    params={'apikey' : td_consumer_key})
##content = json.loads(page.content)
##print(content)

#####################################################################################################
##
##base_url = 'https://api.tdameritrade.com/v1/instruments?&symbol={stock_ticker}&projection={projection}'
##endpoint = base_url.format(stock_ticker = 'AAL',
##    projection = 'fundamental')
##page = requests.get(url=endpoint, 
##            params={'apikey' : td_consumer_key})
##content = json.loads(page.content)
##print(content)
##########################################################################################################
##
##base_url = 'https://api.tdameritrade.com/v1/marketdata/chains?&symbol={stock_ticker}'
##endpoint = base_url.format(stock_ticker = 'AAL')
##page = requests.get(url=endpoint, 
##            params={'apikey' : td_consumer_key})
##content = json.loads(page.content)
##print(content)
##########################################################################################################
def call2(ticker,datep,td_consumer_key,accountId):
    import requests
    import json
    import pandas as pd
    print('--  ',ticker)
    print('inside call2========================================================================================================================')    
    stock_ticker = ticker
    contractType = 'CALL'
    date=datep
    print(date)
    print(stock_ticker)
    base_url = 'https://api.tdameritrade.com/v1/marketdata/chains?&symbol={stock_ticker}&contractType={contractType}&fromDate={date}&toDate={date}'
    endpoint = base_url.format(stock_ticker = ticker,contractType = 'CALL',date=datep)
    page = requests.get(url=endpoint,params={'apikey' : td_consumer_key})
    content = json.loads(page.content)
    print(content,'   calls ',ticker,'   expiration: ',datep)
##    print(type(content),'   ',ticker)
    return(content)
    ##print(content, '66')
    ##print('\n\n')
##################
##################    df=pd.DataFrame()
##################    df['symbol']=''
##################    tt=[]
##################
##################
##################    i=0
##################    for idx, row in content.items():
##################        l=content.keys()
####################        print(i,'    ',idx,'    ',row,'   777744' )
##################        pass
##################
##################
##################        if i < 11:
##################            pass
####################            print(i,'  ',idx,' ----> ',row,'    ')
##################
##################        if i==12:
##################    ##        print('************************ ----> *****************')
##################    ##        print('\n')
##################            p2_bidAskSize=[]
##################            p3_totalVolume=[]
##################            p4_description=[]
##################            p5_bid=[]
##################            p6_ask=[]
##################            p7_mark=[]
##################            p8_markChange=[]
##################            p9_volatility=[]
##################            p10_delta=[]
##################            p11_openPrice=[]
##################            p12_closePrice=[]
##################            p13_lowPrice=[]
##################            p14_highPrice=[]
##################            p15_spread=[]
##################            p16_daysToExpiration=[]
##################            p17_inTheMoney=[]
##################            nn=row
##################    ##        print(' ppppppppppp ',nn.items())
##################            for x,y in nn.items():
####################                print(x,' 442   ',y)
##################
##################                
##################
##################    ##            print('\n')
##################                for m,c in y.items():
##################
##################    ##                print(type(y))
##################                    
##################    ##                print('\n')
##################    ##                print(m+'   '+'PUT')
##################    ##                print(c)
##################                    for g2 in c:
####################                        print(g2)
##################    ##                    print('\n')
##################    ##                    print('************Strike price ***** ',m,' ********************')
##################    ##                    print('\n')
##################    ##                    print(g2,' rrr')
##################                        for k2,k3 in g2.items():
####################                            print(k2,'====   ',k3,'  dd')
##################     
##################                            if k2=='bidAskSize':
##################                                p2_bidAskSize.append(k3)
##################                            elif k2=='totalVolume':
##################                                p3_totalVolume.append(k3)
##################                            elif k2=='description':
##################                                p4_description.append(k3)
##################                            elif k2=='bid':
##################                                p5_bid.append(k3)
##################                            elif k2=='ask':
##################                                p6_ask.append(k3)
##################                            elif k2=='mark':
##################                                p7_mark.append(k3)                                
##################                            elif k2=='markChange':
##################                                p8_markChange.append(k3)
##################                            elif k2=='volatility':
##################                                p9_volatility.append(k3)
##################                            elif k2=='delta':
##################                                p10_delta.append(k3)
##################                            elif k2=='openPrice':
##################                                p11_openPrice.append(k3)    
##################                            elif k2=='closePrice':
##################                                p12_closePrice.append(k3)  
##################                            elif k2=='lowPrice':
##################                                p13_lowPrice.append(k3)  
##################                            elif k2=='highPrice':
##################                                p14_highPrice.append(k3)
##################                            elif k2=='daysToExpiration':
##################                                p16_daysToExpiration.append(k3)
##################                            elif k2=='inTheMoney':
##################                                p17_inTheMoney.append(k3)
##################                            elif k2=='bid':
##################                                p15_spread.append(k3['bid']-k3['ask'])      
##################        i=i+1
##################    ##
##################    ##
##################    ##
##################    ##
##################    ##print('\n\n\n')
##################    ##print(content.keys())
##################    ####p2_bidAskSize=[];p3_totalVolume=[];p4_description=[]
##################    df3=pd.DataFrame([p2_bidAskSize,p3_totalVolume,p4_description,p5_bid,\
##################                      p6_ask,p7_mark,p8_markChange,p9_volatility,p10_delta,\
##################                      p11_openPrice,p12_closePrice,p13_lowPrice,p14_highPrice,p16_daysToExpiration,p17_inTheMoney,p15_spread]).T
##################    df3.columns=['bidAskSize','totalVolume','description','bid','ask','mark','markChange','volatility','delta','openPrice','closePrice','lowPrice','highPrice'\
##################                 ,'daysToExpiration','inTheMoney','spread']
##################    ##
##################    ####print(len(p2_bidAskSize))
##################    print(df3,' df3 call',df3['totalVolume'].sum(),'   ',ticker)
##################    print('call stuff success','   ',ticker)
##################    return(df3)
########################################################################################################################
##########################################################################################################
def put2(ticker,datep,td_consumer_key,accountId):
    import requests
    import json
    import pandas as pd
##    print('\n')
##    print('======= inside put2 ===============','   ',ticker)
    
    stock_ticker = ticker
    contractType = 'PUT'
    date=datep

    base_url = 'https://api.tdameritrade.com/v1/marketdata/chains?&symbol={stock_ticker}&contractType={contractType}&fromDate={date}&toDate={date}'
 

##    
##    base_url = 'https://api.tdameritrade.com/v1/marketdata/chains?&symbol={stock_ticker}&contractType=PUT&fromDate={date}&toDate={date}'
    endpoint = base_url.format(stock_ticker = ticker,contractType = 'PUT',date=datep)
    page = requests.get(url=endpoint, params={'apikey' : td_consumer_key})
    content = json.loads(page.content)

    print(content, '   puts',ticker,'   expiration: ',datep)
    print('\n\n')
    return(content)

##################    df=pd.DataFrame()
##################    df['symbol']=''
##################    tt=[]
##################
##################
##################    i=0
##################    for idx, row in content.items():
##################        l=content.keys()
##################    ##    print(i,'    ',idx,'    ',row,'   777744' )
##################
##################
##################        if i < 11:
##################            pass
####################            print(i,'  ',idx,' ----> ',row,'    ')
##################
##################        if i==12:
##################            p2_bidAskSize=[]
##################            p3_totalVolume=[]
##################            p4_description=[]
##################            p5_bid=[]
##################            p6_ask=[]
##################            p7_mark=[]
##################            p8_markChange=[]
##################            p9_volatility=[]
##################            p10_delta=[]
##################            p11_openPrice=[]
##################            p12_closePrice=[]
##################            p13_lowPrice=[]
##################            p14_highPrice=[]
##################            p15_spread=[]
##################            p16_daysToExpiration=[]
##################            p17_inTheMoney=[]
##################    ##        print('************************ ----> *****************')
##################    ##        print('\n')
##################            nn=row
##################    ##        print(' ppppppppppp ',nn.items())
##################            for x,y in nn.items():
##################
##################                
##################
##################    ##            print('\n')
##################                for m,c in y.items():
##################
##################    ##                print(type(y))
##################                    
##################    ##                print('\n')
##################    ##                print(m+'   '+'PUT')
##################    ##                print(c)
##################                    for g2 in c:
##################    ##                    print(g2)
##################    ##                    print('\n')
##################    ##                    print('************Strike price ***** ',m,' ********************')
##################    ##                    print('\n')
##################    ##                    print(g2,' rrr')
##################                        for k2,k3 in g2.items():
##################    ##                        print(k2,k3,'  dd')
##################     
##################                            if k2=='bidAskSize':
##################                                p2_bidAskSize.append(k3)
##################                            elif k2=='totalVolume':
##################                                p3_totalVolume.append(k3)
##################                            elif k2=='description':
##################                                p4_description.append(k3)
##################                            elif k2=='bid':
##################                                p5_bid.append(k3)
##################                            elif k2=='ask':
##################                                p6_ask.append(k3)
##################                            elif k2=='mark':
##################                                p7_mark.append(k3)                                
##################                            elif k2=='markChange':
##################                                p8_markChange.append(k3)
##################                            elif k2=='volatility':
##################                                p9_volatility.append(k3)
##################                            elif k2=='delta':
##################                                p10_delta.append(k3)
##################                            elif k2=='openPrice':
##################                                p11_openPrice.append(k3)    
##################                            elif k2=='closePrice':
##################                                p12_closePrice.append(k3)  
##################                            elif k2=='lowPrice':
##################                                p13_lowPrice.append(k3)  
##################                            elif k2=='highPrice':
##################                                p14_highPrice.append(k3)
##################                            elif k2=='daysToExpiration':
##################                                p16_daysToExpiration.append(k3)
##################                            elif k2=='inTheMoney':
##################                                p17_inTheMoney.append(k3)
##################                            elif k2=='bid':
##################                                p15_spread.append(k3['bid']-k3['ask'])      
##################        i=i+1
##################    ##
##################    ##
##################    ##
##################    ##
##################    ##print('\n\n\n')
##################    ##print(content.keys())
##################    ####p2_bidAskSize=[];p3_totalVolume=[];p4_description=[]
##################    df4=pd.DataFrame([p2_bidAskSize,p3_totalVolume,p4_description,p5_bid,\
##################                      p6_ask,p7_mark,p8_markChange,p9_volatility,p10_delta,\
##################                      p11_openPrice,p12_closePrice,p13_lowPrice,p14_highPrice,p16_daysToExpiration,p17_inTheMoney,p15_spread]).T
##################    df4.columns=['bidAskSize','totalVolume','description','bid','ask','mark','markChange','volatility','delta','openPrice','closePrice','lowPrice','highPrice'\
##################                 ,'daysToExpiration','inTheMoney','spread']
##################    ##
##################    ####print(len(p2_bidAskSize))
##################    print(df4,' df4 PUT',df4['totalVolume'].sum(),'   ',ticker)
##################    print('put2 success','   ',ticker)
##################    return(df4)
   
###################################################################################################################################################

##base_url = 'https://api.tdameritrade.com/v1/marketdata/chains?&symbol={stock_ticker}&contractType={contractType}&fromDate={date}&toDate={date}'
##endpoint = base_url.format(stock_ticker = 'SPY',
##    contractType = 'PUT',
##    date='2022-05-09')
##page = requests.get(url=endpoint, 
##            params={'apikey' : td_consumer_key})
##content = json.loads(page.content)
##
####print(content)
##
##df=pd.DataFrame()
##df['symbol']=''
##tt=[]
##
##
##i=0
##for idx, row in content.items():
##    l=content.keys()
##
##
##    if i < 11:
##        pass
####        print(i,'  ',idx,' ----> ',row,'    ')
##
##    if i==12:
####        print('\n')
##        nn=row
####        print(' ppppppppppp ',nn.items())
##        for x,y in nn.items():
##            p2_bidAskSize=[]
##            p3_totalVolume=[]
##            p4_description=[]
##
####            print('\n')
##            for m,c in y.items():
##
####                print(type(y))
##                
##                print('\n')
####                print(m+'   '+'PUT')
####                print(c)
##                for g2 in c:
##
####                    print('***************** ',m,' ********************')
####                    print(g2)
##                    for k2,k3 in g2.items():
##                        if k2=='bidAskSize':
##                            p2_bidAskSize.append(k3)
##                        elif k2=='totalVolume':
##                            p3_totalVolume.append(k3)
##                        elif k2=='description':
##                            p4_description.append(k3)
##                            
##                        elif k2=='bid':
##                            p5_bid.append(k3)
##                        elif k2=='ask':
##                            p5_ask.append(k3)
##                        elif k2=='mark':
##                            p7_mark.append(k3)
##                        elif k2=='markChange':
##                            p8_markChange.append(k3)
##                        elif k2=='volatility':
##                            p9_volatility.append(k3)
##                        elif k2=='delta':
##                            p10_delta.append(k3)
##                        elif k2=='openPrice':
##                            p11_openPrice.append(k3)
##                        elif k2=='closePrice':
##                            p12_closePrice.append(k3)
##                        elif k2=='lowPrice':
##                            p13_lowPrice.append(k3)
##                        elif k2=='highPrice':
##                            p14_highPrice.append(k3)
##
##
##                            
##    i=i+1
##
####print('\n\n\n')
##print(content.keys())
####p2_bidAskSize=[];p3_totalVolume=[];p4_description=[]
##df4=pd.DataFrame([p2_bidAskSize,p3_totalVolume,p4_description]).T
##df4.columns=['bidAskSize','totalVolume','description']
##
####print(len(p2_bidAskSize))
##print(df4,' df4 put')
##

##########################################################################################################
##base_url = 'https://api.tdameritrade.com/v1/marketdata/chains?&symbol={stock_ticker}\
##&contractType={contract_type}&strike={strike}&fromDate={date}&toDate={date}'
##endpoint = base_url.format(stock_ticker = 'AAL',
##    contract_type = 'PUT',
##    strike = 9,
##    date='2020-06-19')
##page = requests.get(url=endpoint, 
##            params={'apikey' : td_consumer_key})
##content = json.loads(page.content)
##print(content)
############################################################################################################
##https://medium.com/analytics-vidhya/an-introduction-to-the-td-ameritrade-api-in-python-8c9d462e966c
#https://githubhelp.com/timkpaine/tdameritrade
# https://www.youtube.com/watch?v=sVA0PeuDE4I
##########################################################################################################
##base_url = 'https://api.tdameritrade.com/v1/accounts/{accountId}/transactions'
##endpoint = base_url.format(stock_ticker = 'SPY',\
##    contractType = 'CALL',\
##    date='2021-11-20')
##page = requests.get(url=endpoint, 
##            params={'apikey' : td_consumer_key})
##content = json.loads(page.content)
##print(content)
############################################################################################################

import time
td_consumer_key=str('CLIFWQTIZ6EBH0BD3BVY4TASYUXMINAN')
accountId = '235471191'

##ticker=input(str("Enter Ticker ['ndx','^gspc','^dji','spy','arkk','qqq'] : "))
##ticker='SPY'
##m=['^DJI','SPY']
##datep='2022-05-23'
##
##for ticker in m:
##    df3=call2(ticker,datep,td_consumer_key,accountId)
##    ##time.strftime(str(45))
####    time.sleep(2)
##    df4=put2(ticker,datep,td_consumer_key,accountId)
##    print('=====================================')
##    print('Ticker : ',ticker)
##    print('Call volume=',df3['totalVolume'].sum())
##    print('Put volume=', df4['totalVolume'].sum())
##    if df4['totalVolume'].sum()/df3['totalVolume'].sum() < 1:
##        print(ticker,' Put/Call volume=',round(df4['totalVolume'].sum()/df3['totalVolume'].sum(),2),'     ','put to call < 1', 'Upside-[buy_calls]-bullish')
##    elif df4['totalVolume'].sum()/df3['totalVolume'].sum() > 1:
##        print(ticker,' Put/Call volume=',round(df4['totalVolume'].sum()/df3['totalVolume'].sum(),2),'     ','put to call > 1', 'Downside-[buy_puts]-bearish')
##    accountId = '235471191'
##    del df3
##    del df4
##    print('=====================================')
####    time.sleep(5)
def get_indices(z,datep):
    import json
    import _pickle as pickle
    import requests
    import pandas as pd
    
    td_consumer_key='CLIFWQTIZ6EBH0BD3BVY4TASYUXMINAN'
    df_calls=pd.DataFrame()
    df_puts=pd.DataFrame()
##    m=['ZM']
##    m=QQQ
##    m=QQQ
##    m=['QQQ','SPY','$NDX.X','DOW','$SPX.X']
##    print('no_of_indices: ',len(m))
##    md=['^IXIC','SPY','TSLA','MRNA']
##    ticker='SPY'
    ##ticker=str(ticker).upper()
    ##m=[$SPX.X,'SPY',$DJI]

##    z=QQQ
##    i=0
##    for z in m:
        
        ##for ticker in m:
    df3=call2(z,datep,td_consumer_key,accountId)
        

##        print(df3)
    f= open(str('/home/az2/Downloads/44pp/')+str(z)+str('_')+str('calls.txt'), 'w+')
    f.write(str(df3))
    f.close()
##        df3.('/home/az2/Downloads/44pp'+str(m)+str('_')+str('calls.csv'))
    ##time.strftime(str(45))
    ##    time.sleep(2)
    df4=put2(z,datep,td_consumer_key,accountId)
    f=open(str('/home/az2/Downloads/44pp/')+str(z)+str('_')+str('puts.txt'), 'w+')
    f.write(str(df4))
    f.close()
##        df3.to_csv('/home/az2/Downloads/44pp'+str(m)+str('_')+str('calls.csv'))
##        puts3 = pd.concat([df3, df_puts], axis=1).reindex(df_puts.index)
##        print(i,'  ',df3,df4)
##        print(type(df3))
##    i=i+1
    print('files saved at ','/home/az2/Downloads/44pp/')
    return(df3,df4)




def part2(QQQ,datep):        
    import json
    import ast
    import requests
    import pandas as pd
    print('starting part 2')
    f=open(str('/home/az2/Downloads/44pp/')+str(QQQ)+str('_calls.txt'))
##    with open(str('/home/az2/Downloads/44pp/')+str(QQQ)+str('_calls.txt')) as f:
##    with open('/home/az2/Downloads/44pp/{QQQ}_calls.txt') as f:
    data = f.read()
##    print(data,' nnn part2')
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
    dfc=pd.DataFrame()
    for idx, rowm in js.items():
##        print(k,'   ',idx,'  ',rowm)
        if k==12 or k==13:
            k2=0
            for p1,p2 in rowm.items():
##                print(k2,'  ',p1,'   ',p2)
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
    print('Total Call Volume    ',dfc['totalVolume'].sum())
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
##                print(k2,'  ',p1,'   ',p2)
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
    print(QQQ,'      expiration',datep,' ====================')
    print('Total put volume: ',dfp['totalVolume'].sum())
    p=dfp['totalVolume'].sum()
    c=dfc['totalVolume'].sum()
    d=p/c
    print('PCR=',round(d,3))
    return(QQQ,d,p-c)
##    print('Total put volume    ',dfp['totalVolume'].sum())
    f.close()

import os


dir = '/home/az2/Downloads/44pp'

for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))

m=['tsla','a','nio']

##datep='2022-05-27'
##i='T'
##get_indices(i,datep)
##part2(i,datep)



gm2=[]
gm3=[]
gm4=[]
for i in m:
    print('\n')
    print(i)   
    datep='2022-05-27'
##    QQQ=str(i)
    df3,df4=get_indices(i.upper(),datep)
    print(df3, ' call')
    print(df4,'  put')
##
    f2,f3,f4=part2(i.upper(),datep)


##    
##    gm2.append(f2)
##    gm3.append(f3)
##    gm4.append(f4)
##
##dff=pd.DataFrame(gm2,gm3,gm4).T
##print(dff)




##    if k==2:
##        
##        for c,d in rowm.items():
##            print(c,'   ',d)
##
##    k=k+1    



    
##for r,c in js.items():
##    print(r,'   ',c)
##print(js)

##    calls3.to_csv('/home/az2/Downloads/calls3.csv')
##    puts3.to_csv('/home/az2/Downloads/puts3.csv')

##df_c=pd.DataFrame('/home/az2/Downloads/calls3.csv')
##df_p=pd.DataFrame('/home/az2/Downloads/puts3.csv')
##print(df_c)
##print(df_p)
############    print('=====================================')
############    print('Ticker : ',z)
############    print('Call volume=',df3['totalVolume'].sum())
############    print('Put volume=', df4['totalVolume'].sum())
############    if df4['totalVolume'].sum()/df3['totalVolume'].sum() < 1:
############        print(ticker,' Put/Call volume=',round(df4['totalVolume'].sum()/df3['totalVolume'].sum(),2),'     ','put to call < 1', 'Upside-[buy_calls]-bullish')
############    elif df4['totalVolume'].sum()/df3['totalVolume'].sum() > 1:
############        print(ticker,' Put/Call volume=',round(df4['totalVolume'].sum()/df3['totalVolume'].sum(),2),'     ','put to call > 1', 'Downside-[buy_puts]-bearish')
############    accountId = '235471191'
############    del df3
############    del df4
############    print('=====================================')
    ##    time.sleep(5)



    ##base_url = 'https://api.tdameritrade.com/v1/accounts/${accountId}?fields=positions'
    ##endpoint = base_url.format(stock_ticker = 'SPY',contractType = 'CALL')
    ##page = requests.get(url=endpoint, params={'apikey' : td_consumer_key})
    ##content = json.loads(page.content)
    ##print(content)
    ############################################################################################################
    ##base_url = 'https://api.tdameritrade.com/v1/accounts/{accountId}'
    ##endpoint = base_url.format(stock_ticker = 'SPY',contractType = 'positions')
    ##page = requests.get(url=endpoint, params={'apikey' : td_consumer_key})
    ##content = json.loads(page.content)
    ##print(content)
    ##############################################################################################################3
    ##base_url = 'https://api.tdameritrade.com/v1/accounts/{accountId}/orders'
    ##endpoint = base_url.format(stock_ticker = 'SPY',contractType = 'CALL')
    ##page = requests.get(url=endpoint, params={'apikey' : td_consumer_key})
    ##content = json.loads(page.content)
    ##print(content)
