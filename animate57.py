import matplotlib.animation as ani
import ssl

ssl._create_default_https_context = ssl._create_unverified_context



import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

import matplotlib.animation as ani
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
import pandas as pd

ticker=['tsla','arkk']
##ticker='tsla'

df = yf.download(ticker, period='100d', interval='1d',prepost = True)
df=pd.DataFrame(df)
df=df[['Close','High']]
##df_interest = df['Close']
##df1=df_interest
##df.reset_index(inplace=True)
df.index = pd.to_datetime(df.index)
##print(df['Close'].index)



color = ['red', 'yellow', 'blue', 'grey']
##fig = plt.figure()
fig, axes = plt.subplots(ncols=2,nrows=2)
##animator = ani.FuncAnimation(fig, chartfunc, interval = 100)
##fig = plt.figure(figsize=(20,10))
##plt.xlabel()
##plt.ylabel()
plt.title(ticker)


##for row in ax:
##    for col in row:
##        col.ployt(x,y)


plt.xticks(rotation=45, ha="right", rotation_mode="anchor") #rotate the x-axis values
plt.subplots_adjust(bottom = 0.2, top = 0.9) #ensuring the dates (on the x-axis) fit in the screen
plt.ylabel('No of Deaths')
plt.xlabel('Dates')
plt.grid(True)
plt.ylim(0,1400)
plt.xlim([df.index[0], df.index[-1]])


def buildmebarchart(i=int):
    plt.legend(df.columns)
    p = plt.plot(df[:i].index, df[:i].values) #note it only returns the dataset, up to the point i
##    p[0].set_color(color[0])
    for i in range(0,2):
        p[i].set_color(color[i]) #set the colour of each curve
import matplotlib.animation as ani
animator = ani.FuncAnimation(fig, buildmebarchart, interval = 0)
plt.show()
