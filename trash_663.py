###!/usr/bin/env python3
### -*- coding: utf-8 -*-
##"""
##Created on Wed Oct 23 22:17:44 2019
##
##@author: TysonU
##"""
##from plotly.offline import plot
##import plotly.graph_objects as go
##import random
##import pandas as pd
##
###Create random OHLC and Volume
##high = 40
##low = 20
##dev = 1
##days = 100
##
##fake_market = []
##for each in range(days):
##    ohlc = []
##    ohlc.append(each)
##    if each == 0:
##        o = random.randrange(low, high)
##        ohlc.append(o)
##    else:
##        ohlc.append(c) #I know
##    h = random.randrange(o, high)
##    ohlc.append(h)
##    l = random.randrange(low, o)
##    ohlc.append(l)
##    c = random.randrange(l, h)
##    ohlc.append(c)
##    fake_market.append(ohlc)
##
###Do all the plotly stuff
##fig = go.Figure(
##    data=[
##        go.Bar(
##            x=[str(x) for x in df2.Price.to_list()],
##            y=[str(x) for x in df2.Volume.to_list()],
##            orientation="h",
##            xaxis="x",
##            yaxis="y",
##            visible=True,
##            showlegend=False
##        ),
##        go.Candlestick(
##            x=[str(x) for x in df.Date.to_list()],
##            open=[str(x) for x in df.Open.to_list()],
##            high=[str(x) for x in df.High.to_list()],
##            low=[str(x) for x in df.Low.to_list()],
##            close=[str(x) for x in df.Close.to_list()],
##            xaxis="x2",
##            yaxis="y2",
##            visible=True,
##            showlegend=False
##        )
##    ],
##
##    layout=go.Layout(
##        title=go.layout.Title(text="Candlestick With Volume Profile"),
##        xaxis=go.layout.XAxis(
##            side="top",
##            range=[0, 300],
##            rangeslider=go.layout.xaxis.Rangeslider(visible=False),
##            showticklabels=False
##        ),
##        yaxis=go.layout.YAxis(
##            side="left",
##            range=[low, high],
##            showticklabels=False
##        ),
##        xaxis2=go.layout.XAxis(
##            side="bottom",
##            title="Date",
##            rangeslider=go.layout.xaxis.Rangeslider(visible=False),
##            overlaying="x"
##        ),
##        yaxis2=go.layout.YAxis(
##            side="right",
##            title="Price",
##            range=[low, high],
##            overlaying="y"
##        )
##    )
##)
##
##template = ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "none"]
##fig.update_layout(template=template[2])
##
##plot(fig)





import pandas as pd
import yfinance as yf
import pandas_ta as ta
import matplotlib.pyplot as plt
import numpy as np

x='nvda'
df=yf.download(x,start=pd.to_datetime('2022-05-20'),end=pd.to_datetime('2022-05-30'),interval='1d')
df.reset_index(inplace=True)





def custom_round(x, base=5):
    return int(base * round(float(x)/base))

def round_and_group(data,base=5):
    df = data[['Close', 'Volume']].copy()
    #Round to nearest X
    df['Close'] = df['Close'].apply(lambda x: custom_round(x, base=base))
    # Remove the date index
    df = df.set_index('Close')
    df = df.groupby(['Close']).sum()
    return df

##df=round_and_group(TTF,base=1)
df.reset_index(inplace=True)
plt.figure(figsize=(10,4), dpi=120) # 10 is width, 4 is height
ax1=plt.subplot(1,2,1)
plt.barh(df['Close'],df['Volume'], 2)
ax2= ax1.twiny()
candlestick2_ohlc(ax2,TTF['Open'],
                      TTF['High'],
                      TTF['Low'],
                      TTF['Close'],width = 0.6,colorup='g')
