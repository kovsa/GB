# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает
# учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
dict_1 = []
dict_2 = []
with open("my_file_6.txt", "r") as file_6:
    for string in file_6:
        dict_1.append(string.split()[0].strip()[0:-1])
with open("my_file_6.txt", "r") as file_6:
    for line in file_6:
        name_sum = sum(map(int, "".join([i for i in line if i == " " or i.isdigit()]).split()))
        dict_2.append(name_sum)
dict_all = dict(zip(dict_1, dict_2))
print(dict_all)
# ВАРИАНТ2 -------- С одним словарем---------------------
print("\n ВАРИАНТ2 -------- С одним словарем---------------------\n")
dict_3 = []
with open("my_file_6.txt", "r") as file_6:
    for string in file_6:
        name_s = string.split()[0].strip()[0:-1]
        name_sum = sum(map(int, "".join([i for i in string if i == " " or i.isdigit()]).split()))
        print(name_s)
        print(name_sum)
        dict_3[name_s] = name_sum
print(dict_3)

