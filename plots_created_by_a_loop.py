import pandas as pd
import numpy as np


pd.options.display.float_format = '{:.2f}'.format
pd.options.display.max_columns = 255
pd.options.display.max_rows = 6500000

##pd.options.display.max_rows = 999999
pd.options.display.max_columns = 200
pd.set_option("display.max_columns", 200)
pd.set_option('display.width', 1000)
pd.set_option('display.expand_frame_repr', True)


pd.options.display.float_format = '{:.2f}'.format
pd.options.display.max_columns = 355
##pd.options.display.max_rows = 6500000
pd.options.display.max_rows = 6500
##pd.options.display.max_rows =999999 
##pd.options.display.max_columns = 36
pd.set_option("display.max_columns", 200)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 200)
pd.set_option('display.max_columns', 0)
pd.set_option('display.max_columns', None)
pd.set_option("expand_frame_repr", True)

##def plotx(p1,p2,s3a,s4a,p3):
def plotx(p1,p2,p3,s3a,s4a):
    import matplotlib.pyplot as plt
    import pandas as pd
    import sys
    print("Hello reading funct plotx parameters: ",p1,p2,s3a,s4a,p3)
    
    plt.plot(p1,p2, color='green', marker='o',
             linestyle='dashed',linewidth=2, markersize=1)
    print(type(p2))
    
##    plt.fill_between(p1, p2, where=(p2.squeeze() > 0), color='#00FF00')
##    sys.exit()
##    plt.fill_between(p1, p2, where=(p2.squeeze() < 0), color='#ff0000')
    plt.fill_between(p1, p2, where=(pd.to_numeric(p2) > 0), color='#00FF00')
    plt.fill_between(p1, p2, where=(pd.to_numeric(p2) < 0), color='#ff0000')

##    plt.vlines(['09:30','16:00'], p2.min(), p2.max(), colors='r',
##                      linestyles='solid',
##                      label='hours')
    plt.vlines([s3a,s4a], p2.min(), p2.max(), colors='b',
                      linestyles='solid',
                      label='hours')


    plt.legend()
    plt.xticks(np.arange(0, len(p2)+1,60))
##    plt.yticks(np.arange(0, max(p1), 2))
    plt.title(str(p2.name)+' '+str(p3))
    

#####################################################################

        
def step_3(df,x):
    
    ##print(df['signal'].unique)

    ## 'squeeze_on'
##    df.reset_index(inplace=True)
##    print(df.columns)
    import matplotlib.pyplot as plt 
    ####print(g6[5],'----------------------------')
    ##print(df,' uuu')
    import numpy as np
    import sys

    i=1

    s2=df['signal'].unique()
    print(x,len(s2),'--->', s2,'  ppp ')


    s3a=''
    s3b=''
    for x in df.index:
        if df['signal'].loc[x]=='Buy_signal':
            s3a=x
            b2=df['MOM'].loc[x]
            c2=df['macd'].loc[x]
        if df['signal'].loc[x]=='Sell_signal':
            s3b=x
            b3=df['MOM'].loc[x]
            c3=df['macd'].loc[x]
        else:
            pass

    print(df['ticker'][-1],s3a,'  ',s3b)
    
    if len(s3a) > 0 and len(s3b)> 0:
        print(df['ticker'][-1],s3a,'  ',s3b,'  ',\
              int(s3b.split(':')[0])-int(s3a.split(':')[0]),\
              ':',abs(int(s3b.split(':')[1])-int(s3a.split(':')[1])),'  ',b2.round(2),'/',b3.round(2),'  ',c2.round(2),'/',c3.round(2))
 

    s4a=s3b
    p3=df['ticker'][-1]
    p2=[]
    import matplotlib.pyplot as plt 
    ####print(g6[5],'----------------------------')
    ##print(df,' uuu')
    import numpy as np
    import sys
    print(df,'jj')
    df.reset_index(inplace=True)
    p1=(df.iloc[:,0])
    p2=df.iloc[:,[1,2,3,4,5,6,7,8,9,10,11,12]]
    k=1
    while (k<13):
        plt.fill_between(df.iloc[:,0], df.iloc[:,k], where=(df.iloc[:,k] > 0), color='#00FF00')
        plt.fill_between(df.iloc[:,0], df.iloc[:,k], where=(df.iloc[:,k] < 0), color='#ff0000')
        k=k+1
        
##    p2=p2.append(df.iloc[:,[1,2,3,4,5,6,7,8,9,10,11,12]])
    plt.title(df['ticker'][1])
    plt.plot(p1,p2)
    plt.vlines([s3a,s4a], -300, 300, colors='b',
                      linestyles='solid',
                      label='hours')
    plt.legend([str(df.columns[1]),str(df.columns[2]),
                str(df.columns[3]),str(df.columns[4]),
                str(df.columns[5]),str(df.columns[6]),

                str(df.columns[7]),str(df.columns[8]),
                str(df.columns[9]),str(df.columns[10]),
                str(df.columns[11]),str(df.columns[12])
##                str(df.columns[5]),str(df.columns[6]),
##                str(df.columns[3]),str(df.columns[4]),
##                str(df.columns[5]),str(df.columns[6]),

                ])
    plt.xticks(np.arange(0, len(p2)+1,60))

##    plotx(p1,p2,p3,s3a,s4a)
    
    plt.show()

def tt(dfg,x):
    import matplotlib.pyplot as plt
    import pandas as pd
    import sys

    dfg.reset_index(inplace=True)
    p1=dfg.iloc[:,0]
    p2=dfg.iloc[:,1]
    print('m')
##
##    for x,y in dfg.iteritems():
##        print(x,y)

    i=1
    for x in dfg:
        p1=dfg['s2']
        p2=dfg[x]
        print(x,p1,p2)
        i=i+1
##    plt.plot(p1,p2)
##    plt.xticks(np.arange(0, len(p1)+1,60))
##    plt.show()

##    fig, ax = plt.subplots(2, 2, sharex=True)
##
##    ax[0, 0].plot(p1,p2, 'r') #row=0, col=0
##    ax[0, 0].set_xticks(p1)
##    ax[0, 0].set_xticklabels(p1, rotation='vertical')
##    
##    ax[1, 0].plot(p1,p2, 'b') #row=1, col=0
##    ax[1, 0].set_xticks(p1, minor=False)
##    ax[0, 1].plot(p1,p2, 'g') #row=0, col=1
##    
##    ax[1, 1].plot(p1,p2, 'k') #row=1, col=1



        
  
    
    


def main():
    import pandas as pd
    df=pd.read_csv('/home/az2/df566.csv')
    i=0
##    print(df,'df')
    u=df['ticker'].unique()
    print(u,'   ',' main')
    for x in u:
        dfv=df.loc[df['ticker'] == (x)]
        dfv.reset_index(inplace=True)
        dfv.set_index('s2',inplace=True)
        dfn=dfv[(dfv.index > '08:59') & (dfv.index < '16:01')]
        dfg=dfn[['macd','Close_vwap','Close_EMA5','Close_EMA10','adx','MOM', 'High_delta', 'Low_delta',
                 'MOM_slope', 'SARx',\
                 'bolinger_width', 'CCI', 'RSI', 'EMA_slope', 'fastk', 'DM_delta', 'DI_delta', 'mama','aroonup', 'aroondown','ticker','signal']]

        print(dfg,'  ',x)
        tt(dfg,x)
##        step_3(dfg,x)
        


main()

    
