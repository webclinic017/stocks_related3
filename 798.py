import pandas as pd


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

def plotx(p1,p2,s3a,s4a,p3):
    print("Hello reading funct plotx parameters: ",p1,p2,s3a,s4a,p3)
    
    plt.plot(p1,p2, color='green', marker='o',
             linestyle='dashed',linewidth=2, markersize=1)
    print(type(p2))
    
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
    

##def main():
    
df=pd.read_csv('/home/az2/df566.csv')
i=0
print(df,'df')
u=df['ticker'].unique()
print(u)
for p in u:
    df=pd.read_csv('/home/az2/df566.csv')
        
    gm=p
    print(gm,'element ---------------->')
##    print('\n\n\n',df['ticker'],' 880','\n\n\n')
##    dfv=df[df['ticker'] == p]
    dfv=df.loc[df['ticker'] == str(p)]
    df=dfv
    print(df,'first ticker')
    print(df.columns)
    df.set_index('s2',inplace=True)
    print(df,gm)

    ################## end ###############



    df=df[(df.index > '08:59') & (df.index < '16:01')]
    ##df=df[(df.index.get_level_values(1) > '08:59') & (df.index.get_level_values(1) < '16:01')]
    ##h=df[df.index.get_level_values(1) > '09:00' & df.index.get_level_values(1) < '16:00']
    ##print(df,' df',gm)


    df=df[['macd','Close_vwap','Close_EMA5','Close_EMA10','adx','MOM', 'High_delta', 'Low_delta', 'MOM_slope', 'SARx',
           'bolinger_width', 'CCI', 'RSI', 'EMA_slope', 'fastk', 'DM_delta', 'DI_delta', 'mama','aroonup', 'aroondown','ticker','signal']]
    print(df,'99',gm,' filtered')
    ##print(df['signal'].unique)

    ## 'squeeze_on'
    df.reset_index(inplace=True)
    import matplotlib.pyplot as plt 
    ####print(g6[5],'----------------------------')
    ##print(df,' uuu')
    import numpy as np
    import sys

    i=1

    s2=df['signal'].unique()
    print(s2)
    if len(s2)<=2:
        s3=''
        s4=''
    if len(s2)==1:
        s3=''
        s4=''        
    else:    
        s3=s2[1]
        s4=s2[2]
    print(s3,s4,'---- signals')
    ##sys.exit()

    k=0
    for x in df.index:
        k=k+1
        if df['signal'].loc[x]=='Buy_signal':
            s3a=x    
        if df['signal'].loc[x]=='Sell_signal':
            s4a=x    
            print(x,'   ',df['signal'].loc[x])
        if k==df.shape[0] and df['signal'].loc[x]!='Buy_signal':
            s3a=0
        if k==df.shape[0] and df['signal'].loc[x]!='Sell_signal':
            s4a=0
            

    print('Buy signal index=',s3a,'  ','sell signal index=',s4a)
    print('Trade in :',s4a-s3a)

    print(df,' 99999')
    while (i<(df.shape[1]-2)):
        
        
        
    ##    
    ##    x=df.iloc[:,i]
    ##    print(x.iloc[:,2])
        p1=(df.iloc[:,0])
        print(p1,'s2')
        p2=(df.iloc[:,i])
        p3x=df.columns.get_loc('ticker')
        p3=df.iloc[0,p3x]
        print(p2,p2.name)
    ##    plt.title(str(p2.name)+str(' ')+str(p2.name))
        for x in df.index:
                
    ##        print(df['signal'].loc[x],'   ',s3)
    ##        print(df['signal'].loc[x])    
        ##    plt.plot(p1,p2)
            if df['signal'].loc[x]=='Buy_signal':
                s3a=x
            if df['signal'].loc[x]=='Sell_signal':
                s4a=x   
        plotx(p1,p2,s3a,s4a,p3)


##        plt.show()
        i=i+1

        plt.show()
    df = pd.pivot_table(df,index=['s2','ticker'],columns=['ticker'])
    print(df,'pivot')
