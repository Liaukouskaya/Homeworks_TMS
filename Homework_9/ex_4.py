# Create Metaclass

MyClass = type('MyClass', (object,), {})
print(MyClass)

# def my_metaclass(name, parents, attributes):
#     return 'Hello'
#
# class My_class(metaclass = my_metaclass):
#     pass
#
#
# print(My_class)
# a = My_Class()

def my_metaclass(name, parents, attributes):
    return 'fgf'


class My_class(metaclass=my_metaclass())
    pass

print(My_class)