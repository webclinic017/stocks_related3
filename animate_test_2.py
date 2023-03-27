import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import numpy as np
import pandas as pd
import yfinance as yf



ticker='tsla'

df = yf.download(ticker, period='50d', interval='1d',prepost = True)
df=pd.DataFrame(df)
##df=df['Close']
df.index = pd.to_datetime(df.index)
df.reset_index(inplace=True)
print(df)
data=df
##data = np.loadtxt("example.txt", delimiter=",")
x = data.iloc[:,0]
y = data.iloc[:,1]

fig = plt.figure()
ax = fig.add_subplot(111)
line, = ax.plot([],[], '-')
line2, = ax.plot([],[],'--')
##ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(np.min(y), np.max(y))

def animate(i,factor):
    line.set_xdata(x[:i])
    line.set_ydata(y[:i])
    line2.set_xdata(x[:i])
    line2.set_ydata(factor*y[:i])
    return line,line2

K = 0.75 # any factor 
ani = animation.FuncAnimation(fig, animate, frames=len(x), fargs=(K,),
                              interval=100, blit=True)
plt.show()

'''
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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
##import Technicals
##from Technicals import Techinicalsbb

#############
##data = np.loadtxt("example.txt", delimiter=",")
ticker='tsla'

df = yf.download(ticker, period='50d', interval='1d',prepost = True)
df=pd.DataFrame(df)
##df=df['Close']
df.index = pd.to_datetime(df.index)
print(df['Close'].index,'   ',df['Close'])

dfp=df
##print(df.columns)
df=df[['Close','Low']]


plt.style.use('fivethirtyeight')

fig=plt.figure()
ax1=fig.add_subplot(1,1,1)

def animate(i):
    xs=[]
    ys=[]
    i2=dfp.columns.get_loc('Close')
    plt.plot(dfp['Close'].index, dfp['Close'].values,'-', lw = 2,color='b')

    


ani=animation.FuncAnimation(fig,animate,interval=1000)
plt.show()















x_vals = []
y_vals = []

index = count()


def animate(i):

    x = df['Close'].index
    y1 = df['Close']
    y2 = df['Low']

    plt.cla()

    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()    
'''
