# Insertion Sort builds a sorted sublist one element at a time.
# It iterates through the input list, taking one element at a time
# and inserting it into its correct position
# within the already sorted portion of the list.

def insertion_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


a = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array is:", a)
print("Sorted array is:", insertion_sort(a))
