import numpy as np

matrix = np.random.random((5, 5))

normalize = (matrix - matrix.min()) / (matrix.max() - matrix.min())

print(normalize)