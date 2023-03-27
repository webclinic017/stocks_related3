import numpy as np
import pandas as pd
import cryptocompare as cc
# list of coins
##coin_list = cc.get_coin_list()
##coins = sorted(list(coin_list.keys()))
##print(coins)
from cryptocompare import price as p
print(p.coin_snapshot('btc', 'usd'))
