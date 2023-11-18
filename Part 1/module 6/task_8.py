print('Задача 8. Игра «Компьютер угадывает число»')

# Поменяйте мальчика и компьютер из прошлой задачи местами.
# Теперь мальчик загадывает число между 1 и 100 (включительно).
# Компьютер может спросить у мальчика:
# «Твое число равно, меньше или больше, чем число N?»,
# где N — число, которое хочет проверить компьютер.
# Мальчик отвечает одним из трёх чисел:
# 1 — равно,
# 2 — больше,
# 3 — меньше.
 
# Напишите программу, 
# которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.
 
# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.

# Подсказка: При желании найдите описание алгоритма бинарного поиска и попробуйте применить в этой задаче.
#Разбор подобного решения будет в следующем модуле.

target_number = int(input("Введите число: "))
number_attempts = 0
left = 1
right = 100

while True:
  number_attempts += 1
  mid = (left + right) // 2

  response = int(
    input(f"Твое число равно, меньше или больше, чем число {mid}? (1 - равно, 2 - больше, 3 - меньше): "))

  if response == 1:
    print(f"Компьютер угадал число {mid} за {number_attempts} попыток!")
    break
  elif response == 2:
    left = mid + 1
  elif response == 3:
    right = mid - 1