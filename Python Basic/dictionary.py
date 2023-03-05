# creating a dictionary (Key-pair values)
my_dict = {"name": "Arman", "age": 23, "country": "Pakistan", "YT Channel": "Synthetic Programmer"} 
print(my_dict) # printing the dictionary

# accessing values of a dictionary by using key
print(my_dict["name"])
print(my_dict["country"])

# adding a key-value pair to a dictionary
my_dict["occupation"] = "programmer"
print(my_dict)

# The pop() method retrieves the value of a key, and subsequently deletes the item from the dictionary:
print(my_dict.pop('name'))
print(my_dict)

# The popitem() method retrieves and removes the last key/value pair inserted into the dictionary:
print(my_dict.popitem())
print(my_dict)

# Get a list with the keys in a dictionary using the keys() method, passing its result to the list() constructor:
print("Keys in the list are: ", list(my_dict.keys()) )

# Get the values using the values() method, and the key/value pairs tuples using the items() method:
print(list(my_dict.values()))
print(list(my_dict.items()))


# To copy a dictionary, use the copy() method: d
my_dict = my_dict.copy()
print(my_dict)



