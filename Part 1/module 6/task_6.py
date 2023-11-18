print('Задача 6. Вклады')

# Вклад в банке составляет X рублей.
# Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается.

# Определите, через сколько лет вклад составит не менее Y рублей.

# Напишите программу,
# которая по данным числам X, Y, P определяет,
# сколько лет пройдёт, прежде чем сумма достигнет значения Y.

X = int(input("Введите величину вклада: "))
P = int(input("Введите процентную ставку: "))
Y = int(input("Какую сумма необходима? "))
years = 0
while X < Y:
  percent = X * (P / 100)
  if (percent < 1):
    print(f"Увеличте процентную ставку")
    break
  X += percent
  years += 1
  X //= 1
print(f"{years} лет понадобится")