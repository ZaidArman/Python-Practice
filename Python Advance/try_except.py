# Exceptional Handling:
"""
Python gives us exception handling. Exception handling is important to have a way to handle errors.

-- If you wrap lines of code into a 'try:' block. like:
try:
 # some lines of code
 
-- if an error occurs, Python will alert you and you can determine which kind of error occurred using a 'except' blocks. like:
try:
    # some lines of code
except <ERROR1>:
    # handler <ERROR1>
except <ERROR2>:
    # handler <ERROR2>

-- To catch all exceptions you can use except without any error type:
try:
    # some lines of code
except <ERROR1>:
    # handler <ERROR1>
except:
    # catch all other exceptions

-- The 'else' block is ran if no exceptions were found:
try:
    # some lines of code
except <ERROR1>:
    # handler <ERROR1>
except <ERROR2>:
    # handler <ERROR2>
else:
    # no exceptions were raised, the code ran succes

-- A 'finally' block lets you perform some operation in any case, regardless if an error occurred or not 
try:
    # some lines of code
except <ERROR1>:
    # handler <ERROR1>
except <ERROR2>:
    # handler <ERROR2>
else:
    # no exceptions were raised, the code ran succes
finally:
    # do something in any case
"""

# Example 1: Division by zero
"""
In this example, we will attempt to divide two numbers, but if the second number is zero, 
we will catch the ZeroDivisionError exception and handle it.
"""
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print(" Error: Cannot divide by zero.")
else:
    print(" The result of the division is: ", result)
finally:
    print(" We are using Exceptional Handling Concept: Your error is: ", ZeroDivisionError)

# Explanation:
"""
-- We first prompt the user to enter two numbers using the input() function.
-- We then attempt to divide the first number by the second number and assign the result to a variable called result.
-- If the second number is zero, a ZeroDivisionError exception is raised, and the code inside the except block is executed. In this case, we print an error message.
-- If there is no exception, the code inside the else block is executed, which simply prints the result of the division.
-- Finally, the code inside the finally block is executed, which prints a thank you message.
"""

# Example 2: Reading a file
"""
In this example, we will attempt to read the contents of a file, but if the file does not exist, 
we will catch the FileNotFoundError exception and handle it.
"""
try:
    with open("Arman.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print(" Error: File not found.")
else:
    print(" The contents of the file are:\n", data)
finally:
    print(" We are using Exceptional Handling Concept: Your error is: ", FileNotFoundError)

# Explanation:
"""
-- We open a file called "Arman.txt" in read mode using the open() function and the with statement, which ensures that the file is properly closed after we are done reading it.
-- We attempt to read the contents of the file using the read() method and assign the data to a variable called data.
-- If the file does not exist, a FileNotFoundError exception is raised, and the code inside the except block is executed. In this case, we print an error message.
-- If there is no exception, the code inside the else block is executed, which simply prints the contents of the file.
-- Finally, the code inside the finally block is executed, which prints a thank you message.
"""
