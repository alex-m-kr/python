# Задание 5. Рейтинг
my_list = [7, 5, 3, 3, 2]
answer = 'y'
while answer == 'y':
    number = int(input('Введите очередное натуральное число '))
    i = 0
    for el in my_list:
        if number > el:
            my_list.insert(i, number)
            break
        i += 1
        if i == len(my_list):
            my_list.append(number)
            break
    print('Результат:', *my_list)
    answer = input('Вы хотите ввести ещё элемент? (y/n) ')

