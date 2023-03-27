def tickersp():
    m=['t','oxy','amgn','arkk','tsla','x','googl','aapl','uso','oil']
    return(m)
    


def con_buy_up(df,x):
    buy_condition=(df['ADL'].loc[x] > 0)
    return(buy_condition)

def con_sell_up(df,z):
    sell_condition=(df['ADL'].loc[z] > 0)
    return(sell_condition)


def con_buy_down(df,z):
    buy_condition=(df['macd'].loc[z] < 0) and (df['vzo'].loc[z] > 100)
    return(buy_condition)


def con_sell_down(df,z):
    sell_condition=(df['ADL'].loc[z] > 0) or df['Close'].loc[z] > df['Close'].loc[z]-df['Close'].shift(1).loc[z]*.1
    return(sell_condition)
    




def test33(df,buy_price_gg,xs):
    m=55
    return(m,df,buy_price_gg,xs)


def test34(df,buy_price_gg,xs):
    mp=65
    return(mp,df,buy_price_gg,xs)


def buy_call(df,buy_price_gg,xs):
    
    import f16_buy
    from f16_buy import f16_buyp
    import f16_sell
    from f16_sell import f16_sellp
        
    df,xs,buy_status,b6,buy_price_gg=f16_buy.f16_buyp(df,buy_price_gg,xs)
    if buy_status=='yes':
        print('if buy condt met? === buy cond met')
##        print(df,'   ',xs,'  ',buy_price_gg)       
        xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status=f16_sell.f16_sellp(xs,b6,df,buy_price_gg,buy_status)
        if sell_status=='yes':
            print('if sell condt met? === sell cond met') 
            print("Buy Call/uptrend --> ",(xs,'   ',sell_price_gg-buy_price_gg))
            return(df,xs,buy_status,b6,buy_price_gg)
        else:
            return(df,xs,buy_status,b6,buy_price_gg)
            
    else:
        return(df,xs,buy_status,b6,buy_price_gg)
      
##    if buy_status=='yes':
##        print('if buy condt met? === buy cond met')
####        print(df,'   ',xs,'  ',buy_price_gg)       
##        xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status=f16_sell.f16_sellp(xs,b6,df,buy_price_gg,buy_status)
##
##        print(xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status,'------------')
##        if sell_status=='yes':
##            print('if sell condt met? === sell cond met') 
##            print("Buy Call/uptrend --> ",(xs,'   ',sell_price_gg-buy_price_gg))
####            return(xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status)
##            return(df,buy_status)  
################ end of buy call (stock moving up) ############## 

def buy_put(df,buy_price_gg,xs):
    
    import f17_buy
    from f17_buy import f17_buyp
    import f17_sell
    from f17_sell import f17_sellp
    sell_price_gg=-1
    s7=-1


    df,xs,buy_status,b6,buy_price_gg=f17_buy.f17_buyp(df,buy_price_gg,xs)
    if buy_status=='yes':
##        print(df,'   ',xs,'  ',buy_price_gg)       
        xs,df,buy_price_gg,sell_price_gg,b6,s7=f17_sell.f17_sellp(xs,b6,df,buy_price_gg)
        print("Buy Put/downtrend --> ",(xs,'   ',sell_price_gg-buy_price_gg))
        return(xs,df,buy_price_gg,sell_price_gg,b6,s7)
    else:
        return(xs,df,buy_price_gg,sell_price_gg,b6,s7)
    
