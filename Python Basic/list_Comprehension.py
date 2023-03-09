# List comprehension: 
""" 
List comprehension is a concise way to create a new list by iterating over an existing iterable 
(e.g., list, tuple, dictionary, set, etc.) and applying a condition to select or transform its elements.
List comprehension is often used as an alternative to for loops and map() function calls, 
because it can save time and make your code more readable and maintainable.
"""

# Creating a list of squared numbers from 1 to 10:
squares = [i**2 for i in range(1, 11)]
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Filtering a list of numbers to select only even numbers in the above squares list:
evens = [n for n in squares if n % 2 == 0]
print(evens)  # Output: [4, 16, 36, 64, 100]

# Creating a list of first letters from a list of words:
words = ["apple", "banana", "cherry", "date"]
first_letters = [word[0] for word in words]
print(first_letters)  # Output: ['a', 'b', 'c', 'd']

# Creating a list of tuples from two lists using zip function:
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']
pairs = [(x, y) for x, y in zip(list1, list2)]
print(pairs)  # Output: [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

# Creating a list of common elements from two lists:
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = [x for x in list1 if x in list2]
print(common)  # Output: [3, 4]


