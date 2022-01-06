def general_search(in_list, condition):
    """
    Filters the elements
    :param in_list:
    :param condition:
    :return: the element that respects the condition
    """
    out_list = []
    for element in in_list:
        if condition(element):
            out_list.append(element)
    return out_list

def general_sort(in_list, condition):
    """
    Sorting the values
    :param in_list:
    :param condition:
    :return: the sorted list
    """

    swapped = True
    iterations = 0
    while swapped:
        swapped = False
        for i in range(len(in_list) - iterations - 1):
            if not condition(in_list[i], in_list[i + 1]):
                in_list[i], in_list[i + 1] = in_list[i + 1], in_list[i]
                swapped = True
        iterations += 1
    return in_list


from itertools import permutations


def generate_groups(original_list: list, k: int) -> list[list]:
    """
    Generates all possible combinations of the original list split in groups of len k


    """
    for perm in permutations(original_list):
        l = []
        for i in range(0, len(perm), k):
            l.append(perm[i:i + k])
        yield l


def groups(original_list: list, k: int, test, arg = None) -> list[list] | None:
    """
    Goes trough each group, tests it and returns the first valid group

    """

    if arg:
        f = lambda i: test(i, arg)
    else:
        f = lambda i: test(i)

    for group in generate_groups(original_list, k):
        if f(group):
            return group
    return None