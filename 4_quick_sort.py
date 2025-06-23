# Quick sort follows the divide-and-conquer paradigm:
# it selects a pivot element from the array and partitions the other elements
# into two sub-arrays, according to whether they are less than
# or greater than the pivot.
# The sub-arrays are then recursively sorted.

def quick_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)


a = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array is:", a)
print("Sorted array is:", quick_sort(a))
