# # Написать декоратор к 2-м любым функциям, который бы считал и выводил время их выполнения.
# # Подсказка: from datetime import datetime time=datetime.now()

from datetime import datetime
import random




def decor(func):
    def wrapper():
        start = datetime.now()
        func()
        end = datetime.now()
        print(f'Время выполнения {str(func).split()[1]} = {end - start}')
    return wrapper


@decor
def time_from_cycle():
    temp = []
    for x in range(1000000):
        if x % 2 == 0:
            temp.append(x)


@decor
def time_from_creative():
    temp_two = []
    a = [random.randint(0,10) for i in range(1000000)]
    temp_two.append(a)



time_from_cycle()
time_from_creative()
