class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f'Имя и фамилия сотрудника: {self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


def get_unswear(worker):  # почему-то захотелось так сделать)
    print(worker.get_full_name())
    print(f'Его зарплата {worker.get_total_income()} т.р.')


worker = Position('Ivan', 'Sidorov', 'manager', {
    'wage': 35000,
    'bonus': 10000
})
get_unswear(worker)

worker = Position('Ник', 'Перумов', 'писатель', {
    'wage': 150000,
    'bonus': 200000
})
get_unswear(worker)
