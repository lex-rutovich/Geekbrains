# 1. Создать программный файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

with open('lesson-5-1-file.txt', 'w', encoding='utf-8') as f:
    newline = input('Вводите строки для записи в файл, пустую строку для окончания.\nСтрока: ')
    while newline:
        print(newline, file=f)
        newline = input('Строка: ')


# 2. Создать текстовый файл (не программно),
# сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

# посчитаем количество строк и слов в файле 'lesson-5-2-file.txt'

with open('lesson-5-2-file.txt', 'r') as some_file:
    content = some_file.readlines()

print(f'Количество строк в файле: {len(content)}')

words = 0
for line in content:
    words = words + len(line.split())

print(f'Количество слов в файле: {words}')


# 3. Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч,
# вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.

from statistics import mean

with open('lesson-5-3-file.txt', 'r', encoding='utf-8') as salaries:
    salaries_cont = salaries.readlines()

salaries_db = {}
for line in salaries_cont:
    pair = line.split()
    salaries_db.update({pair[0]: float(pair[1])})

print(f'Оклад менее 20 тысяч получают: {", ".join([key for key, val in salaries_db.items() if val < 20000])}')
print(f'Средняя величина дохода сотрудников: {round(mean(salaries_db.values()),2)}')


# 4. Создать (не программно) текстовый файл со следующим содержимым:
#
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

numbers = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}

with open('lesson-5-4-input.txt', 'r') as src_file:
    content = src_file.readlines()

with open('lesson-5-4-output.txt', 'w', encoding='utf-8') as dst_file:
    for line in content:
        words = line.split()
        print(f'{numbers.get(int(words[2]))} {words[1]} {words[2]}', file=dst_file)


# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

from random import randint

# генерируем набор из 100 псевдослучайных чисел от 0 до 100
some_numbers = [randint(0, 100) for num in range(100)]

# записываем набор чисел, разделеных пробелами, в файл lesson-5-5-file.txt
with open('lesson-5-5-file.txt', 'w') as lesson5_file:
    print(*some_numbers, sep=' ', file=lesson5_file)

# считываем числа из файла и выводим их сумму
with open('lesson-5-5-file.txt', 'r') as lesson5_file:
    content = lesson5_file.read()
    print(f'Общая сумма чисел в файле равна: {sum([int(s) for s in content.split()])}')


# 6. Сформировать (не программно) текстовый файл.
# В нём каждая строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
#
# Сформировать словарь, содержащий название предмета и
# общее количество занятий по нему. Вывести его на экран.
#
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —

# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import re

subjects = {}

with open('lesson-5-6-file.txt', 'r', encoding='utf-8') as lrn_plan:
    content = lrn_plan.readlines()

for line in content:
    subject = line.split()[0]
    # поищем все числа в строке с помощью regexp и функции findall()
    study_load = sum([int(i) for i in re.findall(r'\d+', line)])
    subjects.update({subject:study_load})

print(subjects)


# 7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме:
# название, форма собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл,
# вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
#
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

from statistics import mean
from json import dump, load

result = []
profits = {}
avg_profit = {}

with open('lesson-5-7-input.txt', 'r', encoding='utf-8') as fin_results:
    content = fin_results.readlines()

for row in content:
    cells = row.split()
    profits.update({cells[0]: float(cells[2]) - float(cells[3])})

result.append(profits)
result.append({'average_profit': mean([i for i in profits.values() if i > 0])})

with open('lesson-5-7-output.txt', 'w', encoding='utf-8') as out_file:
    dump(result, out_file)