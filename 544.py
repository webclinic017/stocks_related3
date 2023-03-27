import pandas as pd
import numpy as np
df = pd.DataFrame({'S': [1, 4, 5]})
##df.rolling(1, win_type='triang').sum()
print(df,'  before')
print('\n\n\n')
df=df.S.shift(1)
print(df,'ddd')

##print(df.rolling(2, win_type='triang').sum())
