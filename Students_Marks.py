import random
students = ['Гавейн', 'Ланселот', 'Кей', 'Галахад', 'Персиваль', 'Ламорак', 'Борс', 'Уриенс', 'Ивейн', 'Саграмор', 'Бедивер']
students.sort()
classes = ['Математика', 'Грамматика', 'Информатика', 'Риторика', 'Логика']
students_marks = {}
for student in students:
    students_marks[student] = {}
    for class_ in classes:
        marks = [random.randint(1,5) for i in range(3)]
        students_marks[student][class_] = marks
for student in students:
    print(f'''{student}
    {students_marks[student]}''')
print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Вывести средний балл по каждому предмету по определенному ученику
        5. Вывести все оценки для определенного ученика
        6. Удалить данные: ученика, предмет или оценку
        7. Редактировать данные: ученика, предмет или оценку
        8. Добавить новые данные: ученика, предмет или оценку
        9. Выход из программы
        ''')
while True:
    command = int(input('Введите № команды от 1 до 9: '))
    if command == 1:
        print('1. Добавить ученику оценку по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите название предмета: ')
        mark = int(input('Введите оценку: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys() and 1 <= mark <= 5:
            students_marks[student][class_].append(mark)
            print(f'Сэр {student} получил оценку {mark} по предмету {class_}')
            print(f' Сэр {student} имеет следующие оценки {students_marks[student]}')
        else:
            print('ОШИБКА: неверное имя ученика, название предмета или оценка')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        for student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum//marks_count}')
            print()
    elif command == 3:
        print('Вывести все оценки по всем ученикам')
        for student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('Вывести средний балл по каждому предмету по определенному ученику')
        student = input('Введите имя ученика: ')
        print()
        class_ = input('Введите название предмета: ')
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            marks_avg = sum(students_marks[student][class_])//len(students_marks[student][class_])
            print(f'Сэр {student} имеет среднюю оценка по предмету {class_} равную {marks_avg}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 5:
        print('Вывести все оценки для определенного ученика')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            print(f' Сэр {student} имеет следующие оценки {students_marks[student]}')
        else:
            print('ОШИБКА: неверное имя ученика')
    elif command == 6:
        print('''Выберите команду:
        11. Удалить ученика
        12. Удалить предмет
        13. Удалить оценку
        14. Вернуться в предыдущее меню''')
        while True:
            try:
                sub_command = int(input('Введите № команды (от 11 до 14): '))
            except ValueError:
                print('Введена некорректная команда')
                continue
            if sub_command == 11:
                print('Удалить учетную запись ученика')
                student_to_delete = input('Введите имя ученика: ')
                index = students.index(student_to_delete)
                if student_to_delete in students:
                    del students[index]
                    print(f'Сэр {student_to_delete} был удален')
                    print(f' Оставшиеся ученики: {students}')
                else:
                    print('ОШИБКА: неверное имя ученика')
                break
            elif sub_command == 12:
                (print('Удалить предмет'))
                class_to_delete = input('Введите название предмета: ')
                index = classes.index(class_to_delete)
                if class_to_delete in classes:
                    del classes[index]
                    print(f'Предмет {class_to_delete} был удален')
                    print(f' Оставшиеся предметы: {classes}')
                else:
                    print('Ошибка: предмет отсутствует в базе')
                break
            elif sub_command == 13:
                print('Удалить оценку')
                student_to_change = input('Введите имя ученика: ')
                if student_to_change in students_marks:
                    class_to_change = input('Введите название предмета: ')
                    if class_to_change in students_marks[student_to_change]:
                        marks_list = students_marks[student_to_change][class_to_change]
                        if marks_list:
                            print(f'Сэр {student_to_change} по предмету {class_to_change} имеет оценку {marks_list}')
                            try:
                                mark_to_delete = int(input('Введите оценку для удаления: '))
                                if mark_to_delete in marks_list:
                                    index = marks_list.index(mark_to_delete)
                                    del marks_list[index]
                                    print(f'Была удалена оценка {mark_to_delete} по предмету {class_to_change} для сэра {student_to_change}')
                                    print(f'Сэр {student_to_change} по предмету {class_to_change} сейчас имеет оценки {marks_list}')
                                else:
                                    print('ОШИБКА: такой оценки нет')
                            except ValueError:
                                print('Неверно введена оценка')
                        else:
                            print('Сэр {student_to_change} не имеет оценок по предмету {class_to_change}')
                    else:
                        print('Ошибка: предмет отсутствует в базе')
                else:
                    print('ОШИБКА: неверное имя ученика')
                break
            elif sub_command == 14:
                print('Возврат в предыдущее меню')
                break
    elif command == 7:
        print('''Выберите команду:
        21. Изменить имя ученика
        22. Изменить название предмета
        23. Заменить оценку
        24. Вернуться в предыдущее меню''')
        while True:
            try:
                sub_command_1 = int(input('Введите № команды (от 21 до 24): '))
            except ValueError:
                print('Введена некорректная команда')
                continue
            if sub_command_1 == 21:
                print('Изменить имя ученика')
                student_to_replace = input('Введите имя ученика для замены: ')
                print()
                new_student = input('Введите новое имя ученика: ')
                index = students.index(student_to_replace)
                if student_to_replace in students:
                    students[index] = new_student
                    print(f'Сэр {student_to_replace} был заменен на сэра {new_student}')
                    print(f' Список учеников: {students}')
                else:
                    print('ОШИБКА: неверное имя ученика')
                break
            elif sub_command_1 == 22:
                (print('Изменить название предмета'))
                class_to_replace = input('Введите название предмета для замены: ')
                print()
                new_class = input('Введите новое название предмета: ')
                index = classes.index(class_to_replace)
                if class_to_replace in classes:
                    classes[index] = new_class
                    print(f'Предмет {class_to_replace} был заменен предметом {new_class}')
                    print(f' Список предметов: {classes}')
                else:
                    print('Ошибка: предмет отсутствует в базе')
                break
            elif sub_command_1 == 23:
                print('Заменить оценку')
                student_to_change = input('Введите имя ученика: ')
                if student_to_change in students_marks:
                    class_to_change = input('Введите название предмета: ')
                    if class_to_change in students_marks[student_to_change]:
                        marks_list = students_marks[student_to_change][class_to_change]
                        if marks_list:
                            print(f'Сэр {student_to_change} по предмету {class_to_change} имеет оценку {marks_list}')
                            try:
                                mark_to_replace = int(input('Введите оценку для замены: '))
                                print()
                                new_mark = int(input('Введите новую оценку: '))
                                if mark_to_replace in marks_list:
                                    index = marks_list.index(mark_to_replace)
                                    marks_list[index] = new_mark
                                    print(f'Была заменена оценка {mark_to_replace} по предмету {class_to_change} для сэра {student_to_change} на оценку {new_mark}')
                                    print(f'Сэр {student_to_change} по предмету {class_to_change} сейчас имеет оценки {marks_list}')
                                else:
                                    print('ОШИБКА: такой оценки нет')
                            except ValueError:
                                print('Неверно введена оценка')
                        else:
                            print('Сэр {student_to_change} не имеет оценок по предмету {class_to_change}')
                    else:
                        print('Ошибка: предмет отсутствует в базе')
                else:
                    print('ОШИБКА: неверное имя ученика')
                break
            elif sub_command_1 == 24:
                print('Возврат в предыдущее меню')
                break
    elif command == 8:
        print('''Выберите команду:
        31. Добавить имя ученика
        32. Добавить название предмета
        33. Добавить оценку
        34. Вернуться в предыдущее меню''')
        while True:
            try:
                sub_command_2 = int(input('Введите № команды (от 31 до 34): '))
            except ValueError:
                print('Введена некорректная команда')
                continue
            if sub_command_2 == 31:
                print('Добавить имя ученика')
                student_to_add = input('Введите имя ученика для добавления: ')
                if student_to_add not in students:
                    students.append(student_to_add)
                    print(f'К ученикам добавился сэр {student_to_add}')
                    print(f' Список учеников: {students}')
                else:
                    print('ОШИБКА: имя ученика уже есть в списке')
                break
            elif sub_command_2 == 32:
                (print('Добавить название предмета'))
                class_to_add = input('Введите новое название предмета: ')
                if class_to_add not in classes:
                    classes.append(class_to_add)
                    print(f'В списке появился новый предмет {class_to_add}')
                    print(f' Список предметов: {classes}')
                else:
                    print('Ошибка: предмет уже есть в базе')
                break
            elif sub_command_2 == 33:
                print('Добавить оценку по предмету')
                student_to_change = input('Введите имя ученика: ')
                if student_to_change in students_marks:
                    class_to_change = input('Введите название предмета: ')
                    if class_to_change in students_marks[student_to_change]:
                        marks_list = students_marks[student_to_change][class_to_change]
                        if marks_list:
                            print(f'Сэр {student_to_change} по предмету {class_to_change} имеет оценку {marks_list}')
                            try:
                                mark_to_add = int(input('Введите новую оценку: '))
                                if 0 <= mark_to_add <= 5:
                                    marks_list.append(mark_to_add)
                                    print(f'Была добавлена оценка {mark_to_add} по предмету {class_to_change} для сэра {student_to_change}')
                                    print(f'Сэр {student_to_change} по предмету {class_to_change} сейчас имеет оценки {marks_list}')
                                else:
                                    print('Неверно введена оценка')
                            except ValueError:
                                print('Неверно введена оценка')
                        else:
                            print('Сэр {student_to_change} не имеет оценок по предмету {class_to_change}')
                    else:
                        print('Ошибка: предмет отсутствует в базе')
                else:
                    print('ОШИБКА: неверное имя ученика')
                break
            elif sub_command_2 == 34:
                print('Возврат в предыдущее меню')
                break
    elif command == 9:
        break