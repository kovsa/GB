# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
user_sec = int(input('Введите время в секундах:'))
h = int(user_sec/3600)
m = int((user_sec-h*3600)/60)
s = user_sec-h*3600 - m*60
print(f'{h:02}', f'{m:02}', f'{s:02}', sep=':')
