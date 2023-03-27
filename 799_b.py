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

##    if len(s2)==1:  
##        s3=''
##        s4=' '
##    elif len(s2) ==2:
##        s3=s2[1]
##        s4=' '        
##    else:    
##        s3=s2[1]
##        s4=s2[2]
##    print(x,'  ',s3,s4,'---- signals')
##
##
##    k=0
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
        print(df['ticker'][-1],s3a,'  ',s3b,'  within time:',\
              int(s3b.split(':')[0])-int(s3a.split(':')[0]),\
              ':',abs(int(s3b.split(':')[1])-int(s3a.split(':')[1])),'  MOM: ',b2.round(2),'/',b3.round(2),'  macd: ',c2.round(2),'/',c3.round(2))
 

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

####################################################################################################################################
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    import matplotlib.pyplot as plt
    import numpy as np

    p1=(df.iloc[:,0])
    p2=df.iloc[:,[1,2,3,4,5,6,7,8,9,10,11,12]]
    print(p2.iloc[:,3],'  ',p2.shape,'888')
    print(p2.shape)

    fig, ax = plt.subplots(13,sharex=True)
##    ax = plt.title(p3)
    print(type(p1),' ;;;;')

##    p1=pd.DataFrame(np.random.randint(0,100,size=(15, 1)), columns=list('x'))
    p2=pd.DataFrame(np.random.randint(0,100,size=(406, 1)), columns=list('x'))

    p2=df.iloc[:,2]
    p1=(df.iloc[:406,0])
    print(p1.shape)

    fig.suptitle(p3, fontsize=16)   

    for x in range(0,12,1):
        p1=df.iloc[:,0]
        p2=df.iloc[:,x+1]
        ax[x].plot(df.iloc[:,0],df.iloc[:,x+1])
        ax[x].can_zoom()
        ax[x].autoscale()
        ax[x].legend
        ax[x].grid
        ax[x].tick_params(axis='both', which='major', labelsize=3)
        ax[x].autoscale_view()
        ax[x].set_ylabel(df.columns[x+1],fontsize=5)
        ax[x].set_ylim(df.iloc[:,x+1].min(), df.iloc[:,x+1].max())
        ax[x].vlines(df.iloc[200,0],(df.iloc[:,x+1]).min(),(df.iloc[:,x+1]).max(),'r')
        ax[x].vlines(df.iloc[250,0],(df.iloc[:,x+1]).min(),(df.iloc[:,x+1]).max(),'r')
        
        ax[x].fill_between(p1, p2, where=(pd.to_numeric(p2) > 0), color='#00FF00')
        ax[x].fill_between(p1, p2, where=(pd.to_numeric(p2) < 0), color='#ff0000')
        ax[x].set_xlim(xmin=p1.min(), xmax=p1.max())
        ax[x].set_xbound(lower=p1.min(), upper=p1.max())

    
    plt.show()

###############################################################################################################################
  
##    plt.show()


def main():
    import pandas as pd
    df=pd.read_csv('/home/az2/df566.csv')
    print(df,' 999')
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

##        print(dfg,'  ',gm)
        step_3(dfg,x)
        
##        step_2(u,dfv)
        ################## end ###############
##        df=step_3(df,gm)

##main()

main()
