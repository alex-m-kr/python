# Задание 6_2. Дорога
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculation(self):
        mass = self._width * self._length * 25 * 5
        return f'масса асфальта {int(mass / 1000)} т'


road1 = Road(5000, 20)
print(road1.calculation())
