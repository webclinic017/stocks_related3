import yfinance as yf
import pandas as pd
import talib as taa
import finta as f
from numerize import numerize
from termcolor import colored as cl
##import pandas_ta as ta2

import pandas_ta as ta
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
from matplotlib.axis import Axis
from matplotlib.widgets import Slider, Button, RadioButtons 
import numpy as np    
import sys
import warnings
from math import floor

warnings.filterwarnings("ignore")


pd.options.display.float_format = '{:.2f}'.format
pd.options.display.max_columns = 255
pd.options.display.max_rows = 6500000

##pd.options.display.max_rows = 999999
pd.options.display.max_columns = 76
pd.set_option("display.max_columns", 200)
pd.set_option('display.width', 1000)
pd.set_option('display.expand_frame_repr', False)


pd.options.display.float_format = '{:.2f}'.format
pd.options.display.max_columns = 255
pd.options.display.max_rows = 6500000

##pd.options.display.max_rows =999999 
##pd.options.display.max_columns = 36  ,'spy','msft','tsla','docu','mrna'
pd.set_option("display.max_columns", 100)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 200)
pd.set_option('display.max_columns', 0)
pd.set_option('display.max_columns', None)
pd.set_option("expand_frame_repr", True)



##fg=open('/home/az2/66.txt','w+')
##file_path = '/home/az2/66.txt'
##sys.stdout = open(file_path, "w")


def inputs(df):
    buy_condition=(df['EMA-35'].loc[x] > 0) 
##    fg.write(buy_condition)
    return(buy_condition)


def inputs2(df):
    sell_condition=(df['EMA-35'].loc[z] < 0)
##    fg.write(sell_condition)
    return(sell_condition)

def get_adx(high, low, close, lookback):
    plus_dm = high.diff()
    minus_dm = low.diff()
    plus_dm[plus_dm < 0] = 0
    minus_dm[minus_dm > 0] = 0
    
    tr1 = pd.DataFrame(high - low)
    tr2 = pd.DataFrame(abs(high - close.shift(1)))
    tr3 = pd.DataFrame(abs(low - close.shift(1)))
    frames = [tr1, tr2, tr3]
    tr = pd.concat(frames, axis = 1, join = 'inner').max(axis = 1)
    atr = tr.rolling(lookback).mean()
    
    plus_di = 100 * (plus_dm.ewm(alpha = 1/lookback).mean() / atr)
    minus_di = abs(100 * (minus_dm.ewm(alpha = 1/lookback).mean() / atr))
    dx = (abs(plus_di - minus_di) / abs(plus_di + minus_di)) * 100
    adx = ((dx.shift(1) * (lookback - 1)) + dx) / lookback
    adx_smooth = adx.ewm(alpha = 1/lookback).mean()
    return plus_di, minus_di, adx_smooth

def get_miss(df,loopback):
    df['vzo']=f.TA.VZO(df,loopback)
    return(df['vzo'])

def Trend(df):
   df['55MA']=df['Close'].rolling(55).mean()
   df['Distance to 55SMA in ATR']=(df['Close']-df['55MA'])/df['ATR']
   df['Accumulated Distance']=df['Distance to 55SMA in ATR'].rolling(132).sum()
   df['Absolute AD']=abs(df['Accumulated Distance'])
   df['Max AD']=df['Absolute AD'].rolling(132).max()
   df['TrendSign']=df['Accumulated Distance'].apply(lambda x: 1 if x>0 else -1)
   df['Trend']= df['TrendSign']*(df['Absolute AD']/df['Max AD'])*100
   df['Trend']=df['Trend'].round()
   return(df)

##m=['ndx','spy','tsla']
##m=['tsla','spy','msft']
m=['tsla','spy','^dji','docu','msft','nvda','shop','mrna','f','googl','amzn','adbe','tmo','uso']
b=15
k=4
loopback=15
t3=0
t4=0
g7=0

for xs in m:
    
    df = yf.download(xs,period='1d',interval='1m')
    df['ticker']=xs
##    print(df,'    ',xs,'  55')

    df['Down_Trend']=''
    df['Up_Trend']=''
    df['signal']=''
    df['exit_signal']=''
##    df['highest']=''


    df['plus_di'] = pd.DataFrame(get_adx(df['High'], df['Low'], df['Close'], loopback)[0]).rename(columns = {0:'plus_di'})
     
    df['plus_di'] = pd.DataFrame(get_adx(df['High'], df['Low'], df['Close'], loopback)[0]).rename(columns = {0:'plus_di'})
    df['minus_di'] = pd.DataFrame(get_adx(df['High'], df['Low'], df['Close'], loopback)[1]).rename(columns = {0:'minus_di'})
    df['adx'] = pd.DataFrame(get_adx(df['High'], df['Low'], df['Close'], loopback)[2]).rename(columns = {0:'adx'})
    df['x']=((df['plus_di']-df['minus_di']))
    df['vzo'] = f.TA.VZO(df,loopback)
    df['Boling_upper'], df['Boling_middle'], df['Boling_lower'] = taa.BBANDS(df['Close'], timeperiod=10, nbdevup=2, nbdevdn=2)




    st = ta.supertrend(df['High'], df['Low'], df['Close'], 7, 3)
    v = df['Volume'].values
    tp = (df['Low'] + df['Close'] + df['High']).div(3).values
    df = df.assign(vwap=(tp * v).cumsum() / v.cumsum())

    df['macd'], df['macdsignal'], df['macdhist'] = taa.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    df['AD'] = taa.ADOSC(df['High'], df['Low'], df['Close'], df['Volume'])
    df['adx'] = taa.ADX(df['High'], df['Low'], df['Close'], timeperiod=loopback)
    df['supertrend']=st.iloc[:,1]
    df['MOM'] = taa.MOM(df['Close'], timeperiod=loopback)
    df['STOCHRSI_fastk'], df['STOCHRSI_fastd'] = taa.STOCHRSI(df['Close'], timeperiod=3, fastk_period=5, fastd_period=3, fastd_matype=0)
    df['Close_vwap'] = df['Close'] - df['vwap']
    df['Close_vwap_slope']=df['Close_vwap']-df['Close_vwap'].shift(1)
    df['EMA_3'] = taa.EMA(df['Close'], timeperiod=3)
    df['EMA_5'] = taa.EMA(df['Close'], timeperiod=5)
    df['EMA_10'] = taa.EMA(df['Close'], timeperiod=10)
    df['Close_EMA3'] = df['Close'] - df['EMA_3']
    df['Close_EMA5'] = df['Close'] - df['EMA_5']
    df['Close_EMA10'] = df['Close'] - df['EMA_10']
    df['RSI']= taa.RSI(df['Close'], timeperiod=loopback)
    upmove=df['High']-df['High'].shift(1)
        
##    for x in df.index:
##        if df['supertrend'].loc[x] == 1 and df['x'].loc[x] > 0 and df['AD'].loc[x] > 0 and df['x'].loc[x]>0 and\
##           df['Close_vwap'].loc[x]>0  and (df['Boling_lower'].loc[x]-df['Boling_lower'].shift(1).loc[x])>0 and df['adx'].loc[x] > 25:
##            df['Up_Trend'].loc[x]='A'
##        elif df['supertrend'].loc[x] == -1 and df['x'].loc[x] < 0 and df['AD'].loc[x] < 0 and df['x'].loc[x]<0 and\
##             df['Close_vwap'].loc[x]<0 and (df['Boling_lower'].loc[x]-df['Boling_lower'].shift(1).loc[x])<0 and df['adx'].loc[x] > 25:
##            df['Down_Trend'].loc[x]='B'
##            

##    for x in df.index:
##        if (df['Boling_upper'].loc[x] - df['Boling_upper'].shift(1).loc[x]) > 0:
##            df['Up_Trend'].loc[x]='A'
##        elif (df['Boling_upper'].loc[x] - df['Boling_upper'].shift(1).loc[x]) > 0:
##            df['Down_Trend'].loc[x]='B'
##
##    print(df,'777 =========== ', xs)

    m='Close_EMA3'
    dfp=pd.DataFrame()
    ggs=0
    import sys
    df.reset_index(inplace=True)
    for x in df.index:
##        print(x)
        if df[m].loc[x]  > 0 and (df['vzo'].loc[x]  > -40 and (df['vzo'].shift(1).loc[x]-df['vzo'].loc[x] < 0))\
           and df['RSI'].loc[x] > 30 and (df['RSI'].loc[x] > df['RSI'].shift(1).loc[x]) and df['supertrend'].loc[x] == 1 and\
           df['x'].loc[x]>0 and df['MOM'].loc[x]>0 and df['macd'].loc[x]>0 :
            
            df['Up_Trend'].loc[x]='A'
            df['signal'].loc[x]='Buy'
            t3=df['Close'].loc[x]
            g7 = x
            
            break
##        print(t3,' 66666666666666666666666666') 
##        if df[m].loc[x]  > 0 and (df['vzo'].loc[x]  > -40 and (df['vzo'].shift(1).loc[x]-df['vzo'].loc[x] < 0))\
##           and df['RSI'].loc[x] > 30 and (df['RSI'].loc[x] > df['RSI'].shift(1).loc[x]) and df['supertrend'].loc[x] == 1 and\
##           df['x'].loc[x]>0 and df['MOM'].loc[x]>0 and df['macd'].loc[x]>0:
##            df['Up_Trend'].loc[x]='A'
##            df['signal'].loc[x]='Buy'
##            t3=df['Close'].loc[x]
##            g7 = x
##            
##            break

        

##        if ggs:    
##    for y in range(g7,df.shape[0]):

        
##    dfp=df['Close'].tail(3)
##    df['highest'] = dfp.cummax()
##    df['trailingstop'] = df['highest']*0.99
##    df['exit_signal'] = t3 < df['trailingstop']


        
##        print(,' 999 ======================================================')
        
##                print(y,df['x'].loc[y])

##        dfp = df['Close'].loc[y] #create price array
##        dfp=df.iloc[:y,df.columns.get_loc('Close')]
##        dfp['highest'] = dfp.cummax() #take the cumulative max
##        dfp['trailingstop'] = dfp['highest']*0.99 #subtract 1% of the max
##        df['Trailing_exit_signal'] = df['Close'] < dfp['trailingstop'] #generate exit signal

##    for y in range(g7,df.shape[0]):
####        dfp.loc[y]=df['Close'].loc[y]
##        d=df['Close'].tail(3)
##        print(d.cummax()*.99)
##        sys.exit()
##        df['highest'].loc[y] = d.cummax()
##        df['trailingstop'].loc[y] = d.cummax().loc[y]*0.99
##        df['exit_signal'].loc[y] = df['Close'].loc[y].cummax()
##        t3
##        < d.cummax().loc[y]*0.99
        
##        dfp.loc[y]=df['Close'].tail(3)
##        dfp['highest'].loc[y] = dfp.loc[y].cummax()
##        dfp['trailingstop'].loc[y] = dfp['highest'].loc[y]*0.99
##        df['exit_signal'].loc[y] = t3 < dfp['trailingstop'].loc[y]
        if t3 > 0:
##            if df['supertrend'].loc[y] == -1 or df['macd'].loc[y] < 0 or df['MOM'].loc[y] < 0 \
##               or df['x'].loc[y] < 0 or df['macd'].loc[y] < 0 and df['exit_signal'] :
            if df['supertrend'].loc[y] == -1 :

    ##        if df['supertrend'].loc[y] == -1 or df['x'].loc[y]<0 or df['MOM'].loc[y]<0 or df['MOM'].loc[y]<0:                 
                df['signal'].loc[y]='Sell'
                t4=df['Close'].loc[y]
                break

            if t3==0:
                t4=0
    ##                    print(df['x'].loc[y],'===============================')
                break
     
    ##        break
##                
##        if (df[m].loc[x]) < 0 and df['RSI'].loc[x] > 70 and (df['RSI'].loc[x] < df['RSI'].shift(1).loc[x]) and \
##             df['supertrend'].loc[x] == -1 and df['x'].loc[x] < 0:
##            
##            df['Down_Trend'].loc[x]='B'
####            df['signal'].loc[x]='Sell'

    print(df,'777 =========== ', xs)
    print('\n')

    if t3 > 0 and t4 > 0:
        print('profit=',round((t4-t3),2),'    ',xs,'  ',df.signal.unique())

    ########## trailing stop ##############
##    dfp = df['Close'] #create price array
##    dfp['highest'] = dfp.cummax() #take the cumulative max
##    dfp['trailingstop'] = dfp['highest']*0.99 #subtract 1% of the max
##    df['Trailing_exit_signal'] = df['Close'] < dfp['trailingstop'] #generate exit signal
##
##
##





    
    
##    dfm=Trend(df)
##    print(dfm,' amend ',xs)
    
##aapl['minus_di'] = pd.DataFrame(get_adx(aapl['high'], aapl['low'], aapl['close'], 14)[1]).rename(columns = {0:'minus_di'})
##aapl['adx'] = pd.DataFrame(get_adx(aapl['high'], aapl['low'], aapl['close'], 14)[2]).rename(columns = {0:'adx'})
df = df.dropna()
##aapl.tail()
########################################################################################
import seaborn as sns

sns.set(style='darkgrid')


df['Up_Trend']=''
for x in df.index:
    #   Trend graph
    if df['x'].loc[x] > 0:
##        df['Up_Trend'].loc[x]=df['Close'].loc[x]+20
        df['Up_Trend'].loc[x]=50
    elif df['x'].loc[x] < 0:
##        df['Up_Trend'].loc[x]=df['Close'].loc[x]+20
        df['Up_Trend'].loc[x]=-50



##########################################################################################
ax1 = plt.subplot2grid((11,1), (0,0), rowspan = 5, colspan = 1)
ax2 = plt.subplot2grid((11,1), (6,0), rowspan = 5, colspan = 1)


ax1.plot(df['Close'], linewidth = 2, color = '#ff9800')
ax1.set_title('df CLOSING PRICE')
ax2.plot(df['plus_di'], color = '#26a69a', label = '+ DI 14', linewidth = 3, alpha = 0.3)
ax2.plot(df['minus_di'], color = '#f44336', label = '- DI 14', linewidth = 3, alpha = 0.3)
ax2.plot(df['x'], color = '#26a69a', label = 'x', linewidth = 7, alpha = 0.3)

##ax3.plot(df['supertrend'], color = '#26a69a', label = 'x', linewidth = 7, alpha = 0.3)
##ax2.bar(df['Datetime'], df['macd'], width=1, color='g')

ax2.axhline(0, color = 'grey', linewidth = 2, linestyle = '--')
for x in df.index:
    if df['x'].loc[x] > 0 and df['x'].shift(1).loc[x] < 0:
        ax2.axvline(x,  ymin=-50, ymax=50, color = 'green', linewidth = 2)
        ax1.axvline(x,  ymin=-50, ymax=50, color = 'green', linewidth = 2)
        
    if df['x'].loc[x] < 0 and df['x'].shift(1).loc[x] > 0:
        ax2.axvline(x,  ymin=-50, ymax=50, color = 'red', linewidth = 2)
        ax1.axvline(x,  ymin=-50, ymax=50, color = 'red', linewidth = 2)
        
ax2.plot(df['adx'], color = '#2196f3', label = 'ADX 14', linewidth = 3)
ax2.axhline(25, color = 'grey', linewidth = 2, linestyle = '--')
ax2.legend()
ax2.set_title('df ADX 14')
plt.show()
##lisinopril
#tropol/metaproxil
# https://stackoverflow.com/questions/56861966/trailing-stop-loss-on-pandas-dataframe


############################################################################################################
def implement_adx_strategy(prices, pdi, ndi, adx):
    buy_price = []
    sell_price = []
    adx_signal = []
    signal = 0
    
    for i in range(len(prices)):
        if adx[i-1] < 25 and adx[i] > 25 and pdi[i] > ndi[i]:
            if signal != 1:
                buy_price.append(prices[i])
                sell_price.append(np.nan)
                signal = 1
                adx_signal.append(signal)
            else:
                buy_price.append(np.nan)
                sell_price.append(np.nan)
                adx_signal.append(0)
        elif adx[i-1] < 25 and adx[i] > 25 and ndi[i] > pdi[i]:
            if signal != -1:
                buy_price.append(np.nan)
                sell_price.append(prices[i])
                signal = -1
                adx_signal.append(signal)
            else:
                buy_price.append(np.nan)
                sell_price.append(np.nan)
                adx_signal.append(0)
        else:
            buy_price.append(np.nan)
            sell_price.append(np.nan)
            adx_signal.append(0)
            
    return buy_price, sell_price, adx_signal

buy_price, sell_price, adx_signal = implement_adx_strategy(df['Close'], df['plus_di'], df['minus_di'], df['adx'])

ax1 = plt.subplot2grid((11,1), (0,0), rowspan = 5, colspan = 1)
ax2 = plt.subplot2grid((11,1), (6,0), rowspan = 5, colspan = 1)
ax1.plot(df['Close'], linewidth = 3, color = '#ff9800', alpha = 0.6)
ax1.set_title('AAPL CLOSING PRICE')
ax1.plot(df.index, buy_price, marker = '^', color = '#26a69a', markersize = 14, linewidth = 0, label = 'BUY SIGNAL')
ax1.plot(df.index, sell_price, marker = 'v', color = '#f44336', markersize = 14, linewidth = 0, label = 'SELL SIGNAL')
##ax2.plot(df['plus_di'], color = '#26a69a', label = '+ DI 14', linewidth = 3, alpha = 0.3)
##ax2.plot(df['minus_di'], color = '#f44336', label = '- DI 14', linewidth = 3, alpha = 0.3)
##ax2.plot(df['adx'], color = '#2196f3', label = 'ADX 14', linewidth = 3)
ax2.axhline(25, color = 'grey', linewidth = 2, linestyle = '--')

ax2.plot(df['macd'], color = '#f44336', label = 'macd', linewidth = 3, alpha = 0.3)


ax2.legend()
ax2.set_title('AAPL ADX 14')
##plt.show()

position = []
for i in range(len(adx_signal)):
    if adx_signal[i] > 1:
        position.append(0)
    else:
        position.append(1)
        
for i in range(len(df['Close'])):
    if adx_signal[i] == 1:
        position[i] = 1
    elif adx_signal[i] == -1:
        position[i] = 0
    else:
        position[i] = position[i-1]
        
close_price = df['Close']
plus_di = df['plus_di']
minus_di = df['minus_di']
adx = df['adx']
adx_signal = pd.DataFrame(adx_signal).rename(columns = {0:'adx_signal'}).set_index(df.index)
position = pd.DataFrame(position).rename(columns = {0:'adx_position'}).set_index(df.index)

frames = [close_price, plus_di, minus_di, adx, adx_signal, position]
strategy = pd.concat(frames, join = 'inner', axis = 1)

strategy
strategy[25:30]

df_ret = pd.DataFrame(np.diff(df['Close'])).rename(columns = {0:'returns'})
adx_strategy_ret = []

for i in range(len(df_ret)):
    returns = df_ret['returns'][i]*strategy['adx_position'][i]
    adx_strategy_ret.append(returns)
    
adx_strategy_ret_df = pd.DataFrame(adx_strategy_ret).rename(columns = {0:'adx_returns'})
investment_value = 100000
number_of_stocks = floor(investment_value/df['Close'][-1])
adx_investment_ret = []

for i in range(len(adx_strategy_ret_df['adx_returns'])):
    returns = number_of_stocks*adx_strategy_ret_df['adx_returns'][i]
    adx_investment_ret.append(returns)

adx_investment_ret_df = pd.DataFrame(adx_investment_ret).rename(columns = {0:'investment_returns'})
total_investment_ret = round(sum(adx_investment_ret_df['investment_returns']), 2)
profit_percentage = floor((total_investment_ret/investment_value)*100)
print(cl('Profit gained from the ADX strategy by investing $100k in df : {}'.format(total_investment_ret), attrs = ['bold']))
print(cl('Profit percentage of the ADX strategy : {}%'.format(profit_percentage), attrs = ['bold']))


################################################3

'''
def get_benchmark(start_date, investment_value):
    spy = get_historical_data('SPY', start_date)['close']
    benchmark = pd.DataFrame(np.diff(spy)).rename(columns = {0:'benchmark_returns'})
    
    investment_value = investment_value
    number_of_stocks = floor(investment_value/spy[-1])
    benchmark_investment_ret = []
    
    for i in range(len(benchmark['benchmark_returns'])):
        returns = number_of_stocks*benchmark['benchmark_returns'][i]
        benchmark_investment_ret.append(returns)

    benchmark_investment_ret_df = pd.DataFrame(benchmark_investment_ret).rename(columns = {0:'investment_returns'})
    return benchmark_investment_ret_df

benchmark = get_benchmark('2020-01-01', 100000)

investment_value = 100000
total_benchmark_investment_ret = round(sum(benchmark['investment_returns']), 2)
benchmark_profit_percentage = floor((total_benchmark_investment_ret/investment_value)*100)
print(cl('Benchmark profit by investing $100k : {}'.format(total_benchmark_investment_ret), attrs = ['bold']))
print(cl('Benchmark Profit percentage : {}%'.format(benchmark_profit_percentage), attrs = ['bold']))
print(cl('ADX Strategy profit is {}% higher than the Benchmark Profit'.format(profit_percentage - benchmark_profit_percentage), attrs = ['bold']))

'''
