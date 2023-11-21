print('Задача 7. Пирамидка 2')


# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
# 
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

height = int(input('Введите высоту пирамиды: '))

num = 1
for level in range(height):
  print((height - 1 - level) * '   ' + str(num), end = '')
  num += 2
  for i in range(level):
    print(f'    {num}', end = '')
    num += 2
  print()