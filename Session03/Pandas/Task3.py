import pandas as pd

data_frame = pd.read_csv("Cars93_missing.csv")

data_frame.loc[data_frame["MPG.city"] > 25, "MPG.city"] = 25
print(data_frame["MPG.city"].head(40))