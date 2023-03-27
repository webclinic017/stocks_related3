from matplotlib import pyplot as plt
fig = plt.figure()
ax = fig.add_subplot()
plt.show(block=False)
plt.pause(0.001) # Pause for interval seconds.
input("hit[enter] to end.")
plt.close('all') # all open plots are correctly closed after each run
