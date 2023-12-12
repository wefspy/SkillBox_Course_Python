# У вас есть файл с протоколом регистрации пользователей на сайте — registrations.txt.
# Каждая строка содержит имя, имейл и возраст, разделённые пробелами. Например: Василий test@test.ru 27.
#
# Напишите программу, которая проверяет данные из файла для каждой строки:
#           Присутствуют все три поля.
#           Поле «Имя» содержит только буквы.
#           Поле «Имейл» содержит @ и точку.
#           Поле «Возраст» представляет число от 10 до 99.
#
# В результате проверки сформируйте два файла:
#           registrations_good.log для правильных данных; записывать строки как есть;
#           registrations_bad.log — для ошибочных; записывать строку и вид ошибки.
#
# Для валидации строки данных напишите функцию, которая может выдавать исключения:
#           НЕ присутствуют все три поля: IndexError.
#           Поле «Имя» содержит НЕ только буквы: NameError.
#           Поле «Имейл» НЕ содержит @ и точку: SyntaxError.
#           Поле «Возраст» НЕ представляет число от 10 до 99: ValueError.

good_log = open('registrations_good.txt', 'w', encoding = 'UTF-8')
bad_log = open('registrations_bad.txt', 'w', encoding = 'UTF-8')
with open('registrations.txt', 'r', encoding = 'UTF-8') as registrations:
    clients = registrations.read().split('\n')
    for client in clients:
        try:
            fields = client.split()
            if len(fields) != 3:
                raise IndexError(client)
            if not fields[0].isalpha():
                raise NameError(client)
            if '@' not in fields[1] or '.' not in fields[1]:
                raise SyntaxError(client)
            if not 10 < int(fields[2]) < 99:
                raise ValueError(client)

            good_log.write(f'{client}\n')


        except IndexError as client:
            bad_log.write(f'{client}\tНЕ присутствуют все три поля\n')

        except NameError as client:
            bad_log.write(f'{client}\tПоле «Имя» содержит НЕ только буквы\n')

        except SyntaxError as client:
            bad_log.write(f'{client}\tПоле «Имейл» НЕ содержит @ и точку\n')

        except ValueError as client:
            bad_log.write(f'{client}\tПоле «Возраст» НЕ представляет число от 10 до 99\n')

good_log.close()
bad_log.close()