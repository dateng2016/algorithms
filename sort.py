def merge_sort(arr):
    # The runtime is O(nlog(n)) the space is O(n) mainly need to
    # account for list storage while doing recursive
    if len(arr) <= 1:
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


def in_place_quick_sort(low, high, arr):
    if low >= high:
        return
    pivot_idx = partition(low, high, arr)
    in_place_quick_sort(low, pivot_idx - 1, arr)
    in_place_quick_sort(pivot_idx + 1, high, arr)


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
    """It ensures that the right part of the list is always sortes"""
    l = len(arr)
    for i in range(l):
        swapped = False
        for j in range(l - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return


# space complexity is O(1) since it is in place and there is no call stack
# Run time: Best O(n), average and worst: O(n**2)


def insertion_sort(arr):
    """The left side of the array is always considered sorted
    starting at point i - 1, we move all the elements that are
    greater than key to the right and lastly insert the key
    to the correct position"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            # Move the bigger element one step to the right
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# It has the same performance in terms of time and space as bubble.


# HEAP SORT
def heapify(arr, n, parent_index):
    # * n -> length of the array
    # * parent_index -> the index of the "parent node" that we want to heapify
    largest_index = parent_index
    # * Since it is 0-indexed, left child index = 2 * parent_index + 1
    left_child_index = 2 * parent_index + 1
    # * Similarly for right child except that it is + 2
    right_child_index = 2 * parent_index + 2

    # * Determines which index has the largest value
    if left_child_index < n and arr[left_child_index] > arr[largest_index]:
        largest_index = left_child_index
    if right_child_index < n and arr[right_child_index] > arr[largest_index]:
        largest_index = right_child_index

    # *Determines if any swaps are needed
    if largest_index != parent_index:
        arr[largest_index], arr[parent_index] = arr[parent_index], arr[largest_index]
        # * Recursively heapify the child node that has been swapped
        # * (its index is now largest_index)
        heapify(arr, n, largest_index)


def heap_sort(arr):
    n = len(arr)
    # *Heapify the entire array except the leaf nodes
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(len(arr) - 1, 0, -1):
        # *Here we do POP AND REHEAPIFY
        # * POP
        arr[0], arr[i] = arr[i], arr[0]
        # * REHEAPIFY
        heapify(arr, i, 0)


# arr = [9, 4, 3, 8, 10, 2, 5]
# print(arr)
# heap_sort(arr)
# print(arr)
