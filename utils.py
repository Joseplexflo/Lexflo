def suma(a,b):
    return a+b
def procesarpandas(df):
    dfresult = df.copy()
    temporal = df["columna1"]+df["columna2"]
    dfresult["resultado"] = temporal + 3
    return dfresult