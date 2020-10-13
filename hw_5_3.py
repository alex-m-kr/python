# Задание 5_3. Оклад менее 20 тыс.
dict_poor_employees = {}
sum_income = 0
print('Вот наши сотрудники и их оклады:')
with open('hw_5_3.txt', encoding='utf-8') as f_obj:
    for i, line in enumerate(f_obj, 1):
        print(line.strip())
        surname, income = line.split()[0], float(line.split()[1])
        sum_income += income
        if income < 20000:
            dict_poor_employees[surname] = income
    print()
    print('Сотрудники с доходом ниже 20 тыс.: ', end='')
    print(*[key for key in dict_poor_employees])
    print(f'Всего сотрудников {i}, общая сумма дохода {sum_income}, средняя величина дохода {round(sum_income / i, 2)}')
