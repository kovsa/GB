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


class Clothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height


class MyClass(Clothes):
    def cloth_coat(self):
        print(f"Расход ткани на пальто: {self.size / 6.5 + 0.5:.2f}")

    def cloth_jacket(self):
        print(f"Расход ткани на костюм: {self.height * 2 + 0.3:.2f}")

    def sum_cloth(self):
        print(f"Общий расход затраченной ткани: {(self.size / 6.5 + 0.5 + self.height * 2 + 0.3):.2f}")


mc = MyClass(55, 2)

mc.cloth_coat()
mc.cloth_jacket()
mc.sum_cloth()
