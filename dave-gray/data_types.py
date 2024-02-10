# Numeric data types
import math

# integer type
price = 100
best_price = int(80.001)
print(type(price))
print(isinstance(best_price, int))

# float type
gpa = 3.28
y = float(1)
print(type(gpa))
print(isinstance(y, float))

# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers
gpa = 3.28
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))
