print('Задача 3. Слишком большие числа')

# У неудачливого бухгалтера всё опять идёт наперекосяк: ему приносят такие большие счета, что числа не помещаются на бумаге. 

# Напишите программу, которая считала бы для него, сколько цифр во вводимом числе. Обратите внимание, что число 0 имеет одну цифру.

# Пример:
# Введите число: 567
# Ответ: 3

# Введите число: 1203
# Ответ: 4

number = int(input("Введите число: "))
count_digit = 0
while number > 0:
  number = number // 10
  count_digit += 1
print(f'Ответ: {count_digit}')