# создание пар ключ + значения, с разными типами данных
my_dict = {'Bayonetta': 600, 'Nier': '2B', 'EchoFrost': 'pre-alpha'}

# вывод на экран
print(my_dict)

# обращение по существующему ключу
print(my_dict['Bayonetta'])

# добавление данных в несуществующий ключ
my_dict['Department34'] = 'pre-alpha'

# обращение по несуществующему ключу
print(my_dict['Department34'])

# добавление с помощью метода .update() двух пар ключ + значение
my_dict.update({'Joyville2': 'beta', 'Smuta': False})
print(my_dict)

# удаляем ключ с помощью метода .pop, возвращая значение через переменную
theft = my_dict.pop('Smuta')

# вывод значение False, удаленного ключа 'Smuta', через обращение к объявленной переменной
print(theft)

# вывод из словаря пар ключ + значение с помощью метода items
print(my_dict.items())

# создаем множество
my_set = {1, 2, 2, 1 , False, False, True, 'string'}
print(my_set)

# добавляем во множество три новых значения, два из которых уникальны
my_set.update({3, 4, 4})
print(my_set)

# удаляем с помощью метода .discard, так-как он более предназначен для работы с множествами, в сравнении с методом .remove
my_set.discard(False)
print(my_set)