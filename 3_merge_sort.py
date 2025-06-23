# Merge sort follows the divide-and-conquer paradigm to
# divide the list into smaller sublists, sorting those sublists,
# and then merging them back together in a sorted manner.

def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    sleft = merge_sort(left)
    sright = merge_sort(right)
    return merge(sleft, sright)


def merge(left: list, right: list) -> list:
    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    if left:
        result += left
    if right:
        result += right

    return result


a = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array is:", a)
print("Sorted array is:", merge_sort(a))
