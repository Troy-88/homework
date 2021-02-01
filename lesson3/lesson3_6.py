# первый вариант
def int_func(word):
    return word.title()


# второй вариант(первый показался больно уж простым для 6-го)
def int_func_2(word):
    res = word[0].upper()
    for i in range(1, len(word)):
        res += (word[i].upper() if word[i - 1] == ' ' else word[i])
    return res


user_word = input('Введите слово/текст на латинице: ')
print(int_func(user_word))
print(int_func_2(user_word))
