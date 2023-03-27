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

import datetime
import math
from millify import millify
import time
from time import time
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
    from mplfinance._utils import _construct_vline_collections
    import matplotlib.pyplot as plt
    g=p
    ticker=g
##    no_of_days=365


          #,'ppppp  periodb[-1]     ',periodb[-1])

    df = pd.DataFrame()
    start2=time()
    df=yf.Ticker(g).history(period = periodb, interval = intervalb,prepost = True)
##    df=yf.Ticker(g).history(period = periodb, interval = intervalb)
    df=df[['Open', 'High', 'Low', 'Close', 'Volume']]
    df=df[1:]
    ccvv=len(periodb)-1
    print('=============     ppppp  periodb[-2]    periodb ',periodb,'  cccvv= ',periodb[0:len(periodb)-1],'  <=== ')


##    sys.exit()
##    df = yf.download(ticker, period, interval,prepost = True)
##    s  = mpf.make_mpf_style(base_mpf_style='yahoo',mavcolors=['#ef5714','#e7d111','#9f4878','#ef5714','#ef5714','#ff00dd','#1900ff'])
    plt.style.use('ggplot')
    s  = mpf.make_mpf_style(base_mpf_style='yahoo',mavcolors=['#14ef2e','#e7d111','#9f4878','#ef5714','#56ef14','#ada5a8','#0a0a0a']
                            , rc={'font.size':7})
    end2=time()
    print('read df 66', end2-start2)

    df['delta_price']=''
    for x in df.index:
        df['delta_price'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc[x]
    
    print(df['Close'].tail(5),'\n',ticker,'    hhh  ')

    
    df33=yf.Ticker(g).history(period = '15d', interval = '1d')

    df33['swngb']=''
    for x in df33.index:
        df33['swngb'].loc[x]=df33['High'].loc[x]-df33['Low'].loc[x]

    
##    print(g,'    ',df33.shape)
    cto=df33['Close'][-1]
    c1day=df33['Close'][-3]
##    vv=df33['Close'].shift(1)[-1]
##
##
##
##    print(df33,'\n',cto,'\n',c1day,'\n',vv)
##    sys.exit()
##    c10day=df33['Close'][-10]
##    c30day=df33['Close'][-30]

    v = df['Volume'].values
    tp = (df['Low'] + df['Close'] + df['High']).div(3).values
##    print('tttttttttttttttttttttttttttt --------------------------------------------------->', v.cumsum())
    df = df.assign(vwap=(tp * v).cumsum() / (v.cumsum()+0))
    adp = mpf.make_addplot(df['vwap'], type='line') # ------------------------------------------------------------------------------------->

############################################################   
############################################################   
    
    if  intervalb[-1] == 'm':   # ------------------------------------------------------------------------------------->
        mt3=[]
        mt3c=[]
        
        for x5 in df.index:
            v77=re.findall('09:30:',str(x5))
##            print('v77 ---------------- ',v77,'   ',len(v77))
            if len(v77) > 0 :
                print('mt3 ',str(x5)[0:16])
                mt3.append(str(x5))
                mt3c.append(str('g'))
                

            else:
##                print('09:30 not in df')
                pass
##                
##                m21=x5
##                mt3=df['Open'].loc[x5]
##        print(mt3,'000000000000000000000000000000000000000000000000')
##        sys.exit()
        mt4=[]
        mt4c=[]
        for x5a in df.index:
            v78=re.findall('16:00:',str(x5a))
            if len(re.findall('16:00:',str(x5a))) > 0 :
                print('mt4 tttttttttttttttttttttttttttttttttttttttttttt ',x5a)
                mt4.append(str(x5a))
                mt4c.append(str('r'))
                

            else:
##                print('09:30 not in df')
                pass
###############################################

###########################################

##            print(x)

##        nn55=-1*(100-((float(np.float(mt3))/float(np.float(c1day)))*100))
##        nn54=-1*(100-((cto/c1day)*100))
##        n56=100-((cto/c1day)*100)

        m55=4
        nn54=7
        n56=78
##        print('jjjjjj','\n')
##        def z():
##            for x in mt3:
##                print(x)
##
##
##        def z2():
##            for x in mt4:
##                print(x)                
##        print(z())

##        sys.exit()

        print(mt4)
        print('\n')
        print(mt3)
        mt=[]
        mt=mt3+mt4
        mc=[]
        mc=mt3c+mt4c
        print('mt-> ',mt,'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
        print('mc-> ',mc,'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
        
        zz=['2021-11-23 16:00:00-05:00', '2021-11-24 16:00:00-05:00','2021-11-24 09:30:00-05:00', '2021-11-26 09:30:00-05:00']


        print(df33,'\n','khan ',ticker,'\n')
        print(df33.tail(3),'\n','khan ',ticker,'\n')
        print(df33['Close'].tail(3).min(),'\n','khan ',ticker,'\n')
        
        mpf.plot(df, block=False,type='candle', addplot=adp,volume=True, figratio=(15, 15),
                 mav=(200,100,50,20,10,5,3),title='\n\n\n\n\n\n'+ticker.upper()+'  '+periodb+' '+intervalb+'\n'
                 +'Today_close  '+str(cto.round(2))+'/ Yest_Close  '+str(c1day.round(2))
                 +'/[ Delta  '+str((cto-c1day).round(2))+' / '+str(nn54)+'%] --> '+'\n'+
                 
                 'Todays Open: '+str(round(df33['Open'][-1],2))+'/Yest Close '+str(round(df33['Close'][-2],2))+'/'
                 +' [Delta= '+ str(round((df33['Open'][-1]-df33['Close'][-2]),2))+']'+'\n'+
                 
                 'Todays Open :'+ str(round(df33['Open'][-1],2))+' Close: '+ str(round(df33['Close'][-1],2))
                 +' Low: '+str(round(df33['Low'][-1],2))+ ' High: '+str(round(df33['High'][-1],2))+ 'swng '+
                 str(df33['swngb'][-1])+'\n'+

                 
                ' 3day low '+ str(round(df33['Low'].tail(3).min(),2))+ '3 day high '+ str(round(df33['High'].tail(3).max(),2))+' 3day Swng '
                 +'['+str(round(df33['swngb'].tail(3).min(),2))+' - '+str(round(df33['swngb'].tail(3).max(),2))+']'
                 +'Current Price dis '
                 +str(round((df33['Open'][-1]-df33['Low'].tail(3).min()),2))+'/'+str(round((df33['Open'][-1]-df33['High'].tail(3).min()),2))+
                 '\n'+
        
  
                ' 5day low '+ str(round(df33['Low'].tail(5).min(),2))+ '5 day high '+ str(round(df33['High'].tail(5).max(),2))+' 5day Swng '
                 +'['+str(round(df33['swngb'].tail(5).min(),2))+' - '+str(round(df33['swngb'].tail(5).max(),2))+']'
                 +'Current Price dis '
                 +str(round((df33['Open'][-1]-df33['Low'].tail(5).min()),2))+'/'+str(round((df33['Open'][-1]-df33['High'].tail(5).min()),2))+
                 '\n'+
        
                 

                ' 10day low '+ str(round(df33['Low'].tail(10).min(),2))+ '5 day high '+ str(round(df33['High'].tail(10).max(),2))+' 10day Swng '
                 +'['+str(round(df33['swngb'].tail(10).min(),2))+' - '+str(round(df33['swngb'].tail(10).max(),2))+']'
                 +'Current Price dis '
                 +str(round((df33['Open'][-1]-df33['Low'].tail(10).min()),2))+'/'+str(round((df33['Open'][-1]-df33['High'].tail(10).min()),2))+
                 '\n',
        
                 

 
##                 +str(df33['Close'][-2]),
##                 +str(int(mt3)-int(c1day))+'/'+str(nn55),
                 style=s,show_nontrading=False,
                 hlines=dict(hlines=[cto,c1day],colors=['g','r'],linestyle='-.'),vlines=dict(vlines=mt,colors=mc,linestyle='dotted'))
                 
                 
##                 +' Price_change '+str('%.2f' % float(df['Close'][-1]-df['Close'][-2]))

                 
                 
        
##                    'MA200=Green'+' MA100=Yellow'+' MA50=Pink'+
##                    ' MA20=Orange'+' MA10=Greenish'+' MA5=grey'+
##                    ' MA3=Black',                                       



########################################################################3
    if  periodb[-1] == 'd':
        
        yestd=df['Close'][-1]
        pyest=df['Close'].shift(1)[-1]


        yestd_5=df['Close'][-1]
        pyest_5=df['Close'].shift(5)[-1]

        yestd_10=df['Close'][-1]
        pyest_10=df['Close'].shift(10)[-1]

        yestd_30=df['Close'][-1]
        pyest_30=df['Close'].shift(30)[-1]

        yestd_90=df['Close'][-1]
        pyest_90=df['Close'].shift(90)[-1]

        c33=int(periodb[0:len(periodb)-1])-1

        
        yestd_c33=df['Close'][-1]
        pyest_c33=df['Close'][-1*c33]
       
        

        
                 # ------------------------------------------------------------------------------------->      

        if  float(periodb[0:len(periodb)-1]) < float(90.0) :
##            print('ppppp       ',intervalb[-2])
    ##    start3=time()
            mpf.plot(df, block=False,type='candle', addplot=adp,volume=True,
                              title='\n\n\n\n\n\n'+ticker+' vvv '+ str(periodb)+'  '+str(intervalb) + '\n'+'   1day Price change---> '+str(round(yestd,2))+'/'+str(round(pyest,2))+'/ ['+
##                     str(round(yestd-pyest,2))+'] /'+str(round(-1*100-yestd/pyest*100,2))+'%'+'\n'+
                     str(round(yestd-pyest,2))+'] /'+str(round(yestd/pyest*100-100,2))+'%'+'\n'+
                     
                     '   5day Price change---> '+str(round(yestd_5,2))+'/'+str(round(pyest_5,2))+'/ ['+
                     str(round(yestd_5-pyest_5,2))+'] /'+str(round(yestd_5/pyest_5*100-100,2))+'%'+'\n'+


                     ' 10day Price change---> '+str(round(yestd_10,2))+'/'+str(round(pyest_10,2))+'/ ['+
                     str(round(yestd_10-pyest_10,2))+'] /'+str(round(yestd_10/pyest_10*100-100,2))+'%'+'\n'+

                     ' 30day Price change---> '+str(round(yestd_30,2))+'/'+str(round(pyest_30,2))+'/ ['+
                     str(round(yestd_30-pyest_30,2))+'] /'+str(round(yestd_30/pyest_30*100-100,2))+'%'+'\n'+

                     'day Price change---> '+str(round(yestd_c33,2))+'/'+str(round(pyest_c33,2))+'/ ['+
                     str(round(yestd_c33-pyest_c33,2))+'] /'+str(round(yestd_c33/pyest_c33*100-100,2))+'%'+'\n',     
                     
                              figratio=(15, 15),xrotation=30, mav=(200,100,50,20,10,5,3),style=s,returnfig=False)

        elif float(periodb[0:len(periodb)-1]) > float(90.0) : 

            mpf.plot(df, block=False,type='candle', addplot=adp,volume=True,
                      title='\n\n\n\n\n\n'+ticker+'  '+ str(periodb)+'  '+str(intervalb) + '\n'+'   1day Price change---> '+str(round(yestd,2))+'/'+str(round(pyest,2))+'/ ['+
             str(round(yestd-pyest,2))+'] /'+str(round(yestd/pyest*100-100,2))+'%'+'\n'+
             
             '   5day Price change---> '+str(round(yestd_5,2))+'/'+str(round(pyest_5,2))+'/ ['+
             str(round(yestd_5-pyest_5,2))+'] /'+str(round(yestd_5/pyest_5*100-100,2))+'%'+'\n'+


             ' 10day Price change---> '+str(round(yestd_10,2))+'/'+str(round(pyest_10,2))+'/ ['+
             str(round(yestd_10-pyest_10,2))+'] /'+str(round(yestd_10/pyest_10*100-100,2))+'%'+'\n'+

             ' 30day Price change---> '+str(round(yestd_30,2))+'/'+str(round(pyest_30,2))+'/ ['+
             str(round(yestd_30-pyest_30,2))+'] /'+str(round(yestd_30/pyest_30*100-100,2))+'%'+'\n'+

            ' 90day Price change---> '+str(round(yestd_90,2))+'/'+str(round(pyest_90,2))+'/ ['+
             str(round(yestd_30-pyest_90,2))+'] /'+str(round(yestd_90/pyest_90*100-100,2))+'%'+'\n'+

             'day Price change---> '+str(round(yestd_c33,2))+'/'+str(round(pyest_c33,2))+'/ ['+
             str(round(yestd_c33-pyest_c33,2))+'] /'+str(round(yestd_c33/pyest_c33*100-100,2))+'%'+'\n',           
             
##                      figratio=(15, 15),xrotation=30, mav=(200,100,50,20,10,5,3),style=s,returnfig=False)
                        
             
                      figratio=(15, 15),xrotation=30, mav=(200,100,50,20,10,5,3),style=s,returnfig=False)
                 
        
    ########################################################################3           



##stocks('30d','1d')
##p7=['vg','astr','ispc','mpln','nbev','avya','cei','nvts']
##p2=['now','snow','amc','aapl','f','asml','zm']  #miscl
##p3=['tsla','nio','plug','lcid','rivn','fsr','blnk']  #ev
##p4=['mrna','bntx','nvax','bntx','isrg','biib','pfe','abt']   #covid
##p5=['adbe','gme','nvda','nflx','asml','mu','avgo','amd','asml','qcom','mrvl','txn','intc']
##p6=['dltr','penn','coin','mstr','uber','lyft','z']
##p8=['^ndx','RSX','AUPH']
##u2=['BHP', 'DUST', 'EWY', 'NYCB', 'QID', 'SQQQ', 'SVRA', 'AEP']
##u3=['bby','zm','dks','anf','dltr','xpev'],
gg=['arkk','^ndx','^gspc','^dji','spy','tna','qqq','tsla','^dji']
butter=['pfe','f','intc','spy']
s=['dks']
##s=['arkk']

    
for x in gg:
    
##    while True:

##    xz('32d','1d',x)  # works
##    xz('200d','1d',x)  # works
############    xz('3d','60m',x)   
####    xz('2d','30m',x)
##    xz('7h','5m',x)   # works
    xz('320m','1m',x)
    
sleep(62)



















  
########################################################### clear the cache #######################3
import sys  #system specific parameters and names
import gc   #garbage collector interface

memory_usage_by_variable=pd.DataFrame({k:sys.getsizeof(v) for (k,v) in locals().items()},index=['Size'])
memory_usage_by_variable=memory_usage_by_variable.T
memory_usage_by_variable=memory_usage_by_variable.sort_values(by='Size',ascending=False).head(10)
##print(memory_usage_by_variable.head())

def obj_size_fmt(num):
    if num<10**3:
        return "{:.2f}{}".format(num,"B")
    elif ((num>=10**3)&(num<10**6)):
        return "{:.2f}{}".format(num/(1.024*10**3),"KB")
    elif ((num>=10**6)&(num<10**9)):
        return "{:.2f}{}".format(num/(1.024*10**6),"MB")
    else:
        return "{:.2f}{}".format(num/(1.024*10**9),"GB")


def memory_usage():
    memory_usage_by_variable=pd.DataFrame({k:sys.getsizeof(v)\
    for (k,v) in globals().items()},index=['Size'])
    memory_usage_by_variable=memory_usage_by_variable.T
    memory_usage_by_variable=memory_usage_by_variable\
   .sort_values(by='Size',ascending=False).head(10)
    memory_usage_by_variable['Size']=memory_usage_by_variable['Size'].apply(lambda x: obj_size_fmt(x))
    return memory_usage_by_variable

memory_usage()
##print(memory_usage_by_variable)

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
##print('plotting loop', end4-start4)
##print('mpf plotting time',end3-start3)
##print('read from api/read from y.finance',end2-start2)


##print('--------------------------------------------------','\n\n')

del gg
del xz


#triggering collection
##print('After deleting df,df33,gg ,gc.collect()---',gc.collect())

#finally check memory usage
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





