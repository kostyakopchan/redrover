message = "2__234йшDGмёшSDFжкъrrrщзнSDF78юкйфуSDFшёью$#2Sшжйи3%узфsdf34нкфыvvя"

cipher = {
"а": "щ", "б": "д", "в": "ю", "г": "ф", "д": "з", "е": "м", "ё": "р",
"ж": "т", "з": "п", "и": "я", "й": "с", "к": "н", "л": "э", "м": "к",
"н": "л", "о": "ё", "п": "ж", "р": "ц", "с": "б", "т": "у", "у": "в",
"ф": "о", "х": "и", "ц": "х", "ч": "г", "ш": "е", "щ": "й", "ъ": "ы",
"ы": "ч", "ь": "ш", "э": "ъ", "ю": "а", "я": "ь"
}

deciphered_message = ""
for i in message:
    if i in cipher.keys():
        deciphered_message += cipher.get(i)

print(deciphered_message)

ciphered_response = ""
response = input ('Введите ваш ответ:').replace(' ', '').replace('!', '').replace('?', '').replace(',', '').lower()

for i in response:
    if i in cipher.values():
        ciphered_response += cipher.get(i)

print(ciphered_response)

# Result from GPT
# # Зашифрованное сообщение
# message = "2__234йшDGмёшSDFжкъrrrщзнSDF78юкйфуSDFшёью$#2Sшжйи3%узфsdf34нкфыvvя"

# # Ключ к шифру
# cipher = {
#     "а": "щ", "б": "д", "в": "ю", "г": "ф", "д": "з", "е": "м", "ё": "р",
#     "ж": "т", "з": "п", "и": "я", "й": "с", "к": "н", "л": "э", "м": "к",
#     "н": "л", "о": "ё", "п": "ж", "р": "ц", "с": "б", "т": "у", "у": "в",
#     "ф": "о", "х": "и", "ц": "х", "ч": "г", "ш": "е", "щ": "й", "ъ": "ы",
#     "ы": "ч", "ь": "ш", "э": "ъ", "ю": "а", "я": "ь"
# }

# # Расшифровка сообщения
# decoded_message = ''.join(cipher.get(char, '') for char in message)
# print(decoded_message)

# # Дополнительно: ввод строки и шифрование
# user_input = input("Введите сообщение для шифрования: ")
# encoded_message = ''.join(cipher.get(char, '') for char in user_input)
# print(encoded_message)

#Solution from teacher
# secret_message = "2__234йшDGмёшSDFжкъrrrщзнSDF78юкйфуSDFшёью$#2Sшжйи3%узфsdf34нкфыvvя"

# cipher = {
#     "а": "щ", "б": "д", "в": "ю", "г": "ф", "д": "з", "е": "м", "ё": "р",
#     "ж": "т", "з": "п", "и": "я", "й": "с", "к": "н", "л": "э", "м": "к",
#     "н": "л", "о": "ё", "п": "ж", "р": "ц", "с": "б", "т": "у", "у": "в",
#     "ф": "о", "х": "и", "ц": "х", "ч": "г", "ш": "е", "щ": "й", "ъ": "ы",
#     "ы": "ч", "ь": "ш", "э": "ъ", "ю": "а", "я": "ь"
# }
# decrypted_message = ""

# for c in secret_message:
#     if c in cipher:
#         decrypted_message += cipher[c]

# print(decrypted_message)