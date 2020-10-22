# Задание 7_3. Клетки
class Cell:
    def __init__(self, size):
        self.size = size

    def make_order(self, length=5):
        print(f'Клетка размером: {self.size}. Вывод ячеек по рядам с шириной: {length}')
        print(('*' * length + '\n') * (self.size // length) + '*' * (self.size % length))

    def __add__(self, other):
        print(f'Сложение клеток с размерами {self.size} и {other.size}')
        self.size += other.size
        self.make_order()

    def __mul__(self, other):
        print(f'Умножение клеток с размерами {self.size} и {other.size}')
        self.size *= other.size
        self.make_order()

    def __truediv__(self, other):
        print(f'Деление клеток с размерами {self.size} и {other.size}')
        self.size //= other.size
        self.make_order()

    def __sub__(self, other):
        print(f'Вычитание клеток с размерами {self.size} и {other.size}')
        if self.size - other.size > 0:
            self.size -= other.size
            self.make_order()
        else:
            print('Операция невозможна, разность меньше или равна нулю')


c1 = Cell(26)
c1.make_order(23)

c2 = Cell(20)
c2.make_order(18)

c3 = Cell(3)

c1 + c2
c2 - c1
c1 - c2
c1 * c3
c2 / c3
c2.make_order(3)
