# В файле zen.txt хранится так называемый Дзен Пайтона — текст философии
# программирования на языке Python.
#
# Напишите программу, которая выводит на экран все строки этого файла в обратном порядке.
#
# Пример:
# zen.txt
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
#
# Результат работы программы:
# Namespaces are one honking great idea -- let's do more of those!
# If the implementation is easy to explain, it may be a good idea.

file = open('zen.txt', 'r', encoding = 'UTF-8')
arr_strings = file.read().split('\n')

for string in arr_strings[::-1]:
    print(string)