import pandas as pd

df=pd.read_excel("products.xlsx", "Sheet1")
print df
result= df.pivot(index= 'ID', columns='Product', values='Sales')    # pivot function transposes data
print result