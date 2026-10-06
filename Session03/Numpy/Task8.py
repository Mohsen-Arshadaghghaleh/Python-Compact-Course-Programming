import numpy as np

def generate_numbers():
    for i in range(10):
        yield i

generator = generate_numbers()

array = np.array(list(generator))

print(array)