import pandas as pd
import yfinance as yf
import pandas_ta as ta
import matplotlib.pyplot as plot
import numpy as np

x='nvda'
df=yf.download(x,start=pd.to_datetime('2022-05-20'),end=pd.to_datetime('2022-05-30'),interval='1d')
df.reset_index(inplace=True)
##df.set_index('Date', inplace=True, drop=True)
print(df.tail(3))

fig,ax2=plot.subplots()

ax2.plot(df['Close'],marker='o')
ax2.set_ylabel('Close')

##bin_edges = np.arange(0, df['Volume'].max()+1/4, 1/4)
##plt.hist(data = df, x = 'num_var', bins = bin_edges)

ax3=ax2.twinx()
ax3.set_ylabel('Volume')
ax3.hist(df['Volume'],orientation='horizontal',label=df['Volume'],color='red',alpha=0.2,histtype='bar', stacked=True,\
         )
plot.title(str(x)+str('  ')+str(df['Close'].values[-1].round(2))+str(' / prev  ')+str(df['Close'].values[-2].round(2)))
plot.text(df.index,df.Close,str)
        
ax2.set_ylabel('Volume')

plot.show()
