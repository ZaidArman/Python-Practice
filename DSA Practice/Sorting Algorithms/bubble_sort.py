# Bubble Sort Question: 
"""
A program that uses the Bubble Sort algorithm to sort an array of 50 integers in ascending order, 
and a separate function to sort them in descending order.
"""

import random
def bubble_sort_ascending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Create an array of 50 random integers
arr = [random.randint(1, 100) for _ in range(50)]
print("Original Array:", arr)

# Sort the array in ascending order using Bubble Sort
bubble_sort_ascending(arr)
print("Array in Ascending Order:", arr)

# Sort the array in descending order using the sorting function
bubble_sort_descending(arr)
print("Array in Descending Order:", arr)
