class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        new_str = ''
        for i, el_i in enumerate(self.matrix):
            for j, el_j in enumerate(self.matrix[i]):
                new_str += str(el_j) + ' '
            new_str = new_str[:-1]
            new_str += '\n'
        return new_str[:-1]

    def __add__(self, other):
        new_matrix = []
        for i in range(len(self.matrix)):
            new_matrix.append([])
            for j in range(len(self.matrix[i])):
                new_matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
        return Matrix(new_matrix)


matr_1 = Matrix([[1, 5, 5, 4], [4, 3, 6, 7], [1, -2, -4, 3]])
print(matr_1, end='\n\n')

matr_2 = Matrix([[3, 4, 1, 2], [-2, -1, 0, 4], [5, 9, 6, -1]])
print(matr_2, end='\n\n')

matr_12_sum = matr_1 + matr_2
print(matr_12_sum, end='\n\n')
