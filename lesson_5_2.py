# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
with open("my_file_2.txt", "r") as file_2:
    print(f"Количество строк: {len(file_2.readlines())}")
with open("my_file_2.txt", "r") as file_2:
    for string in file_2.readlines():
        print(f"Количество слов в строках: {len(string.split())}")
