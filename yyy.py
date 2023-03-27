from optionprice import Option



for x in range(5,22,1):
    
    
    some_option = Option(european=False,
                        kind='call',
                        s0=666+x,
                        k=635,
                        t=4,
                        sigma=0.49,
                        r=0.05,
                        dv=0)
    price = some_option.getPrice()
    print(x,price.round(2))
