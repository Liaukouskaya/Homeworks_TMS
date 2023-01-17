original_list = [1, 3, 5, 5, 7, 3, 1, 4, 1, 1]
new_list = []
new_dict = {}


def counter():
    for i in original_list:
        list_1 = []
        count = 0
        for j in range(len(original_list)):
            if i == original_list[j]:
                count += 1
        list_1.append(i)
        list_1.append(count)
        list_2 = tuple(list_1)
        new_list.append(list_2)
    global new_dict
    new_dict = dict(new_list)


counter()
for key in new_dict:
    print(f'{key}: {new_dict[key]}')
