def average(*args):
    """
    Calculates the average of a list of numbers
    """
    result = 0
    for i in args:
        result += int(i)
    return result / len(args)

print(average(1, 2, 3, 4, 5, 6, 7, 8))