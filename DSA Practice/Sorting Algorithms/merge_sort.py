# Merge Sort Question: 
"""
A program that implements Merge Sort for a list of 50 integers and sorts them in ascending order 
using the divide and conquer technique.
"""

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = j = k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

def sort_ascending(arr):
    merge_sort(arr)
    return arr

if __name__ == '__main__':
    # Generate a list of 50 integers in random order
    import random
    random.seed(42)
    nums = [random.randint(1, 100) for i in range(50)]

    # Print the unsorted list
    print("Unsorted List: ", nums)

    # Sort the list using merge sort and print the sorted list in ascending order
    sorted_nums = sort_ascending(nums)
    print("Sorted List (Ascending Order): ", sorted_nums)
