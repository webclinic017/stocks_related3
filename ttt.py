import pandas as pd
import numpy as np
def manipulate_df(df_local):
    df_local.rename(columns={'A': 'grouping_column'}, inplace = True)
    df_local.drop('B', axis=1, inplace=True)
##    df_local.drop(df.query('grouping_column not in (\'1\', \'0\')').index, inplace = True)
##    df_local = df_local.groupby(['grouping_column'])['C'].sum().to_frame().reset_index().copy()
    df['grouping_column'].loc[2]=79888
    df['C'].loc[2]=79888
    print("this is what I need:")
    print(df_local)



df = pd.DataFrame(np.random.randint(0,10,size=(100, 3)), columns=list('ABC'))
print(df)
manipulate_df(df)
print("this is what I got:")
print(df.head(5))    
