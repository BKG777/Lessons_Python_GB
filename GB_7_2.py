# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм.
# этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода ткани. Проверить на практике полученные
# на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    @abstractmethod
    def get_coat(self):
        pass

    @abstractmethod
    def get_suit(self):
        pass

    def get_total(self):
        pass


class Clothes(AbstractClothes):
    def __init__(self, v, h):
        self.v = v
        self.h = h
        self.coat_total = self.v / 6.5 + 0.5
        self.suit_total = self.h * 2 + 0.3

    def get_coat(self):
        return str(f'Расход ткани на пальто = {self.coat_total:.2f}')

    def get_suit(self):
        return str(f'Расход ткани на костюм = {self.suit_total:.2f}')

    @property
    def get_total(self):
        return str(f'Общий расход ткани = {self.coat_total + self.suit_total:.2f}')


clothes = Clothes(2, 3)

print(clothes.get_coat())
print(clothes.get_suit())
print(clothes.get_total)
