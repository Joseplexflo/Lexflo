# %%

import pandas as pd
df = pd.DataFrame()
d = {'columna1': [1, 2], 'columna2': [3, 4]}
df = pd.DataFrame(data=d)
df
print(df)
# %%
import utils as ut
misuma = ut.suma(1,2)
# %%
df1 = ut.procesarpandas(df)
# %%
