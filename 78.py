import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import yfinance as yf
import pandas as pd
import sys

ticker=['tsla','t']
##ticker='tsla'

df = yf.download(ticker, period='100d', interval='1d',prepost = True)
df=pd.DataFrame(df)
df=df['Close']
##df_interest = df['Close']
##df1=df_interest
df.reset_index(inplace=True)
df.index = pd.to_datetime(df.index)


def data_gen():
##    t = data_gen.t
    x = 0
    while x < df.index:
        x+=1
        t += 0.05
        y1 = df['tsla'].loc[x]
        y2 = df['t'].loc[x]
##        print(y1,'   y1')
        # adapted the data generator to yield both sin and cos
        yield  y1, y2



# create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2,1)

# intialize two line objects (one in each axes)
line1, = ax1.plot([], [], lw=2)
line2, = ax2.plot([], [], lw=2, color='r')
line = [line1, line2]

##ax1.set_ylim(df.TSLA.min(),df.TSLA.max())
##ax2.set_ylim(df.T.min(),df.T.max())
##ax1.set_ylim(auto=True)
##ax2.set_ylim(auto=True)

# the same axes initalizations as before (just now we do it for both of them)
##for ax in [ax1, ax2]:
####    print(ax1)
####    if ax == ax1:
##    ax.set_ylim(df.TSLA.min(),df.TSLA.max())
####    if ax == ax2:
####    ax.set_ylim(df.T.min(),df.T.max())
##        
####    ax.set_xlim(df.index.min(),df.index.max())
##    ax.grid()

##sys.exit()
# initialize the data arrays 
xdata, y1data, y2data = [], [], []
def run(data):
    # update the data
    t, y1, y2 = data
    print(t,'ooooooooooooooooooooooooooooooooooooo')
    y1data.append(y1)
    y2data.append(y2)

    # axis limits checking. Same as before, just for both axes
    for ax in [ax1, ax2]:
        xmin, xmax = ax.get_xlim()
        if t >= xmax:
            ax.set_xlim(xmin, 2*xmax)
            ax.figure.canvas.draw()

    # update the data of both line objects
    line[0].set_data(xdata, y1data)
    line[1].set_data(xdata, y2data)

    return line

ani = animation.FuncAnimation(fig, run, data_gen, blit=True, interval=10,
    repeat=False)
plt.show()            
