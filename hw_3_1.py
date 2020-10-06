# Задание 3_1. Деление
def division(first_number, second_number):
    try:
        return first_number / second_number
    except ZeroDivisionError:
        return 'На ноль делить нельзя'

answer = 'y'
while answer.lower() == 'y':
    number_1 = float(input('Введите первое число '))
    number_2 = float(input('Введите второе число '))
    print(division(number_1, number_2))
    answer = input('Продолжим, (y/n)? ')
