
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import numpy as np

# Create a Figure with 2 rows and 2 columns of subplots:

fig, ax = plt.subplots(6, 2,sharex=False)

x = np.linspace(0, 15, 10)
print(x)

# Index 4 Axes arrays in 4 subplots within 1 Figure: 

k=0
for x2 in range(0,6,1):
    ax[x2, 0].plot(x, x/2, 'g',label='j') #row=0, column=0
    ax[x2, 1].plot(x, x/.4*x, 'r',label='j') #row=0, column=0
    ax[x2,0].grid()
    ax[x2,1].grid()
    ax[x2,0].vlines(5,0,(x/2).max(),'r')
    ax[x2,1].vlines(5,0,(x/.4*x).max(),'r')

plt.show()




'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import numpy as np

# Create a Figure with 2 rows and 2 columns of subplots:
fig, ax = plt.subplots(4, 2,sharex=False)

x = np.linspace(0, 5, 10)
print(x)

# Index 4 Axes arrays in 4 subplots within 1 Figure: 
ax[0, 0].plot(x, np.sin(x), 'g',label='j') #row=0, column=0
ax[1, 0].plot(range(100), 'b',label='76') #row=1, column=0
ax[0,0].axhline(0.5)
ax[0,0].axvline(2,-1,1,linewidth=4, color='r')
ax[1,0].axvline(2,-1,1,linewidth=4, color='r')
ax[0,0].can_zoom()
ax[0,0].get_legend()
ax[0,0].grid()


ax[0, 1].plot(x, np.cos(x), 'r') #row=0, column=1
ax[1, 1].plot(x, np.tan(x), 'k') #row=1, column=1
ax[0,1].axvline(2,-1,1)
ax[1,1].axvline(2,-1,1)

ax[2, 0].plot(x, np.tan(x), 'k') #row=1, column=1
ax[2, 1].plot(x, np.tan(x), 'k') #row=1, column=1
ax[2,0].axvline(2,-1,1)
ax[2,1].axvline(2,-1,1)

ax[3, 0].plot(x, np.tan(x), 'k') #row=1, column=1
ax[3, 1].plot(x, np.tan(x), 'k') #row=1, column=1
ax[3,0].axvline(2,-1,1)
ax[3,1].axvline(2,-1,1)
plt.show()








##import numpy as np
##import matplotlib.pyplot as plt
##
##def main():
##    nrows = 12
##    fig, axes = plt.subplots(nrows, 2)
##
##    for row in axes:
##        x = np.random.normal(0, 1, 100).cumsum()
##        y = np.random.normal(0, 0.5, 100).cumsum()
##        print(row,'ddd')
##        plot(row,x, y)
##
##    plt.show()
##
##def plot(axrow, x, y):
##    axrow[0].plot(x, color='red')
##    axrow[1].plot(y, color='green')
##
##main()
'''
