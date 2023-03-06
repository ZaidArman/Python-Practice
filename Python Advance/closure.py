# # Closure are often used with lambda, but here i will explain seperately
# Exaample Closure
def counter(start=0, step=1):
    x = [start]
    def INC(): # increment function
        x[0] += step
        return x[0]
    return INC
c1 = counter()
c2 = counter(100, -10)
print(c1())
print(c2())

# Explanation:
"""
defines a closure function called counter that takes two optional parameters start and step.
start determines the starting value of the counter, and step determines the amount by which the counter will be incremented each time the function is called.
The function returns another function called INC which increments the counter and returns the current value.
The code creates two instances of the counter function c1 and c2 by calling the counter() function twice with different arguments. c1 starts at 0 and increments by 1 each time it is called, while c2 starts at 100 and decrements by 10 each time it is called.
"""