# Реализуйте программу — чат, в котором могут участвовать сразу несколько человек,
# то есть программу, которая может работать одновременно для нескольких пользователей.
# При запуске запрашивается имя пользователя. После этого он выбирает одно из действий:
#           Посмотреть текущий текст чата.
#           Отправить сообщение (затем вводит сообщение).
# Действия запрашиваются бесконечно.
#
# Примечание: для решения задачи вам достаточно текущих знаний, нужно лишь проявить немного
# фантазии и хитрости. Не углубляйтесь в дебри работы с сетями, создание GUI-приложений и прочее.
# Однако, если очень хочется, то останавливать вас никто не будет!

import os
from datetime import datetime

name = input('Введите имя пользователя: ')
while True:
    action = int(input('\n1 Посмотреть чат \n2 Отправить сообщение \nВыберите действие(1/2): '))
    if action == 1:
        if os.path.exists('chat.txt'):
            with open('chat.txt', 'r', encoding = 'UTF-8') as chat:
                print(chat.read())
        else: print('Чат пустой. Оставь первоей сообщение!\n')
    elif action == 2:
        message = input('Введите сообщение: ')
        with open('chat.txt', 'a', encoding = 'UTF-8') as chat:
            chat.write(f'{datetime.now().strftime('%d %b. %Y %H:%M')}. {name}: {message}\n')
    else: print('Неверно. Попробуйте еще раз.\n')