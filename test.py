numbers: list[int] = [455, 322, 432, 55433, 45, 435, 53]

# Sorted is a function that returns a new list
sorted_numbers: list[int] = sorted(numbers)
print(f'{sorted_numbers=}')
print(f'{numbers=}')

# Sort is a method on the class list that works in-place
numbers.sort()
print(f'{numbers=}')