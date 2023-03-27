##import talib as ta
##from ta.utils import dropna
import yfinance as yf
from yfinance import Ticker as yf2
import pandas as pd
import sys
##import re
import numpy as np
##from talib import stream

from millify import millify
##today = datetime.date.today() + datetime.timedelta(days=1)
##today = date.date.today()
##day = datetime.datetime.strptime(Date, '%d %m %Y').weekday()
##print(datetime.today().strftime('%Y-%m-%d'))
##import mpl_finance
##import matplotlib
import sys
##from matplotlib.finance import candlestick2_ohlc
##from mpl_finance import candlestick_ohlc
##from mplfinance.original_flavor import candlestick_ohlc
import streamlit as st
st.legacy_caching.clear_cache()
    
from numerize import numerize
import matplotlib.pyplot as plt
pd.options.display.width = 0
pd.set_option('display.max_columns', None)
pd.options.display.float_format = '{:.2f}'.format
##pd.options.display.max_columns=255
pd.options.display.max_rows=6500000
pd.set_option('display.max_colwidth', 500)
pd.set_option('display.max_columns', 550)
pd.options.mode.chained_assignment = None  # default='warn'
import sys
import re

##global n2,n4,breakz
n2=2
n4=2
##breakz=10000


def Step1_read_tickers_from_file_and_align():
    import os
    os.remove('/home/az2/t65.txt')

##    f3a=open('/home/az2/t7.txt','r')
##    for x in f3a:
##        print(x)
##    f3a.close()


##    fa='/home/az2/t7_monday.txt'
##    fa='/home/az2/t7_tuesday.txt'
    fa='/home/az2/t7_wednesday.txt'
##    fa='/home/az2/t7_thursday.txt'
##    fa='/home/az2/t7_Friday.txt'
##    fa='/home/az2/t7_test_list.txt'


    
##    fa=open('/home/az2/t7_monday.txt', 'r')
##    fa=open('/home/az2/t7_tuesday.txt', 'r')    
##    fa=open('/home/az2/t7_wednesday.txt', 'r')
##    fa=open('/home/az2/t7_thursday.txt', 'r')
##    fa=open('/home/az2/t7_Friday.txt', 'r')
    print('*********************************************************************************************')
    print("[Start] def Step1_read_tickers_from_file_and_align()")
    print("input file:",fa)
    print("output file: --> '/home/az2/t65.txt")
    print('*********************************************************************************************')

    
    f=open(fa,'r')    
    f3=open('/home/az2/t65.txt','w+')
    ticker=[]
    i=0
    k=0
    for x in f:
        i=i+1
##        print(i,'  ',x)
        if re.findall('-',x):
            
    ##        print('- found ',x)
            k=k+1
            ticker.append(x.split('-')[0].strip(' '))
##    print('ooooo [no dashes] k= ',k, ' in ',f)
##    print('ooooo [no dashes] i= ',i, 'lines in ',f)
    print('\n')
##    return (k)
##    f3.close()
    print('****************8 babu2 completed')
    f.close()


################################################
    
    f=open(fa,'r')
##        f=open('/home/az2/t7_tuesday.txt', 'r')

    i=0
    k3a=0


    f=open(fa,'r')
    print("777   ",fa)
##        f=open('/home/az2/t7.txt', 'r')
    f3=open('/home/az2/t65.txt','w')
    if k <  1:
        
        for x in f:
            
            i=i+1

            if "(" not in x:
                print('k < 1', x)
##                    print('data [added] to the file: --> ',x)                    
                k3a=k3a+1
                f3.write(str(x).rstrip('\n'))
##                f3.write(str(x).rstrip('\n')+str(' -').rstrip('\n'))
                f3.write('\n')

##        print('k2 / ', 'stupid removed ) tickers in t65.txt file = ',k2)
    print('k3a /', '55 No of companies to report earnings : ---> ', k3a)
    f.close()

    f=open(fa,'r')
##        f=open('/home/az2/t7_tuesday.txt', 'r')
    i=0
    k3b=0
    if k >  0:
        for x in f:
            print(x)
            if '(' not in x:
                
                k3b=k3b+1
                i=i+1
                print('data written [*withOUT*] dashes: -->',x)
                f3.write(str(x).rstrip('\n')+str(' -').rstrip('\n'))
                print('data written [*withOUT*] dashes: -->',x)
                f3.write(x)
    ##        f3.write(x.split('-')[0].strip(' '))
                f3.write('\n')
##        print('k3 / tickers in t65.txt file [no dashes added]= ',k3)
    print('k3b / 44  No of companies to report earnings : ---> ', k3b)
    print('tipu ', k3a)
    if k3b > k3a:
        k3=k3b
    if k3a > k3b:
        k3=k3a
    print('tipu33 ', k3)    
    
    f3.write('\n')
    f3.write('/home/az2/t7_tuesday.txt')
##    print('\n','output file ----> ','/home/az2/t65.txt')
    f3.close()
    f.close()
    print('*********************************************************************************************')
    print("[End] def Step1_read_tickers_from_file_and_align()")
    print("input file:",fa)
    print("output file: --> '/home/az2/t65.txt")
    print('*********************************************************************************************')
    return (k3,fa)

  




def Step2_yfinanceb_to_file():
    import time,os
    import streamlit as st
    st.legacy_caching.clear_cache()
    import yfinance as yf


    print('*********************************************************************************************')
    print("[Start] def Step3_file_to_output()")
    print('input file:---> /home/az2/t65.txt')
    print("output file: --> /home/az2/output45555.csv")
    print('*********************************************************************************************')
##    print("inside test - Earnings_backup22.py")
##    os.remove('/home/az2/t-215.txt')
##    os.remove('/home/az2/stageaarea.csv')

    import os.path
    file_exists = os.path.exists('/home/az2/output45555.csv')
    if file_exists==True:
        os.remove('/home/az2/output45555.csv')

    file_exists = os.path.exists('/home/az2/stageaarea.csv')
    if file_exists==True:
        os.remove('/home/az2/stageaarea.csv')
        
    
    readp='/home/az2/t65.txt'
##    readp='/home/az2/t__214.txt'
##    write_to='/home/az2/stageaarea.csv'
##    f3=open('/home/az2/t__214.txt','w')

##    f3.close()
    
    
    
    print('kkkkk')
    
##    print(df,'df info')

    v=0
    f=open(readp, 'r+')
    write_to='/home/az2/stageaarea.csv'
    f2=open(write_to,'w')
    i=0
    for x in f:
        p=x.split('-')[0]
        print(p)
        f2.write(p.rstrip())
        f2.write('\n')
        i=i+1
        if i==50 or i==100 or i==150 or i==200 or i==250:
            time.sleep(5)
            print("i=",i, "completed - sleeping for 5 seconds")
        v=v+1
        if v > 2:
            break
        print(i,') ',x)
    f2.close()


    no_of_tickersa=i
    print('no of tickers : ',no_of_tickersa)
    i=0
    mm=[]
    f2=open(write_to,'r')
    mm=[]
    for x in f2:
        mm.append(str(x).rstrip('\n'))
        
    print(mm, ' data from yfinance for each ticker')
    f2.close()


    bx=[]
    print('=== Running ===')
    s2=0
    for x in mm:
        print(s2,') ',x,'    ',s2,'    ','Remaining=',no_of_tickersa-s2)


        bx.append(yf.Ticker(str(x)).info)
        s2=s2+1
    print(bx)    
    df=pd.DataFrame(bx)

    print(df,'jjjjjjj')
    df.to_csv('/home/az2/output45555.csv')
    print('Output is located at: ',
          '/home/az2/output45555.csv')
##
    return df
##
    print('*********************************************************************************************')
    print("[End] Step2_yfinanceb_to_file")
    print('input file:---> /home/az2/t65.txt')
    print("output file: --> /home/az2/output45555.csv")
    print('*********************************************************************************************')
    

def Step3_file_to_output(t):
    import pandas as pd
    import os
##    t=pd.read_csv('/home/az2/output45555.csv', sep=';')
    print(t,'nnnnn')
    print('*********************************************************************************************')
    print("[Start] def Step3_file_to_output()")
    print('input file:---> /home/az2/output45555.csv')
    print("output file: --> /home/az2/sorted_by_highest_volume.csv")
    print('*********************************************************************************************')


    import os.path
    file_exists = os.path.exists('/home/az2/sorted_by_highest_volume.csv')
    if file_exists==True:
        os.remove('/home/az2/output45555.csv')

    file_exists = os.path.exists('/home/az2/sorted_by_highest_market_cap.csv')
    if file_exists==True:
        os.remove('/home/az2/sorted_by_highest_market_cap.csv')    

    file_exists = os.path.exists('/home/az2/sorted_by_next_earning_high_shortration_revenue_growth.csv')
    if file_exists==True:
        os.remove('/home/az2/sorted_by_next_earning_high_shortration_revenue_growth.csv')   

    file_exists = os.path.exists('/home/az2/sorted_by_recommendationKey_strong_buy.csv')
    if file_exists==True:
        os.remove('/home/az2/sorted_by_recommendationKey_strong_buy.csv') 
        
##    os.remove('/home/az2/sorted_by_highest_volume.csv')
##    os.remove('/home/az2/sorted_by_highest_market_cap.csv')
##    os.remove('/home/az2/sorted_by_next_earning_high_shortration_revenue_growth.csv')
##    os.remove('/home/az2/sorted_by_recommendationKey_strong_buy.csv')
##    os.remove('/home/az2/sorted_by_recommendationKey_strong_buy.csv')
##    os.remove('/home/az2/sorted_by_recommendationKey_strong_buy.csv')
##    
    i=0
    for x in t.columns:
        print(i,'  ',x,'  ')
        i=i+1


##        print('\n')
    print(t,' #2 unfiltered')    
##    t5=t.loc[t['sharesShortPriorMonth'] >= 21518860]
##    t.loc[t.recommendationKey.str.contains("foo", NaN)]
##    t.reset_index(inplace=True)
##    t.set_index('symbol',inplace=True)
    
    print(t.sort_values(by=['marketCap'],ascending=False),' #3 sorted by highest marketcap')
    t.to_csv('/home/az2/sorted_by_highest_market_cap.csv')
    
    print(t.sort_values(by=['volume'],ascending=False),'#4 sorted by volume')
    t.to_csv('/home/az2/sorted_by_highest_volume.csv')
##    t['gg']=''
##    t['gg']=t['forwardEps']-t['trailingEps']
##    t.to_csv('/home/az2/sorted_by_highest_eps_forward.csv',' #5 highest forward eps compared to trailing')
##    tv=t[['recommendationKey','forwardEps','trailingEps']].dropna()
##    t = t[t['recommendationKey'].notnull()]
    t5=t.loc[t['volume']> 800000]
    t5.to_csv('/home/az2/filtered_by_vol_greater_80000.csv','# 6vol > 80000')         
    t6=t5.loc[t5['recommendationKey'].str.startswith('st')]
    t6.to_csv('/home/az2/filtered_by_vol_greater_80000_and_recomendation_key_strong_buy.csv','# strong buy + avg_10_day_val > 80000')         
    t6b=t6.sort_values(by=['gg','shortRatio','revenueGrowth'],ascending=False)
             
    t6b.to_csv('/home/az2/sorted_by_next_earning_high_shortration_revenue_growth.csv')
    
    print(t6,'filtered','sorted by strong buyy, high volume')
    print(t6[['symbol','shortName','gg','grossProfits','recommendationKey','totalCash','totalDebt','totalRevenue','grossProfits','regularMarketVolume']],' sorted by high expected eps')
    t6.to_csv('/home/az2/sorted_by_recommendationKey_strong_buy.csv')


Step1_read_tickers_from_file_and_align()
p=Step2_yfinanceb_to_file()
print(p,'kkkkk')
Step3_file_to_output(str(p))
