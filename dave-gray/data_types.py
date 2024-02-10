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
