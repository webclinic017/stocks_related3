import pandas as pd

g=pd.DataFrame({'name':['asad','azhar','naheed','fatima','asad'],
                 'age':[53,51,48,40,53],
                'sex':['M','M','F','F','M']})

##g.reset_index(drop=True)
##g.set_index(['name','sex'],inplace=True)

print(g.iloc[0:4,0:3])
##print(g)
