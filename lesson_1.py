# a = 10
# b = a + 5
# print("10 + 5 =", b)

# print(2 + 2 == 3)

# price = 'price!'
# print(type(price))
# price = 1000
# print(type(price))
# print(type(3.23526))
# print(type(True))

# print(4 ** 2)

# a = input()
# print(a / 2)

# a = int(input("Введите число: "))
# if a % 2 == 0 and a != 0:
#     print('Число чётное!')
# elif a % 2 != 0:
#     print('Число нечётное!')
# else:
#     print('Это же ноль!')
# print('Программа завершена!')

# original_password = 'x777' # правильный пароль, хранится в программе
# password = input('Введите пароль: ')  # просим пользователя ввести пароль
# access = False  # переменная, хранит разрешение на доступ
# if password == original_password: # если введен правильный пароль
#     print('Пароль принят, добро пожаловать в систему')
#     access = True
# if password != original_password: # если введен неправильный пароль
#     print('Пароль неверен, вход запрещен')
# print(access)

counter = 0
while True:
    counter += 1
    if counter % 2 != 0:
        continue
    print(f'Квадрат числа {counter} равен {counter ** 2}')
    if counter == 10:
        break

print()
print('Пример!')
print(f"{5 / 3:.2f}")
