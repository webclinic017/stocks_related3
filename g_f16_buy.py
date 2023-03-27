def inputs(df,buy_price_gg,x,xs):
    import f16_condt
    from f16_condt import con_buy_up
    print(df,buy_price_gg,x,xs)
    buy_status='no'
    b6=-1
##    f = open('/home/az2/b_94519.txt', 'a+')
##    buy_condition=(df['ADL'].loc[x] > 0)
    
    buy_condition=con_buy_up(df,x,xs)
    
##    f.write(str('_'))
##    f.write(buy_condition)
##    f.write(str('_'))
##    f.write('\n')         
##    f.close()         
##    buy_condition=(df['EMA-35'].loc[x] > 0 and (df['MOM'].loc[x] > 0) and (df['ADL'].loc[x] > 0) and\
##                    df['Close_EMA3'].loc[x] > 0 and df['EMA_3_vwap'].loc[x] > 0 and \
##                   df['p2'].loc[x]>0)

##    print("jjjjjhhhhh")
    for x in df.index:
##        buy_condition=con_buy_up(df,x,xs)
        if buy_condition==True:
            b6=x
##            f=open('/home/az2/bb44444.txt','w+')
##            f.write('buy'+str(',')+str(df['ticker'].loc[x])+str(',')+str(' close--> ')+str(df['Close'].loc[x]))
##            f.close()

            buy_price_gg=df['Close'].loc[x]
    ##            print(df['ticker'].loc[x],'=========== ',buy_price_gg)
            print('=========== ',xs,'  ',buy_price_gg)
            buy_status='yes'
            
            return(df,buy_status,b6,buy_price_gg)  
            break
                               
    ##    elif buy_condition==(df['EMA-35'].loc[x] < 0 and (df['MOM'].loc[x] < 0) and (df['ADL'].loc[x] < 0) and\
    ##                    df['Close_EMA3'].loc[x] < 0 and df['EMA_3_vwap'].loc[x] < 0 and \
    ##                   df['p2'].loc[x]<0):
    ##                        
    ##        f=open('/home/az2/bb44444.txt','w+')
    ##        f.write('sell'+str(',')+str(df['ticker'].loc[x])+str(',')+str(' close--> ')+str(df['Close'].loc[x]))
    ##        f.close()
        elif buy_condition==False and df.shape[0]-1==x:
            b6=-1
            buy_price_gg=-1
            buy_status = 'no'
##            print(xs,'  ========= No buy',buy_status)
##            print(df,'  kkkk')

            return(df,buy_status,b6,buy_price_gg)    
        
##    fg.write(buy_condition)


def f16_buyp(df,buy_price_gg,xs):
    
##    print('hello - in f16_buy')        
            ############# Buy condition for Uptrend ########################
    for x in df.index:
        
        
##        print('jjj')
    ##        df['i'].loc[x]=i
    ##        buy_condition=(df['ADL'].loc[x] > 0)
        
        df,buy_status,b6,buy_price_gg=inputs(df,buy_price_gg,x,xs)
##        print(buy_status,'   mmmmm')
##        print(xs,buy_status,b6,buy_price_gg,'      f16_buyp  ')
##        print('------------- 420 is not good ----------')
        return(df,xs,buy_status,b6,buy_price_gg)    
##        if buy_condition==True:
##            buy_price_gg = df['Close'].loc[x]
##            sell_price_gg = 0
##            
##            b=df['adx'].loc[x]
##            b6=x
##            df['buy'].loc[x]='buy'
##            break
            
            
            
    
    

    ##
    ##        if (df['macd'].loc[x] > 0) and (df['Close_vwap'].loc[x] > 0) and (df['Close_vwap'].shift(1).loc[x] < 0)\
    ##           and (df['ADL'].loc[x] > 0):
    ##            or \
    ##           (df['EMA-2150'].loc[x] > 0) or (df['EMA-35'].loc[x] > 0) and (df['EMA-510'].loc[x] > 0) or\
    ##           (df['EMA-1021'].loc[x] > 0) :

    ##           (df['EMA_3_vwap'].loc[x] > 0):
    ##           (df['EMA_5_vwap'].loc[x] > 0) and \
    ##           (df['EMA-2150'].loc[x] > 0):
    ##            (df['Close_vwap'].loc[x] > 0) and (df['Close_vwap'].shift(1).loc[x] < 0) and \
            
##    pg5=df['Close_vwap'].loc[x]+df['EMA_3_vwap'].loc[x]+df['EMA_5_vwap'].loc[x]+df['EMA-2150'].loc[x]






    ##            if df['Boling_upper'].loc[x] < 55500:
    ##                df['bolinger'].loc[x]=df['Close'].loc[x] 
                

    ##            if df['Boling_upper'].loc[x] <= df['Close'].loc[x] <= df['Boling_middle'].loc[x]:
    ##                df['bolinger'].loc[x]='bolinger_upper < close < bolinger_middle'
    ##                df['bolinger_n'].loc[x]=str(round(df['Boling_upper'].loc[x],2))+ str(' < ') + str(round(df['Close'].loc[x],2)) + str(' < ') +  str(round(df['Bolinger_middle'].loc[x],2)) 
    ##            if df['Close'].loc[x]  > df['Boling_upper'].loc[x]:
    ##                df['bolinger'].loc[x]='close > bolinger_upper'
    ##                df['bolinger_n'].loc[x]=str(round(df['Close'].loc[x],2)) + str(' > ') + str(round(df['Boling_upper'].loc[x],2))
    ##                
    ##            if df['Close'].loc[x]  < df['Boling_lower'].loc[x]:
    ##                df['bolinger'].loc[x]='close < bolinger_lower'
    ##                df['bolinger_n'].loc[x]= str(round(df['Close'].loc[x],2)) + str(' < ')+ str(round(df['Boling_lower'].loc[x],2))
    ##            if df['Boling_middle'].loc[x] <= df['Close'].loc[x] <= df['Boling_lower'].loc[x]:
    ##                df['bolinger'].loc[x]='Boling_middle < close < bolinger_lower'
    ##                df['bolinger_n'].loc[x]=str(round(df['Boling_middle'].loc[x],2))+str(' < ') + str(round(df['Close'].loc[x],2))+ str('< ')+ str(round(df['Boling_lower'].loc[x],2)) 
    ##

    ##            df['Boling_upper'], df['Boling_middle'], df['Boling_lower']


##            df['Boling_upper'], df['Boling_middle'], df['Boling_lower']

        


##    elif x==df.shape[0] and buy_price_gg==0:
##        buy_price_gg = 0
##        df['buy'].loc[x]='buy'


    ##    print(buy_price_gg,' n  ',pg5)
    ##    sys.exit()            

