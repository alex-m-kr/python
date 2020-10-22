# Задание 7_1. Матрицы
class Matrix:
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        string = ''
        for line in self.lst:
            for el in line:
                string += str(el) + '\t'
            string += '\n'
        return string

    def __add__(self, other):
        new_lst = []
        new_line = []
        # предполагается, что длина каждого из вложенных списков одинакова
        if len(self.lst) == len(other.lst) and len(self.lst[0]) == len(other.lst[0]):
            for i in range(len(self.lst)):
                for j in range(len(self.lst[0])):
                    new_line.append(self.lst[i][j] + other.lst[i][j])
                new_lst.append(new_line)
                new_line = []
            # print(new_lst)
            # print('Равны')
            return Matrix(new_lst)  # суммарная новая матрица будет выведена методом __str__()
        else:
            return 'Матрицы имеют разные размеры'


a1 = Matrix([[12, 2], [33, 4], [5, 6]])
print(a1)
a2 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
print(a2)
a3 = Matrix([[10, -8], [3, 4], [5, 6]])
print(a3)
a4 = Matrix([[3, 5, 8, 31], [8, 3, 7, -1]])
print(a4)
print(a1 + a2)
print(a1 + a3)
print(a2 + a4)
