# String data type

# literal assignment
first = "Dave"
last = "Johnson"

print(first, type(first))  # Dave <class 'str'>
print(type(first) == str)  # True
print(isinstance(first, str))  # True

# constructor function
pizza = str("Pepperoni")
print(pizza, isinstance(pizza, str))  # Pepperoni True

# Concatenation
fullname = first + " " + last
fullname += "!"
print(fullname)  # Dave Johnson!

# Casting a number to a string
decade = str(1980)
print(decade, type(decade))  # 1980 <class 'str'>
statement = "I like rock music from the " + decade + "s."
print(statement)  # I like rock music from the 1980s.

# Multiple lines
multiline = '''
Hey, how are you?

I was just checking in.   All good?
                    - Dave
'''
print(multiline)
# Hey, how are you?
#
# I was just checking in.   All good?
#                    - Dave

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this \\located?'
print(sentence)
# I'm back at work!	Hey!
#
# Where's this \located?

# String Methods
first = "Dave"
print(first)  # Dave
print(first.lower())  # dave
print(first.upper())  # DAVE

multiline = "hey, how are you?"
print(multiline)  # hey, how are you?
print(multiline.title())  # Hey, How Are You?
print(multiline.replace("hey", "Welcome"))  # Welcome, how are you?
print(len(multiline))  # 17
multiline += "                                        "
multiline = "                  " + multiline
print(len(multiline))  # 75
print(len(multiline.strip()))  # 17
print(len(multiline.lstrip()))  # 57
print(len(multiline.rstrip()))  # 35

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))
print("Tea".ljust(16, ".") + "$1".rjust(4))

# ========MENU========
# Coffee..........  $1
# Muffin..........  $2
# Cheesecake......  $4
# Tea.............  $1

# string index values
first = "Dave"
print(first[1])  # a
print(first[-1])  # e
print(first[1:-1])  # av
print(first[1:])  # ave

# Some methods return boolean data
print(first.startswith("D"))  # True
print(first.endswith("Z"))  # False
