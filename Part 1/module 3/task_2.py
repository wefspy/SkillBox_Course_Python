print('Задача 2. Финансовый отчёт')

# Васе пришло очередное задание — автоматизация финансовой отчётности.
# Звучит сложно, а на деле нужно просто написать код, который будет считать нужные для отчёта вычисления автоматически.
# Вычисления, которые нужно реализовать в программе: сумму дохода первых двух кварталов поделить на сумму последних двух кварталов,
# чтобы понять динамику роста или падения дохода.

# Алгоритм действий в программе:
# 1) Запросить у пользователя четыре числа.
# 2) Отдельно сложить два первых и два вторых.
# 3) Разделить первую сумму на вторую.
# 4) Вывести результат на экран.

first_quarter = int(input("Введите первое число: "))
second_quarter = int(input("Введите второе число: "))
third_quarter = int(input("Введите третье число: "))
fourth_quarter = int(input("Введите четвертое число: "))

sum_first_two_quarters = first_quarter + second_quarter
sum_last_two_quarters = third_quarter + fourth_quarter

income_dynamics = sum_first_two_quarters / sum_last_two_quarters
print(income_dynamics)