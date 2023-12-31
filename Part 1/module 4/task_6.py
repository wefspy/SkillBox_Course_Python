print('Задача 6. Игра в кубики')

# Вася понимает, как важен отдых после тяжёлого рабочего дня, поэтому часто ходит в местный бар с друзьями. Владелец бара любит азартные игры и иногда предлагает посетителям с ним сыграть. Вася избегает азартные игры, но предложил владельцу купить у него программу для расчёта результатов игры, которую можно выводить на экраны бара.

# Напишите программу: на вход в неё подаётся два числа. Если первое число больше или равно второму, то нужно вывести на экран их разность и отдельной строкой: «Игрок платит». В противном случае, вывести их сумму и отдельной строкой: «Владелец платит». Последней строкой на экран должна быть выведена фраза: «Игра окончена».

# Пример:
# Кубик Кости: 3
# Кубик владельца: 4
# Сумма: 7
# Владелец платит
# Игра окончена

number_point_dice_player = int(input('Кубик Кости: '))
number_point_dice_owner = int(input('Кубик владельца: '))

sum_points = number_point_dice_player + number_point_dice_owner

if number_point_dice_player >= number_point_dice_owner:
  print(f'Разность: {number_point_dice_player - number_point_dice_owner}')
  print('Игрок платит')
else:
  print(f'Сумма: {number_point_dice_player + number_point_dice_owner}')
  print('Владелец платит')