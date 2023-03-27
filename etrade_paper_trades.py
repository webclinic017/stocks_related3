import csv
import pandas as pd
import re
##import textwrap

pd.options.display.width = 0
pd.set_option('display.max_columns', None)
pd.options.display.float_format = '{:.2f}'.format
##pd.options.display.max_columns=255
pd.options.display.max_rows=6500000
pd.set_option('display.max_colwidth', 200)
pd.set_option('display.max_columns', 0)

df=pd.read_csv('/home/az2/Downloads/'+'Orders (22).csv',skiprows=1)

df.reset_index(inplace=True)
##print(df)

p='Stop'
p2='Limit'
p3='Sell'
p4='>'
p5='<='
df3=pd.DataFrame()
df4=pd.DataFrame()
df5=pd.DataFrame()
df6=pd.DataFrame()
df7=pd.DataFrame()

print(df)

for x in df.index:
#    print(df.loc[x])    coontain stop and limit
    if (len(re.findall(p, df['Description'].loc[x])) >0) and (len(re.findall(p2, df['Description'].loc[x])) >0):
        df3=df3.append(df.loc[x])

for x in df.index:
#    print(df.loc[x])   coontain stop and sell
    if (len(re.findall(p, df['Description'].loc[x])) < 1) and (len(re.findall(p2, df['Description'].loc[x])) >0):
        df4=df4.append(df.loc[x])

for x in df.index:
#    print(df.loc[x])  coontain stop,sell and limit.
    if (len(re.findall(p, df['Description'].loc[x])) > 0) and (len(re.findall(p2, df['Description'].loc[x])) >0) and (len(re.findall(p3, df['Description'].loc[x])) > 0):
        df5=df5.append(df.loc[x])

for x in df.index:
#    print(df.loc[x])  coontain stop,sell and limit.
    if (len(re.findall(p4, df['Description'].loc[x])) > 0):
        df6=df6.append(df.loc[x])   



for x in df.index:
#    print(df.loc[x])  coontain stop,sell and limit.
    if (len(re.findall(p5, df['Description'].loc[x])) > 0):
        df7=df7.append(df.loc[x])           
        
df7.to_csv('/home/az2/Downloads/pp788.csv')   
##print(df[['Description','Fill','Market','Symbol','Status']])
##print('with stop, with limit')
##print(df3[['Description','Fill','Market','Symbol','Status']])


##print('Buy only and limit only [no stop]')
##print(df4[['Description','Fill','Market','Symbol','Status']])
##print('Buy only and limit only - [no sell]')
print(df7[['Description','Fill','Market','Symbol','Status']])
##print(df5[['Description','Fill','Market','Symbol','Status']])
##print(df5['Description'][:4])

##textwrap.wrap(text=sample_text, width=25)
##df=df[df['Symbol'] != '--']
##df=df[df['Account'] != 'Paper Trade Account']
##dd=pd.DataFrame()
##print(df)
##print(df.filter(regex='^Paper', axis=1))
##
##df[df['Description'].str.count('^[pP].*')>0]
##df[df['Description'].str.match('^Call.*')== True]

##p=[]
##u=df.filter(regex='^SPY', axis=1)
##p.append(u)
##print(u.loc[9])


##for x in u:
##    print(df.loc[x])

##df=df[df['Symbol'] != 'Paper']
##df=df.filter(regex='^(?!Paper).*', axis=1)

##print(df)

##for x in df.index:
####    print(df['Symbol'].loc[x])
####    if 'SPY' in df['Symbol'].loc[x]:
##    if 'Stop to Close' in df['Description'].loc[x]:    
##        dd=dd.append(df.loc[x])
##
##dd2=pd.DataFrame()
##for x in dd.index:
####    print(dd.loc[x])
##    if 'Paper' not in dd['Account'].loc[x]:
##        print(dd.loc[x])
####        dd2=dd2.append(dd.loc[x])
##
##

# ['Account', 'Description', 'Fill', 'ID', 'Market', 'Status', 'Symbol','Time', 'index'],
##print(dd2[['Account']])
