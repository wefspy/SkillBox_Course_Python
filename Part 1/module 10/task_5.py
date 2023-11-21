print('Задача 5. Наибольшая сумма цифр')

# Вводится N чисел. 
# Среди натуральных чисел, которые были введены, 
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

numbers = input('Введите числа через пробел: ').split()

max_sum = 0
max_number = 0

for num in numbers:
  sum = 0
  for digit in num:
    sum += int(digit)
  if sum > max_sum:
    max_sum = sum
    max_number = num

print(f'Наибольшее число: {max_number}. Сумма цифр: {max_sum}')