class IndexCount:
    def __init__(self, index):
        self.count = 1
        self.index = index

    def increase_count(self):
        self.count += 1

def first_non_recurring_char(string):
    if not isinstance(string, str):
        raise TypeError("string parameter must be of type string")
    chars = {}
    for char in enumerate(string):
        if char[1] in chars:
            chars[char[1]].increase_count()
        else:
            chars[char[1]] = IndexCount(char[0])
    result = None
    for key, value in chars.items():
        if value.count == 1:
            if result is None:
                result = key
            elif chars[key].index < chars[result].index:
                result = key

    return result
