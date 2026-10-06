import numpy as np

matrix = np.array([[1, 2, 3], [2, 4, 6], [1, 1, 1]])

rank = np.linalg.matrix_rank(matrix)

print("Rank:", rank)
