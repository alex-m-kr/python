# Задание 5_4. Английские числительные должны заменяться на русские
with open('hw_5_4.txt', encoding='utf-8') as inf, open('txt_5_4.txt', 'w+', encoding='utf-8') as ouf:
    for line in inf:
        if 'One' in line:
            new_line = line.replace('One', 'Один')
        elif 'Two' in line:
            new_line = line.replace('Two', 'Два')
        elif 'Three' in line:
            new_line = line.replace('Three', 'Три')
        elif 'Four' in line:
            new_line = line.replace('Four', 'Четыре')
        ouf.write(new_line)
    print('Вот содержимое старого файла:')
    inf.seek(0)
    print(inf.read())
    print('Вот содержимое нового файла:')
    ouf.seek(0)
    print(ouf.read())
