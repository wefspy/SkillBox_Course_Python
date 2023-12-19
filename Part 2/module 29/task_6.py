# Создайте декоратор, который логирует аргументы, результаты и время выполнения функции.
#
# Реализуйте декоратор как класс и примените его к функции complex_algorithm.
# Запустите задекорированную функцию и проверьте время её выполнения.

import time
from typing import Callable


class LoggerDecorator:
    def __init__(self, func: Callable) -> None:
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        arguments = ", ".join([repr(a) for a in args])
        result = self.func(*args, **kwargs)
        end_time = time.time()

        print(f"Вызов функции {self.func.__name__}")
        print(f"Аргументы: ({arguments}), {kwargs}")
        print(f"Результат: {result}")
        print(f"Время выполнения: {(end_time - start_time):.3f} секунд")

        return result


@LoggerDecorator
def complex_algorithm(arg1, arg2):
    # Здесь выполняется “сложный” алгоритм
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    # Можете попробовать вынести создание файла из циклов и проверить, сколько времени алгоритм будет работать в этом
    # случае
    return result


# Пример вызова функции с применением декоратора
result = complex_algorithm(10, 50)
