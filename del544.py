##
##import numpy as np
##import matplotlib.pyplot as plt
##from matplotlib.animation import FuncAnimation
##fig = plt.Subplot(ax1)
####fig, (ax,ay) = plt.subplots()
##ax1, ax2 = fig.subplots(2, 1, sharey=True,sharex=True)
##xdata, ydata = [], []
##xdata2,ydata2= [], []
##ln, = plt.plot([], [], 'ro') 
##ln2, = plt.plot([], [], 'ro')
##
##def init():
##    ax.set_xlim(0, 2*np.pi)
##    ax.set_ylim(-1, 1)
##    return ln,ln2
##
##def update(frame):
##    xdata.append(frame)
##    ydata.append(np.sin(frame))
##    ln.set_data(xdata, ydata)
##
##    xdata2.append(frame)
##    ydata2.append(np.cos(frame))
##    ln2.set_data(xdata2,ydata2)
##    
##    return ln,ln2
##
##ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
##                    init_func=init, blit=True)
##
##
##plt.show()
import matplotlib.pyplot as plt

##p1 = real_stock_price_volume[:,0]
##v1 = real_stock_price_volume[:,1]
##p2 = predicted_stock_price_volume[:,0]
##v2 = predicted_stock_price_volume[:,1]
##
plt.figure(1)
##plt.plot(p1, color = 'red', label = 'p1')
plt.title('Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Stock Price')

plt.figure(2)
##plt.plot(v1, color = 'brown', label = 'v1')
plt.title('Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Stock Price')

plt.figure(3)
##plt.plot(p2, color = 'blue', label = 'p2')
plt.title('Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Stock Price')

plt.figure(4)
##plt.plot(v2, color = 'green', label = 'v2')
plt.title('Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.legend()

plt.show()
