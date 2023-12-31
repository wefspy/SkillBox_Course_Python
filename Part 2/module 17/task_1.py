# Команде лингвистов понравилось качество ваших программ, поэтому они решили
# заказать функцию для анализатора текста, которая создавала бы список гласных букв
# в нём и считала бы их количество.
#
# Напишите программу, которая запрашивает у пользователя текст
# и генерирует список гласных букв этого материала (сама строка вводится на русском языке).
# Выведите в консоль сам список и его длину.
#
# Пример:
# Введите текст: Нужно отнести кольцо в Мордор!
# Список гласных букв: ['у', 'о', 'о', 'е', 'и', 'о', 'о', 'о', 'о']
# Длина списка: 9

vowels = ['а', 'у', 'о', 'ы', 'э', 'я', 'ю', 'ё', 'и', 'е']

string = input('Введите текст: ')
res = []

for letter in string:
    if letter in vowels:
        res.append(letter)

print(f'Список гласных букв: {res}')
print(f'Длина списка: {len(res)}')