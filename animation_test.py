import yfinance as yf
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

# loading the data
indices = ["^GSPC","tsla", ]
data = yf.download(indices,start='2021-01-01')
data = data[['Close','Open']]
inv_growth = data['Open']

print(inv_growth,data )

## plotting the data

fig, ax = plt.subplots()

ax.set_xlim(inv_growth.index[0], inv_growth.index[-1])
ax.set_ylim(940, 1100)

line, = ax.plot(inv_growth.index[0], 1000)

x_data = []
y_data = []

def animation_frame(date):
    x_data.append(date)
    y_data.append(inv_growth.loc[date])
    
    line.set_xdata(x_data)
    line.set_ydata(y_data)
    
    return (line)

animation = FuncAnimation(fig, 
                          func=animation_frame, 
                          frames=list(data['Close'].index), 
                          interval = 10)
plt.show()
