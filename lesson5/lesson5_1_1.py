with open('lesson5_1_1.txt', 'w') as f:
    while True:
        new_str = input('Введите строку для записи в файл (если строка пустая - запись завершится): ')
        if not new_str:
            break
        else:
            f.write(new_str + '\n')
