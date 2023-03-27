import numpy; import pandas as pd;import random,datetime;from faker import Faker;fake = Faker('en_US')

d1=[];d2=[];d3=[]
for x in range(100):
    d1.append(fake.state())
    d2.append(fake.city())
    d3.append(x)

df1=pd.DataFrame([d3,d2,d1])
df=df1.T
print(df.iloc[:55,[1]])
##print(df)
    
