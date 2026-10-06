import numpy as np

matrix = np.random.random((5, 5))

result = matrix - matrix.mean(axis=1, keepdims=True)
print(result)
