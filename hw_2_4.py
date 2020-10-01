# Задание 4. Слова с новой строки
user_list = input('Введите строку из нескольких слов ').split()
for ind, el in enumerate(user_list, 1):
    print(ind, el[:10])
