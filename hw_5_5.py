# Задание 5_5. Сумма чисел в файле
with open('txt_5_5.txt', 'w+', encoding='utf-8') as f_obj:
    str = input('Введите набор целых чисел через пробел: ')
    f_obj.write(str)
    f_obj.seek(0)
    num_in_file = f_obj.readline().split()
    # print(num_in_file)
    result = sum([int(i) for i in num_in_file])
    print('Сумма чисел в файле:', result)
