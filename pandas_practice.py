import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url = 'http://bit.ly/uforeports'
df = pd.read_csv(url)
##m1="/home/aa/Documents/3A_Drops.xls"
##m2="/home/aa/Documents/3A_Drops.xls"
##df1 = pd.read_excel(m1, sheetname='3A_Drops')
print(df.shape)
print(df.loc[18200:18222])
## reset index
##print(df.index)
##print(df.head(3))
##df.reset_index(drop=True)
##df.set_index('City',inplace=True)
##print(df.index)
##print(df.head(3))

df.reset_index()
##df.set_index('',inplace=True)
print(df.head(3))

##print(df.head())
##print(df.columns)
##print(df.shape)
##print(ufo.groupby.)
##print (df.groupby(['City']).size())
##print(df[(df.City=='Seattle')])
##print(df[(df.City=='Seattle')])
##print(df[(df['City'] =='Seattle') && (df['City'] =='New York City') ])
##print(df[df['City'].notnull()  & (df['City'] == "New York City")])
##print(df[df['City']=='Seattle'  |  (df['City'] == "New York City")])

##df3 = df[(df['City']=='Seattle') | (df['City'] == "New York City")]
####print(df3)
####print(df3.loc[68])
##print("===============")
##print(df3.drop([96,41,68]))

##print(df[(df.City=='Aberdeen')])
##print(df[(df.City=='Aberdeen')])
##print(df.groupby('City').sum())
##print(df.loc[(df['City'] == 'Aberdeen') & (df['City'] == 'Abilene')])
##print(df[['City']].sort)City
##print(df['City'].where(df1['City'] =='Abbeville'))

# Removing column
##print(df.columns)
##list_drop = ['Time', 'Shape Reported','Colors Reported']
##df.drop(list_drop, axis=1, inplace=True)
####ufo.head()
##print(df.columns)

# Removing rows 0 and 1
# axis=0 is the default, so technically, you can leave this out
##rows = [0, 1]
##ufo.drop(rows, axis=0, inplace=True)


# examine duplicated rows
##print(df.dtypes)
##print(df.loc['City'.duplicated(), :])
##print(df.shape)
##print(df.drop_duplicates(keep='first').shape)
##print(df.loc['City'.duplicated(keep='last'), :])
##users.loc[users.duplicated(), :]
df1 = df.drop_duplicates(subset=['first_names', 'last_names'] )
df2 = df1.drop_duplicates(subset=['ss', 'fs'] )
df2=df1.loc[df1.duplicated(), :]

print(df1.shape)
df2=df1.loc[df1['fs'].duplicated(), :]
print(df2.shape)

    print(df1.shape)
    df2=df1.loc[df1['fs'].duplicated(), :]
    print(df2.sort_values(by=['fs'],ascending=False))
    print(df2.shape)

##print(df.head())
####print(df.index)
##df.reset_index(drop=True)
##df.set_index('City',inplace=True)
####print(df.index)
##print(df.head())
##print (df.groupby(['City']).size().sort_values(ascending=False))
##print(df.loc[['City']])
