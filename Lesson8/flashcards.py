import json

with open("flashcard.json", "r", encoding="utf-8") as flashcards:
    data = json.load(flashcards)
while True:
    topic_choice = input("Привет! Выбери сегодняшнюю тему для изучения: city, fruits или введи 'выйти':")
    correct_answers = 0
    incorrect_answers = []
    if topic_choice.lower().strip() == "выйти":
        print("Но ты приходи еще!")
        break
    else:
        try:
            for i in data[f"{topic_choice}"]:
                print(f"Как на русском будет {i} ?")
                answer = input("Ваш ответ:")
                if answer == data[f"{topic_choice}"][i]:
                    print("Верно!")
                    correct_answers += 1
                else:
                    print(f"Неверно! Правильный перевод: {data[f"{topic_choice}"][i]}")
                    incorrect_answers.append(f"{i} - {answer}")
        except KeyError:
            continue
        print(f"Твой результат {correct_answers} из {len(data[f"{topic_choice}"])}.\nТвои неверные ответы:{incorrect_answers}")