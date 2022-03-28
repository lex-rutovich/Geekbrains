# print(abs(-6))
# print(bin(4))
# print(4 << 6)
# print(bin(256))
# print(4 >> 6)

# print(type(4))
# print(type(4.1245))
# print(complex(3,5))

# s1 = 'privet'
# s2 = ' student'
# print(type(s1))
# print(s1 + s2)
# print(s1[5:1:-2])
# print(s1.upper())

# print(s1.islower())

a = [1,2,3,4,3,3,3,3,3,0.31]

# while a.count(3) > 0:
#     a.remove(3)
# print(a)
# a.reverse()
# print(a)
# a.append(5)
# print(a[3:6])
# a.insert(1, 3)
# print(a)
# a.remove(1)
# print(a)
# a.remove(3)
# print(a)
# a.sort(reverse=True)
# print(a)

# kortage = (1,3,5,7)
# print(kortage)

# spisok = list((1,2,3,4,5))
# mnojestvo = set('abrakadabra')
# print(mnojestvo)
# print(mnojestvo.pop())
# print(mnojestvo)
# print(list(mnojestvo))

# capitals = {"Russia": "Moscow", "Germany": "Berlin"}
# capitals_2 = dict(key_1='val_1', key_2='val_2')
# print(capitals)
# print(capitals_2)
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
# print(capitals.setdefault("France"))
# print(capitals)
# capitals["France"] = 'Paris'
# print(capitals)
# capitals.update(capitals_2)
# print(capitals)

# print(2 + 2 == 3)

# print(b'text'.decode('utf-8'))
# print('text'.encode('utf-8'))
# print(bytes([10, 20, 30, 40, 50]))
#
# a = bytearray(b"text text2 text3")
# spisok = [1,2,'stroka',10,100]
# print(spisok[1:4])

# try:
#     print('hello')
#     a = 500/0
#     print('bye')
#     while True:
#         print('ывпывп')
# except ZeroDivisionError:
#     print('Нельзя делить на ноль!')
#     print('Вы что! В самом деле!')
#     a = 500/1
#
# print(a)
# stroka = 'abrakadabra'
# for element in stroka:
#     print(element)

# spisok = [1,2,3]
# new_spisok = []
# for element in spisok:
#     new_spisok.append(element*2)
#
# print(new_spisok)

# a = 4
# b = 0
# print(a/b if b != 0 else 0)

# a = 4.0
# b = 4
# print(a is not b)

# my_list = [[10,20,30], [40,50], [60, 70]]
# print(sum(my_list, []))

# a = 2
# b = 3
#
# a,b = b,a
# print(a,b)

my_list = [1,2,3,3,1,2,3,4,5,5,5,3,6,7,4]
print(max(set(my_list), key=my_list.count))
print(my_list.count(3))

# n = 10
# for i in range(1,n,2):
#     print(i)