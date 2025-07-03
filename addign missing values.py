# to fill missing values we use fillna()
# fillna(default value, inplace=True)

import pandas as pd
data = {
    "Name":["Swapnil",None,"Jagjeet","Arnab","Piyish","Praneet","Shreya","Abhay"],
    "Salary":[26000,32000,50000,61000,45000,None,15000,67000],
    "Performance Score":[85,62,80,75,79,86,94,None]
}
df=pd.DataFrame(data)
# the below code will fill all the missing values with 0
# df.fillna(0,inplace=True)

# the below code will fill missing values of salary with mean
df["Salary"].fillna(df["Salary"].mean(),inplace=True)
df["Performance Score"].fillna(df["Performance Score"].mean(),inplace=True)
print(df)

