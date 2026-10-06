import numpy as np

today = np.datetime64('today')
yesterday = today - np.timedelta64(1, 'D')
tomorrow = today + np.timedelta64(1, 'D')

print("Today:", today)
print("Yesterday:", yesterday)
print("Tomorrow:", tomorrow)