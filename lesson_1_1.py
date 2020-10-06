# less-1
# Поработайте с переменными, создайте несколько, выведите на экран.
last_name = 'Ковалев'
first_name = 'Сергей'
age = 46
print('Меня зовут ', first_name, ' ', last_name, ', мой возраст - ', age, ' лет.', sep='')
# Запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
you_year = int(input('Введите год вашего рождения: '))
now_year = int(input('Введите текущий год: '))
you_last_name = input('Введите вашу Фамилию: ')
you_first_name = input('Введите ваше Имя: ')
print('Вас зовут ', you_first_name, ' ', you_last_name, ', ваш возраст - ', now_year-you_year, sep='')
