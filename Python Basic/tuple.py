my_tuple = (1, 2, 3, "Synthetic", True) # creating a tuple
print(my_tuple) # printing the tuple

# accessing elements of a tuple
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])
print(my_tuple[3])
print(my_tuple[4])

# As with strings and lists, using a negative index will start searching from the end:
print(my_tuple[-2]) # four

# we can count the items in a tuple with the len() function:
print(len(my_tuple)) # 5

# we can check if an item is contained into a tuple with the in operator:
print("Synthetic" in my_tuple) # True

# we can also extract a part of a tuple, using slices: 
print(my_tuple[0:2]) # ('1', '2')
print(my_tuple[1:]) # (2, 3, 'Synthetic', True)

# we can create a sorted version of a tuple using the sorted() function:
my_tuple2 = (1, 3, 6, 0, 10, 8) # creating a new tuple
print(sorted(my_tuple2))

# we can create a new tuple from existing tuples using the + operator:
newTuple = my_tuple + ("Programmer", "with", "Zaid")
print(newTuple)


