s1 = "f10h3a f5a65sdks14h f1kj3as1df1 k23ja55sfk6 10jhas2dk3jh2 0f 100 66"
s2 = " hkjahkj fash ashkjf hash fasshf ashjkfh askjlfhlakhfuihjkweoiqruoewq uoq"
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
    print("There are no numbers in your string")
