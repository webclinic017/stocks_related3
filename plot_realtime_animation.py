##import numpy as np
##from matplotlib import pyplot as plt
##from matplotlib import animation
##import yfinance as yf
##import pandas as pd
##
##ticker='tsla'
##
##df = yf.download(ticker, period='65d', interval='1d',prepost = True)
##df=pd.DataFrame(df)
##
##df.reset_index(inplace=True,drop=False)
##
##fig = plt.figure()
##ax = plt.axes(xlim=(), ylim=(-2, 2000))
##
##line, = ax.step([], [])
##
##def init():
##    line.set_data([], [])
##    return line,
##
##def animate(i):
##    x = df['Date'].loc[i]
##    y = df['Close'].loc[i]
##    line.set_data(x, y)
##    return line,
##
##anim = animation.FuncAnimation(fig, animate, init_func=init,
##                               frames=100, interval=20, blit=True)
##
##
##
##plt.show()

import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import yfinance as yf
import pandas as pd

ticker='btc-usd'

df = yf.download(ticker, period='30m', interval='1m',prepost = True)
df=pd.DataFrame(df)

df.reset_index(inplace=True,drop=False)

plt.style.use('fivethirtyeight')

##x_vals = [0, 1, 2, 3, 4, 5]
##y_vals = [0, 1, 3, 2, 3, 5]

x_vals=df['Datetime']
y_vals=df['Close']

df.set_index('Datetime',inplace=True)



plt.plot(x_vals, y_vals)


index = count()

def animate(i):    
    x_vals.append(next(index))
    y_vals.append(random.randint(0, 5))


    plt.plot(x_vals,y_vals) 


ani=FuncAnimation(plt.gcf(),animate, interval=1, repeat=True)
plt.xticks(rotation = 45)
plt.tight_layout()
plt.xticks(fontsize=9)
plt.yticks(fontsize=9)

plt.grid(True)
plt.show()

