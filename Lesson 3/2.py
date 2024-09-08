items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, None]
numbers = [i for i in items if type(i) is int or type(i) is float]

print(sum(numbers))