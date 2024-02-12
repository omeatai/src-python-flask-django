# Tuples
my_tuple = tuple(('Dave', 42, True))
print(my_tuple)

another_tuple = (1, 4, 2, 8, 2, 2)
print(another_tuple)

print(type(my_tuple))
print(type(another_tuple))
print("")

new_list = list(my_tuple)
print(new_list)
new_list.append('Neil')
print(new_list)
new_tuple = tuple(new_list)
print(new_tuple)
print("")

# unpacking Tuples
another_tuple = (1, 4, 2, 8, 2, 2)
print(another_tuple)
(one, *two, hey) = another_tuple
print(one)
print(two)
print(hey)
print(another_tuple.count(2))
