# Создайте словарь содержащий данные о человеке.
# В качестве строковых ключей используйте егоимя, возраст, пол, рост, вес, размер ноги.

d = {'name':'Николай','age':'41','gender':'М',
     'height':'167','wt':'75','foot_size':'41' }

# Выведите на экран все данные о человеке по ключам.

for key,value in d.items():
    print(key, ' - ', value)

# Добавьте в словарь ключ и значение размера ноги

del d['foot_size']
print(d)

d['foot_size'] = 41
print(d)

# Удалите из словаря возраст.

d.pop('age')
for key,value in d.items():
    print(key, ' - ', value)