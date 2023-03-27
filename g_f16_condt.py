def tickersp():
    m=['t','oxy','amgn','arkk','tsla','x','googl','aapl','uso','oil']
    return(m)
    

######################################################################
# Call / up
def con_buy_up(df,x,xs):
    buy_condition=(df['ADL'].loc[x] > 0)
##    print('nn',' buy_condition rule up------   ',buy_condition)
    return(buy_condition)

def con_sell_up(df,z,xs):
    sell_condition=(df['ADL'].loc[z] > 0)
    return(sell_condition)

######################################################################
# Put / up
def con_buy_down(df,x,xs):
    
    buy_condition=(df['macd'] < 0)
##    g5=str('df['macd'].loc[x] < 0')
##    print(xs,'  close  ',df['Close'].loc[x],' macd---  ',df['macd'].loc[x],'  nn',' buy_condition rule down------   ',buy_condition,' ','  ',df['macd'])
##    buy_condition=(df['macd'].loc[z] < 0) and (df['vzo'].loc[z] > 100)
    return(buy_condition)


def con_sell_down(df,z,xs):
    sell_condition=(df['macd'].loc[z] > 0) 
##    sell_condition=(df['ADL'].loc[z] > 0) or df['Close'].loc[z] > df['Close'].loc[z]-df['Close'].shift(1).loc[z]*.1
    return(sell_condition)
    
######################################################################



def test33(df,buy_price_gg,xs):
    m=55
    return(m,df,buy_price_gg,xs)


def test34(df,buy_price_gg,xs):
    mp=65
    return(mp,df,buy_price_gg,xs)

######################################################################
def buy_call(df,buy_price_gg,xs):
    
    import f16_buy
    from f16_buy import f16_buyp
    import f16_sell
    from f16_sell import f16_sellp

    print(xs,' ========== 999 [Call] thing running')
        
    df,xs,buy_status,b6,buy_price_gg=f16_buy.f16_buyp(df,buy_price_gg,xs)
    if buy_status=='yes':
        print('if buy condt met? === buy cond met  ',df)
##        print(df,'   ',xs,'  ',buy_price_gg)       
        xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status=f16_sell.f16_sellp(xs,b6,df,buy_price_gg,buy_status)
        if sell_status=='yes':
            print('============if sell condt met? === sell cond met') 
            print("============Buy Call/uptrend --> ",(xs,'   ',sell_price_gg-buy_price_gg))
            return(df,xs,buy_status,b6,buy_price_gg)
        else:
            return(df,xs,buy_status,b6,buy_price_gg)
            
    else:
        return(df,xs,buy_status,b6,buy_price_gg)
      

################ end of buy call (stock moving up) ############## 

def buy_put(df,buy_price_gg,xs):
    
    import f17_buy
    from f17_buy import f17_buyp
    import f17_sell
    from f17_sell import f17_sellp
    import sys
    sell_price_gg=-1
    s7=-1
    print(xs,' 999 [Put] Downtrend thing running')


    df,xs,buy_status,b6,sell_price_gg,buy_price_gg,buy_condition=f17_buy.f17_buyp(df,buy_price_gg,xs)
##    print(xs,'pppzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
    if buy_status=='yes':
##        print(buy_price_gg,df,'   ',xs,'  ','put ===', buy_price_gg)
##        print('tata')
##        sys.exit()
        xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status=f17_sell.f17_sellp(xs,b6,df,buy_price_gg,buy_status)
##        print("Buy 77 Put/downtrend --> ",xs)
##        print('\n')
        print(xs,'  ','buy_price= ',round(buy_price_gg,2),' ','sell_price= ',round(sell_price_gg,2))
##        print('\n')
        print(xs,' Profit= ',round((sell_price_gg-buy_price_gg),2),'   ',df)
        return(xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status)
##############################
        if sell_status=='yes':
##            print('if sell condt met? === sell cond met') 
##            print("Buy Call/uptrend --> ",(xs,'   ',sell_price_gg-buy_price_gg))
##            return(df,xs,buy_status,b6,buy_price_gg)
            return(xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status)
        else:
##            return(df,xs,buy_status,b6,buy_price_gg)
            return(xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status)
##################################

    else:
        return(xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status)
    

