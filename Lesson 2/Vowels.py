message = input('Введите текст:')
count = 0

for letter in message:
    if letter.lower() in 'ауоиэыяюеё':
        count += 1

print (count)