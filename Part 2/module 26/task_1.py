# Пользователь вводит число N. Напишите программу, которая генерирует последовательность
# из квадратов чисел от 1 до N (1 ** 2, 2 ** 2, 3 ** 2 и так далее).
# Реализацию напишите тремя способами: класс-итератор, функция-генератор и генераторное выражение.


class SquaresIterator:
    def __init__(self, N: int):
        self.n = N
        self.cur = 1


    def __iter__(self):
        return self


    def __next__(self):
        if self.cur <= self.n:
            res = self.cur ** 2
            self.cur += 1
            return res
        else:
            raise StopIteration



def generate_squares(n):
	current = 1
	while current <= n:
		yield current ** 2
		current += 1


n = int(input("Введите число N: "))

squares = (i ** 2 for i in range(1, n + 1))
for square in squares:
	print(square)