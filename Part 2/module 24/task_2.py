# Реализуйте модель с именем Student, содержащую поля «ФИ», «Номер группы», «Успеваемость» (список из пяти элементов).
# Затем создайте список из десяти студентов (данные о студентах можете придумать или запросить у пользователя)
# и отсортируйте список по возрастанию среднего балла. Выведите результат на экран.


class Student:

    def __init__(self, name, group_number, academic_performance):
        self.name = name
        self.group_number = group_number
        self.academic_performance = academic_performance

    def __str__(self):
        return f'{self.name} |\t{self.group_number} |\t{self.academic_performance}'


import statistics

students : list[Student] = [
    Student('Edward Johnson', 1, [5, 5, 4, 1, 2]),
    Student('Raymond Edwards', 1, [4, 4, 2, 2, 5]),
    Student('Milton Hawkins', 1, [3, 4, 3, 4, 4]),
    Student('Joseph Reynolds', 1, [2, 4, 3, 2, 5]),
    Student('Anthony Floyd', 2, [3, 4, 5, 2, 1]),
    Student('Albert Abbott', 2, [5, 2, 3, 2, 1]),
    Student('Darrell Rodriguez', 2, [4, 4, 5, 3, 5]),
    Student('Glenn Welch', 2, [1, 4, 3, 5, 5]),
    Student('Michael Reynolds', 3, [4, 5, 3, 2, 1]),
    Student('Mark Day', 3, [4, 2, 3, 5, 5])]


sorted_students = sorted(students, key = lambda x: statistics.mean(x.academic_performance))

print('Фамилия Имя |\t№ Группы |\tУспеваемость |\tСредний балл')
for student in sorted_students:
    print(f'{student} |\t{str(statistics.mean(student.academic_performance))}')
