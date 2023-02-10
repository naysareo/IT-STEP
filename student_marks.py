# Вывод следующих данных:
# 1) Имя студента
# 2) Ввод пользователем отметок студента
# 3) Вывод даннных студента: все внесенные отметки, количество внесенных отметок, сумма внесенных отметок, средний балл студента


while True:
    
    list_marks = []
    summa = 0
    name_student = input("Введите имя студента: " )
    
    while True:
        update_marks = input('Продолжайте вводить оценки для выбранного ученика, после выставления нажмите \"R\" для перехода к результатам: \n')
        if update_marks == "R":
            break
        for i in update_marks:
            i = int(i)
            summa += i
            list_marks.append(update_marks)
            quanity = len(list_marks)
    
    print("\nДанные студента", name_student, ":\n" )
    print("\nВсе внесенные отметки: \n", list_marks)
    print("\nКоличесво всех выставленных отметок: \n", quanity)
    print("\nСумма всех отметок для студента: \n", summa)
    print("\nСредний балл студента: ",summa/quanity, "\n\n" )
