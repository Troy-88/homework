class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля{self.name}: {self.speed}')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость автомобиля {self.name} превышена на {self.speed - 60} км/ч.')
        else:
            print(f'Текущая скорость автомобиля {self.name}: {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость автомобиля {self.name} превышена на {self.speed - 40} км/ч.')
        else:
            print(f'Текущая скорость автомобиля {self.name}: {self.speed}')


class PoliceCar(Car):
    pass


def get_info(car):
    print(f'Машина {car.name}. Цвет: {car.color}. Относится к полиции: {car.is_police}')
    car.go()
    car.turn('Налево')
    car.turn('Направо')
    car.show_speed()
    car.stop()
    print()  # сделал для чтобы между вызовами функции была пустая строка


car_1 = WorkCar(70, 'White', 'Газель', False)
get_info(car_1)

car_2 = PoliceCar(150, 'Blue', 'Калина', True)
get_info(car_2)

car_3 = SportCar(200, 'Yellow', 'Субару', False)
get_info(car_3)

car_4 = TownCar(70, 'Black', 'Мазда', False)
get_info(car_4)
