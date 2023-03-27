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
##    x = np.linspace(0, 15, 100)
##    print(p1.loc[15:],'  ',p2.iloc[15:,1],'88')
##    x5=df.iloc[:,0]
##    y5=df.iloc[:,1]
##    print(type(x5),'  ',type(y5))
    fig.suptitle(p3, fontsize=16)   
##    ax[0].plot(df.iloc[:406,0],df.iloc[:,1])
##    ax[1].plot(df.iloc[:406,0],df.iloc[:,2])
##    ax[2].plot(df.iloc[:406,0],df.iloc[:,3])
##    ax[3].plot(df.iloc[:406,0],df.iloc[:,4])
##    ax[4].plot(df.iloc[:406,0],df.iloc[:,5])
##    ax[5].plot(df.iloc[:406,0],df.iloc[:,6])
##    ax[6].plot(df.iloc[:406,0],df.iloc[:,7])
##    ax[7].plot(df.iloc[:406,0],df.iloc[:,8])
##    ax[8].plot(df.iloc[:406,0],df.iloc[:,9])
##    ax[9].plot(df.iloc[:406,0],df.iloc[:,10])
##    ax[10].plot(df.iloc[:406,0],df.iloc[:,11])
##    ax[11].plot(df.iloc[:406,0],df.iloc[:,12])

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


   



##    ax[0].vlines(df.iloc[200,0],(df.iloc[:,1]).min(),(df.iloc[:,1]).max(),'r')
##    ax[0].vlines(df.iloc[250,0],(df.iloc[:,1]).min(),(df.iloc[:,1]).max(),'r')
##    
##    ax[1].vlines(df.iloc[200,0],(df.iloc[:,2]).min(),(df.iloc[:,2]).max(),'r')
##    ax[1].vlines(df.iloc[250,0],(df.iloc[:,2]).min(),(df.iloc[:,2]).max(),'r')
##
##    ax[2].vlines(df.iloc[200,0],(df.iloc[:,3]).min(),(df.iloc[:,3]).max(),'r')
##    ax[2].vlines(df.iloc[250,0],(df.iloc[:,3]).min(),(df.iloc[:,3]).max(),'r')
##
##    ax[3].vlines(df.iloc[200,0],(df.iloc[:,4]).min(),(df.iloc[:,4]).max(),'r')
##    ax[3].vlines(df.iloc[250,0],(df.iloc[:,4]).min(),(df.iloc[:,4]).max(),'r')
##
##    ax[4].vlines(df.iloc[200,0],(df.iloc[:,5]).min(),(df.iloc[:,5]).max(),'r')
##    ax[4].vlines(df.iloc[250,0],(df.iloc[:,5]).min(),(df.iloc[:,5]).max(),'r')
##
##    ax[5].vlines(df.iloc[200,0],(df.iloc[:,6]).min(),(df.iloc[:,6]).max(),'r')
##    ax[5].vlines(df.iloc[250,0],(df.iloc[:,6]).min(),(df.iloc[:,6]).max(),'r')
##
##    ax[6].vlines(df.iloc[200,0],(df.iloc[:,7]).min(),(df.iloc[:,7]).max(),'r')
##    ax[6].vlines(df.iloc[250,0],(df.iloc[:,7]).min(),(df.iloc[:,7]).max(),'r')
##
##    ax[7].vlines(df.iloc[200,0],(df.iloc[:,8]).min(),(df.iloc[:,8]).max(),'r')
##    ax[7].vlines(df.iloc[250,0],(df.iloc[:,8]).min(),(df.iloc[:,8]).max(),'r')
##
##    ax[8].vlines(df.iloc[200,0],(df.iloc[:,9]).min(),(df.iloc[:,9]).max(),'r')
##    ax[8].vlines(df.iloc[250,0],(df.iloc[:,9]).min(),(df.iloc[:,9]).max(),'r')
##
##    ax[9].vlines(df.iloc[200,0],(df.iloc[:,10]).min(),(df.iloc[:,10]).max(),'r')
##    ax[9].vlines(df.iloc[250,0],(df.iloc[:,10]).min(),(df.iloc[:,10]).max(),'r')
##
##    ax[10].vlines(df.iloc[200,0],(df.iloc[:,11]).min(),(df.iloc[:,11]).max(),'r')
##    ax[10].vlines(df.iloc[250,0],(df.iloc[:,11]).min(),(df.iloc[:,11]).max(),'r')
##
##    ax[11].vlines(df.iloc[200,0],(df.iloc[:,12]).min(),(df.iloc[:,12]).max(),'r')
##    ax[11].vlines(df.iloc[250,0],(df.iloc[:,12]).min(),(df.iloc[:,12]).max(),'r')


##    ax[0].set_ylabel(df.columns[1])

##    ax[0].set_ylabel(df.columns[1],fontsize=5)
##    ax[1].set_ylabel(df.columns[2],fontsize=5)
##    ax[2].set_ylabel(df.columns[3],fontsize=5)
##    ax[3].set_ylabel(df.columns[4],fontsize=5)
##    ax[4].set_ylabel(df.columns[5],fontsize=5)
##    ax[5].set_ylabel(df.columns[6],fontsize=5)
##    ax[6].set_ylabel(df.columns[7],fontsize=5)
##    ax[7].set_ylabel(df.columns[8],fontsize=5)
##    ax[8].set_ylabel(df.columns[9],fontsize=5)
##    ax[9].set_ylabel(df.columns[10],fontsize=5)
##    ax[10].set_ylabel(df.columns[11],fontsize=5)
##    ax[11].set_ylabel(df.columns[12],fontsize=5)

##    ax[0].set_xlim(0, df.iloc[:406,0])
    
##    ax[0].set_ylim(df.iloc[:,1].min(), df.iloc[:,1].max())
##    ax[1].set_ylim(df.iloc[:,2].min(), df.iloc[:,2].max())
##    ax[2].set_ylim(df.iloc[:,3].min(), df.iloc[:,3].max())
##    ax[3].set_ylim(df.iloc[:,4].min(), df.iloc[:,4].max())
##    ax[4].set_ylim(df.iloc[:,5].min(), df.iloc[:,5].max())
##    ax[5].set_ylim(df.iloc[:,6].min(), df.iloc[:,6].max())
##    ax[6].set_ylim(df.iloc[:,7].min(), df.iloc[:,7].max())
##    ax[7].set_ylim(df.iloc[:,8].min(), df.iloc[:,8].max())
##    ax[8].set_ylim(df.iloc[:,9].min(), df.iloc[:,9].max())
##    ax[9].set_ylim(df.iloc[:,10].min(), df.iloc[:,10].max())
##    ax[10].set_ylim(df.iloc[:,11].min(), df.iloc[:,11].max())
##    ax[11].set_ylim(df.iloc[:,12].min(), df.iloc[:,12].max())
    
##    ax[1].set_ylim(0, df.iloc[:,2])
##    ax[2].set_ylim(0, df.iloc[:,3])
##    ax[3].set_ylim(0, df.iloc[:,4])
##    ax[4].set_ylim(0, df.iloc[:,5])
##    ax[5].set_ylim(0, df.iloc[:,6])
##    ax[6].set_ylim(0, df.iloc[:,7])
##    ax[7].set_ylim(0, df.iloc[:,8])
##    ax[8].set_ylim(0, df.iloc[:,9])
##    ax[9].set_ylim(0, df.iloc[:,10])
##    ax[10].set_ylim(0, df.iloc[:,11])
##    ax[11].set_ylim(0, df.iloc[:,12])


##    plt.plot(p1,p2)
##
##    k=0
##    for x2 in range(0,6,1):
##        p2.iloc[30,x2]
##        p2.iloc[:,x2] = float(float(p2.iloc[:,x2].fillna(0)))
##        print('kkkkk  ',x2,'  ',p2.iloc[:,x2],'  ',p1)
##        ax[x2, 0].plot(str(df.iloc[:,0]), df.iloc[:,1])
##        ax[x2, 1].plot(df.iloc[:,0], df.iloc[:,1]) 
##        ax[x2,0].grid()
##        ax[x2,1].grid()
##        ax[x2,0].vlines(5,0,(p1/2).max(),'r')
##        ax[x2,1].vlines(5,0,(p1/.4*p1).max(),'r')

    plt.show()

###############################################################################################################################
'''
    p1=(df.iloc[:,0])
    p2=df.iloc[:,[1,2,3,4,5,6,7,8,9,10,11,12]]
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
##                str(df.columns[3]),str(df.columns[4]),
##                str(df.columns[5]),str(df.columns[6]),
##                str(df.columns[3]),str(df.columns[4]),
##                str(df.columns[5]),str(df.columns[6]),
##                str(df.columns[3]),str(df.columns[4]),
##                str(df.columns[5]),str(df.columns[6]),
##                str(df.columns[3]),str(df.columns[4]),
##                str(df.columns[5]),str(df.columns[6]),
                ])
    plt.xticks(np.arange(0, len(p2)+1,60))

##    plotx(p1,p2,p3,s3a,s4a)

    
'''    
##    plt.show()
###############################################################################################################################


    
##    for x in df.index:
##        p1[x]=df.iloc[x,0]
##        p2[x]=df.iloc[x,1]
##        plt.plot(p1[x],p2[x])
##
##
####        plotx(p1,p2,p3,s3a,s4a)
##    plt.show()    
##   



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

##        print(dfg,'  ',gm)
        step_3(dfg,x)
        
##        step_2(u,dfv)
        ################## end ###############
##        df=step_3(df,gm)

##main()
'''
    p1b=[];p2b=[];p3b=[]
    table=[]
    i5=0
    while (i<(df.shape[1]-2)):
        m1b=[];m2b=[]
        
        
        
    ##    
    ##    x=df.iloc[:,i]
    ##    print(x.iloc[:,2])
        p1=(df.iloc[:,0])
        print(p1,'s2')
        p2=(df.iloc[:,i])
        p3x=df.columns.get_loc('ticker')
        p3=df.iloc[0,p3x]
        
        p1b.append(p1)
        p2b.append(p2)
        p3b.append(p3)

        print(p2,p2.name)
        
    ##    plt.title(str(p2.name)+str(' ')+str(p2.name))
##        for x in df.index:
##            
##            m1b.append(i5)
##            m2b.append(i5)
##            i5=i5+1
##        table.append(m1b)
##        table.append(m2b)
##                
##    ##        print(df['signal'].loc[x],'   ',s3)
##    ##        print(df['signal'].loc[x])    
##        ##    plt.plot(p1,p2)
##            if df['signal'].loc[x]=='Buy_signal':
##                s3a=x
##                m1b.append(x)
##            if df['signal'].loc[x]=='Sell_signal':
##                s4a=x
##                m2b.append(x)
##        plotx(p1,p2,s3a,s4a,p3)
##

##        plt.show()
        i=i+1

    i=0
    u=[]
    while(i<21):
        u.append(str(u)+str(i))
        i=i+1
    print(u)    
        
 
    print((df.shape[1]-2),'==================================== 99================>')
    i=1
    while (i<(df.shape[1]-2)):
        fig, (ax1, ax2) = plt.subplots(1, df.shape[1]-2)
        fig.suptitle('Horizontally stacked subplots')
##        for x in df.index:
##            m1b[i,x]=x
##            m2b[i,x]=x
        ax[i].plotx(p1b[i],p2b[i],p3b[i])
        i=i+1
##        ax[i].plot(x, y)
        plt.show()

    df = pd.pivot_table(df,index=['s2','ticker'],columns=['ticker'])
    print(df,'pivot')
'''
main()
