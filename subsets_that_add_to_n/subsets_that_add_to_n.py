

def subsets_that_add_to_n(int_list, target):
    if not isinstance(int_list, list):
        raise TypeError("int_list parameter must be of type list")
    if any([isinstance(integer, int) is False for integer in int_list]):
        raise TypeError("all items in int_list parameter must be of type int")
    if not isinstance(target, int):
        raise TypeError("integer parameter must be of type int")

    if target == 0:
        return []
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
