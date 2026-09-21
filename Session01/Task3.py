# 1- Integer to Float (Convert an integer to a floating-point number)
int_val = 42
float_val = float(int_val)
print("1- Integer to Float conversion")
print(f"int {int_val} to float: {float_val}  (type: {type(float_val).__name__})")

# 2- Float to Integer (Convert a floating-point number to an integer)
float_num = 3.99
int_num = int(float_num)
print("=================\n2- Float to Integer conversion")
print(f"float {float_num} to int: {int_num}  (type: {type(int_num).__name__})")

# 3- Integer to String (Convert an integer to a string)
num = 100
str_val = str(num)
print("=================\n3- Integer to String conversion")
print(f"int {num} to str: '{str_val}'  (type: {type(str_val).__name__})")

# 4- String to Integer (Convert a string containing a number to an integer)
str_num = "250"
int_from_str = int(str_num)
print("=================\n4- String to Integer conversion")
print(f"str '{str_num}' to int: {int_from_str}  (type: {type(int_from_str).__name__})")

# 5- Integer to Boolean (Convert an integer to a Boolean )
print("=================\n5- Integer to Boolean conversion")
print(f"int 1  to bool: {bool(1)}")
print(f"int 0  to bool: {bool(0)}")
print(f"int 42 to bool: {bool(42)}")