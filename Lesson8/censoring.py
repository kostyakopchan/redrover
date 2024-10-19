def censor_print(string):
    abandoned_words = ["запрещенное", "слово"]
    for word in abandoned_words:
        string = string.replace(word, "***")
    return string