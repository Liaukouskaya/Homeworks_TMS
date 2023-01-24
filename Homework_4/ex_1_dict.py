old_dict = {'mitochondria': 'energy',
            'plasma membrane': 'protection',
            'nucleus': 'protection of genetic material',
            'lysosomes': 'hydrolysis'}
new_dict = {}
keys, values = [], []
final_list = []


def kwargs():
    for key in old_dict.keys():
        keys.append(key)
    for value in old_dict.values():
        values.append(value)
    for i in range(len(keys)):
        list_1 = [values[i], keys[i]]
        new_tuple = tuple(list_1)
        final_list.append(new_tuple)
    global new_dict
    new_dict = dict(final_list)
    print(f'Старый словарь: {old_dict}')
    print(f'Новый словарь: {new_dict}')


kwargs()
