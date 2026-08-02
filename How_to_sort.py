def sortimg_anything(object):
    answers = []
    answers_1= []
    answers_2= []
    answers_3= []
    for item in object:
        if type(item) == int and item % 2 == 0:
            answers.append(item)
            answers.sort(reverse=True)
        elif type(item) == str:
            answers_1.append(item)
            answers_1.sort()
        else:
            type(item) == int and item % 2 == 1
            answers_2.append(item)
        if type(item) == int and item >= 5:
            answers_3.append(item * 2)
            answers_3.sort()
    return answers, answers_1, answers_2, answers_3
object1 = [1, 'Арбуз', 3, 'Баян', 5, 'Кулебяка', 6, 7, 'Вол', 9, 8, 16, 64, 32]
result1 = sortimg_anything(object1)
print(result1)