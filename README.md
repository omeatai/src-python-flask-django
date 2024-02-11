# Python-Flask-Django - src

+Dave Gray - Python-Flask

<details>
<summary>1. Python Operators </summary>

# Python Operators

```py
# Assignment Operators
name = "Dave"
print(name)

# Arithmetic Operators
a = 2 + 2
b = 4 - 2
c = 24 / 5
d = 24 // 5
e = round(24 / 5)
f = 24 % 5
g = 2 ** 5

print("a", a, "b", b, "c", c, "d", d, "e", e, "f", f, "g", g)

meaning = 42
meaning += 1
print(meaning)
meaning -= 1
print(meaning)
meaning *= 10
print(meaning)
meaning /= 10
print(meaning)
meaning = round(meaning)
print(meaning)

# Comparison Operators
print(2 == 2)
print(2 != 2)
print(3 != 2)
print(10 > 2)
print(10 < 2)
print(10 >= 10)

if meaning > 10:
    print('Right on!')
else:
    print('Not today')

# Ternary Operator
print('Great!') if meaning > 10 else print('Not today')
```

<img width="1136" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/5a0fd9b7-aa1b-43a6-9f6b-93698862cb56">

# #END</details>

<details>
<summary>2. Data Type - String </summary>

# Data Type - String

[https://github.com/omeatai/src-python-flask-django/commit/786257d573dc94eea4ad0f451ed2a64fea47244c](https://github.com/omeatai/src-python-flask-django/commit/786257d573dc94eea4ad0f451ed2a64fea47244c)

```py
# String data type

# literal assignment
first = "Dave"
last = "Johnson"

print(first, type(first))
print(type(first) == str)
print(isinstance(first, str))

# constructor function
pizza = str("Pepperoni")
print(pizza, isinstance(pizza, str))

# Concatenation
fullname = first + " " + last
fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(1980)
print(decade, type(decade))
statement = "I like rock music from the " + decade + "s."
print(statement)

# Multiple lines
multiline = '''
Hey, how are you?

I was just checking in.   All good?
                    - Dave
'''
print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this \\located?'
print(sentence)

# String Methods
first = "Dave"
print(first)
print(first.lower())
print(first.upper())

multiline = "hey, how are you?"
print(multiline)
print(multiline.title())
print(multiline.replace("hey", "Welcome"))
print(len(multiline))
multiline += "                                        "
multiline = "                  " + multiline
print(len(multiline))
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))
print("Tea".ljust(16, ".") + "$1".rjust(4))

# string index values
first = "Dave"
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# Some methods return boolean data
print(first.startswith("D"))
print(first.endswith("Z"))
```

<img width="1255" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/3338cc92-727b-42ef-8921-afd7e43f0e67">

# #END</details>

<details>
<summary>3. Data Type - Boolean </summary>

# Data Type - Boolean

[https://github.com/omeatai/src-python-flask-django/commit/a379210ee24c5a461d223e4e642654c0fa30b462](https://github.com/omeatai/src-python-flask-django/commit/a379210ee24c5a461d223e4e642654c0fa30b462)

```py
# Boolean data type
x = bool(False)
my_value = True

print(type(x))
print(isinstance(my_value, bool))

```

<img width="1255" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/397f15c1-ae2c-4dd4-90b9-979c69046bb6">

# #END</details>

<details>
<summary>4. Data Type - Numeric </summary>

# Data Type - Numeric

[https://github.com/omeatai/src-python-flask-django/commit/1586574ec08840c3a77cb2b0d93d8667af4f9ed0](https://github.com/omeatai/src-python-flask-django/commit/1586574ec08840c3a77cb2b0d93d8667af4f9ed0)

```py
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

```

<img width="1255" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/28ca3892-458f-498f-b3c7-6cae9a153cd1">

# #END</details>

<details>
<summary>5. User Input & Control Flow </summary>

# User Input & Control Flow

[https://github.com/omeatai/src-python-flask-django/commit/7493f2cdb60aad3ef4098079075f9d7e973dd24a](https://github.com/omeatai/src-python-flask-django/commit/7493f2cdb60aad3ef4098079075f9d7e973dd24a)

```py
import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


player_choice = input(
    "Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

player = int(player_choice)

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")

computer_choice = random.choice("123")
computer = int(computer_choice)

print("")
print(f"You chose {str(RPS(player)).replace("RPS.", "")}.")
print(f"Python chose {str(RPS(computer)).replace("RPS.", "")}.")
print("")

result = (player, computer)

if result == (1, 3) or result == (2, 1) or result == (3, 2):
    print("🥳😜 Congrats! You win!")
elif player == computer:
    print("😎 It's a tie!")
else:
    print("😡 Python wins!")

# References:
# print(RPS(2))           # RPS.PAPER
# print(RPS.ROCK)         # RPS.ROCK
# print(RPS['ROCK'])      # RPS.ROCK
# print(RPS.ROCK.value)   # 1
# sys.exit()

# value = input("Please enter a your name: ")
# print(value)

```

<img width="1255" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/81dcb299-16bc-4464-b192-0349a4bcbe7b">

# #END</details>

<details>
<summary>6. Lists and Tuples </summary>

# Lists and Tuples

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

# #END</details>
