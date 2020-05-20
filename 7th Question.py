import pandas as pd
data = pd.read_csv("D:\Study\Intern\diamonds.csv")
df = pd.DataFrame(data )
print("First five row of the data frame")
print(df.iloc[:5])

