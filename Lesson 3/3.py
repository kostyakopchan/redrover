messages = []

while True:
    user_input = input('Введите текст:')
    if user_input.lower() == 'пока':
        messages.append(user_input)
        print('Ну ладно, пока!')
        break
    messages.append(user_input)
    if len(messages) > 4:
        messages.pop(0)

print(messages)