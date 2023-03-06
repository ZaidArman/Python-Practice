# Insertion Sort Question: 
"""
A program in Python that uses the Insertion Sort algorithm for an array of size 20 
and sorts the elements in descending order.
"""

def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == '__main__':
    # Initialize array of size 20
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20, 65, 14, 12, 99, 88, 73, 19, 23, 72, 49, 38]
    
    # Sort array using insertion sort in descending order
    insertion_sort_desc(arr)
    
    # Print sorted array
    print("Sorted array in descending order: ", arr)
