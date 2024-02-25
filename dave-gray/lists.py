# Python Lists

users = ['Dave', 'John', 'Sara']
data = ['Dave', 42, True]
empty_list = []

print("Dave" in users)  # True
print("Dave" in data)  # True
print("Dave" in empty_list)  # False
print("")

print(users[0])  # Dave
print(users[-2])  # John
print("")

# FInd index of value
print(users.index('Sara'))  # 2
print("")

# Slice from List
print(users[0:2])  # ['Dave', 'John']
print(users[1:])  # ['John', 'Sara']
print(users[-3:-1])  # ['Dave', 'John']
print(users[:])  # ['Dave', 'John', 'Sara']
print("")

# Find length of List
print(len(data))  # 3
print("")

# Append/Extend to List
users.append('Elsa')
print(users)  # ['Dave', 'John', 'Sara', 'Elsa']

users += ['Jason']
print(users)  # ['Dave', 'John', 'Sara', 'Elsa', 'Jason']

users.extend(['Robert', 'Jimmy'])
print(users)  # ['Dave', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']

data = ['Alex', 'Peter']
users.extend(data)
print(users)
# ['Dave', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy', 'Alex', 'Peter']
print("")

# Insert to List
users = ['Fred', 'John']

users.insert(0, 'Bob')
print(users)  # ['Bob', 'Fred', 'John']

users[2:2] = ['Eddie', 'Alex', 'Bob', 'Stewart']
print(users)  # ['Bob', 'Fred', 'Eddie', 'Alex', 'Bob', 'Stewart', 'John']

users[2:4] = ['Robert', 'JPJ']
print(users)  # ['Bob', 'Fred', 'Robert', 'JPJ', 'Bob', 'Stewart', 'John']
print("")

# Remove from List
users.remove('Bob')
print(users)  # ['Fred', 'Robert', 'JPJ', 'Bob', 'Stewart', 'John']

popped = users.pop()
print(users)  # ['Fred', 'Robert', 'JPJ', 'Bob', 'Stewart']
print(popped)  # John

popped = users.pop(2)
print(users)  # ['Fred', 'Robert', 'Bob', 'Stewart']
print(popped)  # JPJ

del users[0]
print(users)  # ['Robert', 'Bob', 'Stewart']

# del data
data.clear()
print(data)  # []
print("")

# Sort List
users = ['Bob', 'Fred', 'John']
print(users)  # ['Bob', 'Fred', 'John']

users[1:2] = ['eddie']
print(users)  # ['Bob', 'eddie', 'John']

users.sort()
print(users)  # ['Bob', 'John', 'eddie']

users.sort(key=str.lower)
print(users)  # ['Bob', 'eddie', 'John']
print("")

nums = [4, 42, 78, 1, 5]
print(nums)  # [4, 42, 78, 1, 5]
nums.reverse()
print(nums)  # [5, 1, 78, 42, 4]

print(sorted(nums, reverse=True))  # [78, 42, 5, 4, 1]
print(nums)  # [5, 1, 78, 42, 4]

# nums.sort(reverse=True)
# print(nums)

# Copy List
nums = [4, 42, 78, 1, 5]
nums_copy1 = nums.copy()
print(nums_copy1)  # [4, 42, 78, 1, 5]

nums_copy2 = list(nums)
print(nums_copy2)  # [4, 42, 78, 1, 5]

nums_copy3 = nums[:]
print(nums_copy3)  # [4, 42, 78, 1, 5]

nums.sort()
print(nums)  # [1, 4, 5, 42, 78]
print(type(nums))  # <class 'list'>

my_list = list([1, "Neil", True])
print(my_list)  # [1, 'Neil', True]
