numbers = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

index = linear_search(numbers, 9)
print("Linear Search: 9 found at index", index)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

sorted_numbers = insertion_sort(numbers.copy())
print("Sorted list:", sorted_numbers)

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1