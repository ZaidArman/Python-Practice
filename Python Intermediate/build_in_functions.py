# Math Functions
# A = 30
# B = 45
# C = 36

# #Output the maximum value of A, B, C
# print(max(A, B, C))

# #Output the minimum value of A, B, C
# print(min(A, B, C))

# #Output the absolute value of the difference of A and C
# print(abs(A - C))

# #Output the absolute value of the difference of C and A
# print(abs(C - A))


# To convert the type of a variable, you can use functions such as:
arr = ['arman', 1, 'zaid'] # array variable
a = 199 # integer variable
b = 3.897 # float variable
print(str(arr)) # to convert to a string, where arr is a array 
print(int(b)) # to convert to an integer., where b is a float
print(float(a)) # to convert to a float. where a is a int 
print(round(b)) # to round to a float value = 3.897 into 4.

# Python has builtin function like "filter", but, 
# The "reduce()" function was moved to the functools module in Python 3, so you need to import it before you can use it.

from functools import reduce
def add(x, y): 
    return x+y
print(reduce(add, [1,2,3,4]))
print(filter(add, [1,2,3,4]))

# Filter():
"""
filter() takes a function and a sequence as input and returns a new sequence consisting of elements for which the function returns True
"""
# reduce()
"""
reduce() takes a function and a sequence as input and returns a single value by applying the function cumulatively to the sequence. 
"""