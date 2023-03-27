import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
import sys
import re

#############################################
##perd='2d'
##intervl='1m'
##
##ticker=['DOCU','tsla','^NDX','SPY','QQQ','^DJI','^GSPC','ARKK']
### [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]
##df = yf.download(ticker, period=perd, interval=intervl,prepost = True)
##df=df['Close']
##print(df)
####plt.rcParams['figure.constrained_layout.use'] = True
##df.reset_index(inplace=True)
##print(df)
##df.rename({'Datetime':''},axis=1,inplace=True)
##df.set_index('',inplace=True)
##print(df)
### Have one subplot
##fig, ax = plt.subplots(4, 2, figsize=(5, 8))
##ax5,ax6,ax7,ax8,ax9,ax10,ax11,ax12=ax.flatten()
##fig.canvas.draw()
##
##print(df.tail(6))
##df['TSLA'].plot(ax=ax5, label='TSLA', title='TSLA').grid()
##df['DOCU'].plot(ax=ax6,label='DOCU', title='DOCU').grid()
##df['^NDX'].plot(ax=ax7, label='^NDX',title='^NDX').grid()
##df['SPY'].plot(ax=ax8, label='SPY',title='SPY').grid()
##df['^GSPC'].plot(ax=ax9, label='^GSPC',title='^GSPC').grid()
##df['^DJI'].plot(ax=ax10,title='^DJI').grid()
##df['QQQ'].plot(ax=ax11,title='QQQ').grid()
##df['ARKK'].plot(ax=ax12, title='ARKK').grid()                 
##
##
##plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.6)
##plt.xticks(df.index, labels='', rotation='vertical')
#############################################
perd='12d'
intervl='1d'

ticker=['DOCU','tsla','^NDX','SPY','QQQ','^DJI','^GSPC','ARKK','TNA','RUT']
# [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]
df = yf.download(ticker, period=perd, interval=intervl,prepost = True)
##print(df.columns)
df=df['Close']

print(df['DOCU'],df['SPY'])


##
df['DOCU_p']=''


for x in df.index:
    df['DOCU_p'].loc[x]=df['DOCU'].loc[x]-df['DOCU'].shift(1).loc[x]
df.reset_index(inplace=True)
print(df.shape)
print(df.tail(1))

print(df.loc[df.shape[0]-1])




##print(df)
####plt.rcParams['figure.constrained_layout.use'] = True
####df.reset_index(inplace=True)
##print(df)
##df=df['Close']



##df['Datetime']=pd.to_datetime(df['Datetime'])
#df['Datetime'] = pd.to_datetime(df['Datetime'].dt.strftime('%Y-%m'))

##df.style.format({'Datetime': lambda t: t.strftime("%m/%d/%Y")})
##
##df.rename({'Datetime':''},axis=1,inplace=True)
##df.set_index('',inplace=True)
##str(df.index).split(' ')[1]
##print(df)
# Have one subplot
##fig, ax = plt.subplots(4, 2, figsize=(5, 8))
####ax5,ax6,ax7,ax8,ax9,ax10,ax11,ax12=ax.flatten()
##fig.canvas.draw()

print(df.tail(6))
print(df.shape)
df.set_index('Date',inplace=True)

##ax5.plot(df.index,df['TSLA'])
##ax5.grid(visible=True,axis='both')
##ax5.autoscale(enable=True)
##ax5.title.set_font('b')
##ax5.get_title(loc='left')
##ax5.set_title('subplot 2')
##ax5.set_xticklabels(df.index, rotation=45)

plt.subplot(8, 2, 1)
plt.plot(df['DOCU'])
plt.gca()
df['DOCU'].plot.line(y=df['DOCU'],color='g',title='docu',linewidth=1,marker='o',grid=True,use_index=True,rot=90,fontsize=7,figsize=(12,8))

plt.subplot(8, 2, 2)
plt.plot(df['^NDX'])
plt.gca()
df['^NDX'].plot.line(y=df['^NDX'],color='r',title='^NDX',linewidth=1,marker='o',grid=True,use_index=True,rot=90,fontsize=7,figsize=(12,8))

plt.subplot(8, 2, 3)
plt.plot(df['^GSPC'])
plt.gca()
df['^GSPC'].plot.line(y=df['^GSPC'],color='r',title='^GSPC',linewidth=1,marker='o',grid=True,use_index=True,rot=90,fontsize=7,figsize=(12,8))



plt.subplot(8, 2, 4)
plt.plot(df['^DJI'])
plt.gca()
df['^DJI'].plot.line(y=df['^DJI'],color='r',title='^DJI',linewidth=1,marker='o',grid=True,use_index=True,rot=90,fontsize=7,figsize=(12,8))


plt.subplot(8, 2, 5)
plt.plot(df['QQQ'])
plt.gca()
df['QQQ'].plot.line(y=df['QQQ'],color='r',title='QQQ',linewidth=1,marker='o',grid=True,use_index=True,rot=90,fontsize=7,figsize=(12,8))



plt.subplot(8, 2, 6)
plt.plot(df['ARKK'])
plt.gca()
df['ARKK'].plot.line(y=df['ARKK'],color='r',title='ARKK',linewidth=1,marker='o',grid=True,use_index=True,rot=90,fontsize=7,figsize=(12,8))



plt.subplot(8, 2, 7)
plt.plot(df['TNA'])
plt.gca()
df['TNA'].plot.line(y=df['TNA'],color='r',title='TNA',linewidth=1,marker='o',grid=True,use_index=True,rot=90,fontsize=7,figsize=(12,8))


plt.subplot(8, 2, 7)
plt.plot(df['RUT'])
plt.gca()
df['RUT'].plot.line(y=df['RUT'],color='r',title='RUT',linewidth=1,marker='o',grid=True,use_index=True,rot=90,fontsize=7,figsize=(12,8))


plt.subplot(8, 2, 8)
plt.plot(df['SPY'])
plt.gca()
df['SPY'].plot.line(y=df['SPY'],color='r',title='SPY',linewidth=1,marker='o',grid=True,use_index=True,rot=90,fontsize=7,figsize=(12,8))





##df['ARKK'].plot.bar(x=df.iloc[0],y=df['ARKK'], marker = 'o')
##df.ARKK.plot.line(x=df.iloc[0],y=df['ARKK'])
##df['TSLA'].plot(ax=ax5, label='TSLA', title='TSLA').grid()
##df['DOCU'].plot(ax=ax6,label='DOCU', title='DOCU').grid()
##df['^NDX'].plot(ax=ax7, label='^NDX',title='^NDX').grid()
##df['SPY'].plot(ax=ax8, label='SPY',title='SPY').grid()
##df['^GSPC'].plot(ax=ax9, label='^GSPC',title='^GSPC').grid()
##df['^DJI'].plot(ax=ax10,title='^DJI').grid()
##df['QQQ'].plot(ax=ax11,title='QQQ').grid()
##df['ARKK'].plot(ax=ax12, title='ARKK').grid()                 

##plt.subplots_adjust(hspace=2)
##plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=1)
####plt.xticks(df.index, labels='', rotation='vertical')
##plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.6)

#############################################
##gg=['arkk','^ndx','^gspc','^dji','spy','tna','qqq','tsla','^dji']
##plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.6)

##plt.xticks(fontsize=2, rotation=90)
##plt.xticks(df.index, labels='', rotation='vertical')

##ax5.axes.xaxis.set_visible(False)
##df.reset_index(inplace=True)


plt.show()

'''
# Use ax for both
df[df['Country'] == 'Bhutan'].plot(x='Year', y='GDP_per_capita', ax=ax, label='Bhutan')
df[df['Country'] == 'Iran'].plot(x='Year', y='GDP_per_capita', ax=ax, label='Iran')
ax.set_title("Iran and Bhutan")

# Asking for TWO subplots, ax1 and ax2.
# Be sure to put them in parenthesis
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

# Use ax1 to plot Bhutan
df[df['Country'] == 'Bhutan'].plot(x='Year', y='GDP_per_capita', legend=False, ax=ax1)
ax1.set_title("Bhutan")

# Use ax2 to plot Iran
df[df['Country'] == 'Iran'].plot(x='Year', y='GDP_per_capita', legend=False, ax=ax2)
ax2.set_title("Iran")

# If you don't do tight_layout() you'll have weird overlaps
plt.tight_layout()

# Receive ax1 and ax2 - note that they go in parens
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=True)

# Use ax1 to plot Bhutan
df[df['Country'] == 'Bhutan'].plot(x='Year', y='GDP_per_capita', legend=False, ax=ax1)
ax1.set_title("Bhutan")

# Use ax2 to plot Iran
df[df['Country'] == 'Iran'].plot(x='Year', y='GDP_per_capita', legend=False, ax=ax2)
ax2.set_title("Iran")

# If you don't do tight_layout() you'll have weird overlaps
plt.tight_layout()


# Beacuse I'm asking for two rows of three columns each,
# I need to separate them out with even MORE parentheses
# Using figsize to make the figure a little bigger, 10"x5"
fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(nrows=2, ncols=3, sharex=True, sharey=True, figsize=(10,5))

# Doing each of these manually (ugh)
df[df['Country'] == 'Bhutan'].plot(x='Year', y='GDP_per_capita', legend=False, ax=ax1)
ax1.set_title("Bhutan")
df[df['Country'] == 'Iran'].plot(x='Year', y='GDP_per_capita', legend=False, ax=ax2)
ax2.set_title("Iran")
df[df['Country'] == 'France'].plot(x='Year', y='GDP_per_capita', legend=False, ax=ax3)
ax3.set_title("France")
df[df['Country'] == 'Ireland'].plot(x='Year', y='GDP_per_capita', legend=False, ax=ax4)
ax4.set_title("Ireland")
df[df['Country'] == 'Kazakhstan'].plot(x='Year', y='GDP_per_capita', legend=False, ax=ax5)
ax5.set_title("Kazakhstan")
df[df['Country'] == 'United Arab Emirates'].plot(x='Year', y='GDP_per_capita', legend=False, ax=ax6)
ax6.set_title("United Arab Emirates")

# If you don't do tight_layout() you'll have weird overlaps
plt.tight_layout()

'''





  
########################################################### clear the cache #######################3
import sys  #system specific parameters and names
import gc   #garbage collector interface

memory_usage_by_variable=pd.DataFrame({k:sys.getsizeof(v) for (k,v) in locals().items()},index=['Size'])
memory_usage_by_variable=memory_usage_by_variable.T
memory_usage_by_variable=memory_usage_by_variable.sort_values(by='Size',ascending=False).head(10)
##print(memory_usage_by_variable.head())

def obj_size_fmt(num):
    if num<10**3:
        return "{:.2f}{}".format(num,"B")
    elif ((num>=10**3)&(num<10**6)):
        return "{:.2f}{}".format(num/(1.024*10**3),"KB")
    elif ((num>=10**6)&(num<10**9)):
        return "{:.2f}{}".format(num/(1.024*10**6),"MB")
    else:
        return "{:.2f}{}".format(num/(1.024*10**9),"GB")


def memory_usage():
    memory_usage_by_variable=pd.DataFrame({k:sys.getsizeof(v)\
    for (k,v) in globals().items()},index=['Size'])
    memory_usage_by_variable=memory_usage_by_variable.T
    memory_usage_by_variable=memory_usage_by_variable\
   .sort_values(by='Size',ascending=False).head(10)
    memory_usage_by_variable['Size']=memory_usage_by_variable['Size'].apply(lambda x: obj_size_fmt(x))
    return memory_usage_by_variable

memory_usage()
##print(memory_usage_by_variable)

##print('\n''kaku khan','\n\n')
##
##print('2) gc.get_count()',gc.get_count())
##
##print('3) memory_usage-->: ',memory_usage())
##print('\n\n')
##print('4) gc.collect',gc.collect())
##print('5) gc.get_count() ',gc.get_count())
##print('memory_usage():',memory_usage())
##print('tota hoai baba')
##
##print('--------------------------------------------------','\n\n')
##print('\n')
##print('plotting loop', end4-start4)
##print('mpf plotting time',end3-start3)
##print('read from api/read from y.finance',end2-start2)


##print('--------------------------------------------------','\n\n')

##del gg
##del xz


#triggering collection
##print('After deleting df,df33,gg ,gc.collect()---',gc.collect())

#finally check memory usage
##print('\n')
##print('After deleting df,df33,gg,memory.usage()',memory_usage())




##['binance',
## 'blueskies',
## ,
## 'charles',
## 'checkers',
## 'classic',
## 'default',
## 'mike',
## 'nightclouds',
## 'sas',
## 'starsandstripes',
## 'yahoo']



######################################################
##import pandas as pd
##import mplfinance as mpf
##import datetime as dt
##import yfinance as yf
##
##
### Load data file.
##g='t'
##ticker=g
##no_of_days=365
##
##df = pd.DataFrame()
##
##
##start = dt.datetime.today() - dt.timedelta(no_of_days)
##end = dt.datetime.today()
##df = yf.download(ticker, start, end,prepost = True)
##
### Plot candlestick.
### Add volume.
### Add moving averages: 3,6,9.
### Save graph to *.png.
##mpf.plot(df, type='candle', style='charles',
##        title='',
##        ylabel='',
##        ylabel_lower='',
##        volume=True, 
##        mav=(200,100,50,20,10,3,5))
##
##
####################################
##import matplotlib.pyplot as plt
##from mpl_finance import candlestick_ohlc
##import pandas as pd
##import matplotlib.dates as mpl_dates
##import yfinance as yf
##import mplfinance as mpf
##
##plt.style.use('ggplot')
##
### Extracting Data for plotting
##df = yf.download('tsla', '2021-01-1','2021-06-28', index=False)
### Plot candlestick.
### Add volume.
### Add moving averages: 3,6,9.
### Save graph to *.png.
##mpf.plot(df, type='candle', style='charles',
##        title='',
##        ylabel='',
##        ylabel_lower='',
##        volume=True, 
##        mav=(3,6,9), 
##        savefig='test-mplfiance.png')






