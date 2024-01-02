# Дана сторона квадрата a. Найти его площадь{{ S = a2}}

def S (a):
    if a <= 0:
        print('Неверные данные !')
    else:
        s = a ** 2
        return s

a = float(input('Введите длину стороны : '))
print(S(a))
