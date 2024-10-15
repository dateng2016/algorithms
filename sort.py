def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res
# The runtime is O(nlog(n)) the space is O(n)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = arr[len(arr) // 2]
    left = [i for i in arr if i < mid]
    middle = [i for i in arr if i == mid]
    right = [i for i in arr if i > mid]
    return quick_sort(left) + middle + quick_sort(right)
# The runtime is on average O(nlog(n)), in worst case it is O(n**2)
# The space is O(n)


def in_palce_quick_sort(low, high, arr):
    if low >= high:
        return
    pivot_idx = partition(low, high, arr)
    in_palce_quick_sort(low, pivot_idx - 1, arr)
    in_palce_quick_sort(pivot_idx + 1, high, arr)


def partition(low, high, arr):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
# In place quick_sort, with space complexity of O(log(N))
# The time complexity remains the same as before

def bubble_sort(arr):
    l = len(arr)
    for i in range(l):
        swapped = False
        for j in range(l - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
# space complexity is O(1) since it is in place and there is no call stack
# Run time: Best O(n), average and worst: O(n**2)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# It has the same performance in terms of time and space as bubble.
