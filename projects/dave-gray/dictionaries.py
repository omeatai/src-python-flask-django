# Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page"
}
band2 = dict(vocals="Plant", guitar="Page")

print(band)  # {'vocals': 'Plant', 'guitar': 'Page'}
print(band2)  # {'vocals': 'Plant', 'guitar': 'Page'}
print(type(band))  # <class 'dict'>
print(len(band))  # 2
print("")

# Access items
print(band["vocals"])  # Plant
print(band.get("guitar"))  # Page
print("")

# list all keys
print(band.keys())  # dict_keys(['vocals', 'guitar'])
# list all values
print(band.values())  # dict_values(['Plant', 'Page'])
# list of key/value pairs as tuples
print(band.items())  # dict_items([('vocals', 'Plant'), ('guitar', 'Page')])
print("")

# verify a key exists
print("guitar" in band)  # True
print("triangle" in band)  # False
print("")

# Change and Add values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})
print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page', 'bass': 'JPJ'}
print("")

# Remove items
print(band.pop("bass"))  # JPJ
print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page'}
band["drums"] = "Borg"
print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Borg'}
print(band.popitem())  # ('drums', 'Borg')
print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page'}
print("")

# Delete and clear
band["drums"] = "Bonham"
print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Bonham'}
del band["drums"]
print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page'}
band2 = dict(vocals="Plant", guitar="Page")
print(band2)  # {'vocals': 'Plant', 'guitar': 'Page'}
band2.clear()
print(band2)  # {}
del band2
print("")

# Copy dictionaries
band2 = band.copy()
band2["drums"] = "Dave"
print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page'}
print(band2)  # {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Dave'}
band3 = dict(band)
print(band3)  # {'vocals': 'Coverdale', 'guitar': 'Page'}
print("")

# Nested dictionaries

member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2
}

print(band)
# {'member1': {'name': 'Plant', 'instrument': 'vocals'}, 'member2': {'name': 'Page', 'instrument': 'guitar'}}
print(band["member1"]["name"])  # Plant
print("")

# Sets
nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))

print(nums)  # {1, 2, 3, 4}
print(nums2)  # {1, 2, 3, 4}
print(type(nums))  # <class 'set'>
print(len(nums))  # 4
print("")

# No duplicate allowed
nums = {1, 2, 2, 3}
print(nums)  # {1, 2, 3}
print("")

# True is a dupe of 1, False is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
print(nums)  # {False, 1, 2, 3, 4}
print("")

# check if a value is in a set
# but you cannot refer to an element in the set with an index position or a key
print(2 in nums)  # True
print("")

# Add a new element to a set
nums.add(8)
print(nums)  # {False, 1, 2, 3, 4, 8}

# Add elements from one set to another
# you can use update with lists, tuples, and dictionaries, too.
more_nums = {5, 6, 7}
nums.update(more_nums)
print(nums)  # {False, 1, 2, 3, 4, 5, 6, 7, 8}

# Merge two sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}
my_new_set = one.union(two)
print(my_new_set)  # {1, 2, 3, 5, 6, 7}

# Keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}
one.intersection_update(two)
print(one)  # {2, 3}

# Keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4}
one.symmetric_difference_update(two)
print(one)  # {1, 4}
