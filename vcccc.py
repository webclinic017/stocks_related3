import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.linspace(0,1,6)
y = [1,2,3,1.2,1.9,2.8]

fig = plt.figure()
plt.xlim(0, 4)
plt.ylim(0, 4)
graph, = plt.plot([], [], 'o')

def animate(i):
    graph.set_data(x[:i+1], y[:i+1])
    return graph

ani = FuncAnimation(fig, animate, frames=12, interval=20)
plt.show()
