import pandas as pd

data_frame = pd.read_csv("Cars93_missing.csv")
print(data_frame["Price"].head(20))

lower = data_frame["Price"].quantile(0.05)
upper = data_frame["Price"].quantile(0.95)

print("\n\nLower:",lower, "\nUpper:", upper)

data_frame_percent = data_frame[(data_frame["Price"] >= lower) & (data_frame["Price"] <= upper)]

print("\n",data_frame_percent["Price"].head(20))
