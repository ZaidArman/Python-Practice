my_list = [1, 2, 3, "Zaid", True] # here creating a list
print(my_list) # printing the above list

# accessing elements of a list
print(my_list[0])
print(my_list[3])

# A list can also be defined as empty:
empty_list = []
print(empty_list)

# we can check if an item is contained into a list with the in operator:
print("Zaid" in my_list) # True

# we can reference the items in a list by their index
print(my_list[0]) # 1
print(my_list[1]) # 2
print(my_list[3]) # "Zaid"

# we can also use the index() method: 
print(my_list.index(1)) # 1 is on 0 index
print(my_list.index("Zaid")) # Zaid is on 4 index

# As with strings, using a negative index will start searching from the end:
print(my_list[-2]) # True

# we can also extract a part of a list, using slices:
print(my_list[0:2]) # [1, 2]
print(my_list[2:]) # [3, "Zaid", True]

# append/adding elements to the above list using append or extend method
my_list.append("five")
my_list.extend(["Six"])

my_list += ["Seven"] # Or we can also use the += operator
print(my_list)

"""
Tip: with extend() or += don't forget the square brackets. Don't do items += "Test" or items.extend("Six") or 
Python will add 4 individual characters to the list, resulting in [1, 2, 3, "Zaid", True, 'S', 'i', 'x']

"""

# Remove an item using the remove() method:
my_list.remove("Six")
print(my_list)

# To add an item in the middle of a list, at a specific index, use the insert() method:
my_list.insert(0, "Lets-Start") # add "Lets-Start" at index 0
print(my_list)

# Sort a list using the sort() method:
my_list2 = [1, 3, 6, 0, 10, 8] # creating a new list2
my_list2.sort()
print(my_list2)

"""
Tip: sort() will only work if the list holds values that can be compared. Strings and integers for
example can't be compared, and you'll get an error like TypeError: '<' not supported between 
instances of 'int' and 'str' if you try.

"""

# The sort() methods orders uppercase letters first, then lowercased letters. To fix this, use:
my_list3 = ["synthetic", "PROGRAMMER"] # creating a new list3
my_list3.sort(key=str.lower)
print(my_list3)


# Get the number of items contained in a list using the len() global function, the same we used to get the length of a string:
print(len(my_list)) # 8