number = input('Введите число: ')
operator = input('Введите оператор: (+ или - или * или / или **: ')
number_2 = input ('Введите второе число: ')

try:
    number = float(number)
    number_2 = float(number_2)
    if operator == '+':
        print(number + number_2)
    elif operator == '-':
        print(number - number_2)
    elif operator == '*':
        print(number * number_2)
    elif operator == '/':
        print(number / number_2)
    elif operator == '**':
        print(number ** number_2)
    else:
        print('Что у тебя вместо оператора?')

except ValueError:
    print('Это не число')