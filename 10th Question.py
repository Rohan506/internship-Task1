#Write a Pandas program to check the number of rows and columns and drop
# those row if 'any' values are missing in a row of diamonds DataFrame.

import pandas as pd
data = pd.read_csv("D:\Study\Intern\diamonds.csv")
print("Original Datafrrame")
print("Number of rows and column")

print(data.shape)
print("After dropping rows where values are missing")

print(data.dropna(how='any').shape)
