import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

x = np.arange(335)
y = np.exp(x)
z1=x.max()
z2=y.max()
###################################
fig1, ax1 = plt.subplots()
ax1.plot(x, y)
ax1.set_title("Axis 1 title")
ax1.set_xlabel("X-label for axis 1")
w = np.cos(x)
ax1.plot(x, w) # can continue plotting on the first axis
z = np.sin(x)
ax1.set_title('first plot')

ax1.get_ygridlines()


ax1.set_ylabel("y1")

ax1.tick_params(axis='y', labelcolor='tab:blue') 
ax1.tick_params(axis='y', labelcolor='tab:red')
ax1.text(x[1],y[1], 'Some text here', horizontalalignment='left')

##ax1.annotate('pixel offset from axes fraction',xy=(30,3), xycoords='axes fraction',xytext=(5, 5),
##textcoords='offset pixels',horizontalalignment='right',verticalalignment='bottom')
##ax1.set_adjustable(adjustable)
              
##ax1.annotate('figure pixels',
##            xy=(5, 5), xycoords='azhar stupid',xytext=(5, 5),textcoords='offset pixels')
ax1.annotate('axes fraction',
            xy=(x[2], y[2]), xycoords='data',
            xytext=(0.8, 0.95), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')

##################################
fig2, (ax2, ax3) = plt.subplots(nrows=2, ncols=1) # two axes on figure
ax2.plot(x, z)
ax3.plot(x, -z)
ax2.set_title('2nd plot')
ax2.annotate('axes fraction',
            xy=(x[2], -z[2]), xycoords='data',
            xytext=(0.8, 0.95), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')

ax2.text(x[1],z[1], 'Some text here', horizontalalignment='left')

##ax1.annotate('pixel offset from axes fraction',xy=(30,3), xycoords='axes fraction',xytext=(5, 5),
##textcoords='offset pixels',horizontalalignment='right',verticalalignment='bottom')
##ax1.set_adjustable(adjustable)
              
##ax1.annotate('figure pixels',
##            xy=(5, 5), xycoords='azhar stupid',xytext=(5, 5),textcoords='offset pixels')
ax2.annotate('axes fraction',
            xy=(x[2], z[2]), xycoords='data',
            xytext=(0.8, 0.95), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
##################################
fig1, ax4 = plt.subplots()
ax4.plot(x, y)
ax4.set_title("Axis 1 title")
ax4.set_xlabel("X-label for axis 1")
w = np.cos(x)
ax4.plot(x, w) # can continue plotting on the first axis
z = np.sin(x)
ax4.set_title('3rd plot')
ax4.text(x[1],y[1], 'Some text here', horizontalalignment='left')

##ax1.annotate('pixel offset from axes fraction',xy=(30,3), xycoords='axes fraction',xytext=(5, 5),
##textcoords='offset pixels',horizontalalignment='right',verticalalignment='bottom')
##ax1.set_adjustable(adjustable)
              
##ax1.annotate('figure pixels',
##            xy=(5, 5), xycoords='azhar stupid',xytext=(5, 5),textcoords='offset pixels')
ax4.annotate('axes fraction',
            xy=(x[2], y[2]), xycoords='data',
            xytext=(0.8, 0.95), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
##################################
plt.show()
