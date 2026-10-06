import pandas as pd

data_frame = pd.read_csv("Cars93_missing.csv")

print("Column names:")
print(data_frame.columns)

print("\nMissing values:")
print(data_frame.isna().sum())

print("\nTotal missing values:")
total_missing = list(data_frame.isna().sum())
print(sum(total_missing))