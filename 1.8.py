# Даны два числа a и b. Найти их среднее арифметическое: (a + b)/2

import statistics
a = float(input('Введите первое число : '))
b = float(input('Введите второе число : '))

def sr_ar():
    sym = [a, b]
    Sr = statistics.mean(sym)
    print('Среднее ариф. = ',Sr)
sr_ar()