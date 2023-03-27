
from optionprice import Option    
some_option = Option(european=True,
                    kind='put',
                    s0=15610,
                    k=15650,
                    t=1,
                    sigma=0.01,
                    r=0.05,
##                    dv=0
                     )

##print(some_option)
price = some_option.getPrice(method='BT',iteration = 1)
print(price)
##
####
####p=['53','55']
####for x in p:
####    print(x)
####    some_option()
##
##
##some_option = Option(european=False,
##                    kind='put',
##                    s0=809,  # stock price
##                    k=239,  # strike price
##                    t=12,
##                    sigma=48,  # vvolatility of stock
##                    r=0.05,  # risk free interest rate per annum
##                    dv=0)
##price = some_option.getPrice()
##print(price)
##some_option = Option(european=False,
##                    kind='call',
##                    s0=x,
##                    k=635,
##                    t=4,
##                    sigma=0.49,
##                    r=0.05,
##                    dv=0)
##
##
##some_option2 = Option(european=False,
##                    kind='call',
##                    s0=x,
##                    k=627.5,
##                    t=4,
##                    sigma=0.49,
##                    r=0.01,
##                    dv=0)

    ##Type:           European
    ##Kind:           call
    ##Price initial:  80
    ##Price strike:   120
    ##Volatility:     1.0%
    ##Risk free rate: 5.0%
    ##Start Date:     2020-03-24
    ##Expire Date:    2020-04-24
    ##Time span:      31.0 days



    ##print(some_option)




##p=['53','55']
##for x in p:
##    print(x)
##    price = some_option.getPrice()
##    price2 = some_option2.getPrice()
    

##    print(x,"vertical spread:" ,(price2-price).round(2))

'''
https://qsctech-sange.github.io/option-price#attributes

european	boolean	True if the option is an European option and False if it’s an American one.
kind	str	‘call’ for call option while ‘put’ for put option. Other strs are not valid.
s0	number	initial price
k	int	strike price
sigma	float	volatility of stock
r	float	risk free interest rate per annum
[optional] dv	float	dividend rate. 0 for non-stock option, which is also the default
[optional] t	int	length of option in days
[optional] start	str	beginning date of the option, string like ‘2008-02-14’,default today
[optional] end	str	end date of the option, string like ‘2008-02-14’,default today plus param t

'''
