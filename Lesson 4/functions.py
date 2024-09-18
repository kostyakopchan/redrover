def sum_ignore_non_numbers(items):
    """
    Calculates the sum of all numbers in the list
    """
    sum = 0
    for i in items:
        if isinstance(i, (int, float)):
            sum += i

    return sum

def is_triange(side_a, side_b, side_c):
    """
    Decides if the triangle may exist
    """
    if side_a < side_b + side_c and side_b < side_a + side_c and side_c < side_a + side_b:
        return True
    else:
        return False
    
def average(*args):
    """
    Calculates the average of a list of numbers
    """
    result = 0
    for i in args:
        result += int(i)
    return result / len(args)

def common_strings(list1, list2, ignore_case = True):
    """    
    Searches for common strings in two lists depending on the value of ignore_case
    """
    result = []
    if ignore_case == True:
        for i in list1:
            if i.lower() in list2:
                result.append(i.lower())
    elif ignore_case == False:
        for i in list2:
            if i in list1:
                result.append(i.lower())
    return result