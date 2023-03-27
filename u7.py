import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import pandas as pd
import matplotlib.dates as mpl_dates
import yfinance as yf
import mplfinance as mpf

plt.style.use('ggplot')

# Extracting Data for plotting
df = yf.download('tsla', '2021-01-1','2022-06-28', index=False)
# Plot candlestick.
# Add volume.
# Add moving averages: 3,6,9.
# Save graph to *.png.
mpf.plot(df, type='candle', style='charles',
        title='',
        ylabel='',
        ylabel_lower='',
        volume=True, 
        mav=(3,6,9), 
        savefig='test-mplfiance.png')
print(mpf,'444')







import mplfinance as mpf
import pandas as pd
import talib as ta
import yfinance as yf





import mplfinance as mpf

ticker='^NDX'

##ticker='^SPX'  https://pypi.org/project/mplfinance/
df = yf.download(ticker, '2021-01-1','2021-06-28', index=False)
print('Running')
##mpf.plot(df, type='candle')
##mpf.plot(df[-100:-1], type='candle', volume=True, figratio=(15, 7), style='yahoo', title='Apple, 2020')
print(df[-100:])
##df=df['Close']
##mpf.plot(df[-100:-1], type='candle', volume=True, figratio=(15, 7), style='yahoo', mav=(3, 13), title=ticker)
mpf.plot(df[-100:], type='candle', volume=True, figratio=(15, 7), style='yahoo', mav=(3, 7,13), title=ticker,show_nontrading=True)
print('finish')
mpf.make_addplot(line20,panel='lower',color='g'), 
##mpf.plot(df,hlines=dict(hlines=[support,resistance],colors=['g','r'],linestyle='-.'), title='MSFT', ylabel='Price', ylabel_lower='Volume', type='candle', style='charles', volume=True, mav=(50, 200), savefig='test-mplfiance.png')

##mpf.plot(df)



# macd
df["macd"], df["macd_signal"], df["macd_hist"] = ta.MACD(df['Close'])

# macd panel
colors = ['g' if v >= 0 else 'r' for v in df["macd_hist"]]
macd_plot = mpf.make_addplot(df["macd"], panel=1, color='fuchsia', title="MACD")
macd_hist_plot = mpf.make_addplot(df["macd_hist"], type='bar', panel=1, color=colors) # color='dimgray'
macd_signal_plot = mpf.make_addplot(df["macd_signal"], panel=1, color='b')

# plot
plots = [macd_plot, macd_signal_plot, macd_hist_plot]
mpf.plot(df, type='candle', style='yahoo', mav=(50,100,200), addplot=plots, title=ticker, volume=True, volume_panel=2, ylabel='', ylabel_lower='')


##mpf.plot(df[-100:-1], type='candle', style='charles',
##        title='',
##        ylabel='',
##        ylabel_lower='',
##        volume=True, 
##        mav=(3,6,9))

##print(help(mpf.plotting))
##mpl_finance.plotting.plot(df['Close'],df['Volume'],mav=(3, 10),title=ticker)
##mpf.candlestick2_ochl(candles, opens=prices_open, closes=prices_close, highs=prices_high, lows=prices_low, ticksize=1, colorup="#04E217", colordown="#DB0000")


##

######df=df.iloc[6:,:]
######print(df)
########print('baba',df.shape)
######
######df.reset_index(inplace = True)
####
######df['day'] = df['Date'].dt.day_name()
####df['ticker']=ticker
####print(df)
######
########data = pd.read_csv('NYSE_BABA, 5s.csv', index_col=0)
######df.index = pd.to_datetime(df.index)
######mpf.plot(df,type='candle')
######mpf.plot_day_summary2_ohlc(ax, opens, highs, lows, closes, ticksize=4, colorup='k', colordown='r')
####
######df.index.name = 'Date'
####print(mpf)
####mpf.plot(df)
##
##import matplotlib.pyplot as plt
##import pandas as pd
##from matplotlib.dates import DateFormatter, MonthLocator, YearLocator
##
##years = YearLocator()  # every year
##months = MonthLocator()  # every month
##yearsFmt = DateFormatter('%Y')
##
####quotes = pd.read_csv('data/yahoofinance-INTC-19950101-20040412.csv',
####                     index_col=0,
####                     parse_dates=True,
####                     infer_datetime_format=True)
##
##quotes=df
##dates = quotes.index
##opens = quotes['Close']
##
##fig, ax = plt.subplots()
##ax.plot_date(dates, opens, '-')
##
### format the ticks
##ax.xaxis.set_major_locator(years)
##ax.xaxis.set_major_formatter(yearsFmt)
##ax.xaxis.set_minor_locator(months)
##ax.autoscale_view()
##
##
### format the coords message box
##def price(x):
##    return '$%1.2f' % x
##
##
##ax.fmt_xdata = DateFormatter('%Y-%m-%d')
##ax.fmt_ydata = price
##ax.grid(True)
##
##fig.autofmt_xdate()
##plt.show()

##
##ohlc['SMA5'] = ohlc['Close'].rolling(5).mean()
##ax.plot(ohlc['Date'], ohlc['SMA5'], color='green', label='SMA5')
##
##fig.suptitle('Daily Candlestick Chart of NIFTY50 with SMA5')
##
##plt.legend()
##
##plt.show()
