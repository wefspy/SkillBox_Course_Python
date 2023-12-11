# Мало кто не знает знаменитый роман Л. Н. Толстого «Война и мир». Это довольно объёмное произведение
# лежит в архиве voina-i-mir.zip. Напишите программу, которая подсчитывает статистику по буквам
# (не только русского алфавита) в этом романе и выводит результат на экран (или в файл).
# Результат должен быть отсортирован по частоте встречаемости букв (по возрастанию или убыванию). Регистр символов имеет значение.
#
# Архив можно распаковать вручную, но, если хотите, можете изучить документацию по модулю zipfile
# (можно использовать и другой модуль) и попробовать написать код, который будет распаковывать архив за вас.

from collections import defaultdict

with open('voina-i-mir.txt', 'r', encoding='windows-1251') as file:
    text = file.read()

dict_freq = defaultdict(int)
char_count = 0

for char in text:
    if char.isalpha():
        char_count += 1
        dict_freq[char] += 1

sorted_freq = sorted(dict_freq.items(), key=lambda x: (-x[1], x[0]))

with open('letter_statistics.txt', 'w', encoding='UTF-8') as file:
    for letter, count in sorted_freq:
        frequency = count / char_count
        file.write(f"{letter}: {frequency:.6f}\n")