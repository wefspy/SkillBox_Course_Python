# Частная контора даёт в прокат ролики самых разных размеров.
# Человек может надеть ролики только своего размера.
#
# Пользователь вводит два списка размеров:
# N размеров роликов и K размеров ног людей.
# Реализуйте код, который определяет, какое наибольшее число человек может
# одновременно взять ролики и пойти кататься.
#
# Пример:
# Количество роликов: 4
# Размер пары 1: 41
# Размер пары 2: 40
# Размер пары 3: 39
# Размер пары 4: 42
# Количество людей: 3
# Размер ноги человека 1: 42
# Размер ноги человека 2: 41
# Размер ноги человека 3: 42
# Наибольшее количество людей, которые могут взять ролики: 2

def check_size(size):
    if size > 0:
        return True
    print('Ошибка. Некорректный размер.')
    return False

num_rollers = int(input('Количество роликов: '))
rollers_sizes = []

for num in range(num_rollers):
    size = int(input(f'Размер пары {num + 1}: '))
    if check_size(size):
        rollers_sizes.append(size)


num_people = num_rollers = int(input('Количество людей: '))
feet_size_people = []

for num in range(num_people):
    size = int(input(f'Размер ноги человека {num + 1}: '))
    if check_size(size):
        feet_size_people.append(size)

count = 0
for person in feet_size_people:
    if person in rollers_sizes:
        count += 1
        rollers_sizes.remove(person)

print(f'Наибольшее количество людей, которые могут взять ролики: {count}')