# Задание 6_4. Машина
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} едет')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула ' + direction)

    def show_speed(self):
        print(f'Скорость машины {self.name} {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        print(f'Скорость машины {self.speed} км/ч')
        if self.speed > 60:
            print('Превышение скорости')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Скорость машины {self.speed} км/ч')
        if self.speed > 40:
            print('Превышение скорости')


class PoliceCar(Car):
    pass


car = Car(40, 'белый', 'Жигули', False)
car.go()
car.stop()
car.turn('Влево')
car.show_speed()
print('цвет ' + car.color)
print()
t_car = TownCar(70, 'желтый', 'Man', False)
t_car.go()
t_car.stop()
t_car.turn('вправо')
t_car.show_speed()
print('цвет ' + t_car.color)
print()
w_car = WorkCar(41, 'желтый', 'hitachi', False)
w_car.go()
w_car.stop()
w_car.turn('вправо')
w_car.show_speed()
print('цвет ' + w_car.color)
print()
p_car = PoliceCar(100, 'синий', 'Lada', True)
p_car.go()
p_car.stop()
p_car.turn('вправо')
p_car.show_speed()
print(f'Скорость машины {p_car.speed}, название машины {p_car.name}, цвет {p_car.color}, полиция: {p_car.is_police}')
