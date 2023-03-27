
import pandas as pd
##import talib as taa
####import finta as f
##from finta import TA 
##import pandas_ta as ta
##from numerize import numerize
import yfinance as yf
import pandas_ta as ta
import sys

import os
p=os.system('ls -ltr').read()
print(p)
sys.exit()


f=open('/home/az2/Downloads/May2_list.txt','r')
g=open('/home/az2/Downloads/May2_list_out.txt','w')
friday29=[]
print('Step 1 - Reading from text file and storing them to an array')
for x in f:
    if '(' not in x:
        print(x)
        friday29.append(x)

print(len(friday29),' tickers reporting earnings today')
if len(friday29) > 0:
      print('Step 2 - Reading from array and pulling info')
for p in friday29:
##    df=yf.download(x, period=perda, interval=intervla,prepost = False)
##    print('\n')
##    print('--------------------------------------------------')
##    print('**************** Analyst recommendations ',p,'*******************')
##    print('--------------------------------------------------')
    g.write('Analyst recommendations')
    g.write(str(p))
    g.write(' **********************************')
    g.write('\n')
    try:
        g.write('recommendationKey --> ')
        g.write(str(yf.Ticker(str(p)).get_info()['recommendationKey']))
        g.write('\n')
        g.write('numberOfAnalystOpinions --> ')
        g.write(str(yf.Ticker(str(p)).get_info()['numberOfAnalystOpinions']))
        g.write('\n')
        g.write('totalCashPerShare-->')
        g.write(str(yf.Ticker(str(p)).get_info()['totalCashPerShare']))
        g.write('\n')
        g.write('heldPercentInstitutions-->')
        g.write(str(yf.Ticker(str(p)).get_info()['heldPercentInstitutions']))
        g.write('\n')
        g.write('\n')
##        print('recommendationKey --> ',yf.Ticker(str(p)).get_info()['recommendationKey'])
##        print('numberOfAnalystOpinions --> ',yf.Ticker(str(p)).get_info()['numberOfAnalystOpinions'])
##        print('totalCashPerShare-->',yf.Ticker(str(p)).get_info()['totalCashPerShare'])
##        print('heldPercentInstitutions-->',yf.Ticker(str(p)).get_info()['heldPercentInstitutions'])
##
##        print('\n\n')
##        print(yf.Ticker(str(p)).get_recommendations().tail(5))
    except AttributeError: pass # expected
f.close()
g.close()
print('completed')
