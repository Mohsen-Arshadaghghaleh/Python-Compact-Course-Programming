import pandas as pd

data_frame = pd.read_csv("Cars93_missing.csv")

def exchange_columns(df, column1, column2):
    columns = list(df.columns)

    i = columns.index(column1)
    j = columns.index(column2)

    columns[i], columns[j] = columns[j], columns[i]

    return df[columns]

print(data_frame.head())

data_frame = exchange_columns(data_frame, "Model", "Type")
print(data_frame.head())

data_frame = data_frame.sort_index(axis=1)
print(data_frame.head())