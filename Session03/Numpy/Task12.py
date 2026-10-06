import numpy as np

A = np.array([[3, 8, 2], [1, 5, 7], [9, 2, 4], [6, 4, 1]])
n = 0
result = A[A[:, n].argsort()]
print(result)
