# При работе с сетью и веб-сервисами иногда используется функция callback,
# так называемая функция обратного вызова. Это функция, которая вызывается при срабатывании
# определённого события: переходе на страницу, получении сообщения или окончании обработки процессором.
# В неё можно передать функцию, чтобы она выполнилась после определённого события.
# Это используется, например, в HTTP-серверах в ответ на URL-запросы. Реализуйте такую функцию.

# Пример функции:
#     @callback('//')
#     def example():
#         print('Пример функции, которая возвращает ответ сервера')
#         return 'OK'

# Основной код:
#     route = app.get('//')
#     if route:
#         response = route()
#         print('Ответ:', response)
#     else:
#         print('Такого пути нет')

# Ожидаемый результат: пример функции, которая возвращает ответ сервера.
#     Ответ: OK.

from typing import Callable

app = {}


def callback(route: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        app[route] = func
        return func

    return decorator


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
