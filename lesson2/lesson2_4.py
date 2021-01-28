user_str = input('Введите текст: ')
i = 1

for el in user_str.split():
    print(f'{i}: {el[0:10]}')
    i += 1
