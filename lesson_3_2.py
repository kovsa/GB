# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
def personal_data(f_name, l_name, year, city, email, tel):
    print(f_name, l_name, year, city, email, tel)


personal_data(f_name="Sergey", l_name="Kovalev", year="1974", city="NN", email="sk@sk.ru", tel="223322")
