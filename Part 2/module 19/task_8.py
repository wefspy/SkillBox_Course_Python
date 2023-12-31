# Пользователь вводит строку. Необходимо написать программу, которая определяет,
# существует ли у этой строки перестановка, при которой она станет палиндромом.
# Затем она должна выводить соответствующее сообщение.
#
# Пример 1
# Введите строку: aab
# Можно сделать палиндромом
#
# Пример 2
# Введите строку: aabc
# Нельзя сделать палиндромом

string = input('Введите строку: ')

def can_be_palindrome(string):
    for i in range(len(string)):
        shift_string = string[i:] + string[:i]
        if shift_string == shift_string[::-1]:
            print('Можно сделать палиндромом')
            return

    print('Нельзя сделать палиндромом')

can_be_palindrome(string)