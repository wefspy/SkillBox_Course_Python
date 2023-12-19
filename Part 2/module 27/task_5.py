# Создайте декоратор, который кэширует (сохраняет для дальнейшего использования)
# результаты вызова функции и, при повторном вызове с теми же аргументами,
# возвращает сохранённый результат.

# Примените его к рекурсивной функции вычисления чисел Фибоначчи.

# В итоге декоратор должен проверять аргументы, с которыми вызывается функция, и,
# если такие аргументы уже использовались, должен вернуть сохранённый результат вместо запуска расчёта.


def memoize(func):
    """
        Кэширование результатов вызовов декорируемой функции

    Args:
        func (_type_): Декорируемая функция

    Returns:
        _type_: Декоратор
    """
    cache = {}

    def memoized_func(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return memoized_func


@memoize
def fibonacci(n):
    """
        Рекурсивная функция для вычисления чисел Фибоначчи.

    Args:
        n (int): номер числа Фибоначчи

    Returns:
        int: значение числа Фибоначчи
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = 100
result = fibonacci(n)
print(f"{n}-е число фибоначчи это: {result}")