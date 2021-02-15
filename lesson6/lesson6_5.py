class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ручки {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандаша {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркера {self.title}')


stationery_1 = Pen('Харри')
stationery_1.draw()

stationery_2 = Pencil('Гарри')
stationery_2.draw()

stationery_3 = Handle('Марри')
stationery_3.draw()
