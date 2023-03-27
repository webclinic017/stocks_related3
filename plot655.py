import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np

# library to get stock data
import ffn

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

fig = plt.figure()

gs1 = gridspec.GridSpec(5, 5)
countries = ["Country " + str(i) for i in range(1, 26)]
axs = []
for c, num in zip(countries, range(1,26)):
    axs.append(fig.add_subplot(gs1[num - 1]))
    axs[-1].plot([1, 2, 3], [1, 2, 3])

plt.show()
##fig=plt.figure(figsize=(15, 6),facecolor='w', edgecolor='k')
##for i in range(10):
##
##    #this part is just arranging the data for contourf 
##    ind2 = py.find(zz==i+1)
##    sfr_mass_mat = np.reshape(sfr_mass[ind2],(pixmax_x,pixmax_y))
##    sfr_mass_sub = sfr_mass[ind2]
##    zi = griddata(massloclist, sfrloclist, sfr_mass_sub,xi,yi,interp='nn')
##
##
##    temp = 251+i  # this is to index the position of the subplot
##    ax=plt.subplot(temp)
##    ax.contourf(xi,yi,zi,5,cmap=plt.cm.Oranges)
##    plt.subplots_adjust(hspace = .5,wspace=.001)
##
##    #just annotating where each contour plot is being placed
##    ax.set_title(str(temp))

plt.show()    
