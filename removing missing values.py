# to remvoe any row or column, we can use dropna()
# df.dropna(axis=0,inplcae=True)  axis=0 is for deleting row
# df.dropna(axis=1,inplcae=True)  axis=0 is for deleting column

import pandas as pd
data = {
    "Name":["Swapnil",None,"Jagjeet","Arnab","Piyish","Praneet","Shreya","Abhay"],
    "Salary":[26000,32000,50000,61000,45000,None,15000,67000],
    "Performance Score":[85,62,80,75,79,86,94,None]
}
df=pd.DataFrame(data)
# if we dont specfify axis then both row and column will be deleted
df.dropna(inplace=True)
print(df)