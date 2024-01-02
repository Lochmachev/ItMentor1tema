# Даны длины ребер a, b, c прямоугольного параллелепипеда.
# Найти его объем V = a·b·c и площадь поверхности S = 2·(a·b + b·c + a·c)

a = float(input('Введите длину стороны a : '))
b = float(input('Введите длину стороны b : '))
c = float(input('Введите длину стороны c : '))

def pr_par():
    if a <= 0 or b <= 0 or c <= 0:
        print('Невеintрные данные !')
    else:
        V = a * b * c
        S = 2 * (a*b + b*c + a*c)
        print('Объём = ',V)
        print('Площадь = ',S)
pr_par()