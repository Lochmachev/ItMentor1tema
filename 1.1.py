# Дана сторона квадрата a. Найти его периметр P = 4·a

def get_perimetr(a):
    if a <= 0:
        print('Неверные данные !')
    else:
        p = 4 * a
        return p

side = float(input('Введите длину стороны : '))
print(get_perimetr(side))