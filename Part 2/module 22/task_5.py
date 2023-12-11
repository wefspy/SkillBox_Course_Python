# Есть файл text.txt, который содержит текст. Напишите программу, которая
# выполняет частотный анализ, определяя долю каждой буквы английского алфавита в общем
# количестве английских букв в тексте, и выводит результат в файл analysis.txt.
# Символы, не являющиеся буквами английского алфавита, учитывать не нужно.
#
# В файл analysis.txt выводится доля каждой буквы, встречающейся в тексте, с тремя
# знаками в дробной части. Буквы должны быть отсортированы по убыванию их доли.
# Буквы с равной долей должны следовать в алфавитном порядке.
#
# Пример:
# Содержимое файла text.txt:
# Mama myla ramu.
#
# Содержимое файла analysis.txt:
# a 0.333
# m 0.333
# l 0.083
# r 0.083
# u 0.083
# y 0.083

from collections import defaultdict

alphabet = 'abcdefghijklmnopqrstuvwxyz'

file = open('text.txt', 'r', encoding = 'UTF-8')
text = file.read()
file.close()

dict_freq = defaultdict(int)
count_char = 0
for char in text:
    char = char.lower()
    if char in alphabet:
        count_char += 1
        dict_freq[char] += 1

sorted_freq = sorted(dict_freq.items(), key=lambda x: (-x[1], x[0]))

analysis_file = open("analysis.txt", "w")
for letter, count in sorted_freq:
    frequency = count / count_char
    analysis_file.write(f"{letter} {frequency:.3f}\n")

analysis_file.close()