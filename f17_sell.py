def inputs2(df,z,buy_price_gg,xs):
    import f16_condt
    from f16_condt import con_sell_down
    sell_status='no'

##    print('888888')
    sell_condition=con_sell_down(df,z,xs) 
    
    
##    sell_condition=(df['ADL'].loc[z] > 0) or df['Close'].loc[z] > df['Close'].loc[z]-df['Close'].shift(1).loc[z]*.1



##    fg.write(sell_condition)
##    trailing_stop=df['Close'].loc[z] < df['Close'].loc[z]-df['Close'].shift(1).loc[z]*.1
    
    return(sell_condition,sell_status)
##sell_price_gg = 0
##print('buy is satisfied')
##print(buy_price_gg)


def f17_sellp(xs,b6,df,buy_price_gg,buy_status,gft,gft2):
##def f17_sellp(xs,b6,df,buy_price_gg,buy_status):
    import sys
    sell_status='no'
    df['sell']=''
##    print('\n')
##    print('start [f17_sell.py]')
##    print('\n')
##    print("jjjj55555    ",buy_price_gg)
##    sys.exit()
##    print('========= 888888')    
    ############# Sell condition for uptrend ########################
    sell_price_gg=0
    for z in range(b6,df.shape[0],1):
        
        
    ##        if df['Close'].loc[z] - buy_price_gg > 0:

    ##        if (df['Close'].loc[b6] < df['Close'].loc[z]  or df['Close'].loc[z]<df['vwap'].loc[z]  or\
    ##               df['ADL'].loc[z] < 0) or (df['MOM'].loc[z] < df['MOM'].shift(1).loc[z] and df['MOM'].shift(1).loc[z]< df['MOM'].shift(2).loc[z]):

        sell_condition,sell_status=inputs2(df,z,buy_price_gg,xs)        
        if  sell_condition == True:
            sell_status='yes'
##            print(sell_condition,' ------------------------------------------------------ 888 ')
            
            
    ##        if df['Close'].loc[z] - buy_price_gg > 0 or (df['ADL'].loc[x] < 0) and df['macd'].loc[z] < 0 or \
    ##           (df['EMA-35'].loc[z] < 0 and df['EMA-510'].loc[z] < 0)  or\
    ##           (df['EMA-1021'].loc[z] < 0) :
            
    ##(df['macd'].loc[z] < 0) or (df['Close_vwap'].loc[z] < 0) or (df['Close_vwap'].shift(1).loc[z] < 0\
    ##           or df['EMA-2150'].loc[z] < 0)\
    ##
    ##           
            sell_price_gg=df['Close'].loc[z]
            df['sell'].loc[z]='sell'
            sell_status = 'yes'
            
            s7=z
##            print('555555')
##            print(xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status)
            
            return(xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status,gft,gft2)
            break

        elif sell_condition==False and df.shape[0]-1==z:
            sell_price_gg=-1
            sell_status = 'no'
            
            s7=z
##            print('mmmm')
##            print('\n')
##            print('end [f17_sell.py]')
##            print('\n')
            return(xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status,gft,gft2)
##    print(sell_price_gg,'-------------------------- sell_Put_price_gg')
##    print(buy_price_gg,'-------------------------- buy_Put_price_gg')
##    print(xs,' profit=',(sell_price_gg-buy_price_gg))
   

        ##            df['Boling_lower'].loc[x]
        ##
        ##            if df['Boling_upper'].loc[z] < df['Close'].loc[z] < df['Boling_middle'].loc[z]:
        ##                df['bolinger'].loc[z]='bolinger_upper < close < bolinger_middle'
        ##                df['bolinger_n'].loc[z]=str(round(df['Boling_upper'].loc[z],2))+ str(' < ') + str(round(df['Close'].loc[z],2)) + str(' < ') +  str(round(df['Bolinger_middle'].loc[z],2)) 
        ##            if df['Close'].loc[z]  > df['Boling_upper'].loc[z]:
        ##                df['bolinger'].loc[z]='close > bolinger_upper'
        ##                df['bolinger_n'].loc[z]=str(round(df['Close'].loc[z],2)) + str(' > ') + str(round(df['Boling_upper'].loc[z],2))
        ##                
        ##            if df['Close'].loc[z]  < df['Boling_lower'].loc[z]:
        ##                df['bolinger'].loc[z]='close < bolinger_lower'
        ##                df['bolinger_n'].loc[z]= str(round(df['Close'].loc[z],2)) + str(' < ')+ str(round(df['Boling_lower'].loc[z],2))
        ##            if df['Boling_middle'].loc[z] < df['Close'].loc[z] < df['Boling_lower'].loc[z]:
        ##                df['bolinger'].loc[z]='Boling_middle < close < bolinger_lower'
        ##                df['bolinger_n'].loc[z]=str(round(df['Boling_middle'].loc[z],2))+str(' < ') + str(round(df['Close'].loc[z],2))+ str('< ')+ str(round(df['Boling_lower'].loc[z],2)) 
        ##
##            df['bolinger'].loc[z]=str(df['Boling_middle'].loc[z])+str('/')+str(df['Boling_lower'].loc[z])\
##                                   +str('/')+str(df['Boling_upper'].loc[z])
                                       

    ##            if df['Boling_middle'].loc[z] <= df['Close'].loc[z] <= df['Boling_upper'].loc[z]:
    ##                df['bolinger'].loc[z]='bolinger_middle < close < bolinger_upper'
    ##                
    ##                df['bolinger_n'].loc[z]=str(round(df['Boling_middle'].loc[z],2))+ str(' < ') + str(round(df['Close'].loc[z],2)) + str(' < ') +  str(round(df['Boling_upper'].loc[z],2)) 
    ##
    ##            if df['Close'].loc[z]  > df['Boling_upper'].loc[z]:
    ##                df['bolinger'].loc[z]='close > bolinger_upper'
    ##                df['bolinger_n'].loc[z]=str(round(df['Close'].loc[z],2)) + str(' > ') + str(round(df['Boling_upper'].loc[z],2))
    ##                
    ##            if df['Close'].loc[z]  < df['Boling_lower'].loc[z]:
    ##                df['bolinger'].loc[z]='close < bolinger_lower'
    ##                df['bolinger_n'].loc[z]= str(round(df['Close'].loc[z],2)) + str(' < ')+ str(round(df['Boling_lower'].loc[z],2))
    ##                
    ##            if df['Boling_lower'].loc[z]  <= df['Close'].loc[z] <= df['Boling_middle'].loc[z]:
    ##                df['bolinger'].loc[z]='Boling_lower < close < bolinger_middle'
    ##                df['bolinger_n'].loc[z]=str(round(df['Boling_lower'].loc[z],2))+str(' < ') + str(round(df['Close'].loc[z],2))+ str('< ')+ str(round(df['Boling_middle'].loc[z],2)) 


        ##            df['Boling_upper'], df['Boling_middle'], df['Boling_lower']



        ##            if  df['Boling_upper'].loc[z] > 0:
        ##                df['Boling_upper'].loc[z]



                
##                break
##        if  buy_price_gg == 0:
##            sell_price_gg == 0
##            print(m,' 77jjjjj')
##            print(xs,' == NOTREND ==','  5 ')


    '''            
        if sell_price_gg > 0 and sell_price_gg > buy_price_gg :
            print(m)
            print(xs,'   UPTREND','  5 ',pg5)
            print('\n')
            print('71 profit/uptrend [sell-buy] =',round((sell_price_gg - buy_price_gg),2),'   ',sell_price_gg,'   ',buy_price_gg)
            print('71 profit/uptrend [sell-buy] ===========================================================> ',round((sell_price_gg - buy_price_gg),2),'  ',xs)
            print('\n')
            print('Close[buy/sell]',round(df['Close'].loc[b6],2),'/',round(df['Close'].loc[s7],2))
            
            print(df['s2'].loc[b6],' / ',df['s2'].loc[s7])
            print('adx [buy/sell]',round(df['adx'].loc[b6],1),'/',round(df['adx'].loc[s7],1))
            print('vzo [buy/sell]',round(df['VZO'].loc[b6],1),' / ',round(df['VZO'].loc[s7],1),'    ','CCI ')
            print('ADL [buy/sell]',round(df['ADL'].loc[b6],1),' / ',round(df['ADL'].loc[s7],1),'    ','MOM ',round(df['MOM'].loc[b6],1),'/',round(df['MOM'].loc[s7],1))
            print('AD [buy/sell]',round(df['AD'].loc[b6],1),' / ',round(df['AD'].loc[s7],1),'    ','macd ',round(df['macd'].loc[b6],1),'/',round(df['macd'].loc[s7],1))



            print('\n')  
            if  round(df['Boling_middle'].loc[b6],1) < round(df['Close'].loc[b6],1) < round(df['Boling_upper'].loc[b6],1):
                print('buy [Boling_upper < close < Boling_middle] ',\
                      round(df['Boling_upper'].loc[b6],1),' < ',round(df['Close'].loc[b6],1),\
                      ' < ',round(df['Boling_middle'].loc[b6],1))
            if round(df['Boling_lower'].loc[b6],1) < round(df['Close'].loc[b6],1) < round(df['Boling_middle'].loc[b6],1):
                print('buy [Boling_middle < close < Boling_lower] ',round(df['Boling_middle'].loc[b6],1),' < ',round(df['Close'].loc[b6],1),' < ',round(df['Boling_lower'].loc[b6],1))
            if round(df['Boling_upper'].loc[b6],1) == round(df['Close'].loc[b6],1):
                print('buy [Boling_upper = close] ',round(df['Boling_upper'].loc[b6],1),' = ',round(df['Close'].loc[b6],1))
            if round(df['Boling_lower'].loc[b6],1) == round(df['Close'].loc[b6],1):          
                print('buy [Boling_lower = close] ',round(df['Boling_lower'].loc[b6],1),' = ',round(df['Close'].loc[b6],1))
            if round(df['Close'].loc[b6],1) > df['Boling_upper'].loc[b6]:
                print('buy [close  > Boling_upper] ',round(df['Close'].loc[b6],1) > round(df['Boling_upper'].loc[b6],1))         
            if round(df['Close'].loc[b6],1) < df['Boling_lower'].loc[b6]:
                print('buy [close  < Boling_lower] ',round(df['Close'].loc[b6],1),' < ',round(df['Boling_lower'].loc[b6],1))    

        ##        print('\n')
        ##        print('77777777777',df['Boling_upper'].loc[s7],'  ',round(df['Close'].loc[s7],1),'  ',round(df['Boling_middle'].loc[s7],1))
            if  round(df['Boling_middle'].loc[s7],1) < round(df['Close'].loc[s7],1) < round(df['Boling_upper'].loc[s7],1):
                print('sell [Boling_upper < close < Boling_middle] ',\
                      round(df['Boling_upper'].loc[s7],1),' < ',round(df['Close'].loc[s7],1),\
                      ' < ',round(df['Boling_middle'].loc[s7],1))
            elif round(df['Boling_lower'].loc[s7],1) < round(df['Close'].loc[s7],1) < round(df['Boling_middle'].loc[s7],1):
                print('sell [Boling_middle < close < Boling_lower] ',round(df['Boling_middle'].loc[s7],1),' < ',round(df['Close'].loc[s7],1),' < ',round(df['Boling_lower'].loc[s7],1))

            elif round(df['Boling_upper'].loc[s7],1) == round(df['Close'].loc[s7],1):
                print('sell [Boling_upper = close] ',round(df['Boling_upper'].loc[s7],1),' = ',round(df['Close'].loc[s7],1))
            elif round(df['Boling_lower'].loc[s7],1) == round(df['Close'].loc[s7],1):          
                print('sell [Boling_lower = close] ',round(df['Boling_lower'].loc[s7],1),' = ',round(df['Close'].loc[s7],1))
            elif round(df['Close'].loc[s7],1) > df['Boling_upper'].loc[s7]:
                print('sell [close  > Boling_upper] ',round(df['Close'].loc[s7],1) > round(df['Boling_upper'].loc[s7],1))         
            elif round(df['Close'].loc[s7],1) < df['Boling_lower'].loc[s7]:
                print('sell [close  < Boling_lower] ',round(df['Close'].loc[s7],1),' < ',round(df['Boling_lower'].loc[s7],1)) 
            print('\n') 



        elif sell_price_gg < buy_price_gg and sell_price_gg > 0:
            print(m)
            print(xs,'   UPTREND',' 6  ',pg5)
            print('72 Loss/uptrend [sell-buy] =',round((sell_price_gg - buy_price_gg),2),'   ',sell_price_gg,'   ',buy_price_gg)
            print('72 profit/uptrend [sell-buy] =============================================================================> ',\
                  round((sell_price_gg - buy_price_gg),2),'  ',xs)
            print('Close[buy/sell]',round(df['Close'].loc[b6],2),'/',round(df['Close'].loc[s7],2))
            print(df['s2'].loc[b6],' / ',df['s2'].loc[s7])
            print('adx',round(df['adx'].loc[b6],1),'/',round(df['adx'].loc[s7],1))
            print('vzo ',round(df['VZO'].loc[b6],1),' / ',round(df['VZO'].loc[s7],1),'    ','CCI ')
            print('ADL ',round(df['ADL'].loc[b6],1),' / ',round(df['ADL'].loc[s7],1),'    ','MOM ',round(df['MOM'].loc[b6],1),'/',round(df['MOM'].loc[s7],1))
            print('AD ',round(df['AD'].loc[b6],1),' / ',round(df['AD'].loc[s7],1),'    ','macd ',round(df['macd'].loc[b6],1),'/',round(df['macd'].loc[s7],1))

            print('\n')  
            if  round(df['Boling_middle'].loc[b6],1) < round(df['Close'].loc[b6],1) < round(df['Boling_upper'].loc[b6],1):
                print('buy [Boling_upper < close < Boling_middle] ',\
                      round(df['Boling_upper'].loc[b6],1),' < ',round(df['Close'].loc[b6],1),\
                      ' < ',round(df['Boling_middle'].loc[b6],1))
            if round(df['Boling_lower'].loc[b6],1) < round(df['Close'].loc[b6],1) < round(df['Boling_middle'].loc[b6],1):
                print('buy [Boling_middle < close < Boling_lower] ',round(df['Boling_middle'].loc[b6],1),' < ',round(df['Close'].loc[b6],1),' < ',round(df['Boling_lower'].loc[b6],1))
            if round(df['Boling_upper'].loc[b6],1) == round(df['Close'].loc[b6],1):
                print('buy [Boling_upper = close] ',round(df['Boling_upper'].loc[b6],1),' = ',round(df['Close'].loc[b6],1))
            if round(df['Boling_lower'].loc[b6],1) == round(df['Close'].loc[b6],1):          
                print('buy [Boling_lower = close] ',round(df['Boling_lower'].loc[b6],1),' = ',round(df['Close'].loc[b6],1))
            if round(df['Close'].loc[b6],1) > df['Boling_upper'].loc[b6]:
                print('buy [close  > Boling_upper] ',round(df['Close'].loc[b6],1) > round(df['Boling_upper'].loc[b6],1))         
            if round(df['Close'].loc[b6],1) < df['Boling_lower'].loc[b6]:
                print('buy [close  < Boling_lower] ',round(df['Close'].loc[b6],1),' < ',round(df['Boling_lower'].loc[b6],1))    

        ##        print('\n')
        ##        print('77777777777',df['Boling_upper'].loc[s7],'  ',round(df['Close'].loc[s7],1),'  ',round(df['Boling_middle'].loc[s7],1))
            if  round(df['Boling_middle'].loc[s7],1) < round(df['Close'].loc[s7],1) < round(df['Boling_upper'].loc[s7],1):
                print('sell [Boling_upper < close < Boling_middle] ',\
                      round(df['Boling_upper'].loc[s7],1),' < ',round(df['Close'].loc[s7],1),\
                      ' < ',round(df['Boling_middle'].loc[s7],1))
            elif round(df['Boling_lower'].loc[s7],1) < round(df['Close'].loc[s7],1) < round(df['Boling_middle'].loc[s7],1):
                print('sell [Boling_middle < close < Boling_lower] ',round(df['Boling_middle'].loc[s7],1),' < ',round(df['Close'].loc[s7],1),' < ',round(df['Boling_lower'].loc[s7],1))

            elif round(df['Boling_upper'].loc[s7],1) == round(df['Close'].loc[s7],1):
                print('sell [Boling_upper = close] ',round(df['Boling_upper'].loc[s7],1),' = ',round(df['Close'].loc[s7],1))
            elif round(df['Boling_lower'].loc[s7],1) == round(df['Close'].loc[s7],1):          
                print('sell [Boling_lower = close] ',round(df['Boling_lower'].loc[s7],1),' = ',round(df['Close'].loc[s7],1))
            elif round(df['Close'].loc[s7],1) > df['Boling_upper'].loc[s7]:
                print('sell [close  > Boling_upper] ',round(df['Close'].loc[s7],1) > round(df['Boling_upper'].loc[s7],1))         
            elif round(df['Close'].loc[s7],1) < df['Boling_lower'].loc[s7]:
                print('sell [close  < Boling_lower] ',round(df['Close'].loc[s7],1),' < ',round(df['Boling_lower'].loc[s7],1)) 
            print('\n') 

        elif sell_price_gg == 0 or sell_price_gg == ' ' :
            print(m)
            print(xs,'   UPTREND','   ',pg5)
            print('no sell, only buy *********************************************===========================================================')
             
        ##print('b6=',buy_price_gg,'  s7=',sell_price_gg)
        print('buy_price [buy/sell] =',round(buy_price_gg,2),' sell_price=',round(sell_price_gg,2))
        print('b6 index=',b6,'   s7 index=',s7)

        df['profit']=sell_price_gg-buy_price_gg
        print('\n\n')
        ##    print(df.iloc[s7,[df.columns.get_loc('profit'),df.columns.get_loc('ticker'),df.columns.get_loc('Close'),df.columns.get_loc('macd'),df.columns.get_loc('MOM'),df.columns.get_loc('adx'),\
        ##                      df.columns.get_loc('Close_vwap'),df.columns.get_loc('AD'),df.columns.get_loc('ADL'),df.columns.get_loc('VZO'),\
        ##                      df.columns.get_loc('STOCHRSI_fastk'), df.columns.get_loc('RSI'),\
        ##                      df.columns.get_loc('SAR'), df.columns.get_loc('SARx')\
        ##                      ,df.columns.get_loc('s3'),df.columns.get_loc('s2'),df.columns.get_loc('Close_EMA3')\
        ##                      ,df.columns.get_loc('Close_EMA5'),df.columns.get_loc('Close_EMA10')\
        ##                      ,df.columns.get_loc('Close_EMA21'),df.columns.get_loc('EMA_3_vwap')\
        ##                      ,df.columns.get_loc('EMA_5_vwap'),df.columns.get_loc('EMA_10_vwap')\
        ##                      ,df.columns.get_loc('EMA_21_vwap'),df.columns.get_loc('EMA_10_vwap')]],'695')
        ##
        ##    print(df.iloc[b6,[df.columns.get_loc('profit'),df.columns.get_loc('ticker'),df.columns.get_loc('Close'),df.columns.get_loc('macd'),df.columns.get_loc('MOM'),df.columns.get_loc('adx'),\
        ##                      df.columns.get_loc('Close_vwap'),df.columns.get_loc('AD'),df.columns.get_loc('ADL'),df.columns.get_loc('VZO'),\
        ##                      df.columns.get_loc('STOCHRSI_fastk'), df.columns.get_loc('RSI'),\
        ##                      df.columns.get_loc('SAR'), df.columns.get_loc('SARx')\
        ##                      ,df.columns.get_loc('s3'),df.columns.get_loc('s2'),df.columns.get_loc('Close_EMA3')\
        ##                      ,df.columns.get_loc('Close_EMA5'),df.columns.get_loc('Close_EMA10')\
        ##                      ,df.columns.get_loc('Close_EMA21'),df.columns.get_loc('EMA_3_vwap')\
        ##                      ,df.columns.get_loc('EMA_5_vwap'),df.columns.get_loc('EMA_10_vwap')\
        ##                      ,df.columns.get_loc('EMA_21_vwap'),df.columns.get_loc('EMA_10_vwap')]],'695')
        print(df['buy'],' buy','\n')
        print(df['sell'],' sell','\n')
        print(df.iloc[:,df.columns.get_loc('sell')],' ------d------- sell')
        print(df.iloc[:,df.columns.get_loc('buy')],' ------d------- buy')

        dfp=df.iloc[s7,[df.columns.get_loc('profit'),df.columns.get_loc('sell'),df.columns.get_loc('ticker'),df.columns.get_loc('Close'),df.columns.get_loc('macd'),df.columns.get_loc('MOM'),df.columns.get_loc('adx'),\
                          df.columns.get_loc('Close_vwap'),df.columns.get_loc('AD'),df.columns.get_loc('ADL'),df.columns.get_loc('VZO'),\
                          df.columns.get_loc('STOCHRSI_fastk'), df.columns.get_loc('RSI'),\
                          df.columns.get_loc('SAR'), df.columns.get_loc('SARx')\
                          ,df.columns.get_loc('s3'),df.columns.get_loc('s2'),df.columns.get_loc('Close_EMA3')\
                          ,df.columns.get_loc('Close_EMA5'),df.columns.get_loc('Close_EMA10')\
                          ,df.columns.get_loc('Close_EMA21'),df.columns.get_loc('EMA_3_vwap')\
                          ,df.columns.get_loc('EMA_5_vwap'),df.columns.get_loc('EMA_10_vwap')\
                          ,df.columns.get_loc('EMA_21_vwap'),df.columns.get_loc('EMA_10_vwap')\
                        ,df.columns.get_loc('bolinger'),df.columns.get_loc('bolinger_n')
                        
                        ]]


        dfg=df.iloc[b6,[df.columns.get_loc('profit'),df.columns.get_loc('buy'),df.columns.get_loc('ticker'),df.columns.get_loc('Close'),df.columns.get_loc('macd'),df.columns.get_loc('MOM'),df.columns.get_loc('adx'),\
                          df.columns.get_loc('Close_vwap'),df.columns.get_loc('AD'),df.columns.get_loc('ADL'),df.columns.get_loc('VZO'),\
                          df.columns.get_loc('STOCHRSI_fastk'), df.columns.get_loc('RSI'),\
                          df.columns.get_loc('SAR'), df.columns.get_loc('SARx')\
                          ,df.columns.get_loc('s3'),df.columns.get_loc('s2'),df.columns.get_loc('Close_EMA3')\
                          ,df.columns.get_loc('Close_EMA5'),df.columns.get_loc('Close_EMA10')\
                          ,df.columns.get_loc('Close_EMA21'),df.columns.get_loc('EMA_3_vwap')\
                          ,df.columns.get_loc('EMA_5_vwap'),df.columns.get_loc('EMA_10_vwap')\
                          ,df.columns.get_loc('EMA_21_vwap'),df.columns.get_loc('EMA_10_vwap')\
                        ,df.columns.get_loc('bolinger'),df.columns.get_loc('bolinger_n')
                        
                        ]]

        dfp=pd.DataFrame(dfp)
        dfg=pd.DataFrame(dfg)
        dfp.reset_index(inplace=True)
        dfg.reset_index(inplace=True)
        print(dfp.columns,'dddd')
        print(dfg.columns,' fffaaa')
        gg=pd.concat([dfg,dfp],axis=1)
        gg.set_index(gg.iloc[:,0],inplace=True)
        print(gg.iloc[:,[1,3]])
        print('\n\n')
        ## $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        ## $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


        print(' ------------------------------------------------------------------------------------')

##        sell_price_ggb=0
##        b6=0
##        s7=0
    '''    



        
