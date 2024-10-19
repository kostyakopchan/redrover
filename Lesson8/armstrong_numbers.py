armstrong_numbers = []
for i in range(100, 1000):
    subresult = []
    for n in str(i):
        subresult.append(int(n) ** 3)
        if sum(subresult) == i:
            armstrong_numbers.append(i)
print(armstrong_numbers)
