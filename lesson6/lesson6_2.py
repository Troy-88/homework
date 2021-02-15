class Road:
    def __init__(self, width, length):
        self._width = width
        self._length = length

    def mass_asphalt(self, mass, thickness):
        return mass * thickness * self._length * self._width


mass = 25  # в киллограммах
thickness = 5  # в сантиметрах
length, width = input('Введите значение длины и ширины дороги через пробел: ').split()

road_alekseeva = Road(int(width), int(length))
print(f'Для строительства дороги потребуется {road_alekseeva.mass_asphalt(mass, thickness)} кг асфальта.')
