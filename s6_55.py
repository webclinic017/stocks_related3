import datetime
from dateutil import parser
import sys
import time
import os
import plotly.graph_objects as go
import yfinance as yf
import pandas as pd
import datetime as dt
import talib as ta
import finta as f
import inspect
from inspect import currentframe, getframeinfo
import numpy as np
import sys,trace
import warnings
import sys
from datetime import date
import datetime
from datetime import timedelta
import random
from dateutil import parser


 
pd.options.display.float_format = '{:.2f}'.format
pd.options.display.max_columns = 255
pd.options.display.max_rows = 6500000

pd.options.display.max_rows = 9999
pd.options.display.max_columns = 76
pd.set_option("display.max_columns", 200)
pd.set_option('display.width', 1000)
pd.set_option('display.expand_frame_repr', False)

gg5 = []


warnings.filterwarnings("ignore")

pd.options.display.float_format = '{:.2f}'.format
pd.options.display.max_columns = 255
pd.options.display.max_rows = 6500000

pd.options.display.max_rows = 9999
pd.options.display.max_columns = 36
pd.set_option("display.max_columns", 100)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 200)
pd.set_option('display.max_columns', 0)
pd.set_option('display.max_columns', None)





def s6(df,u33,df7a):
##def cc(df,test,gt4,x,df9,ss):
    import time
    import matplotlib.pyplot as plt 
    import pandas as pd
    import sys
    from datetime import date
    from dateutil import parser
    ##print('-------------------start of [s6] module-----------------------------')

##
##    ##print(df,'88')

    
##    print('\n\n\n\n')
##    print('********************** summary Data frame df 7 **********************************')
##    print(df7,'df7')
##    print('********************** summary Data frame df 7 **********************************')
##    sys.exit()
    pd.options.display.float_format = '{:.2f}'.format
    pd.options.display.max_columns = 255
    pd.options.display.max_rows = 6500000

    ##pd.options.display.max_rows = 999999
    pd.options.display.max_columns = 76
    pd.set_option("display.max_columns", 200)
    pd.set_option('display.width', 1000)
    pd.set_option('display.expand_frame_repr', False)


    pd.options.display.float_format = '{:.2f}'.format
    pd.options.display.max_columns = 255
    pd.options.display.max_rows = 6500000

    ##pd.options.display.max_rows =999999 
    ##pd.options.display.max_columns = 36
    pd.set_option("display.max_columns", 100)
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_colwidth', 200)
    pd.set_option('display.max_columns', 0)
    pd.set_option('display.max_columns', None)
    pd.set_option("expand_frame_repr", True)

    df_short = pd.DataFrame()
    df4 = pd.DataFrame()
    df5 = pd.DataFrame()
    # df3=df
    g6 = pd.DataFrame()
    g7 = pd.DataFrame()

    # SAR reversal
##    df.reset_index(inplace=True)
    m2 = []
    m3 = []
    m4 = []
    t5=0
    t6=0

    p44=[]
    p45=[]
    i2='53'
    df['i2']=''
    df['i2a']=''





##    print(df,'from s4.py  55 kkkkkk')
##    print(test,'========== inside s6 ============')
# print(df.index,'ddddddddddddddddddd')

########################## buy condition ######################################
# print(df.index,'kkkkkkkkkkkkkkkkkkkkkkkkkkk')

    u=0
    g43=0;g44=0;g45=' ';g46=0.0;g47=0.0
    s43=0;s44=0;s45=' ';s46=0.0;s47=0.0
    v5_buy=0.0
    v6=0.0
    buy_signal_counter=0
    buy_signal_counter_sig=0


##    df.set_index(df['counter'],inplace=True)
##    print(df,'888')
##    print(df.index,'jj')
##    df.reset_index(inplace=True,drop=True)
##    print('\n\n')
##    print(df.index,'jj22-------------------------')
##    df.set_index([s3,s2],inplace=True)
##    print(df.index,'jj22-------------------------')
##    print('\n\n')
##    df['i']=df.index
    df.reset_index(inplace=True,drop=True)
    df.set_index(df['i'],inplace=True)
##    print(df)


    #print(df,'4444444444444444444444444444444444444444444444444444444444444444444444444444444444444')
    
##    df.set_index(df['Datetime'])
    k57=0
##    print(df,'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')



    ##print('babu khan ', df,df.shape)
#################################################################################################
##    print('\n\n\n')
    
    dfm=df.loc[(df['s2'] > '09:00') & (df['s2'] < '16:01')]
    df=dfm
    ##print('\n\n\n')
    ##print('babu khan2 ', df,df.shape)
##    sys.exit()
#################################################################################################

##########################################################################################################    
##    print(df,'nn ',u33)
    ############### buy conditinon loop ##################
    for z in df.index:
        buy_signal_counter=buy_signal_counter+1
##        print(z,'azhar 2')
        u=u+1
        t5=t5+1
        k57=k57+1
        df['i2'].loc[z]=i2



##        buy_condition = df['macd'].loc[z] > 0 and df['macd'].shift(1).loc[z] < 0

        buy_condition = df['Close_vwap'].loc[z] < 0 and (df['Close_vwap'].shift(1).loc[z] < 0) and (df['Close_vwap'].shift(2).loc[z] < 0)\
                and df['macd'].loc[z] > 0 and df['EMA-510'].loc[z] < 0



##        buy_condition = df['macd'].loc[z] > 0 and df['macd'].shift(1).loc[z] < 0 and df['macd'].shift(2).loc[z] < 0\
##                        and df['aroonup'].loc[z].round(1) > 85 

         

##        buy_condition = df['MOM'].loc[z] - df['MOM'].shift(1).loc[z] > 0 and\
##                        df['macd'].loc[z] > 0 and df['adx'].loc[z] > 24 and df['ATR'].loc[z] > .9 and df['TR'].loc[z] > .5

##        buy_condition = df['MOM'].loc[z] - df['MOM'].shift(1).loc[z] 
####################################################################################################################################
        '''
        if buy_condition == True:
            print('-------------------------------------------------------------------------------------------------------------------------------')
            print('index->', z,'  ',buy_condition,' tkr-> ',df['ticker'].loc[z],' macd-> ',df['macd'].loc[z].round(3),' adx-> ',df['adx'].loc[z].round(3),
              ' MOM-> ',df['MOM'].loc[z].round(1),' ATR->',df['ATR'].loc[z].round(1),' Close_vwap->',df['Close_vwap'].loc[z].round(1),' sqz_on->',\
                  df['squeeze_on'].loc[z],' aroonup->',df['aroonup'].loc[z].round(1),' CCI->',df['CCI'].loc[z].round(1),
                  '----------------------------------------------------------->')
            print('-------------------------------------------------------------------------------------------------------------------------------')
##            print(' Close_vwap->',df['Close_vwap'].loc[z].round(1),' squeeze_on->',
##                  df['squeeze_on'].loc[z],' aroonup->',df['aroonup'].loc[z].round(1),' CCI->',df['CCI'].loc[z].round(1),'EMA-35->',
##                  df['EMA-35'].loc[z].round(1),' EMA_5_vwap->',df['EMA_5_vwap'].loc[z].round(1),'EMA_50_vwap->',df['EMA_5_vwap'].loc[z].round(1),' ------------>')

        elif df['macd'].loc[z] > 0:
            print('-------------------------------------------------------------------------------------------------------------------------------')
            print('index->', z,'  ',buy_condition,' tkr-> ',df['ticker'].loc[z],' macd-> ',df['macd'].loc[z].round(3),' adx-> ',df['adx'].loc[z].round(3),
              ' MOM-> ',df['MOM'].loc[z].round(1),' ATR->',df['ATR'].loc[z].round(1),' Close_vwap->',df['Close_vwap'].loc[z].round(1),' sqz_on->',\
                  df['squeeze_on'].loc[z],' aroonup->',df['aroonup'].loc[z].round(1),' CCI->',df['CCI'].loc[z].round(1),
                  '----------------------------------------------------------->')

##            print('-------------------------------------------------------------------------------------------------------------------------------')
##            print(' Close_vwap->',df['Close_vwap'].loc[z].round(1),' squeeze_on->',
##                  df['squeeze_on'].loc[z],' aroonup->',df['aroonup'].loc[z].round(1),' CCI->',df['CCI'].loc[z].round(1),'EMA-35->',
##                  df['EMA-35'].loc[z].round(1),' EMA_5_vwap->',df['EMA_5_vwap'].loc[z].round(1),'EMA_50_vwap->',df['EMA_5_vwap'].loc[z].round(1),' ------------>')

        else:
            print('index->', z,' **** ',buy_condition,'**** tkr-> ',df['ticker'].loc[z],' macd-> ',df['macd'].loc[z].round(1),' adx-> ',df['adx'].loc[z].round(3),
              ' MOM-> ',df['MOM'].loc[z].round(1),' ATR->',df['ATR'].loc[z].round(1),' Close_vwap->',df['Close_vwap'].loc[z].round(1),' sqz_on->',\
                  df['squeeze_on'].loc[z],' aroonup->',df['aroonup'].loc[z].round(1),' CCI->',df['CCI'].loc[z].round(1))
##            print(' Close_vwap->',df['Close_vwap'].loc[z].round(1),' squeeze_on->',
##                  df['squeeze_on'].loc[z],' aroonup->',df['aroonup'].loc[z].round(1),' CCI->',df['CCI'].loc[z].round(1),'EMA-35->',
##                  df['EMA-35'].loc[z].round(1),' EMA_5_vwap->',df['EMA_5_vwap'].loc[z].round(1),'EMA_50_vwap->',df['EMA_5_vwap'].loc[z].round(1))
        '''
####################################################################################################################################            

        if buy_condition:
##        if buy_condition and i2=='53':
            i2 = '51'

            df['signal'].loc[z] = "Buy_signal"



            b_Close_vwap=df['Close_vwap'].loc[z]
            b_macd=df['macd'].loc[z]
            b_mom=df['MOM'].loc[z]
            b_VZO=df['VZO'].loc[z]
            b_CCI=df['CCI'].loc[z]

            b48=b_Close_vwap
            b47=b_macd
            b46=b_mom
            b49=b_VZO
            b50=b_CCI
            

##            =================================================== >>>>>
##            df['signal'].loc[z] = 55
            
            v5_buy = df['Close'].loc[z]  # v5_buy is buy
            v6 = df['CCI'].loc[z]
            t_buy = df['Datetime'].loc[z]

            v8 = df['ticker'].loc[z]
##            print(z,'  z vs u        ',u)
            g43 = z
            g44=df['Datetime'].loc[z]
            g45=df['ticker'].loc[z]
            g46=df['MOM'].loc[z]
            g47=df['macd'].loc[z]
            buy_signal_counter_sig==buy_signal_counter
            break
            
##########################################################################
######################## SELL CONDITION ##################################
##    print('g43=',g43,' 00000000000000000000000000000000000000000000000000000000000')
    i = 0
    mm3 = 'MOM'
    t6=0
##    print('\n')
    
##    print(g43,'   ',g44,'  ',df['ticker'][-1],'----------- buy signal received here --------------')
##    print(u33,'  Buy ',g43,'   at time: ',g44,'  ticker= ',g45,' MOM=',g46,'  MACD=',g47,' ----------- buy signal received here --------------')
##    print('\n')
##    print(u33,'  index Buy ',g43,'  buy=',v5_buy,'   at time: ',g44,'  ticker= ',g45,' MOM=',g46,'  MACD=',g47,' ----------- buy signal received here --------------')
    

    sell_signal_counter=0
    sell_signal_counter_sig=0

    df.dropna(subset=[mm3], how='all', inplace=True)
    ##print(df,df.shape,'8887')

  ###############  conditinon loop ##################

    b88='***'
    if v5_buy == 0:
        
        
        s5d={'stragety':'2','Date':str(u33),'ticker':str(g45),'Buy_at':str('0'),'Sell_at':str('0'),'Profit':''
##             'b_Time':g44,'s_Time':s44,\
##             'b_Close_vwap':'dummy','b_macd':'dummy','b_mom':'dummy','b_VZO':'dummy','b_CCI':'dummy',\
##             'b_break':'***',\
##             's_Close_vwap':'dummy','s_macd':'dummy','s_mom':'dummy','s_VZO':'dummy','s_CCI':'dummy'
             }
        print(s5d)
##        df7a=df7a.append(pd.DataFrame(s5d),index=[0])
    

############################################# Sell algoritham ####################################

    if v5_buy != 0:
        
        
        for z in range(g43, df.index[-1]):
    ##    for z in range(g43, df.index[-1]):
            sell_signal_counter=sell_signal_counter+1
    ##        print(g43,'------------------',df.index[-1])       
            t6=t6+1
            
            sell_condition = df['macd'].loc[z] < 0
##            and df['macd'].shift(1).loc[z] > 0
    ##        print(df['macd'].loc[z] < 0 and df['macd'].shift(1).loc[z] > 0,'  oooooooooooooooooooooooooooooo')
    ##        sell_condition = df['macd'].loc[z] < 0 and df['macd'].shift(1).loc[z] > 0


            
            
    ##        sell_condition = (df[mm3].loc[z] < 0 and (df[mm3].loc[z] - df[mm3].shift(1).loc[z] < 00) and df['Close'].loc[z] > v5_buy)
##            if sell_condition and i2=='51' and g43 != None:
            if sell_condition:
                
                sell_signal_counter_sig==sell_signal_counter
                



                s_Close_vwap=df['Close_vwap'].loc[z]
                s_macd=df['macd'].loc[z]
                s_mom=df['MOM'].loc[z]
                s_VZO=df['VZO'].loc[z]
                s_CCI=df['CCI'].loc[z]


    ##        sell_condition = (df['Close'].loc[z] > v5_buy) and df['macd'].loc[z] < 0
    ##        print(df['macd'].loc[z])
    ##        sell_condition = df['macd'].loc[z] 
            
    ##        sell_condition = df['Close'].loc[z] - df['Close'].shift(1).loc[z] < (.5) or df['Close'].loc[z] < v5_buy-.1 
    ##                         (df['Close'].loc[z] < 0 and df['Close'].shift(1).loc[z] < 0 and df['Close'].shift(2).loc[z] < 0\
    ##                             and df['Close'].shift(3).loc[z] < 0)
            
    ##        sell_condition = (df[mm3].loc[z] < 0 and (df[mm3].loc[z] - df[mm3].shift(1).loc[z] < 00) and df['Close'].loc[z] > v5_buy)
    ##        if float(df['macd'].loc[z])  < float(0):  
    ####        if sell_condition and i2=='51' and g43 != None:
    ##            sell_signal_counter_sig==sell_signal_counter
    ##            print('buy price: ',v5_buy, ' exit price=',v5_buy-.25)
                
                df['i2a'].loc[z]=i2
                i2='53'
                ##                        print(' sell cond')

                ##                    sell_condition=df[mm3].loc[z] < 0
                
                df['signal'].loc[z] = "Sell_signal"
                

                
                t_sell = df['Datetime'].loc[z]
                v4_sell = df['Close'].loc[z]
                v7 = df['ticker'].loc[z]
    ##                        print(v7,'  ',v4_sell,'/',v5_buy,'  ',v4_sell-v5_buy,'  ',t_sell,'/',t_buy)
                xm = v7
                x2 = v5_buy
                x3 = v4_sell
                x5 = v6
                x4 = v4_sell - v5_buy

##                g6 = g6.append([[xm, v5_buy, v4_sell, x4, v7, t_buy, t_sell]])

                i = i + 1

                s43 = z
                s44=df['Datetime'].loc[z]
                s45=df['ticker'].loc[z]
                s46=df['MOM'].loc[z]
                s47=df['macd'].loc[z]
                s48=df['Close_vwap'].loc[z]
                s49=df['VZO'].loc[z]
                s50=df['CCI'].loc[z]
                s51=df['RSI'].loc[z]

            else:
                if z==df.index[-1]:
                    
                    ##print('No Sell')
                    pass

               

    ##                    print('============= Bought but sell condition not met during the day/Loss ===================')
    ##    print(s43,'   at time:  ticker= '' ----------- [sell] signal received here --------------')
    ##    print(u33,'  Sell ',s43,'   at time: ',s44,'  ticker= ',s45,' MOM=',s46,'  MACD=',s47,' ----------- [sell] signal received here --------------')
##        print(u33,'  index Sell ',s43,'  buy=',v4_sell,'   at time: ',s44,'  ticker= ',s45,' MOM=',s46,'  MACD=',s47,' ----------- [sell] signal received here --------------')
        
    ##    print(u33,'  index Buy ',g43,'  buy=',v5_buy,'   at time: ',g44,'  ticker= ',g45,' MOM=',g46,'  MACD=',g47,' ----------- buy signal received here --------------')
        
##        print('\n')
##        if v4_sell-v5_buy > 0:
##            print('================= Profit=',round((v4_sell-v5_buy),2))
##        else:
##            print('================= Loss=',round((v4_sell-v5_buy),2))
##        print('\n')

##        print('\n\n\n\n\n')
    ##    print('Close market: ',df['Close'].loc['c2'],'/',df['Close'].loc['c3'],'  ')
##        g6.drop_duplicates(subset=None, keep='last', inplace=True)
        

##        s5d={'f2':'34','f3':'55'}
        n='0'
        n3='0'
        print('\n\n')
        print('here i am')
##        print(v5_buy,'v5_buy -----------------------------------------')
        if v5_buy != 0 and v4_sell != 0:
            print(u33,'  ','v5_buy != 0 and v4_sell != 0:')
            s5d={'stragety':'2','Date':str(u33),'ticker':g45,'Buy_at':v4_sell,'Sell_at':v5_buy,'Profit':v5_buy-v4_sell\
##             'b_Time':g44,'s_Time':s44,\
##             'b_Close_vwap':b48,'b_macd':b47,'b_mom':b46,'b_VZO':b49,'b_CCI':b50,
##             'b_break':'***',\
##             's_Close_vwap':s48,'s_macd':s47,'s_mom':s46,'s_VZO':s49,'s_CCI':s50
                 }


            
            df7a=df7a.append(s5d,ignore_index=True)

        if v5_buy != 0 and v4_sell == 0:
            print(u33,'  ','v5_buy != 0 and v4_sell == 0:')
            s5d={'stragety':'3','Date':str(u33),'ticker':g45,'Buy_at':v5_buy,'Sell_at':v4_sell,'Profit':v5_buy-v4_sell\
##             'b_Time':g44,'s_Time':s44,\
##             'b_Close_vwap':b48,'b_macd':b47,'b_mom':b46,'b_VZO':b49,'b_CCI':b50,
##             'b_break':'***',\
##             's_Close_vwap':s48,'s_macd':s47,'s_mom':s46,'s_VZO':s49,'s_CCI':s50
                 }


            
##            df7a=df7a.append(s5d,ignore_index=True)   

        if v5_buy == 0 and v4_sell == 0:
            print(u33,'  ','v5_buy == 0 and v4_sell == 0:')
            
##        if v4_sell==0:
##            v5_buy=0

##            df7a = pd.DataFrame({'stragety':'3','Date':str(u33),'ticker':s45,'Buy_at':n,'Sell_at':n3,'Profit':0,\
##                                 'b_Time':' ','s_Time':' ',\
##                                 'b_Close_vwap':'dummy','b_macd':'dummy','b_mom':'dummy','b_VZO':'dummy','b_CCI':'dummy',\
##                                 'b_break':'***',\
##                                 's_Close_vwap':s48,'s_macd':s47,'s_mom':s46,'s_VZO':s49,'s_CCI':s50})


            s5d=({'stragety':'4','Date':str(u33),'ticker':s45,'Buy_at':'90','Sell_at':'90','Profit':0\
##                                 'b_Time':' ','s_Time':' ',\
##                                 'b_Close_vwap':'dummy','b_macd':'dummy','b_mom':'dummy','b_VZO':'dummy','b_CCI':'dummy',\
##                                 'b_break':'***',\
##                                 's_Close_vwap':s48,'s_macd':s47,'s_mom':s46,'s_VZO':s49,'s_CCI':s50
                  })


            
##            df7a=df7a.append(s5d,ignore_index=True)   
                                 
                                 
        if v5_buy == 0 and v4_sell != 0:
            print(u33,'  ','v5_buy == 0 and v4_sell != 0:')
##            df7a = pd.DataFrame({'stragety':'5','Date':str(u33),'ticker':s45,'Buy_at':n,'Sell_at':n3,'Profit':0,\
##                                 'b_Time':' ','s_Time':' ',\
##                                 'b_Close_vwap':'dummy','b_macd':'dummy','b_mom':'dummy','b_VZO':'dummy','b_CCI':'dummy',\
##                                 'b_break':'***',\
##                                 's_Close_vwap':s48,'s_macd':s47,'s_mom':s46,'s_VZO':s49,'s_CCI':s50})
##

            s5d={'stragety':'5','Date':str(u33),'ticker':g45,'Buy_at':v4_sell,'Sell_at':v5_buy,'Profit':v5_buy-v4_sell\
                 
##             'b_Time':g44,'s_Time':s44,\
##             'b_Close_vwap':b48,'b_macd':b47,'b_mom':b46,'b_VZO':b49,'b_CCI':b50,
##             'b_break':'***',\
##             's_Close_vwap':s48,'s_macd':s47,'s_mom':s46,'s_VZO':s49,'s_CCI':s50
                 }


            
##            df7a=df7a.append(s5d,ignore_index=True)   
##################################################################
##        if v5_buy == 0:
##        if df7a.empty==True:    
##            s6d={'stragety':'-1','Date':str(u33),'ticker':s45,'Buy_at':'50','Sell_at':'50','Profit':0,\
##             'b_Close_vwap':'55','b_macd':'dummy','b_mom':'dummy','b_VZO':'dummy','b_CCI':'dummy'}
##            df7a=df7a.append(s6d,ignore_index=True)
##            print(df7a,' =========================================================bbbbbbbbbbbbbbbbb')

##            b_Close_vwap=df['Close_vwap'].loc[z]
##            b_macd=df['macd'].loc[z]
##            b_mom=df['MOM'].loc[z]
##            b_VZO=df['VZO'].loc[z]
##            b_CCI=df['CCI'].loc[z]        



###################################################################

##        if v4_sell==0:
##            v5_buy==0
##            s45==df['ticker'][2]
            
            

##        df7a=df7a.append(s5d,ignore_index=True)

##        print(df7,'--------------- gg55')
        


        ####print(df.shape,'sin34') 
##        if s44 != 0:
##            
##            print(u33,'    45      ','df','      ','g45','  buy sell-signal  ','\n')
##
##                  
##        if s44==0:
##            print(u33,'    46      ','df','      ','s45','  buy sell-signal  ==== [no sell] ====','\n')
##
##        
        
##        print(u33,' -------------------end of [s6] module-----------------------------')
        
        ####print(df.shape,'sin36')

##    x    return(df7,df5)
##    return(df,df7a)


       
        df7a=df7a[['Profit','Buy_at',
                        'Sell_at',
                        'Date']]
##        print(df7a[['Profit','Buy_at',
##                        'Sell_at',
##                        'Date']],'df7a-44')
        return(df7a)

def main(dfb):
    import pandas as pd
    import time
    import datetime as dt
    from datetime import datetime
    from datetime import date
    import datetime
    from dateutil import parser
    import datetime
    from datetime import timedelta
    import sys
    df=pd.read_csv('/home/az2/557/df_input.csv')
##    for x in df.index:
##        df['s3']=str(df['s3']).split('\n')
##        print(df['s3'])

    df['s3']=str(df['s3']).split('\')   
    print(df['s3'].head())
    sys.exit()

    print(df,'df')
    print('\n')
    i=0
    for x in df.columns:
        print(i,'   ',x)
        i=i+1
    print('\n')
    
    gg=df['s3'].unique()
    print(gg,' unique dates')
    pp=[]
    for x in gg:
        if type(x)==str:
            s=x.split('\n')[1]
##            pp=pp.append(s)
            pp.append(s)
    print('\n\n\n')
    print(pp)
###########################################
    '''   
    todays_date = dt.date.today 
    print(todays_date(),"-- Today's Date --")
    
    g=pd.date_range('2022-02-10', todays_date(),freq=pd.offsets.BDay())

    print(g,"-- Date array --")
    print('Script is going to check # of days = ',len(g))
    k=0

    pp=[]
    for x in g:
        p2b=x
             
        px=pd.Series(p2b)
        px=pd.to_datetime(px)
        p2c=px.dt.day_name()
        global p2d
        p2d=str(p2c).split(' ')[4]

        p2b=str(p2b)
        p=d3=datetime.datetime.date(parser.parse(p2b))+datetime.timedelta(days=1)
        d2=str(p)
        pdate=p
        d3=datetime.datetime.date(parser.parse(d2))-datetime.timedelta(days=1)
        pp.append(d2)
##        print(d2)
    
    print(pp,'  pp')
    '''

    ##############################################################################

##    for x in gg:
##        print(x)
##        df=df[df['s2']==x]
##        print(df,'     ','\n',x,' ----------------------------------------')

    import sys
##    sys.exit()

        

    
    
    for x in pp:
        df7a=s6(df,x,df7a)
        print(df7a,' bbb')



dfb=pd.DataFrame()
dfb=pd.DataFrame(columns=['stragety','Date','ticker','Buy_at','Sell_at','Profit'
##             'b_Time','s_Time',\
##             'b_Close_vwap','b_macd','b_mom','b_VZO','b_CCI',
##             'b_break',\
##             's_Close_vwap','s_macd','s_mom','s_VZO','s_CCI'
                           ], index=[0])
main(dfb)    
