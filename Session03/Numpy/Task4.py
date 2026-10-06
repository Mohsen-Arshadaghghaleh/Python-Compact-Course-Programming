import numpy as np

A = np.random.random((5, 3))
B = np.random.random((3, 2))

C = np.dot(A, B)

print(C)
print(C.shape)