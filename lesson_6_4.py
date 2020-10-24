"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.color} автомобиль {self.name} поехал.\n"

    def stop(self):
        return f"Автомобиль {self.name} остановился.\n"

    def turn(self, direction):
        return f"Автомобиль {self.name} повернул {direction}\n"

    def show_speed(self):
        return f"Его скорость {self.speed}\n"


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"Его скорость {self.speed}, выше чем разрешенная 60!\n"
        else:
            return f"Скорость {self.name} в пределах нормы\n"


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"Его скорость {self.speed}, выше чем разрешенная 40!\n"
        else:
            return f"Скорость {self.name} в пределах нормы\n"


class PoliceCar(Car):
    pass


town = TownCar(70, "Синий", "BMW", False)
print(town.go(), town.show_speed(), town.turn("налево"), town.stop(), "Это полиция? " + str(town.is_police))

sport = SportCar(100, "Красный", "KIA", False)
print(sport.go(), sport.show_speed(), sport.turn("направо"), sport.stop(), "Это полиция? " + str(sport.is_police))

work = WorkCar(10, "Белый", "Lada", False)
print(work.go(), work.show_speed(), work.stop(), "Это полиция? " + str(work.is_police))

police = PoliceCar(130, "Зеленый", "Ford", True)
print(police.go(), police.show_speed(), police.turn("направо"), police.stop(), "Это полиция? " + str(police.is_police))
