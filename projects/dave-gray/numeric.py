# Numeric data types
import math

# integer type
price = 100
best_price = int(80.001)
print(type(price))  # <class 'int'>
print(isinstance(best_price, int))  # True

# float type
gpa = 3.28
y = float(1)
print(type(gpa))  # <class 'float'>
print(isinstance(y, float))  # True

# complex type
comp_value = 5+3j
print(type(comp_value))  # <class 'complex'>
print(comp_value.real)  # 5.0
print(comp_value.imag)  # 3.0

# Built-in functions for numbers
gpa = 3.28
print(abs(gpa * -1))  # 3.28
print(round(gpa))  # 3
print(round(gpa, 1))  # 3.3
print(math.pi)  # 3.141592653589793
print(math.sqrt(64))  # 8.0
print(math.ceil(gpa))  # 4
print(math.floor(gpa))  # 3

# Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))  # <class 'int'>
