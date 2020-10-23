# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
import os
with open("my_file_4.txt") as file_4:
    print(f"Чтение оригинального файла\n{file_4.read()}")
rus = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
new_file = []
f = 1
with open("my_file_4.txt") as file_4:
    for i in file_4:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + ' ' + i[1])
        with open("my_file_4_new.txt", "w") as file_4_new:
            file_4_new.writelines(new_file)
        os.rename("my_file_4_new.txt", "my_file_4_new_"+str(f)+".txt")
        new_file = []
        f += 1
