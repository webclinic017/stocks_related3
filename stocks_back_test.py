import pandas as pd 
from tiingo import TiingoClient # for historical data
### for my technical indicators
from ta.momentum import RSIIndicator, stoch 
from ta.trend import MACD as md

client = TiingoClient({'api_key' : 'SECRET_API_KEY'})

datalist = ['NFLX', 'AAPL', 'GOOG']

data = client.get_dataframe(datalist,
                                    metric_name='adjClose',
                                      frequency='daily',
                                      startDate='2015-02-02',
                                      endDate='2020-10-10')

def RSI_base(data,ticker):
    MACD = md(close=data[ticker])
    data["MACD_diff"] = MACD.macd_diff()
    RSI = RSIIndicator(close=data[ticker])
    data["RSI"] = RSI.rsi()
    data["Buy_Signal"] = 0
    data["Sell_Signal"] = 0
    data["SL"] = 0 
    data["TP"] = 0
    data["Pos"] = 0
    data["TW"] = 0.0


    for i in range(0,len(data)):
        if data["Pos"][i-1] == 0:
            if data["RSI"].iloc[i] > 50 and data["MACD_diff"][i] > 0 and (data["Pos"][i] == 0):
                data["Buy_Signal"][i] = 1
                data["Pos"][i] = 1
                data["SL"][i] = (data[ticker][i]*0.97)
                data["TP"][i] = (data[ticker][i]*1.5)
            elif data["RSI"].iloc[i] < 50 and data["MACD_diff"][i] < 0 and (data["Pos"][i] == 0): 
                data["Buy_Signal"][i] = 1
                data["Pos"][i] = -1
                data["SL"][i] = (data[ticker][i]*1.03)
                data["TP"][i] = (data[ticker][i]*0.95)
            else:
                data["Buy_Signal"][i] = 0 
                data["Pos"][i] = 0

                        elif data["Pos"][i-1] == 1:
            data["SL"][i] = data["SL"][i-1] 
            data["TP"][i] = data["TP"][i-1]
            if (data[ticker][i] > data["SL"][i-1]) or (data[ticker][i] < data["TP"][i-1]):
                data["Pos"][i] = 1
            if (data[ticker][i] < data["SL"][i]) or (data[ticker][i] > data["TP"][i-1]):
                data["Pos"][i] = 0
                data["Sell_Signal"][i] = 1

            elif data["Pos"][i-1] == -1:
                data["SL"][i] = data["SL"][i-1] 
                data["TP"][i] = data["TP"][i-1]
                if (data[ticker][i] < data["SL"][i-1]) or (data[ticker][i] > data["TP"][i-1]):
                    data["Pos"][i] = -1
                if (data[ticker][i] > data["SL"][i]) or (data[ticker][i] < data["TP"][i-1]):
                    data["Pos"][i] = 0
                    data["Sell_Signal"][i] = 1


    for i in range(len(data)):
        if (data["Pos"][i] == 1): 
            data["TW"][i] = 1/len(datalist)
        elif (data["Pos"][i] == -1):
            data["TW"][i] = -(1/len(datalist))
        else:
            data["TW"][i] = 0

    weights = data["TW"]

    return weights

df = pd.DataFrame()

for i in datalist:
    temp = RSI_base(data,i)
    temp = temp.rename(i)
    df = pd.concat([df,temp],axis=1)

data = data[['NFLX', 'AAPL', 'GOOG']]
import bt
import matplotlib.pyplot as plt
import numpy as np

#create strategy
crosses = bt.Strategy('Test1', [bt.algos.WeighTarget(df),
                                    bt.algos.Rebalance()])

#create benchmark of buy-and-hold
long_only = bt.Strategy('Benchmark', [bt.algos.RunOnce(),
                        bt.algos.SelectAll(),
                        bt.algos.WeighEqually(),
                        bt.algos.Rebalance()])

#set backtests and commissions
t = bt.Backtest(crosses,data,commissions=lambda q, p: max(1, abs(q) * 0.05))
s = bt.Backtest(long_only, data,commissions=lambda q, p: max(1, abs(q) * 0.05))

report = bt.run(t,s)
plt.title("Portfolio Returns")
report.plot()

report.set_riskfree_rate(0.001)
report.display()
