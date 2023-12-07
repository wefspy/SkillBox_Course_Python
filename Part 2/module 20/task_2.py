# Напишите функцию, возвращающую список элементов итерируемого объекта
# (кортежа, строки, списка, словаря), у которых индекс — это простое число.
#
# Для проверки на простое число напишите отдельную функцию is_prime.
#
# Необязательное усложнение: сделайте так, чтобы основная функция состояла только
# из оператора return и так же возвращала список.
#
# Пример вызова функции:
# print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# Ответ в консоли: [2, 3, 5, 7]
#
# print(crypto('О Дивный Новый мир!'))
# Ответ в консоли: ['Д', 'и', 'н', 'й', 'в', 'й', 'р']

def is_prime(num):
    if num % 2 == 0 or num == 1:
      return num == 2
    div = 3
    while div * div <= num and num % div != 0:
        div += 2
    return div * div > num

def crypto(collection):
    new_collection = []
    for index, item in enumerate(collection):
        if is_prime(index):
            new_collection.append(item)

    return new_collection

print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))