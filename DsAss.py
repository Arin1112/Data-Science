import pandas as pd
import numpy as np

data=pd.read_csv('olympics.csv')
print(data)

df=pd.DataFrame(data)
print("First Country ")
print(df.take([1]))

max=0
max1=0
for i in range (1,29):
    if(df.iat[i,2]>max):
        max=df.iat[i,2]

for i in range (118,146):
    if(df.iat[i,2]>max):
        max1=df.iat[i,2]

for i in range (1,146):
    if max>max1:
        if(df.iat[i,2] == max):
            break
    elif max<max1:
        if(df.iat[i,2] == max1):
            break

print("Most Summer Gold medals :",df.iat[i,0])
