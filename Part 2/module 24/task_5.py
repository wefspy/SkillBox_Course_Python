# Чтобы понять, стоит ли ему жить с кем-то или лучше остаться в гордом одиночестве,
# Артём решил провести необычное исследование. Для этого он реализовал модель человека и модель дома.
#
# Человек может (должны быть такие методы):
#     есть (+ сытость, − еда);
#     работать (− сытость, + деньги);
#     играть (− сытость);
#     ходить в магазин за едой (+ еда, − деньги);
#     прожить один день (выбирает одно действие согласно описанному ниже приоритету и выполняет его).
#
# У человека есть (должны быть такие атрибуты):
#     имя,
#     степень сытости (изначально 50),
#     дом.
#
#
# В доме есть:
#     холодильник с едой (изначально 50 еды),
#     тумбочка с деньгами (изначально 0 денег).
#
# Если сытость человека становится меньше нуля, человек умирает.
#
# Логика действий человека определяется следующим образом:
#     Генерируется число кубика от 1 до 6.
#     Если сытость < 20, то нужно поесть.
#     Иначе, если еды в доме < 10, то сходить в магазин.
#     Иначе, если денег в доме < 50, то работать.
#     Иначе, если кубик равен 1, то работать.
#     Иначе, если кубик равен 2, то поесть.
#     Иначе играть.
#
# По такой логике эксперимента человеку надо прожить 365 дней.
#
# Реализуйте такую программу и создайте двух людей, живущих в одном доме. Проверьте работу программы несколько раз.


class House:

    def __init__(self, food = 50, money = 0):
        self.food = food
        self.money = money

    def there_is_food(self):
        return self.food > 0

    def try_take_food(self):
        if self.there_is_food():
            self.food -= 1
            return True
        return False

    def put_food(self):
        self.food += 1

    def there_is_money(self):
        return self.money > 0

    def try_take_money(self):
        if self.there_is_money():
            self.money -= 1
            return True
        return False

    def put_money(self):
        self.money += 1


import random

class Person:

    def __init__(self, name, house, satiety = 50):
        self.name = name
        self.satiety = satiety
        self.house = house

    def is_alive(self):
        return self.satiety >= 0

    def eat(self):
        if self.house.try_take_food():
            self.satiety += 1

    def work(self):
        self.house.put_money()
        self.satiety -= 1

    def play(self):
        self.satiety -= 1

    def go_shop(self):
        if self.house.try_take_money():
            self.house.put_food()

    def live_day(self):
        dice = random.randint(1, 6)
        if self.satiety < 20: self.eat()
        elif self.house.food < 10: self.go_shop()
        elif self.house.money < 50: self.work()
        elif dice == 1: self.work()
        elif dice == 2: self.eat()
        else: self.play()



def live_in_one_house_365_days(*args):
    family = [*args]
    for day in range(365):
        for person in family:
            if person.is_alive(): person.live_day()
            else:
                print(f'{person.name} умер.')
                family.remove(person)

        if len(family) == 0:
            print(f'Все жители дома погибли на {day+1} день.')
            break

    if len(family) > 0:
        print('Поздравляем! В доме остались выжившие. Имена этих счастливчиков: ')
        for person in family:
            print(person.name)

house = House()
husband = Person('Tom', house)
wife = Person('Monique', house)

live_in_one_house_365_days(husband)