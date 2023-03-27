##import pandas as pd
##pd.options.display.max_rows=9999
##pd.options.display.max_columns=15
##
##tickers_list = ['NDX']
##
### Fetch the data
##import yfinance as yf
##data = yf.download(tickers_list,'2021-1-1')[['Open','Close','Volume']]
##
### Print first 5 rows of the data
##print(data.tail())

##############################################
## Minute level data
import yfinance as yf
import pandas as pd

pd.options.display.max_rows=9999
pd.options.display.max_columns=15

# Get the data
data = yf.download(tickers='$SPX', period="1d", interval="1m")

# Print the data
print(data.tail())
