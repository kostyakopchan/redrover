def sum_ignore_non_numbers(items):
    """
    Calculates the sum of all numbers in the list
    """
    sum = 0
    for i in items:
        if isinstance(i, (int, float)):
            sum += i

    return sum

print(sum_ignore_non_numbers([1, 2, 'Hey', None, 4.3]))