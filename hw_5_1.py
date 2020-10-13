# Задание 5_1. Запись в файл построчно
with open('txt_5_1.txt', 'w', encoding='utf-8') as f_obj:
    while True:
        str = input('Введите строку для записи или пустую для завершения: ')
        if not str:
            break
        f_obj.write(str + '\n')
