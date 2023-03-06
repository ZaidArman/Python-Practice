# Data Types

a = -5          # Integer variable
print(a)
print(type(a)) # Print the type of a

b = 4.0         # Float variable
print(b)
print(type(b)) # Print the type of b

s = "1234abc"   # String variable
print(s)
print(type(s)) # Print the type of s

arr = [1, "ab", 3, "name"]    # Array variable
print(arr)
print(type(arr)) # Print the type of array


"""
Sometimes - we have to accept multiple inputs in a single line.
The way to accept multiple integers in a single line is to use the split and map function.

split function: breaks the input based on the separator - by default, it splits inputs separated by spaces in a single line into different inputs which you can assign to different variables
map function: converts each input into the defined datatype
"""

A, B, C = map(int, input().split())
print (A, B, C)
