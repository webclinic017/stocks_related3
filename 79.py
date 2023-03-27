import numpy as np
import matplotlib.pyplot as plt
import datetime
import numpy as np
import matplotlib.dates as mdates
import pandas
from datetime import date, timedelta
import yfinance as yf


df = yf.download('t', period='60d', interval='1d',prepost = True)
df.reset_index(inplace=True)
##print(df[['Date','Close']])

##sdate = date(2019,3,22)   # start date
##edate = date(2019,4,9)   # end date
##g=pandas.date_range(sdate,edate-timedelta(days=1),freq='d')
##
##print(g)
col=df['Date']
p=[]
for x in col:
    p.append(str(x))
print('p length=',p)    
##f, (ax1, ax2,ax3,ax4,ax5,ax6,ax7,ax8) = plt.subplots(2, 4, sharex=True)
##ax.set_xlim(p[0],p[5])


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, sharex=True)

##ax1.xaxis.set_ticks(p)
##ax2.xaxis.set_ticks(p)
ax1.set_xlim(p)

##f, ax = plt.subplots(4,2,sharex=df.Date,sharey=df.Close)


##ax[1,2].set_title('66t')
##ax[2,2].set_title('987t')
##ax[3,2].set_title('33t')
##
##ax[0,3].set_title('66t')
##ax[1,3].set_title('987t')
##ax[2,3].set_title('33t')


##
##plt_data = range(5, 9)
##plt.subplots_adjust(bottom = 0.2)
##plt.xticks(rotation = 25)


##ax.set_ylim([0, 2225])
##for x in range(16):
##    for y in range(5):
##        ax[x,y].set_ylim([0, 2225])
##
##for x in range(16):
##    for y in range(5):
##        for z in g:
##            ax.set_xlim(z)     

plt.show()
