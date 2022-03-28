# import lesson_3
#
# print(lesson_3.plus(4, 5))

# from lesson_3 import plus
#
# print(plus(4, 5))

# from time import sleep, time
# import random
#
# print('Засыпаю!')
# print(time())
# sleep(5)
# print('Проснулся!')


# from sys import argv
#
# arg_0, arg_1, arg_2, arg_3 = argv
#
# print(f'Введены параметры {arg_0}, {arg_1}, {arg_2}, {arg_3}')

# my_list = list(range(10))
# new_list = [el**2 for el in my_list]
# print(new_list)
# new_dict = {el: el**2 for el in my_list}
# print(new_dict)
# my_set = {el for el in my_list}
# print(my_set)

import random
#
# print(random.random())
# print(random.randint(5, 500))
# print(random.randrange(1,6,2))

# generator = (param ** 2 for param in range(5))

# print(next(generator))
# print(next(generator))
# print(next(generator))

# def generator(my_list):
#     for el in my_list:
#         yield el
#
# my_list = [random.randint(1, 10) for i in range(10)]
# my_list = [1, 2, 3, 4]
# g = generator(my_list)
# g = (el for el in my_list)
# print(g)
# #
# for el in g:
#     print(el)

import itertools

# for el in itertools.count(8):
#     print(el)
#     if el == 20:
#         break

counter = 0
for i, element in enumerate(itertools.cycle('hello')):
    print(element)
    if counter == 10: break


from functools import partial, reduce

# from lesson_3 import plus

def stepen(a, b):
    return a ** b

def mult(a, b):
    return a * b

from lesson_3 import plus

# print(reduce(mult, [1, 2, 3]))

# result = 1
# for i in [1,2,3,4,5]:
#     result = mult(result, i)
#
# print(result)

# new_stepen = partial(stepen, b=2)
# print(new_stepen(9))

# from random import randint


# def generator_sqr(how_many_squares):
#     for i in range(how_many_squares):
#         yield i**2
#
# squares = [el**2 for el in range(10)]
#
# print(f'Последовательнсть квадратов чисел от 0 до 9: {[a for a in generator_sqr(10)]}')


