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

# Solution 2
# messages = []

# while True:
#     message = input("Введите ваше сообщение: ")
#     messages.append(message)
#     if len(messages) > 5:
#         del messages[0]
#     if message == "Пока":
#         print("Ну ладно, пока!")
#         break


# print(messages)