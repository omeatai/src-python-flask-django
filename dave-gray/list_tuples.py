users = ['Dave', 'John', 'Sara']
data = ['Dave', 42, True]
empty_list = []

print("Dave" in users)
print("Dave" in data)
print("Dave" in empty_list)
print("")

print(users[0])
print(users[-2])
print("")

# FInd index of value
print(users.index('Sara'))
print("")

# Slice from List
print(users[0:2])
print(users[1:])
print(users[-3:-1])
print(users[:])
print("")

# Find length of List
print(len(data))
print("")

# Append/Extend to List
users.append('Elsa')
print(users)

users += ['Jason']
print(users)

users.extend(['Robert', 'Jimmy'])
print(users)

data = ['Alex', 'Peter']
users.extend(data)
print(users)
print("")

# Insert to List
users = ['Fred', 'John']

users.insert(0, 'Bob')
print(users)

users[2:2] = ['Eddie', 'Alex', 'Bob', 'Stewart']
print(users)

users[2:4] = ['Robert', 'JPJ']
print(users)
print("")

# Remove from List
users.remove('Bob')
print(users)

popped = users.pop()
print(users)
print(popped)

popped = users.pop(2)
print(users)
print(popped)

del users[0]
print(users)

data.clear()  # del data
print(data)
print("")

# Sort List
users = ['Bob', 'Fred', 'John']
print(users)

users[1:2] = ['eddie']
print(users)

users.sort()
print(users)

users.sort(key=str.lower)
print(users)
print("")

nums = [4, 42, 78, 1, 5]
print(nums)
nums.reverse()
print(nums)

print(sorted(nums, reverse=True))
print(nums)

# nums.sort(reverse=True)
# print(nums)

# Copy List
nums = [4, 42, 78, 1, 5]

nums_copy1 = nums.copy()
print(nums_copy1)

nums_copy2 = list(nums)
print(nums_copy2)

nums_copy3 = nums[:]
print(nums_copy3)

nums.sort()
print(nums)
print(type(nums))

my_list = list([1, "Neil", True])
print(my_list)
