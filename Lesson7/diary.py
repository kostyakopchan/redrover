while True:
    user_input = input("Введите, что необходимо сделать:")
    if user_input.lower() == "прочитать":
        file = open("journal.txt", "r")
        print(file.read())
        file.close()
    elif user_input.lower() == "записать":
        file = open("journal.txt", "a")
        line_to_add = input("Введите, что нужно записать:")
        file.write("\n" + line_to_add)
        file.close()
    elif user_input.lower() == "выйти":
        print("Еще увидимся!")
        break
    else:
        pass

