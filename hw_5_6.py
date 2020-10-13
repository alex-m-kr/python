# Задание 5_6. Учебные предметы
dict = {}
print('Вот наши учебные предметы:')
with open('hw_5_6.txt', encoding='utf-8') as f_obj:
    for line in f_obj:
        print(line.strip())
        subject = line.strip().split(':')[0]
        temp_lst = [i for i in line.strip() if i.isdigit() or i == ' ']  # в списке остаются только цифры и пробелы
        temp_str = ''.join(temp_lst).strip()  # собирается строка, отсекаются пробелы в начале и конце
        # print(temp_lst)
        # print(temp_str)
        temp_lst = temp_str.split() # теперь в списке только числа в стринговом представлении
        # print(temp_lst)
        sum_hour = sum([int(i) for i in temp_lst])
        dict[subject] = sum_hour
print()
print(dict)
