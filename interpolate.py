'''
interpolation helps to-
avoid missing datas
smooth consistency in data

There arer three types of interpolation: linear, polynomial,time
'''
import pandas as pd
data = {
    "Name":["Swapnil","Shyam","Jagjeet","Arnab","Piyish","Praneet","Shreya","Abhay"],
    "Salary":[26000,32000,50000,61000,45000,None,15000,67000],
    "Performance Score":[85,62,80,75,79,86,94,None]
}
df=pd.DataFrame(data)
# to interpolate only on salary column
df["Salary"]=df["Salary"].interpolate(method="linear")
# inplcae interpolation on entire dataframe
df.interpolate(method="linear",inplace=True)
print(df)