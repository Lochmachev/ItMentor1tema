# Даны два ненулевых числа.
# Найти сумму, разность, произведение и частное их квадратов.

a = float(input('Введите первое число : '))
b = float(input('Введите второе число : '))

def my ():
    if a <= 0 or b <= 0:
        print('Неверные данные !')
    else:
        S = a + b
        R1 = a - b
        R2 = b - a
        P = a * b
        Ch_Kv1 = a**2 / b**2
        Ch_Kv2 = b**2 / a**2
        print('Сумма = ',S)
        print('a-b = ',R1)
        print('b-a = ',R2)
        print('Произведение =',P)
        print('Частное квадратов ab = ', Ch_Kv1)
        print('Частное квадратов ab = ', Ch_Kv2)
my()