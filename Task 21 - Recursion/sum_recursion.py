def adding_up_to(numbers, index):
    if index == 0:
        return numbers[0]
    return numbers[index] + adding_up_to(numbers, index - 1)

# Example usage
print(adding_up_to([9, 4, 5, 7, 12, 16], 4))
print(adding_up_to([4, 7, 2, 5], 1))
