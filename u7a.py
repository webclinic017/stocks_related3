import os
import numpy as np
import pandas as pd
pd.set_option('display.max_rows', 800)
pd.set_option('display.max_columns', 290)


dfb=[]
df = pd.DataFrame()
df1 = pd.DataFrame()
df2 = pd.DataFrame()
def m(fa):
    
    import pandas as pd

    g=[]   #read contents
    g1=[]   #build headerrs
    g2=[]
    


    f=open('/home/az2/Downloads/t1/' + fa , 'r',  encoding='ISO-8859-1')
    for x in f:


        print(fa,' --->  ', len(x), '  ------> ',x)
        p=x.split('|')
        print(fa,'  ---->  ',p)
        #print(fa,"  --->   ",p)
        k1=0
        k2=0
        if (p[0]=='PID'):
            p[6]=fa
    ##        print(p[0])
            k=0
            while (k <= (len(p)-1)):
                
##                print(p[k])
                g.append(p[k])   #read contents
                g1.append('col_' + str(k) + '_' + str(p[0]))   #build headerrs
                g2.append(p[6])
                k=k+1
##                if k == len(p)-1:
##                    print(fa,'PID','k=',k,' k1=',k1, 'len(p)=',len(p),g1)
##                df = pd.DataFrame(g,g1)
##                df1=df.append(df)
################################################################
        if (p[0]=='IN1'):
##            p[6]=fa
##            print(k,p[0])
            k=0
            while (k <= (len(p)-1)):
##                print(k,p[k])
                g.append(p[k])   #read contents
                g1.append('col_' + str(k) + '_' + str(p[0]))   #build headerrs
##                g2.append(p[6])
##                print(g,'     ',g1)
                k=k+1
    ##                if k == len(p)-1:
    ##                    print(fa,'PID','k=',k,' k1=',k1, 'len(p)=',len(p),g1)
##                df = pd.DataFrame(g,g1)
##                df1=df.append(df)    
################################################################                        
    ##        print(df1.T)
        df = pd.DataFrame(g,g1)
        df1=df.append(df)

################################################################

    df2=df1.T
    return(fa,df2)

c=pd.DataFrame()

for f in os.listdir('/home/az2/Downloads/t1/'):
##    print(f)
    hh=m(f)
    pp=hh[1][['col_3_PID','col_5_PID','col_7_PID','col_11_PID','col_6_PID','col_3_IN1']]
    pp1=hh[0]
##    print(pp1)
##    print('****************************\n')
    c=c.append(pp)

c = c.loc[:,~c.columns.duplicated()]
c.to_csv('/home/az2/Downloads/jj.txt',index=False)

##print(c)
##df = pd.DataFrame(c)
##print(df.shape)
##print(df.replace('[',''))


