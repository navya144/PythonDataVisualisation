import pandas as pd
df=pd.read_excel('sort.xlsx', 'DATA') #Add by variable name(s) to sort
print df
print df.sort(['Product','Sales'], ascending=[True, False])

### Sort function is deprecated, use sort_values (http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_values.html)
### or sort_index(http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_index.html)