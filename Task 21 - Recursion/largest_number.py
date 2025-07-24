def largest_number(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        max_rest = largest_number(lst[1:])
        if lst[0] > max_rest:
            return lst[0]
        else:
            return max_rest
print(largest_number([3, 4, 5, 3]))          
print(largest_number([3, 2, 6, 9, 2, 4, 7])) 
