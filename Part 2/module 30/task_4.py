# В одной организации перед записью телефонного номера в базу данных его проверяют 
# на соответствие следующим критериям: 
#     Длина номера — ровно десять знаков.
#     Номер начинается с цифры 8 или 9.
#     Остальные знаки — только цифры.

# На вход в программу подаётся список номеров (можно взять готовый или запросить у пользователя). 
# Реализуйте код, который проверяет каждый номер из списка на соответствие критериям и выводит 
# на экран соответствующие сообщения.

# Пример списка:
#     ['9999999999', '999999-999', '99999x9999']

# Результат:
#     первый номер: всё в порядке
#     второй номер: не подходит
#     третий номер: не подходит


import re


def check_phone_numbers(numbers):
	for number in numbers:
		if re.match(r'\b[89]\d{9}\b', number):
			print(f"{number}: всё в порядке")
		else:
			print(f"{number}: не подходит")



phone_numbers = ['9999999999', '999999-999', '99999x9999']


check_phone_numbers(phone_numbers)
