# Мы уже говорили, что в программировании нередко необходимо создавать свои собственные
# структуры данных на основе уже существующих. Одной из таких базовых структур является стек.
#
# Стек — это абстрактный тип данных, представляющий собой список элементов,
# организованных по принципу LIFO (англ. last in — first out, «последним пришёл — первым вышел»).
#
# Простой пример: стек из книг на столе. Единственной книгой, обложка которой видна, является самая верхняя.
# Чтобы получить доступ, например, к третьей снизу книге, нам нужно убрать все книги, лежащие сверху, одну за другой.
#
# Напишите класс, который реализует стек и его возможности (достаточно будет добавления и удаления элемента).
#
# После этого напишите ещё один класс — «Менеджер задач». В менеджере задач можно выполнить команду «новая задача»,
# в которую передаётся сама задача (str) и её приоритет (int). Сам менеджер работает на основе стека (не наследование).
# При выводе менеджера в консоль все задачи должны быть отсортированы
# по следующему приоритету: чем меньше число, тем выше задача.
#
# Вот пример основной программы:
# manager = TaskManager()
# manager.new_task("сделать уборку", 4)
# manager.new_task("помыть посуду", 4)
# manager.new_task("отдохнуть", 1)
# manager.new_task("поесть", 2)
# manager.new_task("сдать ДЗ", 2)
# print(manager)
#
# Результат:
# 1 — отдохнуть
# 2 — поесть; сдать ДЗ
# 4 — сделать уборку; помыть посуду
#
# Дополнительно: реализуйте также удаление задач и подумайте, что делать с дубликатами.

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()


class TaskManager:
    def __init__(self):
        self.tasks = Stack()

    def new_task(self, task, priority):
        self.tasks.push((task, priority))

    def __str__(self):
        sorted_tasks = sorted(self.tasks.items, key=lambda x: x[1])
        print(sorted_tasks)
        result = ''
        prev_priority = None
        for task in sorted_tasks:
            if task[1] != prev_priority:
                if prev_priority is not None:
                    result = result[:-2] + "\n"
                result += f"{task[1]} - {task[0]}, "
                prev_priority = task[1]

            else:
                result += f"{task[0]}, "
        return result