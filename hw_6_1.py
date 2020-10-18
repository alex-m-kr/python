# Задание 6_1. Светофор
from itertools import cycle
from time import sleep


class TrafficLight:
    _color = ['красный', 'жёлтый', 'зелёный']

    def running(self):
        iter = cycle(TrafficLight._color)
        while True:
            print(next(iter))  # красный
            sleep(7)
            print(next(iter))  # жёлтый
            sleep(2)
            print(next(iter))  # зелёный
            sleep(3)


tl1 = TrafficLight()
tl1.running()
