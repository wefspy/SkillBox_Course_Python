# Мы продолжаем тему структур данных и алгоритмов. И в этот раз вам нужно реализовать односвязный список.
#
# Связный список — это структура данных, которая состоит из элементов, называющихся узлами.
# В узлах хранятся данные, а между собой узлы соединены связями. Связь — это ссылка на следующий или предыдущий элемент списка.
#
# В односвязном списке связь — это ссылка только на следующий элемент, то есть в нём можно передвигаться только в сторону конца списка.
# Узнать адрес предыдущего элемента, опираясь на содержимое текущего узла, невозможно.
#
# Реализуйте такую структуру данных без использования стандартных структур Python (list, dict, tuple и прочие) и дополнительных модулей.
#
# Для реализации напишите два класса: Node и LinkedList. В Node должна быть логика работы одного узла (хранение данных и указателя).
#
# Для структуры реализуйте следующие методы:
#     append — добавление элемента в конец списка;
#     get — получение элемента по индексу;
#     remove — удаление элемента по индексу.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get(self, index):
        if index < 0:
            return None
        current = self.head
        for i in range(index):
            if current.next:
                current = current.next
            else:
                return None
        return current.data

    def remove(self, index):
        if index < 0 or not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for i in range(index - 1):
            if current.next:
                current = current.next
            else:
                return
        if current.next:
            current.next = current.next.next

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __repr__(self):
        return '[' + ' '.join(str(data) for data in self) + ']'