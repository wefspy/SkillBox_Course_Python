# Реализуйте декоратор logging, который будет отвечать за логирование функций.
# На экран выводится название функции и её документация. Если во время выполнения декорируемой
# функции возникла ошибка, то в файл function_errors.log записываются название функции и ошибки.

# Также постарайтесь сделать так, чтобы программа не завершалась после обнаружения первой же ошибки,
# а обрабатывала все декорируемые функции и сразу записывала все ошибки в файл.

# Дополнительно: запишите дату и время возникновения ошибки, используя модуль datetime.


from typing import Callable, Any
import functools
import datetime


def logging(func: Callable) -> Callable:
    """Декоратор логирования декорируемой функции

    Args:
        func (Callable): Декорируемая функция

    Returns:
        Callable: Декоратор, подсчитывающий кол-во вызовов и вызывающий функцию
    """    
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(func.__name__)
        print(func.__doc__)
        try:
            return func(*args, **kwargs)

        except Exception:
            with open('function_errors.log', 'a', encoding='UTF-8') as errors_log:
                log = f'{str(datetime.datetime.now().strftime(
                    '%d-%m-%Y %H:%M:%S'))} {func.__name__}\n'
                errors_log.write(log)

    return wrapper


@logging
def func_with_value_error():
    """
        Функция с ошибкой ValueError.
    """
    raise ValueError


@logging
def func_without_error():
    """
        Функция без ошибки.
    """
    return


@logging
def func_with_type_error():
    """
        Функция с ошибкой TypeError.
    """
    raise TypeError


func_with_value_error()
func_without_error()
func_with_type_error()
