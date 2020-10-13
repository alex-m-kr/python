# Задание 5_2. Подсчет количества строк, количества слов в каждой строке
with open('hw_5_2.txt', encoding='utf-8') as f_obj:
    for i, line in enumerate(f_obj, 1):
        print(f'В строке {i} слов: {len(line.split())}')
    print('Всего строк:', i)
