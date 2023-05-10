# 1. Декодировать в строку байтовое значение: b'r\xc3\xa9sum\xc3\xa9'. Затем результат преобразовать в байтовый вид
# в кодировке 'Latin 1' и затем результат снова декодировать в строку (результаты всех преобразований выводить на экран).
import json
import csv
import openpyxl

s = b'r\xc3\xa9sum\xc3\xa9'
dec_str = s.decode('utf-8')
print(f'Декодирование строки "{s}" в байтовое значение: {dec_str}')
enc_str = dec_str.encode('Latin 1')
print(f'Преобразование в Latin 1: {enc_str}')
rev_str = enc_str.decode('Latin 1')
print(f'Обратное декодирование в строку: {rev_str}')


# 2. Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные. Создать файл и записать в него первые 2 строки
# закрыть файл. Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки. В итогом файле должны быть 4
# строки, каждая из которых должна начинаться с новой строки.

# a, b, c, d = str(input()), str(input()), str(input()), str(input())
# list_1 = []
# list_1.append(a)
# list_1.append(b)
# with open('for_ex_2', "w") as f:                      # 'w' - открываем на запись
#     f.writelines("%s\n" % line for line in list_1)    #генератор
#     f.close()
# list_2 = []
# list_2.append(c)
# list_2.append(d)
# with open('for_ex_2', "a") as f:                      # 'а' - открываем на дозапись
#     f.writelines("%s\n" % line for line in list_2)
#     f.close()


# 3. Создать словарь в качестве ключа которого будет 6-ти значное число (id), а в качестве значений кортеж состоящий из
# 2-х элементов имя(str), возраст(int). - Сделать около 5-6 элементов словаря.
# Записать данный словарь на диск в json-файл.

origin_dict = {111111: ('Olya', 18),
               222222: ('Nazar', 21),
               333333: ('Yan', 54),
               444444: ('Serhey', 52),
               555555: ('Ilya', 25)}
# with open('for_3_ex.json', 'w') as f:
#     json.dump(origin_dict, f)
#     f.close()

# 4. Прочитать сохранённый json-файл и записать данные на диск в csv-файл,
# первой строкой которого озаглавив каждый столбец и добавив новый столбец “телефон”.
phones = {111111: +375291111111,
          222222: +375292546987,
          333333: +375295478963,
          444444: +375336985784,
          555555: +375236251475}
# with open('for_3_ex.json', 'r') as f:
#     origin_dict = json.load(f)
# with open('file.csv', 'w', newline='') as csv_file:
#     writer = csv.writer(csv_file, delimiter=';')
#     field_names = ["id", "first_name", "age", "phone"]
#     writer.writerow(field_names)
#     for i in origin_dict:
#         list = origin_dict[i]
#         list.insert(0, i)
#         list.append(phones[int(str(i))])
#         writer.writerow(list)
#     csv_file.close()

# 5. *Прочитать сохранённый csv-файл и сохранить данные в excel-файл, кроме возраста - столбец с этими данными не нужен.


# csv_data = []
# with open('file.csv', 'r', newline='') as csv_file:
#     reader = csv.reader(csv_file, delimiter=';')
#     for row in reader:
#         csv_data.append(row)
# wb = openpyxl.Workbook()
# sheet = wb.active
# for row in csv_data:
#     sheet.append(row)
# wb.save('for_exel.xlsx')

