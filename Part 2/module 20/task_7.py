# В самом конце собеседования вам неожиданно сказали: «Расскажите, что делает функция zip».
# Чтобы произвести впечатление, вы решили не только рассказать о ней, но и написать её аналог.
#
# Даны строка и кортеж из чисел. Напишите программу, которая создаёт генератор из пар кортежей «символ — число».
# Затем выведите на экран сам генератор и кортежи.
#
# Пример:
# Строка: abcd
# Кортеж чисел: (10, 20, 30, 40)
#
# Результат:
# <generator object <genexpr> at 0x00000204A4234048>
# ('a', 10)
# ('b', 20)
# ('c', 30)
# ('d', 40)

def zip_alternative(string, ints):
    return ((string[pointer], ints[pointer]) for pointer in range(min(len(string), len(ints))))

ints = (10, 20, 30, 40)
string = 'abcd'
func = zip_alternative(ints, string)

print(func)
print(*func, sep = '\n')