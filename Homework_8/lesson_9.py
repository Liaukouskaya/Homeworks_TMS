# class MyClass():
#     TOTAL_OBJECTS = 0
#
#     def __init__(self):
#         MyClass.TOTAL_OBJECTS = MyClass.TOTAL_OBJECTS + 1
#
#     @classmethod
#     def total_objects(cls):
#         print("Total objects: ", cls.TOTAL_OBJECTS)
#
#
# # Создаем объекты родительского класса
# my_obj1 = MyClass()
# my_obj2 = MyClass()
#
#
# # Создаем дочерний класс
# class ChildClass(MyClass):
#     TOTAL_OBJECTS = 0
#     pass
#
# MyClass.total_objects()
# ChildClass.total_objects()


class Human:
    """Человек, возраст которого не может быть больше 120 и меньше 0"""

    def __init__(self, age=0):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 120 and age > 0:
            self.__age = age
        else:
            self.__age = 0


h = Human(age=30)
h.age = 150
print(h.age)
