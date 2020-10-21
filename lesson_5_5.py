# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
with open("my_file_5.txt", "w") as file_5:
    string = input("Введите числа через пробел:\n")
    file_5.writelines(string)
with open("my_file_5.txt", 'r') as file_5:
    string = (string.split())
    print(sum(map(int, string)))
