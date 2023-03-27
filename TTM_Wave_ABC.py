import pandas as pd
####import talib as taa
####import finta as f
##from finta import TA 
import pandas_ta as taa
##from numerize import numerize
import yfinance as yf
##import pandas as pd
##import talib as taa
##import finta as f
##import pandas_ta as ta
import talib as taa
from numerize import numerize
import random
import matplotlib.pyplot as plt
import mplcursors
from matplotlib.widgets import Cursor
import matplotlib.pyplot as plt
##import decimal
##from matplotlib.ticker import MaxNLocator
##from mpl_toolkits.axes_grid1.inset_locator import mark_inset
##from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
import numpy as np
import sys
import numerize
from numerize import numerize
##import stackoverflow
##https://www.tradingview.com/script/nYOzTA1Y-UCS-TTM-Wave-A-B-C/
y=['ndx','spy']
df=yf.download('PYPL','2022-01-01','2024-03-30',prepost=True)


##// Created by UCSGEARS on 8/30/2014
##// Updated - 03/22/2014

##study(title="UCS_TTM_Wave A & B & C", shorttitle="WAVE-A/B/C", precision = 2)

##usewa = input(true, title = "Wave A", type=bool)
##usewb = input(true, title = "Wave B", type=bool)
##usewc = input(true, title = "Wave C", type=bool)


##// WAVE CALC
##// Wave A
df['fastMA1'] = taa.EMA(df['Close'], timeperiod=5)

df['slowMA1'] = taa.EMA(df['Close'], timeperiod=9)
df['macd1'] =  df['fastMA1'] - df['slowMA1'] 
df['signal1'] =  taa.EMA(df['macd1'], 9) 
df['hist1'] =  df['macd1'] - df['signal1']

df['fastMA2'] = taa.EMA(df['Close'], timeperiod=5)
df['slowMA2'] = taa.EMA(df['Close'], timeperiod=21)
df['macd2'] = df['fastMA2'] - df['slowMA2'] 
df['signal2'] = taa.EMA(df['macd2'], 21) 
df['hist2'] = df['macd2'] - df['signal2']

##// Wave C
df['fastMA5'] = taa.EMA(df['Close'], timeperiod=5)
df['slowMA5'] = taa.EMA(df['Close'], timeperiod=33)
df['macd5'] = df['fastMA5'] - df['slowMA5'] 
df['signal5'] = taa.EMA(df['macd5'], 33) 
df['hist5'] = df['macd5'] - df['signal5'] 

df['fastMA6'] = taa.EMA(df['Close'], timeperiod=5)
df['slowMA6'] = taa.EMA(df['Close'], timeperiod=37)
df['macd6'] = df['fastMA6'] - df['slowMA6']

print(df)
##// PLOTs
##plt.plot(df['macd6'], color=#FF0000, style=histogram, title="Wave C1", linewidth=3)
##plt.plot(df['hist5'], color=#FF8C00, style=histogram, title="Wave C2", linewidth=3)
##
##plt.plot(df['hist4'], color=#FF00FF, style=histogram, title="Wave B1", linewidth=3)
##plt.plot(df['hist3'], color=#0000FF, style=histogram, title="Wave B2", linewidth=3)
##
##plt.plot(df['hist2'], color=#008000, style=histogram, title="Wave A1", linewidth=3)
##plt.plot(df['hist1'], color=#DAA520, style=histogram, title="Wave A2", linewidth=3)

##    plt.hlines(nn+100,df.iloc[:,df.columns.get_loc('Date')].min(),df.iloc[:,df.columns.get_loc('Date')].max(), lw=1.0, color='teal',label='STOCHRSI_fastk 100')
##   

##plt.hline(0, color=black, title = "Zero Line", linewidth = 2, linestyle = solid)

