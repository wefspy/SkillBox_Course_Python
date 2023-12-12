# Вы стажируетесь в лаборатории искусственного интеллекта, в ней вам поручили разработать класс Matrix
# для обработки и анализа данных. Ваш класс должен предоставлять функциональность для выполнения основных
# операций с матрицами, таких как сложение, вычитание, умножение и транспонирование.
# Это будет полезно для обработки и структурирования больших объёмов данных, которые используются в обучении нейронных сетей.
#
# Задача
# Создайте класс Matrix для работы с матрицами.
# Реализуйте методы:
#     сложения,
#     вычитания,
#     умножения,
#     транспонирования матрицы.
# Создайте несколько экземпляров класса Matrix и протестируйте реализованные операции.

class Matrix:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for col in range(cols)] for row in range(rows)]

    def add(self, matrix):
        if self.rows != matrix.rows or self.cols != matrix.cols:
            return 'Матрицы разного размера'
        
        result = Matrix(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                result.data[row][col] = self.data[row][col] + matrix.data[row][col]
        return result

    def subtract(self, matrix):
        if self.rows != matrix.rows or self.cols != matrix.cols:
            return 'Матрицы разного размера'

        result = Matrix(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                result.data[row][col] = self.data[row][col] - matrix.data[row][col]
        return result

    def multiply(self, matrix):
        if self.cols != matrix.rows:
            return 'Невозможно умножить матрицы'
            
        result = Matrix(self.rows, matrix.cols)
        for row_1 in range(self.rows):
            for col_2 in range(matrix.cols):
                for col_1 in range(self.cols):
                    result.data[row_1][col_2] += self.data[row_1][col_1] * matrix.data[col_1][col_2]
        return result

    def transpose(self):
        result = Matrix(self.cols, self.rows)
        for row in range(self.rows):
            for col in range(self.cols):
                result.data[col][row] = self.data[row][col]
        return result

    def __str__(self):
        return '\n'.join(['\t'.join([str(col) for col in row]) for row in self.data])

m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
print(m1.add(m2))

print("Вычитание матриц:")
print(m1.subtract(m2))

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print("Умножение матриц:")
print(m1.multiply(m3))

print("Транспонирование матрицы 1:")
print(m1.transpose())