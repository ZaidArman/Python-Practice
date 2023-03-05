# Nested Loop
"""
A nested loop is a loop inside a loop.
The "inner loop" will be executed completely for each single iteration of the "outer loop"
"""
# Pattern 1
a = int(input(" Enter a number for pattern making: "))
for i in range(a):
    for j in range(i+1):
        print(j+1, end="")
    print("")
    

# # Pattern 2
a = int(input(" Enter a number for pattern making: "))
for i in range(a):
    for j in range(i+1):
        print("*", end="")
    print("")

# Pattern 3
a = int(input(" Enter a number for pattern making: "))
for i in range(a):
    for j in range(i+a):
        print(i+1, end="")
    print("")