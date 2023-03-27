import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

amp = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))

gg, = ax.step([], [])

def init():
    gg.set_data([], [])
    return gg,

def animate(i):
    x = np.linspace(0, 2, 10)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    gg.set_data(x, y)
    return gg,

################################################
amp2 = plt.figure()
ax2 = plt.axes(xlim=(0, 2), ylim=(-2, 2))

gg2, = ax2.step([], [])

def init2():
    gg2.set_data([], [])
    return gg2,

def animate2(i):
    x = np.linspace(0, 2, 10)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    gg2.set_data(x, y)
    return gg2,






anim2 = animation.FuncAnimation(amp, animate, init_func=init,
                               frames=100, interval=20, blit=True)


anim3 = animation.FuncAnimation(amp2, animate2, init_func=init2,
                               frames=100, interval=20, blit=True)

plt.show()






##import numpy as np
##import matplotlib.pyplot as plt
##from matplotlib.animation import FuncAnimation
##import matplotlib.animation as animation
##
##
##amps = plt.figure(1)
##ax2a = plt.subplot()
##ax2a.grid(True)
##ax2a.set_ylim([0,6])
##ax2a.set_xlabel('Cell Number')
##ax2a.set_ylabel('Amps (V)')
##ax2a.set_title('Amps')
##
##volts = plt.figure(2)
##ax2 = plt.subplot()
##ax2.grid(True)
##ax2.set_ylim([0,6])
##ax2.set_xlabel('Cell Number')
##ax2.set_ylabel('Voltage (V)')
##ax2.set_title('Voltage')
##
##temp = plt.figure(3)
##ax3 = plt.subplot()
##ax3.grid(True)
##ax3.set_ylim([0,6])
##ax3.set_xlabel('Cell Number')
##ax3.set_ylabel('temp')
##ax3.set_title('temp')
##
##fig, ax2 = plt.subplots()
##xdata, ydata0, ydata1 = [], [], []
##ln0, = plt.plot([], [], 'r', animated=True)
##ln1, = plt.plot([], [], 'b', animated=True)
##f = np.linspace(-3, 3, 200)
##
##def init():
##    ax2.set_xlim(0, 3)
##    ax2.set_ylim(0, 10)
##    ln0.set_data(xdata,ydata0)
##    ln1.set_data(xdata,ydata1)
##    return ln0, ln1
##
##def update(frame):
##    xdata.append(frame)
##    ydata0.append(np.exp(-frame**2))
##    ydata1.append(np.exp(frame**2))
##    ln0.set_data(xdata, ydata0)
##    ln1.set_data(xdata, ydata1)
##    return ln0, ln1,
##
##def updateAmps(frameNum):
##    import matplotlib.animation as animation
##    import numpy as np
##    import matplotlib.pyplot as plt
##    from matplotlib.animation import FuncAnimation
##
##    x = np.linspace(0, 2, 10)
##    y = np.sin(2 * np.pi * (x - 0.01 * i))
##    line.set_data(x, y)
##    return line,
##
##
##
####ani = FuncAnimation(fig, update, frames=f,
####                    init_func=init, blit=True, interval=2.5, repeat=False)
##
##anim1 = animation.FuncAnimation(amps, updateAmps,interval = 20, blit = True)
##
##plt.show()
###plot.show()
