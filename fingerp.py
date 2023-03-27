import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import yfinance as yf
import pandas as pd


df = yf.download('BTC-USD','2021-11-05', interval='5m')
df=pd.DataFrame(df)

df.reset_index(inplace=True)



##mm=pd.Timestamp(m)
##df['m']=df['mm']
print(str(df['Datetime'][:]))

##
##style.use('fivethirtyeight')
##
##fig = plt.figure()
##ax1 = fig.add_subplot(1,1,1)
##def animate(i):
##    graph_data = open('example.txt','r').read()
##    lines = graph_data.split('\n')
##    xs = []
##    ys = []
##    for line in lines:
##        if len(line) > 1:
##            x, y = line.split(',')
##            xs.append(float(x))
##            ys.append(float(y))
##    ax1.clear()
##    ax1.plot(xs, ys)
##
##ani = animation.FuncAnimation(fig, animate, interval=1000)
##plt.show()


##import os
##t=[]
##os.sendfile
##
##f=open('/home/az2/t5.txt', 'w+')
####os.remove('/home/az2/t555a.txt')
##for x in f:
##    print(x)
##    t.append(x)
##f.close()   

##print(t)        


##f2=open('/home/az2/t555a.txt','w+')
##for x in t:
##    f2.write(x)
##    f2.write('---->')
##    f2.write(' dddd ')
##    print(x)
##f2.close()        
        
##        f2.write('--'.join(x))


        
    

