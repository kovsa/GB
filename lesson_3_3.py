# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def my_func(arg1, arg2, arg3):
    temp = [arg1, arg2, arg3]
    temp.remove(min(arg1, arg2, arg3))
    return sum(temp)


print(my_func(15, 5, 10))
