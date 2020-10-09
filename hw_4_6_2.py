# Задание 4_6_2. Итератор, повторяющий элементы
from itertools import cycle
stop = int(input('Количество повторений: '))
lst = ['черная', 'белая', 'серая', '----->']
i = 0
for el in cycle(lst):
    print(el)
    i += 1
    if i == stop:
        break
