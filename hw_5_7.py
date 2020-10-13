# Задание 5_7. Фирмы
import json
dict_firm = {}
dict_profit = {}
sum_profit = 0
cnt_profit = 0

print('Вот наши фирмы:')
with open('hw_5_7.txt', encoding='utf-8') as f_obj:
    for line in f_obj:
        print(line.strip())
        name = line.split()[0]
        revenue = float(line.split()[2])
        cost = float(line.split()[3])
        profit = revenue - cost
        if profit >= 0:
            cnt_profit += 1
            sum_profit += profit
        dict_firm[name] = profit
average_profit = sum_profit / cnt_profit  # Условие о не включении убыточных компаний, я понял так, что и делить
# прибыль на них не нужно
dict_profit['average_profit'] = average_profit
result_list = [dict_firm, dict_profit]
print(result_list)

with open('my_file.json', 'w', encoding='utf-8') as write_f:
    json.dump(result_list, write_f, ensure_ascii=False)
'''
Нашел, что по умолчанию ensure_ascii = True и все не-ASCII символы в выводе
экранируются, т.е. кириллица имеет странный вид.
Но при десереализации в обоих случаях работает одинаково. 
'''
