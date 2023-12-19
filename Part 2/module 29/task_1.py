# Напишите декоратор check_permission, который проверяет, есть ли у пользователя доступ
# к вызываемой функции, и если нет, то выдаёт исключение PermissionError.

# Пример кода:
#     user_permissions = ['admin']

#     @check_permission('admin')
#     def delete_site():
#         print('Удаляем сайт')

#     @check_permission('user_1')
#     def add_comment():
#         print('Добавляем комментарий')

#     delete_site()
#     add_comment()

# Результат:
#     Удаляем сайт
#     PermissionError: у пользователя недостаточно прав, чтобы выполнить функцию add_comment


from typing import Callable
import functools


def check_permission(role: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        user_permissions = ['admin']

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if role in user_permissions:
                return func(*args, **kwargs)
            raise PermissionError(f'у пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')

        return wrapper

    return decorator


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
