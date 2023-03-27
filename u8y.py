#import urllib.request
import re
import pandas as pd


f1=open('/home/az2/Downloads/python_66/a/a1.txt','r')
g=f1.readlines()

m='azhar'
n='idno'
##    for x in g.split():
##    s=open('/home/az2/Downloads/python_66/a/a1_out.txt','w+')

##    p=[]
pv=pd.DataFrame(columns=['m','pp'])

print(pv)
##    data = pd.DataFrame({'col1': range(120),'col2': range(120)})

k=0 
while (k < 33):
    
    k=k+1
    if m in x:
        t=x.index(m,0)
        ss = x[t:t+33]
    else:
        print("nnnn")

    print(k,ss)
