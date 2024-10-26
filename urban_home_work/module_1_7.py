immutable_var = 1, 2, True, 'String'
print(immutable_var)

immutable_var = tuple([1, 2] + [True, 'String']) # создаем кортеж с двумя вложенными элементами
immutable_var_1 = list(immutable_var) # преобразуем кортеж в list, записывая tuple внутрь новой переменной
immutable_var_1[0] = 'modified' # меняем по индексу первый элемент внутри первого списка
print(immutable_var_1) # выводим преобразованный tuple в list, с измененным первым элементом
# если пытаться изменить элемент tuple без предварительного преобразования в list, то - это не возможно
# кортеж - это не изменяемый тип данных, если только предварительно не преобразовать кортеж в list, записав преобразование в новую переменную

mutable_list = [[1, False, 'Not string'], [2, True, 'Another string']]
mutable_list[1][0] = 5
mutable_list[1][1] = False
mutable_list[1][2] = 'STRING'
print(mutable_list)
