# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def my_func(x, y):
    res = x / y
    print(f"Результат = {res}")


try:
    argv1 = int(input("Введите числитель: "))
    argv2 = int(input("Введите знаменатель: "))
    my_func(argv1, argv2)
except ZeroDivisionError:
    print("Деление на ноль!")
except ValueError:
    print("Введите число!")
