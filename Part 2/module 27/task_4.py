# Реализуйте декоратор counter, считающий и выводящий количество вызовов декорируемой функции.

# Для решения задачи нельзя использовать операторы global и nonlocal (об этом мы ещё расскажем).

from typing import Callable, Any
import functools
from collections import defaultdict


def counter(func: Callable) -> Callable:
    """
        Декоратор подсчета вызова функции через словарь function_call

    Args:
        func (Callable): Декорируемая функция

    Returns:
        Callable: Декоратор, подсчитывающий кол-во вызовов и вызывающий функцию
    """

    function_call = defaultdict(int)

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        function_call[func.__name__] += 1
        print(f'Функция {func.__name__} вызвана {function_call[func.__name__]} раз.')
        return func(*args, **kwargs)

    return wrapper


@counter
def first_test_func() -> None:
    """
        Тест функция, выводящая сообщение в консоль о своем выполнении
    """    
    print('first test function complete!')


@counter
def second_test_func() -> None:
    """
        Тест функция, выводящая сообщение в консоль о своем выполнении
    """    
    print('second test function complete!')


first_test_func()
first_test_func()
second_test_func()
first_test_func()
