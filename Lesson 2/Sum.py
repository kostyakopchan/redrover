result = 0

while True:
    number = int(input('Введите число:'))
    if number < 0:
        break
    result = result + number
    
print(result)