def get_final_answer(answer):
    return answer

"""
Explanation:
- Function definition begins with “def.”. 
- "get_final_answer" is Function name and  "answer" is its arguments.
- The keyword "return" indicates the value to be sent back to the caller.
"""

# function call:
def myfun(x, y): 
    return x * y

print(myfun(3, 4))

# Default Values for Arguments 
"""
We can provide default values for a functions arguments
These arguments are optional when the function is called 
"""
def myfun(b, c=3, d="hello"): 
    return b + c
print(myfun(5,3, "Hello Arman"))
print(myfun(5,3))
print(myfun(10))

# Note:
""" 
There is no function overloading in Python.
"""
