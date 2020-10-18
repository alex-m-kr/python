# Задание 6_3. Работник
class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


worker1 = Position('Сидор', 'Сидоров', 'chief', {'wage': 100, 'bonus': 50})
worker2 = Position('Иван', 'Иванов', 'cleaner', {'wage': 12, 'bonus': 3})
print(worker1.get_full_name())
print(worker1.get_total_income())
print(worker2.get_full_name())
print(worker2.get_total_income())
# print(worker1._income)
# print(worker2._income)
