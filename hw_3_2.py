# Задание 3_2. Данные пользователя
def user_data(name, surname, year, city, email, phone):
    result = f'{name=}, {surname=}, {year=}, {city=}, {email=}, {phone=}'
    return  result

print(user_data(phone=999123456, city='Moscow', name='Иван', year=1980, surname='Иванов', email='iv@ya.ru'))
