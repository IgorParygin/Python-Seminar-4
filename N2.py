# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import random

def write_file(name, st):
    with open(name, 'w') as data:
        data.write(st)


def create_koef(k):
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
                if my_list[i + 1] != 0 or my_list[i + 2] != 0:
                    a += ' + '
            elif i == len(my_list) - 2 and my_list[i] != 0:
                a += f'{my_list[i]}x'
                if my_list[i + 1] != 0 or my_list[i + 2] != 0:
                    a += ' + '
            elif i == len(my_list) - 1 and my_list[i] != 0:
                a += f'{my_list[i]} = 0'
            elif i == len(my_list) - 1 and my_list[i] == 0:
                a += ' = 0'
    return a


def stepen_mn(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i + 1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num

def koef_mn(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num


def calc_mn(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    k = 0
    if stepen_mn(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1
    ii = l - 1
    while ii >= 0:
        if stepen_mn(st[ii]) != -1 and stepen_mn(st[ii]) == i:
            lst.append(koef_mn(st[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1

    return lst


k1 = int(input("Введите натуральную степень для первого файла k = "))
k2 = int(input("Введите натуральную степень для второго файла k = "))
koef1 = create_koef(k1)
koef2 = create_koef(k2)
write_file("file1.txt", create_str(koef1))
write_file("file2.txt", create_str(koef2))

with open('file1.txt', 'r') as data:
    st1 = data.readlines()
with open('file2.txt', 'r') as data:
    st2 = data.readlines()
print(f"Первый многочлен {st1}")
print(f"Второй многочлен {st2}")
list1 = calc_mn(st1)
list2 = calc_mn(st2)
ll = len(list1)
if len(list1) > len(list2):
    ll = len(list2)
lst_new = [list1[i] + list2[i] for i in range(ll)]
if len(list1) > len(list2):
    mm = len(list1)
    for i in range(ll, mm):
        lst_new.append(list1[i])
else:
    mm = len(list2)
    for i in range(ll, mm):
        lst_new.append(list2[i])
write_file("file3.txt", create_str(lst_new))
with open('file3.txt', 'r') as data:
    st3 = data.readlines()
print(f"Сумма многочленов {st3}")
