class Automobile:
    #атрибуты класса
    # auto_name = "BMW"
    # auto_model = "1-series"
    # auto_year = 2019

    def __init__(self, auto_name, auto_model, auto_year):
        self.auto_name = auto_name
        self.auto_model = auto_model
        self.auto_year = auto_year


    #методы класса
    def auto_start(self, s):
        print(f'Автомобиль заведён {s}')


# a = Automobile('Mazda', 'RX-8', 2006)
# b = Automobile('Mercedes', 'E-class', 2020)
# c = Automobile('Lada', 'Vesta', 2022)
# print(a)
# print(type(a))
# print(a.auto_year)
# print(b.auto_model)
# print(c.auto_name)
# a.auto_start(7)


class Transport:
    consumption = 500

    def custom_method(self):
        print('Я - метод для родительского класса транспорт')

class Auto(Transport):
    auto_count = 0

    def __init__(self, auto_name, auto_model, auto_color):
        self.__auto_color = auto_color
        self.auto_name = auto_name
        self._auto_model = auto_model
        Auto.auto_count += 1
        print(f'Сейчас на карте {Auto.auto_count} авто!')


    def auto_stop(self, param_1, param_2 = None):
        if param_2 is not None:
            print(param_1 + param_2)
        else:
            print(param_1)

    def get_class_info(self):
        print('Детальная информация о классе')

class Bus(Transport):
    consumption = 1000
    def custom_bus_method(self):
        print("Дочерний метод автобуса!")

# a = Auto('Lada', 'Priora', 'black')
#
# a.auto_stop(5)
# a.auto_stop(5, 10)

# a = Auto('Lada', 'Priora', 'black')
#
# print(a.auto_name)
# a._auto_model = 'Vesta'
# print(a._auto_model)

# a._Auto__auto_color = 'red'
# print(a._Auto__auto_color)

# b = Auto('BMW', '1-series', 'white')

# b.custom_method()
# print(b.consumption)
# c = Bus()
# print(c.consumption)
# c.custom_bus_method()

class Gadget:

    charge = 1000

    def gadget_method(self):
        print("Родительский метод класса Gadget")

class Navigator:

    charge = 2000

    def navigator_method(self):
        print("Родительский метод класса Navigator")

class ElectricNavigator(Gadget, Navigator):
    def electric_method(self):
        print("Дочерний метод класса ElectricNavigator")

en = ElectricNavigator()
# en.navigator_method()
# en.electric_method()
# en.gadget_method()
# print(en.charge)

class Shape:
    def __init__(self, color, param_1, param_2):
        self.color = color
        self.param_1 = param_1
        self.param_2 = param_2

    def square(self):
        return self.param_1 * self.param_2


class Rectangle(Shape):
    def __init__(self, color, param_1, param_2, rectangle_p):
        super().__init__(color, param_1, param_2)
        self.rectangle_p = rectangle_p

    def get_r_p(self):
        return self.rectangle_p


class Triangle(Shape):
    def __init__(self, color, param_1, param_2, triangle_p):
        super().__init__(color, param_1, param_2)
        self.triangle_p = triangle_p

    def square(self):
        return 1/2

# r = Shape("white", 10, 20)
# print(r.square())
t = Triangle("red", 30, 40, False)
print(t.square())

