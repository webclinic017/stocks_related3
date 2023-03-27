def tickersp(gft,gft2):
##    m=['t','oxy','amgn','arkk','tsla','x','googl','aapl','uso','oil']
    m=['tsla','uber','x']
    return(m,gft,gft2)
    

######################################################################
# Call / up
def con_buy_up(df,x,xs):
    buy_condition=(df['p2'] > 0)
##    print('nn',' buy_condition rule up------   ',buy_condition)
    return(buy_condition)

def con_sell_up(df,z,xs):
    sell_condition=(df['p2'].loc[z] < 0)
    return(sell_condition)

######################################################################
# Put / up
def con_buy_down(df,x,xs):
    
    buy_condition=(df['p2'] < 0)
##    g5=str('df['macd'].loc[x] < 0')
##    print(xs,'  close  ',df['Close'].loc[x],' macd---  ',df['macd'].loc[x],'  nn',' buy_condition rule down------   ',buy_condition,' ','  ',df['macd'])
##    buy_condition=(df['macd'].loc[z] < 0) and (df['vzo'].loc[z] > 100)
    return(buy_condition)


def con_sell_down(df,z,xs):
    sell_condition=(df['p2'].loc[z] > 0) 
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
##def buy_call(df,buy_price_gg,xs):
##    
##    import f16_buy
##    from f16_buy import f16_buyp
##    import f16_sell
##    from f16_sell import f16_sellp
##
##    print(xs,' ========== 999 [Call] thing running')
##        
##    df,xs,buy_status,b6,buy_price_gg=f16_buy.f16_buyp(df,buy_price_gg,xs)
##    if buy_status=='yes':
##        print('if buy condt met? === buy cond met  ',df)
####        print(df,'   ',xs,'  ',buy_price_gg)       
##        xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status=f16_sell.f16_sellp(xs,b6,df,buy_price_gg,buy_status)
##        if sell_status=='yes':
##            print('============if sell condt met? === sell cond met') 
##            print("============Buy Call/uptrend --> ",(xs,'   ',sell_price_gg-buy_price_gg))
##            return(df,xs,buy_status,b6,buy_price_gg)
##        else:
##            return(df,xs,buy_status,b6,buy_price_gg)
##            
##    else:
##        return(df,xs,buy_status,b6,buy_price_gg)
##      
            ######################################### 55
            ##def buy_call(df,buy_price_gg,xs,gft,gft2):
            ##    
            ##    import f16_buy
            ##    from f16_buy import f16_buyp
            ##    import f16_sell
            ##    from f16_sell import f16_sellp
            ##    import sys
            ##    import summary
            ##    from summary import pp
            ##    sell_price_gg=-1
            ##    s7=-1
            ####    print('llllll')
            ####    global gft
            ##
            ##    
            ##    
            ##    print('[6] ',xs,' 999 [Call] Uptrend thing running')
            ##
            ##
            ##    df,xs,buy_status,b6,sell_price_gg,buy_price_gg,buy_condition,gft,gft2=f16_buy.f16_buyp(df,buy_price_gg,xs,gft,gft2)
            ####    print(xs,'pppzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
            ##    if buy_status=='yes':
            ##        xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status,gft,gft2=f16_sell.f16_sellp(xs,b6,df,buy_price_gg,buy_status,gft,gft2)
            ##        
            ##        print('[7] ',xs,'  ','buy_price= ',round(buy_price_gg,2),' ','sell_price= ',round(sell_price_gg,2))
            ####        print('\n')
            ##        print('[8] ',xs,' Profit= ',round((sell_price_gg-buy_price_gg),2),'   ',df)
            ##        print('[9] ',df['s3'].loc[1])
            ##
            ##        return(xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status,gft,gft2)
            ################################
            ##        if sell_status=='yes':
            ##            profit=sell_price_gg-buy_price_gg
            ##            gft.concat(xs,buy_price_gg,sell_price_gg,b6,s7,profit,axis=0)
            ####            summary.pp(gft)
            ##            return(xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status,gft,gft2)
            ##        else:
            ####            return(df,xs,buy_status,b6,buy_price_gg)
            ##            return(xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status,gft,gft2)
            ####################################
            ##
            ##    else:
            ##        return(xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status,gft,gft2)
            #########################################  55
            ################## end of buy call (stock moving up) ############## 

def buy_put(df,buy_price_gg,xs,gft,gft2):
    
    import f17_buy
    from f17_buy import f17_buyp
    import f17_sell
    from f17_sell import f17_sellp
    import sys
    import pandas as pd
    import json
    import summary
    from summary import pp
    sell_status=' '

##    print('[10] ','running [f16_condt.py]')

    sell_price_gg=-1
    s7=-1
##    print(xs,' 999 [Put] Downtrend thing running')
    df,xs,buy_status,b6,sell_price_gg,buy_price_gg,buy_condition,gft,gft2=f17_buy.f17_buyp(df,buy_price_gg,xs,gft,gft2)
##    print(xs,'pppzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
    if buy_status=='yes':
        xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status,gft,gft2=f17_sell.f17_sellp(xs,b6,df,buy_price_gg,buy_status,gft,gft2)
##        print(xs,'  ','buy_price= ',round(buy_price_gg,2),' ','sell_price= ',round(sell_price_gg,2))
####        print('\n')
##        print(xs,' Profit= ',round((sell_price_gg-buy_price_gg),2),'   ',df)
##        print(df['s3'].loc[1])
##        return(xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status,gft)
##############################
        if sell_status=='yes':

            g5=pd.Series(df['s3'].loc[2])
            g6=pd.Series('Put')
           
            print('[11] ',xs,'  ','buy_price= ',round(buy_price_gg,2),' ','sell_price= ',round(sell_price_gg,2))
##        print('\n')
            print('[12] ',xs,' Profit= ',round((sell_price_gg-buy_price_gg),2),'   ',df,df['s3'].loc[1])
            profit=sell_price_gg-buy_price_gg
##            print('xs',type(xs))
##            print('buy_price_gg',type(buy_price_gg))
##            print('b6',type(b6))
##            print('profit',type(profit))
            xs=pd.Series(xs)
            buy_price_gg=pd.Series(buy_price_gg)
            sell_price_gg=pd.Series(sell_price_gg)
            b6=pd.Series(b6)
            s7=pd.Series(s7)
            profit=sell_price_gg-buy_price_gg
            profit=pd.Series(profit)
            g5=g5
            g6=g6
##            buy_price_gg=pd.to_son(buy_price_gg)
            gft=pd.concat([xs,buy_price_gg,sell_price_gg,b6,s7,profit,g5,g6],axis=0)
##            gft=gft.T

##            print('\n\n\n\n')
            gft=pd.DataFrame(gft)
            gft=gft.T
            gft.columns = ['V', 'W', 'X', 'Y', 'Z','h','j','Stragety']
##            gft.loc[len(gft.index)] = [xs,buy_price_gg,sell_price_gg,b6,s7,profit]
            print('\n\n\n')
            print('[13]   ',gft)
            print('\n\n\n')
            gft2=gft2.append(gft)
##            print(gft)
##            pz=summary.pp(gft,gft2)
##            gft.columns=['xs','buy_price_gg','sell_price_gg','b6','s7','profit']
##            print(gft,'hhhhhhhhhh')
##            print(gft.shape,'9999')
##            print(xs,buy_price_gg,sell_price_gg,b6,s7,profit,'   44444')
    ##            summary.pp(gft)

##            print('[14] ','end [f16_condt.py]')
##            print(pz,'tttt')
            return(xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status,gft,gft2)
        else:
##            print('fff')
            profit=sell_price_gg-buy_price_gg
            gft=pd.concat([xs,buy_price_gg,sell_price_gg,b6,s7,profit],axis=0)
            gft=json.load(gft)   
##            print(xs,buy_price_gg,sell_price_gg,b6,s7,profit,'   55555')
    ##            return(df,xs,buy_status,b6,buy_price_gg)

##            print('[15] ','end [f16_condt.py]')
##            print('\n')
            return(xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status,gft,gft2)
##################################
##        return(xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status,gft,gft2)
##        return(xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status,gft,gft2)

    else:
##        print('\n')
##        print('[16] ','end [f16_condt.py]')
##        print('\n')
        return(xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status,gft,gft2)









############################## new buy call ####################################################################
def buy_call(df,buy_price_gg,xs,gft,gft2):
    
    import f16_buy
    from f16_buy import f16_buyp
    import f16_sell
    from f16_sell import f16_sellp
    import sys
    import pandas as pd
    import json
    import summary
    from summary import pp



##    print('[10] ','running [f16_condt.py]')

    sell_price_gg=-1
    s7=-1


    df,xs,buy_status,b6,sell_price_gg,buy_price_gg,buy_condition,gft,gft2=f16_buy.f16_buyp(df,buy_price_gg,xs,gft,gft2)
####    print(xs,'pppzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
    if buy_status=='yes':
        xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status,gft,gft2=f16_sell.f16_sellp(xs,b6,df,buy_price_gg,buy_status,gft,gft2)
##              
##        print(xs,'  ','buy_price= ',round(buy_price_gg,2),' ','sell_price= ',round(sell_price_gg,2))
####        print('\n')
##        print(xs,' Profit= ',round((sell_price_gg-buy_price_gg),2),'   ',df)
##        print(df['s3'].loc[1])
##        return(xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status,gft)
##############################
        if sell_status=='yes':

            g5=pd.Series(df['s3'].loc[2])
            g6=pd.Series('Call')
           
            print('[11] ',xs,'  ','buy_price= ',round(buy_price_gg,2),' ','sell_price= ',round(sell_price_gg,2))
##        print('\n')
            print('[12] ',xs,' Profit= ',round((sell_price_gg-buy_price_gg),2),'   ',df,df['s3'].loc[1])
            profit=sell_price_gg-buy_price_gg
##            print('xs',type(xs))
##            print('buy_price_gg',type(buy_price_gg))
##            print('b6',type(b6))
##            print('profit',type(profit))
            xs=pd.Series(xs)
            buy_price_gg=pd.Series(buy_price_gg)
            sell_price_gg=pd.Series(sell_price_gg)
            b6=pd.Series(b6)
            s7=pd.Series(s7)
            profit=sell_price_gg-buy_price_gg
            profit=pd.Series(profit)
            profit=pd.Series(profit)
            g5=pd.Series(g5)
            g6=pd.Series(g6)
##            buy_price_gg=pd.to_son(buy_price_gg)
            gft=pd.concat([xs,buy_price_gg,sell_price_gg,b6,s7,profit,g5,g6],axis=0)
##            gft=gft.T

##            print('\n\n\n\n')
            gft=pd.DataFrame(gft)
            gft=gft.T
            gft.columns = ['V', 'W', 'X', 'Y', 'Z','h','j','Stragety']
##            gft.loc[len(gft.index)] = [xs,buy_price_gg,sell_price_gg,b6,s7,profit]
            print('\n\n\n')
            print('[13]   ',gft)
            print('\n\n\n')
            gft2=gft2.append(gft)

            return(xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status,gft,gft2)
##        else:
##            print('================================ fff ======================')
##            profit=sell_price_gg-buy_price_gg
##            profit=pd.Series(profit)
####            print('xs',' ',type(xs))
####            print('buy_price_gg',' ',type(buy_price_gg))
####            print('sell_price_gg',' ',type(sell_price_gg))
####            print('b6',' ',type(b6))
####            print('s7',' ',type(s7))
####            print('profit',' ',type(profit))
##            
##            xs=pd.Series(xs)
##            buy_price_gg=pd.Series(buy_price_gg)
##            sell_price_gg=pd.Series(sell_price_gg)
##            b6=pd.Series(b6)
##            s7=pd.Series(s7)
##            profit=pd.Series(profit)
##            
##            gft=pd.concat([xs,buy_price_gg,sell_price_gg,b6,s7,profit],axis=0)
####            gft=json.load(gft)   
####            print(xs,buy_price_gg,sell_price_gg,b6,s7,profit,'   55555')
##    ##            return(df,xs,buy_status,b6,buy_price_gg)
##
####            print('[15] ','end [f16_condt.py]')
####            print('\n')
##            return(xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status,gft,gft2)
##################################
##        return(xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status,gft,gft2)
##        return(xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status,gft,gft2)

##    else:
####        print('\n')
####        print('[16] ','end [f16_condt.py]')
####        print('\n')
##        return(xs,df,buy_price_gg,sell_price_gg,b6,s7,buy_status,sell_status,gft,gft2)
##    
##    

















    
