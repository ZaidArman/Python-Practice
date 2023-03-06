# Composition are often used with lambda
# Example Composition
def square(x): 
    return x*x
def twice(a): 
    return lambda x: a(a(x))

print(twice)
quad = twice(square) 
print(quad)
print(quad(5))

#Explanation:
"""
we have a function "twice" that takes "a" function a as an argument and returns a new function that applies "a" twice to its argument. 
The function square is passed as an argument to "twice" and the resulting function is assigned to the variable "quad".
The function "quad" is a composition of the square function applied twice. When "quad(5)" is called, 
it first applies the square function to 5, resulting in 25, and then applies square again to 25, 
resulting in 625, which is returned as the output.
"""