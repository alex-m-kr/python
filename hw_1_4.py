# Задание 4. Найдите самую большую цифру в числе
number = int(input('Введите целое число, а я покажу его максимальную цифру '))
max = 0
while number > 0:
    last_number = number % 10
    # print('правое число', last_number)
    if last_number > max:
        max = last_number
    number //= 10
    # print('что остается', number)
print('Самая большая цифра', max)
