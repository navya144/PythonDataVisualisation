import pandas as pd
df=pd.read_excel("store.xls", "Orders") # Load Orders sheet of excel file store
print df.head(3)
