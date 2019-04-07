from collections import defaultdict

def subsets_that_add_to_n(int_list, target):
    if not isinstance(int_list, list):
        raise TypeError("int_list parameter must be of type list")
    if any([isinstance(integer, int) is False for integer in int_list]):
        raise TypeError("all items in int_list parameter must be of type int")
    if not isinstance(target, int):
        raise TypeError("integer parameter must be of type int")

    if target == 0:
        return [[]]
    subsets = []
    for index, integer in enumerate(int_list):
        if target - integer > 0:
            subs = subsets_that_add_to_n(int_list[index + 1:], target - integer)
            for sub in subs:
                integer_list = [integer]
                subsets.append([*integer_list, *sub])
        elif target - integer == 0:
            subsets.append([integer])

    return subsets

def subsets_that_add_to_n_v2(integer_list, target, memo=defaultdict(list)):
    if not isinstance(integer_list, list):
        raise TypeError("integer_list parameter must be of type list")
    if any([isinstance(integer, int) is False for integer in integer_list]):
        raise TypeError("all items in integer_list parameter must be of type int")
    if any([integer <= 0 for integer in integer_list]):
        raise TypeError("all integers must be greater than zero")
    if not isinstance(target, int):
        raise TypeError("integer parameter must be of type int")

    if target == 0:
        return [[]]
    subsets = []
    for index, integer in enumerate(integer_list):
        new_target = target - integer
        if new_target == 0:
            subsets.append([integer])
        elif new_target > 0:
            subs = subsets_that_add_to_n_v2(integer_list[index + 1:], new_target, memo)
            for sub in subs:
                result = [integer, *sub]
                memo[(str(integer_list), target)].append(result)
                subsets.append(result)
    print(integer_list, target,memo)
    print(subsets)
    return subsets


subsets_that_add_to_n_v2([2, 4, 6, 10], 16)
