# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу:  длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т
class Road:

    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._weight = 25
        self._height = height

    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self._weight * self._height / 1000
        print(f"Площадь асфальтирования: {self._length * self._width / 1000000} кв.км \n"
              f"Масса асфальта толщиной {self._height} см: {round(asphalt_mass)} тонн асфальта")


t = Road(5000, 20, 5)
t.asphalt_mass()
