#DOOM
#December - Januar - Febuary -




num_1 = input("Действие: / , * " )
num_2 = int(input("Введите число: " ))
num_3 = int(input("введите число: " ))

if num_3 == 0 and (num_1 == "/" or num_1 == "*"):
    print("Null")
elif num_1 == "/":
    num_4 = num_2/num_3
    print("Результат деления: " + str(num_4))
elif num_1 == "*":
    num_4 == num_2*num_3
    print("Результат умножения: " + str(num_4))
else:
    print("Введен неверный символ")

i = 0
while True:
    print(i)
    i+=1
    if i == 5000:
        break

i = 0
while i < 50:
    if i == 0:
        print(i)
    i+=1

while True:
    moto_distance = int(input("Дистанция в км:" ))
    auto_distance = 
    moto_time = int(input("Время в пути в ч:" ))
    
    if moto_distance == 0 and moto_time == 0:
        print("Введены неверныеданные")
    elif moto_distance == 0 and moto_time != 0: 
        print("Движение не было произведено, дистанция равна 0км ")
    elif moto_time == 0 and moto_distance != 0:
        print("Время в пути 0 часов. Введите данные с учетом")
    elif moto_speed == auto_speed:
        print("у них одинаковая скорость")
    elif moto_speed > auto_speed:
        print("Скорость мотоциклиста больше")
    elif moto_speed < auto_speed:
        print("Скорость автомобилиста больше")
    what = str(input("Для завершения программы нажмите E или e :" ))
    if what == "E" or what == "e":
        print("Программа завершена!")
        break
for i in range(20+1, 0, -1):
    if i != 0 and i %2 == 0:
        print(i)
print("_____")

for i in range(0, 20+1):
    if i != 0 and i %2 == 0:
        print(i)

for i in range( , 20-1 ):
    print(i)
user_str = "string"
print(user_str[-1])


user_str = "string"
print(user_str[:3] + "A" + user_str[-2:])

str_val = "string"
print(len(str_val))
some_str = "one"
some_str = "who_know"
'one' = 'one' + "who_know"

while True:
        name = input("Наименование товара" )
        num = int(input("Количесво товара(ящиков)" ))
        what = int(input("На сколько разделить товар(вместимость в ящике)" ))
        box = num/what
        if box<what:
            box2 = num%what
            print("Получен товар" + name, "количество товара было распределено по" + box + "ящикам и один в дополнительный неполный ящик" + box2) 
            
        break
try:
    1//0
    int("One")
except ValueError :
    print("Error")
    print("Произошла ошибка")
except ZeroDivisionError:
    print("Произошло деление на ноль")
print("Продолжение работы")

try:
    raise ValueError:
except ValueError:
    print("Что-то пошло не так")
except Exception:
    print("Ошибка")

while True:
    num1 = int(input("Введите число:" ))
    num2 = int(input("Введите второе число:"))
    for i in range(num1,num2+1,):
        try:
            print("Текущее число - ",i)
            if i == 0:
                continue
                print(i)
            elif i % 2 == 0:
                raise ValueError
                print("Четное",i)
            else:
                print("Нечетное",i)
        except:
            print("Error")
    exit_val = input("Для выхода нажмите Е, для продолжения нажмите Enter")
    if exit_val == "E":
        print("Пока")
        break
try:
    print("Working")
    raise ZeroDivisionError
except ZeroDivisionError:
    print("Error")
finally:
    print("Это работает")
try:
    block1 = int(input("Введите число " ))
    block2 = int(input("Введите второе число " ))
    results = block1/block2
    raise ZeroDivisionError
    results = block1/block2
except ZeroDivisionError:
    print("Ошибка")
    print("Выполняется\nРезультат деления: ", results)
finally:
    print("Выполняется в любом случае")

text_val = 'Первый{0},второй{2}'
text_format = text_val.format(2,'ppp',1)
print(text_format)

results = '{}Первый{},второй{2{}'.format('hi','second',two=2,one=1) 
print(results)

one = 1
results = 'Первый{one},второй{1}'.format('hi','second',two=2,one=one) 
print(one)

text_val = 'Первый{one:x},второй{two}'
text_format = text_val.format(one=10,two=2)
print(text_format)

string = "{:{}{}{}}"
print(string.format("Питон","-","^",9))
Вывод 'Питон:_^9' прочитать про спецификатор

print("{:^10.2}".format('Python'))



while True:
    try:
        num = int(input("Введите число: \n" ))
        print("Hex {hex_data:>10x}".format(hex_data=num))
        print("Decimal {dec_data:>7d}".format(dec_data=num))
        print("Octal {oct_data:>9o}".format(oct_data=num))
        print("Binary {bin_data:>18b}".format(bin_data=num))
        exit_val = input("Для выхода нажмите E, для продолжения Enter - " )
        if exit_val == "E" or exit_val == "e":
            print("До встречи! " )
            break
    except ValueError:
        print("Неверная операция")


print(format(1,'f'))
print(format(1000.5368,'v>-15,.2f'))
print(format('format','.2'))


string = '{}'
print(string.format({2}).format(1,2,3))



string = "{{{{{{{{{}}}}}}}}}"
print(string.format(1,2,3))



print(format('{1+3}'))

print(f'{1+3}')


some_val = 'ой!'
print(f'{some_val}')

print(f'2+2={2+2:010d}')

заполнмтель = '-'
выравнивание = '^'
ширина = '9'
язык = 'Python'
print(f"{{язык}{заполнитель}{выравнивание}{ширина}}")



#Литералные колекции

group_378 = ['student_1', 'student_2', 'student_3']
print(type(group_378), group_378)
group_379 = ['student_4', 'student_5']
group_380 = group_378 + group_379
print(group_380)


print(id(group_378),(id(group_379)),(id(group_380)))
group_379 = group_379 + group_378
print(group_379)
print(id(group_379),group_379)
print(id(group_379.clear),group_379)


mark_student_1 = [5, 3, 4, 2]
mark_student_2 = [3, 2, 5]
mark_student_2.append(4)
print(mark_student_2)

print(len(mark_student_2))



#Работа над созданием "Электронного дневника"


name_student = input("Введите имя студента: " )
marks_student = input("Запишите оценки студента: " )
while True:
    list_marks = []
    update = list_marks.append(marks_student)
    
    #quanity_marks = len(marks_student)
    #average_score = summa // quanity
    
    #for i in list_marks:
        #summ = int(i)
        #print(summ)
    print(list_marks)
    
    # List в list

num_list = [1,2,3,4,5]
new_num_list = num_list.copy()
print(id(num_list),id(new_num_list))
num_list[2] = 7
print(num_list,new_num_list)
other_list = num_list
print(num_list,other_list)
print(id(num_list),id(other_list))
old_list[:] = num_list
other_list[2] = 6


name_num_list = [['one',1], ['two',2], ['three',3]]
#print((name_num_list[0],type(name_num_list)))
#print(type(name_num_list[-1][0]))
#name_num_list.remove(['two',2])
#name_num_list.pop()
#print(name_num_list)
print(name_num_list.index(['two',2]))


new_list = [1,2,5,1,3,7,9,5,1]
what = new_list.index{
print(what)



new_list = [1,2,5,1,3,7,9,5,1]
print(new_list.index(1,2))



#name_num_list = [['one',1], ['two',2], ['three',3]]
#name_num_list.pop(0)
#print(name_num_list)


#new_list = [1,2,5,1,3,7,9,5,1]
#print(id(new_list))
#new_list = []
#print(id(new_list))
#new_list.clear
#print(id(new_list))



new_tuple = tuple()
print(new_tuple, type(new_tuple))
new_tuple = ()
print(new_tuple, type(new_tuple))
other_tuple = ()
print(other_tuple, type(other_tuple))
other_tuple = (1,)
print(other_tuple, type(other_tuple))
#other_tuple = other_tuple + 1
#print(other_tuple)


new_list = [1,2,5,1,3,7,9,5,1]
count = 0 
for i in num_list
    if i == 1:
        print('index = ', count)
    count += 1
