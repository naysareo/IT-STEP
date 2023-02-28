# 27.02.2023
# dict 
# # CRUD U(update) = setdefault - update  R(read) = get 







# словарь словаря # без 0 в начале не будет работать
test_dict = {0:{1:'one'},2:'two'}
print(test_dict)

# ПЕРВЫЙ СПОСОБ
dict_test = {}
for i in range(13):
    dict_test[i] = i+5
    print(dict_test)

# ВТОРОЙ СПОСОБ
dict_test_2 = {}
for i in range(10):
    dict_test_2[i] = i*i
    print(dict_test_2)


generator = {degree:degree ** 2 for degree in range(10)}
print(generator)

# НУЖНО СДЕЛАТЬ С None через .fromkeys






# СОБЕСЕДОВАНИЯ setdefault отличие от get 
# СОБЕСЕДОВАНИЯ итератор и генератор отличия      


#generator_none = {a:  None for a in range(10)}
#generator_2 = {i for i in range(10)}
#i = str(i)
#from_keys_dict = dict.fromkeys([None])
#print('\n\n\n', from_keys_dict)



print('\n\n\n')
generator_2 = {degree:degree ** 2 for degree in range(10)}
print(generator_2.keys())
print(generator_2.values())
print(generator_2.items())
print('\n\n\n')

for key, value in generator_2.items():
    print(key,value)



new_dict = {1:1,2:4,3:9,1:99}
x = new_dict.get(1,None)
print(x)
print(new_dict)

new_dict = {1:1,2:4,3:9,1:99}
del new_dict[1]
print(new_dict)


# папка - пустой словарь при удалении папка удаляется но Id остается в памяти
# с помощью get можно возвращать значения
# get использует много русурсов
# под капоом get лежит try except


# setdefault = под капотом = test_dict[1] = None
# None при запуске Python сразу же создается      один единственный None
# get
# setdefault добавляет значение которых нету
test_dict.setdefault(1,777)
print(test_dict)
empty_check = test_dict.get(1)
if test_dict is None:
    print('Ok')


# pop - удаляет и возвращает значения 
# pop в словаре (dict) 
# del 

new_dict_2 = {1:1,2:4,3:9,1:99}
print(new_dict_2)
new_dict_2.pop(1)
print(new_dict_2)

