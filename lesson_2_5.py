# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
# натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
try:
    digit = int(input("Введите натуральное число, выход (0): "))
    while digit != 0:
        for i in range(len(my_list)):
            if digit < 0:
                print(f"Введите положительное число!")
                break
            if my_list[i] == digit:
                my_list.insert(i + 1, digit)
                break
            elif my_list[0] < digit:
                my_list.insert(0, digit)
            elif my_list[-1] > digit:
                my_list.append(digit)
            elif my_list[i] > digit and my_list[i + 1] < digit:
                my_list.insert(i + 1, digit)
        print(f"текущий список - {my_list}")
        try:
            digit = int(input("Введите натуральное число, выход (0: "))
        except ValueError:
            print("Нужно было ввести число!")
except ValueError:
    print("Нужно было ввести число!!")
