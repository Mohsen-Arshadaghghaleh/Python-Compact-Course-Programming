import pandas as pd

data_frame = pd.read_csv("Cars93_missing.csv")

#data_frame.index = data_frame["Model"]
#print(data_frame.head())

data_frame = data_frame.set_index("Model")
print(data_frame.head())