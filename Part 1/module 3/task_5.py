print('Задача 5. Часы')

# Напишите программу, 
# которая получает на вход число n — количество минут, — затем считает,
# 1) сколько это будет в часах 
# 2) сколько минут останется
# и выводит на экран эти два результата.
# (В вычислениях вам помогут операции // и %)

time_in_minute = int(input('Введите количество минут: '))
hours = time_in_minute // 60
minutes = time_in_minute % 60

print(f'{hours} часов, {minutes} минут')