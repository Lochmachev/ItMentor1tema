# Дан диаметр окружности d. Найти ее длину{{ L = π·d, π = 3.14}}

def diametr():
    d = float(input('Введите диаметр : '))

    if d <= 0:
        print('Неверные данные !')
    else:
        L = d * 3.14
        print('Длина окружности = ', L)

diametr()