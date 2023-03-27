import os
import pandas as pd

df=pd.read_csv('/home/az2/Downloads/tt42.csv',delimiter=';')
print(df)

print('\n\n\n')
columnsp=[]

table_name='nnnn'


for x in df.columns:
    columnsp.append(x)



##print('\n\n\n')
##
p=open('/home/az2/Downloads/uu77596.txt','w+')    
for i,z in enumerate(df.values):
##    print('insert into ',table_name,' ',list(columnsp),' values ',z,';')
    p.write('insert into ')
    p.write(table_name)
    p.write(' ')
    p.write('(')
    j=0
    for x in (columnsp):
        p.write(str(x))
        
        if j < len(columnsp)-1:
            p.write(',')
        j=j+1
    p.write(')')    
    j2=0    
    p.write(' values (')
    for x2 in (z):
        p.write("'")
        p.write(str(x2))
        p.write("'")
        if j2 < len(z)-1:
            p.write(',')
        j2=j2+1
    p.write(') ')    
 
    p.write(';')
    p.write('\n')

p.close()

print('\n\n')
print('Table name : ', table_name)
print('\n')

g=open('/home/az2/Downloads/uu77596.txt','r+')
for x in g:
    print(x)
g.close()

    
