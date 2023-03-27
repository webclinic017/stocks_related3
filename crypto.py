import ccxt
##print(ccxt.exchanges) # print a list of all available exchange classes
i=0
for x in ccxt.exchanges:
    print(i,'   ',x)
    i=i+1
