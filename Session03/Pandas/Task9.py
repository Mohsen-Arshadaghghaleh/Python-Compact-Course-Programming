import pandas as pd
import matplotlib.pyplot as plt

data_frame = pd.read_csv("Cars93_missing.csv")

average = data_frame["Price"].mean()
print("Average Price:", average, "\n")
data_frame["Price"] = data_frame["Price"].fillna(average)

plt.hist(data_frame["Price"])

plt.xlabel("Price")
plt.ylabel("Frequency")
plt.title("Price Histogram")

plt.show()