# Задание 7_2. Одежда
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size_height, name=None):
        self.size_height = size_height
        self.name = name

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):
    @property
    def calculate(self):
        self.square = self.size_height / 6.5 + 0.5
        return f'расход ткани: {self.square}'


class Suit(Clothes):
    @property
    def calculate(self):
        self.square = self.size_height * 2 + 0.3
        return f'расход ткани: {self.square}'


coat1 = Coat(6.5, 'пальто с названием')
print(coat1.name)
print(coat1.calculate)

suit1 = Suit(4)
print(suit1.calculate)
