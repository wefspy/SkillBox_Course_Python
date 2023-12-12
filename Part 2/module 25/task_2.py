# Один буддист-программист решил создать свой симулятор жизни, в котором нужно
# набрать 500 очков кармы (это константа), чтобы достичь просветления.
#
# Каждый день вызывается специальная функция one_day(), которая возвращает количество
# кармы от 1 до 7 и может с вероятностью 1 к 10 выкинуть одно из исключений:
#
# KillError,
# DrunkError,
# CarCrashError,
# GluttonyError,
# DepressionError.
# (Исключения нужно создать самостоятельно, при помощи наследования от Exception.)
#
# Напишите такую программу. Функцию оберните в бесконечный цикл, выход из которого возможен
# только при накоплении кармы до уровня константы. Исключения обработайте и запишите в отдельный лог karma.log.
#
# По итогу у вас может быть примерно такая структура программы:
#     открываем файл
#     цикл по набору кармы
#        try
#           карма += one_day()
#        except(ы) с указанием классов исключений, которые нужно поймать
#           добавляем запись в файл
#     закрываем файл


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


import random


def one_day():
    errors = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]

    if random.randint(1, 10) == 1:
        raise random.choice(errors)

    return random.randint(1, 7)


final_karma = 500
with open('karma.log', 'w', encoding = 'UTF-8') as karma_log:
    karma = 0
    while karma < final_karma:
        try:
            karma += one_day()
        except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as e:
            karma_log.write(e.__class__.__name__ + '\n')
