import pandas as pd
df=pd.read_excel("products.xlsx", "Sheet1")
print df.head(3)
result= df.pivot(index= 'ID', columns='Product', values='Sales') 
print result.head(3)