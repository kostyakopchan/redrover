# Solution 1
numbers = [15, 3, 8, 42, 3, 23, 8, 7, 42, 1, 9, 23, 15, 5, 9, 4, 6, 1]
numbers_without_duplicates = []

for i in numbers:
    if i not in numbers_without_duplicates:
        numbers_without_duplicates.append(i)
        
numbers_without_duplicates.sort()
print(numbers_without_duplicates)

# Solution 2
# numbers = [15, 3, 8, 42, 3, 23, 8, 7, 42, 1, 9, 23, 15, 5, 9, 4, 6, 1]
# numbers_without_duplicates = list(set(numbers))

# print(numbers_without_duplicates)

