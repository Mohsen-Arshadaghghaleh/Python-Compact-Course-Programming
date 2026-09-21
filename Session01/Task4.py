def factorial_rec(number):
    if number < 0:
        return "Factorial is not defined for negative numbers"
    if number == 0 or number == 1:
        return 1
    return number * factorial_rec(number - 1)

# Test
inputNumber = int(input("Enter a number to calculate its factorial: "))
print(f"{inputNumber}! = {factorial_rec(inputNumber)}")