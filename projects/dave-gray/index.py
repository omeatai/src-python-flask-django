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
