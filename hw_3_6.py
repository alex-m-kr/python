# Задание 3_6. Прописные буквы
int_func = lambda my_str: my_str.capitalize()

text = map(int_func, input('Строка слов через пробелы: ').split())
print(*list(text))
