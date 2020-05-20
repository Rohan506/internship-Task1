import pandas as pd
data=pd.read_csv("D:\Study\Intern\diamonds.csv")
print("Original DataFrame")
print(data.shape)
print("Sample 75% of diamond datFrame's row without replacement:")
result= data.sample(frac=0.75, random_state=99)
print(result)
print("Remaining 25% of the row")
print(data.loc[data.index.isin(result.index),:])
