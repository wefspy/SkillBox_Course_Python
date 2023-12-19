# Реализуйте декоратор singleton, который превращает класс в одноэлементный.
# При множественной инициализации объекта этого класса будет сохранён только первый инстанс,
# а все остальные попытки создания будут возвращать первый экземпляр.
from typing import Callable


def singleton(cls):
    cls.__obj = None

    def wrapper(*args, **kwargs):
        if cls.__obj is None:
            cls.__obj = cls(*args, **kwargs)
        return cls.__obj

    return wrapper


@singleton
class Example:
    pass


example1 = Example()
example2 = Example()
print(example1 is example2)
