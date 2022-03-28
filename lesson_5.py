# f_obj = open('my_text.txt', 'r', encoding='utf-8') # r - read - на чтение
# content = f_obj.readline()
# print(content)
# f_obj.close()
#
# f2_obj = open('my_text_2.txt', 'a')
# content_2 = f2_obj.write('\nДо свидания!')
# f2_obj.close()

# with open("my_text.txt", 'r', encoding='utf-8') as f_obj:
#     for i in f_obj.readlines():
#         print(i)
#
# f_obj = open("my_text.txt")
# print(f_obj.closed)

# try:
#     f_obj = open("my_text.txt", 'r')
#     for line in f_obj:
#         print(line)
# except IOError:
#     print("Произошла ошибка ввода-вывода!")
# finally:
#     f_obj.close()

# with open('my_file.txt', 'r', encoding='utf-8') as f:
#     for i in range(int(input())):
#         print(f.read())
#         print(f.tell())
#         f.seek(0)
#         print(f.tell())

# with open("my_text.txt") as text_file:
#     print(text_file.tell())
#     content = text_file.read()
#     print(text_file.tell())
#     text_file.seek(10)
#     print(text_file.tell())
#     content_2 = text_file.read()
#     print(content_2)

# with open("my_text.txt", "a", encoding='utf-8') as f_obj:
#     print("Необычная работа функции print", file=f_obj)

# import os
# os.remove('test_file.txt')
# os.rename('my_file.txt', 'test_file.txt')
# C:\Users\Ильяс\PycharmProjects\gb_python_basics
# abs_path = os.path.join(r'C:\Users\Ильяс\PycharmProjects', 'gb_python_basics')
# print(abs_path)

import json

# data = {"income": {"salary": 10000, "bonus": 5000}}

# with open("my_file.json", "w") as write_json:
#     json.dump(data, write_json)

# with open("my_file.json") as read_json:
#     data = json.load(read_json)
#
# print(data)
# print(type(data))

# json_str = """{"income": {"salary": 50000, "bonus": 20000}}"""
# data = json.loads(json_str)
# print(data)
# print(type(data))

# with open('my_file.txt', 'w', encoding='utf-8') as obj_1:
#     obj_1.write('Привет!')
#
import shutil
shutil.copyfile('my_text_2.txt', 'my_text_2_copy.txt')

# import sys
# print(sys.path)
# for i in range(10):
#     print(i)
#     if i == 3:
#         print('Я устал, я ухожу')


# print(sys.executable)