import pandas as pd

d1=[5,3,64,22];d2=[64,66,35,33]
d3=['sam','joe','sara','ash']
df=pd.DataFrame([d1,d2,d3])
print(df)
df=df.T
df.columns=['a','n','c']
print(df)
##df=df.reset_index(inplace=True)
##df.columns=[['a','n','c']]
##print(df.columns)
##print(df.shape)
i=1
while (i < df.shape[0]):
    j=0
    while (j < (df.shape[1])):
           print(i,'  ',j,'  ',df.iloc[i,j])
           j=j+1
    i=i+1       
