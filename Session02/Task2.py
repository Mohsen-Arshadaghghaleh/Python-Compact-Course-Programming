s1 = "ab5ff10fc12de3g1go ee20 m 6 j100m"
s2 = "fahskdnc qfhna h qoi hjkasdnn ah qlkjk"

numbers = []
current_number = ""

for item in s1:
    if item.isdigit():
        current_number += item
    else:
        if current_number != "":
            numbers.append(int(current_number))
            current_number = ""

if current_number != "":
    numbers.append(int(current_number))

total = sum(numbers)
count = len(numbers)

if count > 0:
    average = total / count
    print("Sum:", total)
    print("Average:", average)
else:
    average = 0
    print("There is no number in your string")

