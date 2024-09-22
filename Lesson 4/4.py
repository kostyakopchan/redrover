fruits_1 = ['banana', 'APPLE', 'watermelon', 'cherry']
fruits_2 = ['Mango', 'apple', 'orange', 'cherry']

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

print(common_strings(fruits_1, fruits_2))

#Teacher's solution
# def common_strings(list1, list2, ignore_case=True):
#     """
#     Возвращает список из строк, которые находятся в обоих списках, приводя строки к нижнему регистру.

#     :param list1: Первый список строк.
#     :param list2: Второй список строк.
#     :param ignore_case: Если True, то регистр игнорируется. Иначе учитывается.
#     :return: Список из строк (приведенные к нижнему регистру), которые находятся в обоих списках.
#     """

#     if ignore_case:
#         list1 = [i.lower() for i in list1]
#         list2 = [i.lower() for i in list2]
#     return [i.lower() for i in list1 if i in list2]