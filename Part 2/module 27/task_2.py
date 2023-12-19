# В программировании иногда возникает ситуация, когда работу функции нужно замедлить.
# Типичный пример — функция, которая постоянно проверяет, изменились ли данные на веб-странице или её код.

# Реализуйте декоратор, который перед выполнением декорируемой функции ждёт несколько секунд.

from typing import Callable, Any
import time


def delay_perfomance_func(time_delay: int) -> Callable:
    """
        Декоратор, задерживающий выполнение функции на time_delay

    Args:
        time_delay (int): время задержки выполнения функции

    Returns:
        Callable: Декоратор
    """    
    def actual_decorator(func: Callable) -> Callable:
        def wrapper_func(*args, **kwargs) -> Any:
            print('I\'m sleep')
            time.sleep(time_delay)
            print('I\'m get up')
            return func(*args, **kwargs)

        return wrapper_func
    return actual_decorator


@delay_perfomance_func(time_delay=5)
def test_func() -> None:
    """
        Тест функция, выводящая сообщение в консоль о своем выполнении
    """    
    print('function completed')


test_func()
