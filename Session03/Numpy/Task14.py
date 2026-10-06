import numpy as np

A = np.random.randint(1, 10, (16, 16))
print(A)

block_sum = A.reshape(4, 4, 4, 4).sum(axis=(1, 3))
print(block_sum)