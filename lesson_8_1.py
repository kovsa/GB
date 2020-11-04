"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
формата «день-месяц-год».  В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных."""


class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []
        for i in day_month_year.split():
            if i != "-":
                my_date.append(i)
                Data.valid(int(i))
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(i):
        if 1 <= i <= 31:
            if 1 <= i <= 12:
                if 1 <= i <= 9999:
                    return f"ok"
                else:
                    print(f'Неправильный год')
            else:
                print(f"Неправильный месяц")
        else:
            print(f"Неправильный день")

    def __str__(self):
        return f"Текущая дата {Data.extract(self.day_month_year)}"


today = Data("32 - 11 - 20001")
print(today)



