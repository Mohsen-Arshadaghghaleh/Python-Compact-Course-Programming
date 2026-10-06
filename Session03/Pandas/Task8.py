import pandas as pd

dict1 = {"City": ["Dortmund", "Berlin", "Cologne"], "Population": [614495, 3700000, 1025523]}
data_frame1 = pd.DataFrame(dict1)
print(data_frame1)

dict2 = {"City": ["Dortmund", "Berlin", "Cologne"], "Postal-Codes": ["44001-44388", "10115-14199", "50441–51149"]}
data_frame2 = pd.DataFrame(dict2)
print(data_frame2)

merged = pd.merge(data_frame1, data_frame2, on="City")
print(merged)
