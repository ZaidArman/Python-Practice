# Selection Sort Question: 
"""
A program in Python that uses the Insertion Sort algorithm for an array of size 20 
and sorts the elements in descending order.
"""

import random
import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# generate random array of size 10000
arr = [random.randint(0, 1000) for i in range(10000)]
# arr = [54, 26, 93, 17, 77, 31, 44, 55, 20, 65, 14, 12, 99, 88, 73, 19, 23, 72, 49, 38]

# calculate execution time
start_time = time.time()
sorted_arr = selection_sort(arr)
end_time = time.time()

# print sorted array and execution time
print("Sorted array:", sorted_arr)
print("Execution time:", end_time - start_time, "seconds")

