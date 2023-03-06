# Decorator
"""
Decorators are a way to change, enhance or alter in any way how a function works.
Decorators are defined with the @ symbol followed by the decorator name, just before the function definition.

A decorator is a function that takes a function as a parameter, wraps the function in an inner function that
performs the job it has to do, and returns that inner function.

OR 

a decorator function is a function that takes another function and extends or modifies its behavior without modifying its source code. 
It is a design pattern that allows us to add functionality to an existing function by wrapping it with another function. 
Decorators use the concept of higher-order functions, which means that they take one or more functions as arguments and/or return a function as its output.
"""

# Why We Need Decorator Function:
"""
The need for a decorator function arises when we want to add some additional functionality to an existing function without modifying its source code. 
For example: we may want to add logging or timing functionality to a function, or we may want to add authentication or caching functionality to a function. 
Using a decorator, we can easily add this functionality without having to modify the original function, which makes our code more modular and easier to maintain. 
Decorators also help to keep the code DRY (Don't Repeat Yourself) by allowing us to reuse the same code for multiple functions.
"""

# Example 1:
def logtime(func):  
    def wrapper():
        val = func() 
        return val 
    return wrapper

@logtime
def hello(): 
    print('hello!')

print(hello(), "\n\n")

# Explain:
"""
This hello function has the logtime decorator assigned.
Whenever we call hello() , the decorator is going to be called.
 """


# Example 2: A decorator that logs the execution time of a function

import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end-start} seconds")
        return result
    return wrapper

@timeit
def add(x, y):
    return x + y

print(add(2, 3), "\n\n")

# Explanation: 
"""
the "timeit" decorator takes a function and returns a new function that prints the time taken by the original function to execute. 
The "wrapper" function uses the time module to measure the time taken by the original function, and then prints the time and returns the result.
"""


# Example 3: A decorator that adds two numbers and then multiplies the result by a given number
def multiply_by(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return (result + n) * n
        return wrapper
    return decorator

@multiply_by(2)
def add(x, y):
    return x + y

print(add(2, 3))

# Explanation:
"""
the 'multiply_by' decorator takes a number 'n' and returns another decorator that takes a function and returns a new function that adds the result of the original function to 'n',
multiplies the result by 'n', and then returns the result. The wrapper function does the actual computation. 
In the end, we decorate the 'add' function with 'multiply_by(2)' to get a new function that adds two numbers and then multiplies the result by '2'.
"""



