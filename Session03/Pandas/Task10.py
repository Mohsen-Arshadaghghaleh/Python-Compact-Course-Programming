import pandas as pd
import matplotlib.pyplot as plt

data_frame = pd.read_csv("Cars93_missing.csv")

correlation_matrix = data_frame.corr(numeric_only=True)

print(correlation_matrix)


plt.imshow(correlation_matrix, cmap="coolwarm")

plt.colorbar()
plt.xticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns,
    rotation=90
)
plt.yticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns
)

plt.title("Correlation Matrix")
plt.show()