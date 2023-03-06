# Recursion in Python
"""
A function in Python can call itself. That's what recursion is. 
The common way to explain recursion is by using the factorial calculation.
"""

#Example 1: Factorial
def factorial(n):
    if n == 1: 
        return 1
    else:
        return (n * factorial(n-1))
print(factorial(3)) # 6
print(factorial(4)) # 24
print(factorial(5)) # 120

# Example 2: Binary Search
"""
The second example is a function to perform a binary search on a sorted list of integers using recursion. 
A binary search is an efficient algorithm for finding a specific value in a sorted list by repeatedly dividing the list in half and checking the middle value. 
"""
def binary_search(arr, left, right, target):
    if right >= left:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, left, mid - 1, target)
        else:
            return binary_search(arr, mid + 1, right, target)
    else:
        return -1

# arr = [2, 3, 4, 10, 40]
arr = list(map(int, input("Enter the array elements separated by space: ").split()))
print(arr.sort()) # sort the entered array into ascending
target = int(input(" Enter Target value from above array "))
result = binary_search(arr, 0, len(arr) - 1, target)
if result != -1:
    print(f"Element {target} is present at index {result}")
else:
    print("Element is not present in array")

# Exaplanation:
"""
-- The binary_search() function takes four parameters: the sorted list arr, the left and right indices to search between (left and right), and the target value we are searching for (target).
-- We calculate the mid index as the average of left and right, rounded down to the nearest integer.
-- If the value at the mid index equals the target value, we return mid.
-- If the value at the mid index is greater than the target value, we call binary_search() recursively with left and mid - 1.
-- If the value at the mid index is less than the target value, we call binary_search() recursively with mid + 1 and right.
-- If we reach a point where right is less than left, we have searched the entire list without finding the target value, so we return -1.
-- We create a sample sorted list arr and a target value 10, then call binary_search() with the appropriate parameters.
-- The output prints the index of the target value in the list, which is 3 in this case.
"""
