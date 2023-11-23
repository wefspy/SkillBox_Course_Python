print('Задача 2. Посчитай чужую зарплату...')

# Бухгалтер устала постоянно считать вручную среднегодовую зарплату сотрудников компании
# и, чтобы облегчить себе жизнь, обратилась к программисту.
 
# Напишите программу,
# которая принимает от пользователя зарплату сотрудника за каждый из 12 месяцев 
# и выводит на экран среднюю зарплату за год.

salary = 0
for month in range(1, 12+1):
  salary += int(input(f"Введите зарплату за {month} месяц: "))
print(f"Среднегодовая зарплата сотрудника: {salary / 12}")