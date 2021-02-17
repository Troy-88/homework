class Cell:
    def __init__(self, num_of_cell):
        self.num_of_cell = num_of_cell

    def __add__(self, other):
        return self.num_of_cell + other.num_of_cell

    def __sub__(self, other):
        sub = self.num_of_cell - other.num_of_cell
        if sub > 0:
            return sub
        else:
            return f'Нельзя вычесть из меньшей клетки большую'

    def __mul__(self, other):
        return self.num_of_cell * other.num_of_cell

    def __truediv__(self, other):
        return round(self.num_of_cell / other.num_of_cell)

    def make_order(self, n):
        res = ('*' * n + '\n') * (self.num_of_cell // n) + '*' * (self.num_of_cell % n)
        return res


cell_1 = Cell(5)
cell_2 = Cell(20)
cell_3 = Cell(4)

cell_add_1 = cell_1 + cell_2
print(cell_add_1)

cell_sub_1 = cell_1 - cell_2
print(cell_sub_1)

cell_sub_2 = cell_1 - cell_3
print(cell_sub_2)

cell_mul_1 = cell_1 * cell_2
print(cell_mul_1)

cell_truediv_1 = cell_1 / cell_3
print(cell_truediv_1)

print(cell_2.make_order(9))
