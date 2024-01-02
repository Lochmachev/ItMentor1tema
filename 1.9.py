# Даны два неотрицательных числа a и b.
# Найти их среднее геометрическое, т. е.
# квадратный корень из их произведения: (a·b)1/2

import statistics
a = float(input('Введите первое число : '))
b = float(input('Введите второе число : '))

def sr_geo ():
    sym = [a, b]
    Sr = statistics.geometric_mean(sym)

    # Sr = (a * b) / 2

    print('Среднее геометр. = ',Sr)
sr_geo()