# Пользователь вводит искомый ключ. Если он хочет, то может ввести максимальную
# глубину — уровень, до которого будет просматриваться структура.
#
# Напишите функцию, которая находит заданный пользователем ключ в словаре и выдаёт
# значение этого ключа на экран. По умолчанию уровень не задан.
#
# Пример 1
# Введите искомый ключ: head
# Хотите ввести максимальную глубину? Y/N: n
# Значение ключа: {'title': 'Мой сайт'}
#
# Пример 2
# Введите искомый ключ: head
# Хотите ввести максимальную глубину? Y/N: y
# Введите максимальную глубину: 1
# Значение ключа: None

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

import math

def find_record(dictionary, user_key, depth = math.inf):
    found_record = None
    if user_key in dictionary:
        return dictionary[user_key]

    if depth > 1:
        for key in dictionary:
            found_record = find_record(dictionary[key], user_key, depth - 1)

    return found_record



user_key = input('Введите искомый ключ: ')
can_set_depth = input('Хотите ввести максимальную глубину? Y/N: ').lower()

if can_set_depth == 'y':
    depth = int(input('Введите максимальную глубину: '))
    record = find_record(site, 'head', depth)
else:
    record = find_record(site, 'head')


print(record)