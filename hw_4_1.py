# Задание 4_1. Зарплата через скрипт с параметрами
from sys import argv
# print(argv)
# print(argv[1:4])
try:
    production, salary, bonus = argv[1:4]
    income = float(production) * float(salary) + float(bonus)
    print(f'Выработка в часах: {production}, ставка: {salary}, премия: {bonus}')
    print(f'Заработная плата составила: {round(income, 2)}')
except ValueError:
    print('Запустите скрипт с тремя численными параметрами: выработка, ставка, премия')
