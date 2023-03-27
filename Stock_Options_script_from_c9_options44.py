from yahoo_fin import options 
import pandas as pd
import yfinance as yf
from yahoo_fin import stock_info as f


import textwrap 
#pd.set_option("max_colwidth", 12)
from yahoo_fin import news as g
import html5lib
import numpy as np 
from numerize import numerize 
import sys
import datetime
import re

from datetime import date
from termcolor import colored

print(colored('hello', 'red'), colored('world', 'green'))

import os

# System call
os.system("")

# Class of different styles
class style():
        BLACK = '\033[30m'
        RED = '\033[31m'
        GREEN = '\033[32m'
        BLUE = '\033[34m'
        YELLOW = '\033[33m'
        MAGENTA = '\033[35m'
        CYAN = '\033[36m'
        WHITE = '\033[37m'
        UNDERLINE = '\033[4m'
        RESET = '\033[0m'

#print(style.YELLOW + "Hello, World!")

##from sty import fg, bg, ef, rs
##foo = fg.red + 'This is red text!' + fg.rs
##bar = bg.blue + 'This has a blue background!' + bg.rs
##baz = ef.italic + 'This is italic text' + rs.italic
##qux = fg(201) + 'This is pink text using 8bit colors' + fg.rs
##qui = fg(255, 10, 10) + 'This is red text using 24bit colors.' + fg.rs
##
### Add custom colors:
##
##from sty import Style, RgbFg
##
##fg.orange = Style(RgbFg(255, 150, 50))
##
##buf = fg.orange + 'Yay, Im orange.' + fg.rs
# https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal



##print(foo, bar, baz, qux, qui, sep='\n')



today = date.today()
print(today)



money=input("Enter Amount of funds/$ like to purchase:")

ticker='T'
#ticker='spx'



pd.options.display.max_columns = 50
pd.options.display.max_rows = 1000
 #pd.options.display.max_colwidth =180
pd.set_option('display.max_colwidth', 16)
pd.set_option("display.expand_frame_repr", False)


cc='October 15, 2021'
print("[stock price > VWAP --- Sell],   [stock price < VWAP --- Buy] ......If the stock price is above VWAP, it is a good intraday price to sell. If the price is below VWAP, it is a good intraday price to buy")
print("[stock price > Pivot --- Buy] bull, [stock price < Pivot --- Sell] bearish")
print("The closing price on a stock can tell you much about the near future. If a stock closes near the top of its range,\
        this indicates that momentum could be upward for the next day")
print("Compare each day’s opening bid to the previous day’s stock price. If pre-market bids run higher than the closing price, the stock may have more upside potential. \
        If bids run lower than the previous day’s closing price, investors may be ready to dump the stock.")
print("If a stock price goes up on very low volume, only a small number of investors drove the price up and the rise won’t last. \
        A stock that goes down on increased volume may have much more downside risk because people are getting out of it. A stock that goes \
        down on light volume presents less of a risk that it will go down further.")
print("The range in prices for a stock reflects volatility. If you see a stock taking wild swings in one day, this indicates that some kind of news has come out about the company issuing the stock. Compare the range of prices \
                on any given day to other days. If you see a sudden large swing in prices, this may indicate ensuing volatility for that stock.")
print("^GSPC ticker for spx")
print('\n\n')

ticker=input("Enter ticker: ")
# if ticker=None:
#     ticker='^ndx'   # khan



###########################################################################################################
nflx_dates = options.get_expiration_dates(ticker)


print(nflx_dates)
cc=input("Enter expirtion Date: ")  


what_option=input("What option_call (1) _or_put (2) : ") #khan


# what_option=1   # khan
if what_option=='1':
    what_option='calls'
if what_option=='2':
    what_option='puts'


chain = options.get_options_chain(ticker,cc)
###################################################
#print(nflx_dates)
#print(chain)


#ticker=input("Enter ticker: ")
#cc=input("Enter expirtion Date: ")
#cc='October 15, 2021'

###################################################################################################################
data =yf.download(ticker, period='1d', interval='1m',prepost = True)

df4=pd.DataFrame(data)

df4.reset_index(drop=False,inplace=True)
print('\n\n\n')
print(df4.tail(3))
ss=df4['Close'].tail(1)
ss=ss.to_string(header=None, index=None)
print('***************   Stock price right now ---------> ',ss, ' ****************************************')
#print(df4['Close'].tail(1))
print('\n\n\n')
print("hello *****************************************************************************************************************************",'\n')
i=0
while(i<12):
    print('sleep azhar ***********************************','\n')
    i=i+1
############################################################################# daily price ###############################################
# data3a =yf.download(ticker, period='356d', interval='1d',prepost = True)
# df5=pd.DataFrame(data3a)

# df5.reset_index(drop=False,inplace=True)
# High52d=df5['High'].rolling(365).max()
# High52d_33=df5['High'].max()

# vv3day_low=df5['Low'].rolling(3).min()
# vv3day_high=df5['High'].rolling(3).max()


# print('\n\n\n',"HHHHHHHHHHHHHHHHHHHHH",'\n\n\n')
# print('bbbbbbbbbbbb  3day_low=',vv3day_low,'        3day_high= ',vv3day_high)
# print("End of sleep",' ***********************************')
# print('\n\n\n')
#print(df5.tail(3))
#ss=df5['Close'].tail(1)
#ss=ss.to_string(header=None, index=None)
###########################################################################################################################################
################### 1 day ##########################
data2 =yf.download(ticker, period='400d', interval='1d')
#data2 =yf.download(ticker, period='6d', interval='1d',prepost = True)
df4a=pd.DataFrame(data2)
df4a.reset_index(drop=False,inplace=True)
print(df4a.tail(10))
print('kaku')


print('\n\n\n')
print('1day_low/High =======> ',(df4a['Low'].tail(1).min()).round(2),'    ',df4a['High'].tail(1).max(),' swing = ', (df4a['High'].tail(1).max()- df4a['Low'].tail(1).min()).round(2),
'   Volume:',(df4a['Volume'].tail(1).mean()).round(2))
print('3day_low/High =======> ',(df4a['Low'].tail(3).min()).round(2),'    ',df4a['High'].tail(3).max(),' swing = ', (df4a['High'].tail(3).max()- df4a['Low'].tail(3).min()).round(2),
'    Volume:',(df4a['Volume'].tail(3).mean()).round(2))
print('5day_low/High =======> ',(df4a['Low'].tail(5).min()).round(2),'    ',df4a['High'].tail(5).max(),' swing = ', (df4a['High'].tail(5).max()- df4a['Low'].tail(5).min()).round(2),
'    Volume:',(df4a['Volume'].tail(5).mean()).round(2))
print('7day_low/High =======> ',(df4a['Low'].tail(7).min()).round(2),'    ',df4a['High'].tail(7).max(),' swing = ', (df4a['High'].tail(7).max()- df4a['Low'].tail(7).min()).round(2),
'    Volume:',(df4a['Volume'].tail(7).mean()).round(2))
print('10day_low/High =======> ',(df4a['Low'].tail(10).min()).round(2),'    ',df4a['High'].tail(10).max(),' swing = ', (df4a['High'].tail(10).max()- df4a['Low'].tail(10).min()).round(2),
'    Volume:',(df4a['Volume'].tail(10).mean()).round(2))
print('21day_low/High =======> ',(df4a['Low'].tail(21).min()).round(2),'    ',df4a['High'].tail(21).max(),' swing = ', (df4a['High'].tail(21).max()- df4a['Low'].tail(21).min()).round(2),
'    Volume:',(df4a['Volume'].tail(21).mean()).round(2))
print('30day_low/High =======> ',(df4a['Low'].tail(30).min()).round(2),'    ',df4a['High'].tail(30).max(),' swing = ', (df4a['High'].tail(30).max()- df4a['Low'].tail(30).min()).round(2),
'    Volume:',(df4a['Volume'].tail(30).mean()).round(2))
print('60day_low/High =======> ',(df4a['Low'].tail(60).min()).round(2),'    ',df4a['High'].tail(60).max(),' swing = ', (df4a['High'].tail(60).max()- df4a['Low'].tail(60).min()).round(2),
'    Volume:',(df4a['Volume'].tail(60).mean()).round(2))
print('90day_low/High =======> ',(df4a['Low'].tail(90).min()).round(2),'    ',df4a['High'].tail(90).max(),' swing = ', (df4a['High'].tail(90).max()- df4a['Low'].tail(90).min()).round(2),
'    Volume:',(df4a['Volume'].tail(90).mean()).round(2))
print('180day_low/High =======> ',(df4a['Low'].tail(180).min()).round(2),'    ',df4a['High'].tail(180).max(),' swing = ', (df4a['High'].tail(180).max()- df4a['Low'].tail(180).min()).round(2),
'    Volume:',(df4a['Volume'].tail(180).mean()).round(2))
print('300day_low/High =======> ',(df4a['Low'].tail(300).min()).round(2),'    ',df4a['High'].tail(300).max(),' swing = ', (df4a['High'].tail(300).max()- df4a['Low'].tail(300).min()).round(2),
'    Volume:',(df4a['Volume'].tail(180).mean()).round(2))

# print('tail 1',df4a['Date'].tail(1))
# print('tail 2',df4a['Date'].tail(2))
print('\n\n\n')

print(today,'   ddddddddddddddddddddddddddd', df4a['Date'].tail(1))
if today is not df4a['Date'].tail(1):
    print("JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ")
    
    
    pp=(df4a['Close'].tail(1)+df4a['Low'].tail(1)+df4a['High'].tail(1))/3
    r1=2*pp-df4a['Low'].tail(1).round(0)
    r2=pp+(df4a['High'].tail(1)-df4a['Low'].tail(1))
    s1=2*pp-df4a['High'].tail(1)
    s2=pp-(df4a['High'].tail(1)-df4a['Low'].tail(1))
    r3=df4a['High'].tail(1)+2*(pp-df4a['Low'].tail(1))
    s3=df4a['Low'].tail(1)-2*(df4a['High'].tail(1)-pp)

    pp=pp.to_string(header=None, index=None)
    r1=r1.to_string(header=None, index=None)
    r2=r2.to_string(header=None, index=None)
    r3=r3.to_string(header=None, index=None)
    
    s1=s1.to_string(header=None, index=None)
    s2=s2.to_string(header=None, index=None)
    s3=s3.to_string(header=None, index=None)
    
    
    s1=s1.split('.')[0]
    s2=s2.split('.')[0]
    s3=s3.split('.')[0]
    r1=r1.split('.')[0]
    r2=r2.split('.')[0]
    r3=r3.split('.')[0]
    pp=pp.split('.')[0]
    
########################################################


####################### 60 mins #########################
# ###################  ##########################
# data3 =yf.download(ticker, period='1d', interval='5m',prepost = True)
# df4b=pd.DataFrame(data3)
# df4b.reset_index(drop=False,inplace=True)

# ppb=(df4b['Close'].tail(1)+df4b['Low'].tail(1)+df4b['High'].tail(1))/3
# r1b=2*ppb-df4b['Low'].tail(1).round(0)
# r2b=ppb+(df4b['High'].tail(1)-df4b['Low'].tail(1))
# s1b=2*ppb-df4b['High'].tail(1)
# s2b=ppb-(df4b['High'].tail(1)-df4b['Low'].tail(1))
# r3b=df4b['High'].tail(1)+2*(ppb-df4b['Low'].tail(1))
# s3b=df4b['Low'].tail(1)-2*(df4b['High'].tail(1)-ppb)

# ppb=ppb.to_string(header=None, index=None)
# r1b=r1b.to_string(header=None, index=None)
# r2b=r2b.to_string(header=None, index=None)
# r3b=r3b.to_string(header=None, index=None)
# s1b=s1b.to_string(header=None, index=None)
# s2b=s2b.to_string(header=None, index=None)
# s3b=s3b.to_string(header=None, index=None)
# ########################################################
# ########################################################
# ################### 5m  ##########################
# data4 =yf.download(ticker, period='1d', interval='5m',prepost = True)
# df4c=pd.DataFrame(data4)
# df4c.reset_index(drop=False,inplace=True)

# ppc=(df4c['Close'].tail(1)+df4c['Low'].tail(1)+df4c['High'].tail(1))/3
# r1c=2*ppc-df4c['Low'].tail(1).round(0)
# r2c=ppc+(df4c['High'].tail(1)-df4c['Low'].tail(1))
# s1c=2*ppc-df4c['High'].tail(1)
# s2c=ppc-(df4c['High'].tail(1)-df4c['Low'].tail(1))
# r3c=df4c['High'].tail(1)+2*(ppc-df4c['Low'].tail(1))
# s3c=df4c['Low'].tail(1)-2*(df4c['High'].tail(1)-ppc)

# ppc=ppc.to_string(header=None, index=None)
# r1c=r1c.to_string(header=None, index=None)
# r2c=r2c.to_string(header=None, index=None)
# r3c=r3c.to_string(header=None, index=None)
# s1c=s1c.to_string(header=None, index=None)
# s2c=s2c.to_string(header=None, index=None)
# s3c=s3c.to_string(header=None, index=None)
# ########################### 30 m #############################
# data5 =yf.download(ticker, period='1d', interval='30m',prepost = True)
# df4d=pd.DataFrame(data5)
# df4d.reset_index(drop=False,inplace=True)

# ppd=(df4d['Close'].tail(1)+df4d['Low'].tail(1)+df4d['High'].tail(1))/3
# r1d=2*ppd-df4d['Low'].tail(1).round(0)
# r2d=ppd+(df4d['High'].tail(1)-df4d['Low'].tail(1))
# s1d=2*ppd-df4d['High'].tail(1)
# s2d=ppd-(df4d['High'].tail(1)-df4d['Low'].tail(1))
# r3d=df4d['High'].tail(1)+2*(ppd-df4d['Low'].tail(1))
# s3d=df4d['Low'].tail(1)-2*(df4d['High'].tail(1)-ppd)

# ppd=ppd.to_string(header=None, index=None)
# r1d=r1d.to_string(header=None, index=None)
# r2d=r2d.to_string(header=None, index=None)
# r3d=r3d.to_string(header=None, index=None)
# s1d=s1d.to_string(header=None, index=None)
# s2d=s2d.to_string(header=None, index=None)
# s3d=s3d.to_string(header=None, index=None)

##########################################################
###################   ##########################

########################################################
#uu=='calls'


uu=chain['calls']
uu = uu.replace('-', '0')
mm_calls=0
for x in uu.index:
    mm_calls=mm_calls+int(uu['Volume'].loc[x])
    
##########
uu=chain['puts']
uu = uu.replace('-', '0')
mm_puts=0
for x in uu.index:
    mm_puts=mm_puts+int(uu['Volume'].loc[x])
        #    print(uu['Volume'].loc[x])
    

##########################################################
uu=chain[what_option]

if what_option == 'calls':
#     uu = uu.replace('-', '0')
# #    print(uu)
#     print("kaku calls:")
    
#     mm_calls=0
#     for x in uu.index:
#         mm_calls=mm_calls+int(uu['Volume'].loc[x])
    
    d1=[]
    d2=[]
    d3=[]
    d4=[]
    for x in uu.index:
        d1.append(ss)
        d2.append(cc[0:6])
        d3.append('calls')
        d4.append('x')
    
    df4=pd.DataFrame([d1,d2,d3,d4])
    df4=df4.T
    df4.columns=['Stock_Price','b','c','d']
    # print(df4)
    uu33=pd.concat([uu,df4],axis=1)
    # print(uu33.columns)

    uu33['mid']=''
    uu33['distance']=''
    uu33['mid2']=''
    uu33['mid3']=''
    uu33['Cntrt_Price']='' 
    uu33['Stop_loss']=''
    uu33['wide']=''
    uu33['Loss']=''
    uu33['Prft']=''
    uu33['Stp_loss_loss']=''
    uu33['shares']=''

    uu33['Bid'] = uu33['Bid'].replace('-', '0')
    uu33['Ask'] = uu33['Ask'].replace('-', '0')

#    uu33['u6']=uu33['Stock_Price']-uu33['Strike']


    print('andrea boggs')
    print(type(uu33['Cntrt_Price'].loc[3]),'    ',type(money))



    for x in uu33.index:
        uu33['wide'].loc[x]=uu33['Strike'].loc[x]-uu33['Strike'].shift(1).loc[x]
#        print(type(np.float64(uu33['Stock_Price'].loc[x])),'    ',type(uu33['Strike'].loc[x]))
        uu33['distance'].loc[x] = np.float64(uu33['Stock_Price'].loc[x]) - uu33['Strike'].loc[x]
      #  uu33['mid'].loc[x]=(np.float64(uu33['Bid'].loc[x])+np.float64(uu33['Ask'].loc[x]))/2
        uu33['mid'].loc[x]=uu33['Last Price'].loc[x]
        uu33['mid2'].loc[x]=uu33['mid'].shift(1).loc[x]
        uu33['mid3'].loc[x]=abs(uu33['mid2'].loc[x]-uu33['mid'].loc[x])
        uu33['Cntrt_Price'].loc[x]=uu33['mid3'].loc[x]
        uu33['shares'].loc[x]=np.int64((np.int64(money) / np.float64(uu33['Cntrt_Price'].loc[x]))/100)
        uu33['Stop_loss'].loc[x]=uu33['Cntrt_Price'].loc[x]+uu33['Cntrt_Price'].loc[x]*10/100
        uu33['Loss'].loc[x]=(uu33['wide'].loc[x]-uu33['Cntrt_Price'].loc[x])*np.int64(uu33['shares'].loc[x])*100
        
        
    for x in uu33.index:
        uu33['Prft'].loc[x]=np.int64(uu33['shares'].loc[x]) * np.float64(uu33['Cntrt_Price'].loc[x]) *100
        
        
        
        # uu33['Stp_loss_loss'].loc[x]=   *np.float64(uu33['shares'].loc[x])*100).round(0)

    for x in uu33.index:
        if (uu33['mid3'].loc[x]) > 0.2:
            uu33['Cntrt_Price'].shift(1).loc[x]=uu33['mid3'].loc[x]


 # -uu33['Strike'].loc[x]
 
    # uu33=uu33[['Contract Name', 'Last Trade Date', 'Strike', 'Stock_Price','distance','Last Price', 'Bid','Ask', 'Change', '% Change', 'Volume', 'Open Interest','Implied Volatility', 'Stock_Price', 'b', 'c', 'd', 'distance']]
    # uu33=uu33[['Contract Name', 'Last Trade Date', 'Strike', 'Stock_Price','distance','mid','Cntrt_Price','Stop_loss','Last Price', 'Bid','Ask', 
    # # 'Change', '% Change', 'Volume', 'Open Interest','Implied Volatility', 'b', 'c', 'd','mid3','wide']]
    # uu33=uu33[['Contract Name', 'Last Trade Date', 'Strike', 'Stock_Price','distance','Cntrt_Price','Stop_loss','wide','Last Price', 'Bid','Ask', 'mid',
    # 'Change', '% Change', 'Volume', 'Open Interest','Implied Volatility', 'c','mid3','Loss','Prft','shares']]
    uu33=uu33[['Last Trade Date', 'Strike', 'Stock_Price','distance','Cntrt_Price','Stop_loss','wide','Last Price', 'Bid','Ask', 'mid',
    'Change', '% Change', 'Volume', 'Open Interest','Implied Volatility', 'c','mid3','Loss','Prft','shares']]
    uu33=uu33[np.float64(uu33['distance']) < 0]
    uu33=uu33[np.float64(uu33['mid3']) > 0.2]


    uu33.reset_index(drop=True,inplace=True)

#df = df.reset_index()

#    print(uu33.index)
#    uu33.style.apply(highlight_greaterthan, threshold=1.0,  axis=1)


#    s = uu33.reset_index(drop=True).style.applymap(color_negative_red)
#    print(s)
    print(bg.blue +str(uu33) + bg.rs)
    print('\n\n')
    print(ticker,' calls ----> ',mm_calls,'   ',cc)
    print(ticker,' for ',cc,' calls-puts volume, [calls_volume-puts_volume]= ',mm_calls-mm_puts, '   % of calls=',(100*mm_calls/(mm_calls+mm_puts)), '% of puts=',(100-100*mm_calls/(mm_calls+mm_puts))  )


# bg.blue + 'This has a blue background!' + bg.rs

##################################################
# uu=chain[what_option]
if what_option=='puts':
    # uu = uu.replace('-', '0')
    # print(uu)
    # print("kaku puts:")
    
    # mm_puts=0
    # for x in uu.index:
    #     mm_puts=mm_puts+int(uu['Volume'].loc[x])
    #         #    print(uu['Volume'].loc[x])
    
    
    d1=[]
    d2=[]
    d3=[]
    d4=[]
    for x in uu.index:
        d1.append(ss)
        d2.append(cc)
        d3.append('puts')
        d4.append('x')
    
    df4=pd.DataFrame([d1,d2,d3,d4])
    df4=df4.T
    # print(df4)
    
    
    df4.columns=['Stock_Price','b','c','d']
    # print(df4)
    uu33=pd.concat([uu,df4],axis=1)
    # print(uu33.columns)
    


    uu33['mid']=''
    uu33['distance']=''
    uu33['mid2']=''
    uu33['mid3']=''
    uu33['Cntrt_Price']=''
    uu33['Stop_loss']=''


    uu33['Bid'] = uu33['Bid'].replace('-', '0')
    uu33['Ask'] = uu33['Ask'].replace('-', '0')






#    uu33['u6']=uu33['Stock_Price']-uu33['Strike']
    for x in uu33.index:
#        print(type(np.float64(uu33['Stock_Price'].loc[x])),'    ',type(uu33['Strike'].loc[x]))
        uu33['distance'].loc[x] = np.float64(uu33['Stock_Price'].loc[x]) - uu33['Strike'].loc[x]
#        uu33['mid'].loc[x]=(np.float64(uu33['Bid'].loc[x])+np.float64(uu33['Ask'].loc[x]))/2
        uu33['mid'].loc[x]=uu33['Last Price'].loc[x]
        uu33['mid2'].loc[x]=uu33['mid'].shift(1).loc[x]
        uu33['mid3'].loc[x]=abs(uu33['mid2'].loc[x]-uu33['mid'].loc[x])
        uu33['Cntrt_Price'].loc[x]=uu33['mid3'].loc[x]
        uu33['Stop_loss'].loc[x]=uu33['Cntrt_Price'].loc[x]+uu33['Cntrt_Price'].loc[x]*10/100

    for x in uu33.index:
        if uu33['mid3'].loc[x] > 0.2:
            uu33['Cntrt_Price'].shift(1).loc[x]=uu33['mid3'].loc[x]



 # -uu33['Strike'].loc[x]

#    uu33=uu33[['Contract Name', 'Last Trade Date', 'Strike', 'Stock_Price','distance','Last Price', 'Bid','Ask', 'Change', '% Change', 'Volume', 'Open Interest','Implied Volatility', 'Stock_Price', 'b', 'c', 'd', 'distance']]
    uu33=uu33[['Contract Name', 'Last Trade Date', 'Strike', 'Stock_Price','distance','mid','Cntrt_Price','Stop_loss','Last Price', 'Bid','Ask', 
    'Change', '% Change', 'Volume', 'Open Interest','Implied Volatility', 'b', 'c', 'd','mid3']]
    uu33=uu33[np.float64(uu33['distance']) > 0]
    uu33=uu33[np.float64(uu33['Cntrt_Price']) > 0.2]





    print(uu33)

    print('\n\n')
    print(ticker,' puts --- > ',mm_puts,'   ',cc)
    print(ticker,' for ',cc,' calls-puts volume, [calls_volume-puts_volume]= ',mm_calls-mm_puts, '   % of calls=',100*mm_calls/(mm_calls+mm_puts)), '% of puts=',100-int(100*mm_calls/(mm_calls+mm_puts))
####################################################
print('\n\n')
print('***************************************************')
print('\n\n')
#print('Stock Calls/Puts distribution for options',x)

'''
print(nflx_dates)
print('\n')

for x in nflx_dates:

    chain = options.get_options_chain(ticker,x)
    uu5=chain['calls']
    uu5 = uu5.replace('-', '0')
    mm_calls3=0
    for x2 in uu5.index:
        mm_calls3=mm_calls3+int(uu5['Volume'].loc[x2])
        
    uu6=chain['puts']
    uu6 = uu6.replace('-', '0')
    mm_puts3=0
    for x2 in uu6.index:
        mm_puts3=mm_puts3+int(uu6['Volume'].loc[x2])   
    
    print(x,'  ',ticker,'   [calls-puts=]',mm_calls3-mm_puts3, '   % of calls=',int(100*mm_calls3/(mm_calls3+mm_puts3+.1)), '  % of puts=',100-int(100*mm_calls3/(mm_calls3+mm_puts3+.1)))    
'''
print('\n\n')
print('****************** pivot Fabonaci *** ', ticker,' 1 day ******************************')
t3=(np.float(ss)-np.float(pp))

s1a=np.float(s1)-np.float(ss)
s2a=np.float(s2)-np.float(ss)
s3a=np.float(s3)-np.float(ss)

r1a=np.float(r1)-np.float(ss)
r2a=np.float(r2)-np.float(ss)
r3a=np.float(r3)-np.float(ss)

print(ticker, '-->', s1,' ',s2,' ',s3,'  ******** ',pp,' ********',r1,' ',r2,' ',r3,' ',' stockprice=  ',np.round(np.float(ss),1), '  [stkprice - pivot]= ',np.round(t3,1))
print(ticker, '-->', np.round(s1a,0),' ',np.round(s2a,0),' ',np.round(s3a,0),' ****** ',np.round(t3,0),' ****** ',np.round(r1a,0),' ',np.round(r2a,0),' ',np.round(r3a,0))



#################################################################
################### 1h  ##########################
data2 =yf.download(ticker, period='20d', interval='1h')
#data2 =yf.download(ticker, period='6d', interval='1d',prepost = True)
df4a=pd.DataFrame(data2)
df4a.reset_index(drop=False,inplace=True)
u7=df4a.shape[0]
# print(df4a.tail(u7))
# print(df4a.tail(5))
print('kaku')


# print('tail 1',df4a['Date'].tail(1))
# print('tail 2',df4a['Date'].tail(2))


#print('5day ','   ddddddddddddddddddddddddddd', df4a['Datetime'].tail(1))

    
pp=(df4a['Close'].tail(1)+df4a['Low'].tail(1)+df4a['High'].tail(1))/3
r1=2*pp-df4a['Low'].tail(1).round(0)
r2=pp+(df4a['High'].tail(1)-df4a['Low'].tail(1))
s1=2*pp-df4a['High'].tail(1)
s2=pp-(df4a['High'].tail(1)-df4a['Low'].tail(1))
r3=df4a['High'].tail(1)+2*(pp-df4a['Low'].tail(1))
s3=df4a['Low'].tail(1)-2*(df4a['High'].tail(1)-pp)

pp=pp.to_string(header=None, index=None)
r1=r1.to_string(header=None, index=None)
r2=r2.to_string(header=None, index=None)
r3=r3.to_string(header=None, index=None)

s1=s1.to_string(header=None, index=None)
s2=s2.to_string(header=None, index=None)
s3=s3.to_string(header=None, index=None)


s1=s1.split('.')[0]
s2=s2.split('.')[0]
s3=s3.split('.')[0]
r1=r1.split('.')[0]
r2=r2.split('.')[0]
r3=r3.split('.')[0]
pp=pp.split('.')[0]
    

print('\n\n')
print('****************** pivot Fabonaci *** ', ticker,' 1h ******************************')
t3=(np.float(ss)-np.float(pp))

s1a=np.float(s1)-np.float(ss)
s2a=np.float(s2)-np.float(ss)
s3a=np.float(s3)-np.float(ss)

r1a=np.float(r1)-np.float(ss)
r2a=np.float(r2)-np.float(ss)
r3a=np.float(r3)-np.float(ss)

print(ticker, '-->', s1,' ',s2,' ',s3,'  ******** ',pp,' ********',r1,' ',r2,' ',r3,' ',' stockprice=  ',np.round(np.float(ss),1), '  [stkprice - pivot]= ',np.round(t3,1))
print(ticker, '-->', np.round(s1a,0),' ',np.round(s2a,0),' ',np.round(s3a,0),' ****** ',np.round(t3,0),' ****** ',np.round(r1a,0),' ',np.round(r2a,0),' ',np.round(r3a,0))


###############################################################################################################################
################### 90 min  ##########################
data2 =yf.download(ticker, period='20d', interval='90m')
#data2 =yf.download(ticker, period='6d', interval='1d',prepost = True)
df4a=pd.DataFrame(data2)
df4a.reset_index(drop=False,inplace=True)
u7=df4a.shape[0]
# print(df4a.tail(u7))
# print(df4a.tail(5))
print('kaku')


# print('tail 1',df4a['Date'].tail(1))
# print('tail 2',df4a['Date'].tail(2))


#print('5day ','   ddddddddddddddddddddddddddd', df4a['Datetime'].tail(1))

    
pp=(df4a['Close'].tail(1)+df4a['Low'].tail(1)+df4a['High'].tail(1))/3
r1=2*pp-df4a['Low'].tail(1).round(0)
r2=pp+(df4a['High'].tail(1)-df4a['Low'].tail(1))
s1=2*pp-df4a['High'].tail(1)
s2=pp-(df4a['High'].tail(1)-df4a['Low'].tail(1))
r3=df4a['High'].tail(1)+2*(pp-df4a['Low'].tail(1))
s3=df4a['Low'].tail(1)-2*(df4a['High'].tail(1)-pp)

pp=pp.to_string(header=None, index=None)
r1=r1.to_string(header=None, index=None)
r2=r2.to_string(header=None, index=None)
r3=r3.to_string(header=None, index=None)

s1=s1.to_string(header=None, index=None)
s2=s2.to_string(header=None, index=None)
s3=s3.to_string(header=None, index=None)


s1=s1.split('.')[0]
s2=s2.split('.')[0]
s3=s3.split('.')[0]
r1=r1.split('.')[0]
r2=r2.split('.')[0]
r3=r3.split('.')[0]
pp=pp.split('.')[0]
    

print('\n\n')
print('****************** pivot Fabonaci *** ', ticker,' 90m ******************************')
t3=(np.float(ss)-np.float(pp))

s1a=np.float(s1)-np.float(ss)
s2a=np.float(s2)-np.float(ss)
s3a=np.float(s3)-np.float(ss)

r1a=np.float(r1)-np.float(ss)
r2a=np.float(r2)-np.float(ss)
r3a=np.float(r3)-np.float(ss)

print(ticker, '-->', s1,' ',s2,' ',s3,'  ******** ',pp,' ********',r1,' ',r2,' ',r3,' ',' stockprice=  ',np.round(np.float(ss),1), '  [stkprice - pivot]= ',np.round(t3,1))
print(ticker, '-->', np.round(s1a,0),' ',np.round(s2a,0),' ',np.round(s3a,0),' ****** ',np.round(t3,0),' ****** ',np.round(r1a,0),' ',np.round(r2a,0),' ',np.round(r3a,0))


###############################################################################################################################
################### 5 min  ##########################
data2 =yf.download(ticker, period='20d', interval='30m')
#data2 =yf.download(ticker, period='6d', interval='1d',prepost = True)
df4a=pd.DataFrame(data2)
df4a.reset_index(drop=False,inplace=True)
u7=df4a.shape[0]
# print(df4a.tail(u7))
# print(df4a.tail(5))
print('kaku')


# print('tail 1',df4a['Date'].tail(1))
# print('tail 2',df4a['Date'].tail(2))


#print('5day ','   ddddddddddddddddddddddddddd', df4a['Datetime'].tail(1))

    
pp=(df4a['Close'].tail(1)+df4a['Low'].tail(1)+df4a['High'].tail(1))/3
r1=2*pp-df4a['Low'].tail(1).round(0)
r2=pp+(df4a['High'].tail(1)-df4a['Low'].tail(1))
s1=2*pp-df4a['High'].tail(1)
s2=pp-(df4a['High'].tail(1)-df4a['Low'].tail(1))
r3=df4a['High'].tail(1)+2*(pp-df4a['Low'].tail(1))
s3=df4a['Low'].tail(1)-2*(df4a['High'].tail(1)-pp)

pp=pp.to_string(header=None, index=None)
r1=r1.to_string(header=None, index=None)
r2=r2.to_string(header=None, index=None)
r3=r3.to_string(header=None, index=None)

s1=s1.to_string(header=None, index=None)
s2=s2.to_string(header=None, index=None)
s3=s3.to_string(header=None, index=None)


s1=s1.split('.')[0]
s2=s2.split('.')[0]
s3=s3.split('.')[0]
r1=r1.split('.')[0]
r2=r2.split('.')[0]
r3=r3.split('.')[0]
pp=pp.split('.')[0]
    

print('\n\n')
print('****************** pivot Fabonaci *** ', ticker,' 30m ******************************')
t3=(np.float(ss)-np.float(pp))

s1a=np.float(s1)-np.float(ss)
s2a=np.float(s2)-np.float(ss)
s3a=np.float(s3)-np.float(ss)

r1a=np.float(r1)-np.float(ss)
r2a=np.float(r2)-np.float(ss)
r3a=np.float(r3)-np.float(ss)

print(ticker, '-->', s1,' ',s2,' ',s3,'  ******** ',pp,' ********',r1,' ',r2,' ',r3,' ',' stockprice=  ',np.round(np.float(ss),1), '  [stkprice - pivot]= ',np.round(t3,1))
print(ticker, '-->', np.round(s1a,0),' ',np.round(s2a,0),' ',np.round(s3a,0),' ****** ',np.round(t3,0),' ****** ',np.round(r1a,0),' ',np.round(r2a,0),' ',np.round(r3a,0))


###############################################################################################################################
################### 5 min  ##########################
data2 =yf.download(ticker, period='20d', interval='5m')
#data2 =yf.download(ticker, period='6d', interval='1d',prepost = True)
df4a=pd.DataFrame(data2)
df4a.reset_index(drop=False,inplace=True)
u7=df4a.shape[0]
# print(df4a.tail(u7))
# print(df4a.tail(5))
print('kaku')


# print('tail 1',df4a['Date'].tail(1))
# print('tail 2',df4a['Date'].tail(2))


#print('5day ','   ddddddddddddddddddddddddddd', df4a['Datetime'].tail(1))

    
pp=(df4a['Close'].tail(1)+df4a['Low'].tail(1)+df4a['High'].tail(1))/3
r1=2*pp-df4a['Low'].tail(1).round(0)
r2=pp+(df4a['High'].tail(1)-df4a['Low'].tail(1))
s1=2*pp-df4a['High'].tail(1)
s2=pp-(df4a['High'].tail(1)-df4a['Low'].tail(1))
r3=df4a['High'].tail(1)+2*(pp-df4a['Low'].tail(1))
s3=df4a['Low'].tail(1)-2*(df4a['High'].tail(1)-pp)

pp=pp.to_string(header=None, index=None)
r1=r1.to_string(header=None, index=None)
r2=r2.to_string(header=None, index=None)
r3=r3.to_string(header=None, index=None)

s1=s1.to_string(header=None, index=None)
s2=s2.to_string(header=None, index=None)
s3=s3.to_string(header=None, index=None)


s1=s1.split('.')[0]
s2=s2.split('.')[0]
s3=s3.split('.')[0]
r1=r1.split('.')[0]
r2=r2.split('.')[0]
r3=r3.split('.')[0]
pp=pp.split('.')[0]
    

print('\n\n')
print('****************** pivot Fabonaci *** ', ticker,' 5min ******************************')
t3=(np.float(ss)-np.float(pp))

s1a=np.float(s1)-np.float(ss)
s2a=np.float(s2)-np.float(ss)
s3a=np.float(s3)-np.float(ss)

r1a=np.float(r1)-np.float(ss)
r2a=np.float(r2)-np.float(ss)
r3a=np.float(r3)-np.float(ss)

print(ticker, '-->', s1,' ',s2,' ',s3,'  ******** ',pp,' ********',r1,' ',r2,' ',r3,' ',' stockprice=  ',np.round(np.float(ss),1), '  [stkprice - pivot]= ',np.round(t3,1))
print(ticker, '-->', np.round(s1a,0),' ',np.round(s2a,0),' ',np.round(s3a,0),' ****** ',np.round(t3,0),' ****** ',np.round(r1a,0),' ',np.round(r2a,0),' ',np.round(r3a,0))


###############################################################################################################################
################### 5 min  ##########################
data2 =yf.download(ticker, period='20d', interval='30m')
#data2 =yf.download(ticker, period='6d', interval='1d',prepost = True)
df4a=pd.DataFrame(data2)
df4a.reset_index(drop=False,inplace=True)
u7=df4a.shape[0]
# print(df4a.tail(u7))
# print(df4a.tail(5))
print('kaku')


# print('tail 1',df4a['Date'].tail(1))
# print('tail 2',df4a['Date'].tail(2))


#print('5day ','   ddddddddddddddddddddddddddd', df4a['Datetime'].tail(1))

    
pp=(df4a['Close'].tail(1)+df4a['Low'].tail(1)+df4a['High'].tail(1))/3
r1=2*pp-df4a['Low'].tail(1).round(0)
r2=pp+(df4a['High'].tail(1)-df4a['Low'].tail(1))
s1=2*pp-df4a['High'].tail(1)
s2=pp-(df4a['High'].tail(1)-df4a['Low'].tail(1))
r3=df4a['High'].tail(1)+2*(pp-df4a['Low'].tail(1))
s3=df4a['Low'].tail(1)-2*(df4a['High'].tail(1)-pp)

pp=pp.to_string(header=None, index=None)
r1=r1.to_string(header=None, index=None)
r2=r2.to_string(header=None, index=None)
r3=r3.to_string(header=None, index=None)

s1=s1.to_string(header=None, index=None)
s2=s2.to_string(header=None, index=None)
s3=s3.to_string(header=None, index=None)


s1=s1.split('.')[0]
s2=s2.split('.')[0]
s3=s3.split('.')[0]
r1=r1.split('.')[0]
r2=r2.split('.')[0]
r3=r3.split('.')[0]
pp=pp.split('.')[0]
    

print('\n\n')
print('****************** pivot Fabonaci *** ', ticker,' 30m ******************************')
t3=(np.float(ss)-np.float(pp))

s1a=np.float(s1)-np.float(ss)
s2a=np.float(s2)-np.float(ss)
s3a=np.float(s3)-np.float(ss)

r1a=np.float(r1)-np.float(ss)
r2a=np.float(r2)-np.float(ss)
r3a=np.float(r3)-np.float(ss)

print(ticker, '-->', s1,' ',s2,' ',s3,'  ******** ',pp,' ********',r1,' ',r2,' ',r3,' ',' stockprice=  ',np.round(np.float(ss),1), '  [stkprice - pivot]= ',np.round(t3,1))
print(ticker, '-->', np.round(s1a,0),' ',np.round(s2a,0),' ',np.round(s3a,0),' ****** ',np.round(t3,0),' ****** ',np.round(r1a,0),' ',np.round(r2a,0),' ',np.round(r3a,0))


###############################################################################################################################
################### 5 min  ##########################
data2 =yf.download(ticker, period='2d', interval='1m')
#data2 =yf.download(ticker, period='6d', interval='1d',prepost = True)
df4a=pd.DataFrame(data2)
df4a.reset_index(drop=False,inplace=True)
u7=df4a.shape[0]
# print(df4a.tail(u7))
# print(df4a.tail(5))
print('kaku')


# print('tail 1',df4a['Date'].tail(1))
# print('tail 2',df4a['Date'].tail(2))


#print('5day ','   ddddddddddddddddddddddddddd', df4a['Datetime'].tail(1))

    
pp=(df4a['Close'].tail(1)+df4a['Low'].tail(1)+df4a['High'].tail(1))/3
r1=2*pp-df4a['Low'].tail(1).round(0)
r2=pp+(df4a['High'].tail(1)-df4a['Low'].tail(1))
s1=2*pp-df4a['High'].tail(1)
s2=pp-(df4a['High'].tail(1)-df4a['Low'].tail(1))
r3=df4a['High'].tail(1)+2*(pp-df4a['Low'].tail(1))
s3=df4a['Low'].tail(1)-2*(df4a['High'].tail(1)-pp)

pp=pp.to_string(header=None, index=None)
r1=r1.to_string(header=None, index=None)
r2=r2.to_string(header=None, index=None)
r3=r3.to_string(header=None, index=None)

s1=s1.to_string(header=None, index=None)
s2=s2.to_string(header=None, index=None)
s3=s3.to_string(header=None, index=None)


s1=s1.split('.')[0]
s2=s2.split('.')[0]
s3=s3.split('.')[0]
r1=r1.split('.')[0]
r2=r2.split('.')[0]
r3=r3.split('.')[0]
pp=pp.split('.')[0]
    

print('\n\n')
print('****************** pivot Fabonaci *** ', ticker,' 1min ******************************')
t3=(np.float(ss)-np.float(pp))

s1a=np.float(s1)-np.float(ss)
s2a=np.float(s2)-np.float(ss)
s3a=np.float(s3)-np.float(ss)

r1a=np.float(r1)-np.float(ss)
r2a=np.float(r2)-np.float(ss)
r3a=np.float(r3)-np.float(ss)

print(ticker, '-->', s1,' ',s2,' ',s3,'  ******** ',pp,' ********',r1,' ',r2,' ',r3,' ',' stockprice=  ',np.round(np.float(ss),1), '  [stkprice - pivot]= ',np.round(t3,1))
print(ticker, '-->', np.round(s1a,0),' ',np.round(s2a,0),' ',np.round(s3a,0),' ****** ',np.round(t3,0),' ****** ',np.round(r1a,0),' ',np.round(r2a,0),' ',np.round(r3a,0))


###############################################################################################################################
#print(' ',np.float(s1)-np.float(ss),' ',np.float(s2)-np.float(ss),'/',np.float(s3)-np.float(ss))
#'***','  ','****',np.float(r1)-np.float(ss),' ',np.float(r2)-np.float(ss),' ',np.float(r3)-np.float(ss))


#print('1day --> ',s1,'/',s2,'/',s3,'  ',pp,'  ',r1,'/',r2,'/',r3, '  ',ticker,'  stockprice=  ',ss,' stock_price-pivot=',ss-pp)
#print('1day --> ',int(s1),' - ',int(s2),' - ',int(s3),'***** ',int(pp),' **** ',int(r1),' - ',int(r2),' - ',int(r3),'   currend',ticker,' = ',ss)
#print('1day --> ',s1,'-',s2,'-',s3)
#,' ',int(float(s2)),' ',int(float(s3)),' ')
#####2,'-',s3,' *** ',pp, ' *** ', r1,'-',r2,'-',r3)
# print('60m --> ',s1b,'/',s2b,'/',s3b,'  ',ppb,'  ',r1b,'/',r2b,'/',r3b)
#s12,'/',s22,'/',s32,'  ',pp2,'  ',r12,'/',r22,'/',r32)
#print('3day --> ',s1,'/',s2,'/',s3,'  ',pp,'  ',r1,'/',r2,'/',r3)
# print('5mins_today---> ', s1c,'/',s2c,'/',s3c,'  ',ppc,'  ',r1c,'/',r2c,'/',r3c)
# print('30mins_today---> ', s1d,'/',s2d,'/',s3d,'  ',ppd,'  ',r1d,'/',r2d,'/',r3d)
# print('60mins_today---> ', s1b,'/',s2b,'/',s3b,'  ',ppb,'  ',r1b,'/',r2b,'/',r3b)



