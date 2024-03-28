# while loop
value = 1
arr = []
while value <= 10:
    arr.append(value)
    value += 1
print(arr)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# while loop with break
value = 1
arr = []
while value <= 10:
    if value == 5:
        break
    arr.append(value)
    value += 1
print(arr)  # [1, 2, 3, 4]

# while loop with continue
value = 0
arr = []
while value <= 10:
    value += 1
    if value == 5:
        continue
    arr.append(value)
else:
    print("Value is now " + str(value))  # Value is now 11
print(arr)  # [1, 2, 3, 4, 6, 7, 8, 9, 10, 11]
print("")

# for loop on List
names = ["Dave", "Sara", "John"]
for x in names:
    print(x)
# Dave
# Sara
# John

# for loop on String
y = ""
for x in "Mississippi":
    y += x
print(y)  # Mississippi

# for loop on List with break
names = ["Dave", "Sara", "John"]
for x in names:
    if x == "Sara":
        break
    print(x)  # Dave

# for loop on List with continue
names = ["Dave", "Sara", "John"]
for x in names:
    if x == "Sara":
        continue
    print(x)
print("")
# Dave
# John

# for loop in range
y = ""
for x in range(4):
    y += str(x)
print(y)  # 0123

# for loop in range with start/stop
y = ""
for x in range(2, 4):
    y += str(x)
print(y)
print("")  # 23

# for loop in range with start/stop/step
y = []
for x in range(5, 101, 5):
    y.append(x)
else:
    print("Glad that\'s over!")
print(y)
# Glad that's over!
# [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
print("")

# nested for loop
names = ["Dave", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

for name in names:
    for action in actions:
        print(name + " " + action + ".")
# Dave codes.
# Dave eats.
# Dave sleeps.
# Sara codes.
# Sara eats.
# Sara sleeps.
# John codes.
# John eats.
# John sleeps.

# for action in actions:
#     for name in names:
#         print(name + " " + action + ".")
