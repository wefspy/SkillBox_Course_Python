print('Задача 4. Недоделка 2')

# Вы всё так же работаете в конторе по разработке игр и смотрите различные программы прошлого горе-программиста. В одной из игр для детей, связанной с мультяшной работой с числами, вам нужно было написать код согласно следующим условиям: программа получает на вход два числа; в первом числе должно быть не менее трёх цифр, во втором — не менее четырёх, иначе программа выдаёт ошибку. Если всё нормально, то в каждом числе первая и последняя цифры меняются местами, а затем выводится их сумма.

# И тут вы натыкаетесь на программу, которая была написана предыдущим программистом и которая как раз решает такую задачу. Однако старший программист попросил вас немного переписать этот код, чтобы он не выглядел так ужасно. Да и вам самим становится, мягко говоря, не по себе от него.

# Постарайтесь разделить логику кода на три отдельные логические части (функции):
# count_numbers — получает число и возвращает количество цифр в числе;
# change_number — получает число, меняет в нём местами первую и последнюю цифры и возвращает изменённое число;
# main — функция ничего не получает на вход, внутри она запрашивает нужные данные от пользователя, выполняет дополнительные проверки и вызывает функции 1 и 2 для выполнения задачи (проверки и изменения двух чисел).

# Разбейте приведённую ниже программу на функции. Повторений кода должно быть как можно меньше. Также сделайте, чтобы в основной части программы был только ввод чисел, затем изменённые числа и вывод их суммы.


def count_numbers(n):
  return len(str(n))

def change_number(n):
  temp = str(n)
  return int(temp[-1] + temp[1:-1] + temp[0])

def main():
  n1 = int(input('Введите первое число: '))
  if count_numbers(n1) < 3:
    print('Число должно содержать не менее трёх цифр')
    return
    
  n2 = int(input('Введите второе число: '))
  if count_numbers(n2) < 4:
    print('Число должно содержать не четырех трёх цифр')
    return

  n1 = change_number(n1)
  n2 = change_number(n2)

  print(f'Сумма чисел: {n1 + n2}')

main()