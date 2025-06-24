# Counting sort is a non-comparison-based sorting algorithm that
# counts the number of objects that have each distinct key value
# and uses those counts to compute the positions
# of each key value in the output sequence

def count_sort(arr: list) -> list:
    M = max(arr)
    count = [0] * (M + 1)
    for num in arr:
        count[num] += 1
    for i in range(1, M + 1):
        count[i] += count[i - 1]
    output = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    return output


a = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array is:", a)
print("Count Sorted array is:", count_sort(a))
