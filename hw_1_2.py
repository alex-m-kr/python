# Задание 2. Время
time_in_second = int(input('Введите целое количество секунд '))

# hour = time_in_second // 3600  # сразу не смог понять, как вывести секунды
# time_in_second %= 3600  # пришлось поэтапно убирать из времени часы и минуты
# minute = time_in_second // 60
# time_in_second %= 60
# second = time_in_second
# print(hour, minute, second)

hour = time_in_second // 3600
minute = time_in_second % 3600 // 60
second = time_in_second % 3600 % 60
print(f'Время в формате чч:мм:сс - {hour:02d}:{minute:02d}:{second:02d}')  # пришлось погуглить, чтобы вместо "1" выводилось "01"
