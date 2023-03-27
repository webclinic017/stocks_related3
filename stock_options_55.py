from yahoo_fin import options 
import pandas as pd
from yahoo_fin import stock_info as f
import textwrap 
#pd.set_option("max_colwidth", 12)
from yahoo_fin import news as g
import html5lib
import numpy as np 
from numerize import numerize 
import sys
import datetime
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


ticker='t'
#ticker='spx'



pd.options.display.max_columns = 50
pd.options.display.max_rows = 1000
 #pd.options.display.max_colwidth =180
pd.set_option('display.max_colwidth', 16)
pd.set_option("display.expand_frame_repr", False)

#############################################################################################################
##nflx_dates = options.get_expiration_dates(ticker)
##chain = options.get_options_chain(ticker)
#####################################################
##print(nflx_dates)
##print(chain)



##uu=chain['calls']
##
##uu = uu.replace('-', '0')
##
##mm=0
##for x in uu.index:
##    mm=mm+int(uu['Volume'].loc[x])
##
##print(ticker,' calls ----> ',mm)
####################################################
##uu=chain['puts']
##
##uu = uu.replace('-', '0')
##
##mm=0
##for x in uu.index:
##    mm=mm+int(uu['Volume'].loc[x])
##        #    print(uu['Volume'].loc[x])
##
##print(ticker,' puts --- > ',mm)
######################################################
##print('stupid azhr','\n\n')
###print(type(uu['Last Trade Date']))
###ff=str(uu['Last Trade Date']).split('-')[0]
###print(ff)
##
##print('uu type --- > ',type(uu))
##
##u1=pd.DataFrame()
##
##print('mm=    ',mm, '    ', type(mm))
##
##for x in uu.index:
##    u1=u1.append(
##    u1.loc[x]=u1.loc[x].append(uu['Volume'].loc[x])
#    print(x)

#print('uu ' ,type(uu))
#print('u1 ',type(u1),u1)

