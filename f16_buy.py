def inputs(df,buy_price_gg,x,xs,gft,gft2):
    import f16_condt
    from f16_condt import con_buy_up
##    print(df['EMA-35'].loc[x])
    buy_status='no'
    sell_price_gg=-1
    b6=-1

    df.reset_index(inplace=True)
    
    df['gg']=''
    for x in range(0,df.shape[0],1):
        df['gg'].loc[x]=x
##        print(x)
##    print('hhhh',df)

    

    for x in df.index:
        dfq=df.iloc[x,:]
        buy_condition=f16_condt.con_buy_up(dfq,x,xs)
##        buy_condition=(df['macd'].loc[x] < 0)
        
##        buy_condition=con_buy_up(df,x,xs)
        if buy_condition==True:
##            print(xs,'buy put condition met -----James Bond 007--------------')
            b6=x
##            f=open('/home/az2/bb44444.txt','w+')
##            f.write('sell'+str(',')+str(df['ticker'].loc[x])+str(',')+str(' close--> ')+str(df['Close'].loc[x]))
##            f.close()

            buy_price_gg=df['Close'].loc[x]
    ##            print(df['ticker'].loc[x],'=========== ',buy_price_gg)
##            print(b6,'=========== ',buy_price_gg)
            buy_status='yes'
            
            return(df,xs,buy_status,b6,sell_price_gg,buy_price_gg,buy_condition,gft,gft2)  
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
##            print(xs,'  ========= No Put buy',buy_status)
##            print(df,'  kkkk')

            return(df,xs,buy_status,b6,sell_price_gg,buy_price_gg,buy_condition,gft,gft2)    
        
##    fg.write(buy_condition)


def f16_buyp(df,buy_price_gg,xs,gft,gft2):    
##    print('hello - in f16_buy')        
            ############# Buy condition for Uptrend ########################
    for x in df.index:
        
        
##        print('jjj')
    ##        df['i'].loc[x]=i
    ##        buy_condition=(df['ADL'].loc[x] > 0)
        
        df,xs,buy_status,b6,sell_price_gg,buy_price_gg,buy_condition,gft,gft2=inputs(df,buy_price_gg,x,xs,gft,gft2)
##        print('buy price from f16_buy= ',buy_price_gg)
##        print(df,buy_status,b6,buy_price_gg,'   mmmmm')
        return(df,xs,buy_status,b6,sell_price_gg,buy_price_gg,buy_condition,gft,gft2)    
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

