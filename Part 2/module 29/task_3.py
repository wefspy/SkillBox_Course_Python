# Реализуйте декоратор, который будет логировать все методы декорируемого класса 
# (кроме магических методов) и в который можно передавать формат вывода даты и времени логирования.


import datetime
import time
from typing import Callable, Any


def log_method(func: Callable, date_formate: str) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        print(f'Запускается {func.__name__}. Дата и время запуска: {datetime.datetime.now().strftime(date_formate)}.')
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Завершение {func.__name__}, время работы = {(end_time - start_time):.3f} s.')
        return result

    return wrapper


def log_methods(date_formate: str) -> Callable:
    def decorator(cls) -> None:
        for method in dir(cls):
            if not method.startswith('__'):
                current_method = getattr(cls, method)
                decorate_method = log_method(current_method, date_formate)
                setattr(cls, method, decorate_method)

        return cls

    return decorator


@log_methods('%b %d %Y — %H:%M:%S')
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods('%b %d %Y - %H:%M:%S')
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print('Наследник test sum 1')

    def test_sum_2(self):
        print('test sum 2')
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
