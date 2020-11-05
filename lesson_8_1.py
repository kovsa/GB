"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
формата «день-месяц-год».  В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных."""


class Data:
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def extract(cls, date: "Data"):
        return list(map(int, date.day_month_year.split("-")))

    @staticmethod
    def valid(date: "Data"):
        parser = date.day_month_year.split("-")
        if len(parser[2]) not in {2, 4}:
            raise ValueError("Неправильный год")
        if not 1 <= int(parser[1]) <= 12:
            raise ValueError("Неправильный месяц")
        if not 1 <= int(parser[0]) <= 31:
            raise ValueError("Неправильный день")
        print("Введенные данные ок")

    def __str__(self):
        return f"Текущая дата {Data.extract(self.day_month_year)}"


date = Data("31-12-2020")
date.valid(date)
print(Data.extract(date))



