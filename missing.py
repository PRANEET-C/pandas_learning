# NaN-it means not a number, ti is used for numbers
# null-it is used for objects
# to know if there is missign value, pandas has isnull() method
# this gives boolean value, if True then value is missing else not

import pandas as pd

data = {
    "Name":["Swapnil",None,"Jagjeet","Arnab","Piyish","Praneet","Shreya","Abhay"],
    "Salary":[26000,32000,50000,61000,45000,None,15000,67000],
    "Performance Score":[85,62,80,75,79,86,94,None]
}
df=pd.DataFrame(data)
# wherever data is missing, isnull() will give True otherrwise False
print(df.isnull())

# to get a count of number of missing values, sum() function is there
print(df.isnull().sum())