# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
with open("my_file_3.txt") as file_3:
    print(file_3.read())
with open("my_file_3.txt", 'r') as file_3:
    sum_sal = 0
    count = 0
    l_name = []
    for string in file_3.readlines():
        string = string.split()
        if int(string[1]) < 20000:
            l_name.append(string[0])
        sum_sal += int(string[1])
        count += 1
print(f"Оклад менее 20 тыс.: {' и '.join(l_name)}. Cредний оклад {int(sum_sal / count)} р.")
