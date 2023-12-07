# На вход в программу подаётся строка, в которой буква h встречается как минимум два раза.
# Реализуйте код, который разворачивает последовательность символов, заключённую между
# первым и последним появлением буквы h, в противоположном порядке.
#
# Пример 1:
# Введите строку: hqwehrty
# Развёрнутая последовательность между первым и последним h: ewq.
#
# Пример 2:
# Введите строку: hh
# Развёрнутая последовательность между первым и последним h:
#
# Пример 3:
# Введите строку: hhqwerh
# Развёрнутая последовательность между первым и последним h: rewqh.

string = input('Введите строку: ')

print(f'Развёрнутая последовательность между первым и последним h: {string[string.rindex('h')-1:string.index('h'):-1]}')