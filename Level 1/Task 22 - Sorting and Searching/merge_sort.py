def merge_sort_by_length(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort_by_length(lst[:mid])
    right = merge_sort_by_length(lst[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if len(left[0]) >= len(right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left or right)
    return result

list1 = ["apple", "banana", "kiwi", "grapefruit", "fig", "date", "mango", "papaya", "plum", "blueberry"]
sorted1 = merge_sort_by_length(list1.copy())
print("Sorted List 1 by string length:")
print(sorted1)

list2 = ["cat", "elephant", "giraffe", "dog", "hippopotamus", "lion", "zebra", "bear", "monkey", "rabbit"]
sorted2 = merge_sort_by_length(list2.copy())
print("\nSorted List 2 by string length:")
print(sorted2)

list3 = ["car", "spaceship", "bike", "skateboard", "rollerblades", "scooter", "plane", "submarine", "train", "bus"]
sorted3 = merge_sort_by_length(list3.copy())
print("\nSorted List 3 by string length:")
print(sorted3)
