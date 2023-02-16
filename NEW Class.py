# 16.02 H/W
#Перевернуть строку 1000000001 
# Работа через цикл


#############################
val_str = 'string'
some_list = []
some_list.extend('string')
i = some_list.index('i')
some_list[3] = 'O'
print(some_list)

# или

val_str = 'string'
some_list = []
some_list.extend('string')
i = some_list.index('i')
some_list[i] = 'O'
print(some_list)
#############################

# 16.02 / 2023
# set (множество) \ одна из самх быстрых структур
# объявляется  set()
# структура обозначается {1, 2, 3}
# работает с int, float, bool, str, tuple   ---------------   В SET ВХОДЯТ ТОЛЬКО НЕИЗМЕНЕННЫЕ ТИПЫ ДАННЫХ 
# не работает с list
# (Python 3.9 3.10 работает)

some_set_type = set()
print(type(some_set_type))

some_set_1 = {1,2,3}
print(some_set_1)

some_set_2 = {True, False}
print(some_set_2)

some_set_3 = {'s' 't' 'r'} 
print(some_set_3)

some_set_4 = tuple
print(some_set_4)

# НЕ РАБОТАЕТ
some_set_5 = ['list']
print(some_set_5)

# \НЕ РАБОТАЕТ


# syntax sugar
not_unic_list = [1, 2, 1, 5, 2]
unic_list = []
for i in not_unic_list:
    if i not in unic_list:
        unic_list.append(i)
print(unic_list)

set_unic = set(not_unic_list)
print(set_unic)





# 16.02 / 2023
# set (множество) \ одна из самх быстрых структур
# SET это изменяемая структура данных включающая неизменяемые элементы (неизменяемые уникальные элементы)
# объявляется  set()
# структура обозначается {1, 2, 3}
# работает с int, float, bool, str, tuple   ---------------   В SET ВХОДЯТ ТОЛЬКО НЕИЗМЕНЕННЫЕ ТИПЫ ДАННЫХ 
# ИСКЛЮЧЕНИЯ: set не может быть set ----------   не работает с list    ---------     set изменяемый, но принимает только неизменяемые значения
# (Python 3.9 3.10 работает)
# 


# SET это изменяемая структура данных включающая неизменяемые элементы (неизменяемые уникальные элементы)
some_set_type = set()
print(type(some_set_type))

some_set_1 = {1,2,3}
print(some_set_1)

some_set_2 = {True, False}
print(some_set_2)

some_set_3 = {'s' 't' 'r'} 
print(some_set_3)

some_set_4 = tuple
print(some_set_4)

# НЕ РАБОТАЕТ
some_set_5 = ['list']
print(some_set_5)

# \НЕ РАБОТАЕТ


# syntax sugar ________ под капотом set
not_unic_list = [1, 2, 1, 5, 2]
unic_list = []
for i in not_unic_list:
    if i not in unic_list:
        unic_list.append(i)
print(unic_list)

set_unic = set(not_unic_list)
print(set_unic)


# МЕТОДЫ

# добавление в set через add
my_set_1 = {1, 2, 3}
my_set_1.add(4)
print(my_set_1)

# стирает все в set
my_set_2 = {1, 2, 3}
my_set_2.clear
print(my_set_2)


# объединение union
my_set_3 = {1, 2, 3}
my_set_3.union([1, 5, 9, 3])
print(my_set_3)

new_set = my_set_3 | {1, 5, 9, 3}
print(new_set)


# ***Лист листа           ОШИБКА Exception has occurred: TypeError unhashable type: 'list'
#my_set_4 = set([1,[2,3]])
#print(my_set_4)



# УДАЛЕНИE --------

# удаление через pop           нельзя взять через index т.к. pop удаляет и возвпращает рандомые объекты
my_set_4 = {1, 2, 3}
my_set_4.pop()
print(my_set_4)


# удаление через remove (значения обязательны должны находиться в set) 
my_set_5 = {1, 2, 3}
my_set_5.remove(1)
print(my_set_5)


# удаление через .discard   (если вставить несуществующее значение ничего не произойдет)  (БЕЗОПАСНОЕ УДАЛЕНИЕ)   discard. лучше записывать в set 
my_set_6 = {1, 2, 3}
my_set_6.discard(3)
print(my_set_6)

# \УДАЛЕНИЕ --------


# .difference ------------

# (выводит то, что не повтаряется)
my_set_7 = {1, 2, 3}
my_other_set = {1, 5, 9, 3}
my_other_set.difference(my_set_7)
print(my_other_set)

# в данном выводит всё, что нету в my_set_8
my_set_8 = {1, 5, 9, 3} 
my_other_set = {1, 2, 3} #my_set_8
my_other_set.difference(my_set_8)
print(my_other_set)

# 
my_set_9 = {1, 5, 9, 3} 
my_other_set_2 = {1, 2, 3, 8}
minus_set = my_set_9 - my_other_set_2
print(minus_set)

# \.difference ------------
