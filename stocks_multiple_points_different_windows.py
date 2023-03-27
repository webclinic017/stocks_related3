import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

import matplotlib.animation as ani
import matplotlib.pyplot as plt2
import numpy as np
import pandas as pd
import yfinance as yf
import pandas as pd
import datetime as dt
import sys
import Technicals
from Technicals import Techinicalsbb
#################################################################
ticker='^gspc'

df = yf.download(ticker, period='2100d', interval='1d',prepost = False)
df=pd.DataFrame(df)

##df=df['Close']
##df.index = pd.to_datetime(df.index)


##dfp=dfpp[['close','vwap','EMA_50','EMA_10','EMA_21','SAR','EMA_100','EMA_200']]


df=df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]
df.columns=['open', 'high', 'low', 'close', 'adj Close', 'volume']
df=Technicals.Techinicalsbb(df)
df=df[['close','vwap','EMA_50','EMA_10','EMA_21','SAR','EMA_100','EMA_200','EMA_5','volume','SAR']]

pd.to_datetime(df.index)
x=df.index
y=df['close']
y2=df['vwap']
y3=df['EMA_5']
y4=df['EMA_10']
y5=df['EMA_21']
y6=df['EMA_50']
y7=df['EMA_100']
y8=df['EMA_200']
y9=df['SAR']

#####################################################################


amp = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
amp.suptitle('black')

gg, = ax.step([], [],color='black')

def init():
    gg.set_data([], [])
    return gg,

def animate(i):
    x=df.index
    y=df['close']
    y2=df['vwap']
    y3=df['EMA_5']
    y4=df['EMA_10']
    y5=df['EMA_21']
    y6=df['EMA_50']
    y7=df['EMA_100']
    y8=df['EMA_200']
    y9=df['SAR']
    
##    x = np.linspace(0, 2, 10)
##    y = np.sin(2 * np.pi * (x - 0.01 * i))
    gg.set_data(x, y)
    return gg,

################################################
amp2 = plt.figure()
amp2.suptitle('green')
ax2 = plt.axes(xlim=(0, 2), ylim=(-2, 2))

gg2, = ax2.step([], [],color='g')

def init2():
    gg2.set_data([], [])
    return gg2,

def animate2(i):
    x = np.linspace(0, 2, 10)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    gg2.set_data(x, y)
    return gg2,

################################################
amp3 = plt.figure()
amp3.suptitle('red')
ax3 = plt.axes(xlim=(0, 2), ylim=(-2, 2))

gg3, = ax3.step([], [], color='r')

def init3():
    gg3.set_data([], [])
    return gg3,

def animate3(i):
    x = np.linspace(0, 2, 10)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    gg3.set_data(x, y)
    return gg3,





anim2 = animation.FuncAnimation(amp, animate, init_func=init,
                               frames=100, interval=20, blit=True)


anim3 = animation.FuncAnimation(amp2, animate2, init_func=init2,
                               frames=100, interval=20, blit=True)


anim4 = animation.FuncAnimation(amp3, animate3, init_func=init3,
                               frames=100, interval=20, blit=True)

plt.show()




