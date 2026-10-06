import pandas as pd

data_frame = pd.read_csv("Cars93_missing.csv")
print(data_frame["Min.Price"].head(10))

average = data_frame["Min.Price"].mean()

print("Min.Price:", average, "\n")

data_frame["Min.Price"] = data_frame["Min.Price"].fillna(average)

print(data_frame["Min.Price"].head(10))
