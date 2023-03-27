import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def my_func(nfigs):
    anims = []
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    import pandas as pd
    import yfinance as yf
    import talib as taa
    from finta import TA
    
    perda='3d'
    intervla='1m'
    x='BTC-USD'
    df=yf.download(x, period=perda, interval=intervla,prepost = False)

    df['v']=df['Volume']
    df['tp2']=''
    df['tp2']=df['Close']+df['Low']+df['High']
    df['tp2']=df['tp2'].div(3).values
    df['v']=np.cumsum(df['v'])

    df['vwap']=(df['tp2']*df['v']).cumsum()/df['v'].cumsum()
    df['SAR']=TA.SAR(df,0.02,0.2)
    df['EMA_7'] = taa.EMA(df['Close'], timeperiod=7)
    df['EMA_21'] = taa.EMA(df['Close'], timeperiod=21)
    df['EMA_50'] = taa.EMA(df['Close'], timeperiod=50)
    df['EMA_100'] = taa.EMA(df['Close'], timeperiod=100)
    df['EMA_200'] = taa.EMA(df['Close'], timeperiod=200)
    df['BB_upperband'], df['BB_middleband'], df['BB_lowerband'] = taa.BBANDS(df['Close'], timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)


    df=df.tail(10)

    ys=df.iloc[1:,8].values  #vwap

    
    ys2=df.iloc[1:,df.columns.get_loc('SAR')].values  #SAR
    xs=list(range(1,len(ys)+1))
    xs2=list(range(1,len(ys2)+1))

    
##    ax1.plot(xs,ys,color = 'darkviolet',label='Close'+str(''),  lw=1.0,marker='o',markersize=.7)
##    ax1.plot(xs,ys2,color = 'blue',label='VWAP'+str(''),  lw=.5,marker='o',markersize=.5)
   
    for i in range(nfigs):
        fig = plt.figure()
##        ax = fig.add_subplot(111)
        ax = plt.subplot(1, 1, 1)
##        fig = plt.Subplot(444)        
####        bx = fig.add_subplot(111)
##        bx = plt.subplot(2,2,2, frameon=False)

        def animate(i):
            print(i)

              
            ax.plot(xs,ys,color = 'darkviolet',label='Close'+str(''),  lw=1.0,marker='o',markersize=.7)
##                ax.plot(xs,ys2,color = 'blue',label='VWAP'+str(''),  lw=.5,marker='o',markersize=.5) 
##                ax.plot(xs,ys2,color = 'blue',label='VWAP'+str(''),  lw=.5,marker='o',markersize=.5)
                            
            bx.plot(xs2,ys2,color = 'red',label='vwap'+str(''),  lw=1.0,marker='o',markersize=.7)
                   
##            fig.show()
##        col = ax.bar(x=range(10), height=np.zeros((10,)))
##        ax.set_ylim([0, 1])

##        def animate(k, bars):
##            new_data = np.random.random(size=(10,))
##            for j, b in enumerate(bars):
##                b.set_height(new_data[j])
##            return bars,

        ani = animation.FuncAnimation(fig, animate, frames=100)
        anims.append(ani)

    return anims

nfigs=2
my_anims = my_func(nfigs)
# calling simply my_func() here would not work, you need to keep the returned
# array in memory for the animations to stay alive
plt.show()
