# Пользователь вводит строку. Напишите программу, которая меняет регистр символов
# в этой строке так, чтобы первая буква каждого слова была прописной, а остальные — строчными.
#
# Пример
# Введите строку: Кажется, я забыл выключить утюг.
# Результат: Кажется, Я Забыл Выключить Утюг.

string = input('Введите строку: ')

print(f'Результат: {string.title()}')