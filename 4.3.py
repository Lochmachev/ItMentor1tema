# Дан список [«a», «s», «1», «a», «32», «23»].
# Разбейте его на два списка: только с буквами и только с числами.

Ls = ['a', 's', '1', 'a', '32', '23']
Ls1 = []
Ls2 = []

for x in Ls[:]:
    if x.isalpha():
        Ls1 += x
    else:
        Ls2 += x

print(Ls1)
print(Ls2)

Ls1.pop(-1)
Ls1.reverse()
print(Ls1)