# Во входном файле numbers.txt записано N целых чисел, которые могут быть
# разделены пробелами и концами строк. Напишите программу, которая выводит
# сумму чисел во выходной файл answer.txt.
#
# Пример:
# Содержимое файла numbers.txt
#      2 2
# 2
#   2
#         2
# Содержимое файла answer.txt
# 10

strings = open('numbers.txt', 'r', encoding = 'UTF-8')

total_sum = 0
for string in strings:
    nums = [int(num) for num in string.split() if num.isdigit()]
    total_sum += sum(nums)

answer = open('answer.txt', 'w', encoding = 'UTF-8')
answer.write(str(total_sum))

strings.close()
answer.close()