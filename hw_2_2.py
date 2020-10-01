# Задание 2. Обмен соседних элементов списка
my_list = []
answer = 'y'
while answer == 'y':
    my_list.append(input('Введите очередной элемент списка '))
    answer = input('Вы хотите ввести ещё элемент? (y/n) ')
print('Исходный список', my_list)
i = 0
while i <= len(my_list) - 2:
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    i += 2
print('Изменённый список', my_list)
