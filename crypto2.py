

import cbpro
import time
import pandas as pd
import json

pd.options.display.max_rows=9999
pd.options.display.max_columns=15
##pd.options.display.max_colwidth


data = []
timeout = time.time() + 5
public_client = cbpro.PublicClient()
m=public_client.get_time()
print(m)

while time.time() < timeout:
    data.append(public_client.get_product_ticker(product_id='BTC-USD'))
##    time.sleep(0.5)

df = pd.DataFrame(data)
print(df)
