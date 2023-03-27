# Notes for azhar.
# ta_candles6_v3.py is stable.
# ta_candles8_v3.py is the Best version.
import sys  #system specific parameters and names
import gc   #garbage collector interface
import talib as ta
import yfinance as yf
import pandas as pd
import datetime as dt
import sys
import re
import numpy as np
from talib import stream
import matplotlib.pyplot as plt
##from datetime import date
##today = date.today().isoformat()
import datetime
import math
from millify import millify
import time
from time import time

##today = datetime.date.today() + datetime.timedelta(days=1)
today = datetime.date.today()
##print(datetime.today().strftime('%Y-%m-%d'))
import mplfinance
import matplotlib
##from matplotlib.finance import candlestick2_ohlc
##from mpl_finance import candlestick_ohlc
##from mplfinance.original_flavor import candlestick_ohlc
from mplfinance.original_flavor import candlestick_ohlc
from optionprice import Option 
import mplfinance as mpf

##import matplotlib.pyplot as plt
##import matplotlib.ticker as ticker
##import datetime as datetime
##import numpy as np


pd.options.display.float_format = '{:.2f}'.format
pd.options.display.max_columns=255
pd.options.display.max_rows=6500000

pd.options.display.max_rows=9999
pd.options.display.max_columns=36
pd.set_option("display.max_columns", 100)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 200)
pd.set_option('display.max_columns', 0)


############################################################    
def xz(periodb,intervalb,p):
    import time
    from time import time
    import re


    
    pd.options.display.float_format = '{:.2f}'.format
    pd.options.display.max_columns=255
    pd.options.display.max_rows=6500000

    pd.options.display.max_rows=9999
    pd.options.display.max_columns=36
    pd.set_option("display.max_columns", 100)
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_colwidth', 200)
    pd.set_option('display.max_columns', 0)

    g=p
    ticker=g
##    no_of_days=365

    df = pd.DataFrame()
    start2=time()
    df=yf.Ticker(g).history(period = periodb, interval = intervalb,prepost = True)
##    df=yf.Ticker(g).history(period = periodb, interval = intervalb)
    df=df[1:]
##    df = yf.download(ticker, period, interval,prepost = True)
##    s  = mpf.make_mpf_style(base_mpf_style='yahoo',mavcolors=['#ef5714','#e7d111','#9f4878','#ef5714','#ef5714','#ff00dd','#1900ff'])
    s  = mpf.make_mpf_style(base_mpf_style='yahoo',mavcolors=['#14ef2e','#e7d111','#9f4878','#ef5714','#ef5714','#489f93','#0a0a0a'])
    end2=time()
##    print('read df 66', end2-start2)
##    print(df,' hhh')

    
    df33=yf.Ticker(g).history(period = '3d', interval = '1d')
    cto=df33['Close'][-1]
    c1day=df33['Close'][-2]
##    c10day=df33['Close'][-10]
##    c30day=df33['Close'][-30]

    v = df['Volume'].values
    tp = (df['Low'] + df['Close'] + df['High']).div(3).values
##    print('tttttttttttttttttttttttttttt --------------------------------------------------->', v.cumsum())
    df = df.assign(vwap=(tp * v).cumsum() / (v.cumsum()+0))
    adp = mpf.make_addplot(df['vwap'], type='line') # ------------------------------------------------------------------------------------->

############################################################   
    
    if  intervalb[-1] == 'm':   # ------------------------------------------------------------------------------------->
        mt3=[]
        m21=[]
        
##        print(df,' ticker',df.index)
        for x5 in df.index:
            v77=re.findall('09:30:',str(x5))
##            print('kkkkkkkkkkkkk ',x5)
            if re.findall('09:30:',str(x5)) is None:
                print('not found')
            elif re.findall('09:30:',str(x5)):

                mt3.append(str(x5).split('00')[0][0:16])
##                print(x5)

        for x5 in df.index:
            v78=re.findall('15:59:',str(x5))
            if re.findall('15:59:',str(x5)) is None:
                print('not found')
            elif re.findall('15:59:',str(x5)):

                m21.append(str(x5)[0:16])
##                print(x5)
                

        print(mt3)
        print(m21)
##        sys.exit()
##            
##            if v77 :
##                print('09:30 not in df')
##                break
##
##            else:    
##                m21.append(x5)
##                mt3.append(df['Open'].loc[x5])
####                print(mt3,' ',x5,'  bbbbbbbbb *******ttt*********************************************************************')
##    ##        if re.search('09:30:',str(x5)):
##    ##            m21=x5
##    ##            print(m21)        
##
##        print(mt3,'000000000000000000000000000000000000000000000000')
##        for x5a in df.index:        
##            if re.search('15:55:',str(x5a)):
##                m22=x5a
##                print(m22)
##
##
##        print(type(mt3))
##        nn55=-1*(100-((float(np.float(mt3))/float(np.float(c1day)))*100))
##        nn54=-1*(100-((cto/c1day)*100))
##        n56=100-((cto/c1day)*100)
####        +' Today_close/yes_close'+str(n56.round(2))+'%'+'/'+str(cto-c1day),
##          
##    ##    print(m21,'ddddddddddddddddddd ',m22)        
##    ##    for x in df.index:        
##    ##        if re.search('13:30:',str(x)):
##    ##            m22=x    
##    ##            
##    ##    print('********************** ',m21,'***************************** ',m22)
##    ##
##                
##
##    ##    start3=time()
##        mpf.plot(df, block=False,type='candle', addplot=adp,volume=True, figratio=(15, 15), mav=(200,100,50,20,10,5,3),
##             title=ticker.upper()
####                 '  '+str(cto.round(2))+'/'+str(c1day.round(2))+'/['+str((cto-c1day).round(2))+'/'+str(nn54.round(2))+'%] --> '
####                   +' Price_change '+str('%.2f' % float(df['Close'][-1]-df['Close'][-2]))+'  '
####                        +periodb+' '+intervalb   +'    Open:'+str(round(mt3,2))+'/'+str(round(c1day,2))+'['+str((mt3-c1day).round(2))+
####                 '/'+str(round(nn55,2))+'%/]'
##                 ,              
##
##        
##               
##        ##     str(p).split()[1]+' / (diff) '+str(p2).split()[1] + ', Open: '+ str(p5).split()[1] + ' ,low: '+str(p3).split()[1]+ ' ,High: '+ str(p4).split()[1]
##        ##     + ', day swing: ' + str(u3).split('.')[0],
##                 style=s,
##             show_nontrading=False,hlines=dict(hlines=[cto,c1day],colors=['g','r'],linestyle='-.')
####                 ,vlines=dict(vlines=[m21,m22],colors=['g','r'],linestyle='-.')
##                 )
##
############################## original #########################33


 
        mpf.plot(df, block=False,type='candle', addplot=adp,volume=True, figratio=(15, 15), mav=(200,100,50,20,10,5,3),
             title=ticker.upper() +'  '+str(cto.round(2))+'/'+str(c1day.round(2))+'/['+str((cto-c1day).round(2))+'] --> ' +periodb+' '+intervalb
                 +' Price_change '+str('%.2f' % float(df['Close'][-1]-df['Close'][-2])),
        ##     str(p).split()[1]+' / (diff) '+str(p2).split()[1] + ', Open: '+ str(p5).split()[1] + ' ,low: '+str(p3).split()[1]+ ' ,High: '+ str(p4).split()[1]
        ##     + ', day swing: ' + str(u3).split('.')[0],
                 style=s,
             show_nontrading=False,hlines=dict(hlines=[cto,c1day],colors=['g','r'],linestyle='-.')
             ,vlines=dict(vlines=[mt3[0],mt3[1],m21[0],m21[1],m21[2]],colors=['g','g','r','r','r'],linestyle='-.')  
                ) 
####################################################################

        
        
##
##    ############################################################
##    if  intervalb[-1] == 'd':   # ------------------------------------------------------------------------------------->      
##
##    ##    start3=time()
##        mpf.plot(df, block=False,type='candle', addplot=adp,volume=True, figratio=(15, 15), mav=(200,100,50,20,10,5,3),
##             title=ticker.upper()
##                 +'  '+str(cto.round(2))+'/'+str(c1day.round(2))+'/['+str((cto-c1day).round(2))+'] --> ' +periodb+' '+intervalb
##                 +' Price_change '+str('%.2f' % float(df['Close'][-1]-df['Close'][-2])),
##        ##     str(p).split()[1]+' / (diff) '+str(p2).split()[1] + ', Open: '+ str(p5).split()[1] + ' ,low: '+str(p3).split()[1]+ ' ,High: '+ str(p4).split()[1]
##        ##     + ', day swing: ' + str(u3).split('.')[0],
##                 style=s,
##             show_nontrading=False,hlines=dict(hlines=[cto,c1day],colors=['g','r'],linestyle='-.')
##                 )
##
##
##    ##    end3=time()
##
##
##
##        
##gg=['arkf','^ndx','^gspc','^dji','spy','tna','arkk']
##
####for x in gg:
######    daily('20d','1d',x)
######    daily('5h','5m',x)                                            # best one
####    hourly('1d','5m',x)
####    hourly('2h','1m',x)
##    ############################################################  
##    
####stocks('30d','1d')
##p7=['vg','astr','ispc','mpln','nbev','avya','cei','nvts']
##p2=['now','snow','amc','aapl','f','asml','zm']  #miscl
##p3=['tsla','nio','plug','lcid','rivn','fsr','blnk']  #ev
##p4=['mrna','bntx','nvax','bntx','isrg','biib','pfe','abt']   #covid
##p5=['adbe','gme','nvda','nflx','asml','mu','avgo','amd','asml','qcom','mrvl','txn','intc']
##p6=['dltr','penn','coin','mstr','uber','lyft','z']
##p8=['^ndx','RSX','AUPH']
##u2=['BHP', 'DUST', 'EWY', 'NYCB', 'QID', 'SQQQ', 'SVRA', 'AEP']
##u3=['bby','zm','dks','anf','dltr','xpev']
gg=['arkf','^ndx','^gspc','^dji','spy','tna','arkk','qqq','tsla','vix']
for x in gg:
##    
####    xz('20d','1d',x)  # works
##############    xz('3d','60m',x)
######    xz('2d','30m',x)
####    xz('7h','5m',x)   # works
    xz('920m','1m',x)
##
##
































##
##
##
##   
############################################################# clear the cache #######################3
##import sys  #system specific parameters and names
##import gc   #garbage collector interface
##
##memory_usage_by_variable=pd.DataFrame({k:sys.getsizeof(v) for (k,v) in locals().items()},index=['Size'])
##memory_usage_by_variable=memory_usage_by_variable.T
##memory_usage_by_variable=memory_usage_by_variable.sort_values(by='Size',ascending=False).head(10)
##print(memory_usage_by_variable.head())
##
##def obj_size_fmt(num):
##    if num<10**3:
##        return "{:.2f}{}".format(num,"B")
##    elif ((num>=10**3)&(num<10**6)):
##        return "{:.2f}{}".format(num/(1.024*10**3),"KB")
##    elif ((num>=10**6)&(num<10**9)):
##        return "{:.2f}{}".format(num/(1.024*10**6),"MB")
##    else:
##        return "{:.2f}{}".format(num/(1.024*10**9),"GB")
##
##
##def memory_usage():
##    memory_usage_by_variable=pd.DataFrame({k:sys.getsizeof(v)\
##    for (k,v) in globals().items()},index=['Size'])
##    memory_usage_by_variable=memory_usage_by_variable.T
##    memory_usage_by_variable=memory_usage_by_variable\
##   .sort_values(by='Size',ascending=False).head(10)
##    memory_usage_by_variable['Size']=memory_usage_by_variable['Size'].apply(lambda x: obj_size_fmt(x))
##    return memory_usage_by_variable
##
##memory_usage()
##print(memory_usage_by_variable)
##
##print('\n''kaku khan','\n\n')
##
##print('2) gc.get_count()',gc.get_count())
##
##print('3) memory_usage-->: ',memory_usage())
##print('\n\n')
##print('4) gc.collect',gc.collect())
##print('5) gc.get_count() ',gc.get_count())
##print('memory_usage():',memory_usage())
##print('tota hoai baba')
##
##print('--------------------------------------------------','\n\n')
##print('\n')
####print('plotting loop', end4-start4)
####print('mpf plotting time',end3-start3)
####print('read from api/read from y.finance',end2-start2)
##
##
##print('--------------------------------------------------','\n\n')
##del p5
##del gg
##del xz
##del p4
##del p7
##
###triggering collection
##print('After deleting df,df33,gg ,gc.collect()---',gc.collect())
##
###finally check memory usage
##print('\n')
##print('After deleting df,df33,gg,memory.usage()',memory_usage())
##['binance',
## 'blueskies',
## ,
## 'charles',
## 'checkers',
## 'classic',
## 'default',
## 'mike',
## 'nightclouds',
## 'sas',
## 'starsandstripes',
## 'yahoo']



######################################################
##import pandas as pd
##import mplfinance as mpf
##import datetime as dt
##import yfinance as yf
##
##
### Load data file.
##g='t'
##ticker=g
##no_of_days=365
##
##df = pd.DataFrame()
##
##
##start = dt.datetime.today() - dt.timedelta(no_of_days)
##end = dt.datetime.today()
##df = yf.download(ticker, start, end,prepost = True)
##
### Plot candlestick.
### Add volume.
### Add moving averages: 3,6,9.
### Save graph to *.png.
##mpf.plot(df, type='candle', style='charles',
##        title='',
##        ylabel='',
##        ylabel_lower='',
##        volume=True, 
##        mav=(200,100,50,20,10,3,5))
##
##
####################################
##import matplotlib.pyplot as plt
##from mpl_finance import candlestick_ohlc
##import pandas as pd
##import matplotlib.dates as mpl_dates
##import yfinance as yf
##import mplfinance as mpf
##
##plt.style.use('ggplot')
##
### Extracting Data for plotting
##df = yf.download('tsla', '2021-01-1','2021-06-28', index=False)
### Plot candlestick.
### Add volume.
### Add moving averages: 3,6,9.
### Save graph to *.png.
##mpf.plot(df, type='candle', style='charles',
##        title='',
##        ylabel='',
##        ylabel_lower='',
##        volume=True, 
##        mav=(3,6,9), 
##        savefig='test-mplfiance.png')




