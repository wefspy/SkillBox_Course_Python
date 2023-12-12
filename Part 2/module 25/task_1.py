# Реализуйте иерархию классов, описывающих имущество налогоплательщиков.
# Она должна состоять из базового класса Property и производных от него классов Apartment, Car и CountryHouse.
#
# Базовый класс должен иметь атрибут worth (стоимость), который передаётся в конструктор,
# и метод расчёта налога, переопределённый в каждом из производных классов.
# Налог на квартиру вычисляется как 1/1000 её стоимости, на машину — 1/200, на дачу — 1/500.
#
# Каждый дочерний класс должен иметь конструктор с одним параметром,
# передающий свой параметр конструктору базового класса.
#
# Разработайте интерфейс программы. Пусть она запрашивает у пользователя количество его денег
# и стоимость имущества, а затем выдаёт налог на соответствующее имущество
# и показывает, сколько денег ему не хватает (если это так).

from abc import ABC, abstractmethod


class Property(ABC):
    def __init__(self, worth):
        self.worth = worth

    @abstractmethod
    def calculate_tax(self):
        pass


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.worth * 1 / 1000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.worth * 1 / 200


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.worth * 1 / 500



money = float(input('Сколько у вас денег: '))

apartment = Apartment(float(input('Стоимость квартиры: ')))
car = Car(float(input('Стоимость машины: ')))
countryHouse = CountryHouse(float(input('Стоимость загородного дома: ')))

total_tax = apartment.calculate_tax() + car.calculate_tax() + countryHouse.calculate_tax()

if money < total_tax:
    print(f'Для погашения налоговой декларации вам не хватает {total_tax - money}.')
else: print(f'Вам хватает средств оплатить налоговую декларацию.')
