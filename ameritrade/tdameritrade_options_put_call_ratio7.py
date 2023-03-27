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




def call2(ticker,datep,td_consumer_key,accountId):
    import requests
    import json
    import pandas as pd
##    print('--  ',ticker)
##    print('inside call2========================================================================================================================')    
    stock_ticker = ticker
    contractType = 'CALL'
    date=datep
##    print(date)
##    print(stock_ticker)
    base_url = 'https://api.tdameritrade.com/v1/marketdata/chains?&symbol={stock_ticker}&contractType={contractType}&fromDate={date}&toDate={date}'
    endpoint = base_url.format(stock_ticker = ticker,contractType = 'CALL',date=datep)
    page = requests.get(url=endpoint,params={'apikey' : td_consumer_key})
    content = json.loads(page.content)
##    print(content,'   calls ',ticker,'   expiration: ',datep)
##    print(type(content),'   ',ticker)
    return(content)

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
    
##    print(content, '   puts',ticker,'   expiration: ',datep)
##    print('\n\n')
    return(content)


import time
td_consumer_key=str('CLIFWQTIZ6EBH0BD3BVY4TASYUXMINAN')
accountId = '235471191'


def get_indices(z,datep):
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

    df3=call2(z,datep,td_consumer_key,accountId)
        

##        print(df3)
    f= open(str('/home/az2/Downloads/44pp/')+str(z)+str('_')+str('calls.txt'), 'w+')
    f.write(str(df3))
    f.close()



    
##    df3.to_csv('/home/az2/Downloads/44pp'+str(m)+str('_')+str('calls.csv'))
    ##time.strftime(str(45))
    ##    time.sleep(2)
    df4=put2(z,datep,td_consumer_key,accountId)
    f=open(str('/home/az2/Downloads/44pp/')+str(z)+str('_')+str('puts.txt'), 'w+')
    f.write(str(df4))
    f.close()

##    print('files saved at ','/home/az2/Downloads/44pp/')
    return(df3,df4)




def part2(QQQ,datep):        
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
##    print(QQQ,'      expiration',datep,' ====================')
##    print('Total put volume: ',dfp['totalVolume'].sum())
    p=dfp['totalVolume'].sum()
    c=dfc['totalVolume'].sum()
    d=p/c
##    print('PCR=',round(d,3))
    return(QQQ,d,p-c,p,c)
##    print('Total put volume    ',dfp['totalVolume'].sum())
    f.close()

import os


##m=['TSLA','NVDA','TOLL','SNOW','SPLK','DKS','SHIP','NIO','ADSK','DELL','COST','MRVL','WDAY','ZS']

m=['spy','toll','tsla','wmt','nvda','splk','dks','nio','adsk','cost','mrvl','wday','zs']

datep='2022-05-27'
##i='T'
##for i in m:
##    get_indices(str(i).upper(),'2022-05-27')
##    part2(i,datep)


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
    datep='2022-05-27'
##    QQQ=str(i)
    df3,df4=get_indices(str(i).lower().upper(),datep)
##    print(df3, ' call')
##    print(df4,'  put')
    f2,f3,f4,f5,f6=part2(str(i).upper(),datep)


##    
    gm2.append(f2)
    gm3.append(f3)
    gm4.append(f4)
    gm5.append(f5)
    gm6.append(f6)

print('\n\n')
dff=pd.DataFrame({'ticker':gm2,'pcr':gm3,'delta_vol':gm4,'put_vol': gm5, 'call_vol':gm6})
print(dff)

    

