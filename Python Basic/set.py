my_set = {1, 2, 3, 4, 5} # creating a set
print(my_set) # printing the set

# adding an element to a set
my_set.add(6)
print(my_set)

# removing an element from a set
my_set.remove(3)
print(my_set)

# we can intersect two sets:
set1 = {"Synthetic", "Programmer"}
set2 = {"Synthetic"}
intersect = set1 & set2 #{'Synthetic'}

# we can create a union of two sets:
set1 = {"Synthetic", "Programmer"}
set2 = {"with", "Zaid"}
union = set1 | set2 #{'Synthetic', 'Programmer', 'With', "Zaid"}

# we can count the items in a set with the global function len() :
names = {"Synthetic", "Programmer"}
len(names) # 2

# we can get a list from the items in a set by passing the set to the list() constructor:
names = {"Synthetic", "Programmer"}
list(names) #['Synthetic', 'Programmer']
print("Synthetic" in names) # False