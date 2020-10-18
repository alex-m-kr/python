# Задание 6_5. Stationery
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'{self.title}: Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title} начинает писать')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} начинает чертить')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title} начинает выделять')


st = Stationery('Канцелярская принадлежность')
st.draw()
pen = Pen('Ручка')
pen.draw()
pencil = Pencil('Карандаш')
pencil.draw()
handle1 = Handle('Маркер №1')
handle1.draw()
