# Tuples
my_tuple = tuple(('Dave', 42, True))
print(my_tuple)  # ('Dave', 42, True)

another_tuple = (1, 4, 2, 8, 2, 2)
print(another_tuple)  # (1, 4, 2, 8, 2, 2)

print(type(my_tuple))  # <class 'tuple'>
print(type(another_tuple))  # <class 'tuple'>
print("")

new_list = list(my_tuple)
print(new_list)  # ['Dave', 42, True]
new_list.append('Neil')
print(new_list)  # ['Dave', 42, True, 'Neil']
new_tuple = tuple(new_list)
print(new_tuple)  # ('Dave', 42, True, 'Neil')
print("")

# unpacking Tuples
another_tuple = (1, 4, 2, 8, 2, 2)
print(another_tuple)  # (1, 4, 2, 8, 2, 2)
(one, *two, hey) = another_tuple
print(one)  # 1
print(two)  # [4, 2, 8, 2]
print(hey)  # 2
print(another_tuple.count(2))  # 3
