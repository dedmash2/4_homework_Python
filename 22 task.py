"""
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества.
m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
"""
n = int(input("Введите кол-во элементов первого множества: "))
m = int(input("Введите кол-во элементов второго множества: "))
N = []
M = []
for i in range(n):
    N.append(int(input()))
for i in range(m):
    M.append(int(input()))
NM = N + M

clear_list = []
for i in NM:
    if NM.count(i) > 1 and i not in clear_list:
        clear_list.append(i)
print(clear_list)
