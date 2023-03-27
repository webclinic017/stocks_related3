##def x2(x,y,z):
##    
##    import yfinance as yf
##    import mplfinance as mpf
##    import talib as ta
##
##    ticker_name = x
##    yticker = yf.Ticker(x)
##    data = yticker.history(period = y, interval = z) # max, 1y, 3mo
##
##    # trim volume to avoid exponential form
##    data['Volume'] = data['Volume'] / 1000
##
##    # macd
##    data["macd"], data["macd_signal"], data["macd_hist"] = ta.MACD(data['Close'])
##
##    # macd panel
##    colors = ['g' if v >= 0 else 'r' for v in data["macd_hist"]]
##    macd_plot = mpf.make_addplot(data["macd"], panel=1, color='fuchsia', title="MACD")
##    macd_hist_plot = mpf.make_addplot(data["macd_hist"], type='bar', panel=1, color=colors) # color='dimgray'
##    macd_signal_plot = mpf.make_addplot(data["macd_signal"], panel=1, color='b')
##
##    # plot
##    plots = [macd_plot, macd_signal_plot, macd_hist_plot]
##    mpf.plot(data, type='candle', style='yahoo', mav=(5,10,21,50,100,200), addplot=plots, title=f"\n{ticker_name}", volume=True, volume_panel=2, ylabel='', ylabel_lower='')
##
##
##x2('tsla','2d','5m')


import yfinance as yf
df = yf.Ticker('MSFT').history(period='1y')
import mplfinance as mpf
import pandas_ta as ta
apdict = mpf.make_addplot(ta.sma(df['Close'], length=10), linestyle='solid',width=1)
##apdict = mpf.make_addplot(ta.sma(df['Close'], length=10), linestyle='dotted',width=4)
mpf.plot(df, block=False, volume=True, addplot=apdict)
