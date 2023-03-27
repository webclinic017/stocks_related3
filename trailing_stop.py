df['Close'].loc[z] < df['Close'].loc[z]-df['Close'].shift(1).loc[z]*.2
