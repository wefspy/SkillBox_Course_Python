# Реализуйте два класса: «Родитель» и «Ребёнок».
#
# У родителя есть:
#     имя,
#     возраст,
#     список детей.
# И он может:
#     сообщить информацию о себе,
#     успокоить ребёнка,
#     покормить ребёнка.
#
# У ребёнка есть:
# имя,
# возраст (должен быть меньше возраста родителя хотя бы на 16 лет),
# состояние спокойствия,
# состояние голода.
#
# Реализация состояний — на ваше усмотрение. Это может быть и простой «флаг», и словарь состояний, и что-то поинтереснее.

from enum import Enum

class Mood(Enum):
    calm = 1
    cry = 2

class Satiety(Enum):
    full = 1
    hungry = 2


class Child:

    def __init__(self, name: str, age: int, mood: Mood, satiety: Satiety):
        self.name = name
        self.age = age
        self.mood = mood
        self.satiety = satiety



class Parent:

    def __init__(self, name: str, age: int, children: list[Child]):
        self.name = name
        self.age = age
        self.children = children

    def toString(self):
        return f'{self.name}, {self.age} лет. Её дети: {self.children}.'

    def calm_down(self, child):
        child.mood = Mood.calm

    def feed(self, child):
        child.satiety = Satiety.full

    def register_child(self, child):
        if self.age < 16: raise ValueError('Родителю должно быть хотя бы 16 лет.')
        self.children.append(child)