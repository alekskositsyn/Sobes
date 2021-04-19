keys = [1, 2, 3, 4]
values = ['a', 'b', 'c', 'd', 'e']


def new_d(keys, values):
    if len(keys) > len(values):
        new_dict = {}
        n = 0
        for k in keys:
            try:
                new_dict[k] = values[n]
                n += 1
            except IndexError:
                new_dict[k] = None
        return new_dict
    else:
        new_dict = (dict(zip(keys, values)))
        return new_dict


print(new_d(keys, values))
