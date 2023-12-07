# Напишите программу, которая инициализирует список из 10 случайных целых чисел,
# а затем делит эти числа на пары кортежей внутри списка. Выведите результат на экран.
#
# Дополнительно: решите задачу несколькими способами.
#
# Оригинальный список: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Новый список: [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]

import random

array = [random.randint(1,20) for integer in range(10)]
print(f'Оригинальный список: {array}')

new_array = []
while len(array) > 0:
    random_index = random.randint(0, len(array)-1)
    elm1 = array.pop(random_index)

    random_index = random.randint(0, len(array)-1)
    elm2 = array.pop(random_index)

    new_array.append((elm1, elm2))

print(f'Новый список: {new_array}')



array = [random.randint(1,20) for integer in range(10)]
print(f'Оригинальный список: {array}')

new_array = [tuple([array[x], array[x+1]]) for x in range(0, 10, 2)]
print(f'Новый список: {new_array}')