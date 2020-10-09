# Задание 4_6_1. Итератор, генерирующий целые числа
from itertools import count
start, stop = int(input('Начало: ')), int(input('Конец: '))
for el in count(start):
    print(el)
    if el == stop:
        break
