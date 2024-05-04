# Assignment Operators
name = "Dave"
print(name)  # Dave

# Arithmetic Operators
a = 2 + 2
b = 4 - 2
c = 24 / 5
d = 24 // 5
e = round(24 / 5)
f = 24 % 5
g = 2 ** 5

print("a", a, "b", b, "c", c, "d", d, "e", e, "f", f, "g", g)
# a 4 b 2 c 4.8 d 4 e 5 f 4 g 32

meaning = 42
meaning += 1
print(meaning)  # 43
meaning -= 1
print(meaning)  # 42
meaning *= 10
print(meaning)  # 420
meaning /= 10
print(meaning)  # 42.0
meaning = round(meaning)
print(meaning)  # 42

# Comparison Operators
print(2 == 2)  # True
print(2 != 2)   # False
print(3 != 2)  # True
print(10 > 2)  # True
print(10 < 2)  # False
print(10 >= 10)  # True

if meaning > 10:
    print('Right on!')  # Right on!
else:
    print('Not today')

# Ternary Operator
print('Great!') if meaning > 10 else print('Not today')
# Great!
