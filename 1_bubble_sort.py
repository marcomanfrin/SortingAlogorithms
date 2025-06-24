# Bubble Sort repeatedly compares adjacent elements and
# swaps them if they are in the wrong order.
# The process is repeated until the entire list is sorted.

def bubble_sort(arr: list) -> list:
    # Outer loop to iterate through the list n times
    for i in range(len(arr)):
        has_swap_occurred = False
        # Inner loop to compare adjacent elements
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Mark that a swap has occurred
                has_swap_occurred = True
        # If no swaps occurred, the list is already sorted
        if not has_swap_occurred:
            break
    return arr


a = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array is:", a)
print("Bubble Sorted array is:", bubble_sort(a))
