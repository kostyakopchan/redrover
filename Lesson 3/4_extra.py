dialog = """Doc: Запомни! Согласно моей теории, ты помешал знакомству
своих родителей.
Если они не встретятся, то не влюбятся, не поженятся, и у них не будет детей.
Поэтому твой старший брат исчезает с фотографии. Затем очередь твоей
сестры,
и если ты все не исправишь, ты будешь следующим.
Marty: Тяжелый случай.
Doc: Вес тут совершенно ни при чем. """

dialog = dialog.replace('\n', '').replace('Doc:', '').replace('Marty:', '').replace('.', '').replace(',', '').replace(' ', '').replace('!', '').replace('?', '').lower()

words_amount = {}

for i in dialog:
    words_amount[i] = words_amount.get(i, 0) + 1

print(words_amount)