# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random


def write_file(st):
    with open('file.txt', 'w') as data:
        data.write(st)

def create_mn(k):
    my_list = [random.randint(0, 101) for i in range(k + 1)]
    return my_list


def create_str(sp):
    my_list = sp[::-1]
    a = ''
    if len(my_list) < 1:
        a = 'x = 0'
    else:
        for i in range(len(my_list)):
            if i != len(my_list) - 1 and my_list[i] != 0 and i != len(my_list) - 2:
                a += f'{my_list[i]}x^{len(my_list) - i - 1}'
                if my_list[i + 1] != 0:
                    a += ' + '
            elif i == len(my_list) - 2 and my_list[i] != 0:
                a += f'{my_list[i]}x'
                if my_list[i + 1] != 0:
                    a += ' + '
            elif i == len(my_list) - 1 and my_list[i] != 0:
                a += f'{my_list[i]} = 0'
            elif i == len(my_list) - 1 and my_list[i] == 0:
                a += ' = 0'
    return a


k = int(input("Введите натуральную степень k = "))
koef = create_mn(k)
write_file(create_str(koef))
print(create_str(koef))