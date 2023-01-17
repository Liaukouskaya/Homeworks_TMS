from datetime import datetime
import time

n = int(input())  # количество элементов в новом списке


def gen_func(number):
    data_original = []
    for i in range(n):
        data = (datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'))
        time.sleep(1)
        data_original.append(data)

    print(data_original)


gen_func(n)
