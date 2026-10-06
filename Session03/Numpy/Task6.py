import numpy as np

x = np.random.uniform(0, 10, 5)
print(x)

method1 = x.astype(int)
print(method1)

method2 = np.floor(x).astype(int)
print(method2)

method3 = np.trunc(x).astype(int)
print(method3)

method4 = (x // 1).astype(int)
print(method4)

fraction, integer = np.modf(x)
method5 = integer.astype(int)
print(method5)