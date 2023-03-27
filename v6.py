import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 2, 0.01)
y1 = np.sin(2 * np.pi * x)
y2 = 1.2 * np.sin(4 * np.pi * x)




##fig, (ax, ax1) = plt.subplots(2, 1, sharex=True)
##ax.plot(x, y1, x, y2, color='black')
##ax.fill_between(x, y1, y2, where=y2 >= y1, facecolor='green', interpolate=True)
##ax.fill_between(x, y1, y2, where=y2 <= y1, facecolor='red', interpolate=True)
##ax.set_title('fill between where')
##
### Test support for masked arrays.
##y2 = np.ma.masked_greater(y2, 1.0)
##ax1.plot(x, y1, x, y2, color='black')
##ax1.fill_between(x, y1, y2, where=y2 >= y1,
##                 facecolor='green', interpolate=True)
##ax1.fill_between(x, y1, y2, where=y2 <= y1,
##                 facecolor='red', interpolate=True)
##ax1.set_title('Now regions with y2>1 are masked')

plt.show(y2,y1)
