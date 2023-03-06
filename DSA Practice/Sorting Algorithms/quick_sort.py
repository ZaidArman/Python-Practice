# Quick Sort Question: 
"""
A program that uses the Quick Sort algorithm to sort an array of 50 integers in ascending order.
"""

# Ascending Order
import random
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quick_sort(left) + [pivot] + quick_sort(right)

# Generate a random array of 50 integers
arr = [random.randint(1, 100) for i in range(50)]

print("Original array:")
print(arr)

# Sort the array using quick sort in ascending order
sorted_arr = quick_sort(arr)

print("Sorted array (ascending order):")
print(sorted_arr)


# Descending order
def quick_sort_descending(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] > pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quick_sort_descending(left) + [pivot] + quick_sort_descending(right)

# Generate a random array of 50 integers
arr = [random.randint(1, 100) for i in range(50)]

print("Original array:")
print(arr)

# Sort the array using quick sort in descending order
sorted_arr = quick_sort_descending(arr)

print("Sorted array (descending order):")
print(sorted_arr)

