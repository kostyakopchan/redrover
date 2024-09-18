def text(entered_string):
    result = ''
    
    for index, char in enumerate(entered_string):
        if char.isalpha():
            if index % 2 == 0:
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char
    
    return result

entered_string = input('Введите текст: ')
print(text(entered_string))