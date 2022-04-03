class ComplexNum:

    num_of_numbers = 0

    def __init__(self, re, im):
        self.re = re
        self.im = im
        ComplexNum.num_of_numbers += 1

    def __del__(self):
        print(f'Удалили число {self.re} + i*{self.im}')

    def __str__(self):
         return f"Комплексное число {self.re} + i*{self.im}"

    def __add__(self, other):
        return ComplexNum(self.re + other.re, self.im + other.im)

    def __eq__(self, other):
        return self.re == other.re and self.im == other.im

    @staticmethod
    def my_method():
        return f"Количество чисел - {ComplexNum.num_of_numbers}"

    @classmethod
    def class_method(cls):
        return(f'Инициализировано {ComplexNum.num_of_numbers} класса {cls}')


# mc = ComplexNum(1, 2)
# mc2 = ComplexNum(3, 4)
# print(mc)
# print(mc + mc2)
# print(mc == mc2)
# print(ComplexNum.my_method())
# print(ComplexNum.class_method())
# print(ComplexNum.__name__)
#
# del mc

class ParentClass:
    def __init__(self):
        print("Конструктор класса-родителя")

    def my_method(self):
        print("Метод my_method() класса ParentClass")


class ChildClass(ParentClass):
    def __init__(self):
        print("Конструктор дочернего класса")
        ParentClass.__init__(self)

    def my_method(self):
        ParentClass.my_method(self)
        print("Метод my_method() класса ChildClass")

# cc = ChildClass()
# cc.my_method()

from abc import ABC, abstractmethod

class CustomAbstractClass(ABC):

    @abstractmethod
    def method(self):
        pass

    @abstractmethod
    def method_2(self):
        pass


class MyClass(CustomAbstractClass):

    def method(self):
        pass

# my_list = [30, 105.6, "text", True]
# for el in my_list:
#     print(el)


# mc = MyClass()

class Iterator:
    def __init__(self, start=0, stop=5, step=1):
        self.i = start
        self.stop = stop
        self.step = step

    def __next__(self):
        self.i += self.step
        if self.i <= self.stop:
            return self.i
        else:
            raise StopIteration


class IterObj:
    def __init__(self, start, stop, step=1):
        self.start = start - 1
        self.stop = stop
        self.step = step
    def __iter__(self):
        return Iterator(self.start, self.stop, self.step)

# obj = IterObj(start=0, stop=9)
# for el in obj:
#     print(el)


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def square(self):
        return self.width * self.height

# r = Rectangle(10, 20)
# print(r.square)


class WindowAndDoor:
    def __init__(self, width, height):
        self.square = width * height


class Room:
    def __init__(self, width, length, height):
        self.square = 2 * height * (width + length)
        self.wd = []

    def add_wd(self, window_width, window_height):
        self.wd.append(WindowAndDoor(window_width, window_height))

    def needed_square(self):
        main_square = self.square
        for el in self.wd:
            main_square -= el.square
        return main_square


# r = Room(3,7,6)
# print(r.square)
# r.add_wd(2,2)
# r.add_wd(2,2)
# print(r.needed_square())

def test(a1=5, a2=5):
    return a1 + a2

print(test(4, 3))