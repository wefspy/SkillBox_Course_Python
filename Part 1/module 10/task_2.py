print('Задача 2. Лестница')

# Пользователь вводит число N.
# Напишите программу, которая выводит такую “лесенку” из чисел:

# Введите число: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

N = int(input("Введите число: "))
for row in range(N):
  for col in range(row + 1):
    print(row + 1, end = "\t")
  print()