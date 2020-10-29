""" 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property"""
from abc import ABC, abstractmethod


class Clothes(ABC):

    @property
    @abstractmethod
    def value(self):
        pass

    @staticmethod
    def sum_value(all_coat):
        res = 0
        for clothes in all_coat:
            res += clothes.value
        return res


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def value(self):
        return self.size / 6.5 + 0.5


class Jacket(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def value(self):
        return 2 * self.height + 0.3


coat_1 = Coat(56)
coat_2 = Jacket(2)
sum_coat = [coat_1, coat_2]

print(f"Общий расход ткани: {Clothes.sum_value(sum_coat):.2f}")
