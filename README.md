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
<summary>3. Data Type - Numeric </summary>

# Data Type - Numeric

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

```py

```

```py

```

# #END</details>
