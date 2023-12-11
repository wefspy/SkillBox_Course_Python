# В файле first_tour.txt записано число K и данные об участниках турнира по настольной игре «Орлеан»:
# фамилии, имена и количество баллов, набранных в первом туре. Во второй тур проходят участники,
# которые набрали более K баллов в первом туре.
#
# Напишите программу, которая выводит в файл second_tour.txt данные всех участников,
# прошедших во второй тур, с нумерацией.
#
# В первой строке нужно вывести в файл second_tour.txt количество участников второго тура.
# Затем программа должна вывести фамилии, инициалы и количество баллов всех участников, прошедших во второй тур,
# с нумерацией. Имя нужно сократить до одной буквы. Список должен быть отсортирован по убыванию набранных баллов.
#
# Пример:
# Содержимое файла first_tour.txt:
# 80
# Ivanov Serg 80
# Sergeev Petr 92
# Petrov Vasiliy 98
# Vasiliev Maxim 78
#
# Содержимое файла second_tour.txt:
# 2
# 1) V. Petrov 98
# 2) P. Sergeev 92

first_tour = open('first_tour.txt', 'r', encoding = 'UTF-8')
second_tour = open('second_tour.txt', 'w', encoding = 'UTF-8')

passing_score = int(first_tour.readline())
passing_players = []
for player in first_tour:
    name, surename, score = player.split()
    if int(score) > passing_score:
        passing_players.append(f'{name[0]}. {surename} {score}')

first_tour.close()


second_tour.write(f'{str(len(passing_players))} \n')
for player in passing_players:
    second_tour.write(f'{player}\n')

second_tour.close()