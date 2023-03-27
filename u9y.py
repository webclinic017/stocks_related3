def b(ba):
    
    import pandas as pd;from faker import Faker;fake=Faker('en_US')

    d1=[];d2=[]

    for x in range(100):
        d1.append(fake.state())
        d2.append(fake.city())


    df1=pd.DataFrame([d1,d2])
    df2=df1.T

    print(df2.shape)
    print(df2.size)
    print(df2.columns.size)

    df2.to_csv('home/az2/Downloads/ut2/' +  str(ba) + '.csv' , index=false, header=None, sep=';')
        

for x in range(12):
    b(x) 
    
