# 1. Создать родительский класс auto, у которого есть атрибуты: brand, age, color, mark и weight. А так же методы: move,
# birthday и stop. Методы move и stop выводят сообщение на экран «move» и «stop», a birthday
# увеличивает атрибут аде на 1. Атрибуты brand, age и mark являются обязательными при объявлении объекта.

import time


class Auto:
    def __init__(self, brand, age, mark, weight=15, color='Yellow'):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.weight = weight
        self.color = color

    def move(self):
        print('move')

    def birthday(self):
        self.age += 1
        print(self.age)

    def stop(self):
        print('stop')


first_car = Auto('audi', 3, 'a47')
first_car.stop()
first_car.move()
first_car.birthday()


# 2. Создать 2 класса truck и саг, которые являются наследниками класса auto. Класс truck имеет дополнительный
# обязательный атрибут max_load. Переопределенный метод move, перед появлением надписи «move» выводит надпись
# «attention», его реализацию сделать при помощи оператора super. А так же дополнительный метод load.
# При его вызове происходит пауза 1 сек., затем выдается сообщение <load» и снова пауза 1 сек.
# Класс саг имеет дополнительный обязательный атрибут max_speed и при вызове метода move, после появления надписи
# «move» должна появиться надпись «max speed is <max_speed>». Создать по 2 объекта для каждого из классов truck и саг,
#  проверить все их методы и атрибуты.

class Truck(Auto):
    def __init__(self, max_load):
        self.max_load = max_load

    def move(self):
        print('attention')
        print('move')

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def move(self):
        print('move')
        print(f'max speed is {self.max_speed}')


super = Truck(25)
super.move()  # проверяем методы
super.load()  # проверяем методы
print(f'Атрибуты экземпляра super: {super.__dict__}')  # атрибуты

super_2 = Car(50)
super_2.move()  # проверяем методы
print(f'Атрибуты экземпляра super_2: {super_2.__dict__}')  # атрибуты
