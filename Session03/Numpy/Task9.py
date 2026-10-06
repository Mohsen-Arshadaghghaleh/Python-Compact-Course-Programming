import numpy as np

A = np.random.random(5)
B = np.random.random(5)

print("A:", A)
print("B:", B)

print(np.array_equal(A, B))
print(A==B)