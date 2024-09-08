# Solution 1
# numbers = []
# for i in range(100 + 1):
#     if i % 2 == 0 and i % 3 == 0:
#         numbers.append(i)
# print(numbers)

# Solution 2
numbers = [i for i in range(100 + 1) if i % 2 == 0 and i % 3 == 0]
print(numbers)

