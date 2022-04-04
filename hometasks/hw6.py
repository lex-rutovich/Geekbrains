# 1. Создать класс TrafficLight (светофор).
#
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы:
# красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд,
# второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться
# только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep


class TrafficLight:
    _color = 'Красный'
    __red_delay = 7
    __yellow_delay = 2
    __green_delay = 5

    def running(self):
        """ Метод переключения состояния светофора
        Выводит текущее состояние,
        после установленной задержки переключает его к следующему
        и выводит время задержки и новое состояние.
        ps. По идее за зеленым должен идти желтый,
        но по условию задания выше - сразу опять красный
        :return: void
        """
        print(f'{self._color} >> переключается за ', end='')
        if self._color == 'Красный':
            sleep(self.__red_delay)
            print(f'{self.__red_delay} сек. на', end=' ')
            self._color = 'Желтый'
        elif self._color == 'Желтый':
            sleep(self.__yellow_delay)
            print(f'{self.__yellow_delay} сек. на', end=' ')
            self._color = 'Зелёный'
        else:
            sleep(self.__green_delay)
            print(f'{self.__green_delay} сек. на', end=' ')
            self._color = 'Красный'
        print(f'>> {self._color}')


tl_1 = TrafficLight()
tl_1.running()
tl_1.running()
tl_1.running()
tl_1.running()
tl_1.running()
tl_1.running()
tl_1.running()


# 2. Реализовать класс Road (дорога).
#
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу:
# длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    # задаим параметры по умолчанию как аттрибуты класса Road
    _length = 5000
    _width = 20
    _cost = 25
    _roadbed_thickness = 5

    def __init__(self, length=_length, width=_width):
        """ Инициализатор класса
        :param length: по умолчанию равен аттрибуту класса Road._length
        :param width: по умолчанию равен аттрибуту класса Road._width
        """
        self._length = length
        self._width = width

    def calc_asfalt(self, cost=_cost, roadbed_thickness=_roadbed_thickness):
        """ Метод расчета массы асфальта
        :param cost: удельные затраты асфальта на 1 кв.м толщиной 1 см, по умолчанию равен Road._cost
        :param roadbed_thickness: толщина покрытия, по умолчанию равен Road._roadbed_thickness
        :return: рассчитанное значение массы асфальта
        """
        return self._width * self._length * cost * roadbed_thickness


some_road = Road(length=1000, width=25)
print(some_road.calc_asfalt(30, 3))


# 3. Реализовать базовый класс Worker (работник).
#
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};

# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных:
# создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
        self._total_income = self._income['wage'] + self._income['bonus']

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._total_income


some_role = Position('John', 'Smith', 'CIO', 10000, 150000)
print(some_role.get_full_name())
print(some_role.get_total_income())


# 4. Реализуйте базовый класс Car.
#
# у класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы:
# go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля;

# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def show_speed(self):
        print(f'{self.name} едет со скоростью: {self.speed}')

    def go(self, speed):
        self.speed = speed
        self.show_speed()

    def stop(self):
        self.speed = 0
        print(f'{self.name} остановился')

    def turn(self, direction):
        print(f'{self.name} повернул {direction}')


class TownCar(Car):
    def __init__(self, name, color='black', speed=60):
        super().__init__('TownCar ' + name, color, speed, False)

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} превышает скорость!', end=' ')
        super().show_speed()


class WorkCar(Car):
    def __init__(self, name, color='yellow', speed=40):
        super().__init__('WorkCar ' + name, color, speed, False)

    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} превышает скорость!', end=' ')
        super().show_speed()


class SportCar(Car):
    def __init__(self, name, color='red&white', speed=120):
        super().__init__('SportCar ' + name, color, speed, False)


class PoliceCar(Car):
    def __init__(self, name, color='blue&yellow', speed=140):
        super().__init__('PoliceCar ' + name, color, speed, True)


car_1 = SportCar('Lightning McQueen', 'red', 180)
car_2 = TownCar('Luigi', 'yellow', 55)
car_3 = WorkCar('Guido', 'custom blue', 50)
car_4 = PoliceCar('Sheriff', 'black')

car_1.show_speed()
car_2.show_speed()
car_3.show_speed()
car_3.go(35)
car_4.show_speed()
car_1.turn('налево')
car_1.stop()
car_4.turn('направо')
print(f'У {car_1.name} цвет {car_1.color}')
print(f'У {car_2.name} цвет {car_2.color}')
print(f'У {car_3.name} цвет {car_3.color}')
print(f'У {car_4.name} цвет {car_4.color}')
car_2.go(70)
print(f'{car_2.name} - это {"" if car_2.is_police else "не "}полицейская машина')
print(f'{car_4.name} - это {"" if car_4.is_police else "не "}полицейская машина')


# 5. Реализовать класс Stationery (канцелярская принадлежность).
#
# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stationery:
    title = ''

    def draw(self):
        print('Запуск отрисовки для класса Stationery')


class Pen(Stationery):

    def __init__(self):
        Pen.title = 'Ручка'

    def draw(self):
        print(f'Рисует {Pen.title}')


class Pencil(Stationery):

    def __init__(self):
        Pencil.title = 'Карандаш'

    def draw(self):
        print(f'Чертит {Pencil.title}')


class Handle(Stationery):

    def __init__(self):
        Handle.title = 'Маркер'

    def draw(self):
        print(f'Выделяет {Handle.title}')


items = [Pen(), Pencil(), Handle()]

for item in items:
    item.draw()