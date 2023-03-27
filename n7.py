import pandas as pd
import numpy as np
idx0 = np.array(['bar', 'bar', 'bar', 'baz', 'foo', 'foo'])
idx1 = np.array(['one', 'two', 'three', 'one', 'one', 'two'])
df = pd.DataFrame(index = [idx0, idx1], columns = ['A', 'B'])
s = pd.Series([True, False, True],index = np.unique(idx0))
print (df)
print (s)
