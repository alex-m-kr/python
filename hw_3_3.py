# Задание 3_3. Сумма двух
def my_func(number_1, number_2, number_3):
    list_number = sorted([number_1, number_2, number_3])
    print(f'Наибольшие аргументы: {list_number[1]} и {list_number[2]}')
    return list_number[1] + list_number[2]

# print(my_func(83, 2, 45))
a, b, c = map(int, input('Введите три числа через пробел ').split())
print('Сумма наибольших аргументов:', my_func(a, b, c))
