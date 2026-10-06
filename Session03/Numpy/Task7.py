import numpy as np

dtype = [("position", [("x", float), ("y", float)]), ("color", [("r", int), ("g", int), ("b", int)])]

data = np.array([((10, 20), (255, 0, 0)), ((30, 40), (255, 255, 255))], dtype=dtype)

print(data)

print(data["position"]["x"])
print(data["position"]["y"])

print(data["color"]["r"])
print(data["color"]["g"])
print(data["color"]["b"])