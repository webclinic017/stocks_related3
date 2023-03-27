from yahoo_fin import stock_info as si

# pulls historical OHLC data into a pandas data frame
si.get_data("nflx")
