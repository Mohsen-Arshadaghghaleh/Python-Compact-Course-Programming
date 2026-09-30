def convert(x):
    return list(x)

strings = ["Digital Transformation", "Dortmund", "Python Week2", "Winter Semester"]

result = map(convert, strings)

for item in result:
    print("Converted: ",list(item))