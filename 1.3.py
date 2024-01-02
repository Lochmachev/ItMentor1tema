# Даны стороны прямоугольника a и b.
# Найти его площадь S = a·b и периметр P = 2·(a + b)


def S_and_P(a,b):
    if a <= 0 or b <= 0:
        print('Неверные данные !')
    else:
        s = a * b
        p = (a+b)* 2
    return s,p

a = float(input('Введите длину стороны а : '))
b = float(input('Введите длину стороны в : '))
print(S_and_P(a,b))
