while True:
    user_input = input("Введите, что необходимо сделать:")
    if user_input.lower() == "прочитать":
        with open("journal.txt", "r") as file:
            print(file.read())
    elif user_input.lower() == "записать":
        with open("journal.txt", "a") as file:
            line_to_add = input("Введите, что нужно записать:")
            file.write("\n" + line_to_add)
    elif user_input.lower() == "выйти":
        print("Еще увидимся!")
        break
    else:
        pass

