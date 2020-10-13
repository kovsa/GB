# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().
# ver 1
def int_func():
    word = input("Введите слова: ")
    print(word.title())
    return


int_func()


# ver 2
def int_func2():
    word = input("Введите слова: ").split(' ')
    caps_words = []
    for i in word:
        caps_word = i[0].upper() + i[1:].lower()
        caps_words.append(caps_word)
    res = ' '.join(caps_words)
    print(res)


int_func2()


# ver 3
def int_func3():
    word = input("Введите слова: ").split(' ')
    caps_words = []
    for i in word:
        caps_words.append(i.capitalize())
    res = ' '.join(caps_words)
    print(res)


int_func3()
