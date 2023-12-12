# Вы работаете в команде разработчиков мобильной игры, и вам досталась часть от ТЗ заказчика.
#
# Есть два юнита, каждый называется «Воин». Каждому устанавливается здоровье в 100 очков.
# Они бьют друг друга в случайном порядке. Тот, кто бьёт, здоровье не теряет.
# У того, кого бьют, оно уменьшается на 20 очков от одного удара.
# После каждого удара надо выводить сообщение, какой юнит атаковал и сколько у противника осталось здоровья.
# Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.

class Warrior:
    def __init__(self, name, health=100, damage=20):
        self.name = name
        self.health = health
        self.damage = damage

    def hit(self, warrior):
        return warrior.hurt(self.damage)

    def hurt(self, damage):
        self.health -= damage
        return self.health

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f'Имя:{self.name} Здоровье:{self.health} Урон:{self.damage}'



import random

def fight(*args : Warrior):
    fighters = [*args]
    print(f'Вашему вниманию предоставляются бойцы: ')
    for num, fighter in enumerate(fighters):
        print(f'{num+1}) {fighter}')

    print('Бой начинается!')
    while len(fighters) > 1:
        attacking, damaged = random.sample(fighters, 2)
        print(f'{attacking.name} наносит удар по {damaged.name}')
        attacking.hit(damaged)
        print(f'{damaged.name} пропускает удар на {attacking.damage} очков. У него осталось {damaged.health} здоровья.')
        if not damaged.is_alive():
            print(f'К сожалению, {damaged.name} выбывает из игры!')
            fighters.remove(damaged)

    print(f'Победу одерживает {fighters[0].name}! У него осталось {fighters[0].health} здоровья! Поздравим его.')





warrior1 = Warrior('Tom')
warrior2 = Warrior('Jack')
warrior3 = Warrior('Conor')
warrior4 = Warrior('Tyler')

fight(warrior1, warrior2, warrior3, warrior4)

