# Задание 3_5. Строка чисел
def sum_list(data):
    list_int = list(map(int, data))
    # print(list_int)
    return sum(list_int)

sum_result = 0
while True:
    my_list = input('Строка чисел через проблелы или "q" (можно после чисел) для завершения: ').split()
    if my_list[0] == 'q':
        print('Завершение программы')
        break
    elif 'q' in my_list:
        sum_result += sum_list(my_list[:my_list.index('q')])
        print(f'Текущая сумма чисел равна: {sum_result}')
        print('Завершение программы')
        break
    sum_result += sum_list(my_list)
    print(f'Текущая сумма чисел равна: {sum_result}')
