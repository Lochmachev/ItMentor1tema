# Даны целые положительные числа A и B (A > B).
# На отрезке длины A размещено максимально возможное
# количество отрезков длины B (без наложений).
# Используя операцию взятия остатка от деления нацело,
# найти длину незанятой части отрезка A.

A = int(input('Длина отрезка A = '))
B = int(input('Длина отрезка B = '))

def a_b():
    if A <= 0 or B <= 0 or A < B :
        print('Некорректные данные !')
    else:
        Ost = A % B
        print('Остаток = ',Ost)