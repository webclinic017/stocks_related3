# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

fig, (ax, ax1) = plt.subplots(1, 2)
plt.subplots_adjust(bottom = 0.25)
t = np.arange(0.0, 1.0, 0.001)
a0 = 5
f0 = 3
delta_f = 5.0
s = a0 * np.sin(2 * np.pi * f0 * t)
ax.plot(t, s, lw = 2, color = 'green')

ax1.plot(t, s, lw = 2, color = 'green')
ax1.margins(0.005)

ax.set_title("Without margin() Function")
ax1.set_title("With margin value = 0")

fig.suptitle('matplotlib.axes.Axes.margins() function \
Example\n', fontweight ="bold")
fig.canvas.draw()
plt.show()

