#Write a Pandas program to count the duplicate rows of diamonds DataFrame
import pandas as pd
data=pd.read_csv("D:\Study\Intern\diamonds.csv")
print("Original DataFrame")
print(data.shape)
print("Duplicate rows of diamond DataFrames:")
print(data.duplicated().sum())
