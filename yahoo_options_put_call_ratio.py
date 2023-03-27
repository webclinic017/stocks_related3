#https://theautomatic.net/2019/04/17/how-to-get-options-data-with-python/
#http://theautomatic.net/yahoo_fin-documentation/


from yahoo_fin.options import get_options_chain
from yahoo_fin import options
import datetime 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from urllib.request import urlopen
import os
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


os.system('color')



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




def bb(xx,expiration_date):



    
    nflx_dates = options.get_expiration_dates(xx)
    ##options.get_calls("nflx", "04/26/19")
    ##options.get_puts("nflx", "04/26/19")
    print('\n')
    print('####################################################')
    print(xx,'       expiration dates    ')
    print(nflx_dates)
    all_calls_puts=options.get_options_chain(xx,  date=nflx_dates[expiration_date], raw=True)
    puts4=options.get_puts(xx, nflx_dates[expiration_date])
    ##puts4=pd.DataFrame(puts4)

    #############################################################
    calls4=options.get_calls(xx, nflx_dates[expiration_date])
    calls4=pd.DataFrame(calls4)
    print(calls4,puts4,'   ',xx,'  ',nflx_dates[expiration_date])
    calls4['Volume'].replace(0,'-')
    for x in calls4.index:
        if calls4['Volume'].loc[x]=='-':
    ##        print(calls4.loc[x])
            calls4['Volume'].loc[x]='0'
    calls4['Volume'].apply(lambda x: float(x))

    cca=0
    for x in calls4.index:
        cca=int(calls4['Volume'].loc[x])+int(cca)
    ##print('\n\n')    
    ##print(cca,'Calls sum of volume')
    #############################################################
    ##puts4=options.get_puts(x, nflx_dates[0])
    puts4=pd.DataFrame(puts4)
##    print(calls4,puts4,'   ',xx,'  ',nflx_dates[expiration_date])
    puts4['Volume'].replace(0,'-')
    for x in puts4.index:
        if puts4['Volume'].loc[x]=='-':
    ##        print(calls4.loc[x])
            puts4['Volume'].loc[x]='0'
    puts4['Volume'].apply(lambda x: float(x))
    ####
    ppa=0
    for x in puts4.index:
        ppa=int(puts4['Volume'].loc[x])+int(ppa)
    ##print('\n')    
    ##print(ppa,' Puts sum of volume')
    ###############################################################

    print('ticker= ',xx,'    ',nflx_dates[expiration_date])
    print('Call Volume: ',cca, '   Put Volume: ', ppa)
    print('put to call ratio: ',round(ppa/cca,2))
    print('calls_vol ',cca)
    print('puts_vol ',ppa)
    print('puts-calls=',ppa-cca)
    print('####################################################')
##    day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
##    day = datetime.datetime.strptime(nflx_dates[expiration_date], '%d %m %Y').weekday()
    import datetime
##    print(help(datetime.datetime))
####    print(day_name[day])
##    
##    print(nflx_dates[expiration_date].split()[0])


    datetime_object = datetime.datetime.strptime(nflx_dates[expiration_date].split()[0], "%B")
    mm = datetime_object.month
##    print(month_number
##    mm=(nflx_dates[expiration_date].split()[2],nflx_dates[expiration_date].split()[0],nflx_dates[expiration_date].split()[1])
    print(mm,' ================================')
##    print(datetime.date.weekday(nflx_dates[expiration_date]))

    


        
    ##   	^DJI $INDU .DJI DJIA     
    ##print(calls4['Volume'].sum(axis=1),' jjjj')

    ##print(puts4.Volume.sum()-calls4.Volume.sum())

##'^ndx','^gspc','^dji','qqq','spy','tna','arkk','amzn','googl'
##xx='arkk'
##expiration_date=0
##m=['IXIC','spy','tsla']
####m=['^DOW','^RUT','IJR','VIOO','\ES','^SPX','^ndx','arkk','spy','tsla','qqq','^SPX','t','mrna','arkk','spy',]
##for x in m:
##    bb(x,expiration_date)
##    



import yfinance as yf
p='mrna'

msft = yf.Ticker(p)

# get stock info
msft.info
print('\n')
print(p,'  info  ','\n',msft.info)
# get historical market data
hist = msft.history(period="max")

# show actions (dividends, splits)
msft.actions
##opt = msft.option_chain('2022-05-23')
nflx_dates = options.get_expiration_dates(p)
print('\n')
print(p,' options expiration: ','\n',nflx_dates)

print('\n')
print(p,' inst_holders','\n',msft.institutional_holders)
print('\n')
print(p,' options_expirations   ','\n', msft.options)
print('\n')
print(p,'  analyst_recommd',msft.recommendations.tail(13))
