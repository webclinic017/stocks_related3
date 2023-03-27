# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

import matplotlib.animation as ani
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
import pandas as pd
import datetime as dt
import sys

#############
##data = np.loadtxt("example.txt", delimiter=",")
ticker='tsla'

df = yf.download(ticker, period='300d', interval='1d',prepost = True)
df=pd.DataFrame(df)
##df=df['Close']
df.index = pd.to_datetime(df.index)
print(df['Close'].index)
##df.reset_index(inplace=True)
##pp=[]
##for x in df.index:
##    df['Date'].loc[x]=str(df['Date'].loc[x]).split(' ')[0].strip(' ')
##    pp.append(df['Date'].loc[x])
##z=df.shape[0]
##
##df=(df[['Date','Close']])
print(df.columns)
df=df[['Close']]


fig, axes = plt.subplots(ncols=1)
plt.xticks(rotation=45, ha="right", rotation_mode="anchor") #rotate the x-axis values
plt.subplots_adjust(bottom = 0.2, top = 0.9) #ensuring the dates (on the x-axis) fit in the screen
plt.ylabel('Stock')
plt.xlabel('Dates')
plt.grid(True)
plt.ylim((df['Close'].min(),df['Close'].max()))

##print(df)
##print(df.iloc[:,0])
################
##x = df.iloc[:,0]
##x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in pp]
##
##df["Date"] = pd.to_datetime(df["Date"])

##print(df['Date'][0])
##print(df['Date'].iloc[-1])
##
##xx=pd.date_range(start=df['Date'][0],end=df['Date'].iloc[-1]). to_pydatetime().tolist()
##
##x=xx
##y = df.iloc[:,1]
####print(y)
##fig = plt.figure()
##ax = fig.add_subplot(111)
##line, = ax.plot([],[], '-')
##line2, = ax.plot([],[],'--')
##ax.set_xlim(np.min(df['Date']), np.max(df['Date']))
##ax.set_ylim(np.min(df['Close']), np.max(df['Close']))
##plt.xticks(rotation=45, ha="right", rotation_mode="anchor") #rotate the x-axis values

##
##def animate(i,factor):
##    line.set_xdata(x[:i])
##    line.set_ydata(y[:i])
##    line2.set_xdata(x[:i])
##    line2.set_ydata(factor*y[:i])
##    return (line,line2)
##
##
##
##K = 0.75 # any factor 
####ani = animation.FuncAnimation(fig, animate, frames=len(x), fargs=(K,),interval=1, blit=True)
##ani = animation.FuncAnimation(fig, animate, np.arange(1, len(y[0])),
##                              interval=1, blit=True, init_func=init)
##plt.show()



def buildmebarchart(i=int):
    plt.legend(df.columns)
    p = plt.plot(df[:i].index, df[:i].values) #note it only returns the dataset, up to the point i
##    for i in range(0,4):
##        p[i].set_color(color[i]) #set the colour of each curve

import matplotlib.animation as ani
animator = ani.FuncAnimation(fig, buildmebarchart, interval = 0)
plt.show()
