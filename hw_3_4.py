# Задание 3_4. Отрицательная степень

# вариант 1
# def my_func(x, y):
#     return x ** y

# вариант 2
def my_func(x, y):
    result = 1
    for i in range(abs(y)):
        result /= x
    return result

x = float(input('Введите число x '))
y = int(input('Введите число y '))
print(my_func(x, y))
