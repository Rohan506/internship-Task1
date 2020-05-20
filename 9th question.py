import pandas as pd
data=pd.read_csv("D:\Study\Intern\diamonds.csv")
print("count, minimum, maximum price for each cut of diamonds DataFrame")
print(data.groupby('cut').price.agg(['count','min','max']))
