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



# 21.02 / 2023
# list и set
# проверка id переменных (проверка переменных, а также их копий) - id разные в copy и в переменной без copy
# 
#       dip copy это "[:]" под капотом выполняется через   for i in test_list: 
#                                                          copy_list.append(i)
#
#
#
#



# о листах 
test_list = [ [1], [2], [3] ]
copy_list = test_list.copy()
print(id(copy_list))
copy_list.append(['y'])
print(copy_list)
print(id(copy_list))


print(id(test_list))
print(test_list)

test_list.append([4])
test_list[0][0] = ['x']
print(test_list)

# ________________________________________
# пустой сет может быть только один #3

#1 неверно
test_list = { }

#2 неверно
test_list = {}

#3 выполняется!!!
test_list = set()
# ________________________________________

# /о листах 




# о SET

test_set = set()
test_set.add('new')
print(test_set)
test_set.union('new')
print(test_set)

print(test_set.union(set('old')))
# о 178 строке     почему 'old' разбвает в рандомном порядке - идет итерация (это приведенная строка)  |   для того чтобы предотвратить итерацию нужно написать следующие 
other_set_1 = {'old'}
test_set.union(other_set_1)
print(test_set)
# на 180 и 182 строке мы объявляем {'old'}


# проверка вхождения элементов в set
# оператор in проверяет вхождение и работает во всех коллекциях
other_set_2 = {'old', 'new', 'real'}
print(other_set_2)
if 'real' in other_set_2:
    print(' \'real\' входит в set' )

# проверяем работу in под капотом через цикл for
other_set_3 = {'old', 'new', 'real'}
for i in other_set_3:
    if i == 'real':
        print(' \'real\' входит в set ')
    break

# ОПЕРАТОРЫ СРАВНЕНИЯ

# сравнение через оператор  == :
a = 20
b = 20.0
c = a == b # результат вывода True
print(c)
# (проверяет равенство двух объектов)


# сравнение через оператор is :
d = a is b # результат вывода False
print(d)
#(проверяет идентичность самих объектов) 

# /ОПЕРАТОРЫ СРАВНЕНИЯ







# NEW update в лист

# не работает 

test_set_5 = {'old', 'new'}
test_set_5.update([1, 2, 99])
print(test_set_5)

# /не работает 

test_set_5 = {'old', 'new'}
test_set_5.update(['string'])
print(test_set_5)

### set_other = {1, 5 (['string'])}






other_set_4 = {'old', 'new', 1, 2, 3, 4, 5}
test_set_6 = {'old', 'new'}

# выводит 
print('intersection: ', other_set_4.intersection(test_set_6))

# выводит 
print('union: ', other_set_4.union(test_set_6))

# выводит одну часть
print('difference: ', other_set_4.difference(test_set_6))

# выводит уникальные для п обоих элементов  то чего нету в первой и в второй перменных 
print('symmetric_difference: ', other_set_4.symmetric_difference(test_set_6))

# выводит 
print('issubset: ', other_set_4.issubset(test_set_6))

# выводит
print('issuperset: ', other_set_4.issuperset(test_set_6))

# выводит
print('difference_update: ', other_set_4.difference_update(test_set_6))

# выводит
print('isdisjoint: ', other_set_4.isdisjoint(test_set_6))




# ПРОВЕРЯЕМ ЗАНИМАЕМУЮ ПАМЯТЬ ЧЕРЕЗ getsizeof

from sys import getsizeof
number = 1_000_000

num_tuple = tuple(range(number))
num_list = list(range(number))
num_set = set(range(number))

num_tuple_size = getsizeof(num_tuple)
num_list_size = getsizeof(num_list)
num_set_size = getsizeof(num_set)

print("\n\nОбъем памяти tuple: ",num_tuple_size)
print("Объем памяти list: ",num_list_size)
print("Объем памяти set: ",num_set_size )

# вывод чисел от 0 до 10
number_1 = 10
set_num = set(range(number_1))
print(set_num)

# ГЕНЕРАТОР - работает в tuple, list, set
# вывод нечетных чисел через set
some_set = {i for i in range(1,11)} 
print(some_set)


# /о SET

# H/W нужно вывести результат через один print - входит или не входит чтобы не программа не писала два раза входит(x2) или не входит(x2)




# 23.02 / 2023
# SET и dict
# dict неупорядочные коллекциии произвольных объектов
# 
# 
# 


# НЕЛЬЗЯ присвоить к set " , " ---- { , }


# HOMEWORK
test_set = {1, 2, 3}
test_list = list(test_set)

test_list.append(5)
test_set.add(4)

print("\n\n", test_list)
print(test_set)

test_list[0] = 11
test_list.insert(3,4)


print("\n\n", test_list)
print(test_set)

# заменить 1 на 22 в set
print("\n\n", test_list)
print(test_set)



# найти минимальные и максимальные значения

exit_set = {97, 89, 4, 17, 99, 46, 50, 73, 81, 85}

max_set = 0
min_set = 100

for i in exit_set:
        print(i)

# /HOMEWORK



# NEW!   dict
# пустой dict сщздается с помощью my_dict = {}  
my_dict_1 = {}
print(type(my_dict_1))

my_dict_2 = {'my_key' : 'my_key'}
print(my_dict_2)

# не работает 
# my_dict_3 = dict(exit_set)



# dict это set : list

# coding
some_list_1 = [(1,2)]
print(some_list_1)
print(type(some_list_1))

some_list_2 = [(1,2),3,4]
print(some_list_2)
print(type(some_list_2))

some_list_3 = {'my_key_2' : None}
print(some_list_3)
print(type(some_list_3))

some_list_4 = dict(x=1, y=2)
print(some_list_4)
print(type(some_list_4))

some_list_5 = dict(x = (1,2), y = 2)
print(some_list_5)
print(type(some_list_5))


some_list_6 = dict(x=1)
print(some_list_6)
print(type(some_list_6))

some_list_7 = dict.fromkeys(exit_set)
print(some_list_7)
print(type(some_list_7))

some_list_7['один'] = 99
print(some_list_7)
print(type(some_list_7))

some_list_7['один'] = 99
print(some_list_7)
print(type(some_list_7))


some_list_7.get('один', 'Нет ключа')
print(some_list_7)
print(type(some_list_7))

some_list_7.pop
print(some_list_7)
print(type(some_list_7))






