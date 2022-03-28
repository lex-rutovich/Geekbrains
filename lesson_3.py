def plus(arg_1, arg_2):
    '''Функция возвращает сумму двух аргументов

    Именованные параметры:
    arg_1 - первое слагаемое
    arg_2 - второе слагаемое

    '''
    return arg_1 + arg_2

# a = plus(4, 5)
# print(a)

# print(plus(4, 5))

def plus_2(arg_1, arg_2):
    print(arg_1 + arg_2)
    return

# print(plus(4, 5))
# print(plus_2(4, 5))

# a = plus(4, 5)
# print(plus(4, 2))
# print(a)

def none_type():
    print('Я ничего не возвращаю!')
    return

# print(none_type())

def minus(a, b):
    pass

def s_calc():
    try:
        r_val = float(input("Укажите радиус: "))
        h_val = float(input("Укажите высоту: "))
    except ValueError:
        return
    s_side = 2 * 3.14 * r_val * h_val
    s_circle = 3.14 * r_val ** 2
    s_full = s_side + 2 * s_circle
    return r_val, h_val

# s_side_val, s_full_val = s_calc()
# print(f"Площадь боковой пов-ти - {s_side_val}; Полная площадь - {s_full_val}")
# a = 10

def divide(divider = 10, divisor = 2):
    return divider / divisor

# b = divide(divisor = 7, divider = 14)
# a = divide()
# print(a)
# print(b)
# b = divide(divisor=5, divider=10)
# print(a)
# print(b)
# c = divide(10)
# print(c)

def summa(*args):
    summa = 0
    for element in args:
        summa += element
    return summa


# print(summa(4, 5, 1, 2, 3))

# print(my_func(arg_1 = 2, arg_2 = 3))

# average = lambda s1, s2: (s1 + s2)/2
# print(average(6, 8))

# def my_func(*args):
#     return sum(args)

# print(my_func(10, 29, 50, 50))

# def my_func_2(**kwargs):
#     return kwargs

# print(my_func_2(arg_1=10, arg_2=30, arg_4=50))

#
# for el in range(1, 9):
#     print(el**2)

def full_s_calc():
    global r_val, h_val, s_side, s_circle
    r_val = float(input("Укажите радиус: "))
    h_val = float(input("Укажите высоту: "))
    s_side = 2 * 3.14 * r_val * h_val
    s_circle = 3.14 * r_val ** 2
    s_full = s_side + 2 * s_circle
    return s_full
#
# s_val = full_s_calc()
# print(s_val)
# print(s_circle)
# print(r_val)

def ext_func():
    my_var = 0
    def int_func():
        nonlocal my_var
        my_var += 3
        return my_var
    return int_func

# func_obj = ext_func()
# print(func_obj)
# print(func_obj())
# print(func_obj())
# print(func_obj())

if __name__ == '__main__':
    a: int = 5
    print(a)
