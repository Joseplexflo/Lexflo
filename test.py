# %%
import pandas as pd
import utils as ut
df = pd.DataFrame()
d = {'columna1': [1, 2], 'columna2': [3, 4]}
df = pd.DataFrame(data=d)
# utilizando mi function suma
misuma = ut.suma(1,2)
df1 = ut.procesarpandas(df)

# descargar df en archivo csv sin indice
df1.to_csv('archivo.csv', index=False)

# %%
