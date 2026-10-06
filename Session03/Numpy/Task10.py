import numpy as np

points = np.random.random((100, 2))
print(points.shape)

distances = np.linalg.norm(points, axis=1)
print(distances)